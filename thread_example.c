#include <pthread.h>
#include <stdio.h>
#include <stdio.h>

#define THREAD_NUM 8
int sum = 0;
void *thfun(void *param){
	int idx = (int)param;
	printf("This is a child process %d\n", idx);
	int i;
	for(i=0;i<1000000;i++)
		sum += 1;
}
int main()
{
	pthread_t tid[THREAD_NUM];
	pthread_attr_t attr;
	int i;

	pthread_attr_init(&attr);
	for(i=0;i<THREAD_NUM;i++)
		pthread_create(&tid[i], &attr, thfun, i);

	for(i=0;i<THREAD_NUM;i++)
		pthread_join(tid[i],NULL);
	printf("The sum = %d\n", sum);
}
