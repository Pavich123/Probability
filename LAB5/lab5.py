import numpy as np
import math
from sympy import *
import sympy as sp

def Factorial(n):
    if (n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n*Factorial(n-1)

def SpecialCombinationsForAll(k,n):
    resultMuptipleUp=1
    lastUp=max([n-k,k])+1
    while(lastUp<=n):
        resultMuptipleUp*=lastUp
        lastUp+=1
    return resultMuptipleUp/Factorial(min([n-k,k]))

def Bernulli(n,k,p):
    q = 1 - p
    P = SpecialCombinationsForAll(k,n)*pow(p,k)*pow(q,n-k)
    return P

def BernulliAppendLoop(n, p,start):
    probsOfEvent=[]
    while(start<=n):
        probsOfEvent.append(Bernulli(n,start,p))
        start+=1
    return probsOfEvent.index(max(probsOfEvent)), max(probsOfEvent)

def Laplas(n,k,p):
    if(n*k*p<10):
        return Bernoulli(n,k,p)
    q=1-p
    x=np.abs((k-n*p)/np.sqrt(n*p*q))
    function = math.exp(-x*x/2) / math.sqrt(2*math.pi)
    result=(1/np.sqrt(n*p*q))*function
    return result


def LaplasInt(n, i, j, p):
    q = 1 - p
    x1 = (i - n * p) / math.sqrt(n * p * q)
    x2 = (j - n * p) / math.sqrt(n * p * q)
    x = Symbol('x')

    if x1 > 5:
        function1 = 0.5
    else:
        function1 = integrate(sp.exp(-x * x / 2), (x, 0, x1)) / math.sqrt(2 * math.pi)

    if x2 > 5:
        function2 = 0.5
    else:
        function2 = integrate(sp.exp(-x * x / 2), (x, 0, x2)) / math.sqrt(2 * math.pi)

    result = function2 - function1
    return result

def WriteFile():
    result_file=open("result.txt", "w")
    result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n')
    result_file.write("LAB5"+ '\n')
    #TASK1
    result_file.write("=============================================="+ '\n'+"TASK1"+'\n')
    result_file.write('P(k) = '+ str(round(Bernulli(5,3,0.2),4))+'\n')
    
    #TASK2
    result_file.write("=============================================="+ '\n'+"TASK2"+'\n')
    result_file.write("A) P(k) = "+ str(round(Bernulli(5,4,0.8),4))+'\n')
    result_file.write("B) P(k) = "+ str(round(Bernulli(5,4,0.8)+Bernulli(5,5,0.8),4))+'\n')

    #TASK3
    result_file.write("=============================================="+ '\n'+"TASK3"+'\n')
    result_file.write('P(k) = '+ str(round(Bernulli(400,80,0.2),4))+'\n')

    #TASK4
    result_file.write("=============================================="+ '\n'+"TASK4"+'\n')
    result_file.write('P(k) = '+ str(round(Laplas(100000,5,0.0001),4))+'\n')

    #TASK5
    result_file.write("=============================================="+ '\n'+"TASK5"+'\n')
    result_file.write("P(k) = " + str(round(LaplasInt(600, 228, 252, 0.4), 4))+'\n')

    #TASK6
    result_file.write("=============================================="+ '\n'+"TASK6"+'\n')
    number, prob = BernulliAppendLoop(100,0.4,0)
    result_file.write('The most probability number = '+ str(number)+'\n')
    result_file.write('Probability of this number = '+ str(round(prob,4))+'\n')

    #TASK7
    result_file.write("=============================================="+ '\n'+"TASK7"+'\n')
    result_file.write("P(k) = " + str(round(LaplasInt(4000, 0, 170, 0.04), 4))+'\n')


    #TASK8
    result_file.write("=============================================="+ '\n'+"TASK8"+'\n')
    result_file.write('P(k) = '+ str(round(Laplas(10000,5000,0.5),4))+'\n')

    #TASK9
    result_file.write("=============================================="+ '\n'+"TASK9"+'\n')
    result_file.write('P(k) = '+ str(round(Bernulli(1000,5,0.002),4))+'\n')

    #TASK10
    result_file.write("=============================================="+ '\n'+"TASK10"+'\n')
    number, prob = BernulliAppendLoop(150,0.97,1)
    result_file.write('The most probability number = '+ str(number)+'\n')

WriteFile()
