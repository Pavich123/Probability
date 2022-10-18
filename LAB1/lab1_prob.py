import  matplotlib.pyplot as plt
import numpy as np

result_file=open("result.txt", "w")

result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n'+"LAB1"+ '\n')

path = input()
with open(path) as file:
    a=[]
    
    for item in file:
        item = int(item)
        a.append(item)
    a1 = a.pop(0)

    a.sort()

def task1(a):
    result_file.write("======================================================================"+ '\n'+"TASK 1"+ '\n')
    unique_massive = []
    frequency_massive=[]
    quantity =0
    
    for i in range(len(a)):
        if a[i] not in unique_massive:
            frequency_massive.append(quantity)
            quantity=1
            unique_massive.append(a[i])
        else:
            quantity+=1
    frequency_massive.append(quantity)
    frequency_massive.pop(0)


    result_file.write("Movie  Frequency   Cumulative frequency"+ '\n')
    cum_sum=0
    for i in range(len(unique_massive)):
        cum_sum+=frequency_massive[i]
        result_file.write(str(unique_massive[i])+"         "+str(frequency_massive[i])+"               "+str(cum_sum)+ '\n')

    moda_massive = []
    maximum = max(frequency_massive)
    founded_maximum = maximum
    help_massive = []

    
    for i in range(len(frequency_massive)):
        help_massive.append(frequency_massive[i])
        

    k=0
    while(founded_maximum==maximum):
        if k>0:
            moda_massive.append(unique_massive[help_massive.index(founded_maximum)+k])
        else:
            moda_massive.append(unique_massive[help_massive.index(founded_maximum)])
        help_massive.pop(help_massive.index(founded_maximum))
        founded_maximum = max(help_massive)
        k+=1
        
        

    result_file.write("Movie(s) with the biggest number of reviews: ")
    for i in range(len(moda_massive)):
        result_file.write(str(moda_massive[i])+" ")
    
    
    return unique_massive, frequency_massive, moda_massive
    

def task2(a):
    unique_massive, frequency_massive, moda_massive = task1(a)
    result_file.write("\n"+"======================================================================"+ '\n'+"TASK 2"+ '\n')

    if (len(a)/2==0):
        median = (a[len(a)/2]+a[len(a)/2-1])/2
    else:
        median = a[round((len(a)/2))-1]

    result_file.write("Median = "+str(median)+ '\n')
    result_file.write("Moda(modes) = ")
    for i in range(len(moda_massive)):
        result_file.write(str(moda_massive[i])+" ")
    
    return unique_massive, frequency_massive


def task3(a):
    unique_massive, frequency_massive = task2(a)
    result_file.write("\n"+"======================================================================"+ '\n'+"TASK 3"+ '\n')

    sum_a=0
    for i in range(len(unique_massive)):
        sum_a+=frequency_massive[i]*unique_massive[i]
    average = sum_a/len(a)

    sum_for_var = 0
    for i in range(len(unique_massive)):
        sum_for_var+=frequency_massive[i]*pow(unique_massive[i],2)

        
    Var = sum_for_var/len(a)-pow(average,2)
    Standard_Deviation=pow(Var,0.5)
    result_file.write("Var = "+str(round(Var,2))+ '\n')
    result_file.write("Standard_Deviation = "+str(round(Standard_Deviation,2))+ '\n')
    return unique_massive

def task4(a, a1):
    unique_massive = task3(a)
    result_file.write("======================================================================"+ '\n'+"TASK 4"+ '\n'+"Histogram"+ '\n')
    
    unique_massive.append(max(unique_massive)+a1)
    plt.hist(a, unique_massive)
    plt.title("Frequency histogram")
    plt.show()


task4(a, a1)


result_file.close() 


    
    
    


















    
