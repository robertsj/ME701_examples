// The syntax is %module module_name, i.e., the name
// you want to import.  All of the C++ includes you need
// should be included here.
%module utils_cc
%{
#include "utilities.hh"
%}

// OPTION 1 (see the SWIG documentation)
%include std_vector.i
namespace std
{
%template(vec_dbl) vector<double>;
}
 


// OPTION 2 (inspired by http://wiki.scipy.org/Cookbook/SWIG_NumPy_examples)
%{
#define SWIG_FILE_WITH_INIT
%}
%include "numpy.i"
%init %{
  import_array();
%}
%apply (double* ARGOUT_ARRAY1,  int DIM1) {(double *z, int n)}
%apply (double* INPLACE_ARRAY1, int DIM1) {(double *x, int n)}
 

// INCLUDE THE HEADER FILE WITH THE ACTUAL DECLARATIONS
%include "utilities.hh"
