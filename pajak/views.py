from django.shortcuts import render
from django.http import HttpResponse

import time


def coba(request):
    now = time.ctime()

    tm = "<html><body><h1>My name is <i>{name}</i></h1><h2>It is now {waktu}</h2><hr></body></html>"
    hasil = tm.format(name = "agos", waktu = now)
    return HttpResponse(hasil)
