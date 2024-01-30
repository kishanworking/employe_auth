from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View


from .models import Student
from .forms import StudentForm

# Create your views here.

class Index(View):
    template_name = "students/home.html"

    def get(self,request):
        details = Student.objects.all()
        context={
            'students' : details,
        }
        return render(request, self.template_name, context)



class View_student(View):
    def get(self,request, id):
        student = Student.objects.get(pk = id)
        return HttpResponseRedirect(reverse('index')) 




# geting data and validating it in forms
class Add(View):
    template_name = "students/add.html"
    
    def get(self,request):
        form = StudentForm()
        context={
            'form' : form,
        }
        return render(request, self.template_name, context )

    def post(self,request):
        
        form = StudentForm(request.POST)#puting all your form taken values in 
        
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['fiels_of_study']
            new_cgpa = form.cleaned_data['cgpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_name,
                last_name = new_last_name,
                email = new_email,
                fiels_of_study = new_field_of_study,
                cgpa = new_cgpa
            )
            new_student.save()
            
            return render(request, self.template_name ,{
                'form': StudentForm(),
                'success': True
            })
        




class Edit(View):
    template_name = "students/edit.html"

    def get(self,request,id):
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
        return render(request, self.template_name, {'form':form})
    
    def post(self,request,id):
        student = Student.objects.get(pk = id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save() 
            return render(request, 'students/edit.html', {'form':form,'success':True})






class Delete(View):
    def get(self,request,pk):
        task = get_object_or_404(Student, pk=pk)
        task .delete()
        return redirect('index')




