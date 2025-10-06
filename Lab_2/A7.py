x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
def get_color(x,y):
    return (x+y)%2==0
def get_color_name(white):
    return 'White' if white else 'Black'
color1 = get_color(x1,y1)
color2 = get_color(x2,y2)
if color1==color2:
    print("YES")
    color_name = get_color_name(color1)
    print(color_name)
else:
    print("NO") 