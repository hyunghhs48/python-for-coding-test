# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

result = 0

#한 줄씩 입력받아 확인하기
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수 찾기'
  min_value = 10001 #문제 조건에서 list 내 수 10000 이하 (아래에서 비교하기 위해 data에 없는 값으로 초기화)
  for a in data:
    min_value = min(min_value,a) #min_value 값과 data의 a값 비교해서 더 작은 값 min_value에 저장
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result)
