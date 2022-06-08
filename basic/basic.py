# #csv 파일을 읽어보자
# import csv #모듈을 불러온다
# f = open('seoul.csv', 'r', encoding = 'cp949') #csv파일을 open함수로 열어서 f에 저장한다
# data = csv.reader(f,delimiter = ',') #f를 reader함수에 넣어 data라는 csv.reder 객체를 생성
# print(data)#data 출력
# f.close()

# 데이터를 출력해보자
# import csv
# f = open('seoul.csv', 'r', encoding='cp949')
# data = csv.reader(f)
# for row in data:
#     print(row)
# f.close()

# 헤더를 저장해보자 헤더란 수많은 데이터를 다룰 때 표지판과 같은 역할을 한다,
# 데이터 파일에서 여러가지 값들이 어떤 의미를 갖는지 표시한 행을 말한다.
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# header = next(data) # 헤더라는 변수에 데이터 행을 저장
# print(header) # 헤더변수 출력
# f.close() 

# 서울의 최고 기온이 가장 높았던 날은 ?
# 문제 해결방안 (1) 최고 기온 값 확인, (2) 최고기온이 가장 높은 날짜를 변수에 저장
# (3) 저장된 날짜와 최고 기온 출력 
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# header = next(data)
# for row in data:
#     print(row)
# f.close 
# 현재 최고기온은 문자열이기 때문에 값을 더하거나 비교가 불가능하다
# 숫자 타입으로 변환해 주자
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# header = next(data)
# for row in data:
#     row[-1] = float(row[-1]) # 실수로 변환하고 최고기온은 리스트 맨 뒤이므로 -1로 접근
#     print(row)
# f.close 

# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# header = next(data)
# for row in data:
#     if row[-1] == '':  
#         row[-1] = -999 #빈 문자열을 999로 표시
#     # row[-1] = float(row[-1]) # 실수로 변환하고 최고기온은 리스트 맨 뒤이므로 -1로 접근
#     print(row)
# f.close 

# 최고기온이 높았던 날 알아보자 : 탐색과 비교의 과정을 거쳐야한다 
# 기준값을 기준값과 새 값을 비교한 후, 더 큰값이 나타나면 업데이트 한다
# 따라서 기준값을 저장할 변수가 필요하다

# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# header = next(data)
# max_temp = -999
# max_date = ''
# for row in data:
#     if row[-1] == '':
#         row[-1] = -999
#     row[-1] = float(row[-1])
#     if max_temp < row[-1]:
#         max_date = row[0]
#         max_temp = row[-1]
#     f.close()

#     print(max_temp , max_date)

# 기본 그래프를 그려보자 
# import matplotlib.pyplot as plt
# plt.plot([10,20,30,40])
# plt.show()

# import matplotlib.pyplot as plt
# plt.plot([1,2,3,4,],[12,43,25,15])
# plt.show()

# 그래프에 옵션을 추가해보자 !
# 1. 제목
# import matplotlib.pyplot as plt
# plt.title("서현식")
# plt.plot([1,2,3,4,],[12,43,25,15])
# plt.show()

# 2. 범례 보통 두개 이상의 데이터를 표시할 때 사용한다 
# import matplotlib.pyplot as plt
# plt.title("서현식")
# plt.plot([1,2,3,4,], label = 'asc')
# plt.plot([5,4,3,2,1], label = 'desc')
# plt.legend
# plt.show()

# 3. 그래프 색상 바꿔보기 
# import matplotlib.pyplot as plt
# plt.title("서현식")
# plt.plot([1,2,3,4,], label = 'asc', color = 'blue')
# plt.plot([5,4,3,2,1], label = 'desc',color = 'red')
# plt.legend
# plt.show()

# 4. 그래프 선 모양 바꿔보기 
# import matplotlib.pyplot as plt
# plt.title("서현식")
# plt.plot([1,2,3,4,], label = 'asc',linestyle = 'dotted', color = 'blue')
# plt.plot([5,4,3,2,1], label = 'desc',linestyle = ':',color = 'red')
# plt.legend()
# plt.show()

# 5. 마커모양 바꾸기
# import matplotlib.pyplot as plt
# plt.title("서현식")
# plt.plot([1,2,3,4,],'r', label = 'asc', linestyle = 'dotted', color = 'blue')
# plt.plot([5,4,3,2,1],'g^', label = 'desc',linestyle = ':',color = 'red')
# plt.legend()
# plt.show()

# 내 생일의 기온변화를 그래프로 그려보자 

# 데이터 읽어오기 
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# for row in data:
#     print(row)

# 맨 윗줄에 있는 헤더부분을 제외시킨 후, 최고기온 데이터만 출력
# import csv 
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# for row in data:
#     print(row[-1])

# 데이터 리스트에 저장하기
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# result = []
# for row in data:
#     if row[-1] != '': #최고 기온 값이 존재한다면
#         result.append(float(row[-1]))

# print(len(result)) # len 함수를 통해 데이터 개수 확인

# 데이터를 시각화 해보자 !
# import csv
# import matplotlib.pyplot as plt
# plt.plot(result,'r')
# plt.show()

# 날짜 데이터 추출해보기 : split을 이용해서 분리시키자 !
# for row in data :
#     if row[-1] != ' ': #최고 기온 값이 존재한다면
#         if row[0].split('-')[1] == '08':
#             result.append(float(row[-1]))
# plt.plot(result, 'hotpink')
# plt.show()

# for row in data :
#     if row[-1] != ' ': #최고 기온 값이 존재한다면
#        if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14' :
#             result.append(float(row[-1]))
# plt.plot(result, 'hotpink')
# plt.show()

# 전체 코드를 작성해보자 ! 
# import csv
# import matplotlib.pyplot as plt

# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# high = [ ] #최고 기온 값을 저장하는 리스트
# low = [] #최저 기온을 저장하는 리스트

# for row in data :
#     if row[-1] != ' ' and row[-2] != '': #최고 기온 값과 최저 기온 값이 존재한다면
#         if 1983 <= int(row[0].split('-')[0]) :
#             if row[0].split('-')[1] == '02' and row[0].split('-')[2] == '14': #2월 14일 이라면
#                 high.append(float(row[-1]))
#                 low.append(float(row[-2]))


# plt.rc('font', family = 'Malgun Gothic')
# plt.rcParams['axes.unicode_minus'] = False #마이너스 기호 깨짐 방지
# plt.plot(high, 'hotpink', label ='hight')
# plt.plot(low,'skyblue', label = 'row')
# plt.show()
# plt.legend()

# 기온 데이터를 다양하게 시각화해보자 !

# hist 함수 : 직사각형 모양의 막대 그래프로 나타낸 치수
# import matplotlib.pyplot as plt
# plt.hist([1,1,2,3,4,5,6,6,7,8,9,10])
# plt.show()

# # 주사위 시뮬레이션 및 히스토그램 표현
# import random
# print(random.randint(1,6))

# import random
# dice = []
# for i in range(5) :
#     dice.append(random.randint(1,6))
# print(dice)

# import matplotlib.pyplot as plt
# plt.hist(dice, bins=6) #여기서 빈은 가로축 개수 정함
# plt.show()

# 가온 데이터를 히스토그램으로 표현해보자 !
# import csv
# import matplotlib.pyplot as plt

# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# result = []

# for row in data :
#     if row[-1] != '' :
#         result.append(float(row[-1]))

# plt.hist(result, bins=100, color='r') #히스토 그램으로 나타내기
# plt.show()

# 이번엔 8월 !
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# aug = []

# for row in data:
#     if row[0].split('-')[1]: #-로 구분된 값ㅈ우 두번째 값을 저장
#         if month == '08':
#             aug.append(float(row[-1]))

# plt.hist(result, bins=100, color='r') #히스토 그램으로 나타내기
# plt.show()

# 1월과 8월을 나타내보자 !
# import csv
# import matplotlib.pyplot as plt
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)

# aug = []
# jan = []

# for row in data :
#     month = row[0].split('-')[1] # =로 구분된 값중 두번째 값을 month에 저장
#     if row[-1] != ' ' :
#         if month == '08':
#             aug.append(float(row[-1]))
#         if month == '01':
#             jan.append(float(row[-1])) # 여기 실수형 변환 왜 안되는지 모르겠음
# plt.hist(aug, bins=100, color='r', label=aug)
# plt.hist(jan, bins=100, color='skyblue', label=jan)
# plt.legend()
# plt.show()

# 가온 데이터를 상자 그림으로 표현하자 !
# import matplotlib.pyplot as plt
# import random
# result = []
# for i in range(13) :
#     result.append(random.randint(1,1000))
# print(sorted(result))

# plt.boxplot(result)
# plt.show()

# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# result = []

# for row in data:
#     if row[-1] != '':
#         result.append(float(row[-1]))

# import matplotlib.pyplot as plt
# plt.boxplot(result)
# plt.show()

# 1월과 8월의 상자 그림을 함께 그려보자 !
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)
# aug = []
# jan = []

# for row in data:
#     month = row[0].split('-')[1]
#     if row[-1] != '' :
#         if month == '08':
#             aug.append(float(row[-1]))
#         if month == '01':
#             jan.append(float(row[-1]))
# import matplotlib.pyplot as plt
# plt.boxplot(aug)
# plt.boxplot(jan)
# plt.show()

# 기온을 월별로 구분해서 저장해보자 !
# import matplotlib.pyplot as plt
# import csv

# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)

# #월별 데이터를 저장할 리스트
# month = [[],[],[],[],[],[],[],[],[],[],[],[]]

# for row in data:
#     if row[-1] != ' ':
#         #월과 같은 번호의 인덱스에 월별 데이터 저장
#         # 1월 -> month[0]
#         month[int(row[0].split('-')[1])-1].append(float(row[-1])) #이부분 왜 안되는지 모르겠음 ..
# plt.boxplot(month)
# plt.show()

# 8월 일별가온 데이터를 상자 그림으로 표현하기
# import matplotlib.pyplot as plt
# import csv
# f = open('seoul.csv')
# data = csv.reader(f)
# next(data)

# day = [] #일별 데이터를 저장할 리스트 day 생성
# for i in range(31):
#     day.append([])

# for row in data:
#     if row[-1] != ' ':
#         if row[0].split('-')[1] == '08': #8월 이라면
#            day[int(row[0].split('-')[2])-1].append(float(row[-1])) #왜 오류가 날까..

# plt.style.use('ggplto') #그래프 스타일 지정
# plt.figure(figsize=(10,5), dpi=300) #그래프 크기 수정
# plt.boxplot(day, showfliers=False) #아웃라이어 값 생략
# plt.show()

# 인구파일 알고리즘 설계
# (1) 인구 데이터 파일을 읽어온다
# (2) 전체 데이터에서 한줄씩 반복해서 읽어온다
# (3) 우리 동네에 대한 데이터인지 확인한다
# (4) 우리 동네일 경우 0세부터 100세 이상까지의 인구수를 순서대로 작성한다
# (5) 저장된 연령별 인구수 데이터를 시각화 한다 

#인구 파일 데이터를 읽어서 한줄 씩 출력
# import csv
# f = open('age.csv')
# data = csv.reader(f)

# for row in data:
#     # print(row)    

# #우리동네만 출력
#     if '서울특별시 구로구 신도림동(1153051000)' == row[0] :
#         print(row)
#         print('신도림' in '서울특별시 구로구 신도림동(1153051000)')
#         print('1153' in '서울특별시 구로구 신도림동(1153051000)')
#         print('()' in '서울특별시 구로구 신도림동(1153051000)')

# in 연산자 사용하여 간단하게 구현 
# import csv
# f = open('age.csv')
# data = csv.reader(f)

# for row in data:
#     if '신도림' in row[0]:
#         print(row)

# 0세 부터 100세 이상까지의 인구수를 순서대로 저장해보자  리스트 3번부터  끝까지 읽으면 됨
# import csv
# f = open('age.csv')
# data = csv.reader(f)
# for row in data:
#     if '신도림' in row[0]:
#         for i in row[3:] :
#             print(i)

# 데이터를 읽었으니 순서대로 저장해보자 ! 
# import csv
# f = open('age.csv')
# data = csv.reader(f)
# result = []
# for row in data :
#     if '신도림' in row[0]:
#         for i in row[3:] :
#             result.append(int(i))

# print(result)

# 시각화를 해보자 !
# import matplotlib.pyplot as plt

# import csv
# f = open('age.csv')
# data = csv.reader(f)
# result = []
# for row in data :
#     if '신도림' in row[0]:
#         for i in row[3:] :
#             result.append(int(i))

# plt.style.use('ggplot')
# plt.plot(result)
# plt.show()

# 인구 구조를 다양한 형태로 시각화 해보자 !
# import csv
# from os import name
# f = open('age.csv')
# data = csv.reader(f)
# result = []
# name = input('인구 구조가 알고 싶은 지역의 이름을 입력해 주세요 :')

# for row in data :
#     if name in row[0]:
#         for i in row[3:]:
#             result.append(int(i.replace(',','')))

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.rc('font', family='Malgun Gothic')
# plt.title(name + '지역의 인구 구조')
# plt.plot(result)
# plt.show()

# 막대 그래프를 그려보자 !
# import matplotlib.pyplot as plt
# plt.bar([0,1,2,4,6,10],[1,2,3,5,6,7]) #막대를 표시할 위치, 막대의 높이, rnage 함수로도 가능
# plt.show()

# 우리 동네의 인구 구조를 막대 그래프로 표시해보자 !
# import csv
# f = open('age.csv')
# data = csv.reader(f)

# result = []

# for row in data : 
#     if '신도림' in row[0]:
#         for i in row[3:]:
#             result.append(int(i))

# import matplotlib.pyplot as plt
# plt.bar(range(101),result) #여기서 barh 함수로 바꾸면 수평방향으로 그려진다.
# plt.show()

# 항아리 모양 그래프 그리기 
# 남성 데이터와 여성 데이터를 각각 따로 저장해보자 ! 
# 남성데이터는 맨 앞에서부터 리스트 m에 저장하고
# 여성데이터는 맨뒤에서부터 저장한 수, 다시 역순으로 뒤집는다
# 남성은 리스트값 3부터, 여성은 -1부터 시작된다는 점을 유의하자

# import csv
# f = open('gender.csv')
# data = csv.reader(f)
# m = []
# f = []

# for row in data:
#     if '신도림' in row[0]:
#         for i in range(0,101): # 이 구문이 이해가 안됨
#             m.append(-int(row[i+3]))
#             f.append(int(row[-(i+1)]))
# f.reverse()

# import matplotlib.pyplot as plt
# plt.barh(range(101),m, label ='남성')
# plt.barh(range(101),f, label = '여성')
# plt.show()

# 우리 동네 인구 구조를 항아리 모양 그래프로 그려보자 !
# import csv
# from os import altsep
# f = open('gender.csv')
# data = csv.reader(f)

# m = []
# f = []
# name = input('찾고 싶은 지역을 입력하세요 : ')
# for row in data:
#     if name in row[0]:
#         for i in row[3:104]:
#             m.append(-int(i))
#         for i in row[106:]:
#             f.append(int(i))

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.figure(figsize=(10,5), dpi=300)
# plt.rc('font', family='Magun Gothic')
# plt.rcParams['axes.unicode_minus'] = False
# plt.title(name+ '지역의 남녀 성별 인구 분포도') 
# plt.barh(range(101),m, label ='남성') # 여기가 갑자기 왜 안될까
# plt.barh(range(101),f, label = '여성')
# plt.legend()
# plt.show()

# 제주도에는 여성의 비율이 더 높을까 ?

# import csv
# from os import altsep
# f = open('gender.csv')
# data = csv.reader(f)

# m = []
# f = []
# name = input('찾고 싶은 지역을 입력하세요 : ')
# for row in data:
#     if name in row[0]:
#         for i in row[3:104]:
#             m.append(-int(i))
#         for i in row[106:]:
#             f.append(int(i))
#         break

# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.figure(figsize=(10,5), dpi=300)
# plt.rc('font', family='Magun Gothic')
# plt.rcParams['axes.unicode_minus'] = False
# plt.title(name+ '지역의 남녀 성별 인구 분포도') 
# plt.barh(range(101),m, label ='남성') # 여기가 갑자기 왜 안될까
# plt.barh(range(101),f, label = '여성')
# plt.legend()
# plt.show()

# 혈액형 비율 표현하기
# import matplotlib.pyplot as plt
# plt.pie([10,20])
# plt.show()

# import matplotlib.pyplot as plt
# size = [2441, 2312, 1031, 1233]
# label = ['a형','b형','c형','ab형']
# color = ['darkmagenta','deeppink','hotpink','pink']
# plt.axis('equal')
# plt.pie(size, labels=label, autopct='%.1f%%', colors=color)
# explode = (0,0,0.1,0) #이거 안됨
# plt.legend()
# plt.show()

# import csv
# from os import name
# from matplotlib import colors
# f = open('gender.csv')
# data = csv.reader(f)
# size = []
# name = input('지역을 선택하세요')
# for row in data:
#     if name in row[0] :
#         m = 0
#         f = 0
#         for i in range(101) : 
#             m += int(row[i+3])
#             f += int(row[i+106])
#         break
# size.append(m)
# size.append(f)
# # print(size)

# import matplotlib.pyplot as plt
# plt.rc('font', family='Magun Gothic')
# color = ['crimson', 'darkcyan']
# plt.axis('equal')
# plt.pie(size, labels=['남', '여'], autopct='%.1f%%', colors= color, startangle=90)
# plt.title(name + '지역의 남녀 성별 비율')
# plt.show()

# 우리 동네 인구를 산점도로 표현하기 !
# 꺽은선 그래프로 표현하기

# import csv 
# f = open('gender.csv')
# data = csv.reader(f)
# m = []
# f = []

# name = input('궁금한 동네 입력:')
# for row in data:
#     if name in row[0] :
#         for i in range(3,104):
#             m.append(int(row[i]))
#             f.append(int(row[i+103]))
#         break
# import matplotlib.pyplot as plt
# plt.plot(m, label ='남성')
# plt.plot(f, label ='여성')
# plt.legend()
# plt.show()

# 막대 그래프로 표현해보자 !
# import csv 
# f = open('gender.csv')
# data = csv.reader(f)
# result = []

# name = input('궁금한 동네 입력:')
# for row in data:
#     if name in row[0] :
#         for i in range(3,104):
#           result.append(int(row[i]) - int(row[i+103]))
#         break
# import matplotlib.pyplot as plt
# plt.bar(range(101),result)
# plt.show()

# 산점도로 표현하기
# import matplotlib.pyplot as plt
# plt.scatter([1,2,3,4],[10,30,20,40]) # 1,10 2,30 3,30 4,40 에 점이 그려진다
# plt.show()

# 버블차트 그리기 
# import matplotlib.pyplot as plt
# plt.scatter([1,2,3,4],[10,30,20,40], s=[100,200,250,300], c=['red','blue','green','gold'],cmap='jet') # 1,10 2,30 3,30 4,40 에 점이 그려진다 s는 크기를 의미, cmap는 컬러바 속성
# plt.colorbar()
# plt.show()

# import matplotlib.pyplot as plt
# import random
# x = []
# y = []
# size = []
# for i in range(100):
#     x.append(random.randint(50,100))
#     y.append(random.randint(50,100))
#     size.append(random.randint(10,100))
# plt.scatter(x,y,s = size, c=size, cmap='jet', alpha=0.7)
# plt.colorbar()
# plt.show()

# 제주도의 연령대별 성별 비율을 산점도로 표현해보자 ! 
# import csv 
# import matplotlib.pyplot as plt
# import math
# f = open('gender.csv')
# data = csv.reader(f)
# m = []
# f = []
# size = []
# name = input('궁금한 지역 입력:')
# for row in data : 
#     if name in row[0]:
#         for i in range(3,104):
#             m.append(int(row[i]))
#             f.append(int(row[i+103]))
#             size.append(math.sqrt(int(row[i])+int(row[i+103]))) #사이즈 크기 조절
#         break
# plt.style.use('ggplot')
# plt.rc('font', family="Magun Gothic")
# plt.figure(figsize=(10,5), dpi=300)
# plt.title(name)
# plt.scatter(m,f,s=size, c=range(101),alpha=0.5,cmap='jet')
# plt.colorbar()
# plt.plot(range(max(m)),range(max(m)), 'g') #이거 뭔지 모르겠음
# plt.xlabel('남성인구수')
# plt.xlabel('여성인구수')
# plt.show()

# 대중교통 데이터 시각화 하기 
# import csv
# f= open('subwayfee.csv')
# data = csv.reader(f)
# next(data)
# for row in data:
#     for i in range(4,8):
#         row[i] = int(row[i])
#     print(row)

# 유임 승차 비율이 가장 높은 역은 어디일까 ?
# 알고리즘
# 1. 데이터를 읽어온다. 2. 모든 역의 데이터를 바탕으로 각 역의 비율 계산 rate = 유임승차/무임승차
# 3. 비율기 가장 높은 역 찾는다, 4. 높은 역 출력

# 유임 승차 비율이 가장 높은 역 찾기
# import csv

# from numpy import round_
# f = open('subwayfee.csv')
# data = csv.reader(f)
# next(data)
# mx = 0
# rate = 0
# for row in data:
#     for i in range(4,8):
#         row[i] = int(row[i])
#         if row[6] != 0  and (row[4]+row[6]) > 100000: #이부분이 실행이 안되는데 문제 해결 못함
#             rate = row[4] / (row[4]+row[6])
#             if rate > mx :
#                 mx = rate
#                 mx_station = row[3] + ' ' + row[1]

# print(mx_station,round(mx*100,2))

# 유무임 승차가 가장 많은 역은 어디일까 ?
# 알고리즘 1. 데이터를 읽어온다 2. 모든역을 바탕으로 유,무임 승하차가 가장 많은 역 찾음
# 3. 각각의 인원이 가장 많은 역 찾는다

# import csv
# f= open('subwayfee.csv')
# data = csv.reader(f)
# next(data)
# mx = [0] * 4
# mx_station = [''] * 4

# for row in data : # 모든 역에 대해 반복한다
#     for i in range(4,8) :
#         row[i] = int(row[i]) # 4번인덱스 유임승차 인원부터 7번인덱스 무임하차 인원수까지 반복하여 데이터를 정수로 바꿈 이때 역이 지금까지 젖아된 최댓값보다 클 경우 mx와 mx_station의 값을 바꾼다
#         if row[i] > mx[i-4] :
#             mx[i-4] = row[i]
#             mx_station[i-4] = row[3] + ' ' + row[1]
#             for i in range(4):
#                 print(mx_station[i],mx[i])

# 유무임 승차 인원이 가장 많은 역 찾기 총 정리
# import csv
# f = open('subwayfee.csv')
# data = csv.reader(f)
# next(data)

# mx = [0] * 4
# mx_station = [''] * 4
# label = ['유임승차','유임하차','무임승차','무임하차']
# for row in data :
#     for i in range(4,8):
#         row[i] = int(row[i])
#         if row[i] > mx[i-4] :
#             mx[i-4] = row[i]
#             mx_station[i-4] = row[3] + '  '+ row[1]
# for i in range(4):
#     print(label[i]+ ':' +mx_station[i], mx[i])

# 모든 역의 유뮤임 승하차 비율은 어떻게 될까 파이차트로 표현하자 ! 
# import csv
# import matplotlib.pyplot as plt
# f = open('subwayfee.csv')
# data = csv.reader(f)
# next(data)
# label = ['유임승차','유임하차','무임승차','무임하차']
# for row in data :
#     for i in range(4,8) :
#         row[i] = int(row[i])

# plt.pie(row[4:8])
# plt.axis('equal')
# plt.show()

# 다음은 역 이름을 제목으로 표시하고 각각의 비율과 레이블 색상을 추가한 전체 코드
# import csv
# import matplotlib.pyplot as plt

# f = open('subwayfee.csv')
# data = csv.reader(f)
# next(data)
# label = ['유임승차','유임하차','무임승차','무임하차']
# c = ['#14CCC0', '#389993', '#FF1C6A', '#CC14AF']
# plt.rc('font', family='Malgun Gothic')

# for row in data:
#     for i in range(4,8):
#         row[i] = int(row[i])
      

# plt.figure(dpi=300)
# plt.title(row[3]+' '+row[i]) #이거 안되는데 왜 안되는지 아는사람 ?
# plt.pie(row[4:8], labels=label, colors=c, autopct='%1.f%%')
# plt.axis('equal')
# plt.savefig(row[3]+' '+row[1]+ '.png')
# plt.show()

# 지하철 시간대별 데이터 시각화하기 
# import csv
# import math
# f = open('subwaytime.csv')
# data = csv.reader(f)
# for row in data :
#     row[4:] = map(int, row[4:]) #모든 값이 int로 바뀐다 이부분 안됨
#     print(row)

# 출근 시간대 사람들이 가장 많이 타고 내리는 역은 어디일까 
# 승차 데이터는 10번 위치에 저장되어 있다 10번 인덱스 데이터를 추출해서 리스트에 저장하고,
# 리스트의 길이와 리스트에 저장된 값을 출력하면 현재 598역에 대한 데이터가 정수 형태로 저장된 것을 확인 할 수 있다.

# import csv
# f = open('subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)
# result = []
# for row in  data:
#     row[4:] = map(int, row[4:])
#     result.append(sum(row[10:15:2]))

# # print(len(result))
# # print(result)

# # 막대그래프로 표현 
# import matplotlib.pyplot as plt
# result.sort()
# plt.bar(range(len(result)), result)
# plt.show()

# 최댓값 찾기 
# import csv
# f = open('subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)
# mx = 0 # 최댓값을 저장할 변수 초기화
# mx_station = ' ' # 최댓값을 갖는 역 이름 저장 변수 초기화 
# for row in data : # 최댓값 찾기(전부 탐색하여 최댓값을 갱신하는 방식)
#     row[4:] = map(int, row[4:])
#     if sum(row[10:15:2]) > mx :
#         mx = sum(row[10:15:2])
#         mx_station = row[3]+'('+row[1]+')'

# print(mx_station, mx)

# 출근 시간대 사람들이 가장 많이 타고 내리는 역 찾기 

# import csv
# f = open('subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)
# mx = 0 # 최댓값을 저장할 변수 초기화
# mx_station = ' ' # 최댓값을 갖는 역 이름 저장 변수 초기화 
# for row in data : # 최댓값 찾기(전부 탐색하여 최댓값을 갱신하는 방식)
#     row[4:] = map(int, row[4:])
#     a = row[11:16:2] #하차 인원 값 추출
#     if sum(a) > mx :
#         mx = sum(a)
#         mx_station = row[3] + row[1]
# print(mx_station,mx)

# 밤 11시에 사람들이 가장 많이 타는 역은 어디일까 
# 출근시간의 경우 7시,8시,9시라서 한칸씩 셀 수있는데, 23(23~23:59)시니까 패턴을 찾아 분석해야 한다
# i = 4 + (t-4) * 2
# import csv
# f = open('subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)
# mx = 0
# mx_station = ''
# t = int(input('몇 시의 승차 인원이 가장 많은 궁금하세요? :'))

# for row in data:
#     row[4:] = map(int, row[4:])
#     a = row[4+(t-4)*2] #입력 받은 시각의 승차 인원 값 추출하기
#     if a > mx : #모든 데이터 탐색
#         mx = a
#         mx_station = row[3]+ row[1]
# print(mx_station,mx)

# 시간대별로 사람들이 가장 많이 타고 내리는 역은 어디일까
# i = j*2 +4

# import csv
# f= open('subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)
# mx = [0] * 24 # 시간대별 최대 승차 인원 저장 리스트 초기화
# mx_station = [''] * 24 #시간대별 최대 승차 인원 역 이름 저장 리스트 초기화
# for row in data:
#     row[4:] = map(int, row[4:])
#     for j in range(24) : 
#         a = row[j*2+4] # j와 인덱스 번호 사이에 관계식 사용
#         if a > mx[j] :
#             mx[j] = a
#             mx_station[j] = row[3]
# print(mx_station)
# print(mx)

# import matplotlib.pyplot as plt
# plt.rc('font', family='Magun Gothic')
# plt.bar(range(24),mx)
# plt.xticks(range(24),mx_station, rotation=90)
# plt.show()

# 시간대별로 하차 인원이 가장 많은 역을 찾는 코드
# import csv
# import matplotlib.pyplot as plt
# f = open('subwaytime.csv')
# data =  csv.reader(f)
# next(data)
# next(data)
# mx = [0] * 24 # 시간대별 최대 승차 인원을 저장할 리스트 초기화
# mx_station = [''] * 24  #시간대별 최대 승차 인원 역 이름을 저장할 리스트 초기화

# for row in data:
#     row[4:] = map(int, row[4:])
#     for j in range(24) :
#         b = row[5 + j * 2] #j값과 인덱스 번호 값의 관계식 사용
#         if b > mx[j] :
#             mx[j] = b
#             mx_station[j] = row[3] + '(' +str(j+4)+')'

# plt.rc('font', family = 'Malgun Gotinc')
# plt.bar(range(24), mx, color='b') # 막대그래프 속성 변경
# plt.xticks(range(24), mx_station, rotation=90)
# plt.show()

# 모든 지하철역에서 시간대별 승하차 인원을 모두 더하면
# 1. 데이터를 읽어온다.
# 2. 모든 역에 대해 시간대별 승차 인원과 하차 인원을 누적해서 더한다.
# 3. 시간대별 승차 인원 하차 인원을 그래프로 표현한다

# import csv
# import matplotlib.pyplot as plt
# f = open('subwaytime.csv')
# data = csv.reader(f)
# next(data)
# next(data)

# s_in = [0] *24 # 승차 인원 저장 리스트 초기화
# s_out = [0] * 24 #하차 인원 저장 리스트 초기화

# for row in data:
#     row[4:] = map(int, row[4:])
#     for i in range(24) :
#         s_in[i] += row[4+i*2]
#         s_out[i] += row[5+i*2]

# plt.rc('font', family = "Magun Gothic")
# plt.title('지하철 시간대별 승하차 인원 추이') #제목 추가
# plt.plot(s_in, label='승차')
# plt.plot(s_out, label='하차')
# plt.legend()
# plt.xticks(range(24), range(4,28))
# plt.show()

# 프로젝트 !
# numpy 라이브러리 : 숫자를 더 쉽게 다룰 수 있다
# import numpy
# print(numpy.sqrt(2)) # 2의 제곱근 ,루트 2출력

# 넘피로 삼각함수 구하는 법 !
# from os import replace
# import numpy as np
# from numpy import random
# print(np.pi)
# print(np.sin(0))
# print(np.cos(np.pi))

# a = np.random.rand(5) # 0~1사이 실수 5개 랜덤 출력
# print(a)
# print(type(a))

# print(random.choice(6,10)) # 0에서 5사이(6-1) 수를 랜덤하게 10번 뽑음
# print(random.choice(6,10,replace=False)) #이러면 중복방지임
# print(random.choice(6,10,replace=False,p=[0.1,0.2,0.3,0.2,0.1,0.1])) #확률 지정

# numpy라이브러리를 통해 그래프 그리기

# # 1. 막대
# import matplotlib.pyplot as plt
# import numpy as np
# dice = np.random.choice(6,10)
# plt.hist(dice, bins=6)
# plt.show()

# # 2.버블
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.randint(10,100,200) #10부터 100까지 정수 200개 추출
# y = np.random.randint(10,100,200) #10부터 100까지 정수 200개 추출
# size = np.random.rand(100) * 100

# plt.scatter(x,y, s=size ,c = x,cmp='jet', alpha=0.7)
# plt.colorbar()
# plt.show()

# numpy array 사용하기 : n차원 배열이다. 리스트와 같은 연속된 데이터는 numpy array로 변환 가능
# import numpy as np
# a = np.array([1,2,3,4])
# print(a[1],a[-1]) #일반 배열과 차이점은 쉼표가 없다

# numpy array는 한가지 타입 데이터만 저장이 가능, 예를들어 숫자,문자 저장되어 있으면 문자로 출력
# import numpy as np
# a = np.array([1,2,'3',4])
# print(a)
# b = np.zeros(10) # 0으로 이루어진 크기가 10인 배열 생성
# c = np.ones(10) #1로 이루어진 크기가 10인 배열 생성
# d = np.eye(3) #3x3열의 단위 배열 생성

# #연속된 숫자로 데이터를 생성하는 배열
# print(np.arange(3))
# print(np.arange(3,7)) #[3,4,5,6]
# print(np.arange(3,7,2)) # 이건 2 간격으로 생성
# print(np.linspace(1,2,11)) # 1과 2 사이를 11개 구간으로 나눈 실수 생성

#초기값이 5인 배열 100개 만들어 보기
# import numpy as np
# a = np.zeros(10) + 5
# print(a)

# 싸인함수 그래프
# import matplotlib.pyplot as plt
# import numpy as np
# a = np.arange(-np.pi, np.pi, np.pi/100)
# plt.plot(a, np.sin(a))
# plt.show()

# 싸인함수 평행이동
# import matplotlib.pyplot as plt
# import numpy as np
# a = np.arange(-np.pi, np.pi, np.pi/100)
# plt.plot(a, np.sin(a))
# plt.plot(a, np.cos(a))
# plt.plot(a+np.pi/2, np.sin(a))
# plt.show()

# 마스크 기능 : 어떤 조건에 부합하는 데이터만 선별적으로 저장한다 
# import numpy as np
# a = np.arange(-5,5)
# print(a[a<0])
# mask1 = abs(a) > 3 #절대값이 3보다 큰 값
# mask2 = abs(a) %2 == 0
# print(mask1)
# print(a[mask1+mask2]) #둘중 하나의 조건이라도 참일 경우
# print(a[mask1*mask2]) # 두 가지 조건 모두 참일 경우

# numpy 라이브러리를 이용하여 재미있는 버블차트를 그려보자 !
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.random.randint(-100,100,1000) #1000개의 랜덤 값 추출
# y = np.random.randint(-100,100,1000) #1000개의 랜덤 값 추출
# size = np.random.rand(100) * 100 #이코드가의미하는건 무엇일까
# mask1 = abs(x) > 50
# mask2 = abs(y) > 50
# x = x[mask1+mask2]
# y = y[mask1+mask2]
# plt.scatter(x, y, s=size, c=x, cmp='jet', alpha=0.7) # 여기가 안돼요
# plt.colorbar()
# plt.show()

# 직접 프로젝트를 해보자 ! 
# 질문
# 1. 전국에서 영유아들이 가장 많이 사는 지역은 ?
# 2. 보통 학군이 좋다고 알려진 지역에는 청소년들이 얼마나 살까?
# 3. 광역시 데이터를 10년 단위로 살펴보면 청년 비율이 줄고 있다는 사실을 알 수 있을까?
# 4. 서울에서 지난 5년간 인구가 가장 많이 증가한 구는 어디일까?
# 5. 우리 동네의 인구 구조와 가장 비슷한 동네는 어디일까 ? 이거로 갑니다 !!

#알고리즘
#1. 데이터를읽어온다
# 2. 궁금한 지역의 이름을 입력ㅂ다는다
# 3. 궁금한 지역의 인구 구조를 저장한다
# 4. 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다
# 5. 가장 비슷한 곳의 인구 구조와 궁금한 지역의 인구 구조를 시각화한다

# 데이터를 읽어온다
# import csv
# f = open('age.csv')
# data = csv.reader(f)
# next(data)
# for row in data:
#     print(row)

# # 궁금한 지역이름을 받는다
# name  = input('인구 구조가 알고 싶은 지역의 이름 입력하세요:')

# 궁금한 지역의 인구 구조를 저장한다

# import csv
# f = open('age.csv')
# data = csv.reader(f)
# next(data)
# home = [] #입력받은 데이터를 저장할 리스트
# name  = input('인구 구조가 알고 싶은 지역의 이름 입력하세요:')
# for row in data:
#     if name in row[0]: #입력받은 지역의 이름이 포함된 행 찾기
#         for i in row[3:]: # 3번 인덱스 값 부터 슬라이싱
#             home.append(int(i)) #입력받은 데이터를 홈에 저장
# print(home)

# 위의 코드를 numpy를 이용해 좀 더 간단히 해보자 ! 

# import csv
# import numpy as np
# import matplotlib.pyplot as plt
# f = open('age.csv')
# data = csv.reader(f)
# next(data)
# home = [] #입력받은 데이터를 저장할 리스트
# name  = input('인구 구조가 알고 싶은 지역의 이름 입력하세요:')
# for row in data:
#     if name in row[0]: #입력받은 지역의 이름이 포함된 행 찾기
#         home = np.array(row[3:], dtype=int)
# print(home)

#그래프로 표현
# plt.rc('font', family='Magun Gothic')
# plt.title(name)
# plt.plot(home)
# plt.show

# 자 이제 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾아보자 !
# 1. 전국의 모든 지역중 한곳을 택한다
# 2. 궁금한 지역의 0세 인구비율에서 기존지역의 인구비율 0을 뺀다
# 3. 2번을 100세 이상까지 반복한 이후 그 차이를 모두 더한다
# 4. 차이가 가장 작은 지역을 찾는다

# 한번에 불러온 데이터 여러번 사용하기 
# import csv
# import numpy as np
# import matplotlib.pyplot as plt
# f = open('age.csv')
# data = csv.reader(f)
# next(data)
# data = list(data)
# name  = input('인구 구조가 알고 싶은 지역의 이름 입력하세요:')
# for row in data:
#     if name in row[0]: #입력받은 지역의 이름이 포함된 행 찾기
#         home = np.array(row[3:], dtype=int) / int(row[2])

# for row in data:
#     away = np.array(row[3:], dtype=int) /int(row[2])
#     print(home-away)

#그래프로 표현
# plt.rc('font', family='Magun Gothic')
# plt.title(name)
# plt.plot(home)
# plt.show

# 이코드는 현재 내 수준에서는 이해가 어렵다 더 공부해보자 
# import numpy as np
# import csv
# import matplotlib.pyplot as plt
# # 데이터를 읽어온다
# f = open('age.csv')
# data = csv.reader(f)
# next(data)
# data = list(data)

# # 궁금한 지역의 이름을 입력받는다
# name = input('인구 구조가 알고 싶은 지역의 이름을 입력해주세요? : ')
# mn = 1 # 최솟값을 저장 변수 생성 및 초기화
# result_name = '' #최솟값을 갖는 지역의 이름을 저장할 변수 생성 및 초기화
# result = 0 # 최솟값을 갖는 지역의 연령대별 인구 비율을 저장할 배열 생성 및 초기화

# # 궁금한 지역의 인구 구조를 저장한다
# for row in data:
#     if name in row[0] :
#         home = np.array(row[3:], dtype=int) / int(row[2])

# # 궁금한 지역의 인구 구조와 가장 비슷한 인구 구조를 가진 지역을 찾는다
# for row in data:
#     away = np.array(row[3:], dtype=int) /int(row[2])
#     s = np.sum((home-away)**2) #제곱을 해서 음수 방지
#     if s < mn and name not in row[0] :
#         mn = s
#         result_name = row[0]
#         result = away
# # 궁금한 지역의 인구 구조와 가장 비슷한 곳의 인구 구조를 시각화 한다
# plt.style.use('ggplot')
# plt.figure(figsize=(10,5), dpi=300)
# plt.rc('font', family='Malgun Gothic')
# plt.title(name)
# plt.plot(home,label=name)
# plt.plot(result,label=result_name)
# plt.legend()
# plt.show()

# 판다스를 체험해보자 ! : 테이블 형태의 데이터를 쉽게 다루도록 도와준다  이유는 모르겟지만 안깔린다 ..
import pandas as pd
df = pd.read_html('http://en.wikipeda.org/wiki/All-time_Olympic_Games_medal_table')