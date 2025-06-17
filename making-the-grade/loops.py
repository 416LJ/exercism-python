import itertools
def round_scores(student_scores):
    """Round all provided student scores.
    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """ 
    return [round(x,0) for x in student_scores]

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.
    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    count = 0
    for x in student_scores:
        if x <= 40:
            count += 1
    return count

def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.
    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores = []
    best = threshold
    
    for x in student_scores:
        if x >= best:
            best_scores.append(x)
    return(best_scores)

def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.
    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:
            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    shift = round((highest-41)/4)
    print(shift)
    return [41,41+shift*1,41+shift*2, 41+shift*3]        

def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.
    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    the_list = []
    for i, (name,score) in enumerate(zip(student_names,student_scores),start = 1):
        the_list.append(f"{i}. {name}: {score}")
    return the_list

def perfect_score(student_info):
    the_record = []
    found_student = False
    
    for list in student_info:
        if list[1] == 100:
            while found_student == False:
                the_record.append(list[0])
                the_record.append(list[1])
                found_student = True
        else:
            continue
        
    return the_record
