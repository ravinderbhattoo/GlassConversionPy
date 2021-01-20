#imports
import mendeleev as table
import numpy as np
import pandas
import pandas as pd

fprecision = 2

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
    return table.element(element).mass

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
