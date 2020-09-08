# Dijkstra

Input

s [the number of tests <= 10]
n [the number of cities <= 10000]
NAME [city name]
p [the number of neighbors of city NAME]
nr cost [nr - index of a city connected to NAME (the index of the first city is 1)]
           [cost - the transportation cost]
r [the number of paths to find <= 100]
NAME1 NAME2 [NAME1 - source, NAME2 - destination]
[empty line separating the tests]

Example<br>

Input:<br>
1<br>
4<br>
gdansk<br>
2<br>
2 1<br>
3 3<br>
bydgoszcz<br>
3<br>
1 1<br>
3 1<br>
4 4<br>
torun<br>
3<br>
1 3<br>
2 1<br>
4 1<br>
warszawa<br>
2<br>
2 4<br>
3 1<br>
2<br>
gdansk warszawa<br>
3 - output<br>
bydgoszcz warszawa<br>
2 - output<br>

