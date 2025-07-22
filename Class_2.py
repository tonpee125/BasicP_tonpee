km = input ("ระยะทาง : ")
print(km)
if (int(km) < 5):
    print("ไม่ส่ง")
elif (int(km) <= 5):
    print("ค่าขนส่ง 10")
elif (int(km) <= 51):
    print("ค่าขนส่ง 15")
elif (int(km) <= 101):
    print("ค่าขนส่ง 25")
elif (int(km) <= 301):
    print("ค่าขนส่ง 35")
elif (int(km) <= 500):
    print("ค่าขนส่ง 45")
else:
    print
