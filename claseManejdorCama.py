from claseCama import Cama
import csv
from claseManejadorMedicamentos import
class ManejadorCama:
    __listaCamas = []

    def __init__(self):
        self.__listaCamas = []

    def testListaCama(self):
        archivo = open('camas.csv')
        reader = csv.reader(archivo, delimiter=';')
        bandera = True
        for linea in reader:
            if bandera:
                bandera = False
            else:
                idc = linea[0]
                hab = linea[1]
                est = linea[2]
                nom = linea[3]
                diag = linea[4]
                intern = linea[5]
                alta = linea[6]
                unaCama = Cama(idc,hab,est,nom,diag,intern,alta)
                self.cargaCama(unaCama)

    def cargaCama(self, unaCama):
        if type(unaCama) == Cama:
            self.__listaCamas.append(unaCama)

        else:
            print("Error de tipos en la carga.")


    def buscaPaciente(self):
        nombre = input('Ingrese el nombre del paciente que desea buscar. (Apellido, Nombre)\n ')
        bandera = True
        i = len(self.__listaCamas)
        retorno = 0
        while i >= 0 && bandera:
            if nombre == self.__listaCamas[i].getNom():
                retorno = self.__listaCamas[i]
                bandera = False
            else:
                i -= 1
        return retorno

    def darAlta(self):
        paciente = self.buscaPaciente()
        paciente.cargaAlta('09/05/2022')
        if type(paciente) == Cama:
            paciente.muestraPaciente()
        return paciente.getID()






