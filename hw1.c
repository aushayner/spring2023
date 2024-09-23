#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define BUFFER_SIZE 100

/*------------------------------------------------
Given an maximum number,
this function returns a random number 
in range of 0 ... (maximum-1)
eg) rand_int(100) --> a number in 0 ... 99
------------------------------------------------*/
int rand_int(int maximum)
{	
	// This one needs to be called only once for all calls of rand()
	// But keeping it for the convenience.
	srand(time(NULL));

	return (rand() % maximum);
}


/*------------------------------------------------
Given an integer array with its size,
this function prints the contents in a pretty format 
using curly brackets and commas as shown below
eg) {1, 10, -5, 3, 7, 102, 110} 
------------------------------------------------*/
void print_int_array(int *p, int size)
{
	int i;

	printf("{");

	if(size > 0) printf("%i", *(p));
	

	for(i = 1; i < size; i++){
		printf(", %i", *(p+i));
	}

	printf("}\n");
}

/*------------------------------------------------
Given an integer,
this function returns 1 if it is a prime number
and returns 0 if it is not.
It does not have to be an efficent algorithm.
But it would be good to think about it. 
------------------------------------------------*/
int is_prime(int a)
{
	int i = 0;

	if(a == 0||a == 1) return 0;

	for(i = 2; i < (a/2)+1; i++){
		if (a % i == 0) return 0;
	}


	return 1;
}

/*------------------------------------------------
Given a buffer and an integer,
this function fills the buffer with prime numbers 
that are less than the integer n and returns the number of prime numbers.
eg) cnt = generate_prime_numbers(buff,20)
--> buffer = {2,3,5,7,11,13,17,19,...}
    cnt = 8
* Using is_prime() function defined above will make this function easier.
------------------------------------------------*/
int generate_prime_numbers(int *p, int n)
{
// You can access individual position of the buffer using index. eg) p[0], p[1],...
	int i;
	int x = 0;
	for(i = 0; i < n; i++){

		do{
			x++; 
		}while(!(is_prime(x)));

		*(p+i) = x;
	}	
	
	return n; //value of cnt should be greater than 0?
	//return 0;
}



/* Please keep this main() as the last part of the file */
int main()
{
	int numbers[] = {1, 10, -5, 3, 7, 102, 110};
	int buff[BUFFER_SIZE];

	print_int_array(numbers, 7);

	// Followings are example codes to test the functions.
	// Get them out of comment when testing your functions.

	int n = rand_int(1000);
	n = 613;
	//n = 2;
	if (is_prime(n))
		printf("%d is a prime number\n", n);
	else
		printf("%d is NOT a prime number\n", n);

	// test for generate_prime_number()
	int cnt = generate_prime_numbers(buff, 20);
	print_int_array(buff, cnt);
	//print_int_array(buff, BUFFER_SIZE);

}