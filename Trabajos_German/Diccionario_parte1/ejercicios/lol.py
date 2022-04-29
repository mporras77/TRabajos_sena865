#1---------------------------------------------------------------------------------------------------------
"""
diccionario1 = {"huevo": 550, "papa": 1000, "aguacate": 2500, "comida gato": 7500, "comida perro": 10000}
producto = input("digite su compra")
print("--------------------------------------------------------------------------------------------------")
print(diccionario1.get(producto))
"""
#2---------------------------------------------------------------------------------------------------------
"""
nom = {"Juan": 1004077654, "Luis": 2003955411, "Tomas": 8005411290, "Nicolas": 3002866548 , "santiago": 1002766544, "Roberto": 4007780522, "Miguel": 5007419866, "Danny": 9008526433, "Mauricio": 1005088577, "shochan": 88007933510}
indentidad = input("ingrese nombre")
print("--------------------------------------------------------------------------------------------------")
print(nom.get(indentidad))
"""
#3--------------------------------------------------------------------------------------------------------
"""
continente = {"Europa": ( "ESPAÑA", "ISLANDIA", "KAZAJISTAN", "FINLANDIA", "IRLANDA"),
              "América": ("CANADÁ", "ESTADOS UNIDOS", "MEXICO", "CHILE", "COLOMBIA"),
              "Asia": ("LA MADRE RUSIA", "INDONESIA", "IRÁN", "AZERBAIYAN", "BARÉIN"),
              "África": ("ETIOPÍA", "MAURICIO", "ANGOLA", "EGIPTO", "LIBIA"),
              "Oceanía": ("Nauru", "Micronesia", "Australia", "Islas Marshall", "Zelanda")}

píases = input("ingrese su continente")
print("--------------------------------------------------------------------------------------------------")
for i in continente[píases]:
   print(píases, "=", i)
"""
#4---------------------------------------------------------------------------------------------------------

documento = input("ingrese documento")
nombre = input("ingrese nombre")
telefono = input("ingrese telefono")

print(documento, "Datos", pasiente [documento])
cita = input("desea cambiar el dia de su cita")

if cita == "si":
    fecha = input("este es el orario de su cita")
    print("este es el dia de su cita: ", fecha)
    
elif cita == "NO":
    fecha = print("su cita no esta disponible",)