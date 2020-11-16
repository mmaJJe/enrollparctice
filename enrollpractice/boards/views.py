from django.shortcuts import render
from .models import EnrollNumber, EnrollRank, EnrollStartTime

def waitBoard(request):
    EnrollStartTimeSet = EnrollStartTime.objects.all()[:1]
    preEnrollStartTime = EnrollStartTimeSet[1]
    nextEnrollStartTime = EnrollStartTimeSet[0]
    nextEnrollNumber = EnrollNumber.objects
    preEnrollResult = EnrollRank.objects
    return render(request, "boards/waitboard.html")

def enrollBoard(request):
    # 신청 하는 경우
    if request.method == "POST":

    # 신청 페이지로 들어오는 경우
    else:

    return render(request, "boards/enrollboard.html")

def rankingBoard(request):
    return render(request, "boards/rankingboard.html")