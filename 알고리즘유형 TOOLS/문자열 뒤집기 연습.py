a=['a','b','c']
#a.reverse()
#print(a)

#a[:]=a[::-1]
#print(a)

'''
def reversString(str):
    left_idx,right_idx=0,len(str)-1
    while left_idx<right_idx:
        str[left_idx],str[right_idx]=str[right_idx],str[left_idx]
        left_idx+=1
        right_idx-=1
    print(str)

reversString(a)
'''
'''
data = ['1 A', '1 B', '6 A', '2 D', '4 B']
data.sort(key=lambda x:( x[0][1] ))
print(data)
'''
'''
data = ["hanpy 20101213 재미없다 235 재미있다", "hanpy 20101444 재미없다 235 재미있다","hanpy 2010133333 재미없다 235 재미있다","hanpy 2010122213 재미없다 235 재미있다"]
def divide_sentence(listdat):
    str_l,int_l=[],[]
    listdat = listdat.split()[2:]
    print(listdat)
divide_sentence(data)
'''

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
import re
banned='hit'
#정규식 처리 후 , lower()로 소문자로 바꾸고, split()으로 문자열단위로 리스트만듬
word_list=re.sub('[^\w]',' ',paragraph ).lower().split()

#word_list에서 hit이라는 단어를 제외시키고 남은 단어만 words에 담는다.
words=[word for word in word_list if word not in banned]
print(word_list)
print(words)

import collections
# Counter함수로 단어의 빈도수 추출
counts=collections.Counter(words)
print(counts)

#most_common으로 빈도수가 제일 높은 단어를 출력한다.
print(counts.most_common()[0][0])
