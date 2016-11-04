#include <cstdio>

void dgemv(char transa, int m, int n, double alpha,  double *A,  int  lda,  
           double  *x, int incx, double beta, double *y, int incy);

int main()
{
  char transa = 'n';
  double alpha = 1.0, beta = 0.0;  
  int incx = 1, incy = 1;

  int m = 9;
  int lda = m;
  int n = 9;
  double A[m*n];
  double x[n];
  double y[m];

  for (int i = 0; i < m; ++i)
  {
    x[i] = 1.0;
    for (int j = 0; j < n; ++j)
    {
      A[i*n+j] = i + 2*j;
    }
  }

  dgemv(transa, m, n, alpha, A, lda, x, incx, beta, y, incy);
  
  for (int i = 0; i < m; ++i) 
    printf("%10.5f\n", y[i]);

  return 0;
}
