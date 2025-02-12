# 3.6.9 게임 만들기
'''
3.6.9.게임을 만들기 위해 먼저 사용자 입력과
컴퓨터 입력을 만들어 주고 100까지의 범위를 지정해 준다.
3.6.9일때 사용자의 입력이 True 인지 False 인지 판별하고
True라면 계속 진행을 False라면 문구와 함깨 종료한다.
'''
# 사용자 입력 함수 만들기
def user_input():
    return input("사용자 차례: ")

# 3.6.9 일때 함수 만들기
def check_369(number):
    number = str(number)
    clap_count = 0
    for i in range(len(number)):
        if number[i] == "3" or number[i] == "6" or number[i] == "9":
            clap_count += 1
    return clap_count

# True, False 함수 만들기
def check_correct(now_number, answer):
    clap = check_369(now_number)
    if clap:
        if answer == "짝"*clap:
            print("")
            return True
        else:
            return False
    else:
        return now_number == answer