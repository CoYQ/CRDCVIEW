# coding=utf-8
__author__ = 'CK'

import os
import paramiko
import subprocess


class Connection(object):
    """连接到指定host的连接类"""

    def __init__(self, host, username=None, private_key=None, passwd=None, port=None):
        self._sftp = None
        self._sftp_live = False

        if not username:
            username = 'ubuntu'
        if not port:
            port =22
        print host
        print port
        self._transport = paramiko.Transport((host, port))
        self._transport_live = True
        #print 'ok4'
        if passwd:
            self._transport.connect(username=username, password=passwd)
        else:
            if not private_key:
                raise TypeError, "You have not specified a password or key."
            private_key_file = os.path.expanduser(private_key)
            rsa_key = paramiko.RSAKey.from_private_key_file(private_key_file)
            self._transport.connect(username=username, pkey=rsa_key)
            #print 'ok5'

    def _sftp_connect(self):
        """建立SFTP连接"""
        if not self._sftp_live:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)
            self._sftp_live = True

    def get(self, remotepath, localpath=None):
        """从服务器下载文件"""
        if not localpath:
            localpath = os.path.split(remotepath)[1]
        self._sftp_connect()
        self._sftp.get(remotepath, localpath)

    def put(self, localpath, remotepath=None):
        """向服务器上传文件"""
        if not remotepath:
            remotepath = os.path.split(localpath)[1]
            # print remotepath
        self._sftp_connect()
        self._sftp.put(localpath, remotepath)

    def execute(self, command):
        """执行单条命令"""
        channel = self._transport.open_session()
        channel.exec_command(command)
        output = channel.makefile('rb', -1).readlines()
        if output:
            return output
        else:
            return channel.makefile_stderr('rb', -1).readlines()

    def execute2(self, command):
        """执行单条长命令"""
        channel = self._transport.open_session()
        channel.exec_command(command)
        a = channel.makefile('rb', -1).readline()
        while True:
            print a
            a = channel.makefile('rb', -1).readline()

    def close(self):
        """关闭连接"""
        if self._sftp_live:
            self._sftp.close()
            self._sftp_live = False
        if self._transport_live:
            self._transport.close()
            self._transport_live = False

    def __del__(self):
        self.close()

    # popen = subprocess.Popen(['ping', 'www.baidu.com', '-n', '3'], stdout=subprocess.PIPE)


