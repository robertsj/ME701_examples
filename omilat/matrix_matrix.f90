subroutine dgemm(transa, transb, m, n, k, alpha, A, lda, B, ldb, beta, C, ldc)
! Simplified DGEMM that does
!     C := A*B
! We follow the BLAS signature for compatibility.  For more,
! see http://netlib.org/blas/.
  implicit none
  ! input/output
  character*1, intent(in)         :: transa, transb
  integer, intent(in)             :: m, n, k, lda, ldb, ldc
  double precision, intent(in)    :: alpha, beta
  double precision, intent(in)    :: A(m, n), B(n, k)
  double precision, intent(inout) :: C(m, k)
  ! local
  integer :: i, j, l
  ! do C = A*B
  do l = 1, n
    do j = 1, n
      do i = 1, n
        C(i, l) = C(i, l) + A(i, j) * B(j, l)
      end do
    end do
  end do
end subroutine dgemm
