from const import c_ocean as c
from const import ocean_V as vo
from const import plotnost as ro
def armagedon(ma, v):
    """Последствия превосходного проишествия
    """
    m = vo * ro
    t = ((ma*v**2)/2)/(2*c*m)
    if t >=50:
        print("Все мертвы, замечательно")
    elif t >=30 and t <=50:
        print("Погибло лишь 90%, этого мало")
    elif t <= 30:
        print("Всего лишь больно? Жаль, но щас исправим")
        print(speed(ma))

def speed(ma, m=vo*ro):
        speed=((2*c*50*m)/ma)**0.5
        return speed
armagedon(ma=300, v=157003000080)
