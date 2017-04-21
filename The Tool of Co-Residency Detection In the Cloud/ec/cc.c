#include <stdio.h>
#include <inttypes.h>
#include <stddef.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <fcntl.h>
#include <string.h>
#include <xenctrl.h>
#include <xen/sys/privcmd.h>
#include <xen/event_channel.h>
#include <time.h>
#include <sys/time.h>

#define BIT_1 1
#define BIT_0 0

#define SECOND_LEN 1000000

int64_t PERIOD_LEN = 1000;//microseconds

int64_t this_tick_time, transmission_begin_time = 0;

struct timespec sleeping;
struct timeval lastprint;

int64_t num_of_periods = 0;
int64_t printf_countdown = 1000;

int is_sender = 0;
#define is_receiver (!is_sender)

unsigned int current_chn_open = 0;
evtchn_port_t port, remote_port;
domid_t remote_dom;

inline void mk_privcmd_hcall(void * arg, unsigned int opnum){
    int fd, ret;
    privcmd_hypercall_t hcall = {__HYPERVISOR_event_channel_op ,{opnum, (__u64)arg, 0, 0, 0}};

    if((fd = open("/proc/xen/privcmd", O_RDWR)) < 0){
        perror("open");
        return;
    }

    if((ret = ioctl(fd, IOCTL_PRIVCMD_HYPERCALL, &hcall))){
        return;
    }

    if(close(fd)){
        perror("close");
        return;
    }
}

void chn_creat(){
    int fd, ret;
    struct evtchn_alloc_unbound arg;

    arg.dom = DOMID_SELF;
    arg.remote_dom = remote_dom;

    mk_privcmd_hcall(&arg, EVTCHNOP_alloc_unbound);

    port = arg.port;
}


void chn_connect(){
    int fd, ret;
    struct evtchn_bind_interdomain arg;

    arg.remote_dom = remote_dom;
    arg.remote_port = remote_port;

    mk_privcmd_hcall(&arg, EVTCHNOP_bind_interdomain);

    port = arg.local_port;
}

unsigned int chn_is_open(){
    int fd, ret;
    struct evtchn_status arg;

    arg.dom = DOMID_SELF;
    arg.port = port;

    mk_privcmd_hcall(&arg, EVTCHNOP_status);

    return (arg.status == EVTCHNSTAT_interdomain)?BIT_1:BIT_0;
}

evtchn_port_t chn_remote_port(){
    int fd, ret;
    struct evtchn_status arg;

    arg.dom = DOMID_SELF;
    arg.port = port;

    mk_privcmd_hcall(&arg, EVTCHNOP_status);

    return arg.u.interdomain.port;
}

void chn_close(){
    int fd, ret;
    struct evtchn_close arg;

    arg.port = port;

    mk_privcmd_hcall(&arg, EVTCHNOP_close);
}

inline uint64_t timenow(){
    struct timeval tv;
    gettimeofday(&tv,NULL);
    return tv.tv_sec*(uint64_t)SECOND_LEN+tv.tv_usec;
}

inline void tick(int64_t T){
    this_tick_time = timenow();

    int64_t this_shift, this_period_start_time, this_target, to_sleep;
    this_shift = this_tick_time - transmission_begin_time; this_shift %= T;
    this_period_start_time = this_tick_time - this_shift;
    this_target =  this_period_start_time + T;
    to_sleep = this_target - this_tick_time;

    sleeping.tv_sec = 0;
    sleeping.tv_nsec = to_sleep * 1000;

//    total += this_shift;

    if (nanosleep(&sleeping, NULL)){
        printf("\n"); printf("transmission_begin_time: %ld", transmission_begin_time);
        printf("\n"); printf("this_shift: %ld", this_shift);
        printf("\n"); printf("this_tick_time: %ld", this_tick_time);
        printf("\n"); printf("this_period_start_time: %ld", this_period_start_time);
        printf("\n"); printf("this_target: %ld", this_target);
        printf("\n"); printf("to_sleep: %ld", to_sleep); printf("\n");
    }
}

//int flip = 2000;
//unsigned int pop(){
//	flip--;
//	if(flip>=1000)
//		return BIT_0;
//	else
//		return BIT_1;
//}

#define NUM_FLIP 6
int flip=NUM_FLIP;
unsigned int pop(){//just some dirty codes to output sequence like 11111100000011111 ....
    flip --;
    if(flip < -NUM_FLIP)
        flip = NUM_FLIP;
    return flip>0?BIT_0:BIT_1;
}

inline void to_low(){
    if(chn_is_open())
        chn_close();
}

inline void to_high(){
    if(! )
        chn_connect();
}

void message_loop(){
    unsigned int cbit = 0;
    unsigned int count = 0;
    unsigned int old = 0;

    int m=0;
    while(m<2000){
	m++;

        if(is_sender){
            cbit = pop();
            cbit == 1 ? to_high() : to_low();
        }

        if(is_receiver){
            cbit = chn_is_open();
        }
	
        printf("%d", cbit);
        num_of_periods ++;
        if(num_of_periods%printf_countdown == 0){
            printf("\ncurrent_time: %ld\n", this_tick_time);
        }

	tick(PERIOD_LEN*2);

    }

}

int main(int argc, char* argv[]){
    printf("started\n");

    is_sender = atoi(argv[1]);
    remote_dom = atoi(argv[2]);

    if(argc == 5){
        PERIOD_LEN = atoi(argv[4]);
        printf_countdown = SECOND_LEN/PERIOD_LEN;
    }
    printf("Period: %ld us\n", PERIOD_LEN);

    int64_t tmp =  PERIOD_LEN*3;

    if(is_sender){
        printf("sender\n");
        remote_port = atoi(argv[3]);
        chn_connect();
		tick(tmp);
    }

    if(is_receiver){
        printf("receiver\n");
        chn_creat();
        printf("port:%d\n", port);
        printf("waiting for connection\n");
        while(!chn_is_open());
        remote_port = chn_remote_port();
        printf("connected to %d\n", remote_port);
        tick(tmp);
		tick(PERIOD_LEN);
    }
    message_loop();

    return 0;
}
