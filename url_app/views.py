from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .forms import UserDataForm, SecretKeyForm
from .models import UserData
from simplecrypt import encrypt, decrypt
import random, string



def index(request):
    return render(request, 'url_app/home.html')



class UserDataView(TemplateView):
    template_name = "url_app/data_edit.html"

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        form = UserDataForm()
        context = {'form' : form}
        return context
    
    def post(self, request):
        form = UserDataForm(request.POST)
        if form.is_valid():
            userData = form.save(commit=False)
            ciphercode = encrypt(userData.secret_key, userData.text)
            userData.text_encrypt = ciphercode
            print(userData.text_encrypt)
            randomPattern = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
            userData.pattern = randomPattern
            userData.save()
            return redirect('index') 
        form = UserDataForm()
        return render(request, 'url_app/data_edit.html', {'form': form})



class UserDataDetailView(TemplateView):
    template_name = "url_app/user_data_detail.html"
    
    def get(self, request, pk):
        userData = get_object_or_404(UserData, pk=pk)
        if userData.secret_key is None:
            return render(request, 'url_app/user_data_detail.html', {'userData': userData})
        form = SecretKeyForm()
        return render(request, 'url_app/secret_key_form.html', {'form': form})

    def post(self, request, pk):
        form = SecretKeyForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            secret_key = cleaned_data.get('secret_key')
            userData = get_object_or_404(UserData, pk=pk)
            if userData.secret_key == secret_key:
                plain_text = decrypt(secret_key, userData.text_encrypt)
                userData.text = plain_text
                return render(request, 'url_app/user_data_detail.html', {'userData': userData})
            else:
                print("wrong key")
            return redirect('index') 
        form = SecretKeyForm()
        return render(request, 'url_app/secret_key_form.html', {'form': form}) 

# def user_data_new(request):
#     if request.method == "POST":
#         form = UserDataForm(request.POST)
#         if form.is_valid():
#             userData = form.save(commit=False)
#             #ciphercode = encrypt(userData.secret_key, userData.text)
#             #userData.text = ciphercode
#             randomPattern = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
#             userData.pattern = randomPattern
#             userData.save()
#             return redirect('index')
#     else:
#         form = UserDataForm()
#     return render(request, 'url_app/data_edit.html', {'form': form})