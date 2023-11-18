# #. 1. 말 따라하기
# while True:
#     talk = input("나: ")
#     print("앵무새: ", talk)
#     if talk == "":
#         break

# # 2. 챗봇 음식주문
# while True:
#     food = input("챗봇: 무슨 음식을 주문하시겠어요? ")
#     if food == "":
#         break
#     print("챗봇: ", food, "를 주문하시는군요, 몇 인분요?")
#     dish = int(input("음식 수량: "))
#     print("챗봇: ", food, "를", dish, "인분 주문하시는군요.")
#     print("챗봇: 총 주문 금액은", dish * 10000, "원 입니다.")

# 3. 숫자 맞추기
# import random
# # com = 78
# com = random.randrange(1, 100)

# while True:
#     num = int(input("1~100 사이 숫자를 입력해주세요 : "))
#     if com == num :
#         print("정답")
#         break
#     elif com > num :
#         print("Up")
#     elif com < num :
#         print("Down")

# # 4. 축구 승부차기
# import random
# # -1 컴퓨터가 막을 곳을 리스트에 저장(변수) "왼쪽", "중앙", "오른쪽"
# option = ["왼쪽", "중앙", "오른쪽"]
# # -2 컴퓨터가 막을 방향을 선택한다.
# select = random.choice(option)
# # -3 내가 공을 찰 방향을 입력한다.
# user_select = input('어느 방향으로 막을까요?("왼쪽", "중앙","오른쪽")')
# # -4 만약에 같은 방향이라면 "골이 막힘"
# if select == user_select :
#     print("골이 막힘")
# # -5 아니라면 "골"
# else :
#     print("골")

# 5. 함수
# a, b = input().split()
# a = int(a)
# b = int(b)

# 정의, 호출
# def add(num1, num2):
#     # total = num1 + num2
#     # return total
#     return num1 + num2

# a, b = map(int, input().split())
# # rst = add(a, b)
# # print(a, "+", b, "=", a+b)
# # print(f"{a}+{b}={a+b}입니다")

# print(a, "+", b, "=", add(a+b))
# print(f"{a}+{b}={a+b}입니다")