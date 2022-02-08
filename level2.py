

def print_sort_words(s_):
    for i in range(0, len(s_)):
        print(s_[i])

def get_num_words():
    n = int(input())
    word_list = []
    for _ in range(0, n):
        word = input()
        word_list.append(word)
    return word_list

def lsort(word_list):
    len_word_ = []
    for word in word_list:
        len_word_.append([len(word), word])
    len_word_.sort()
    return len_word_
    # return [l_w[1] for l_w in le)n_word_]

def dsort(len_word_list):
    def _count_same(n, len_word_):
        cnt = 0
        for len_word in len_word_:
            if n == len_word[0]:
                cnt += 1
        return cnt

    def _extract(l, w_):
        ext_ = []
        for w in w_:
            if w[0] == l :
                ext_.append(w)
        return ext_

    def dict_sort(w_):
        d_sort = []
        for w in w_:
            d_sort.append(w[1])
        d_sort.sort()
        return(d_sort)

    # for i, len_word in enumerate(len_word_list):
    for i in range(len(len_word_list)):
        len_word = len_word_list[i]
        length = len_word[0]
        cnt = _count_same(length, len_word_list)
        if cnt > 1 :
            ex_list = _extract(length, len_word_list)
            d_sort_list = dict_sort(ex_list)

            for _ in range(cnt):
                len_word_list.pop(i)

            for d_sort_i, d_sort in enumerate(d_sort_list):
                len_word_list.insert(i+d_sort_i, [length, d_sort])
            i = i + (cnt-1)


def dsort1(len_word_list):
    def _count_same(n, len_word_):
        cnt = 0
        for len_word in len_word_:
            if n == len_word[0]:
                cnt += 1
        return cnt

    def _extract(l, w_):
        ext_ = []
        for w in w_:
            if w[0] == l :
                ext_.append(w)
        return ext_

    def dict_sort(w_):
        d_sort = []
        for w in w_:
            d_sort.append(w[1])
        d_sort.sort()
        ret_ = [[len(s), s] for s in d_sort]
        return(ret_)



    def extract_same_length(c, l_w_):
        ret_ = []
        try:
            for i in range(c):
                l_w = l_w_.pop()
                ret_.append(l_w)
        except:
            print('extract_same_lengt except')
        return(ret_)


    ret_ = []
    len_word_list.reverse()
    while True:
        try:
            cnt = _count_same(len_word[0], len_word_list)
            len_word = len_word_list.pop()
            if cnt == 1:
                ret_.append(len_word)
            else:
                # pass
                extract_same_length_word_ = extract_same_length(cnt, len_word_list)
                d_sort_ = dict_sort(extract_same_length_word_)
                ret_.extend(d_sort_)
        except IndexError:
            break


def word_sort():
    word_list = get_num_words()
    word_l_sorted = lsort(word_list)
    word_dict_sorted = dsort1(word_l_sorted)
    print_sort_words(word_dict_sorted)




if __name__ == '__main__':
    word_sort()




