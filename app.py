import tkinter as tk
from tkinter import CENTER 

class AgeInputApp:
    def __init__(self, parent):
        self.parent = parent
        self.age_entries = []
        self.age_labels = []
        self.create_widgets()
        
    def create_widgets(self):
        self.parent.title("Age Input")
        tk.Label(self.parent, text="Enter the number of ages (max: 429):").pack()
        self.quant_idades_entry = tk.Entry(self.parent)
        self.quant_idades_entry.pack()
        tk.Button(self.parent, text="OK", command=self.create_age_inputs).pack()
        
    def create_age_inputs(self):
        try:
            quant_idades = int(self.quant_idades_entry.get())
            if quant_idades > 429:
                quant_idades = 429
        except ValueError:
            return
        
        self.parent.destroy()
        self.parent = tk.Tk()
        self.parent.title("Age Input")
    
        tk.Label(self.parent, text="Enter Ages:").grid(row=0, column=0)
        for i in range(quant_idades):
            row = i // 13+1
            col = i % 13
            age_label = tk.Label(self.parent, text=f"Age {i+1}: " , font=("Helvitica", 8))
            age_label.grid(row=row, column=col*14, sticky=tk.E)
            self.age_labels.append(age_label)
            age_entry = tk.Entry(self.parent)
            age_entry.grid(row=row, column=col*14+1, padx=5, pady=5)
            self.age_entries.append(age_entry)
    
        tk.Button(self.parent, text="Calculate" , font=("Helvetica", 8), command=self.calculate_ages).grid(row=row+1, column=round((col*14+1)), sticky=tk.E)

        
    def calculate_ages(self):
        idades = []
        for entry in self.age_entries:
            try:
                age = int(entry.get())
                idades.append(age)
            except ValueError:
                pass
        self.parent.destroy()
        AgeCalculationApp(idades)
        
        
class AgeCalculationApp:
    def __init__(self, idades):
        self.idades = idades
        self.create_widgets()
        
    def create_widgets(self):
        self.parent = tk.Tk()
        self.parent.title("Age Calculations")
        tk.Label(self.parent, text=f"Ages: {self.idades}").pack()
        tk.Button(self.parent, text="Calculate Mean", command=self.calculate_mean).pack()
        tk.Button(self.parent, text="Calculate Median", command=self.calculate_median).pack()
        tk.Button(self.parent, text="Calculate Mode", command=self.calculate_mode).pack()
        
    def calculate_mean(self):
        soma = 0
        for idade in self.idades:
            soma += idade
        media = soma/len(self.idades)
        tk.Label(self.parent, text=f"Mean: {round(media, 2)}").pack()
        
    def calculate_median(self):
        sorted_idades = sorted(self.idades)
        if len(sorted_idades)%2 !=0:
            indice_mediana = int(len(sorted_idades)/2)
            tk.Label(self.parent, text=f"Median: {sorted_idades[indice_mediana]}").pack()
        else:
            indice1 = int(len(sorted_idades)/2)
            indice2 = indice1 - 1
            soma = sorted_idades[indice1] + sorted_idades[indice2]
            mediana = soma/2
            tk.Label(self.parent, text=f"Median: {round(mediana, 2)}").pack()
        
    def calculate_mode(self):
        repete = [0]*len(self.idades)
        conta = 0
        for i in range(len(self.idades)):
            for j in range(i+1, len(self.idades)):
                if self.idades[i] == self.idades[j]:
                    repete[i] +=1
                    if repete[i] > conta:
                        conta = repete[i]
                        moda  = self.idades[i]
            repete[i] = 0
        if conta == 0:
            tk.Label(self.parent, text="The list has no mode").pack()
        else:
            tk.Label(self.parent, text=f"Mode: {moda}").pack()
            
        self.parent.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgeInputApp(root)
    root.mainloop()
