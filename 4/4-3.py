# 8 x 8 좌표평면
# 현재 나이트의 위치 입력받기
input_data = input()
# y값, x값
row = int(input_data[1]) #ex) a1 입력 시 1이라 data[1]
# ord 함수 : 문자를 아스키코드로 변환
# 아스키코드 - a값 + 1 : a = 1, b = 2 ... 변환
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 장향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, -2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인

result = 0
for step in steps:
  #이동하고자 하는 위치 확인
  next_row = row + step[0]
  next_column = column + step[1]

  if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8 :
    result += 1

print(result)
