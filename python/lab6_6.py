"""
챕터: day6
주제: 정규식
문제: compile, match, serach 기초 연습
작성자: 김은정
작성일: 2018.11.15
"""

import re #regular expression 모듈을 수입
r = re.compile('p.') #re 모듈의 compile을 호출, 'p.'을 찾고 싶음. 해당 문자열을 찾을 때 사용하는 regular
                    #expression 객체가 반환됨. .은 임의의 한 문자를 의미
print(r.search("pizza")) # r.search()는 'pizza' 문자열에서 'p.'에 매칭되는 부분에 대한 정보가 반환됨.
print(r.match("pizza")) # r.match()는 'pizza' 문자열에서 맨 앞에 'p.'에 매칭되는 부분에 대한 정보가 반환됨.

r = re.compile('[z]') #re 모듈의 compile을 호출, a,e,i,o,u 중 하나를 찾고 싶음. 해당 문자열을 찾을 때 사용하는 regular
                    #expression 객체가 반환됨. []안에 찾고 싶은 문자를 열거
print(r.search("pizza")) # r.search()는 'pizza' 문자열에서 '[z]'안에 처음으로 매칭되는 글자에 대한 정보가 반환됨.
print(r.match("pizza",2)) # r.search()는 'pizza' 문자열에서 맨 앞에 'p.'에 매칭되는 부분에 대한 정보가 반환됨.