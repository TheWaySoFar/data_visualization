import csv
from datetime import datetime
from matplotlib import pyplot as plt

print(((1+0.042)**16)*16)

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    print(head_row)
    dates,highs,lows = [],[],[]
    for row in reader:
        try:
            current_date = datetime.strptime(row[0],"%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date,"missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


fig = plt.figure(dpi=128,figsize=(10,6))
plt.title("Daily high and low temperatures - 2014")
plt.plot(dates,highs,c='red')
plt.plot(dates,lows,c='green')
plt.legend(['High','Low'])
plt.fill_between(dates,lows,highs,facecolor='blue',alpha=0.1)
plt.xlabel('Date',fontsize=16)
plt.ylabel('Temperature(F)',fontsize=16)
plt.tick_params(axis='both',which='major',labelsize=16)



fig.autofmt_xdate()
plt.show()