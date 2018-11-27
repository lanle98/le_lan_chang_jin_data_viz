import csv
import numpy as np
import matplotlib.pyplot as plt

city = [] # strip out the first row of text
medal = [] # push the medal data here
year = [] # push the year data here

# open the csv file and parse it
with open("USA.csv") as csvfile:
    reader = csv.reader(csvfile)
    line_count = 0

    for row in reader:
        if line_count is 0: # strip the headers out 
             print('pushing text row to city array')
             city.append(row)
             line_count += 1
        else:
            # collect the medal info
            medalData = row[7]
            medal.append(row)
            line_count += 1

            # print('collect the rest of the data')


print('processed', line_count, "rows of data")
print('first line:', medal [0])
print('last line:', medal [-1])

np_medal = np.array(medal)


gold_medal = np_medal = 1

print(gold_medal)

silver_medal = np_medal = 2

print(silver_medal)

bronze_medal = np_medal = 3

print(bronze_medal)

# now we can plot stuffs!
labels = ['Canada(109)', 'USA(167)', 'Norway(127)']
sizes = [109, 167, 127]
colors = ['#cd7f32', '#cd7f32', '#cd7f32']
explode = (0.1, 0.1, 0.1)




plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=200)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Comparing Bronze Medals between CAD, USA, and NOR")
plt.xlabel("USA has won the most bronze medals from winter olympics!!!!")
plt.show()
