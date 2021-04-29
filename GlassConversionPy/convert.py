#imports
import numpy as np
import pandas
import pandas as pd

fprecision = 2

table = {'H': {'name': 'Hydrogen', 'mass': 1.008}, 'He': {'name': 'Helium', 'mass': 4.002602}, 'Li': {'name': 'Lithium', 'mass': 6.94}, 'Be': {'name': 'Beryllium', 'mass': 9.0121831}, 'B': {'name': 'Boron', 'mass': 10.81}, 'C': {'name': 'Carbon', 'mass': 12.011}, 'N': {'name': 'Nitrogen', 'mass': 14.007}, 'O': {'name': 'Oxygen', 'mass': 15.999}, 'F': {'name': 'Fluorine', 'mass': 18.998403163}, 'Ne': {'name': 'Neon', 'mass': 20.1797}, 'Na': {'name': 'Sodium', 'mass': 22.98976928}, 'Mg': {'name': 'Magnesium', 'mass': 24.305}, 'Al': {'name': 'Aluminum', 'mass': 26.9815385}, 'Si': {'name': 'Silicon', 'mass': 28.085}, 'P': {'name': 'Phosphorus', 'mass': 30.973761998}, 'S': {'name': 'Sulfur', 'mass': 32.06}, 'Cl': {'name': 'Chlorine', 'mass': 35.45}, 'Ar': {'name': 'Argon', 'mass': 39.948}, 'K': {'name': 'Potassium', 'mass': 39.0983}, 'Ca': {'name': 'Calcium', 'mass': 40.078}, 'Sc': {'name': 'Scandium', 'mass': 44.955908}, 'Ti': {'name': 'Titanium', 'mass': 47.867}, 'V': {'name': 'Vanadium', 'mass': 50.9415}, 'Cr': {'name': 'Chromium', 'mass': 51.9961}, 'Mn': {'name': 'Manganese', 'mass': 54.938044}, 'Fe': {'name': 'Iron', 'mass': 55.845}, 'Co': {'name': 'Cobalt', 'mass': 58.933194}, 'Ni': {'name': 'Nickel', 'mass': 58.6934}, 'Cu': {'name': 'Copper', 'mass': 63.546}, 'Zn': {'name': 'Zinc', 'mass': 65.38}, 'Ga': {'name': 'Gallium', 'mass': 69.723}, 'Ge': {'name': 'Germanium', 'mass': 72.63}, 'As': {'name': 'Arsenic', 'mass': 74.921595}, 'Se': {'name': 'Selenium', 'mass': 78.971}, 'Br': {'name': 'Bromine', 'mass': 79.904}, 'Kr': {'name': 'Krypton', 'mass': 83.798}, 'Rb': {'name': 'Rubidium', 'mass': 85.4678}, 'Sr': {'name': 'Strontium', 'mass': 87.62}, 'Y': {'name': 'Yttrium', 'mass': 88.90584}, 'Zr': {'name': 'Zirconium', 'mass': 91.224}, 'Nb': {'name': 'Niobium', 'mass': 92.90637}, 'Mo': {'name': 'Molybdenum', 'mass': 95.95}, 'Tc': {'name': 'Technetium', 'mass': 97.90721}, 'Ru': {'name': 'Ruthenium', 'mass': 101.07}, 'Rh': {'name': 'Rhodium', 'mass': 102.9055}, 'Pd': {'name': 'Palladium', 'mass': 106.42}, 'Ag': {'name': 'Silver', 'mass': 107.8682}, 'Cd': {'name': 'Cadmium', 'mass': 112.414}, 'In': {'name': 'Indium', 'mass': 114.818}, 'Sn': {'name': 'Tin', 'mass': 118.71}, 'Sb': {'name': 'Antimony', 'mass': 121.76}, 'Te': {'name': 'Tellurium', 'mass': 127.6}, 'I': {'name': 'Iodine', 'mass': 126.90447}, 'Xe': {'name': 'Xenon', 'mass': 131.293}, 'Cs': {'name': 'Cesium', 'mass': 132.90545196}, 'Ba': {'name': 'Barium', 'mass': 137.327}, 'La': {'name': 'Lanthanum', 'mass': 138.90547}, 'Ce': {'name': 'Cerium', 'mass': 140.116}, 'Pr': {'name': 'Praseodymium', 'mass': 140.90766}, 'Nd': {'name': 'Neodymium', 'mass': 144.242}, 'Pm': {'name': 'Promethium', 'mass': 144.91276}, 'Sm': {'name': 'Samarium', 'mass': 150.36}, 'Eu': {'name': 'Europium', 'mass': 151.964}, 'Gd': {'name': 'Gadolinium', 'mass': 157.25}, 'Tb': {'name': 'Terbium', 'mass': 158.92535}, 'Dy': {'name': 'Dysprosium', 'mass': 162.5}, 'Ho': {'name': 'Holmium', 'mass': 164.93033}, 'Er': {'name': 'Erbium', 'mass': 167.259}, 'Tm': {'name': 'Thulium', 'mass': 168.93422}, 'Yb': {'name': 'Ytterbium', 'mass': 173.045}, 'Lu': {'name': 'Lutetium', 'mass': 174.9668}, 'Hf': {'name': 'Hafnium', 'mass': 178.49}, 'Ta': {'name': 'Tantalum', 'mass': 180.94788}, 'W': {'name': 'Tungsten', 'mass': 183.84}, 'Re': {'name': 'Rhenium', 'mass': 186.207}, 'Os': {'name': 'Osmium', 'mass': 190.23}, 'Ir': {'name': 'Iridium', 'mass': 192.217}, 'Pt': {'name': 'Platinum', 'mass': 195.084}, 'Au': {'name': 'Gold', 'mass': 196.966569}, 'Hg': {'name': 'Mercury', 'mass': 200.592}, 'Tl': {'name': 'Thallium', 'mass': 204.38}, 'Pb': {'name': 'Lead', 'mass': 207.2}, 'Bi': {'name': 'Bismuth', 'mass': 208.9804}, 'Po': {'name': 'Polonium', 'mass': 209.0}, 'At': {'name': 'Astatine', 'mass': 210.0}, 'Rn': {'name': 'Radon', 'mass': 222.0}, 'Fr': {'name': 'Francium', 'mass': 223.0}, 'Ra': {'name': 'Radium', 'mass': 226.0}, 'Ac': {'name': 'Actinium', 'mass': 227.0}, 'Th': {'name': 'Thorium', 'mass': 232.0377}, 'Pa': {'name': 'Protactinium', 'mass': 231.03588}, 'U': {'name': 'Uranium', 'mass': 238.02891}, 'Np': {'name': 'Neptunium', 'mass': 237.0}, 'Pu': {'name': 'Plutonium', 'mass': 244.0}, 'Am': {'name': 'Americium', 'mass': 243.0}, 'Cm': {'name': 'Curium', 'mass': 247.0}, 'Bk': {'name': 'Berkelium', 'mass': 247.0}, 'Cf': {'name': 'Californium', 'mass': 251.0}, 'Es': {'name': 'Einsteinium', 'mass': 252.0}, 'Fm': {'name': 'Fermium', 'mass': 257.0}, 'Md': {'name': 'Mendelevium', 'mass': 258.0}, 'No': {'name': 'Nobelium', 'mass': 259.0}, 'Lr': {'name': 'Lawrencium', 'mass': 262.0}, 'Rf': {'name': 'Rutherfordium', 'mass': 267.0}, 'Db': {'name': 'Dubnium', 'mass': 268.0}, 'Sg': {'name': 'Seaborgium', 'mass': 271.0}, 'Bh': {'name': 'Bohrium', 'mass': 274.0}, 'Hs': {'name': 'Hassium', 'mass': 269.0}, 'Mt': {'name': 'Meitnerium', 'mass': 276.0}, 'Ds': {'name': 'Darmstadtium', 'mass': 281.0}, 'Rg': {'name': 'Roentgenium', 'mass': 281.0}, 'Cn': {'name': 'Copernicium', 'mass': 285.0}, 'Nh': {'name': 'Nihonium', 'mass': 286.0}, 'Fl': {'name': 'Flerovium', 'mass': 289.0}, 'Mc': {'name': 'Moscovium', 'mass': 288.0}, 'Lv': {'name': 'Livermorium', 'mass': 293.0}, 'Ts': {'name': 'Tennessine', 'mass': 294.0}, 'Og': {'name': 'Oganesson', 'mass': 294.0}}


#functions and classes
def get_mass(element):
    """Return mass of an element.

    Parameters
    ----------
    element : string
        Element from periodic table.

    Returns
    -------
    float
        Atomic mass of an element.

    """
    return table[element]['mass']

def formula2components(formula):
    """Convert a glass/any composition formula to component dictionary.

    Parameters
    ----------
    formula : string
        Glass/any composition for e.g. 50Na2O-50SiO2.

    Returns
    -------
    dictionary
        Dictionary where keys are components of glass/any composition and values are their ratio.

    """
    dict1 = {}
    parts = formula.split('-')
    if len(parts)==1:
        dict1[parts[0]] = 1.0
    else:
        for i in parts:
            k = ''
            p = ''
            for ind, j in enumerate(i):
                try:
                    float(j)
                    p += j
                except:
                    if j == '.':
                        p += j
                    else:
                        k = i[ind:]
                        break
            dict1[k] = float(p)
    if sum(dict1.values())==100:
        for k,v in dict1.items():
            dict1[k] = dict1[k]/100
        return dict1
    elif sum(dict1.values())==1.0:
        return dict1
    else:
        try:
            raise Exception("Invalid Formula: {}.".format(formula))
        except Exception as e:
            print(e)
            raise

def get_molar_mass(formula):
    """Return molar mass of a glass/any composition.

    Parameters
    ----------
    formula : string
        Glass/any composition for e.g. 50Na2O-50SiO2.

    Returns
    -------
    float
        Molar mass of a glass/any composition.

    """
    dict1 = cleanit(formula)
    s = 0
    for key, value in dict1.items():
        s += value * molar_mass(key)
    return s

def molecule2atoms(formula):
    """Convert a molecule formula to dictionary of atoms/number pair.

    Parameters
    ----------
    formula : string
        Molecule formula for e.g SiO2 or CH4.

    Returns
    -------
    dict
        Dictionary of atoms/number pair.

    """
    formula = formula.strip()
    dict1 = {}
    k = ''
    p = '0'
    for ind, i in enumerate(formula):
        if i == i.upper():
            try:
                float(i)
                p += i
                if ind == (len(formula) - 1):
                    dict1[k] = float(p)
            except:
                try:
                    dict1[k] = float(p)
                    p = ''
                    k = ''
                    k += i
                except:
                    dict1[k] = 1.0
                    p = ''
                    k = ''
                    k += i
        else:
            k += i

        if ind == (len(formula) - 1):
            try:
                float(formula[-1])
            except:
                dict1[k] = float(1.0)
    dict1.pop('')
    return dict1

def molar_mass(formula):
    """Return molar mass of a molecule.

    Parameters
    ----------
    formula : string
        Molecule formula for e.g SiO2 or CH4.

    Returns
    -------
    float
        Molar mass.

    """
    dict1 = molecule2atoms(formula)
    s = 0
    for i in dict1:
        s += dict1[i] * get_mass(i)
    return s

def cleanit(formula):
    """Utility function for internal use.
    Convert string/dict/DataFrame to dict

    Parameters
    ----------
    formula : string/dict/DataFrame


    Returns
    -------
    dict


    """
    if type(formula)==dict:
        dict1 = formula
    elif type(formula)==pandas.core.frame.DataFrame:
        dict1 = formula.to_dict('list')
    else:
        dict1 = formula2components(formula)
    for key in dict1.keys():
        dict1[key] = np.array(dict1[key])
    return dict1

def convert2sametype(dict_, formula):
    """Utility function for internal use.
    Convert string/dict/DataFrame to dict

    Parameters
    ----------
    dict_ : dict

    formula : string/dict/DataFrame

    Returns
    -------
    type(formula)


    """
    return convert2type(dict_, type(formula))


def convert2type(dict_, type_):
    """Utility function for internal use.
    Convert dict to string/dict/DataFrame

    Parameters
    ----------
    dict_ : dict


    Returns
    -------
    type_


    """
    if type_==str:
        str_ = "{" + ":.{}f".format(fprecision) + "}" + "{" + "}"
        out = "-".join([str_.format(v,k) for k,v in dict_.items()])
    elif type_==pandas.core.frame.DataFrame:
        out = pd.DataFrame(dict_)
    else:
        out = dict_
    return out

def weight2mol(formula, out_type=None):
    """Convert weight% to mol%.

    Parameters
    ----------
    formula : string/dict/DataFrame
        Glass/Any composition.

    Returns
    -------
    dict/DataFrame/string
        Glass/Any composition.

    """
    dict1 = cleanit(formula)
    dict2 = dict1.copy()
    dict3 = dict1.copy()
    for key, value in dict1.items():
        dict2[key] = value / molar_mass(key)
    for key, value in dict2.items():
        dict3[key] = dict2[key] * 100 / sum(dict2.values())
    if type(out_type)==type(None):
        out = convert2sametype(dict3, formula)
    else:
        out = convert2type(dict3, out_type)
    return out


def mol2weight(formula, out_type=None):
    """Convert mol% to weight%.

    Parameters
    ----------
    formula : string/dict/DataFrame
        Glass/Any composition.

    Returns
    -------
    dict/DataFrame/string
        Glass/Any composition.

    """
    dict1 = cleanit(formula)
    dict2 = dict1.copy()
    dict3 = dict1.copy()
    for key, value in dict1.items():
        dict2[key] = dict1[key] * molar_mass(key)
    for key, value in dict2.items():
        dict3[key] = dict2[key] * 100 / sum(dict2.values())
    if type(out_type)==type(None):
        out = convert2sametype(dict3, formula)
    else:
        out = convert2type(dict3, out_type)
    return out
