#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/shm.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include "hw2.c"

int main()
{
	const char *name = "OS-acl11930"; // ATTENTION: Change this to the same name you used in producer.c
	const int SIZE = sizeof(shm_structure);

	int shm_fd;
	shm_structure *ptr;
	int i;
	int item;

	/* open the shared memory segment */
	shm_fd = shm_open(name, O_RDWR, 0666);
	if (shm_fd == -1) {
		printf("shared memory failed\n");
		exit(-1);
	}

	/* now map the shared memory segment in the address space of the process */
	ptr = mmap(0,SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
	if (ptr == MAP_FAILED) {
		printf("Map failed\n");
		exit(-1);
	}

	/***************************************************
	Add your code for consumer here.
	Read an item after another from the shared memory
	And display to screen using printf().
	Need to wait if the buffer is empty.
	Check if this displays all the items in 'input.txt' 
	except end-of-message signal '-1'
	***************************************************/

	const int num_elements = 8;
	i = 0;

	while(item != -1){
		while(ptr -> buffer[(i+1) % num_elements] ==0);

		item = ptr -> buffer[(i + 1) % num_elements];
		ptr -> buffer[(i + 1) & num_elements] = 0;
		printf("item = %d\n", item);
		i++;
	}
	
	/* remove the shared memory segment */
	if (shm_unlink(name) == -1) {
		printf("Error removing %s\n",name);
		exit(-1);
	}

	return 0;
}
