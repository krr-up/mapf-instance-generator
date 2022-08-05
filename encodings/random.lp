% size:
#const s=2.
% number of vertices:
#const v=2.

% nodes:
v{vertex((1..s,1..s))}v.

% edges from nodes that are adjacent:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.

% ensure connection:
1{init(X,Y) : vertex((X,Y))}1.
linked(X,Y) :- init(X,Y).
linked(X,Y) :- edge((X,Y),(DX,DY)), linked(DX,DY).
:- vertex((X,Y)), not linked(X,Y).

#show edge/2.
#show vertex/1.
