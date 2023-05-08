#const x=5.
#const y=5.

dimx(1..x).
dimy(1..y).
dimx2((D*2)-1) :- dimx(D).
dimy2((D*2)-1) :- dimy(D).

1 { parent(X,Y, 0,-2);
    parent(X,Y, 2, 0);
    parent(X,Y,-2, 0);
    parent(X,Y, 0, 2) } 1 :-
dimx2(X), dimy2(Y).

edge((X     ,Y     ),(X+DX/2,Y+DY/2)) :- parent(X,Y,DX,DY).
edge((X+DX/2,Y+DY/2),(X+DX  ,Y+DY  )) :- parent(X,Y,DX,DY).

edge(V,U) :- edge(U,V).

:- edge(_,(X,_)), X<1.
:- edge(_,(_,Y)), Y<1.

vertex(V) :- edge(V,_).

1{init(X,Y) : dimx2(X), dimy2(Y)}1.
linked(X,Y) :- init(X,Y).
linked(X,Y) :- parent(X,Y,DX,DY), linked(X+DX,Y+DY).
:- dimx2(X), dimy2(Y), not linked(X,Y).

#show.
#show edge/2.
#show vertex/1.
