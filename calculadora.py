import tkinter as tk

def calcular():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    operacion = operacion_var.get()
    
    if operacion == "Suma":
        resultado.set(num1 + num2)
    elif operacion == "Resta":
        resultado.set(num1 - num2)
    elif operacion == "División":
        if num2 == 0:
            resultado.set("Bro, si sabes que no se puede dividir entre cero, cierto... ¿Cierto?")
        else:
            resultado.set(num1 / num2)
    elif operacion == "Multiplicación":
        resultado.set(num1 * num2)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Variables para almacenar los números y el resultado
resultado = tk.StringVar()
resultado.set("Resultado")

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, textvariable=resultado)
label_resultado.pack()

# Entradas para los números
entry_num1 = tk.Entry(ventana)
entry_num2 = tk.Entry(ventana)
entry_num1.pack()
entry_num2.pack()

# Opciones para la operación
operacion_var = tk.StringVar()
operacion_var.set("Suma")
opcion_suma = tk.Radiobutton(ventana, text="Suma", variable=operacion_var, value="Suma")
opcion_resta = tk.Radiobutton(ventana, text="Resta", variable=operacion_var, value="Resta")
opcion_division = tk.Radiobutton(ventana, text="División", variable=operacion_var, value="División")
opcion_multiplicacion = tk.Radiobutton(ventana, text="Multiplicación", variable=operacion_var, value="Multiplicación")
opcion_suma.pack()
opcion_resta.pack()
opcion_division.pack()
opcion_multiplicacion.pack()

# Botón para calcular
boton_calcular = tk.Button(ventana, text="Efectuar Cálculo", command=calcular)
boton_calcular.pack()

# Ejecutar la aplicación
ventana.mainloop()