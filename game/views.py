from django.shortcuts import render
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')

def opens(request):
    people = [
        '박효진', '정사랑', '최수정', '배진경', '박채연', '이지은', 
        '노신욱', '정지성', '기호정', '박선영', '조경진', '박우민', '정현지', '정재윤', '장진우',
        '장승욱', '김경일', '김경우', '이동완', '김병관', '안원일'
    ]
    group = random.sample(people, len(people))
    team = {
        'teamA_first': ['양이안', '김여빈'],
        'teamA_second': ['김광진', '김정한'],
        'teamA_third': ['선용원', '류제선'],
        'teamB_first': ['이승원'],
        'teamB_second': ['송윤제','나정훈'],
        'teamB_third': ['김재승','김유정'],
    }
    for i in range(len(people)):
        if i % 6 == 0:
            team['teamB_first'].append(group[i])
        elif i % 6 == 1:
            team['teamB_second'].append(group[i])
        elif i % 6 == 2:
            team['teamA_third'].append(group[i])
        elif i % 6 == 3:
            team['teamA_first'].append(group[i])
        elif i % 6 == 4:
            team['teamA_second'].append(group[i])
        elif i % 6 == 5:
            team['teamB_third'].append(group[i])
    
            
    context = {
        'team': team,
        'group': ', '.join(group),
    }
    return render(request, 'game.html', context)