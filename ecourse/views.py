from django.shortcuts import render
from .models import Accounts,Courses,Videos,Comments
from django.contrib.auth.decorators import login_required


def start(request):
    return render(request,'login.html')
def login(request):
    if request.method=='POST':
        user_form=request.POST
        print(user_form)
        Courses(cname="java",description="learn java",url="http://127.0.0.1:8000/courses/java").save()
        Courses(cname="py",description="learn python",url="http://127.0.0.1:8000/courses/py").save()
        Courses(cname="cpp",description="learn c++",url="http://127.0.0.1:8000/courses/cpp").save()
        print("vid save")
        c=Courses.objects.get(cname="java")
        print(c)
        Accounts(user_form["Username"],user_form["Password"],user_form["Email"]).save()
       # UserProfile('1001',password,datetime.now(),False,False,all,username,False,False,False,datetime.now(),phoneno).save()
        present_acc=Accounts(user_form["Username"],user_form["Password"],user_form["Email"])
        print("Saved")
    return render(request,'login.html')
def signup(request):
    return render(request,'signup.html')

def courses(request):
    if request.method=='POST':
        log=request.POST
        print(log)
        if Accounts.objects.filter(email=log["email"],password=log["password"]).exists() :
            present_acc=Accounts.objects.get(email=log["email"])
            courses=Courses.objects.all()
            acc=Accounts.objects.all()
            print(acc)
            print("courses")
            print(courses)
            for i in courses:
                print(i)
            print(present_acc.name,present_acc.email)
            sendd={'name':present_acc.name,'email':present_acc.email}
            print(sendd)
            return render(request,'courses.html', {'name':present_acc.name,'email':present_acc.email,'courses':courses})
        else:
            return render(request,'login.html')

@login_required
def getvid(request,cname):
    print(cname)
    c=Courses(cname=cname)
    va=Videos.objects.all()
    print(va)
    v=Videos.objects.filter(course=c)
    print(v)
    if request.method=='POST':
        log=request.POST
        print("hello")
        print(log)
    return render(request,'videos.html',{'vlist':v})


@login_required
def playvid(request,cname,vno):
    if request.method=='POST':
        log=request.POST
        print(log)
        co=Courses.objects.get(cname=cname)
        vi=Videos.objects.get(course=co,vno=vno)
        Comments(vid=vi,cmt=log['cmt']).save()

    vidurl="https://codaglobal.s3.us-east-2.amazonaws.com/"
    vidurl+=cname+"/"+vno+".mp4"
    print(vidurl)
    v=Videos.objects.filter(course=cname)
    c=Courses(cname=cname)
    print(c)
    vc=Videos.objects.filter(course=cname,vno=vno)
    print(vc)
    for i in vc:
        vidd=i
        break
    print(vidd)
    cmts=Comments.objects.filter(vid=vidd)
    print(cmts)    
    return render(request,'vidcmt.html',{'url':vidurl,'vl':v,'cmnt':cmts})

# Create your views here.
