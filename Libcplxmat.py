import numpy as np
def adicc_vec(v1,v2):
    res = []
    if len(v1)== len (v2):
        for j in range (len(v1)):
            res.append(v1[j]+v2[j])
        return res
    else :
        return "Vectores con tamaños diferentes"

def inv_adit(v1):
    res = []
    for j in range (len(v1)):
        res.append(v1[j]*-1)
    return res

def esc_vec(e,v1):
    res = []
    for j in range (len(v1)):
        res.append(v1[j]*e)
    return res

def suma_mat(m1,m2):
    matR= []
    if len(m1) == len (m2):
        for j in range (len(m1)):
            fila = []
            for k in range (len(m1[0])):
                fila.append(m1[j][k]+m2[j][k])
            matR.append(fila)
        return matR
    else :
        return "matrices con tamaños diferentes"

def invAd_mat(m1):
    matR = [[0 for y in range(len(m1[0]))] for x in range(len(m1))]
    for j in range (len(m1)):
        for k in range(len(m1[0])):
            matR[j][k] = -1*(m1[j][k])
    return matR

def esc_mat(e,m1):
    matR = [[0 for y in range(len(m1[0]))] for x in range(len(m1))]
    for j in range (len(m1)):
        for k in range(len(m1[0])):
            matR[j][k] = e*(m1[j][k])
    return matR

def transpuesta(m1):
    matR = [[0 for y in range(len(m1))] for x in range(len(m1[0]))]
    for j in range (len(m1)):
        for k in range(len(m1[0])):
            matR[k][j] = m1[j][k]
    return matR

def conjugada(m1):
    fil = len(m1)
    col = len(m1[0])
    for i in range(fil):
        for j in range(col):
            m1[i][j] = m1[i][j].conjugate()
    return m1

