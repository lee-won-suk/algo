#1027 : [기초-입출력] 년월일 입력 받아 형식 바꿔 출력하기
year, month, day = input().split(".")
print(day.zfill(2), month.zfill(2), year.zfill(4), sep="-")
