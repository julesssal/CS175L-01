#Julia Salerno
#CS-175L
#AverageFromInput.py

def main():

    numbers_file = open('numbers.txt', 'r')
    counter = 1
    total = 0.0
    avg = 0.0
    num_lines = 0

    for line in numbers_file:

       amt = float(line)
       total = total + amt
       print(f"I read in {counter} number(s) Current number is: {amt:.2f} Total is: {total:.2f}")
       counter = counter + 1
       num_lines = num_lines+1

    numbers_file.close()
    
    avg = total / num_lines
    print(f"Average: {avg:.2f}")
    
if __name__ == '__main__':
    main()

    
