from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import JobApplication
from .forms import JobApplicationForm
import csv

@login_required
def application_list(request):
    status_filter = request.GET.get('status', '')
    applications  = JobApplication.objects.filter(user=request.user)
    if status_filter:
        applications = applications.filter(status=status_filter)
    return render(request, 'applications/list.html', {
        'applications': applications,
        'status_filter': status_filter,
        'status_choices': JobApplication.STATUS_CHOICES,
    })

# Create application
@login_required
def application_create(request):
    form = JobApplicationForm(request.POST or None)
    if form.is_valid():
        app      = form.save(commit=False)
        app.user = request.user
        app.save()
        return redirect('application_list')
    return render(request, 'applications/form.html', {'form': form, 'title': 'Add Application'})

# Edit application
@login_required
def application_edit(request, pk):
    app  = get_object_or_404(JobApplication, pk=pk, user=request.user)
    form = JobApplicationForm(request.POST or None, instance=app)
    if form.is_valid():
        form.save()
        return redirect('application_list')
    return render(request, 'applications/form.html', {'form': form, 'title': 'Edit Application'})

# Delete application
@login_required
def application_delete(request, pk):
    app = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        app.delete()
        return redirect('application_list')
    return render(request, 'applications/confirm_delete.html', {'app': app})

# Update application status
@login_required
def application_status_update(request, pk):
    app = get_object_or_404(JobApplication, pk=pk, user=request.user)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in dict(JobApplication.STATUS_CHOICES):
            app.status = new_status
            app.save()
    return redirect('application_list')

# Export information to CSV
@login_required
def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="applications.csv"'
    writer = csv.writer(response)
    writer.writerow(['Company', 'Role', 'Location', 'Status', 'Applied Date', 'URL', 'Notes'])
    for app in JobApplication.objects.filter(user=request.user):
        writer.writerow([
            app.company, app.role, app.location,
            app.get_status_display(), app.applied_date, app.url, app.notes
        ])
    return response