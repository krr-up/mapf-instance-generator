% Dimensions:
#const x=2.
#const y=2.

% Shelf width:
#const w=5.

% Vertices:
vertex((X,1..y)) :- X=1..x, X\(w+1)=1.
vertex((1..x,Y)) :- Y=1..y, Y\  3  =1.

% Edges:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.


#show vertex/1.
#show edge/2.
