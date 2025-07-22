km = input ("ระยะทาง : ")
print(km)
if (int(km) < 5):
    print("ไม่ส่ง")
elif (int(km) <= 5):
    print("10")
elif (int(km) <= 51):
    print("15")
elif (int(km) <= 101):
    print("25")
elif (int(km) <= 301):
    print("35")
elif (int(km) <= 500):
    print("45")
else:
    print
