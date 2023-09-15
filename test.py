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

    def test_adjun(self):
        a =  [[-9+14j, 16-49j], [1-1j, 7+27j]]
        respm = [[-9-14j, 1+1j], [16+49j, 7-27j]]
        respc = lm.adjunta(a)
        self.assertEqual(respc, respm)	

    def test_productomatri(self):
        a = [[8+1j, 4-5j], [7-4j, 6], [10+11j, -12j]]
        b = [[7-5j, 14+1j, -6j], [8+4j, 3, 8-4j]]
        respm = [[(113-57j), (123+7j), (18-104j)], [(77-39j), (120-49j), (24-66j)], [(173-69j), (129+128j), (18-156j)]]
        respc = lm.productoma(a, b)
        self.assertEqual(respc, respm)

    def test_accion(self):
        a = [[7-4j, 1+45j, 79-83j], [17+13j, 12j, 5-9j], [-14+1j, 1+19j, -7+8j]]
        v = [19+5j, 20-3j, -1+4j] 
        respm = [(561+1255j), (325+601j), (-219+290j)]
        respc = lm.accionmsobrev(a,v)
        self.assertEqual(respc, respm)

    def test_prointerno(self):
        u = [3+4j,8,0,1+3j]
        v = [1j,5-4j,7j,3j]
        respm = 53-26j
        respc = lm.producintern(u,v)
        self.assertEqual(respc,respm)

    def test_normal(self):
        u = [1+2j,3-4j,-3j]
        respm = 6.24
        respc = lm.normalvec(u)
        self.assertEqual(respc,respm)

    def test_distanciavec(self):
        u = [4,2-1j,2+4j]
        v = [4-3j,-1j,2j]
        respm = 4.58
        respc = lm.distvec(u,v)
        self.assertEqual(respc, respm)

    def test_vect_val(self):
        a =[[-1,-1j],[1j,1]]
        respm = "valores: [-1.41+0.j  1.41+0.j]. vectores: [ 0.92387953+0.j         -0.        -0.38268343j]"
        respc = lm.val_vec_propios(a)
        self.assertEqual(respc, respm)

    def test_unitaria(self):
        u = [[2/3,(-2+1j)/3],[(2+1j)/3,2/3]]
        respm = "Es unitaria"
        respc = lm.unitario(u)
        self.assertEqual(respc, respm)
    
    def test_hermitiana(self):
        u = [[3,2-1j,-5j],[2+1j,0,9-5j],[5j,9+5j,6]]
        respm =  "Es hermitiana"
        respc = lm.hermitiana(u)
        self.assertEqual(respc, respm)
    
    def test_tensor(self):
        u = [[2,3],[1,4]]
        v = [[5,3,2],[1,0,2],[-2,5,6]]
        respm = [[10, 6, 4, 15, 9, 6], [2, 0, 4, 3, 0, 6], [-4, 10, 12, -6, 15, 18], [5, 3, 2, 20, 12, 8], [1, 0, 2, 4, 0, 8], [-2, 5, 6, -8, 20, 24]]
        respc = lm.producto_tensor(u,v)
        self.assertEqual(respc, respm)
		
if __name__ == "__main__":
	unittest.main()
