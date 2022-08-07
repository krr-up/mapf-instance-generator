#const s = 4.

dim(1..s).
dim2((D*2)-1) :- dim(D).

1 { parent(X,Y, 0,-2);
    parent(X,Y, 2, 0);
    parent(X,Y,-2, 0);
    parent(X,Y, 0, 2) } 1 :-
dim2(X), dim2(Y).

edge((X     ,Y     ),(X+DX/2,Y+DY/2)) :- parent(X,Y,DX,DY).
edge((X+DX/2,Y+DY/2),(X+DX  ,Y+DY  )) :- parent(X,Y,DX,DY).

edge(V,U) :- edge(U,V).

:- edge(_,(X,_)), X<1.
:- edge(_,(_,Y)), Y<1.

vertex(V) :- edge(V,_).

connected(A,B) :- edge(A,B).
connected(A,B) :- edge(B,A).
connected(A,C) :- edge(B,C), connected(A,B).
:- not connected((X,Y),(X2,Y2)), dim2(X), dim2(Y), dim2(X2), dim2(Y2).

#show.
#show edge/2.
#show vertex/1.
