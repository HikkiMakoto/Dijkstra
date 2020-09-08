# Dijkstra

Input

s [the number of tests <= 10]<br>
n [the number of cities <= 10000]<br>
NAME [city name]<br>
p [the number of neighbors of city NAME]<br>
nr cost [nr - index of a city connected to NAME (the index of the first city is 1)]<br>
           [cost - the transportation cost]<br>
r [the number of paths to find <= 100]<br>
NAME1 NAME2 [NAME1 - source, NAME2 - destination]<br>
[empty line separating the tests]<br>

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

