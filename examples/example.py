import GlassConversionPy as gc
import pandas as pd

a = {"CaO": 50, "MgO": 10, "Al2O3": 40}
b = {"CaO": [50], "MgO": [10], "Al2O3": [40]}
c = "50CaO-10MgO-40Al2O3"
df = pd.DataFrame(b)

# mol% to weight%
print(gc.mol2weight(a))
print(gc.mol2weight(b))
print(gc.mol2weight(c))
print(gc.mol2weight(df))

# weight% to mol%
print(gc.weight2mol(a))
print(gc.weight2mol(b))
print(gc.weight2mol(c))
print(gc.weight2mol(df))

# extra
print(gc.get_molar_mass("10Na2O-10K2O-80SiO2"))
print(gc.molar_mass("SiO2"))
print(gc.formula2components("0.1Na2O-0.1K2O-0.8SiO2"))
