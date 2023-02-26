
def solution(id_list, report, k):
    answer = [0]*len(id_list)
    
    report_list = []
    for i in range(len(id_list)):
        report_list.append(set())
    for i in range(len(report)):
        reporter, crimimal = report[i].split()
        report_list[id_list.index(crimimal)].add(reporter)
    
    for i in range(len(report_list)):
        if(len(report_list[i])>=k):
            for j in report_list[i]:
                check = id_list.index(j)
                answer[check] +=1
    
    return answer