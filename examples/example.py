import GlassConversionPy as gc
import pandas as pd

a = {"CaO": 50, "MgO": 10, "Al2O3": 40}
b = {"CaO": [50], "MgO": [10], "Al2O3": [40]}
df = pd.DataFrame(b)

# mol% to weight%
print(gc.M2W(a))
print(gc.M2W(b))
print(gc.M2W(df))

# weight% to mol%
print(gc.W2M(a))
print(gc.W2M(b))
print(gc.W2M(df))
