from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    
    out_data={
            "names":["sai","jay","shiva"],
            "age":[25,40,67],
            }
    print(type(request))
    return render(request,"index.html",out_data)

def home2(request):
    va=["sai","jay","shiva"]
    out_data={
            "names":["sai","jay","shiva"],
            "age":[25,40,67],
            }
    print(type(out_data['names']))
    #print(type(request))
    return render(request,"legend/home.html",out_data)

def home3(request):
    va=[{'name':'sai','age':24},{'name':'Jay','age':21},{'name':'Shiva','age':19},{'name':'Jayanth','age':17}]

    return render(request,"legend/home.html",{'data':va,'Branch':'Information Technology'})

def greet(request,name):
    result="Hello "+ name +"! How are you dude !"
    return render(request,"output.html",{'out':result})

def greet2(request,old):
    va=[{'name':'sai','age':24},{'name':'Jay','age':21},{'name':'Shiva','age':20},{'name':'Jayanth','age':17}]
    li=[]
    for item in va:
        if item['age']==old:
            li.append(item)
    return render(request,"legend/home.html",{'data':li})



#{"st1":"sai","st2":"Jay","st3":"Shiva"}


"""class car():
    def __init__(name,model):
        self.car_name=name
        self.car_model=model
    

obj1=car(name="tata",model=2023)
obj2=car(name="tata",model=2023)

QuerySet=[obj1,obj2]"""



def form_view(request):
    print(type(request.method))
    if request.method=="POST":
        m1=request.POST['movie_name']
        #m1=request.POST.get('movie_name')
        h1=request.POST.get('hero_name')
        y1=request.POST.get('year')
        return render(request,"form.html",{'movie':m1,'hero':h1,'year':y1,'r1':request.method})
    else:
        return render(request,"form.html",{'r1':type(request.method)})