from django.shortcuts import render, redirect
from .models import Person

def index(request):
    all_person = Person.objects.all()
    return render(request, 'index.html', {'all_person': all_person})


def form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')

        Person.objects.create(name=name, age=age)
        return redirect('/')

    return render(request, 'form.html')
# --- ส่วนที่ต้องเพิ่มใหม่ (SS+ Logic) ---

# 1. ฟังก์ชันลบข้อมูล
def delete(request, id):
    person = Person.objects.get(id=id) # ดึงข้อมูลตาม ID ที่ส่งมาจากปุ่มลบ
    person.delete()                    # สั่งลบ
    return redirect('/')               # ลบเสร็จกลับหน้าแรกทันที

# 2. ฟังก์ชันแก้ไขข้อมูล
def edit(request, id):
    person = Person.objects.get(id=id) # ดึงข้อมูลคนเดิมมาโชว์ก่อน
    
    if request.method == 'POST':
        # ถ้ามีการกดปุ่มบันทึกการแก้ไข (POST)
        person.name = request.POST.get('name')
        person.age = request.POST.get('age')
        person.save()                  # บันทึกทับข้อมูลเดิม
        return redirect('/')           # แก้เสร็จกลับหน้าแรก
        
    # ถ้าแค่กดปุ่มแก้ไขมาเฉยๆ ให้โชว์หน้าฟอร์มพร้อมข้อมูลเก่า
    return render(request, 'form.html', {'person': person})