module utilities

    implicit none

    ! module variable definitions
    double precision, parameter :: PI = 3.141592653589793_8
    integer :: i

contains

    ! module subprogram units (i.e., subroutines and functions)

    subroutine print_i()
        print *, "i = ", i
    end subroutine 

    subroutine linspace(a, b, x, n)
        ! input arguments
        double precision, intent(in) :: a, b
        integer, intent(in) :: n
        double precision, intent(out) :: x(n)
        ! local variables
        integer :: i
        double precision :: dx
        dx = (b-a)/(n-1)
        do i = 1, n
            x(i) = a + dx*(i-1)
        end do
    end subroutine

    double precision function sum_of_squares(x)
        ! input arguments
        double precision, intent(in), dimension(:) :: x
        ! local variables
        integer n, i
        sum_of_squares = 0
        n = size(x)
        do i = 1, n
            sum_of_squares = sum_of_squares + x(i)**2
        end do
    end function sum_of_squares

end module utilities
