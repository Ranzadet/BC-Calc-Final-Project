import math
import itertools
x = open("FrequencyVals.txt", "r")
frequencies = []
amps = []
negAmps = []

line = x.readline()
while line:
    line = line.strip().split("\t")
    num1 = float(line[0])
    num2 = float(line[1])
    freq = num1*2
    frequencies.append(freq)
    negAmps.append(num2)
    amps.append(abs(num2))
    line = x.readline()

print("Minimum dB: ", min(negAmps))
lower = min(negAmps)
upper = max(negAmps)

for i in range(len(negAmps)):
    negAmps[i] += abs(lower)

print(negAmps)


big = max(negAmps)
small = min(negAmps)

amps2 = []

for i in range(len(negAmps)):
    scaledNum = negAmps[i] * math.pow(10, ((negAmps[i]-small)/10))
    amps2.append(scaledNum)

big = max(amps2)
small = min(amps2)
amps3 = []

print("max: ", big)
print("min, ", small)

for i in range(len(amps2)):
    val = (amps2[i]-small) / (big-small)
    amps3.append(val)
    print("%.3f" % val)


print("----printing equations------")

file = open("SoundEquations.txt", "w")
# iterEq = ("y = {a:.3f}sin({b:.3f}pit)\n".format(a=amps3[i], b=frequencies[i]) for i in range(len(amps3)))
#Here, we only need to multiply by pi because the frequencies were already multiplied by 2 in the first while loop
iterEq = ("{a:.4f}sin({b:.4f}t) + ".format(a=amps3[i], b=frequencies[i]*math.pi) for i in range(len(amps3)) if abs(round(amps3[i], 3)) > 0.000)
endEq = ("0" for i in [0])
fullEq = (i for i in itertools.chain(iterEq, endEq))
file.writelines(fullEq)

print("f(t) = ", end="")
for i in range(len(amps3)):
    equation = "{a:.3f}sin({b:.3f}πt)".format(a=amps3[i], b=frequencies[i])
    print(equation, end=" + ")
print("0")
