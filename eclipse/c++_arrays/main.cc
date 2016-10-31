#include <vector>
#include <cstdio>
#include <cstdlib>

typedef std::vector<double> vec_dbl;

void linspace(double a, double b, double *x, int n)
{
	for (int i = 0; i < n; ++i)
		x[i] = a + (b-a)/(n-i);
}

void linspace(double a, double b, vec_dbl &x)
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

double sum_of_squares(vec_dbl x)
{
	double s = 0;
	for (int i = 0; i < x.size(); ++i)
		s += x[i]*x[i];
	return s;
}

int main()
{
	int n = 10000000;
	double v[n];
	for (int i = 0; i < 10; ++i)
		v[i] = 1;

	double *x = new double[10];
	double *y;
	y = (double *)malloc(sizeof(double)*n);

	for (int i = 0; i < 10; i++)
	{
		x[i] = 2;
		y[i] = 3;
	}

	double a = 0;
	double b = 0;
	double c = 0;
	//a = sum_of_squares(x, n);

	vec_dbl z(n, 0.0);
	linspace(0, 10., z);

	b = sum_of_squares(z);
	c = sum_of_squares(&z[0], z.size());
	printf("%10.4f, %10.4f, %10.4f\n", a, b, c);

	return 0;
}
