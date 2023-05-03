import csv
class Registro:
    __Temperatura = 0.0
    __Humedad = 0
    __Presion = 0
    
    def __init__(self,tem,hum,pre):
        self.__Temperatura = tem
        self.__Humedad = hum
        self.__Presion = pre
    
    def Max_Min(self,mini,maxi):
        ban=0
        if self.__Temperatura < mini[0] and self.__Humedad < mini[1] and self.__mini[2]:
            mini[0] = self.__Temperatura
            mini[1] = self.__Humedad
            mini[2] = self.__Presion
    
            if self.__Temperatura > maxi[0] and self.__Humedad > maxi[1] and self.__Presion > maxi[2]:
                maxi[0] = self.__Temperatura
                maxi[1] = self.__Humedad
                maxi[2] = self.__Presion
                ban = 1
        
        return ban
    
    def temperatura(self):
        return self.__Temperatura
    
    def listar(self,i):
        print('{:20}{:20}{:20}{:20}'.format(i,self.__Temperatura,self.__Humedad,self.__Presion))
    


if __name__ == "'__main__":
    
    matriz = []
    lista = []
    
    archivo = open('RegistroMetereologico.cvs')
    reader = csv.reader(archivo,delimiter=';')
    for fila in reader:
        hora = Registro(fila[0],fila[1],fila[2])
        lista.append(hora)
        matriz.append(lista)
    
    archivo.close()
    
    opcion = ''
    while opcion == 's':
        opcion = input('\na-Mostrar menor y mayor valor\nb-Temperatura promedio mensual\nc-Mostrar por el dia\ns-Salir\n')
        
        if opcion == 'a':
            valor_min = [100,200,10000]
            valor_max = [-100,-200,-10000]
            
            for i in range(28):
                for j in range(24):
                    ban = matriz[i][j].Max_Min(valor_min,valor_max)
                    if ban == 1:
                        dia = i+1
                        hora = j+1
            
            print('El dia{}, a la hora {}, se registraron los valores maximos. Fueron'.format(dia,hora))
            print('Tempreratura: {}°\nHumedad:{}%\nPresion: {}Pa'.format(valor_max[0],valor_max[1],valor_max[2]))
            print('El dia{}, a la hora {}, se registraron los valores minimos. Fueron'.format(dia,hora))
            print('Tempreratura: {}°\nHumedad:{}%\nPresion: {}Pa\n'.format(valor_min[0],valor_min[1],valor_min[2]))
        
            print('\n¿Que desea hacer ahora?\n')
        
        elif opcion == 'b':
            for i in range(28):
                total = 0
                for j in range(24):
                    total = total + matriz[i][j].temperatura()
                
                print('la temperatura promedio del mes {}, es de {}\n'.format(i+1,total/24))
            
            
            print('¿Que desea hacer ahora?\n')
        
        elif opcion == 'c':
            dia = int(input('Ingrese el dia: '))
            print('{:20}{:20}{:20}{:20}'.format('Hora','Temperatura','Humedad','Presion'))
            for i in range(24):
                matriz[dia-1][i].listar(i)
                
                
            print('¿Que desea hacer ahora?\n')
        
        elif opcion == 's':
            print('--------FIN DEL PROGRAMA---------')
        
        else:
            print('Ingreso mal la opcion')
            
        
        
