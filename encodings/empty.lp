% size:
#const x=2.
#const y=2.

% vertices:
{vertex((1..x,1..y))} = x*y.

% edges from vertices that are adjacent:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.

#show   edge/2.
#show vertex/1.
