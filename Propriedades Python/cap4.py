import numpy as np

# CRIANDO UM NUMPY ARRAY
# ndarray 1 dimensao
arr = np.array([1, 2, 3])
print('nparray 1 dimensao: ', arr, '\n')

# ndarray 2 dimensoes
mtz = np.array([[1, 2], [3, 4]])
print('nparray 2 dimensoes: ', mtz, '\n')



# FUNCOES PARA ESTRUTURACAO DE NUMPY ARRAY
# zeros
ar1 = np.zeros(6)
print(ar1, '\n')

# ones com reshape (redimensionando o array)
mtz1 = np.ones(9).reshape(3, 3)
print(mtz1, '\n')

# arange
ar2 = np.arange(1, 11, 1)
print(ar2, '\n')


# COMO CONCATENAR UM NUMPY ARRAY
arr1 = np.arange(1, 5, 1)
arr2 = np.arange(5, 9, 1)

print(np.concatenate([arr1, arr2]))


# EXTRAINDO PROPRIEDADES DE UM NUMPY ARRAY
mtz2 = np.arange(1, 13, 1).reshape(3, 4)

print(mtz2.size)
print(mtz2.ndim)  # numero de dimensoes
print(mtz2.shape)

