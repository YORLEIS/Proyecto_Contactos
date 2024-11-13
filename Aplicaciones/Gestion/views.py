from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Ciudad, Persona, Telefono, Email
from django.conf import settings
from .models import Ciudad

# Create your views here.

def formularioContacto(request):
    return render(request, "formularioContacto.html")


def contactar(request):
    if request.method == "POST":
        asunto = request.POST["txtAsunto"]
        mensaje = (
            f"Identificación: {request.POST['txtCedula']}\n"
            f"Apellido Paterno: {request.POST['txtApellidoPaterno']}\n"
            f"Apellido Materno: {request.POST['txtApellidoMaterno']}\n"
            f"Nombres: {request.POST['txtNombres']}\n"
            f"Fecha de Nacimiento: {request.POST['txtFechaNacimiento']}\n"
            f"Sexo: {request.POST['txtSexo']}\n"
        )
        
        # Obtener el objeto Ciudad correspondiente al código
        ciudad_codigo = request.POST["txtCiudad"]
        ciudad = Ciudad.objects.get(codigo=ciudad_codigo)
        mensaje += f"Ciudad: {ciudad.nombre}\n"

        mensaje += f"Correo Electrónico: {request.POST['txtCorreoElectronico']}\n"
        mensaje += f"Asunto: {request.POST['txtAsunto']}\n"
        mensaje += f"Mensaje: {request.POST['txtMensaje']}\n"
        mensaje += f"Teléfono: {request.POST['txtTelefono']}."

        # Crear y guardar una nueva persona en la base de datos
        nueva_persona = Persona(
            cc=request.POST["txtCedula"],
            apellidoPaterno=request.POST["txtApellidoPaterno"],
            apellidoMaterno=request.POST["txtApellidoMaterno"],
            nombres=request.POST["txtNombres"],
            sexo=request.POST["txtSexo"],
            fechaNacimiento=request.POST["txtFechaNacimiento"],
            ciudad=ciudad  # Usar el objeto Ciudad en lugar del código
        )
        nueva_persona.save()

        # Crear y guardar un teléfono asociado a la persona
        nuevo_telefono = Telefono(
            persona=nueva_persona,
            numero=request.POST["txtTelefono"]
        )
        nuevo_telefono.save()

        # Crear y guardar un correo electrónico asociado a la persona
        nuevo_email = Email(
            persona=nueva_persona,
            email=request.POST["txtCorreoElectronico"]
        )
        nuevo_email.save()

        # Envía el correo
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["estudiandosoftware19@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)

        return redirect('contacto_exitoso')

     
  


def formularioContacto(request):
    # Obtener la lista de ciudades para el formulario
    ciudades = Ciudad.objects.all()

    return render(request, "formularioContacto.html", {'ciudades': ciudades})


def contacto_exitoso(request):
    return render(request, 'contactoExitoso.html')

