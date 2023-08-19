import tkinter as tk

# Dictionary of atomic masses (in g/mol)
elements_data = {
    'H': 1.008, 'He': 4.0026, 'Li': 6.94, 'Be': 9.0122, 'B': 10.81,
    'C': 12.01, 'N': 14.01, 'O': 16.00, 'F': 19.00, 'Ne': 20.18,
    'Na': 22.99, 'Mg': 24.31, 'Al': 26.98, 'Si': 28.09, 'P': 30.97,
    'S': 32.07, 'Cl': 35.45, 'Ar': 39.95, 'K': 39.10, 'Ca': 40.08,
    'Sc': 44.96, 'Ti': 47.87, 'V': 50.94, 'Cr': 52.00, 'Mn': 54.94,
    'Fe': 55.85, 'Ni': 58.69, 'Co': 58.93, 'Cu': 63.55, 'Zn': 65.38,
    'Ga': 69.72, 'Ge': 72.63, 'As': 74.92, 'Se': 78.96, 'Br': 79.90,
    'Kr': 83.80, 'Rb': 85.47, 'Sr': 87.62, 'Y': 88.91, 'Zr': 91.22,
    'Nb': 92.91, 'Mo': 95.95, 'Tc': 98.00, 'Ru': 101.07, 'Rh': 102.91,
    'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.71,
    'Sb': 121.76, 'Te': 127.60, 'I': 126.90, 'Xe': 131.29, 'Cs': 132.91,
    'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24,
    'Pm': 145.00, 'Sm': 150.36, 'Eu': 152.00, 'Gd': 157.25, 'Tb': 158.93,
    'Dy': 162.50, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05,
    'Lu': 175.00, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21,
    'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59,
    'Tl': 204.38, 'Pb': 207.20, 'Bi': 208.98, 'Th': 232.04, 'Pa': 231.04,
    'U': 238.03, 'Np': 237.00, 'Pu': 244.00, 'Am': 243.00, 'Cm': 247.00,
    'Bk': 247.00, 'Cf': 251.00, 'Es': 252.00, 'Fm': 257.00, 'Md': 258.00,
    'No': 259.00, 'Lr': 262.00, 'Rf': 267.00, 'Db': 270.00, 'Sg': 271.00,
    'Bh': 270.00, 'Hs': 277.00, 'Mt': 276.00, 'Ds': 281.00, 'Rg': 280.00,
    'Cn': 285.00, 'Nh': 284.00, 'Fl': 289.00, 'Mc': 288.00, 'Lv': 293.00,
    'Ts': 294.00, 'Og': 294.00
}

class MolarMassCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chemical Molar Mass Calculator")

        self.label = tk.Label(root, text="Enter a chemical formula: (Match the case)")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.calculate_button = tk.Button(root, text="Calculate", command=self.calculate)
        self.calculate_button.pack()

        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def calculate(self):
        formula = self.entry.get()
        molar_mass = self.calculate_molar_mass(formula)
        self.result_label.config(text=f"The molar mass of {formula} is {molar_mass:.4f} g/mol.")

    def calculate_molar_mass(self, chemical_formula):
        total_mass = 0
        current_element = ""
        current_count = ""

        i = 0
        while i < len(chemical_formula):
            char = chemical_formula[i]

            if char.isalpha():
                current_element = char

                if i + 1 < len(chemical_formula) and chemical_formula[i + 1].islower():
                    current_element += chemical_formula[i + 1]
                    i += 1

                if current_count:
                    count = int(current_count)
                else:
                    count = 1

                total_mass += elements_data[current_element] * count
                current_element = ""
                current_count = ""
            elif char.isdigit():
                current_count += char

            i += 1

        return total_mass

def main():
    root = tk.Tk()
    app = MolarMassCalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
