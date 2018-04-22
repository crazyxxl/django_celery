# from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
#
# from utils.jwtutils import generate_token, ver_token
#
#
# class SimpleMiddleware():
#     def __init__(self):
#         pass
#
#     def request_filter(self, request):
#
#         token = request.META.get("token")
#         ver_token(token)
#         if request.path != '/login/' and request.path != '/Web/CheckCode/':
#             if request.session.get('user', None):
#                 pass
#             else:
#                 return HttpResponseRedirect('/login/')
