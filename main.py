import time


def main():
    print('강한친구 대한육군')
    print('강한친구 대한육군')





def print_cat():
    print("\\    /\\")
    print(" )  ( ')")
    print("(  /  )")
    print(" \\(__)|")

def print_dog():
    print("|\\_/|")
    print("|q p|    /}")
    print('( 0 )"""\\')
    print('|"^"`    |')
    print('||_/=\\\\__|')
    

def word_test():
    word = input()

    s = time.time()
    word = word.upper()
    e = time.time()
    print(e-s)
    ch_ = list(word)
    ch__ ={}
    for ch in ch_:
        ch__[ch] = word.count(ch)

    max_value = 0
    max_ch = ''
    for key in ch__.keys():
        cur_value = ch__[key]
        if max_value < cur_value :
            max_value = cur_value
            max_ch = key
        else:
            if max_value == cur_value :
                max_ch = '?'

    print(max_ch)

from string import ascii_uppercase


def word_test1():
    word = input()
    word = word.upper()
    alphabet__ = {}
    for ch in list(ascii_uppercase):
        alphabet__[ch] = 0

    for idx in range(0, len(word)):
        char = word[idx]
        alphabet__[char] += 1

    max_value = 0
    max_ch = ''
    for key in alphabet__.keys():
        cur_value = alphabet__[key]
        if max_value < cur_value :
            max_value = cur_value
            max_ch = key
        else:
            if max_value == cur_value :
                max_ch = '?'

    print(max_ch)

def word_test2():
    word = input()
    word = word.upper()
    alphabet__ = {}
    ascii_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for ch in list(ascii_upper):
        alphabet__[ch] = 0

    for idx in range(0, len(word)):
        char = word[idx]
        alphabet__[char] += 1

    max_value = 0
    max_ch = ''
    for key in alphabet__.keys():
        cur_value = alphabet__[key]
        if max_value < cur_value :
            max_value = cur_value
            max_ch = key
        else:
            if max_value == cur_value :
                max_ch = '?'

    print(max_ch)

def word_test3():
    word = input()
    word = word.upper()

    word_set = set(word)

    word_ = list(word)
    word_cnt = []
    word_set_ = list(word_set)
    for ch in word_set_ :
        word_cnt.append(word_.count(ch))

    max_cnt = max(word_cnt)

    if word_cnt.count(max_cnt) >= 2:
        max_char = '?'
    else:
        idx = word_cnt.index(max_cnt)
        max_char = word_set_[idx]

    print(max_char)


def nums_compare():
    a, b = map(int, input().split())
    if a > b : ret = '>'
    if a < b : ret = '<'
    if a == b : ret = '=='

    # print(a, b)
    print(ret)

def 평균():
    s_num = int(input())
    s_val_ =list(map(int, input().split()))
    max_score = max(s_val_)
    fake_score = lambda a: a / max_score * 100
    e_val_ =list(map(fake_score, s_val_))
    print(e_val_)
    # for s_val in s_val_:
    #     s_val
    print(e_val_)
    fake_average = sum(e_val_)/s_num
    print(fake_average)

def print_star(n):
    def print_line_star(n):
        star = '*'* n
        print(star)

    for i in range(1,n+1):
        print_line_star(i)
        # print()

def print_stars():
    n = int(input())
    print_star(n)

def print_back_star(n):
    def print_line_star_with_right(n, max_star):
        star = ' '*(max_star-n)+'*'*n
        print(star)

    for i in range(1, n+1):
        print_line_star_with_right(i, n)

def print_back_stars():
    n = int(input())
    print_back_star(n)


def 검증수():
    five_digit_ = list(map(int, input().split()))

    five_digit_square =list(map(lambda x : x ** 2, five_digit_))
    eval_digit = sum(five_digit_square)%10

    print(eval_digit)

def max_val_index():
    # n_ = list(map(int, input().split()))
    n_ = []
    for i in range(1, 10):
        n_.append(int(input()))
    max_val = max(n_)
    max_index = n_.index(max_val)
    max_index = max_index + 1

    print(max_val)
    print(max_index)

def count_0_9():
    a = int(input())
    b = int(input())
    c = int(input())

    abc = a * b * c
    # abc_str = ''+abc
    abc_str = str(abc)

    digit_count_ = []
    for i in range(0, 10):
        digit_count_.append(abc_str.count(str(i)))

    for digit in digit_count_:
        print(digit)
    # pp = lambda x : print(x)
    # map(pp, digit_count_)

    

def 문자열반복():
    t = int(input())

    for _ in range(0, t):
        r, s = input().split()
        r_int = int(r)
        s_str = s
        s_list = list(s_str)

        ret = str()
        for s_single in s_list:
            ret += s_single * r_int

        print(ret)


def 문자열반복1():
    t = int(input())

    r_s_ = []
    for _ in range(0, t):
        r, s = input().split()
        r_int = int(r)
        s_str = s
        s_list = list(s_str)
        r_s_.append([r_int,s_list])



    for r_s in r_s_:
        s_list = r_s[1]
        r_int = r_s[0]

        ret = str()
        for s_single in s_list:
            ret += s_single * r_int

        print(ret)


def gugudan():
    n = int(input())

    for i in range(1, 10):
        print("{} * {} = {}".format(n, i, n*i))


def print_N():
    n = int(input())

    for i in range(1, n+1):
        print(i)

def print_NN():
    n = int(input())

    for i in range(n, 0, -1):
        print(i)

def 윤년():
    n = int(input())

    if n % 4 != 0 :
        ret = 0
    else:
        if n % 100 !=0 :
            ret = 1
        else:
            if n % 400 == 0 :
                ret = 1
            else:
                ret = 0
    print(ret)

class HH_MM_Calculator:
    def __init__(self):
        pass
    def __init__(self, hh, mm):
        self.hh = hh
        self.mm = mm
    def minus(self, m_hh, m_mm):
        if self.mm >= m_mm :
            self.mm -= m_mm
        else:
            self.mm = 60 + self.mm - m_mm
            if self.hh > 0 :
                self.hh = self.hh - 1
            else:
                self.hh = 23

def hhmm_minus():
    hh, mm = map(int, input().split())
    hhmm = HH_MM_Calculator(hh, mm)

    hhmm.minus(0, 45)
    print(hhmm.hh, hhmm.mm)


def 상근이숫자비교():
    def num_back(num):
        num_str_ = list(num)
        back_num_str_ = num_str_.reverse()
        back_num_str_ = num_str_
        back_num_str = ''.join(back_num_str_)
        return int(back_num_str)

    a, b = input().split()

    back_a = num_back(a)
    back_b = num_back(b)

    if back_a > back_b :
        big_num = back_a
    else:
        big_num = back_b

    print(big_num)



def 상근이숫자비교1():
    def num_back(num):
        num_str_ = list(num)
        back_num_str_ = num_str_.reverse()
        back_num_str_ = num_str_
        back_num_str = ''.join(back_num_str_)
        return int(back_num_str)

    def num_back1(num):
        back_num_str = num[::-1]
        return int(back_num_str)

    def num_back2(num):
        back_num_str = ''.join(reversed(num))
        return int(back_num_str)

    a, b = input().split()

    back_a = num_back1(a)
    back_b = num_back2(b)

    if back_a > back_b :
        big_num = back_a
    else:
        big_num = back_b

    print(big_num)


def 음계():
    a_ = list(input().split())

    asc = ['1', '2', '3', '4', '5', '6', '7', '8']
    des = asc[::-1]

    if a_ == asc :
        ret = 'ascending'
    else:
        if a_ == des :
            ret = 'descending'
        else:
            ret = 'mixed'

    print(ret)





    


if __name__ == '__main__':
    # main()
    # print_cat()
    # print_dog()
    # word_test3()
    # nums_compare()
    # 평균()
    # print_stars()
    # print_back_stars()
    # 검증수()
    # max_val_index()
    # count_0_9()
    # 문자열반복1()
    # gugudan()
    # print_N()
    # print_NN()
    # 윤년()
    # hhmm_minus()
    # 상근이숫자비교1()
    음계()



