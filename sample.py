import random

people = [
    '김유정', '박효진', '정사랑', '최수정', '배진경', '박채연', '김여빈', '선용원', '이지은', '양이안',
    '송윤제', '노신욱', '정지성', '기호정', '박선영', '조경진', '박우민', '정현지', '정재윤', '장진우',
    '박성연', '장승욱', '류제선', '이승원', '김광진', '김경일', '김정한', '김경우', '이도완', '김재승', '김병관'
]

group = random.sample(people, 31)
print(type(group))