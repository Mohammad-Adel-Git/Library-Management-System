from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func (request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
            # if request.user.groups.filter(name = 'customer'):
            #     return redirect('homeeUser')
            # if request.user.groups.filter(name = 'admin'):
            #     return redirect('homeeAdmin')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            group = list()
            print (len(allowed_roles)-1)
            if request.user.groups.filter(name__in=allowed_roles).exists():
                #
                #This user has (at least) one group that meets authorisation requirement
                return view_fun(request, *args, **kwargs)

            else:
                #no group found for this user..
                return redirect('forbidden')
        return wrapper_fun
    return decorator

"""
def allowed_users(allowed_roles=[]):
    def decorator(view_fun):
        def wrapper_fun(request, *args, **kwargs):
            group = list()
            print (len(allowed_roles)-1)
            if request.user.groups.exists():
                for i in range(0,len(allowed_roles)-1):
                    group.append (request.user.groups.all()[i].name)
                    print(request.user.groups.all()[i].name)                                
            for role in group:
                if role in allowed_roles:
                    return view_fun(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_fun
    return decorator
"""