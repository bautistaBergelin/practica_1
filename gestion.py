# Inicializacion del inventario
inventory = {}
# Creacion del mensaje de opciones
options = ("agregar un producto ", "eliminar un producto ", "mostrar inventario ", "salir")
# Funcion para imprimir las opciones
def print_options():
    print("seleccione una opcion:")
    for i,option in enumerate(options):
        print(f"{i + 1}. {option}")
#inicio de programa
while True:
    print("")
    print_options()
    entry = (input())
    if entry == "1":
        product = input("ingrese el nombre de producto a agregar ")
        if inventory.get(product, "no esta") == "no esta":
            quantity = int(input("ingrese la cantidad a ingresar "))
            inventory[product] = quantity
        else:
            print("el producto ya existe")
    elif entry =="2":
        product = input("ingrese el nombre de producto a eliminar ")
        if inventory.get(product, "no esta") != "no esta":
            inventory.pop(product)
        else:
            print("el producto no existe en el inventario")
    elif entry =="3":
        for i,j in inventory.items():
            print(f"producto: {i} cantidad: {j}")
    elif entry == "4":
        break
    else:
        print("ingrese un numero valido")
    
    