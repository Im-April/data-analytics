# -*- coding: utf-8 -*-

import numpy as np

# 배열 만들기
a1 = np.array([1,2,3,4,5])
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
a3 = np.array([[[1,2,3],[4,5,6],[7,8,9]],
      [[1,2,3],[4,5,6,],[7,8,9]],
      [[1,2,3],[4,5,6],[7,8,9]]])

# 배열 조회

# 배열 속성 정보
def array_info(array) :
  # 배열 자체를 출력
  print(array)

  print(f'배열의 차원 수 : {array.ndim}')
  print(f'배열의 형태 : {array.shape}')
  print(f'배열의 데이터 타입 : {array.dtype}')
  print(f'배열에 포함된 천체 원소 개수 : {array.size}')
  print(f'각 원소의 바이트 크기 : {array.itemsize}')
  print(f'배열 전체가 차지하는 메모리 바이트 수 : {array.nbytes}')
  print(f'다음 원소로 이동하기 위해 건너뛰는 바이트 수 : {array.strides}')
  print()


array_info(a1)
array_info(a2)
array_info(a3)