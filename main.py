from claseManejdorCama import ManejadorCama
from claseManejadorMedicamentos import ManejadorMedicamento

if __name__ == '__main__':
    mc = ManejadorCama()
    mm = ManejadorMedicamento()

    mc.testListaCama()
    mm.testMedicamentos()

    idc = mc.darAlta()
    mc.

