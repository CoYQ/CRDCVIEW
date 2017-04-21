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

int is_sender = 0;

unsigned int current_chn_open = 0;

evtchn_port_t port, remote_port;

domid_t remote_dom;

inline void mk_privcmd_hcall(void * arg, unsigned int opnum){
    int fd, ret;
    privcmd_hypercall_t hcall = {__HYPERVISOR_event_channel_op ,{opnum, (__u64)arg, 0, 0, 0}};

    if((fd = open("/proc/xen/privcmd", O_RDWR)) < 0){
        perror("open error:");
        exit(-1);
    }
//    else
//        printf("open /proc/xen/privcmd is ok\r\n");

    if((ret = ioctl(fd, IOCTL_PRIVCMD_HYPERCALL, &hcall))!=0){
        perror("ioctl error:");
		exit(-1);
    }
//    else
//        printf("ioct1 is ok\r\n");

    if(close(fd)){
        perror("close error:");
        exit(-1);
    }
//    else
//        printf("close is ok \r\n");
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
//    print "arg.status"+str(arg.status)
    return (arg.status == EVTCHNSTAT_interdomain)?1:0;
}

void chn_close(){
    int fd, ret;
    struct evtchn_close arg;

    arg.port = port;

    mk_privcmd_hcall(&arg, EVTCHNOP_close);
}

int main(int argc, char* argv[]){

    is_sender = atoi(argv[1]);
    remote_dom = atoi(argv[2]);

    if(is_sender){
        remote_port = atoi(argv[3]);
        chn_connect();
		printf("Yes\n");
    }

    if(!is_sender){
        chn_creat();
        printf("%d\n", port);
		//while(!chn_is_open());
		//printf("Yes\n");
    }
	
    return 0;
}
