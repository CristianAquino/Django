from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Company, Profile
import json

# Create your views here.

class CompanyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,req,id=0):
        if id>0:
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company = companies[0]
                datos = {'message':"Success",'companies':company}
            else:
                datos = {'message':"Compnies not found..."}
            return JsonResponse(datos)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos = {'message':"Success",'companies':companies}
            else:
                datos = {'message':"Compnies not found..."}
            return JsonResponse(datos)
                
    def post(self,req):
        # print(req.body)
        jd = json.loads(req.body)
        # print(jd)
        Company.objects.create(name=jd['name'],website=jd['website'],foundation=jd['foundation'])
        datos = {'mensaje':"Success"}
        return JsonResponse(datos)
        
    def put(self,req,id):
        jd = json.loads(req.body)
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()
            datos = {'mensaje':"Success"}
        else:
            datos = {'message':"Compnies not found..."}
        return JsonResponse(datos)
        
    def delete(self,req,id):
        companies=list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos = {'mensaje':"Success"}
        else:
            datos = {'message':"Compnies not found..."}
        return JsonResponse(datos)

class ProfileView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,req,id=0):
        if id>0:
            profiles=list(Profile.objects.filter(id=id).values())
            if len(profiles)>0:
                profile = profiles[0]
                datos = {'message':"Success",'profile':profile}
            else:
                datos = {'message':"Profile not found..."}
            return JsonResponse(datos)
        else:
            profiles = list(Profile.objects.values())
            if len(profiles)>0:
                datos = {'message':"Success",'profiles':profiles}
            else:
                datos = {'message':"Profiles not found..."}
            return JsonResponse(datos)
                
    def post(self,req):
        jd = json.loads(req.body)
        Profile.objects.create(name = jd['name'],
            email = jd['email'],
            phone = jd['phone'],
            address = jd['address'],
            about = jd['about'])
        datos = {'mensaje':"Success"}
        return JsonResponse(datos)
        
    def put(self,req,id):
        jd = json.loads(req.body)
        profiles=list(Profile.objects.filter(id=id).values())
        if len(profiles)>0:
            profile = Profile.objects.get(id=id)
            profile.name = jd['name']
            profile.email = jd['email']
            profile.phone = jd['phone']
            profile.address = jd['address']
            profile.about = jd['about']
            profile.save()
            datos = {'mensaje':"Success"}
        else:
            datos = {'message':"Profile not found..."}
        return JsonResponse(datos)
        
    def delete(self,req,id):
        profiles=list(Profile.objects.filter(id=id).values())
        if len(profiles)>0:
            Profile.objects.filter(id=id).delete()
            datos = {'mensaje':"Success"}
        else:
            datos = {'message':"Profile not found..."}
        return JsonResponse(datos)