# 10.Tuition Increase

current = 8000
for x in range(1,6):
    current += (current*.03)
    print(format(current,'.2f'), "projected semester tuition after",x,"year(s).")
