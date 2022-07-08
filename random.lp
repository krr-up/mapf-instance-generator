% dimensions:
#const x=2.
#const y=2.
% number of vertices:
#const v=2.

% nodes:
v{node((1..x,1..y))}v.

% edges from nodes that are adjacent:
edge((X,Y),(X+DX,Y+DY)) :- node((X,Y)), node((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.

% ensure connection:
1{start(X,Y) : node((X,Y))}1.
linked(X,Y) :- start(X,Y).
linked(X,Y) :- edge((X,Y),(DX,DY)), linked(DX,DY).
:- node((X,Y)), not linked(X,Y).

#show edge/2.
