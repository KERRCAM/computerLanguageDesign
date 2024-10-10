#include <stdio.h>
#include <string.h>
#include "headers/lexer.h"


int main(){

    FILE* fptr;
    fptr = fopen("../TestFiles/test1.txt", "r");
    printf("%s", fptr);

    return 0;
}