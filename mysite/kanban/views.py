# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import View
from django.http import QueryDict

from kanban.models import User, Board, List, Card

# import json
from CustomLog import CustomLog
# Create your views here.

custom_log = CustomLog("kanban_views")
log = custom_log._get_logger()


class BoardView(View):
    def get(self, request, *args, **kwargs):
        queryset = Board.objects.all()

    def post(self, request, *args, **kwargs):
        pass


class ListView(View):
    def get(self, request, *args, **kwargs):
        queryset = List.objects.all().filter(board_id=Board.objects.get(id=1))

        log.debug("queryset : {}".format(queryset))

        return queryset

    def post(self, request, *args, **kwargs):
        log.debug("List View Post")
        order_num = request.POST.get('order_num')

        board_obj = Board.objects.get(id=1)
        list_data = List.objects.create(order_num=order_num,
                                        title="List",
                                        board_id=board_obj)

        content = {'list_id': list_data.id}
        return JsonResponse(content)

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        log.debug("List View Delete")

        # delete method를 wsgi에서 지원하지 않아서 QueryDict를 이용하여 delete method사용
        delete = QueryDict(request.body)

        list_id = delete.get('list_id')

        List.objects.all().filter(id=list_id).delete()

        return HttpResponse(status=204)


class CardView(View):
    def get(self, request, *args, **kwargs):
        log.debug("args: {}".format(False))

        '''
        내부(index method)에서의 호출과 외부(Web)에서의 호출이 발생하기에
        내부 호출의 경우 arg에 True 값을 같이 전달하여, 내/외부를 구분
        내부호출:
            card 전체의 데이터를 추출
        외부호출:
            card_id/list_id 에 따른 특정 card 하나만을 호출
        '''
        if (len(args) > 0):
            call_check = args[0]
        else:
            call_check = False

        if call_check:
            log.debug("type: {}".format("True"))
            queryset = Card.objects.all().filter(board_id=Board.objects.get(id=1))

            log.debug("queryset : {}".format(queryset))
            return queryset
        else:
            log.debug("type: {}".format("False"))
            card_id = request.GET.get('card_id')
            list_id = request.GET.get('list_id')

            log.debug("card_id : {}, list_id : {}".format(card_id, list_id))

            queryset = Card.objects.all().get(id=card_id, list_id=list_id)

            content = {'title': queryset.title,
                        'description': queryset.info,
                        'tag': queryset.tag}

            log.debug("content: {}".format(content))

            return JsonResponse(content)

    def post(self, request, *args, **kwargs):
        log.debug("Card View Post")

        order_num = request.POST.get('order_num')
        title = request.POST.get('title')
        list_id = request.POST.get('list_id')

        # card의 정렬 순서를 만들기 위한 용도의 코드, 하지만 정렬기능 미구현
        if order_num is None:
            order_num = 1
        else:
            order_num += 1

        log.debug("order_num :{}, title:{}, list_id:{}".format(order_num,
                                                                title,
                                                                list_id))

        board_obj = Board.objects.get(id=1)
        list_obj = List.objects.get(id=list_id)

        card_data = Card.objects.create(order_num=order_num,
                                        title=title,
                                        list_id=list_obj,
                                        board_id=board_obj)

        content = {'card_id': card_data.id}

        return JsonResponse(content)

    def put(self, request, *args, **kwargs):
        put = QueryDict(request.body)

        card_id = put.get('card_id')
        list_id = put.get('list_id')
        title = put.get('title')
        description = put.get('description')
        tag = put.get('tag')

        list_obj = List.objects.get(id=list_id)
        Card.objects.filter(id=card_id, list_id=list_obj).update(
                                                        title=title,
                                                        info=description,
                                                        tag=tag)

        return HttpResponse(status=204)

    def delete(self, request, *args, **kwargs):
        # delete method를 wsgi에서 지원하지 않아서 QueryDict를 이용하여 delete method사용
        delete = QueryDict(request.body)

        card_id = delete.get('card_id')
        list_id = delete.get('list_id')

        log.debug("Card View Delete card_id:{}, list_id:{}".format(card_id,
                                                                    list_id))

        list_obj = List.objects.get(id=list_id)

        Card.objects.all().filter(id=card_id, list_id=list_obj).delete()

        return HttpResponse(status=204)


def index(request):
    log.debug("index call")

    '''
    처음 화면을 호출할때 List/Card의 데이터를 가져와서 template 화면에 전
    '''
    list_view = ListView()
    card_view = CardView()

    lists = list_view.get(request)
    cards = card_view.get(request, True)

    content = {'lists': lists, 'cards': cards}
    return render(request, 'kanban/index.html', content)
