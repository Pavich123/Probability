import  matplotlib.pyplot as plt
import numpy as np
import math


def GetMainMassive(path):
    with open(path) as file:
        x = int(file.readline())
        sum_mas = []
        time_mas = []
        
        first_massive = file.read().replace("\t", " ").replace("\n", " ").replace(",", ".").split(" ")
        if (first_massive[len(first_massive)-1]==''):
            first_massive.pop(len(first_massive)-1)
        index = 0
        for i in first_massive:
            if (index%2==0):
                i = float(i)
                sum_mas.append(i)
            else:
                i=int(i)
                time_mas.append(i)
            index+=1
    return sum_mas, time_mas

def WriteFile(sum_mas, time_mas):
    result_file=open("result.txt", "w")
    result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n')
    result_file.write("LAB3"+ '\n')
    #TASK1
    result_file.write("=============================================="+ '\n'+"TASK1"+'\n')
    result_file.write("Scatter plot"+ '\n')
    DrawScatterPlot(sum_mas,time_mas)
    
    #TASK2
    result_file.write("=============================================="+ '\n'+"TASK2"+'\n')

    money_average, cov, time_average = GetCovariation(sum_mas, time_mas)
    
    result_file.write("Center of gravity: ("+ str(money_average)+"," + str(time_average)+")" +'\n')
    result_file.write("Covariation: "+ str(cov)+'\n')
    #TASK3
    result_file.write("=============================================="+ '\n'+"TASK3"+'\n')

    b1, b0, var_money = GetRegressionEquation(sum_mas,time_mas)
    result_file.write("Regression equation:"+ '\n')
    result_file.write("y = "+ str(b1)+"*x"+str(b0)+'\n')

    #TASK4
    result_file.write("=============================================="+ '\n'+"TASK4"+'\n')
    CORRELATION = GetCorrelation(sum_mas, time_mas, var_money, time_average, money_average)
    result_file.write("Correlation coefficient: "+ str(CORRELATION)+'\n')
    result_file.close() 

def DrawScatterPlot(sum_mas, time_mas):
    plt.scatter(sum_mas, time_mas)

    z = np.polyfit (sum_mas, time_mas, 1 )
    p = np.poly1d (z)

    plt.plot (sum_mas, p(sum_mas))
    plt.show()    

def SumOfElementsInMassive(massive):
    sum_massive = 0
    for i in range(len(massive)):
        sum_massive+=massive[i]
    return sum_massive
        
def GetAverageOfMassive(massive):
    average = round(SumOfElementsInMassive(massive)/len(massive),2)
    return average

def GetCumulativeSum(mas1, mas2):
    cum_sum=0
    for i in range(len(mas1)):
        cum_sum+=mas1[i]*mas2[i]
    return cum_sum

def GetCovariation(sum_mas, time_mas):
    money_average = GetAverageOfMassive(sum_mas)
    time_average = GetAverageOfMassive(time_mas)

    cum_sum = GetCumulativeSum(sum_mas, time_mas)
    
    cov = round(1/(len(sum_mas))*cum_sum - money_average * time_average,2)
    return money_average, cov, time_average


def GetSumDeviation(mas):
    var_sum = 0
    for i in range(len(mas)):
        var_sum+=pow(mas[i],2)
    return var_sum

def GetDeviation(var_sum, mas, average):
    var = round(var_sum/len(mas)-pow(average,2),2)
    return var

def GetRegressionEquation(sum_mas, time_mas):
    money_average, cov, time_average = GetCovariation(sum_mas, time_mas)
    
    var_sum1 = GetSumDeviation(sum_mas)
    var_money = GetDeviation(var_sum1, sum_mas, money_average)
    
    b1 = round(cov/var_money,2)
    b0 = round(time_average - b1*money_average,2)

    
    return b1, b0, var_money


def ControlSum(mas1, mas2, average1, average2, var1, var2):
    CONTROL_SUM = 0
    for i in range(len(mas1)):
        CONTROL_SUM+=((mas1[i] - average1)/pow(var1,0.5))*((mas2[i] - average2)/pow(var2,0.5))
    return CONTROL_SUM

def GetCorrelation(sum_mas, time_mas, var_money, time_average, money_average):
    var_sum2 = GetSumDeviation(time_mas)
    var_time = GetDeviation(var_sum2, time_mas, time_average)
    
    n = len(sum_mas)

    
    CORRELATION = round(1/(n-1)*ControlSum(sum_mas, time_mas, money_average, time_average, var_money, var_time),3)
    return CORRELATION
    
path = input()
sum_mas, time_mas = GetMainMassive(path)
WriteFile(sum_mas, time_mas)



    
    
    


















    
