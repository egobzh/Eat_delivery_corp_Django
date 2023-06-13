from django.shortcuts import render
from django.views.generic.base import View
from.form import *
from .models import *
from datetime import date
import random

class index(View):
    def get(self, request):
        workers=[x.name for x in Worker.objects.all()]
        food=[x.name for x in Food.objects.all()]
        return render(request , 'deliv_main/base.html',{'range':range(1),'workers':workers,'food':food,'num':''})
    def post(self, request):
        worker=request.POST['worker']
        if worker=='-Выберите сотрудника-':
            return render(request , 'deliv_main/worker_error.html')
        else:
            food_or=[]
            if request.POST['food0']!='-Выберите блюдо-':
                food_or.append(request.POST['food0'])
            try:
                if request.POST['merandom']:
                    food = [x.name for x in Food.objects.all()]
                    for x in range(random.randint(1,5)): food_or.append(food[random.randint(0,len(food)-1)])
            except:
                pass
            try:
                datee = request.POST['date']
                if date.fromisoformat(datee) < date.today():
                    datee = date.today().strftime("%Y-%m-%d")
            except:
                datee = date.today().strftime("%Y-%m-%d")
            order = Order.objects.create(date=datee, order_worker=Worker.objects.get(name=worker))
            if len(food_or)==0:
                return render(request, 'deliv_main/order_error.html')
            else:
                order_e=''
                summ=0
                for i in food_or:
                    order_e+=f'{i}, '
                    summ+=Food.objects.get(name=i).price
                    Food_order.objects.create(orderr=order, order_food=Food.objects.get(name=i))
                return render(request , 'deliv_main/good_order.html',{'name':worker,'date':datee,'order':order_e[:-2],'sum':summ})
class indexnum(View):
    def get(self, request, num):
        workers=[x.name for x in Worker.objects.all()]
        food=[x.name for x in Food.objects.all()]
        request.num = num
        return render(request , 'deliv_main/base.html',{'range':range(num),'workers':workers,'food':food,'num':num})
    def post(self, request, num):
        worker=request.POST['worker']
        if worker=='-Выберите сотрудника-':
            return render(request, 'deliv_main/worker_error.html')
        else:
            food_or=[]
            for i in range(num):
                if request.POST['food'+str(i)]=='-Выберите блюдо-':
                    pass
                else:
                    food_or.append(request.POST['food'+str(i)])
            try:
                if request.POST['merandom']:
                    food = [x.name for x in Food.objects.all()]
                    for x in range(random.randint(1,5)): food_or.append(food[random.randint(0,len(food)-1)])
            except:
                pass
            try:
                datee=request.POST['date']
                if date.fromisoformat(datee)<date.today():
                    datee = date.today().strftime("%Y-%m-%d")
            except:
                datee = date.today().strftime("%Y-%m-%d")
            order = Order.objects.create(date=datee, order_worker=Worker.objects.get(name=worker))
            if len(food_or)==0:
                return render(request, 'deliv_main/order_error.html')
            else:
                order_e=''
                summ=0
                for i in food_or:
                    order_e+=f'{i}, '
                    summ+=Food.objects.get(name=i).price
                    Food_order.objects.create(orderr=order, order_food=Food.objects.get(name=i))
                return render(request , 'deliv_main/good_order.html',{'name':worker,'date':datee,'order':order_e[:-2],'sum':summ})
class history(View):
    def get(self, request):
        form = Historyform()
        return render(request , 'deliv_main/user_histiory_select.html',{'form':form})
    def post(self,request):
        form = Historyform(request.POST)
        if form.is_valid():
            uid=Worker.objects.get(name=form.cleaned_data['name']).id
            orders=Order.objects.filter(order_worker=uid)
            ordrs=[]
            for i in orders:
                sostav=''
                price=0
                for x in Food_order.objects.filter(orderr=i.id):
                    sostav+=x.order_food.name+', '
                    price+=float(x.order_food.price)
                ordrs.append({'sst':sostav[:-2],'price':round(price,2),'date':i.date})
        return render(request, 'deliv_main/user_history.html', {'orders': ordrs,'worker':form.cleaned_data['name']})
class ondate(View):
    def get(self, request):
        form = Ondateform()
        return render(request , 'deliv_main/ondate_select.html',{'form':form})
    def post(self,request):
        form = Ondateform(request.POST)
        if form.is_valid():
            orders=Order.objects.filter(date=form.cleaned_data['date'])
            bluda=[]
            sostav = ''
            summ_itogo=0
            for i in orders:
                for x in Food_order.objects.filter(orderr=i.id):
                    sostav += x.order_food.name + ', '
            for eat in Food.objects.all():
                clv=sostav.count(eat.name)
                price=clv*eat.price
                summ_itogo+=price
                bluda.append({'name':eat.name,'colvo':clv,'price':eat.price,'sum':round(price,2)})
        return render(request, 'deliv_main/ondate.html', {'eat': bluda,'date':form.cleaned_data['date'],'sum':round(summ_itogo,2)})

