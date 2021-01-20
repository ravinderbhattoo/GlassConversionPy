import unittest
import GlassConversionPy as gc

class TestConvertMethods(unittest.TestCase):

    def test_mol2weight(self):
        self.assertEqual(gc.mol2weight("100O-0H"), '100.00O-0.00H')
        self.assertEqual(gc.mol2weight("50C-50H"), '{:.2f}C-{:.2f}H'.format(gc.molar_mass('C')/(gc.molar_mass('H')+gc.molar_mass('C'))*100, gc.molar_mass('H')/(gc.molar_mass('H')+gc.molar_mass('C'))*100))

    def test_weight2mol(self):
        self.assertEqual(gc.weight2mol("100O-0H"), '100.00O-0.00H')
        self.assertEqual(gc.weight2mol("50C-50H"), '{:.2f}C-{:.2f}H'.format(gc.molar_mass('H')/(gc.molar_mass('H')+gc.molar_mass('C'))*100, gc.molar_mass('C')/(gc.molar_mass('H')+gc.molar_mass('C'))*100))

if __name__ == '__main__':
    unittest.main()
