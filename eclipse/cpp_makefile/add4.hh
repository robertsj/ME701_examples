// function declarations
#ifndef FUNCTIONS2_HH_
#define FUNCTIONS2_HH_

#include "add2.hh"

#include <cstdio>


// Why is "inline" needed?
int add4(int a, int b, int c, int d)
{
  printf("add 4 ints\n");
  return add2(a, b) + add2(a, c);
}

int add4(double a, double b, double c, double d)
{
  printf("add 4 doubles\n");
  return add2(a, b) + add2(a, c);
}

#endif /* FUNCTIONS_HH2_ */
