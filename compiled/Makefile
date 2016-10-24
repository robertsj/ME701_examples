slides :
	pdflatex cpp_fortran.tex
	pdflatex cpp_fortran.tex

hello_world :
	g++ hello_world.cc -o hello_world_cc
	gfortran hello_world.f90 -o hello_world_f90

declaring :
	g++ declaring.cc -o declaring_cc
	gfortran declaring.f90 -o declaring_f90

simple_math :
	g++ simple_math.cc -o simple_math_cc
	gfortran simple_math.f90 -o simple_math_f90

control_if :
	g++ control_if.cc -o control_if_cc
	gfortran control_if.f90 -o control_if_f90

control_case :
	g++ control_case.cc -o control_case_cc
	gfortran control_case.f90 -o control_case_f90

loops :
	g++ loops.cc -o loops_cc
	gfortran loops.f90 -o loops_f90

functions :
	g++ functions.cc -o functions_cc
	gfortran functions.f90 -o functions_f90

command_line :
	g++ command_line.cc -o command_line_cc
	gfortran command_line.f90 -o command_line_f90

file_io :
	g++ file_io.cc -o file_io_cc
	gfortran file_io.f90 -o file_io_f90

all : hello_world declaring simple_math control_if control_case loops \
      functions command_line file_io

clean :
	rm cpp_fortran.log cpp_fortran.aux cpp_fortran.pdf cpp_fortran.toc \
     cpp_fortran.snm  cpp_fortran.nav cpp_fortran.out \
     hello_world_cc hello_world_f90 declaring_cc declaring_f90 \
     simple_math_cc simple_math_f90 \
     control_if_cc control_if_f90 control_case_cc control_case_f90 \
     loops_cc loops_f90 functions_cc functions_f90 \
     command_line_cc command_line_f90 file_io_cc file_io_f90
