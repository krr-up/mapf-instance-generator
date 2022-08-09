% size:
#const s=2.

% percent of possible vertices used:
#const c=50.

% get number of vertices from size and coverage
numVertices(N)       :- N=(s*s*c)/100.

% vertices:
{vertex((1..s,1..s))}=N :- numVertices(N).

% edges from vertices that are adjacent:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.

% ensure connection:
1{init(V) : vertex(V)}1.
linked(V) :- init(V).
linked(V) :- edge(V,U), linked(U).
:- vertex(V), not linked(V).

#show   edge/2.
#show vertex/1.
