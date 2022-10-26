% Dimensions:
%% Total:
#const s=2.

%% Shelves:
#const w=3.

% Vertices:
vertex((1..s,1..s)).

% Edges:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.

% Shelves:
noShelf((1..s,(s/4)*3-1..s)).
noShelf((s,1..s)).
noShelf((X,Y)) :- vertex((X,Y)), X\(w+1)=1.
noShelf((X,Y)) :- vertex((X,Y)), Y\  3  =1.
  shelf(  V  ) :- not noShelf(V), vertex(V).
  
% Start area:
start_area((1..s,(s/4)*3..s)).

% agents:

% number of agents:
#const a=1.

agent(1..a).

1{start(A,S) :  vertex(S)}1 :- agent(A).
1{ goal(A,G) :  vertex(G)}1 :- agent(A).

:- 2{start(A,S) : agent(A)}, vertex(S).
:- 2{ goal(A,G) : agent(A)}, vertex(G).

:- start(A,V), goal(A,V).

:- start(A,S), shelf(S).
:-  goal(A,G), not shelf(G).
:- start(A,S), not start_area(S).

#show vertex/1.
#show agent/1.
#show edge/2.
#show start/2.
#show goal/2.
