from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person

# --- ของเดิมที่มีอยู่แล้ว ---
def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {"all_person": all_person})

def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        Person.objects.create(name=name, age=age)
        return redirect("/")
    else:
        return render(request, 'form.html')

# --- ส่วนที่เพิ่มใหม่ (เขียนต่อท้าย แต่อย่าให้เบี้ยวเข้าข้างใน) ---

# ฟังก์ชันลบข้อมูล
def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/")

# ฟังก์ชันแสดงหน้าแก้ไข (ดึงข้อมูลเก่าไปแสดงที่ฟอร์ม)
def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'edit.html', {"person": person})

# ฟังก์ชันรับค่าที่แก้ไขแล้วไปบันทึกในฐานข้อมูล
def update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        person = Person.objects.get(id=id)
        person.name = name
        person.age = age
        person.save() # สั่งบันทึกข้อมูลที่แก้ไขแล้ว
        return redirect("/")