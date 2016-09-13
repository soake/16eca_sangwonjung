# -*- coding: utf8 -*-
""""
Simple demo of the fill function.
"""

# "line_bars_and_markers example code: fill_demo.py," Matplotlib 1.5.0 documentation. [online]. Available:
#  https://matplotlib.org/1.5.0/examples/lines_bars_and_markers/fill_demo.html. [Acessed: 21-aug-2016].

# 각 문자열을 화면에 표시
# 배열, 행렬 관련 기능을 담고 있는 numpy 모듈을 불러 들임
# 관련 기능은 np. 으로 시작함
import numpy as np

#그래프 관련 기능을 담고 있는 matplotlib 모듈을 plt 라는 이름으로 불러줌
# 관련기능은 plt. 으로 시작함
import matplotlib.pyplot as plt

#data 준비 시작
# x data 생성 : 0 부터 1 사이를 500구간으로 나눔
x = np.linspace(0, 1, 500)
# y data 생성 : exp() 함수와 sin() 함수의 곱으로 생성
# x와 같은 수의 data를 생성함
# >>> print len(X)
# >>> print len(y)
# 위 두 결과가 같을 것임
y = np.sin(10 * 2 * np.pi * x) * np.exp(-5 * x)
# data 준비 끝

#그래프 준비 시작
#그래프를 그리고 x 축과의 사이를 'r'에 따라 빨간색으로 칠함
plt.fill(x, y, 'r')
#모눈 생성
plt.grid(True)
#그래프 준비 끝

#그래프를 화면에 표시
plt.show()
