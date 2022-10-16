import  matplotlib.pyplot as plt

result_file=open("result.txt", "w")

result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n')
result_file.write("LAB1"+ '\n')

path = input()
with open(path) as file:
    result_file.write("======================================================================"+ '\n')
    result_file.write("TASK 1"+ '\n')
    a=[]
    
    for item in file:
        item = int(item)
        a.append(item)
    a1 = a.pop(0)
    
    sum=0
    for i in range(a1):
        sum+=a[i]

    result_file.write("Index of movie  Frequency   Relative frequency    Cumulative frequency"+ '\n')
    cum_sum=0
    for i in range(a1):
        cum_sum+=a[i]
        result_file.write(str(i+1))
        result_file.write("                  ")
        result_file.write(str(a[i]))
        result_file.write("            ")
        result_file.write(str(round(a[i]/sum*100,2)))
        result_file.write("%")
        result_file.write("                  ")
        result_file.write(str(cum_sum)+ '\n')
    result_file.write("Movie with the most frequency: ")
    result_file.write(str(a.index(max(a))+1)+ '\n')
    


    result_file.write("======================================================================"+ '\n')
    result_file.write("TASK 2"+ '\n')
    new_arr = []
    k=1
    for i in range(len(a)):
        for j in range(a[i]):
            new_arr.append(k)
        k+=1
    if (len(new_arr)/2==0):
        median = (new_arr[len(new_arr)/2]+new_arr[len(new_arr)/2-1])/2
    else:
        median = new_arr[round((len(new_arr)/2))-1]

    result_file.write("Median = ")
    result_file.write(str(median)+ '\n')
    result_file.write("Moda = ")
    result_file.write(str(a.index(max(a))+1)+ '\n')



    
    result_file.write("======================================================================"+ '\n')
    result_file.write("TASK 3"+ '\n')
    
    sum3=0
    for i in range(len(a)):
        sum3+=(i+1)*a[i]
    average = sum3/cum_sum

    sum3_1 = 0
    for i in range(len(a)):
        sum3_1+=a[i]*pow(i+1,2)

        
    Dispersia = sum3_1/cum_sum-pow(average,2)
    Standard_Deviation=pow(Dispersia,0.5)
    result_file.write("Dispersia = ")
    result_file.write(str(round(Dispersia,2))+ '\n')
    result_file.write("Standard_Deviation = ")
    result_file.write(str(round(Standard_Deviation,2))+ '\n')


    result_file.write("======================================================================"+ '\n')
    result_file.write("TASK 4"+ '\n')
    result_file.write("Histogram"+ '\n')
    movie_mas = []
    for i in range(len(a)+1):
        movie_mas.append(i+1)
    plt.hist(new_arr, bins = movie_mas) 
    plt.title("Frequency histogram")
    plt.show()


result_file.close() 


    
    
    


















    
