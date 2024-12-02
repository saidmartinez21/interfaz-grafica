class ReciboAgua:
    # Precondiciones + Postcondiciones de los casos de uso
    # Atributos: Encapsulacion 
    __lecturaAnterior=0.0
    __lecturaActual=0.0
    __tarifa=0
    __montoPagar=0.0
    
    # Metodos: 1 metodo por cada caso de uso
    # def nombreCasoUso(self,parametros(precondiciones separadas con ',')):
    def calculoMontoPagar(self,lecrturaAnterior,lecturaActual,tarifa):
        self.__lecturaAnterior=lecrturaAnterior
        self__lecturaActual=lecturaActual
        self.__tarifa=tarifa
        self.__montoPagar=self.__lecturaAnterior-lecturaActual*(tarifa)
        return self.__montoPagar
    
        
        