// Definitions for shared memory structure
#define BUFFER_SIZE 10
typedef struct{
	int buffer[BUFFER_SIZE];
	int in;
	int out;
} shm_structure;

#include <time.h>

char time_str[100];
char *get_time()
{
	
	time_t t=time(NULL);	// get time info (month, day, hour, min)
	struct tm *tm1 = localtime(&t); // convert to easy format

	struct timeval tv;
	struct tm *tm;
	gettimeofday(&tv, NULL); 	// get time info (month, day, hour, min)
	tm=localtime(&tv.tv_sec);	// convert to easy format

	sprintf(time_str,"(%02d/%02d %d:%d:%d %d)", tm1->tm_mon+1,tm1->tm_mday,tm->tm_hour,tm->tm_min,tm->tm_sec, tv.tv_usec);
	return time_str;
}

