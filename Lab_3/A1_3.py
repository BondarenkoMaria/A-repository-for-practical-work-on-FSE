x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if x1==0 or y1==0 or x2==0 or y2==0:
	print ("Ошибка")
else:
	if (x1>0 and y1>0): 
		region1=("1 четверть")
	elif (x1<0 and y1>0):
		region1=("2 четверть")
	elif (x1<0 and y1<0):
		region1=("3 четверть")
	else:
		region1=("4 четверть")
	if (x2>0 and y2>0):
		region2=("1 четверть")
	elif (x2<0 and y2>0):
		region2=("2 четверть")
	elif (x2<0 and y2<0):
		region2=("3 четверть")
	else:
		region2=("4 четверть")
if region1==region2:
    print(f"Yes, { region1 }")
else:
        print("No")