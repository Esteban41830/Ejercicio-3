import csv
class Registro:
    __Temperatura = 0.0
    __Humedad = 0.0
    __Presion = 0.0
    
    def __init__(self,Temperatura,Humedad,Presion):
        self.__Temperatura = Temperatura
        self.__Humedad = Humedad
        self.__Presion = Presion

    def Maximos_y_Minimos(self,VMax,VMin):
        if (self.__Temperatura > VMax[0])and(self.__Humedad > VMax[1])and(self.__Presion > VMax):
            VMax[0] = self.__Temperatura
            VMax[1] = self.__Humedad
            VMax[2] = self.__Presion
        
        if (self.__Temperatura < VMin[0])and(self.__Humedad < VMin[1])and(self.__Presion < VMin):
            VMin[0] = self.__Temperatura
            VMin[1] = self.__Humedad
            VMin[2] = self.__Presion
        
    def TemperaturaPromedio(self):
        return self.__Temperatura
        
            
    def Listar(self,hora):
        print("{:20}{:20}{:20}{:20}".format("Hora","Temperatura","Humedad","Presion"))
        print("\n{:20}{:20}{:20}{:20}".format(hora,self.__Temperatura,self.__Humedad,self.__Presion))



if __name__ == '__main__':
  
  matriz = [[]]
  lista = []
  archivo = open('registro_Meterologico.csv')
  reader = csv.reader(archivo,delimiter=',')
  for fila in reader:
      hora = Registro(fila[0],fila[1],fila[2])
      lista.append(hora)
  
  archivo.close()
  matriz.append(lista)

  
  
  matriz[0].Mostrar()
  
  opcion = ''
  while opcion != 's':
      print('a)_Mostrar para cada variable el día y hora de menor y mayor valor.')
      print('b)_Indicar la temperatura promedio mensual por cada hora.')
      print('c)_listar los valores de las tres variables para cada hora del día dado.')
      print('s)_Salir')
      opcion = (input())
      
      if opcion == 's':
          break
      
      elif opcion == 'a':
          ListaValoresMaximos = [-50,-100,-2000]
          ListaValoresMinimos = [50,200,2000]
          for i in range(28):
              for j in range(24):
                  matriz[i][j].Maximos_y_Minimos(ListaValoresMaximos,ListaValoresMinimos)
                 
              print('Dia:{} Con valores maximos de:\nTemperatura: {}\nHumedad: {}\nPresion: {}'.format(
                      i+1,ListaValoresMaximos[0],ListaValoresMaximos[1],ListaValoresMaximos[2]))
              print('Y con valores minimos de:\nTemperatura: {}\nHumedad: {}\nPresion: {}'.format(
                      ListaValoresMinimos[0],ListaValoresMinimos[1],ListaValoresMinimos[2]))
      
      elif opcion == 'b':
          for i in range(28):
              total = 0
              for j in range(24):
                  total = total + matriz[i][j].TemperaturaPromedio()
            
              print('Para el dia {} la temperatura promedio fue de: {}'.format(i+1,total/24))
      
      elif opcion == 'c':
          dia = int(input('Ingrese el dia: '))
          for hora in range(24):
              matriz[dia-1][hora].Listar(hora)
            
      else:
          print('Error, opcion incorrecta')

  