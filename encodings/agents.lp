% number of agents:
#const a=1.
#const d=1.

agent(1..a).

1{start(A,S) :  vertex(S)}1 :- agent(A).
1{ goal(A,G) :  vertex(G)}1 :- agent(A).

:- 2{start(A,S) : agent(A)}, vertex(S).
:- 2{ goal(A,G) : agent(A)}, vertex(G).

:- start(A,V), goal(A,V).

dist(D) :- D=|X-X2|+|Y-Y2|, start(A,(X,Y)), goal(A,(X2,Y2)), agent(A).
:- dist(D), D<d.

#show vertex/1.
#show agent/1.
#show edge/2.
#show start/2.
#show goal/2.
