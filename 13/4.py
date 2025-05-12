

# 입력예시
# "(()())()"
# 출력예시
# "(()())()"

# +

# 입력예시
# ")("
# 출력예시
# "()"


# 균형잡힌 문자열 = ( 와 )의 개수가 맞는 문자열
# 올바른 문자열 = ( 와 )의 개수 그리고 배열이 맞는 문자열

# "균형잡힌 괄호 문자열"의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            print("balanced i :",p[i])
            count += 1
        else:
            count -= 1
        # len(p) 만큼 코드를 계속 도는게 아닌, 어느순간 count = 0 이 되면 i를 반납하고 종료되는 코드
        if count == 0:
            return i
# 위 코드의 경우 ( 의 개수를 +1 
# ) 의 개수를 -1 을 하여 문자열 내의 ( 과 )의 총 개수를 의미하는
# count를 나타낸다.
# "올바른 괄호 문자열"인지 판단

# 밑에 check_proper은 올바른 괄호 문자열의 특성만 파악하면 심플하다
# 올바른 괄호 문자열은 1. '(' 과 ')' 의 갯수가 맞으며 2. '(' 가 먼저 나오고 그 다음에 ')'
# 오면 올바른 문자열이라고 할 수 있다. 
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            print("check i :",i)
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 False 반환 설명은 solution 위 참조조
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환


# 닫는 괄호 )가 먼저 나오는 경우
# 예: ")(", ")()("
# 여는 괄호 (보다 닫는 괄호 )가 더 많은 경우
# 예: "(()))", ")()())"
# 여는 괄호 (의 개수가 더 많은 경우 (문자열이 끝났을 때 count > 0)
# 예: "((()", "(()("


def solution(p):
    answer = ''
    if p == '':
        return answer
    print("\n")
    print("########solution 문 진입##########")
    print("p :",p)
    print("balanced_index(p) :",balanced_index(p))
    index = balanced_index(p)
    print("index :",index)
    print("p[:index + 1] :",p[:index + 1])
    print("p[index + 1:] :",p[index + 1:])
    u = p[:index + 1]
    v = p[index + 1:]
    print("u:",u)
    print("v:",v)
    # "올바른 괄호 문자열"이면, v에 대해 함수를 수행한 결과를 붙여 반환
    print("\n")
    if check_proper(u):
        print("\n")
        print("check 문 도입 아래의 solution문 시작")
        print("solution(v) :",solution(v))
        # solution(v) : () 가 나온 이유는 u = (()())  v =  () 에서 v를 넣었을때 추출 된 값이다.
        print("check 문 도입 아래의 check문 시작")
        print("check_proper(u) :",check_proper(u))
        print("u :",u)
        answer = u + solution(v)
        print("87 answer :",answer)
        print("\n")
    # "올바른 괄호 문자열"이 아니라면 아래의 과정을 수행
    else:
        print("\n")
        print("#######else문 진입########")
        # 이 파트는, 괄호가 안맞을시에 이를 수정해주는 파트
        # 예를 들어 ))(( 가 있다고 할 시 ,
        # 아래의 
        # answer = '('
        # answer += solution(v)
        # answer += ')'
        # 구문을 통해 맨처음과 마지막 ) 과 ( 는 ( 그리고 )로 대체된다.
        # 그리고 u = list(u[1:-1]) 구문을 통해
        # 내부의 값도 ()() 반대의 값이 되어 결과적으로 올바른 괄호로 바뀌게 되는것것
        

        print("solution(v) :",solution(v))
        print("105 v :",v)
        answer = '('
        answer += solution(v)
        answer += ')'
        print("u :",u)
        print("u[1:-1] :",u[1:-1]) # [1:-1], 두번째 요소부터 마지막 전 요소까지 슬라이싱싱
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거 #1.
        print("112 u :",u)
        print("\n")
        # 예를들어 ))(( 라고하자 그러면 일단 solution(v)는 그냥 빈칸이 되어
        #  answer  = () 가 된다.
        # ) 과 ( 를 추가하는 과정을 통해() 가 된다 이후 u = ))(( 에서서
        # 일단 위의 과정을 통해 )(만 남게
        # 되며, ) => ( 가 되고
        # ) => ( 가 된다. 
        # 마지막으로 () (정상적인 괄호) 가 생성된다.
        # 그러면 answer와 u를 합하여 최종적으로 ()() 옳바른 괄호가 생성된다.
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        print("u :",u)
        print("126 answer :",answer)
        answer += "".join(u)
        print("128 answer :",answer)
    return answer

# (()())()
# Cha = input() # input() 문장열 형태로 받는다
Cha = "(()())))(("
print(solution(Cha))


#1.
# u[1:-1] 이 의미하는 바는 0번째가 아닌 1번째부터 -1(마지막요소) 전까지 데이터들을 가져온다는 의미
# 쉽게 말해 처음데이터랑 마지막데이터를 제외한 값만 가져온다다