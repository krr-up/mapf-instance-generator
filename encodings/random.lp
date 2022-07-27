% dimensions:
%#const x=2.
%#const y=2.
#const w=2.
% number of vertices:
#const v=2.
%% use percentage instead

% nodes:
v{vertex((1..w,1..w))}v.

% edges from nodes that are adjacent:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.

% ensure connection:
1{init(X,Y) : vertex((X,Y))}1.
linked(X,Y) :- init(X,Y).
linked(X,Y) :- edge((X,Y),(DX,DY)), linked(DX,DY).
:- vertex((X,Y)), not linked(X,Y).

#show edge/2.
