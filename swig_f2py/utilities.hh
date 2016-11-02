#include <vector>
#include <cstdio>
#include <cstdlib>
typedef std::vector<double> vec_dbl;
void linspace(double a, double b, double *z, int n);
void linspaceV(double a, double b, vec_dbl &x);
double sum_of_squares(double *x, int n);
double sum_of_squaresV(vec_dbl x);
