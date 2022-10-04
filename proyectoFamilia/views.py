from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader

from home.models import Familia

def hola(request):
    
    template = loader.get_template('hola.html')
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado)


def mi_template(request, nombre):
   
    template = loader.get_template('mi-template.html')
    template_renderizado = template.render({'persona': nombre})
        
    return HttpResponse(template_renderizado)

def crear_familia(request):
        
    familiar1= Familia(nombre='Homero',apellido='Addams',parentezco='Padre',anio_nacimiento=1961, edad=datetime.now().year - 1961,fecha_registro=datetime.now())
    familiar1.save()
    
    
    familiar2= Familia(nombre='Morticia',apellido='Addams',parentezco='Madre',anio_nacimiento=1968, edad=datetime.now().year - 1968,fecha_registro=datetime.now())
    familiar2.save()
    
   
    familiar3= Familia(nombre='Merlina',apellido='Addams',parentezco='Hija',anio_nacimiento=2008, edad=datetime.now().year - 2008,fecha_registro=datetime.now())
    familiar3.save()
    
  
    familiar4= Familia(nombre='Pericles',apellido='Addams',parentezco='Hijo',anio_nacimiento=2011, edad=datetime.now().year - 2011,fecha_registro=datetime.now())
    familiar4.save()
    
    template = loader.get_template('crear-familia.html')
    template_renderizado = template.render({})
    
    return HttpResponse(template_renderizado)

def ver_familia(request):
    
    familia = Familia.objects.all()
    
    template = loader.get_template('ver-familia.html')
    template_renderizado = template.render({'familia': familia})
        
    return HttpResponse(template_renderizado)
