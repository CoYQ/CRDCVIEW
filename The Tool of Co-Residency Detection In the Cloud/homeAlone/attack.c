#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>
#include <string.h>
#include <fcntl.h>
#include <zlib.h>
#include <sys/mman.h>
#define PAGE_SIZE 4096
#define PAGE_MASK (~(PAGE_SIZE-1))
int main(int argc, char* argv[]){
     char *file_path = argv[1];
//     printf("%s\n", argv[1]);
     int group = atoi(argv[2]);
     char *serviceName = argv[3];
     int nPageNum = 200;
     int nBufSize = nPageNum * PAGE_SIZE;
     
     /* 建立文件,存储测试数据用 */
     FILE *fp;
     // 这个路径记住重设
     fp= fopen("./detect/result_data.txt", "at");
     if(fp == NULL){
          printf("file open error");
          return -1;
     }
     
     /* 动态分配以页为边界的堆内存 */
     char *buf;
     int nRet = 0;
     nRet = posix_memalign(&buf, PAGE_SIZE, nBufSize);
     if(nRet){
          printf("memory allocation error\n");
          return -1;
     }
     if(!buf){
          printf("memory allocation failed\n");
          return -1;
     }
     
     /* 加载 firefox 到动态分配的堆内存*/
     int number = 0, size = 0;
     gzFile zip;
     // "/usr/lib/firefox/libnss3.so"
     zip = gzopen(file_path,"rb");
     number = gzread(zip, buf, nBufSize);
     if(number==0){
          printf("file read error\n");
          return -1;
     }
     buf = (char *)((unsigned long)buf & PAGE_MASK);  //buf为内存页的页号

     /*允许 buf 指针所指向的内存区域可融合*/
     size = madvise(buf, size, MADV_MERGEABLE);
     if(size == -1){
          printf("%d madvise failed\n", __LINE__);
          return -1;
     }

     /* 睡眠3分钟,此时内存融合机制工作,合并相同内容的内存页*/
     //printf("waitting 10 minutrs\n");
     sleep(2);
     
     //buf
     double timeuse = 0;
     struct timeval start, end;
     int gettimeofday(struct timeval *tv, struct timezone *tz);

     /* 记录当前时间*/
     gettimeofday(&start, NULL);

     /* 对所分配内存页写访问,触发写时复制*/
     memset(buf, 1, strlen(buf));

     /* 写访问完成后,记录当前时间*/
     gettimeofday(&end, NULL);

     /*计算出写时复制的时间*/
     timeuse = 1000000 * ((double)end.tv_sec -(double)start.tv_sec) + (double)end.tv_usec - (double)start.tv_usec;
     printf("The %s-%d group used: %lf ms.", serviceName, group, timeuse);
     fprintf(fp,"%s\t%d\t%lf\n", serviceName, group, timeuse);
     gzclose(zip);
     free(buf);
     fclose(fp);
     return 0;
}
