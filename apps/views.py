from django.shortcuts import render
from models import Grade
# Create your views here.


def upload_grade(username, grade):
    try:
        Grade.objects.create(username=username,grade=grade)
    except Exceptions as error:
        return {'error':'数据插入失败.'}
    return {'message':'数据插入成功.'}


def search_grade(username,rank_start, rank_end):
    search_query = Grade.object.filter().order_by('-grade')[rank_start:rank_end]
    user_best_grade = Grade.object.filter(username=username).order_by('-grade')[1:]

    return {'rank_query': search_query, 'user_best_grade': user_best_grade}
