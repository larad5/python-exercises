# 6.Celsius to Fahrenheit

print("In Celsius\tIn Fahrenheit\n--------------------------------")
# repetition structure to calculate each degree conversion
for cels in range(0,21):
    fahr = (9/5)*cels + 32
    print(cels,"\t\t",fahr,sep='')
