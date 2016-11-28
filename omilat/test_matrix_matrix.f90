! Driver program to test matrix-vector multiplication
program test_matrix_vector
  implicit none
  double precision, allocatable :: A(:, :), B(:, :), C(:, :)
  double precision :: alpha = 1.0, beta = 0.0, t, t2, omp_get_wtime, flops
  integer :: n, m, k, lda, ldb, ldc, i, j, maxi
  do j = 1, 50
    ! Matrix size
    m   = 16 * j
    n   = m
    k   = m
    lda = m
    ldb = m
    ldc = m
    ! Create the matrix and vector
    allocate(A(m, m), B(m, m), C(m, m))
    ! Initialize A and x
    A = 1.0
    B = 1.0
    ! Start the timer.
    t = omp_get_wtime()
    ! Loop over and apply A several times for consistent timing
    maxi = 10
    do i = 1, maxi
      ! Reset
      C = 0.0
      call dgemm('n', 'n', m, n, k, alpha, A, lda, B, ldb, beta, C, ldc)
    end do
    t2 = omp_get_wtime()-t
    ! we should subtract m for our own implementation, since
    ! we don't do y = Ax-y, just y = Ax
    flops = 2.0*dble(m)**3*maxi 
    print *, m,  flops / dble(1e6) / t2
    deallocate(A, B, C)
  end do
end program test_matrix_vector
