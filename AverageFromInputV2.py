#Julia Salerno
#CS-175L
#AverageFromInputV2.py
import sys

def main():
    
    amount, numlines, tot = getValues()
    getAverage(tot, numlines)
    
def getValues():
    total = 0
    num_lines = 0
    counter = 1
    
    try:
        
        numbers_file = open('numbers.txt', 'r')
    except IOError:
        
        print("An error occured trying to read the file.")
        sys.exit()
        
    for line in numbers_file:
        
        try:
            amt = float(line)
            total= total + amt
            print(f"I read in {counter} number(s) Current number is: {amt:.2f} Total is: {total:.2f}")
            counter = counter + 1
            num_lines = num_lines +1
            
        except ValueError:
            
            print("Non-numeric data found in the file. Skipping.")

    numbers_file.close()
    
    return amt, num_lines, total
       
def getAverage(values, nums):

    avg = values/nums
    print(f"Average: {avg:.2f}")

        
if __name__ == '__main__':
    main()
