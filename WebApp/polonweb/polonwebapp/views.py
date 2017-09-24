

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from polonwebapp.forms import RegistrationForm


@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email']
            )
            return HttpResponseRedirect(reverse('register_success'))
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
        'form': form
    })

    return render_to_response(
        'registration/register.html',
        variables,
    )


def register_success(request):
    return render_to_response('registration/success.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def scopus_hindex_all(request):
    return render_to_response('database_files/scopus_hindex_all.html')

def scopus_hindex_dr(request):
    return render_to_response('database_files/scopus_hindex_dr.html')

def scopus_hindex_drhab(request):
    return render_to_response('database_files/scopus_hindex_drhab.html')

def scopus_num_of_pubs_all(request):
    return render_to_response('database_files/scopus_num_of_pubs_all.html')

def scopus_num_of_pubs_dr(request):
    return render_to_response('database_files/scopus_num_of_pubs_dr.html')

def scopus_num_of_pubs_drhab(request):
    return render_to_response('database_files/scopus_num_of_pubs_drhab.html')

def dblp_num_of_pubs_all(request):
    return render_to_response('database_files/dblp_num_of_pubs_all.html')

def dblp_num_of_pubs_dr(request):
    return render_to_response('database_files/dblp_num_of_pubs_dr.html')

def dblp_num_of_pubs_drhab(request):
    return render_to_response('database_files/dblp_num_of_pubs_drhab.html')

def google_scholar_citations_all(request):
    return render_to_response('database_files/google_scholar_citations_all.html')

def google_scholar_citations_dr(request):
    return render_to_response('database_files/google_scholar_citations_dr.html')

def google_scholar_citations_drhab(request):
    return render_to_response('database_files/google_scholar_citations_drhab.html')

def google_scholar_hindex_all(request):
    return render_to_response('database_files/google_scholar_hindex_all.html')

def google_scholar_hindex_dr(request):
    return render_to_response('database_files/google_scholar_hindex_dr.html')

def google_scholar_hindex_drhab(request):
    return render_to_response('database_files/google_scholar_hindex_drhab.html')

@login_required
def homeit(request):
    return render_to_response(('home.html', {'user': request.user}))
    #return HttpResponseRedirect(reverse('homeit'))
