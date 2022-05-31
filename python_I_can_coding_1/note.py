# 주석
# '+'를 ','로 대체하면 str()은 붙일 필요가 없지만 ' '(띄어쓰기)가 포함된다.
# ctrl + '/' : 단체 주석처리
# ''' ~ ''' : 여러 문장 주석처리


# ---------------------------------------------------------------
# 기본 연산자
# print(2**3) : 2의 3제곱
# print(5%3) : 5를 3으로 나눈 나머지
# print(5//3) : 5를 3으로 나눈 몫


# ---------------------------------------------------------------
# AND OR
# and(&) : 이고
# or(|) : 또는


# ---------------------------------------------------------------
# 수학함수
# from math import*
# abs(-5) : 절대값
# pow(4,2) : 4의 2제곱

# round : 반올림
# floor : 내림
# ceil : 올림
# sqrt : 제곱근


# ---------------------------------------------------------------
# 랜덤함수 RANDOM
# from random import *
# print(random()) : 0.0 ~ 1.0 미만의 임의의 값 생성
# print(int(random()*10)) : 0 ~ 10 미만의 임의의 정수 생성
# print(randrange(1,46)) : 1 ~ 46 미만의 임의의 정수 생성
# print(randint(1,45)) : 1 ~ 45 이하의 임의의 정수 생성


# jumin = "000724-1234567"

# print("성별 : " +jumin[7] )
# print("생년월일 : " + jumin[0:6])
# print("생년월일 : " + jumin[:6])

# print("뒤 7자리 : "+jumin[7:14])
# print("뒤 7자리 : "+jumin[7:])


# ---------------------------------------------------------------
# 문자열 STRING

# python = "Python is Amazing"

# print(python.lower())
# 소문자로
# print(python.upper())
# 대문자로
# print(python[0].isupper())
# 해당되는 문자가 대문자인가? True False
# print(len(python))
# 문자열의 길이
# print(python.replace("Python","Java"))
# 문자열 교체 Python > Java

# index_num = python.index("n")
# print(index_num)
# index_num = python.index("n",index_num+1)
# print(index_num)

# print(python.find("Java"))
# print(python.count("n"))


# ---------------------------------------------------------------
# 방법 1
# print("나는 %d살입니다."% 20)
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple은 %c로 시작해요." % "A")
# '%s'를 사용하면 무엇을 쓰도 상관 X 

# print("나는 %s색과 %s색을 좋아해요."%("파란","빨간"))

# 방법 2
# print("나는 {}살입니다.". format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란","빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란","빨간"))
# 순서대로 넣는다.

# 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age =20,color="빨간"))
# 변수처럼 format뒤의 값을 사용할 수 있다.

# 방법 4
# age =20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")
# 실제 변수의 값을 가져옴


# ---------------------------------------------------------------
# 탈출문자

# \n : 줄바꿈
# print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표 표현 가능
# 저는 "나도코딩"입니다.
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")

# \\ : 문장 내에서 '\'
# print("C:\\Users\\aidi0\\Desktop\\python-tutorial")

# \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")
# 'Red '를
# 'Pine'이 대체

#\b : 백스페이스(한 글자 삭제)
# print("Redd\bApple")
# d를 하나 삭제

#\t : 탭
# print("Red\tApple")

# ---------------------------------------------------------------
# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

#조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

#하하씨가 다음 정류장에서 다음 칸에 탐
#append : list의 맨 뒤에 추가
# subway.append("하하")
# print(subway)

#정형돈씨를 유재석 / 조세호 사이에 넣기
# subway.insert(1, "정형돈")
# print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway)
# print(subway.count("유재석"))

# 정렬도 가능
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# 순서 뒤집기도 가능
# num_list.reverse()
# print(num_list)

# 모두 지우기
# num_list.clear()
# print(num_list)

# 다양한 자료형 함께 사용
# mix_list = ["조세호", 20, True]
# print(mix_list)

# 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# ---------------------------------------------------------------
# 사전 dictionary

# 키 : 3, 100 , 사용자 : 유재석, 김태호
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# 없는 값을 가져오면 None이라는 결과를 얻는다(get()을 이용할 때에만!)
# print(cabinet.get(5))
# print(cabinet.get(5,"사용가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# 새로운 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# 간 손님
# del cabinet["A-3"]
# print(cabinet)

# key만 출력
# print(cabinet.keys())

# value만 출력
# print(cabinet.values())

# key, value 함께 출력
# print(cabinet.items())

# 목욕탕 폐점
# cabinet.clear()
# print(cabinet)


# ---------------------------------------------------------------
# 튜플(변경되지 않는 목록)

# menu = ("돈까스", "치즈까스")
# print(menu[0])
# print(menu[1])

# 오류발생 - menu.add("생선까스")

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)


# ---------------------------------------------------------------
# 집합 set
# 중복 안됨, 순서 없음

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# 교집합(java 와 python을 모두 할 수 있는 개발자)
# print(java & python)
# print(java.intersection(python))

# 합집합(java 또는 python을 할 수 있는 개발자)
# print(java | python)
# print(java.union(python))

# 차집합(java는 가능, but python을 불가능한 개발자)
# print(java-python)
# print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)


# ---------------------------------------------------------------
# 자료구조의 변경
# 커피숍
# 자료형 : set
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# 자료형을 list로 바꿈
# menu = list(menu)
# print(menu, type(menu))

# 자료형을 tuple로 바꿈
# menu = tuple(menu)
# print(menu, type(menu))

# 자료형을 set로 바꿈
# menu = set(menu)
# print(menu, type(menu))


# ---------------------------------------------------------------
#IF
#if 조건:
#   실행 명령문

# weather = input("오늘 날씨는 어때요? ")
# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("날씨가 좋아요!")

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요.")
# elif 10 <= temp < 30:
#     print("괜찮은 날씨에요.")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요.")
# else:
#     print("너무 추워요. 나가지 마세요.")


# ---------------------------------------------------------------
# For

# randrange()에서 사용한 range()
# for waiting_num in range(1, 6): #1, 2, 3, 4, 5
#     print("대기번호 : {0}" .format(waiting_num))

# starbucks = ["아이언맨", "토르", "아이엠 그루트"]
# for customer in starbucks:
#     print("{0}, 커피가 준비되었습니다.".format(customer))


# ---------------------------------------------------------------
# while

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# 무한루프
# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer,index))
#     index += 1

# customer = "토르"
# person = "Unknown"

# 조건을 만족할 때까지 반복
# while person != customer:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?")


# ---------------------------------------------------------------
#continue : 스킵하고 다음 반복문 진행
#break : 현 상황에서 반복문 종료

# 결석
# absent = [2,5]
# 책을 두고옴
# no_book = [7]
# for student in range(1,11): #1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print("{0}, 책을 읽어봐".format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4,5]
# print(students)
# students =[i+100 for i in students]
# print(students)

# 학생 이름을 길이로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [len(i) for i in students]
# print(students)

# 학생 이름을 대문자로 변환
# students = ["Iron man", "Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)


# ---------------------------------------------------------------
# 함수

# from pytz import common_timezones


# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# open_account()

# def deposit(balance, money): # 입금
#     print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): # 출금
#     if balance >= money: # 잔액이 출금보다 많은 경우
#         print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
#         return balance

# def withdraw_night(balance, money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0 # 잔액
# balance = deposit(balance,1000)
# print(balance)
# balance = withdraw(balance,500)
# print(balance)
# commission, balance = withdraw_night(balance, 300)
# print("수수료는 {0}원이며, 잔액은 {1}원 입니다.".format(commission,balance))


# ---------------------------------------------------------------
# 함수의 인자를 섞어도 매칭이 되어있으면 호출 가능

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name="유재석",main_lang="파이썬", age=20)
# profile(main_lang="자바",age=25,name="김태호" )


# ---------------------------------------------------------------
# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end= " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language): # *language에는 내가 원하는 만큼의 양을 넣을 수 있다.
#     print("이름 : {0}\t나이 : {1}\t".format(name,age),end= " ")
#     for lang in language:
#         print(lang, end = " ")
#     print()

# profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("김태호", 25, "Kothlin", "Swift")


# ---------------------------------------------------------------
# 지역변수와 전역변수

# gun = 10

# def checkpoint(soldiers): # 경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))

# def checkpoint_ret(gun1, soldiers):
#     gun1 = gun1 - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun1))
#     return gun1

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# gun = checkpoint_ret(gun,2)
# print("남은 총 : {0}".format(gun))


# ---------------------------------------------------------------
# 표준 입출력

# print("Python", "Java", sep = ", ", end="? ")
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

# 오른쪽, 왼쪽 정렬
# 시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     print(subject.ljust(8),str(score).rjust(4), sep = ":")

# 은행 대기순번표
# 001, 002, 003, ...
# 빈 자리 0으로 채우기
# for num in range(1,21):
#     print("대기번호 : "+ str(num).zfill(3))

# 사용자에게 입력을 받을 경우 항상 string 문자열 형태이다.
# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은" + answer + "입니다.")


# ---------------------------------------------------------------
# # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# # 양수일 땐 +로 표시, 음수일 땐 -로 표시(부호를 표시)
# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 '_'로 채움
# print("{0:_<10}".format(500))

# # 3자리마다 ","찍기
# print("{0:,}".format(100000000000))

# # 3자리마다 ","찍고, 부호 표시
# print("{0:+,}".format(100000000000))
# print("{0:+,}".format(-100000000000))

# # 3자리마다 ","찍고, 부호 표시, 자릿수 확보
# # 빈자리는 "^"로 채우기
# print("{0:^<+30,}".format(100000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))

# # 소수점 특정 자릿수까지 출력(소수점 2번째까지 표시)
# print("{0:.2f}".format(5/3))


# ---------------------------------------------------------------
# 파일 입출력

# 새로 파일을 만들어 쓰기 : w
# score_file = open("score.txt", "w", encoding = "utf8")
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# 쓰던 파일에 이어서 쓰기 : a
# score_file = open("score.txt", "a", encoding = "utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

# 파일을 읽어오기 : r
# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.read())
# score_file.close()

# 한 줄씩 읽어오기 방법1
# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.readline(), end="") # 한 줄씩 읽고, 커서는 다음 줄로 이동
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="") 
# print(score_file.readline(), end="") 
# score_file.close()

# 한 줄씩 읽어오기 방법2
# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line: # line이 없는 경우
#         break
#     print(line, end="")
# score_file.close()

# 한 줄씩 읽어오기 방법3
# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines() # list 형태로 저장
# for line in lines:
#     print(line, end = "")
# score_file.close()


# ---------------------------------------------------------------
# pickle 파일 형태로 저장

# import pickle
# profile_file = open("profile.pickle","wb") # wb : 쓰기목적 & 바이너리
# profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
# print(profile)
# pickle.dump(profile,profile_file) # profile 에 있는 정보를 file 에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb") # rb : 읽기목적 & 바이너리
# profile = pickle.load(profile_file) # file 에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()


# ---------------------------------------------------------------
# with
# pickle을 사용한 불러오기 방법

# import pickle
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# with 만 사용한 파일 쓰기 방법
# with open("study.txt","w",encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with 만 사용한 파일 읽기 방법
# with open("study.txt","r",encoding = "utf8") as study_file:
#     print(study_file.read())


# ---------------------------------------------------------------
# 클래스 class

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음

# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp,damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반모드 / 시즈 모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank_damage)

# __init__ 함수
# class Unit:
#     def __init__(self, name, hp, damage): 
#         self.name = name
#         self.hp =hp
#         self.damage  = damage
#         print("{0} 유닛이 생성 되었습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

# marine1,2 와 같이 Unit클래스로 만들어지는 것들을 객체라고 한다.
# 객체가 생성될 때에는 self를 제외하고 init 함수에 정의된 갯수 만큼 필요하다.
# marine1,2,tank를 Unit클래스의 인스턴스라고 한다.

# marine1= Unit("마린", 40, 5)
# marine2= Unit("마린", 40, 5)
# tank= Unit("마린", 150, 35)

# 멤버 변수

# 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage)) # '.'을 활용해 멤버 변수에 접근

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True

# # 클래스 외부에서 변수를 확장시킬 수 있음
# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))

# 상속
# # 일반 유닛
# class Unit:
#     def __init__(self, name, hp): 
#         self.name = name
#         self.hp =hp

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage): 
#         Unit.__init__(self, name, hp) # 상속을 받는다
#         self.damage  = damage

#     def attack(self, location): # 클래스 내에서 method 앞에 항상 self를 적어주어야 한다.
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage): 
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 메딕 : 의무병

# # 파이어뱃 : 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# ---------------------------------------------------------------
# 다중 상속
# 부모 클래스가 여러 개인 경우

# # 일반 유닛
# # 부모 클래스
# class Unit:
#     def __init__(self, name, hp): 
#         self.name = name
#         self.hp =hp

# # 공격 유닛
# # 자식 클래스
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage): 
#         Unit.__init__(self, name, hp) # 상속
#         self.damage  = damage

#     def attack(self, location): # 클래스 내에서 method 앞에 항상 self를 적어주어야 한다.
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage): 
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
 
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
#         .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit 과 Flyable 을 모두 상속 받음(다중 상속)
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# # 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6 ,5)
# valkyrie.fly(valkyrie.name, "3시")


# ---------------------------------------------------------------
# 메소드 오버라이딩 - fly & move > move로 한 번에!

# # 일반 유닛
# # 부모 클래스
# class Unit:
#     def __init__(self, name, hp, speed): 
#         self.name = name
#         self.hp = hp
#         self.speed = speed

#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
#             .format(self.name, location, self.speed))
# # 공격 유닛
# # 자식 클래스
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): 
#         Unit.__init__(self, name, hp, speed) # 상속
#         self.damage  = damage

#     def attack(self, location): # 클래스 내에서 method 앞에 항상 self를 적어주어야 한다.
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage): 
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 드랍쉽 : 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격X

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
 
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
#         .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit 과 Flyable 을 모두 상속 받음(다중 상속)
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# # 벌쳐 :  지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecruiser.move("9시")

# pass : 함수가 완성된 것처럼 진행시키기


# ---------------------------------------------------------------
# super

# class BuildingUnit(Unit): # Unit 클래스를 상속받음
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # super 를 이용하면 괄호를 붙이고 self는 안붙인다.
#         self.location = location

# super를 사용할 때 문제점
# class Unit:
#     def __init__(self):
#         print("Unit 생성자")

# class Flyable:
#     def __init__(self):
#         print("Flyable 생성자")

# class FlyableUnit(Flyable, Unit):
#     def __init__(self):
#         # super().__init__() 
#         # 2개 이상의 부모 클래스를 다중 상속받으면 맨처음의 클래스만 상속됨.
#         # 아래와 같이 각각 선언해줘야 ㄴ함.  
#         Unit.__init__(self)
#         Flyable.__init__(self)

# # 드랍쉽
# dropship = FlyableUnit()


# ---------------------------------------------------------------
# ---------------------------------------------------------------
# 스타크래프트 시뮬레이션

# from random import *

# # 일반 유닛
# # 부모 클래스
# class Unit:
#     def __init__(self, name, hp, speed): 
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
#             .format(self.name, location, self.speed))

#     def damaged(self, damage): 
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# # 공격 유닛
# # 자식 클래스
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage): 
#         Unit.__init__(self, name, hp, speed) # 상속
#         self.damage  = damage

#     def attack(self, location): # 클래스 내에서 method 앞에 항상 self를 적어주어야 한다.
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 : {2}]"\
#             .format(self.name, location, self.damage))

# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# # 탱크
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동 불가
#     seize_developed = False # 시즈모드 개발 여부
    

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         # 현재 시즈모드일 때 -> 시즈모드 해제
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
 
#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 : {2}]"\
#         .format(name, location, self.flying_speed))

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable): # AttackUnit 과 Flyable 을 모두 상속 받음(다중 상속)
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         self.fly(self.name, location)

# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.clocked = False # 클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True: # 클로킹 모드 -> 모드 해제
#             print("{0} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else: # 클로킹 모드 해제 -> 모드 설정
#             print("{0} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg") # good game
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")


# # 실제 게임 진행
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리 (생성된 모든 유닛 append)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")


# # 공격 모드 준비 (마린 : 스팀팩. 탱크 : 시즈모드, 레이스 : 클로킹)
# for unit in attack_units:
#     if isinstance(unit, Marine): # isinstance : 해당 객체가 어느 클래스의 인스턴스인지 파악
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5,20)) # 공격은 랜덤으로 받음 (5 ~ 20)

# # 게임 종료
# game_over()


# ---------------------------------------------------------------
# 예외처리
# try 구문을 실행 후 에러가 발생하면 except로 넘어간다.

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print(err)


# ---------------------------------------------------------------
# 에러 일부로 발생시키기

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")


# ---------------------------------------------------------------
# 사용자 정의 에러

# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력 값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.") 
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)

# finally : 에러가 있든 없든 무조건 실행
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")



# ---------------------------------------------------------------
# 모듈
# theater_module.py
# # 일반 가격
# def price(people):
#     print("{0}명 가격은 {1}원 입니다.".format(people, people * 10000))

# # 조조할인 가격
# def price_morning(people):
#     print("{0}명 가격은 {1}원 입니다.".format(people, people * 6000))

# # 군인 할인 가격
# def price_soldier(people):
#     print("{0}명 가격은 {1}원 입니다.".format(people, people * 4000))


# 모듈 방법1
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때 가격
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# 모듈 방법2
# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# 모듈 방법3
# from theater_module import *
# # (from random import *)
# price(3)
# price_morning(4)
# price_soldier(5)

# 모듈 방법4
# from theater_module import price, price_morning
# price(5)
# price_morning(6)

# 모듈 방법5
# from theater_module import price_soldier as price
# price(5)


# ---------------------------------------------------------------
# 모듈

# import travel.thailand # (from없이) import 뒤에는 모듈이나 패키지만 적는다.
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand  import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# (from random import *)
# from travel import *
# trip_to = thailand.ThailandPackage()
# trip_to.detail()
# ---------------------------------------------------------------
# 파일 내, 외부에서 실행하는지 검사하기
# thailand.py
# if __name__ == "__main__":
#     print("Thailand 모듈을 직접 실행")
#     print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
#     trip_to = ThailandPackage()
#     trip_to.detail()
# else:
#     print("Thailand 외부에서 모듈 호출")

# practice.py
# import inspect
# import random
# from travel import *

# print(inspect.getfile(random))
# print(inspect.getfile(thailand))


# ---------------------------------------------------------------
# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())


# ---------------------------------------------------------------
# 내장 함수
# list of python builtins

# input : 사용자 입력을 받는 함수
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # 외장 함수
# print(dir())
# import pickle
# print(dir())

# print(dir(random))
# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))


# ---------------------------------------------------------------
# 외장 함수
# Python Module Index

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생서
#     print(folder, "폴더를 생성하였습니다.")
# print(os.listdir())

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일 저장
# print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후


# ---------------------------------------------------------------