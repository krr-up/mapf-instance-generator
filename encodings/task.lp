% number of agents:
#const a=1.

vertex(N) :- edge(N,_).
vertex(N) :- edge(_,N).

agent(1..a).

1{start(R,S) :  vertex(S)}1 :- agent(R).
1{ goal(R,G) :  vertex(G)}1 :- agent(R).


:- 2{start(R,S) : agent(R)}, vertex(S).
:- 2{ goal(R,G) : agent(R)}, vertex(G).

:- start(R,V), goal(R,V).

#show vertex/1.
#show agent/1.
#show edge/2.
#show start/2.
#show goal/2.
