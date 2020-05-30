from django.shortcuts import render, get_object_or_404, redirect
from .models import Plant
from .forms import ContactForm
from django.core.mail import EmailMessage, send_mail
from django.template.loader import get_template
from django.db.models import Q

def plant_detail(request, slug):
    '''view for individual plant pages'''
    template_name = 'plant_detail.html'
    plant = get_object_or_404(Plant, slug=slug)
    return render(request, 'guide/plant_detail.html', { 'plant':plant })

def plant_list(request):
    '''view for main page'''
    native_plants = Plant.objects.filter(status='Native').order_by('-date')
    non_native_plants = Plant.objects.filter(status='Non-native').order_by('-date')
    invasive_plants = Plant.objects.filter(status='Invasive').order_by('-date')
    return render(request, "guide/plant_list.html", {'native_plants':native_plants, 'non_native_plants':non_native_plants, 'invasive_plants':invasive_plants})

def about(request):
    '''view for about page'''
    return render(request, 'guide/about.html')

def contact(request):
    '''view for contact page'''
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name', ''
            )

            contact_email = request.POST.get(
                'contact_email', ''
            )

            form_content = request.POST.get(
                'content', ''
            )

            #Email the profile with the contact information
            template = get_template('guide/contact_template.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'form_content' : form_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Plants and Animals of the San Diego Trails" + '',
                ['rebgrasshopper@gmail.com'],
                headers = {'Reply-To': contact_email}
            )

            email.send()
            return redirect('contact')

    return render(request, 'guide/contact.html', {'form':form_class})


def search_results(request):
    if request.method == 'GET':
        query= request.GET.get('q')

        submitbutton= request.GET.get('submit')

        if query is not None:

            lookups= Q(name__icontains=query) | Q(genus__icontains=query) | Q(species__icontains=query) | Q(family__icontains=query)

            results= Plant.objects.filter(lookups)

            context={'results': results,
                     'submitbutton': submitbutton}

            return render(request, 'guide/search_results.html', context)

        else:
            return render(request, 'guide/search_results.html')

    else:
        return render(request, 'guide/search_results.html')