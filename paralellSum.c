#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>

#define THREAD_NUM 8
int sum = 0;

//format for paralell function
void *run(void *param){
    int i;
    int maxn = atoi(param);
    for(i = 0; i < maxn; i++){
        sum = sum + 1;
    }
    printf("I am a child thread. Done.\n");
}
int main(int argc, char * argv[]){
    pthread_t tid[4]; //output
    pthread_attr_t attr; //input

    pthread_attr_init(&attr); // input
    int i;
    for (i = 0; i < THREAD_NUM; i++){
        pthread_create(&tid[i], &attr, run, argv[1]);
    }
    /*
    pthread_create(&tid, &attr, run, NULL);
    pthread_create(&tid2, &attr, run, NULL);

    pthread_join(tid, NULL); // blocking until child is done
    pthread_join(tid2, NULL);
    */
    
    for(i = 0; i < THREAD_NUM; i++){
        pthread_join(tid[i], NULL);
    }
    
    printf("Sum = %d.\n", sum);

    return 1;
}
