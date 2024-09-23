#include <stdio.h>
#include <stdlib.h>
#include "hw2.c"

int main()
{
	int	item;
	FILE 	*fp;

	fp = fopen("input.txt","r");
	while(fscanf(fp, "%d",&item)!= EOF){
		printf("%s Read %d from the file\n",get_time(),item);
	}
	fclose(fp);
}


