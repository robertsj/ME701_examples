#include <cstdio>
void dgemv(char transa, int m, int n, double alpha,  double *A,  int  lda,  
           double  *x, int incx, double beta, double *y, int incy)
{
  /* Simplified DGEMV that does
       y := A*x
     We follow the BLAS signature for compatibility.  For more,
     see http://netlib.org/blas/ 
  */
 
}
