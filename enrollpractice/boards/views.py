from django.shortcuts import render, redirect
from .models import EnrollNumber, EnrollRank, EnrollStartTime

def waitBoard(request):
    user = str(request.user)
    EnrollStartTimeSet = EnrollStartTime.objects.order_by("-pk")[:2]
    # 처음 수강신청 때 이전 수강신청시간이 없을 경우 빈 리스트 출력
    try:
        preEnrollStartTime = EnrollStartTimeSet[1]
    except IndexError as e:
        preEnrollStartTime = []
        print("첫 수강신청임", e)

    try:
        preEnrollNumbers = EnrollNumber.objects.filter(enrollStartTime=preEnrollStartTime)
    except TypeError as e:
        preEnrollNumbers = []
        print("첫 수강신청임", e)

    # 다음 수강신청시간,번호 (서버 시작할 때 생성됨)
    try:
        nextEnrollStartTime = EnrollStartTimeSet[0]
    except IndexError as e:
        nextEnrollStartTime = []
        print("서버 켜지는 중", e)

    try:
        nextEnrollNumbers = EnrollNumber.objects.filter(enrollStartTime=nextEnrollStartTime)
    except TypeError as e:
        nextEnrollNumbers = []
        print("서버 켜지는 중", e)


    context = { "nextEnrollStartTime":nextEnrollStartTime,
                "nextEnrollNumbers":nextEnrollNumbers,
                "preEnrollNumbers":preEnrollNumbers, }

    return render(request, "boards/waitboard.html", context)

def enrollBoard(request):
    nowEnrollStartTime = EnrollStartTime.objects.order_by("-pk")[:1]
    nowEnrollStartTime = nowEnrollStartTime[0]
    nowEnrollNumbers = EnrollNumber.objects.filter(enrollStartTime=nowEnrollStartTime)
    context = {"nowEnrollNumbers" : nowEnrollNumbers}
    return render(request, "boards/enrollboard.html", context)

def enroll(request):
    EnrollStartTimeSet = EnrollStartTime.objects.order_by("-pk")[:1]
    enrollStartTime = EnrollStartTimeSet[0]

    applynumber = request.POST['applyNumber']
    enrollNumber = EnrollNumber.objects.get(number=applynumber)

    rankingList = EnrollRank.objects.filter(enrollNumber=enrollNumber,
                                            enrollStartTime=enrollStartTime)

    rank = len(rankingList) + 1

    # 소셜 로그인 구현 한 뒤 'blue' 부분을 유저정보를 담고 있는 캐쉬로 바꿔줘야함
    applied = EnrollRank.objects.filter(enrollNumber=enrollNumber,
                                        enrollStartTime=enrollStartTime,
                                        user='blue')
                                        
    if applied.exists():
        return redirect("enrollBoard")
    else:
        # 소셜 로그인 구현 한 뒤 'blue' 부분을 유저정보를 담고 있는 캐쉬로 바꿔줘야함
        enroll = EnrollRank(enrollNumber=enrollNumber,
                            rank= rank, 
                            enrollStartTime=enrollStartTime,
                            user="blue")
        enroll.save()
        return redirect("enrollBoard")


def rankingBoard(request):
    # 소셜 로그인 구현 한 뒤 'blue' 부분을 유저정보를 담고 있는 캐쉬로 바꿔줘야함
    myRanks = EnrollRank.objects.filter(user="blue")
    print(myRanks)
    context = {"myRanks": myRanks}
    return render(request, "boards/rankingboard.html", context)