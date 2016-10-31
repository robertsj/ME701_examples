program fortran_arrays

    ! use is like include in c/c++ and import in python
    use utilities

    implicit none

    ! declarations
    integer :: i
    integer, parameter :: n = 10
    double precision :: v(10), x(n), a, b, c
    double precision, allocatable, dimension(:) :: y, z

    ! set v to 1's
    do i = 1, 10
        v(i) = 1.0
    end do

    ! set x to 2
    x = 2.0  ! easy, no?

    ! allocate y and z
    allocate(y(n), z(n))

    y = 3

    do i = 1, n+1
        z(i) = i
    end do

    a = sum(v)
    b = sum_of_squares(x)
    c = product(y)

    call linspace(0.0_8, 10.0_8, z, n)

    print *, "a, b, and c = "
    print 101, a, b, c

    print *, "z = "
    print '(3f10.5)', z

101 format(f10.5," ",e9.2," ",es9.2)

end program fortran_arrays
