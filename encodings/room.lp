% Dimensions:
%% Total:
#const s=2.

%% Room:
#const w=3.


% Vertices:
%% Rooms:
vertex((X,Y)) :- X=1..s, Y=1..s, X\(w+1)!=0, Y\(w+1)!=0.

%% Doors:
{vertex((X,Y+F*(w+1))) : Y=1..w}1 :- X=1..s, X\(w+1)=0, F=0..(s/(w+1)).
{vertex((X+F*(w+1),Y)) : X=1..w}1 :- Y=1..s, Y\(w+1)=0, F=0..(s/(w+1)).


% Edges:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.


% All vertices must be reachable:
1{init(V) : vertex(V)}1.
linked(V) :- init(V).
linked(V) :- edge(V,U), linked(U).
:- vertex(V), not linked(V).


#show   edge/2.
#show vertex/1.
