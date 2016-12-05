# Makefile for linear algebra tests 

#===============================================================================
# User Options
#===============================================================================

COMPILER = gfortran
OPTIMIZE = yes
DEBUG = yes

#===============================================================================
# Vendor BLAS implementations
#===============================================================================

# For linking MKL, see:
#   http://software.intel.com/en-us/articles/intel-mkl-link-line-advisor/
MKLDIR=/home/robertsj/opt/miniconda/lib/
LIBMKLSERIAL   = -L${MKLDIR} -Wl,--no-as-needed -lmkl_intel_lp64 \
                 -lmkl_sequential -lmkl_core -lpthread -lm -ldl
LIBMKLOPENMP   = -L${MKLDIR} -Wl,--no-as-needed -lmkl_intel_lp64 \
                 -lmkl_intel_thread -lmkl_core -liomp5 -lpthread -lm -ldl

# BLAS defines a generic set of functions with vendor-specific
# implementations; here, we use the blas implementation from the 
# software repository.
LIBBLAS        = -L/usr/lib -lblas

#===============================================================================
# Compiler Definitions
#===============================================================================

ifeq ($(COMPILER),gfortran)
  F90 = gfortran
  OMPFLAG = -fopenmp
  ifeq ($(OPTIMIZE),yes)
    OPT = -O3
  endif
endif

ifeq ($(COMPILER),ifort)
  F90 = ifort
  OMPFLAG = -openmp
  ifeq ($(OPTIMIZE),yes)
    OPT = -O3
  endif
endif

#===============================================================================
# Targets
#===============================================================================

all: driver-mv-row-x driver-mv-col-x driver-mv-blas-x driver-mv-mkl-x \
     driver-mm-x driver-mm-blas-x driver-mm-mkl-x

#===============================================================================
# Matrix-Vector Tests
#===============================================================================

# Row-major MV test
driver-mv-row-x:
	$(F90) $(OPT) $(OMPFLAG) matrix_vector_rm.f90 test_matrix_vector.f90 -o $@ 

# Column-major MV test
driver-mv-col-x:
	$(F90) $(OPT) $(OMPFLAG) matrix_vector_cm.f90 test_matrix_vector.f90 -o $@ 

# Use the repository's BLAS implementation
driver-mv-blas-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_vector.f90 -o $@ $(LIBBLAS)

# Use MKL as distributed in miniconda2
driver-mv-mkl-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_vector.f90 -o $@ $(LIBMKLSERIAL)

# Use MKL as distributed in miniconda2
driver-mv-mkl-omp-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_vector.f90 -o $@ $(LIBMKLOPENMP)

###

# Naive MM
driver-mm-x:
	$(F90) $(OPT) $(OMPFLAG) matrix_matrix.f90 test_matrix_matrix.f90 -o $@ 

# Use MKL as distributed in miniconda2
driver-mm-blas-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_matrix.f90 -o $@ $(LIBBLAS)

# Use MKL as distributed in miniconda2
driver-mm-mkl-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_matrix.f90 -o $@ $(LIBMKLSERIAL)

# Use MKL as distributed in miniconda2 with threading
driver-mm-mkl-omp-x:
	$(F90) $(OPT) $(OMPFLAG) test_matrix_matrix.f90 -o $@ $(LIBMKLOPENMP)

# Remove objects, module files, and exectables
clean:
	@rm -f *.o *.mod *-x

# Same, but leave the executable
neat:
	@rm -f *.o *.mod

#===============================================================================
# Rules
#===============================================================================

.SUFFIXES: .F90 .o
.PHONY: clean neat

%.o: %.f90
	$(F90) $(F90FLAGS) $(INCLUDE) -c $<
