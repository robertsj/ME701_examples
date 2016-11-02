# F2PY demonstration
f2py_demo:
	f2py -c -m $@ utilities.f90

# F2PY demonstration
swig_demo:
	swig -python -c++ utilities.i
	g++ -fPIC -c utilities.cc utilities_wrap.cxx -I/home/robertsj/opt/miniconda/include/python2.7/
	g++ -shared utilities.o utilities_wrap.o -o _utils_cc.so 
