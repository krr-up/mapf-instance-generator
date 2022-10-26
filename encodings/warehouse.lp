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

#show   edge/2.
#show vertex/1.
#show shelf/1.
#show start_area/1.
