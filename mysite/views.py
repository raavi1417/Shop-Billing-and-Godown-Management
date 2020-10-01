import io
from django.shortcuts import render,redirect
from mysite.forms import *
from django.http import *
from mysite.models import *
from django.contrib.auth.models import User,auth
from django.contrib import messages
from reportlab.pdfgen import canvas

def index(request):
    data=ShopData.objects.all()
    var=5
    var1=0
    len_item=[]
    for i in data:
        if i.stock <=5:
            len_item.append(i.id)
    total=len(len_item)
    return render(request,'index.html',{'total':total,'var1':var1})

def update(qty,pid):
    all_data=ShopData.objects.get(item_id=pid)
    left=int(all_data.stock)-int(qty)
    all_data.stock=left
    all_data.save()
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username Already Taken')
            return redirect('/admin_login')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email already Taken')
            return redirect('/admin_login')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.info(request,'User Registration Successfully')
            return redirect('/admin_login')
    else:
        return render(request,'register.html')

def admin_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            request.session['username']=username
            #print(username)
            return redirect('/admin_part')
            
        else:
            return HttpResponse('''<script> alert("Please enter right information");document.location='admin_login'</script>''')
    
    return render(request,'admin_login.html')
def show(request):
    obj=ShopData.objects.all()
    print(obj)
    return render(request,'show.html',{'key1':obj,'ses':request.session['username']})

def admin_part(request):
    if request.method == 'POST':
        obj=ShopForm(request.POST)
        if obj.is_valid():
            try:
                obj.save()
                obj1=ShopData.objects.all()
                return render(request,'show.html',{'key1':obj1},)
            except:
                pass
    else:
        obj=ShopForm()
        return render(request,'admin.html',{'key':obj,'ses':request.session['username']})
def admin_logout(request):
    del request.session['username']
    auth.logout(request)
    return redirect('/')
def search(request):
    if request.method == 'GET':
        search=request.GET['search']
        print(search)
        if search:
            match=ShopData.objects.filter(item_name__icontains=search)
            if match:
                return render(request,'index.html',{'mtch':match})
            else:
                return HttpResponse('''<script> alert("Not matched");document.location='/'</script>''')
        else:
            return redirect('/')
    else:
        return (request,'index.html')
def add_to_cart(request):
    if request.method == 'POST':
        pid=request.POST['pid']
        qty=request.POST['qty']

        product=ShopData.objects.get(item_id=pid)
        st=product.stock
        print(type(st))
        if int(qty)>int(st):
            return HttpResponse('''<script> alert("Out of stock");document.location='/'</script>''')
        else:
            is_exist=cart.objects.filter(pid=pid)
            if len(is_exist)>0:
                return HttpResponse('''<script> alert("Already Exist in Cart");document.location='/'</script>''')
            else:
                price=product.price*int(qty)
                print(price)
                c=cart(item=product,qty=qty,pid=pid,price=price)
                c.save()
                update(qty,pid)
                return HttpResponse('''<script> alert("Item Added Into Cart");document.location='/'</script>''')
             #ftch=cart.objects.all()
             #print(ftch)
             #return render(request,'cart.html',{'key':ftch})
         
    return render(request,'cart.html')
def cart_details(request):
    all_ftch=cart.objects.all()
    print(len(all_ftch))
    if(len(all_ftch)>0):
        price=[]
        for i in all_ftch:
            price.append(i.price)
            total=sum(price)
        return render(request,'cart.html',{'key':all_ftch,'total':total})
    else:
        return HttpResponse('''<script> alert("Cart is empty");document.location='/'</script>''')
def Billing(request):
    if request.method == 'GET':
        ftch=cart.objects.all()
        all_ftch=cart.objects.all()
        price=[]
        dict_item={}
        for i in all_ftch:
            price.append(i.price)
            total=sum(price)
            dict_item[i.item]=i.qty
        print(dict_item)
        
        name=request.GET['name']
        print(name)
        mobile=request.GET['mobile']
        final=total
        print(final)
        items=str(dict_item)
        print(items)
        address=request.GET['address']
        status=request.GET['status']
        bill_number=name[:4]+mobile
        Bill=bill(name=name,mobile=mobile,final=final,items=items,address=address,status=status,bill_number=bill_number)
        Bill.save()
        #return render(request,'index.html')
        buffer=io.BytesIO()
        p=canvas.Canvas(buffer)
        p.setTitle('%s'%bill_number)
        p.drawString(260,770,'Invoice')
        p.drawString(40,780,'Invoice Number: %s'%bill_number)
        p.drawString(20,750,'------------------------------------------------------------------------------------------------------------------------------------------')
        p.drawString(80,700,'Customer Name  :  %s'%name)
        p.drawString(80,660,'Contact Number  :  %s'%mobile)
        c=cart.objects.all()
        for i in c:
            
            p.drawString(80,620,'Items  :  %s'%i.item)
            p.drawString(380,620,'Quantity  :  %s'%i.qty)
            #p.drawString(80,600,'Items  :  %s'%i.items[45:60])
        p.drawString(80,590,'Payment Status :  %s'%status)
        p.drawString(80,550,'Address  :  %s'%address)
        p.drawString(80,490,'Total   %s:'%total)
        p.drawString(420,420,'Signature')
        p.showPage()
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename=' %s.pdf'%bill_number)
    return render(request,'cart.html')
def delete_item_cart(request,id):
    data=cart.objects.get(id=id)
    data.delete()
    return HttpResponse('''<script> alert("Item Delete");document.location='/cart'</script>''')
def delete_all(request):
    data=cart.objects.all()
    data.delete()
    return HttpResponse('''<script> alert("Clear Cart");document.location='/'</script>''')
def delete_item(request,id):
    data=ShopData.objects.get(id=id)
    data.delete()
    return redirect('/show')
def edit(request,id):
    item=ShopData.objects.get(id=id)
    return render(request,'edit.html',{'it':item})
def Data_update(request,id):
    up=ShopData.objects.get(id=id)
    form=ShopForm(request.POST,instance=up)
    if form.is_valid():
        form.save()
        return HttpResponse('''<script> alert(" Item Updated");document.location='/show'</script>''')
def notification(request):
    data=ShopData.objects.all()
    var=5
    var1=0
    msg='Stock Finish'
    return render(request,'notifiaction.html',{'key':data,'var':var,'var1':var1,'msg':msg})
def stock(request):
    return render(request,'stock.html')           
           
