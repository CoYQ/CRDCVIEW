# coding=utf-8
# !/usr/bin/python
import logging
from socket import *
from time import ctime
import time, thread, string
import pdb
import re


class Client:
    BUFSIZ = 10240

    def __init__(self, host, port, speed, connection):
        self.ADDR = (host, port)
        self.tcp_clisock = socket(AF_INET, SOCK_STREAM)
        self.speed = speed
        self.time_delay = 0
        self.complete = None
        self.resu = None
        self.conn = connection
        self.time_delay_list = []
        self.total_packages = 0
        self.time_regex = '->(\d+)<-'

    def detect_speed_and_timedelay(self):
        self.speed_list = []
        recent_number = 0
        recent_time_delay = 0
        origin_time = time.time()
        start_time = origin_time
        stable_num = 0
        avg_time_delay = 0
        stable_time_delay = 0
        rate = 0
        packet_loss = False
        cur_packages = self.total_packages
        while True:
            data = None
            time_gap = time.time() - start_time
            if time_gap >= 5:
                stable = False
                if time.time() - origin_time > 300:
                    self.tcp_clisock.close()
                    return False
                print "计划发送数目：%s" % self.speed
                real_speed = self.total_packages - cur_packages
                print "实际发送数目:%s" % real_speed
                last_rate = rate
                rate = real_speed / (self.speed * time_gap / 5.0)
                print "总延时率:%f" % rate
                cur_packages = self.total_packages
                print "实际接收数目:%s" % recent_number
                avg_time_delay = recent_time_delay / recent_number
                print '当前时延:%f' % avg_time_delay
                start_time = time.time()
                recent_time_delay = 0.0
                if recent_number < real_speed:
                    print '丢包，降速'
                    self.speed *= 0.95
                    packet_loss = True
                else:
                    if rate >= 1:
                        if packet_loss:
                            stable_num += 1
                            stable = True
                            print '已有丢包，保持速度%s' % self.speed
                        else:
                            if last_rate > 0.99:
                                self.speed += 10
                                stable_num = 0
                                print "增加到%s" % self.speed
                    elif rate < 0.9:
                        self.speed -= 5
                        stable_num = 0
                        print "减少到%s" % self.speed
                    elif rate < 0.85:
                        self.speed -= 10
                        stable_num = 0
                        print "增加到%s" % self.speed
                    else:
                        stable = True

                if stable:
                    if not stable_num:
                        stable_time_delay = 0
                    stable_num += 1
                    print "保持在%s" % self.speed
                    stable_time_delay += avg_time_delay
                    print stable_time_delay
                    print 'stable_num %d' % stable_num
                    if stable_num > 4:
                        self.time_delay = stable_time_delay / stable_num
                        print self.time_delay
                        print "数目稳定为%s,开始检测" % self.speed
                        return True
                recent_number = 0

            try:
                data = self.tcp_clisock.recv(self.BUFSIZ)
            except Exception as e:
                print "receving data error for %s" % str(e).decode('gbk')
                time.sleep(0.1)
            if data:
                send_times = re.findall(self.time_regex, data)
                for send_time in send_times:
                    time_delay = time.time() - float(send_time)
                    recent_number += 1
                    recent_time_delay += time_delay

    def start_flooder(self):
        if self.conn:
            print "开始发动洪泛攻击"
            thread.start_new_thread(self.conn.execute, ("python ./Flooder.py",))
        self.check_speed()

    def check_speed(self):
        print "开始检测洪泛攻击之后的时延"
        self.speed_list = []
        recent_number = 0
        recent_time_delay = 0
        origin_time = time.time()
        start_time = origin_time
        while True:
            data = None
            if time.time() - start_time >= 5:
                if time.time() - origin_time >= 100:
                    break
                cur_time_delay = recent_time_delay / recent_number if recent_number else 1000
                print "当前时延:%s" % cur_time_delay
                self.time_delay_list.append(cur_time_delay)
                start_time = time.time()
                recent_time_delay = 0
                recent_number = 0
            try:
                data = self.tcp_clisock.recv(self.BUFSIZ)
            except Exception as e:
                logging.error(e)
            if data:
                send_times = re.findall(self.time_regex, data)
                for send_time in send_times:
                    time_delay = time.time() - float(send_time)
                    recent_number += 1
                    recent_time_delay += time_delay
        self.judge_tongzhu()

    def judge_tongzhu(self):
        score = 0
        for time_delay in self.time_delay_list:
            if time_delay > self.time_delay * 10:
                score += 5
            elif time_delay > self.time_delay * 5:
                score += 3
            elif time_delay > self.time_delay * 2.5:
                score += 2
            elif time_delay > self.time_delay * 1.2:
                score += 1

        print "score is %d" % score
        if score > len(self.time_delay_list) * 1.5:
            self.resu = True
        else:
            self.resu = False
        self.complete = True

    def process_commucate(self):
        if self.detect_speed_and_timedelay():
            self.start_flooder()

    def send_data(self):
        self.tcp_clisock.connect(self.ADDR)
        data = string.printable * 10
        last_send_time = 0
        while True:
            if time.time() - last_send_time < (5.0 / self.speed):
                continue
            last_send_time = time.time()
            self.total_packages += 1
            self.tcp_clisock.send("->%d<-%s" % (time.time(), data))
        self.tcp_clisock.close()


def main():
    client = Client("218.241.135.34", 4356, 10, None)
    thread.start_new_thread(client.send_data, ())
    thread.start_new_thread(client.process_commucate, ())
    while not client.complete:
        time.sleep(0.5)
        pass
    return client.resu


if __name__ == '__main__':
    main()
