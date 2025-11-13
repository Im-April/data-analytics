# -*- coding: utf-8 -*-

# 표준 데이터 타입
np.zeros(20, dtype=int)
np.ones((3,3),dtype=bool)
np.full((3,3),1.0,dtype=float)

# 날짜/시간 배열 생성
date = np.array('2020-01-01',dtype=np.datetime64)
date

datetime = np.datetime64('2020-01-01 12:00')
datetime
np.datetime64('2020-01-01 12:00:12.34','ns')