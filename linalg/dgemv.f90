subroutine dgemv(trans, m, n, alpha, A, lda, x, incx, beta, y, incy)
! Simplified DGEMV that does
!     y := A*x
! We follow the BLAS signature for compatibility.  For more,
! see http://netlib.org/blas/.
  implicit none
  ! input/output
  character*1, intent(in)         :: trans ! ignore
  integer, intent(in)             :: m, n  ! input sizes 
  integer, intent(in)             :: lda, incx, incy ! ignore
  double precision, intent(in)    :: alpha, beta ! ignore
  double precision, intent(in)    :: A(m, n) ! input matrix
  double precision, intent(in)    :: x(n) ! input vector
  double precision, intent(inout) :: y(m) ! output vector
  ! local
  integer :: i, j
  ! do y = A*x

end subroutine dgemv
