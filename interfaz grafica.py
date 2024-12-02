import tkinter as tk
from tkinter import messagebox


class ConsumoAguaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Consumo de Agua")

        self.label_anterior = tk.Label(root, text="Lectura anterior (m³):")
        self.label_anterior.grid(row=0, column=0, padx=10, pady=10)

        self.entry_anterior = tk.Entry(root)
        self.entry_anterior.grid(row=0, column=1, padx=10, pady=10)

        self.label_actual = tk.Label(root, text="Lectura actual (m³):")
        self.label_actual.grid(row=1, column=0, padx=10, pady=10)

        self.entry_actual = tk.Entry(root)
        self.entry_actual.grid(row=1, column=1, padx=10, pady=10)

        self.label_tarifa = tk.Label(root, text="Tarifa (por m³):")
        self.label_tarifa.grid(row=2, column=0, padx=10, pady=10)

        self.entry_tarifa = tk.Entry(root)
        self.entry_tarifa.grid(row=2, column=1, padx=10, pady=10)

        self.button_calcular = tk.Button(root, text="Calcular", command=self.calcular_monto)
        self.button_calcular.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def calcular_monto(self):
        try:
            lectura_anterior = float(self.entry_anterior.get())
            lectura_actual = float(self.entry_actual.get())
            tarifa = float(self.entry_tarifa.get())
            consumo = lectura_actual - lectura_anterior
            if consumo < 0:
                raise ValueError("La lectura actual debe ser mayor que la lectura anterior.")
            monto = consumo * tarifa
            messagebox.showinfo("Monto a Pagar", f"Consumo: {consumo:.2f} m³\nMonto a pagar: ${monto:.2f}")
        except ValueError as e:
            messagebox.showerror("Error", f"Entrada inválida: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ConsumoAguaApp(root)
    root.mainloop()
