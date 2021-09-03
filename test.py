import mod1
# import는 현재 디렉터리에 있는 파일이나 파이썬 라이브러리가 저장된 디렉터리에 있는 모듈만 불러올 수 있다.
# 파이썬 라이브러리는 파이썬을 설치할 때 자동으로 설치되는 파이썬 모듈을 말한다.
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

from mod1 import add
print(add(3, 4))

from mod1 import add, sub
print(add(3, 4))
print(sub(4, 2))

from mod1 import *
print(add(3, 4))
print(sub(4, 2))

import mod1
print(mod1.__name__)

import mod2
result = mod2.add(3, 4)