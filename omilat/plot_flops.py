import matplotlib.pyplot as plt
import numpy as np

x, mv_row = np.loadtxt('mv-row.txt', unpack=True)
x, mv_col = np.loadtxt('mv-col.txt', unpack=True)
x, mv_blas = np.loadtxt('mv-blas.txt', unpack=True)
x, mv_mkl = np.loadtxt('mv-mkl.txt', unpack=True)

plt.figure(1)
plt.plot(x, mv_row, x, mv_col, x, mv_blas, x, mv_mkl)
plt.xlabel('size')
plt.ylabel('MFLOP/s')

x, mm = np.loadtxt('mm.txt', unpack=True)
x, mm_blas = np.loadtxt('mm-blas.txt', unpack=True)
x, mm_mkl = np.loadtxt('mm-mkl.txt', unpack=True)

plt.figure(2)
plt.plot(x, mm, x, mm_blas, x, mm_mkl)
plt.xlabel('size')
plt.ylabel('MFLOP/s')

plt.show()



