#include "utilities.hh"

void linspace(double a, double b, double *z, int n)
{
	for (int i = 0; i < n; ++i)
		z[i] = a + (b-a)/(n-i);
}

void linspaceV(double a, double b, vec_dbl &x)
{
	int n = x.size();
	for (int i = 0; i < n; ++i)
		x[i] = a + (b-a)/(n-i);
}

double sum_of_squares(double *x, int n)
{
	double s = 0;
	for (int i = 0; i < n; ++i)
		s += x[i]*x[i];
	return s;
}

double sum_of_squaresV(vec_dbl x)
{
	double s = 0;
	for (int i = 0; i < x.size(); ++i)
		s += x[i]*x[i];
	return s;
}
