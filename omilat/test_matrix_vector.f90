! Driver program to test matrix-vector multiplication
program test_matrix_vector
  implicit none
  double precision, allocatable :: A(:, :)
  double precision, allocatable :: x(:), y(:)
  double precision :: alpha = 1.0, beta = 0.0, t, t2, omp_get_wtime, flops
  integer :: n, m, lda, incx = 1, incy = 1, i, j, maxi
  do j = 1, 50
    ! Matrix size
    m   = 16 * j
    n   = m
    lda = m
    ! Create the matrix and vector
    allocate(A(m, n), x(n), y(n))
    ! Initialize A and x
    A = 1.0
    x = 1.0
    ! Start the timer.
    t = omp_get_wtime()
    ! Loop over and apply A several times for consistent timing
    maxi = 200
    do i = 1, maxi
      ! Reset
      y = 0.0
      call dgemv('n', m, n, alpha, A, lda, x, incx, beta, y, incy)
    end do
    t2 = omp_get_wtime()-t
    ! we should subtract m for our own implementation, since
    ! we don't do y = Ax-y, just y = Ax
    flops = (2*m*m-m)*maxi 
    ! print out mflops
    print *, m,  flops / dble(1e6) / t2
    deallocate(A, x, y)
  end do
end program test_matrix_vector
