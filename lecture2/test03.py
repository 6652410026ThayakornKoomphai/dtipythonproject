#แสดงข้อมูลหลายๆ ประเภทใน Print เดียว
#1. ใช้ ,
print("SAU",555,123,456,True,10+50)

#2. ใช้ + มีข้อแม้ ข้อมูลที่ไม่ใช่ string ต้องแปลงเป็น string และไม่มี space เหมือนกับ ,
print("SAU "+str(555)+str(123.456)+str(True)+str(10+50))

#3. Method ชื่อ Format
print("SAU {} {} {} {}".format(555, 123.456, True, 10+50))
print("SAU {0} {1} {2} {3}".format(555, 123.456, True, 10+50))

#4. ใช้ F-String ***
print(f"SAU {555} {123.456} {True} {10+50}")

#-------------
#
print("aaa"); print(111); print(True)