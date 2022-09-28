from reporteine import ReporteINE
from time import time
from datosipc import datosIPC

if __name__ == "__main__":
    t = time()
    datos = datosIPC(8, 2022)
    reporte = ReporteINE(
        nombre="Prueba_IPC"
    )
# capitulo 2
    reporte.agregar_capitulo(
        titulo="Variables exógenas"
    )
    subcap_data = datos.indice_precio_alimentos()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Precio internacional de los alimentos",
        titulo_grafico="Índice de precios de los alimentos de la FAO",
        descripcion_grafico="Indicador internacional, serie histórica, adimensional",
        descripcion=subcap_data[1],
        fuente="FAO",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico=dict(Q4Etiquetas=True)
    )

    subcap_data = datos.petroleo()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Precio del pretróleo",
        titulo_grafico="Precio promedio mensual del barril del petróleo",
        descripcion_grafico="Indicador internacional, serie histórica, en dólares por barril",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.cambio_quetzal()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Cambio del quetzal",
        titulo_grafico="Tipo de cambio nominal promedio",
        descripcion_grafico="República de Guatemala, serie histórica, en quetzales por dólar estadounidense",
        descripcion=subcap_data[1],
        fuente="Banco de Guatemala",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.tasa_interes()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Tasa de interés",
        titulo_grafico="Tasas de interés activa bancaria",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="Banco de Guatemala",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.ipc_usa()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Índice de precios al consumidor de EE.UU.",
        titulo_grafico="Variación interanual del IPC de Estados Unidos de América",
        descripcion_grafico="Estados Unidos de América, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )

    subcap_data = datos.ipc_mex()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Índice de precios al consumidor de México",
        titulo_grafico="Variación interanual del IPC de México",
        descripcion_grafico="Estados Unidos Mexicanos, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="FRED",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.inflacion()
    reporte.agregar_subcapitulo(
        indice_capitulo=0,
        titulo="Inflación en Centro América, República Dominicana y México",
        titulo_grafico="Tasa de variación interanual del IPC de los países Centroamericanos, República Dominicana y México",
        descripcion_grafico="Centro América, República Dominicana y México, meses seleccionados, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="tabla",
        data=subcap_data[0],
        opciones_grafico={"precision":2}
    )
# capitulo 3
    reporte.agregar_capitulo(
        titulo="Resultados del IPC"
    )
    subcap_data = datos.serie_IPC(0)
    reporte.agregar_subcapitulo(
        indice_capitulo=1,
        titulo="Evolución del IPC",
        titulo_grafico="IPC, base diciembre del 2010",
        descripcion_grafico="República de Guatemala, Serie histórica 1 año, adimensional",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'interanual')
    reporte.agregar_subcapitulo(
        indice_capitulo=1,
        titulo="Evolución del cambio anual del IPC",
        titulo_grafico="Variación interanual del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'acumulada')
    reporte.agregar_subcapitulo(
        indice_capitulo=1,
        titulo="Evolución del cambio acumulado del IPC",
        titulo_grafico="Variación acumulada del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_inflacion(0, 'intermensual')
    reporte.agregar_subcapitulo(
        indice_capitulo=1,
        titulo="Evolución del cambio mensual del IPC",
        titulo_grafico="Variación intermensual del IPC",
        descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
    subcap_data = datos.serie_poder_adquisitivo(0)
    reporte.agregar_subcapitulo(
        indice_capitulo=1,
        titulo="Valor del dinero",
        titulo_grafico="Poder adquisitivo del quetzal",
        descripcion_grafico="República de Guatemala, serie histórica mensual, en porcentaje",
        descripcion=subcap_data[1],
        fuente="INE",
        tipo_grafico="lineal",
        data=subcap_data[0],
        opciones_grafico={"precision":2, "Q4Etiquetas":True}
    )
#capitulo 4
    reporte.agregar_capitulo(
        titulo="Serie histórica de índices a nivel nacional de todos los gastos básicos"
    )
    datos_gba = datos.series_Gba(0)
    for Gba in datos_gba:
        nombre = Gba[0]
        datos = Gba[1]
        desc = Gba[2]
        reporte.agregar_subcapitulo(
            indice_capitulo=2,
            titulo=f"Evolución del IPC del gasto basico {nombre}",
            titulo_grafico="IPC, base diciembre del 2010",
            descripcion_grafico="República de Guatemala, Serie histórica 1 año, adimensional",
            descripcion=desc,
            fuente="INE",
            tipo_grafico="lineal",
            data=datos,
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
# capitulos 5 a 12
    region = {
        1: 'I',
        2: 'II',
        3: 'III',
        4: 'VI',
        5: 'V',
        6: 'VI',
        7: 'VII',
        8: 'VIII'
    }
    indice_inicial = 3
    for i in range(1, 9):
        indice = indice_inicial + i - 1
        reporte.agregar_capitulo(
            titulo=f"Resultados del IPC para la region {region[i]}"
        )
        subcap_data = datos.serie_IPC(i)
        reporte.agregar_subcapitulo(
            indice_capitulo=indice,
            titulo="Evolución del IPC",
            titulo_grafico="IPC, base diciembre del 2010",
            descripcion_grafico="República de Guatemala, Serie histórica 1 año, adimensional",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(i, 'interanual')
        reporte.agregar_subcapitulo(
            indice_capitulo=indice,
            titulo="Evolución del cambio anual del IPC",
            titulo_grafico="Variación interanual del IPC",
            descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(i, 'acumulada')
        reporte.agregar_subcapitulo(
            indice_capitulo=indice,
            titulo="Evolución del cambio acumulado del IPC",
            titulo_grafico="Variación acumulada del IPC",
            descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_inflacion(i, 'intermensual')
        reporte.agregar_subcapitulo(
            indice_capitulo=indice,
            titulo="Evolución del cambio mensual del IPC",
            titulo_grafico="Variación intermensual del IPC",
            descripcion_grafico="República de Guatemala, serie histórica, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
        subcap_data = datos.serie_poder_adquisitivo(i)
        reporte.agregar_subcapitulo(
            indice_capitulo=indice,
            titulo="Valor del dinero",
            titulo_grafico="Poder adquisitivo del quetzal",
            descripcion_grafico="República de Guatemala, serie histórica mensual, en porcentaje",
            descripcion=subcap_data[1],
            fuente="INE",
            tipo_grafico="lineal",
            data=subcap_data[0],
            opciones_grafico={"precision":2, "Q4Etiquetas":True}
        )
    reporte.crear_reporte()
    #reporte.compilar_reporte()
    tf = time()
    print(f"[{tf-t:.2f} s]")