from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from .models import Employee
from .serializers import EmployeeSerializer

# 1. API ViewSet for frontend (React)
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

# 2. Payslip HTML View
def payslip_view(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    net_salary = employee.basic_salary + employee.allowance - employee.deductions
    return render(request, 'payslip.html', {
        'employee': employee,
        'net_salary': net_salary
    })

# 3. PDF Download View
def download_payslip_pdf(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    net_salary = employee.basic_salary + employee.allowance - employee.deductions

    # Prepare PDF response
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="payslip_{employee.name}.pdf"'

    # Create PDF
    p = canvas.Canvas(response)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, f"Payslip for {employee.name}")

    p.setFont("Helvetica", 12)
    p.drawString(100, 760, f"Role: {employee.role}")
    p.drawString(100, 740, f"Basic Salary: ₹{employee.basic_salary}")
    p.drawString(100, 720, f"Allowance: ₹{employee.allowance}")
    p.drawString(100, 700, f"Deductions: ₹{employee.deductions}")
    p.drawString(100, 680, f"Net Salary: ₹{net_salary}")

    p.showPage()
    p.save()
    return response
