import os
os.environ["R_HOME"] = r"C:\Program Files\R\R-4.2.1" # change as needed
import rpy2.robjects.packages as rpackages
import rpy2.robjects as robjects

class FuncionesINE:
    def __init__(self) -> None:
        devtools = rpackages.importr('devtools')
        devtools.install_github("1u1s4/funcionesINE")
        self.__funcionesINE = rpackages.importr('funcionesINE')
        self.__datos = list
        self.Qanual = True

    def cargaMasiva(self, csv_path: str) -> None:
        self.__datos = self.__funcionesINE.cargaMasiva(csv_path, codificacion='utf-8')

    def escribirCSV(self, ruta_libro: str, ruta_salida: str) -> None:
        self.__funcionesINE.escribirCSV(
            lista=self.__funcionesINE.leerLibro(ruta=ruta_libro),
            ruta=ruta_salida
            )

    def escribirCSVcocinado(self, ruta_libro: str, ruta_salida: str) -> None:
        self.__funcionesINE.escribirCSV(
            lista=self.__funcionesINE.leerLibroNormal(ruta=ruta_libro),
            ruta=ruta_salida
            )

    def graficaLinea(
        self,
        data_index: int,
        ruta_salida: str,
        nombre: str,
        inicio: int = -1,
        ancho: float = 1.5,
        precision: int = 1,
        escala: str = "normal",
        rotar: bool = True,
        final = None,
        Q4Etiquetas: bool = False) -> None:
        if self.Qanual:
            self.__funcionesINE.anual(
                robjects.r("rgb(0,0,1)"),
                robjects.r("rgb(0.6156862745098039,0.7333333333333333,1)")
            )
        if Q4Etiquetas:
            self.__funcionesINE.cuatroEtiquetas()
        if rotar:
            rotar = robjects.r("T")
        else:
            rotar = robjects.r("F")
        if final is None:
            final = robjects.r("NA")
        self.__funcionesINE.exportarLatex(
            ruta_salida + f"/{nombre}.tex",
            self.__funcionesINE.graficaLinea(
                self.__datos[data_index],
                inicio=inicio,
                ancho=ancho,
                precision=precision,
                escala=escala,
                rotar=rotar,
                final=final
            )
        )
