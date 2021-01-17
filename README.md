## GlassConversionPy
Library to do simple conversions in glass science.

### Installation
**Using pip**
```
pip install GlassConversionPy
```

### Example
```
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
```


**Output**
```
{'CaO': 38.48644068551324, 'MgO': 5.5322414016046695, 'Al2O3': 55.9813179128821}
{'CaO': array([38.48644069]), 'MgO': array([5.5322414]), 'Al2O3': array([55.98131791])}
{'CaO': 38.48644068551324, 'MgO': 5.53224140160467, 'Al2O3': 55.98131791288211}
         CaO       MgO      Al2O3
0  38.486441  5.532241  55.981318
{'CaO': 58.19834334911537, 'MgO': 16.194861552145408, 'Al2O3': 25.60679509873923}
{'CaO': array([58.19834335]), 'MgO': array([16.19486155]), 'Al2O3': array([25.6067951])}
{'CaO': 58.19834334911537, 'MgO': 16.19486155214541, 'Al2O3': 25.60679509873923}
         CaO        MgO      Al2O3
0  58.198343  16.194862  25.606795
63.683813856
60.083
{'Na2O': 0.1, 'K2O': 0.1, 'SiO2': 0.8}
```
