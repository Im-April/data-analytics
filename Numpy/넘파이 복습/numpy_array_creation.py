# -*- coding: utf-8 -*-

import numpy as np

# 배열 만들기
a1 = np.array([1,2,3,4,5])
print(a1)
print(f'a1의 타입 : {type(a1)}')
print(f'a1의 형태 : {a1.shape}')
print(f'a1의 0번째 인덱스 : {a1[0]}')
print(f'a1의 1번째 인덱스 : {a1[1]}')
print(f'a1의 2번째 인덱스 : {a1[2]}')
print(f'a1의 3번째 인덱스 : {a1[3]}')
print(f'a1의 4번째 인덱스 : {a1[4]}')

a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2)
print(f'a2의 형태 : {a2.shape}')
print(f'a2[0,0] : {a2[0,0]}')
print(f'a2[1,1] : {a2[1,1]}')
print(f'a2[2,2] : {a2[2,2]}')

a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
      [[1,2,3],[4,5,6,],[7,8,9]],
      [[1,2,3],[4,5,6],[7,8,9]]])

print(a3)
print(a3.shape)