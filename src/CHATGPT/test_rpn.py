import unittest
from rpn import rpn_eval, RPNError
import math


"""
rpn.py

Evaluador de expresiones en Notación Polaca Inversa (RPN).

Características:
Soporta enteros y floats,
Operaciones básicas (+, -, *, /),
Funciones matemáticas (sqrt, log, ln, etc.),
Funciones trigonométricas en grados,
Manejo de pila (dup, swap, drop, clear),
Memorias (00 a 09) con STO/RCL,
Manejo de errores mediante RPNError,
"""

class TestRPN(unittest.TestCase):

    # -----------------------
    # Operaciones básicas
    # -----------------------
    def test_suma(self):
        self.assertEqual(rpn_eval("3 4 +"), 7)

    def test_expresion_compleja(self):
        self.assertEqual(rpn_eval("5 1 2 + 4 * + 3 -"), 14)

    def test_multiplicacion_y_suma(self):
        self.assertEqual(rpn_eval("2 3 4 * +"), 14)

    def test_float(self):
        self.assertAlmostEqual(rpn_eval("2.5 2 *"), 5.0)

    def test_negativos(self):
        self.assertEqual(rpn_eval("-4 2 *"), -8)

    # -----------------------
    # Funciones matemáticas
    # -----------------------
    def test_sqrt(self):
        self.assertEqual(rpn_eval("9 sqrt"), 3)

    def test_log(self):
        self.assertAlmostEqual(rpn_eval("100 log"), 2)

    def test_ln(self):
        self.assertAlmostEqual(rpn_eval("2.718281828 ln"), 1, places=2)

    def test_ex(self):
        self.assertAlmostEqual(rpn_eval("1 ex"), math.e)

    def test_10x(self):
        self.assertEqual(rpn_eval("2 10x"), 100)

    def test_yx(self):
        self.assertEqual(rpn_eval("2 3 yx"), 8)

    def test_inverso(self):
        self.assertEqual(rpn_eval("2 1/x"), 0.5)

    # -----------------------
    # Trigonometría
    # -----------------------
    def test_sin(self):
        self.assertAlmostEqual(rpn_eval("90 sin"), 1, places=5)

    def test_cos(self):
        self.assertAlmostEqual(rpn_eval("0 cos"), 1, places=5)

    def test_tg(self):
        self.assertAlmostEqual(rpn_eval("45 tg"), 1, places=5)

    # -----------------------
    # Pila
    # -----------------------
    def test_dup(self):
        self.assertEqual(rpn_eval("3 dup +"), 6)

    def test_swap(self):
        self.assertEqual(rpn_eval("3 4 swap -"), 1)

    def test_drop(self):
        self.assertEqual(rpn_eval("3 4 drop"), 3)

    def test_clear_error(self):
        with self.assertRaises(RPNError):
            rpn_eval("3 4 clear")

    # -----------------------
    # Constantes
    # -----------------------
    def test_pi(self):
        self.assertAlmostEqual(rpn_eval("p"), math.pi)

    def test_e(self):
        self.assertAlmostEqual(rpn_eval("e"), math.e)

    def test_phi(self):
        self.assertAlmostEqual(rpn_eval("j"), (1 + math.sqrt(5)) / 2)

    # -----------------------
    # Memorias
    # -----------------------
    def test_memoria_sto_rcl(self):
        self.assertEqual(rpn_eval("5 STO00 RCL00"), 5)

    def test_memoria_invalida(self):
        with self.assertRaises(RPNError):
            rpn_eval("5 STO10")

    # -----------------------
    # Errores (Try/Except)
    # -----------------------
    def test_token_invalido(self):
        try:
            rpn_eval("3 4 foo")
            self.fail("Debería lanzar RPNError")
        except RPNError:
            pass

    def test_pila_insuficiente(self):
        try:
            rpn_eval("+")
            self.fail("Debería lanzar RPNError")
        except RPNError:
            pass

    def test_division_por_cero(self):
        try:
            rpn_eval("3 0 /")
            self.fail("Debería lanzar RPNError")
        except RPNError:
            pass

    def test_resultado_multiple(self):
        try:
            rpn_eval("3 4")
            self.fail("Debería lanzar RPNError")
        except RPNError:
            pass

    def test_sqrt_negativo(self):
        try:
            rpn_eval("-1 sqrt")
            self.fail("Debería lanzar RPNError")
        except RPNError:
            pass


if __name__ == "__main__":
    unittest.main()