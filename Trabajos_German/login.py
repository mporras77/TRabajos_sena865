from tkinter import *
import os
import cv2
from matplotlib import pyplot
from mtcnn.mtcnn import MTCDNNpip
import numpy as np

#---------------------------creamos una funcion que se encargara de registar el usuario --------------------------------

def registar_usuario():
    usuario_info = usuario.get () #obtenemos la informacion almacenada en usuario
    contra_info = usuario.get () #obtenemos la informacion almacenada en contra
    
    
    archivo = open(usuario_info, "w") #abrimos la informacion en modo escritura
    archivo.write (usuario_info + "\n") #escribimos la informacion en modo escritura
    archivo.write (contra_info) 
    archivo.close()
    
    #limpiaremos los text variable
    usuario_entrada.delete (O, END)
    contra_entrada.delete (O, END)
    
    #ahora le diremos al usurio que su registro ha sido exitoso
    Label(pantalla, text = "registro convecional", fg = "green", font = ("calibri",ll)).pack()
    
#-----------------------funcion para almacenar el registro cacial------------------------------------------------------------

def registro_facial ():
    #vamps a capturar el rostro
    cap = cv2.VideoCapture (O)         #elegimos la camara con la que vamos a hacer la deteccion
    while(True) :
        ret,frame = cap.read ()        #leemos el video
        cv2.imshow ('registro facial',frame)   #mostramos el video en la pantalla
        if cv2.waitKey (1) == 27:              #cuando oprimamos "escape" rompe el video
            break 
    usuario_img = usuario.get ()
    cv2.imwrite (usuario_img+".jpg",frame)       #guardamos la ultima captura del video como imagen asignamos el nombre del usuario
    cap.release ()                               #cerramos
    cv2.destroyALLWindows ()

    usuario_entrada.delete(O, END)    #limpiamos los text variables
    contra_entrada.delete (O, END)
    label (pantallal, text = "Registro Facial Exitoso", fg = "green", font = ("calibri",11)).pack ()

    #-----------------determinamos el rostro y exportamos los pixeles--------------------------------------------------------

    def reg_rostro(img, Lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1,ancho, alto = lista_resultados[i]["box"]
            x2,y2 = x1 + ancho , y1 + alto
            pyplot.subplot (1, len(lista_resultados),i+1)
            pyplot.axis('off')
            cara_reg = data [y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg, (150,200), interpolation = cv2.INTER_CUBIC)      #guardamos la imagen con un tamaño de 150x200
            cv2.imwrite (usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot,show ()

    img = usuario_img+".jpg"
    pixeles = pyplot.imread (img)
    dectector = MTCDNN ()
    caras = dectector.detect_faces(pixeles)
    reg_rostro (img, caras)

#-----------------------creamos una funcion para asignar al boton registro------------------------------------------------

def registro ():
    global usuario
    global contra #globalizamos las variables para usarlas en otra funciones 
    global usuario_entrada
    global contra_entrada
    global pantallal
    pantalla1 = toplevel (pantalla) #esta pantalla es un nivel superior a la principal
    pantalla1.title("Registro")
    pantalla1.geometry("300X250")   #asignamos el tamaño de la ventana

#-------------empezar a crear entradas----------------------------------------------------------------------------

    usuario = stringVar()
    contra = stringVar ()

    Label (pantalla1, text = "Registro facial: debe de asignar un usuario:").pack ()
    #Label(pantalla1,  text) ="").pack () #dejamos un poco de espacio
    Label (pantalla1, text = "Registro tradicional: debe asignar usuario y contraseña:").pack ()
    Label (pantalla1, text = "").pack ()   #dejamos un poco de espacio
    Label (pantalla1, text = "usiario * ").pack ()  #mostramos en la pantalla 1 el usuario
    usuario_entrada = Entry(pantalla1, textvariable = usuario)  #creamos un text variable para el usuario ingrese la contra
    usuario_entrada.pack ()
    Label (pantalla1, text = "contraseña * ").pack ()  #mostrar en la pantalla 1 cantraseña  
    Button(pantallal, text = "Registro tradicional", width = 15, height = 1, command = registar_usuario).pack()

    #---------------------------------------vamos a crear el boton para el registro facial--------------------------------------------

    Label(pantalla1, text = "").pack()
    Button(pantalla1, text = "Registro Facial", width = 15, height = 1, command = registro_facial).pack()

#---------------------------------------funcion para vereficar los datos al login---------------------------------------------------------------

def verificacion_login ():
    log_usuario = verificacion_usuario.get()
    log_contra = verificacion_contra.get()
    
    usuario_entrada2.delete (O, END)
    contra_entrada2.delete (O, END)
    
    lista_archivos = os.listdir()
    if log_usuario in lista_archivos:
        archivo2 = open(log_usuario, "r")
        verificacion = archivo2.read(). splitlines()
        if log_contra in verificacion:
            print("inicio de sesion exitoso")
            Label(pantalla2, text = "Inicio de sesion exitoso", fg = "green", font = ("calibri",lll)).pack() 
        else:
            print("Contraseña incorrecta, ingrese de nuevo")
            Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("calibri",ll)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text = "Usuario no encontrado", fg = "red", font = ("calibri",ll)).pack()
        
#--------------------------------------función para el login facial-----------------------------------------------------------------------------
       
def login_facial():
    
#-------------------------------------vamos a capturar rostro-----------------------------------------------------------------------------------

    cap = cv2.VideoCapture(0)
    while(True):
        ret,frame = cap.read()
        cv2.imshow ('Login Facial', frame)
        if cv2.waitkey(1) == 27:
            break
    usuario_login = vereficacion_usuario.get()
    cv2.imshow (usiario_login+"LOG.jpg", frame)
    cap.release()
    cv2.destroyAllwindows()
    
    usuario_entrada2.delete(O, END)
    contra_entrada2.delete(O, END)
    Label(pantallal, text = "registro Facial Exitoso", fg = "green", font = ("calibri",ll)).pack()
    
    #-------------------------------------funcion para guardar rostro--------------------------------------------------------------------------------

    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            x1,y1, ancho, alto = lista_resultados[1] ['box']
            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot (1, len(lista_resultados), i+1)
            pyplot.axis ('off')
            cara_reg = data [y1:y2, x1:x2]
            cara_reg = cv2.resize(vara_reg,(150,200),cara_reg)
            cv2.imwite(usuario_img+"LOG.jpg",cara_reg)
            return pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()
    
    #--------------------------------------detectamos el rostro---------------------------------------------------------------------------------------

    img = usuario_login+"LOG.jpg"
    pixeles = pyplot.imread(img)
    dectector = MTCDNN ()
    caras = dectector.detect_faces(pixeles)
    log_rostro(img, caras)

    #-------------------------------------funcion para comparar rostro-------------------------------------------------------------------------------

    def orb_sim (img1, img2):
        orb = cv2.ORB_create()
    
        kpa, descr_a = orb.detectAndCompure(img1, None)
        kpa, descr_b = orb.detectAndCompure(img2, None)
    
        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    
        matches = comp.march(descr_b)
    
        regiones_asimilares = [1 for i in matches if i.distance < 70]
        if len(matches) == 0:
            return ()
        return len(regiones_asimilares)/len(matches)

    #----------------------------------------importamos las imagenes y llamamos la funcion de comparacion--------------------------------------------

    im_archivos = os.listdir()
    if usuario_login+".jpg" in im_archivos:
        rostro_reg = cv2.imread(usuario_login+".jpg",0)
        rostro_log = cv2.imread(usuario_login+"LOG.jpg",0)
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.9:
            Label(pantalla2, text = "Inicio de Sesion Exitoso", fg = "green", font = ("calibri",lll)).pack()
            print("Bienvenido al Sistema Usuario: ",usuario_login)
            print("compatibilidad con la foto del registro: ",similitud)
        else:
            print("Rostro Incirrecto, Certifique su Usiario")
            print("compatibilidad con la foto del registro: ",similitud)
            Label(pantalla2, text = "Usiario no encontrado", fg = "red", font = ("calibri",lll)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantalla2, text = "usuario no encontrado", fg = "red", font = ("calibri",ll)).pack()
            
#------------------------------------------funcion que asignaremos al boton login----------------------------------------------------------------------

def login():
    global pantalla2
    global verificacion_usuario
    global verificacion_contra
    global usuario_entrada2
    global contra_entrada2
    
    pantalla2 = Toplevel(pantalla)
    pantalla2.title("Login")
    pantalla2.geometry ("300x250")     
    Label(pantalla2, text = "Login facial: debe asignar un usuario:").pack()
    Label(pantalla2, text = "Login tradicional: debe asignar usuario y contraseña:").pack()
    
    verificacion_usuario = StringVar()
    verificacion_contra = StringVar()
    
    #----------------------------------------Ingresamos los datos----------------------------------------------------------------------------------------
    Label(pantalla2, text = "Usuario * ").pack()
    usuario_entrada2 = Entry(pantalla2, textvariable = verificacion_usuario)
    usuario_entrada2.pack
    Label(pantalla2, text = "contraseña * ").pack()
    contra_entrada2 = Entry(pantalla2, textvariable = verificacion_contra)
    contra_entrada2.pack()
    Label(pantalla2, text = "").pack()
    Button(pantalla2, text ="Inicio de sesion tradicional", width = 20, height = 1, command = verificacion_login).pack()
    
    #----------------------------------------vamos a hacer el boton para hacer el login facial-----------------------------------------------------------
    Label(pantalla2, text = "").pack()
    Button(pantalla2, text = "Inicio de sesion facial", width =20, height = 1 , command = verificacion_facial).pack()

#--------------------------------------------funcion de nuestra pantalla princial------------------------------------------------------------------------
def pantalla_principal():
    global pantalla
    pantalla = Tk()
    pantalla.geometry ("300x250")
    pantalla.title ("M.I.P:F")
    Label(text = "Login Inteligente de Mundo Intelectual de Profecionales Formativos")
    
#------------------------------------------vamos a crear las funciones----------------------------------------------------------------------------------
    Label(text = "").pack()
    Button(text = "Iniciar sesion", height = "2", width = "30", font = ("verdina", 13)).pack()
    Label( text = "").pack()
    Button(text = "Registro", height = "2", width = "30", compound = registro).pack()
    
    pantalla.mainloop()
    
pantalla_principal()