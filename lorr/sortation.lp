% Default and minimal dimensions:
#const x=13.
#const y=13.

% Nr. of fitting stations per dimension:
xfs(1..(x-11)/2).
yfs(1..(y-11)/2).


% Corners:
corner((X,Y)) :- X= 1 ..4, Y= 1 ..4.
corner((X,Y)) :- X=x-3..x, Y= 1 ..4.
corner((X,Y)) :- X= 1 ..4, Y=y-3..y.
corner((X,Y)) :- X=x-3..x, Y=y-3..y.


% Stations (filled from top-left to bottom-right:
station((X,Y)) :- X=5+2*XF, Y=5+2*YF, xfs(XF), yfs(YF).


% Vertices:
vertex((X,Y)) :- X=1..x, Y=1..y, not corner((X,Y)), not station((X,Y)).


% Edges:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.


% Emitter:
%% left (from top to bottom):
emitter((1,Y)) :- vertex((1,Y)), Y>5, Y<y-4, Y\2=0.

%% right (from bottom to top):
emitter((x,Y)) :- vertex((x,Y)), Y>5, Y=y-4-M, M\2=1, M=1..y-10.

%% top (from right to left):
emitter((X,1)) :- vertex((X,1)), X>5, X=x-4-M, M\2=1, M=1..x-10.

%% bottom (from left to right):
emitter((X,y)) :- vertex((X,y)), X>5, X<x-4, X\2=0.


% Service points:
service((X,Y)) :- vertex((X,Y)), X>5, X<x-4, Y>5, Y<y-4, not vertex((X+X2,Y+Y2)), X2=-1..1, Y2=-1..1, |X2|+|Y2|=1.


#show vertex/1.
#show edge/2.
#show emitter/1.
#show service/1.
