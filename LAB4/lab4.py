def Factorial(n):
    if (n==0):
        return 1
    elif(n==1):
        return 1
    else:
        return n*Factorial(n-1)
    
def Combinations(n,k):
    return Factorial(n)/(Factorial(k)*Factorial(n-k))

def Bayes(probability_massive_1, probability_massive_2, index):
    control_mult = probability_massive_1[index]*probability_massive_2[index]
    control_sum = SumOfProbabilities(probability_massive_1, probability_massive_2)
    return control_mult/control_sum

def SumOfProbabilities(probability_massive_1, probability_massive_2):
    control_sum = 0
    for i in range(len(probability_massive_1)):
        control_sum += probability_massive_1[i]*probability_massive_2[i]
    return control_sum

def GetCertainProbability(massive, indexes):
    sum_of_All = 0
    sum_of_Indexes = 0
    for i in range(len(massive)):
        sum_of_All+=massive[i]
    for i in range(len(indexes)):
        sum_of_Indexes+=massive[indexes[i]]
    return sum_of_Indexes/sum_of_All

def GetLastProbability(massive):
    SUM=0
    for i in range(len(massive)):
        SUM+=massive[i]
    return 1 - SUM

def GetAntiProbablity(all_quantity, certain_quantity, needed_quantity):
    return 1 - Combinations(all_quantity-certain_quantity, needed_quantity)/Combinations(all_quantity, needed_quantity)

def GetProbabilityForTrains(colies, trains, number_of_needed_colies):
    RESULT_SUM = 1
    for i in range(number_of_needed_colies):
        RESULT_SUM*=(trains-i)/(colies-i)
    return RESULT_SUM

def GetDataForStudents(massive_people, massive_tasks, indexes, number_of_queastion, right_questions):
    RESULTS_MASSIVE = []
    sum_people = 0
    for i in range(len(massive_people)):
        sum_people+=massive_people[i]
    for i in range(len(massive_people)):
        massive_people[i]/=sum_people
    for i in range(len(massive_people)):
        RESULTS_MASSIVE.append(Combinations(massive_tasks[i],right_questions)/Combinations(number_of_queastion, right_questions))
    FINAL_MASSIVE = []
    for i in range(len(indexes)):
        FINAL_MASSIVE.append(Bayes(massive_people, RESULTS_MASSIVE, indexes[i]))
    return FINAL_MASSIVE
def WriteFile():
    result_file=open("result.txt", "w")
    result_file.write("Pavlyuchenko Artem, IPZ-21/1"+ '\n')
    result_file.write("LAB4"+ '\n')
    #TASK1
    result_file.write("=============================================="+ '\n'+"TASK1"+'\n')
    result_file.write('P(A) = '+ str(GetCertainProbability([40,26,22,12],[2,3]))+'\n')
    
    #TASK2
    result_file.write("=============================================="+ '\n'+"TASK2"+'\n')
    result_file.write("P(A) = "+ str(round(GetAntiProbablity(10,8,2),2))+'\n')

    #TASK3
    result_file.write("=============================================="+ '\n'+"TASK3"+'\n')
    result_file.write('P(A) = '+ str(round(GetAntiProbablity(10,2,3),2))+'\n')

    #TASK4
    result_file.write("=============================================="+ '\n'+"TASK4"+'\n')
    result_file.write('P5 = '+ str(round(GetLastProbability([0.15,0.25,0.2,0.1]),2))+'\n')

    #TASK5
    result_file.write("=============================================="+ '\n'+"TASK5"+'\n')
    result_file.write('P(A) = '+ str(round(GetProbabilityForTrains(120,80,2),3))+'\n')

    #TASK6
    result_file.write("=============================================="+ '\n'+"TASK6"+'\n')
    result_file.write('P(A) = '+ str(round(SumOfProbabilities([0.9],[0.8]),2))+'\n')

    #TASK7
    result_file.write("=============================================="+ '\n'+"TASK7"+'\n')
    result_file.write("P(A) for excellent student: "+str(round(GetDataForStudents([3,4,2,1],[20,16,10,5],[0,3],20,3)[0],3))+'\n')
    result_file.write("P(A) for bad student : "+str(round(GetDataForStudents([3,4,2,1],[20,16,10,5],[0,3],20,3)[1],3))+'\n')

    #TASK8
    result_file.write("=============================================="+ '\n'+"TASK8"+'\n')
    result_file.write('P(A) = '+ str(round(SumOfProbabilities([0.4,0.3,0.3],[0.9,0.95,0.95]),2))+'\n')

    #TASK9
    result_file.write("=============================================="+ '\n'+"TASK9"+'\n')
    result_file.write('P(A) = '+ str(round(Bayes([0.4,0.3,0.3],[0.8,0.7,0.85],1),3))+'\n')

    #TASK10
    result_file.write("=============================================="+ '\n'+"TASK10"+'\n')
    result_file.write('P(A) = '+ str(round(Bayes([0.3,0.7],[0.9,0.8],0),3))+'\n')

WriteFile()
