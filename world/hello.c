#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // get the user's name
    string name = get_string("What's your name?\n");

    // output the names hello IN LOWERCASE
    printf("hello, %s\n", name);
}
