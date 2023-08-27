import unittest
import Libcplxmat as lm
class TestLibVecSpaces(unittest.TestCase):
    def test_sumvec(self):
        v = [3j, 4+5j, 6-9j,5]
        w = [6j, 10-10j, 4+9j, 70j]
        sumam = [9j, 14-5j, 10, 5+70j]
        sumac = lm.adicc_vec(v,w)
        self.assertEqual(sumac, sumam)
	
    def test_inversovec(self):
        v = [41j, -24+15j, 46-19j,-5-8j]
        invervecm = [-41j, 24-15j, -46+19j, 5+8j]
        invervecc = lm.inv_adit(v)
        self.assertEqual(invervecc, invervecm)
    
    def test_multescalar(self):
        v = [31j, 0, 13-9j, 1+8j]
        k = 2j
        respm = [-62, 0, 18+26j, -16+2j]
        respc = lm.esc_vec(k, v)
        self.assertEqual(respc, respm)
    def test_summatrix(self):
        a = [[3+2j, 9-10j, 0], [9j, 6+11j, -8+1j], [49, -8j, 1-2j]]
        b = [[4+1j, 10+9j, 4-7j], [8, 20j, +8-1j], [-49+16j, 8j, -3+4j]]
        respm = [[7+3j, 19-1j, 4-7j], [8+9j, 6+31j, 0], [16j, 0, -2+2j]]
        respc = lm.suma_mat(a, b)
        self.assertEqual(respc, respm)
        
    def test_inversoma(self):
        a = [[-13+8j, 39+14j, 9j],[-15-4j, 7+7j, -1+5j]]
        respm = [[13-8j, -39-14j, -9j], [15+4j, -7-7j, 1-5j]]
        respc = lm.invAd_mat(a)
        self.assertEqual(respc, respm)
    def test_traspu(self):
        a =  [[6+2j, 4-1j], [-2j, 6-14j], [7-8j, 3j]]
        respm = [[6+2j, -2j, 7-8j], [4-1j, 6-14j, 3j]]
        respc = lm.transpuesta(a)
        self.assertEqual(respc, respm)
    
    def test_conjugate(self):
        a =  [[8+10j, 6-14j, 15+9j], [-7j, 1+12j, 3-3j], [4, 15-19j, 81j]]
        respm = [[8-10j, 6+14j, 15-9j], [7j, 1-12j, 3+3j], [4, 15+19j, -81j]]
        respc = lm.conjugada(a)
        self.assertEqual(respc, respm)


if __name__ == "__main__":
	unittest.main()
