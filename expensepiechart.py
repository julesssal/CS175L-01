#Julia Salerno
#CS-175L
#expensepiechart.py
import matplotlib.pyplot as plt

def main():

    try:
        
        file = open('expenses.txt', 'r')
        
    except IOError:
        print("An error occured trying to read that file")
        sys.exit()
    
    category = []
    values = []

    for line in file:
        l = line.strip('\n')
        cols = l.split('\t')
        category.append(cols[0])
        values.append(int(cols[1]))

    mycolors = ['#00FFFF', '#7FFF00', '#CD5C5C', '#4B0082', '#FFA07A', '#DA70D6']
    
    
    plt.title('Monthly Expenses')
    
    plt.pie(values, labels =category, colors = mycolors)

    plt.show()

if __name__ == '__main__':
    main()
        
        
