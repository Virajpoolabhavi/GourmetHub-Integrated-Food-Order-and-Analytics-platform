from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate,login

from orderservice.models import MenuItem

from orderservice.models import OrderList

from django.contrib.auth.decorators import login_required





def homepage(request):

    return render(request,'base.html')


def register(request):

    return render(request,'register.html')


def menu(request):

    items = MenuItem.objects.all()

    return render(request,'Menu.html',{'menu':items})


def login_page(request):

    return render(request,'login.html')

def reg_save(request):

        if request.method =='POST':

            fname=request.POST.get('fname')

            lname=request.POST.get('lname')

            username=request.POST.get('username')

            password=request.POST.get('password')
        

            user = User.objects.filter(first_name=fname,last_name=lname,username=username)
        

            if user.exists():

                return HttpResponseRedirect('/login/')

            else:

                user = User.objects.create(first_name=fname,last_name=lname,username=username)

                user.set_password(password)

                user.save()

                return HttpResponseRedirect('/login/')



def login_save(request):

     if request.method =='POST':

            username=request.POST.get('uname')

            password=request.POST.get('password')
            

            user = authenticate(username=username,password=password)
            

            if user is None:

                return HttpResponseRedirect('/login/')
            elif username=='admin' and password=='admin123':
                
                login(request,user)
                return HttpResponseRedirect('/new/')

            else:

                login(request,user )

                return HttpResponseRedirect('/menu/')
            

def add(request):  

    if request.method =="POST":

        menu_items = MenuItem.objects.all()

        for item in menu_items:
            if (int(request.POST.get(f'{item.id}_qty',0)))>0:

                order_item,created = OrderList.objects.get_or_create(

                    menu_item=item,

                    customer= request.user,

                    quantity= int(request.POST.get(f'{item.id}_qty',0))
                )
                order_item.save()
                

        return HttpResponseRedirect('/menu/')

    else:

        return HttpResponseRedirect('/menu/')
    
    
def order(request):
    return HttpResponseRedirect('/order_summary/')

@login_required
def order_summary(request):


    order_lists = OrderList.objects.filter(customer=request.user)


    total_price = sum(order_list.total_price for order_list in order_lists)
    
    return render(request, 'order_summary.html', {'order_lists': order_lists, 'total_price': total_price})
        
@login_required           
def dash(request):
    if request.method =='POST':
        
        data=[]
        label=[]
        items = MenuItem.objects.all()
        for i in items:
            label.append(i.name)
        query = OrderList.objects.filter(customer=request.user)
        pc=0
        pt=0
        mc=0
        r=0
        vb=0
        mr=0
        for p in query:
            if(p.menu_item.name == 'Panner Curry'):
                    pc=pc+p.quantity
                    
            elif(p.menu_item.name== 'Panner Tikka'):
                pt=pt+p.quantity
            elif(p.menu_item.name== 'Mushroom Curry'):
                mc=mc+p.quantity
            elif(p.menu_item.name== 'Roti'):
                r=r+p.quantity
            elif(p.menu_item.name== 'Veg Biryani'):
                vb=vb+p.quantity
            elif(p.menu_item.name== 'Mushroom Rice Bowl'):
                mr=mr+p.quantity
            
                
        data.append(pc)    
        data.append(pt) 
        data.append(mc)
        data.append(r)
        data.append(vb)
        data.append(mr)     
         
        return render(request,'user_dash.html',{
            'label':label,
            'data':data
            })  
             
def cdash(request):
    if request.method =='POST':
        data=[]
        label=[]
        items = MenuItem.objects.all()
        for i in items:
            label.append(i.name)
        query = OrderList.objects.all()
        pc=0
        pt=0
        mc=0
        r=0
        vb=0
        mr=0
        
        for p in query:
            if(p.menu_item.name == 'Panner Curry'):
                    pc=pc+p.quantity
                    
            elif(p.menu_item.name== 'Panner Tikka'):
                pt=pt+p.quantity
            elif(p.menu_item.name== 'Mushroom Curry'):
                mc=mc+p.quantity
            elif(p.menu_item.name== 'Roti'):
                r=r+p.quantity
            elif(p.menu_item.name== 'Veg Biryani'):
                vb=vb+p.quantity
            elif(p.menu_item.name== 'Mushroom Rice Bowl'):
                mr=mr+p.quantity
            
                
        data.append(pc)    
        data.append(pt) 
        data.append(mc)
        data.append(r)
        data.append(vb)
        data.append(mr)
        return render(request,'cdash.html',{
            'label':label,
            'data':data
            })
    
    