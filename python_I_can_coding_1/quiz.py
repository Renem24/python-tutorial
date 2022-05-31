# Quiz3 : 비밀번호 생성하기 
# url = "http://naver.com"

# my_str = url.replace("http://", "")
# my_str = my_str[:my_str.index(".")] 

# password = my_str[:3] + str(len(my_str))+str(my_str.count("e"))+"!"

# print("{0}의 비밀번호는 {1}입니다.".format(url,password))


# Quiz4 : 당첨자 추첨하기
# from random import*

# users = range(1, 21)
# # 1부터 20까지 숫자
# # print(type(users))
# users = list(users)
# # print(type(users))
 
# print(users)
# shuffle(users)
# print(users)

# winners = sample(users,4)

# print("--당첨자 발표--")
# print("치킨 당첨자 : {0}" .format(winners[0]))
# print("커피 당첨자 : {0}" .format(winners[1:]))
# print("--축하합니다--")

# Quiz5 : 5~15분 이내의 탑승시간을 가지는 승객 선택하기
# from random import *
# matching_num = 0
# for passenger in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         match = "O"
#         matching_num += 1
#     else:
#         match = " "
#     print("[{0}] {1}번째 손님 (소요시간 : {2}분)".format(match,passenger,time))
# print("총 탑승 승객 : {0} 분".format(matching_num))


# Quiz6 : 표준체중 측정하기
# def std_weight(height, gender):
#     if gender == "남자":
#         weight = round((height/100)*(height/100)*22,2)
#         print("키 {0}cm 남자의 표준체중은 {1}kg 입니다.".format(height,weight))
#     else: 
#         weight = round((height/100)*(height/100)*21,2)
#         print("키 {0}cm 여자의 표준체중은 {1}kg 입니다.".format(height,weight))

# height = 181
# gender = "남자"

# std_weight(height, gender)


# Quiz7 1 ~ 50주차까지의 보고서 작성하기

# for i in range(1,51):
#     with open(str(i) + "주차.txt","w",encoding = "utf8") as report_file:
#         # 질문? 
#         # 왜"{0}주차.txt".format(i)로 하지 않는가?
#         report_file.write("- {0} 주차 주간보고 -".format(i))
#         report_file.write("\n부서 :")
#         report_file.write("\n이름 :")
#         report_file.write("\n업무 요약 :")

# Quiz8 부동산 프로그램 작성하기

# class House:
#     # 매물 초기화
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.competion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type,\
#             self.deal_type, self.price,  self.competion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50", "2000년")
# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}개의 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# Quiz9 자동 주문 시스템 제작하기(예외처리)
# class SoldOutError(Exception):
#     pass
# chicken = 10
# waiting = 1 # 홀 안에는 현재 만석, 대기번호 1부터 시작
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))    
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때    
#             print("재료가 부족합니다.")    
#         elif order <= 0:
#             raise ValueError       
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))      
#             waiting += 1    
#             chicken -= order       
#         if chicken == 0:
#             raise SoldOutError    
#     except ValueError:
#             print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#             print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#             break        

# Quiz10 프로젝트 내에 나만의 시그니처를 남기는 모듈 만들기
import byme
byme.sign()
