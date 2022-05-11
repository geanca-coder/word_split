from itertools import combinations

''' 
    Jose Geancarlo Bermudez Blandon
    Pros
    Avoids loops by reusing python built in functions making it more efficient!.
    Uses combinations instead of permutations since permutations are more time consuming in running time!.
    Shortness!
    Easy to understand!
'''


def word_split(str_arr):
    word = str_arr[0]
    lst = str_arr[1].split(',')
    pair = list(filter(lambda c: sorted(c[0] + c[1]) == sorted(word), list(combinations(lst, 2))))
    pair = pair[0] if len(pair) > 0 else []
    if pair:
        if word[:len(pair[0])] == pair[0]:
            return pair[0] + ',' + pair[1]
        elif word[:len(pair[1])] == pair[1]:
            return pair[1] + ',' + pair[0]
    return 'Not Possible'


print(word_split(["hellocat", "apple,bat,cat,goodbye,hello,yellow,why"]))
print(word_split(["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]))
print(word_split(["abcgefd", "a,ab,abc,abcg,b,c,dog,e,efd,zzzz"]))
