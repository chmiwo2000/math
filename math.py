# 복리 계산

n = 12 # 적금 가입 개월수
p = 500000 # 최초 가입 금액
a = 500000 # 매월 납입 금액
r = 0.05 # 년 이자율

amount_1 = p+(p*(r/12)) # 첫째 달 원리금
amount_2 = amount_1+a+((amount_1+a)*(r/12)) # 두번째 달 원리금
amount_3 = amount_2+a+((amount_2+a)*(r/12))
amount_4 = amount_3+a+((amount_3+a)*(r/12))
amount_5 = amount_4+a+((amount_4+a)*(r/12))
amount_6 = amount_5+a+((amount_5+a)*(r/12))
amount_7 = amount_6+a+((amount_6+a)*(r/12))
amount_8 = amount_7+a+((amount_7+a)*(r/12))
amount_9 = amount_8+a+((amount_8+a)*(r/12))
amount_10 = amount_9+a+((amount_9+a)*(r/12))
amount_11 = amount_10+a+((amount_10+a)*(r/12))
amount_12 = amount_11+a+((amount_11+a)*(r/12))
