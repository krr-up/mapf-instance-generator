% number of agents:
#const a=1.

agent(1..a).

1{start(A,S) :  vertex(S)}1 :- agent(A).
1{ goal(A,G) :  vertex(G)}1 :- agent(A).

:- 2{start(A,S) : agent(A)}, vertex(S).
:- 2{ goal(A,G) : agent(A)}, vertex(G).

:- start(A,V), goal(A,V).

#show vertex/1.
#show agent/1.
#show edge/2.
#show start/2.
#show goal/2.
