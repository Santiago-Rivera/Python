"""
Crea un programa que solicite dos numeros y una operación (+, -, *, /) y muestre el resultado. Incluye manejo de división por cero.
"""

def operacion():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        if num2 == 0:
            print("Error: División por cero no permitida.")
            return
        else:
            resultado = num1 / num2
    else:
        print("Operación no válida.")
        return

    print(f"El resultado de {num1} {operacion} {num2} es: {resultado}")
    
if __name__ == "__main__":
    operacion()