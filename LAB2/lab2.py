import  matplotlib.pyplot as plt
import math

result_file=open("result.txt", "w")

result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n')
result_file.write("LAB2"+ '\n')

path = input()
with open(path) as file:

    a=[]
    
    for item in file:
        item = int(item)
        a.append(item)
    a.pop(0)
    
def task1(a):
    result_file.write("========================================"+"\n"+"TASK1"+"\n")
    a.sort()

    
    q1 = math.floor((len(a)+1)/4)
    Q1=a[q1-1]+(a[q1]-a[q1-1])/4

    result_file.write("Q1 = ")
    result_file.write(str(Q1)+"\n")
    

    q3 = math.floor((len(a)+1)*3/4)
    Q3=a[q3-1]+(a[q3]-a[q3-1])*3/4
    
    result_file.write("Q3 = ")
    result_file.write(str(Q3)+"\n")

    p90=math.floor(90/100*(len(a)+1))
    P90 = a[p90-1]
    result_file.write("P90 = "+str(P90)+"\n")


def task2(a):
    result_file.write("========================================"+"\n"+"TASK2"+"\n")

    sum_a = 0
    for i in range(len(a)):
        sum_a += a[i]
    
    average = sum_a/len(a)

    sum_quad = 0
    for i in range(len(a)):
        sum_quad+=pow(a[i],2)

        
    mean = round(sum_quad/len(a)-pow(average,2),2)
    standard = round(pow(mean,0.5),2)

    result_file.write("Mean deviation = "+ str(mean)+"\n"+ "Standard deviation = "+ str(standard)+"\n")
    return average, standard


def task3(a):
    

    average, standard = task2(a)
    result_file.write("========================================"+"\n"+"TASK3"+"\n")
    new_average = 95
    new_max = 100
    A = round((new_max-new_average)/(new_max-average),1)
    B = new_max-new_max*A

    result_file.write("y = "+str(A)+"x + "+str(B)+"\n")
    result_file.write("y average = "+str(round(A*average+B))+"\n")
    y_standard = round(abs(A)*standard,2)
    result_file.write("y standard deviation = "+str(y_standard)+"\n")


def task4(a):
    

    
    result_file.write("========================================"+"\n"+"TASK4"+"\n")
    result_file.write("Stem and Leaf diagram: "+"\n")
    a.sort()

    new_massive = []
    second_massive = []
    help_massive = []
    for i in range(len(a)):
        if (math.floor(a[i]/10) not in new_massive):
            if (i>0):
                second_massive.append(help_massive)
            help_massive = []
            new_massive.append(math.floor(a[i]/10))
            help_massive.append(a[i]%10)
        else:
            help_massive.append(a[i]%10)
    second_massive.append(help_massive)  
            

    for i in range(len(new_massive)):
        result_file.write(str(new_massive[i])+" | "),
        for j in range(len(second_massive[i])):
              result_file.write(str(second_massive[i][j])+" "),
        result_file.write("\n")
    result_file.write("Key: "+str(new_massive[0])+ "|"+ str(second_massive[0][0])+ " means "+str(new_massive[0])+str(second_massive[0][0])+"\n")



def task5(a):
    result_file.write("========================================"+"\n"+"TASK5"+"\n")
    result_file.write("Boxplot")
    a.sort()

    if (len(a)/2==0):
        median = (a[len(a)/2]+a[len(a)/2-1])/2
    else:
        median = a[round((len(a)/2))-1]
    
    plt.boxplot(a)
    plt.show()
    


task1(a)
task3(a)
task4(a)
task5(a)

result_file.close() 


    
    
    


















    
