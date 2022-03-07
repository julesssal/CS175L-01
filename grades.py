#Julia Salerno
#CS-175L
#2/28/2022

def main():

    s1, s2, s3, s4, s5, average = calc_average()
    g1, g2, g3, g4, g5, avgerage_grade= determine_grade(s1, s2, s3, s4, s5, average)
    print("Score\tNumeric Grade\tLetter Grade")
    print("-----------------------------------")
    outputResults(s1, s2, s3, s4, s5, g1, g2, g3, g4, g5, average, avgerage_grade)
    ToF = repeat1()
    if ToF:
        main()

def determine_grade(score1, score2, score3, score4, score5, avg):
    if score1 >= 90 and score1 <= 100:
        grade1 = "A"
    elif score1<=89 and score1>=80:
        grade1 = "B"
    elif score1<=79 and score1>=70:
        grade1 = "C"
    elif score1<=69 and score1>=60:
        grade1 = "D"
    elif score1<60:
        grade1 = "F"
    else:
        print("score entered is invalid")

    if score2 >= 90 and score2 <= 100:
        grade2 = "A"
    elif score2<=89 and score2>=80:
        grade2 = "B"
    elif score2<=79 and score2>=70:
        grade2 = "C"
    elif score2<=69 and score2>=60:
        grade2 = "D"
    elif score2<60:
        grade2 = "F"
    else:
        print("score entered is invalid")


    if score3 >= 90 and score3 <= 100:
        grade3 = "A"
    elif score3<=89 and score3>=80:
        grade3 = "B"
    elif score3<=79 and score3>=70:
        grade3 = "C"
    elif score3<=69 and score3>=60:
        grade3 = "D"
    elif score3<60:
        grade3 = "F"
    else:
        print("score entered is invalid")

    if score4 >= 90 and score4 <= 100:
        grade4 = "A"
    elif score4<=89 and score4>=80:
        grade4 = "B"
    elif score4<=79 and score4>=70:
        grade4 = "C"
    elif score4<=69 and score4>=60:
        grade4 = "D"
    elif score4<60:
        grade4 = "F"
    else:
        print("score entered is invalid")

    if score5 >= 90 and score5 <= 100:
        grade5 = "A"
    elif score5<=89 and score5>=80:
        grade5 = "B"
    elif score5<=79 and score5>=70:
        grade5 = "C"
    elif score5<=69 and score5>=60:
        grade5 = "D"
    elif score5<60:
        grade5 = "F"
    else:
        print("score entered is invalid")

    if avg >= 90 and avg <= 100:
        avg_grade = "A"
    elif avg<=89 and avg>=80:
        avg_grade = "B"
    elif avg<=79 and avg>=70:
        avg_grade = "C"
    elif avg<=69 and avg>=60:
        avg_grade = "D"
    elif avg<60:
        avg_grade = "F"
    else:
        print("score entered is invalid")
    return grade1, grade2, grade3, grade4, grade5, avg_grade

def outputResults(score1, score2, score3, score4, score5, grade1, grade2, grade3, grade4, grade5, avg, avg_grade):
    print(f"score1: \t{score1}\t{grade1}")
    print(f"score2: \t{score2}\t{grade2}")
    print(f"score3: \t{score3}\t{grade3}")
    print(f"score4: \t{score4}\t{grade4}")
    print(f"score5: \t{score5}\t{grade5}")
    print(f"Average Score: \t{avg}\t{avg_grade}")
    
def calc_average():
    total = 0
    avg = 0.0
    num_scores = 5
    s1= float(input("Enter score 1: "))
    total = total + s1
    s2= float(input("Enter score 2: "))
    total = total + s2
    s3= float(input("Enter score 3: "))
    total = total + s3
    s4= float(input("Enter score 4: "))
    total = total + s4
    s5= float(input("Enter score 5: "))
    total = total + s5
    avg = total / num_scores
    return s1, s2, s3, s4, s5, avg

def repeat1():
    keep_going = input("Enter 'yes' if you would like to do another calculation: ")
    if keep_going.lower() == "yes":
        return True
    else:
        return False
    
main()

