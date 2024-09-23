#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include "hw2.c"

int main()
{
	const int SIZE = sizeof(shm_structure);

	const char *name = "OS-acl11930"; // ATTENTION: Change this to 'OS-<your ID>' (eg. OS-abc23450) to avoid conflicts with others

	int	item;
	FILE 	*fp;

	int shm_fd;
	shm_structure *ptr;

	/* create the shared memory segment */
	shm_fd = shm_open(name, O_CREAT | O_RDWR, 0666);

	/* configure the size of the shared memory segment */
	ftruncate(shm_fd,SIZE);

	/* now map the shared memory segment in the address space of the process */
	ptr = mmap(0,SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	if (ptr == MAP_FAILED) {
		printf("Map failed\n");
		return -1;
	}

	/*
	//Writing to shared memory with fixed values


	ptr->buffer[0]=2;
	ptr->buffer[1] = 10;
	ptr->buffer[2] = 0x11223344;
	ptr->in = 3; //(*ptr).in = 3
	*/
	/*****************************************************
	Add your code here.
	Read one item after another from the file 'input.txt'.
	And write it to the shared memory so the consumer can read.
	Need to wait if the buffer is full
	*****************************************************/
	
	fp = fopen("./input.txt", "r");
	int i = 0;
	const int num_elements = 8;
	while(fscanf(fp, "%d", &item) != EOF){
		while(ptr -> buffer[(i+1) % num_elements] != 0);
		ptr -> buffer[(i+1) % num_elements] = item;
		printf("Read %d from the file\n", ++i);
	}
	fclose(fp);
	printf("Success\n");
	return 0;
}
