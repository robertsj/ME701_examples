program test_dgemv
  implicit none
  double precision, allocatable :: A(:, :)
  double precision, allocatable :: x(:), y(:)
  double precision :: alpha = 1.0, beta = 0.0  
  integer :: n, m, lda, incx = 1, incy = 1, i, j 
  character*1 :: trans = 'n'
  m   = 9
  n   = 9
  lda = m
  ! Create the matrix and vector
  allocate(A(m, n), x(n), y(n))
  ! Initialize A and x
  do i = 1, m
    do j = 1, n
      A(i, j) = i + 2.0*j
    end do
  end do
  x = 1.0
  y = 0.0
  call dgemv('n', m, n, alpha, A, lda, x, incx, beta, y, incy)
  print '(3f10.5)', y
  deallocate(A, x, y)
end program test_dgemv
