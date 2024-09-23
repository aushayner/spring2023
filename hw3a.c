#include <stdio.h>
#include <sys/time.h>
#include <pthread.h>

#define THREAD_NUM 8
#define BUFFER_SIZE 4000000
int countPrime=0; 
int numbers[BUFFER_SIZE];

int isPrime(int n)
{
	int i;
	for(i=2;i<n;i++)
		if (n%i==0)
			return 0;
	return 1;
}

void *primeWorker(void *param){
	int *args = (int*)param;
	int start = *(args);
	int end = *(args+1);

	int i;
	for(i = start; i < end; i++){
		if(isPrime(numbers[i])){
			countPrime++;
		}
	}

}


int main()
{
	pthread_t tid[THREAD_NUM];
	pthread_attr_t attr;

	int i;

	pthread_attr_init(&attr);
	// fill the buffer
	for(i=0;i<BUFFER_SIZE;i++){
		numbers[i] = (i+100)%100000;
	}

	int segmentSize = BUFFER_SIZE / THREAD_NUM;
	int lowHigh[] = {0, 0};
	for(i = 0; i < THREAD_NUM; i++){
		lowHigh[0] = i * segmentSize;
		lowHigh[1] = (i + 1) * segmentSize;
		pthread_create(&tid[i], &attr, primeWorker, &lowHigh);
	}

	for(i=0;i<THREAD_NUM;i++){
		pthread_join(tid[i],NULL);
	}
	



	// Computation
	/*
	for(i=0;i<BUFFER_SIZE;i++)
		if (isPrime(numbers[i]))
			countPrime++;
	*/
	printf("count of prime numbers = %d\n",countPrime);
}
