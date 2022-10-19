import  matplotlib.pyplot as plt
import math




def WriteFile(path):
    result_file=open("result.txt", "w")
    result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n')
    result_file.write("LAB2"+ '\n')
    #TASK1
    result_file.write("========================================"+"\n"+"TASK1"+"\n")
    main_massive = GetMainMassive(path)
    result_file.write("Lower Quartile = "+str(GetQuartile(main_massive, 1))+"\n")
    result_file.write("Upper Quartile = "+str(GetQuartile(main_massive, 3))+"\n")
    result_file.write("Percantile 90 = "+str(GetPercantile(main_massive, 90))+"\n")
    
    #TASK2
    result_file.write("========================================"+"\n"+"TASK2"+"\n")
    mean, standard = GetDeviations(main_massive)
    result_file.write("Mean deviation = "+ str(mean)+"\n"+ "Standard deviation = "+ str(standard)+"\n")
    
    #TASK3
    result_file.write("========================================"+"\n"+"TASK3"+"\n")
    A, B = GetCoefficients(main_massive)
    result_file.write("y = "+str(A)+"x + "+str(B)+"\n")
    
    result_file.write("y average = "+str(round(A*GetAverageOfMassive(main_massive)+B))+"\n")

    result_file.write("y variance = "+str(GetYVariance(A, mean))+"\n")    

    result_file.write("y standard deviation = "+str(GetYStandardDeviation(A, standard))+"\n")
    
    #TASK4
    result_file.write("========================================"+"\n"+"TASK4"+"\n")
    result_file.write("Stem and Leaf diagram: "+"\n")
    
    new_massive, second_massive = GetStemAndLeaf(main_massive)
    
    for i in range(len(new_massive)):
        result_file.write(str(new_massive[i])+" | "),
        for j in range(len(second_massive[i])):
            result_file.write(str(second_massive[i][j])+" "),
        result_file.write("\n")
    result_file.write("Key: "+str(new_massive[0])+ "|"+ str(second_massive[0][0])+ " means "+str(new_massive[0])+str(second_massive[0][0])+"\n")

    #TASK5
    result_file.write("========================================"+"\n"+"TASK5"+"\n")
    result_file.write("Boxplot")
    DrawBoxPlot(main_massive)
    
    result_file.close() 

def GetMainMassive(path):
    with open(path) as file:
        main_massive=[]
        
        for item in file:
            item = int(item)
            main_massive.append(item)
        main_massive.pop(0)
        main_massive.sort()
    return main_massive

def GetQuartile(massive,quartile):
    q = math.floor((len(massive)+1)*quartile/4)
    Q=massive[q-1]+(massive[q]-massive[q-1])*quartile/4
    return Q

def GetPercantile(massive, percantile):
    p=math.floor(percantile/100*(len(massive)+1))
    P= massive[p-1]
    return P

def GetAverageOfMassive(massive):
    sum_massive = 0
    for i in range(len(massive)):
        sum_massive += massive[i]
    average = sum_massive/len(massive)
    return average

def GetSumDeviation(massive):
    sum_deviation = 0
    for i in range(len(massive)):
        sum_deviation+=pow(massive[i],2)
    return sum_deviation
    

def GetDeviations(massive):
    
    sum_quad = GetSumDeviation(massive)
    average = GetAverageOfMassive(massive)
    
    mean = round(sum_quad/len(massive)-pow(average,2),2)
    standard = round(pow(mean,0.5),2)

    return mean, standard

def GetCoefficients(massive):
    new_average = 95
    new_max = 100
    A = round((new_max-new_average)/(new_max-GetAverageOfMassive(massive)),1)
    B = new_max-new_max*A
    return A,B

def GetYVariance(A, mean):
    y_variance = round(pow(A,2)*mean,2)
    return y_variance


def GetYStandardDeviation(A, standard):
    y_standard = round(abs(A)*standard,2)
    return y_standard
    

def GetStemAndLeaf(massive):
    new_massive = []
    second_massive = []
    help_massive = []
    for i in range(len(massive)):
        if (math.floor(massive[i]/10) not in new_massive):
            if (i>0):
                second_massive.append(help_massive)
            help_massive = []
            new_massive.append(math.floor(massive[i]/10))
            help_massive.append(massive[i]%10)
        else:
            help_massive.append(massive[i]%10)
    second_massive.append(help_massive)  
            
    return new_massive, second_massive

def DrawBoxPlot(massive):
    plt.boxplot(massive)
    plt.show()
    

path = input()
WriteFile(path)






    
    
    


















    
