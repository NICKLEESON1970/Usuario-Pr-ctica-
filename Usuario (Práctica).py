
class Usuario:
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = 30000
        self.saldo_pagar = 0

    def hacer_compra(self, monto):  
        if self.saldo_pagar + monto <= self.limite_credito:
            self.saldo_pagar += monto  
            print(f"Compra de ${monto} realizada con éxito para {self.nombre} {self.apellido}.")
        else:
            print(f"Compra de ${monto} excede el límite de crédito para {self.nombre} {self.apellido}.")

    def pagar_tarjeta(self, monto):  
        if monto > 0 and monto <= self.saldo_pagar:
            self.saldo_pagar -= monto  
            print(f"Pago de ${monto} realizado con éxito para {self.nombre} {self.apellido}.")
        elif monto <= 0:
            print("Monto de pago debe ser mayor a cero.")
        else:
            print(f"No hay suficiente saldo a pagar para realizar un pago de ${monto} para {self.nombre} {self.apellido}.")

    def mostrar_saldo_usuario(self):  
        print(f"Usuario: {self.nombre} {self.apellido}, Saldo a Pagar: ${self.saldo_pagar}")

    def transferir_deuda(self, otro_usuario, monto):  
        if monto > 0 and monto <= self.saldo_pagar:
            self.saldo_pagar -= monto  
            otro_usuario.saldo_pagar += monto  
            print(f"Transferencia de deuda de ${monto} de {self.nombre} {self.apellido} a {otro_usuario.nombre} {otro_usuario.apellido} realizada con éxito.")
        elif monto <= 0:
            print("Monto de transferencia debe ser mayor a cero.")
        else:
            print(f"No hay suficiente saldo a pagar para realizar una transferencia de ${monto} para {self.nombre} {self.apellido}.")


# Crear 3 instancias de la clase Usuario
usuario1 = Usuario("Nariyoshi", "Miyagi", "nariyoshi.miyagi@example.com")
usuario2 = Usuario("Daniel", "LaRusso", "daniel.larusso@example.com")
usuario3 = Usuario("Johnny", "Lawrence", "johnny.lawrence@example.com")


# Simulaciones de compras y pagos
print("\n**Simulación de Compras y Pagos**")

# Usuario 1: 2 compras y 1 pago
usuario1.hacer_compra(1000)
usuario1.hacer_compra(2000)
usuario1.mostrar_saldo_usuario()
usuario1.pagar_tarjeta(2500)
usuario1.mostrar_saldo_usuario()

print("\n---")

# Usuario 2: 1 compra y 2 pagos
usuario2.hacer_compra(500)
usuario2.mostrar_saldo_usuario()
usuario2.pagar_tarjeta(200)
usuario2.pagar_tarjeta(300)
usuario2.mostrar_saldo_usuario()

print("\n---")

# Usuario 3: 3 compras y 4 pagos
usuario3.hacer_compra(1500)
usuario3.hacer_compra(2500)
usuario3.hacer_compra(1000)
usuario3.mostrar_saldo_usuario()
usuario3.pagar_tarjeta(500)
usuario3.pagar_tarjeta(1000)
usuario3.pagar_tarjeta(1500)
usuario3.pagar_tarjeta(2000)
usuario3.mostrar_saldo_usuario()