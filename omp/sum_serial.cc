#include <cstdio>
using std::printf;
int main()
{
 const long n = 100000;
 double v[n];
 for (int i = 0; i < n; ++i)
  v[i] = (double)i;
 // do the sum
 double s = 0.0;
 for (int i = 0; i < n; ++i)
   s += v[i];
 double s_ref = 0.5*(n*n - n);
 printf("sum is %f, "
  "expected %f\n", s, s_ref);
}
