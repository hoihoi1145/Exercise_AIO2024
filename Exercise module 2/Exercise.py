#Data Structure - Exercise
from heapq import heappop, heappush
from collections import defaultdict


def test_int_list(w):
    for i in w:
        try:
            int(i)
        except ValueError:
            print('your list must be combined of integers separated by the space')
            return 0
    return 1


def test_int(n):
    try:
        int(n)
    except ValueError:
        print('the number must be integer')
        return 0
    return 1


def test_pos_number(n):
    if test_int(n):
        if int(n) > 0:
            return 1
        else:
            print('the number must be positive integer')
            return 0
    return 0


def hidden_algorithm1(w, k):
    h, d, q, n, a = [], [], defaultdict(int), len(w), -10**99
    if k <= n:
        for i in range(k):
            heappush(h, -w[i])
            a = max(a, w[i])
        d += [a]
        for i in range(k, n):
            heappush(h, -w[i])
            q[w[i-k]] += 1
            while 1:
                a = -heappop(h)
                if a in q:
                    q[a] -= 1
                    if q[a] == 0:
                        del q[a]
                else:
                    d += [a]
                    heappush(h, -a)
                    break
        return d
    else:
        print('The number k must be smaller than the number of numbers in the list')


def hidden_algorithm2(s):
    d = dict()
    for i in s:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    return d


def Levenshtein(s1, s2):
    n, m = len(s1), len(s2)
    prev = list(range(n+1))
    curr = [0]*(n+1)
    for i in range(m):
        curr[0] = i+1
        for j in range(n):
            if s2[i] == s1[j]:
                curr[j+1] = prev[j]
            else:
                curr[j+1] = 1 + min(curr[j], prev[j], prev[j+1])
        prev = curr.copy()
    return curr[n]


def exercise1():
    w = input('Give me a list (For example: 2 3 4): ').split()
    k = int(input('Give me a number k: '))
    if test_int_list(w) and test_pos_number(k):
        w, k = list(map(int, w)), int(k)
        print(hidden_algorithm1(w, k))


def exercise2():
    s = input('Give me a word: ')
    d = hidden_algorithm2(s)
    print(d)


def exercise3():
    file_path = input('Give me file path: ')
    word = input('Give me a word: ')
    with open(file_path, 'r') as file_object:
        content = file_object.read()
        d = hidden_algorithm2(content.split())
        print(d)
        if word not in d:
            print(0)
        else:
            print(d[word])


def exercise4():
    word1 = input('Give me word 1: ')
    word2 = input('Give me word 2: ')
    print(Levenshtein(word1, word2))


def main():
    exercise_number = input('Give me the exercise number(1 | 2 | 3 | 4): ')
    if test_pos_number(exercise_number):
        exercise_number = int(exercise_number)
        match exercise_number:
            case 1:
                exercise1()
            case 2:
                exercise2()
            case 3:
                exercise3()
            case 4:
                exercise4()
            case _:
                print('The exercise number is not existed, try again from 1 to 4')

main()

