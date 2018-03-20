from die import Die
import pygal

die1 = Die()
die2 = Die()
results = []
for roll_num in range(1000):
    results.append(die1.roll() + die2.roll())
frequencies = []
for value in range(2,13):
    frequencies.append(results.count(value))
print(frequencies)

hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times"
hist.x_labels = [str(x) for x in range(2,13)]
hist.x_title = "Result"
hist.y_title = "Frequency of result"
hist.add('D6',frequencies)
hist.render_to_file('die_visual.svg')