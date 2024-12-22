import sys
import math

# Definir las funciones que los comandos ejecutarán
def cx_wlcm():
    print("Hola, bienvenido a CommandX")

def cx_plus(args):
    try:
        # Convertir los argumentos en números y sumarlos
        numeros = list(map(int, args))
        print(f"El resultado de la suma es: {sum(numeros)}")
    except ValueError:
        print("Error: Debes ingresar solo números enteros.")


def cx_rest(args):
    try:
        # Convertir los argumentos en números y restarlos
        numeros = list(map(int, args))
        resultado = numeros[0]
        for num in numeros[1:]:
            resultado -= num
        print(f"El resultado de la resta es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar solo números enteros.")

def cx_mult(args):
    try:
        numeros = list(map(int, args))
        resultado = 1
        for num in numeros:
            resultado *= num
        print(f"El resultado de la multiplicacion es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar solo numeros enteros")

def cx_div(args):
    try:
        numeros = list(map(int, args))
        resultado = numeros[0]
        for num in numeros[1:]:
            if num == 0:
                print("Error: No se puede dividir entre cero.")
                return
            resultado /= num
        print(f"El resultado de la division es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar solo numeros enteros")
    except ZeroDivisionError:
        print("Error: No se puede divir entre cero")

def cx_ptnc(args):
    try:
        base = int(args[0])
        exponente = int(args[1])
        resultado = base ** exponente
        print(f"El resultado de la potencia es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar solo numeros enteros")
    except IndexError:
        print("Error: Debes proporcionar dos numeros, uno para la base y otro para el exponente")

def cx_srqt(args):
    try:
        numero = int(args[0])
        if numero < 0:
            print("Error: No se puede calcular la raiz cuadrada de un numero negativo")
        else:
            resultado = math.sqrt(numero)
            print(f"El resultado de la raiz cuadrada es: {resultado}")
    except ValueError:
        print("Error: Debes ingresar un numero entero")
    except IndexError:
        print("Error: Debes proporcionar un número para calcular su raíz cuadrada.")

def cx_help():
    # Mostrar todos los comandos disponibles
    print("""
Comandos disponibles:
- cx_wlcm: Muestra un saludo de bienvenida.
- cx_plus [num1 num2 ...]: Suma los números proporcionados.
- cx_rest [num1 num2 ...]: Resta los números proporcionados.
- cx_mult [num1 num2 ...]: Multiplica los números proporcionados.
- cx_div [num1 num2 ...]: Divide el primer número por los demás.
- cx_ptnc [base exponente]: Calcula la potencia de la base elevada al exponente.
- cx_sqrt [num]: Calcula la raíz cuadrada del número proporcionado.
- cx_rept [texto]: Repite el texto proporcionado.
- cx_exit: Sale de la terminal.
""")

def cx_rept(args):
    # Repetir lo que se pasa como argumento
    if args:
        print(" ".join(args))
    else:
        print("Error: Debes proporcionar algo para repetir.")

def cx_exit():
    print("Saliendo de CommandX...")
    sys.exit(0)

# Diccionario que asocia comandos con sus funciones
comandos = {
    "cx_wlcm": cx_wlcm,
    "cx_plus": cx_plus,
    "cx_rest": cx_rest,
    "cx_mult": cx_mult,
    "cx_div": cx_div,
    "cx_ptnc": cx_ptnc,
    "cx_sqrt": cx_srqt,
    "cx_rept": cx_rept,
    "cx_exit": cx_exit,
    "cx_help": cx_help,
}

# Función principal para manejar la entrada de usuario
def terminal_personalizada():
    while True:
        # Leer el comando
        comando = input("CommandX> ").strip()

        # Verificar si el comando existe
        if comando.startswith("cx_"):
            partes = comando.split()
            nombre_comando = partes[0]
            args = partes[1:]  # Los argumentos son todo después del comando

            if nombre_comando in comandos:
                # Si el comando no requiere argumentos, no pasarlos
                if nombre_comando in ["cx_wlcm", "cx_exit", "cx_help"]:
                    comandos[nombre_comando]()  # Ejecuta sin argumentos
                else:
                    comandos[nombre_comando](args)  # Ejecuta con argumentos
            else:
                print(f"Comando desconocido: {comando}. Usa 'cx_help' para ver los comandos disponibles")
        else:
            print("Error: Los comandos deben comenzar con 'cx_'")

# Iniciar la terminal personalizada
if __name__ == "__main__":
    terminal_personalizada()
