orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]
find = []

def find_farthest_orbit(orbits):
    orbits_new = [(0,0)]
    max = 0
    pi = 3.14
    for i in orbits:
        if i[0] != i[1]:
            if max < pi * i[0] * i[1]:
                max = pi * i[0] * i[1]
                orbits_new.pop()
                orbits_new.append(i)
    return orbits_new[0]
print(*find_farthest_orbit(orbits))