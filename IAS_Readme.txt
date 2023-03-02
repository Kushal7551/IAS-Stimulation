Finding the value of n+n^2+n^3+m+m^2+m^3(n+n(square)+n(cube)+m+m(square)+m(cube))
Please give the input:
1 
-5
6
LOAD MQ,M(X) 0 MUL M(X) 0
LOAD MQ STOR M(X) 2
MUL M(X) 0 LOAD MQ
STOR M(X) 3
LOAD MQ,M(X) 1 MUL M(X) 1
LOAD MQ STOR M(X) 4
MUL M(X) 1 LOAD MQ
STOR M(X) 5
ADD M(X) 4 ADD M(X) 3
ADD M(X) 2 ADD M(X) 1
ADD M(X) 0
STOR M(X) 6
HALT



In the first problem we have to find n^2,n^3,m^2,m^3
Load the value present in the memory location 0 to MQ Then multiply than value with the value in the memory location 
0 to get n^2 in MQ.Then we are storing than value in AC and then store it in the memory location 2
Multiply the value in MQ with the value in the memory location 0 and then store it in the AC.Then store the value 
i.e n^3 in the memory location 3.
Load the value present in the memory location 1 to MQ Then multiply than value with the value in the memory location 
1 to get m^2 in MQ.Then we are storing than value in AC and then store it in the memory location 4
Multiply the value in MQ with the value in the memory location 1 and then store it in the AC.Then store the value 
i.e m^3 in the memory location 5.
Adding the value present in memory location 4 i.e m^2.Adding the value present in memory location 3 i.e n^3
Adding the value present in memory location 2 i.e n^2.Adding the value present in memory location 1 i.e m.
Then finally Adding the value present in the memory location 0 i.e n.
Storing this value in the memory location 6


MEMORY MAP
0------------------>n
1------------------>m
2------------------>n^2
3------------------>n^3
4------------------>m^2
5------------------>m^3
6------------------>n+n^2+n^3+m+m^2+m^3





Finding the nth term of the series T(N)=T(n-1)+T(n-2)+T(n-3)
Please give this input:
2
0
1
2
5
LOAD M(X) 0 ADD M(X) 1
ADD M(X) 2 STOR M(X) 6
LOAD M(X) 1 STOR M(X) 0
LOAD M(X) 2 STOR M(X) 1
LOAD M(X) 6 STOR M(X) 2
JUMP M(X,0:19) 0
HALT



In this problem the numbers 0,1,2 are stored in the memory location 0,1,2 and 5 is the n th term of the series
To find the 5 term we use this number as the JumpCounter.
First we load the value present in 0 th location to AC then add the value present in 1 st location and then add the value in the 
second location and store it in 6 th location


MEMORY MAP
0------------------>0
1------------------>1
2------------------>2
6------------------>3

We are loading the value present in the memory location 1 to AC and then storing it in memory location 0
We are loading the value present in the memory location 2 to AC and then storing it in memory location 1
We are loading the value present in the memory location 6 to AC and then storing it in memory location 2


MEMORY MAP
0------------------>1
1------------------>2
2------------------>3
6------------------>3

First we load the value present in 0 th location to AC then add the value present in 1 st location and then add the value in the 
second location and store it in 6 th location

MEMORY MAP
0------------------>1
1------------------>2
2------------------>3
6------------------>6

We are loading the value present in the memory location 1 to AC and then storing it in memory location 0
We are loading the value present in the memory location 2 to AC and then storing it in memory location 1
We are loading the value present in the memory location 6 to AC and then storing it in memory location 2

MEMORY MAP
0------------------>2
1------------------>3
2------------------>6
6------------------>6

First we load the value present in 0 th location to AC then add the value present in 1 st location and then add the value in the 
second location and store it in 6 th location

MEMORY MAP
0------------------>2
1------------------>3
2------------------>6
6------------------>11

We are loading the value present in the memory location 1 to AC and then storing it in memory location 0
We are loading the value present in the memory location 2 to AC and then storing it in memory location 1
We are loading the value present in the memory location 6 to AC and then storing it in memory location 2

MEMORY MAP
0------------------>3
1------------------>6
2------------------>11
6------------------>11

First we load the value present in 0 th location to AC then add the value present in 1 st location and then add the value in the 
second location and store it in 6 th location


MEMORY MAP
0------------------>3
1------------------>6
2------------------>11
6------------------>20

We are loading the value present in the memory location 1 to AC and then storing it in memory location 0
We are loading the value present in the memory location 2 to AC and then storing it in memory location 1
We are loading the value present in the memory location 6 to AC and then storing it in memory location 2

MEMORY MAP
0------------------>6
1------------------>11
2------------------>20
6------------------>20


First we load the value present in 0 th location to AC then add the value present in 1 st location and then add the value in the 
second location and store it in 6 th location


MEMORY MAP
0------------------>6
1------------------>11
2------------------>20
6------------------>37

We are loading the value present in the memory location 1 to AC and then storing it in memory location 0
We are loading the value present in the memory location 2 to AC and then storing it in memory location 1
We are loading the value present in the memory location 6 to AC and then storing it in memory location 2

MEMORY MAP
0------------------>11
1------------------>20
2------------------>37
6------------------>37

First we load the value present in 0 th location to AC then add the value present in 1 st location and then add the value in the 
second location and store it in 6 th location

MEMORY MAP
0------------------>11
1------------------>20
2------------------>37
6------------------>68

So the 5 th term of the series is 68...
