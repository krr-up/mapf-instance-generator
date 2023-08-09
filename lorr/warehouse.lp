% Default and minimal dimensions:
#const x=19.
#const y=18.


% Nr. of fitting picking stations per dimension:
xfp(1..(x-8)/7).
yfp(1..(y-8)/7).

% Nr. of fitting shelves per dimension:
xfs(1..(x-15)/4).
yfs(1..(y-15)/3).


% Corners:
corner((X,Y)) :- X= 1 ..4, Y= 1 ..4.
corner((X,Y)) :- X=x-3..x, Y= 1 ..4.
corner((X,Y)) :- X= 1 ..4, Y=y-3..y.
corner((X,Y)) :- X=x-3..x, Y=y-3..y.


% Shelves (filled from top-left to bottom-right:
shelf((X,Y)) :- X=5+4*XF..5+4*XF+2, Y=6+3*YF..6+3*YF+1, xfs(XF), yfs(YF).


% Picking stations:
%% top (filled from right to left):
station((X,1..3)) :- X=x-(7*F)-1..x-(7*F)+1, xfp(F).

%% bottom (filled from left to right):
station((X,y-2..y)) :- X=7*F..7*F+2, xfp(F).

%% left (filled from top to bottom)):
station((1..3,Y)) :- Y=7*F..7*F+2, yfp(F).

%% right (filled from bottom to top)):
station((x-2..x,Y)) :- Y=y-(7*F)-1..y-(7*F)+1, yfp(F).


% Vertices:
vertex((X,Y)) :- X=1..x, Y=1..y,
                 not corner((X,Y)), not station((X,Y)), not shelf((X,Y)).


% Edges:
edge((X,Y),(X+DX,Y+DY)) :- vertex((X,Y)), vertex((X+DX,Y+DY)), DX=-1..1, DY=-1..1, |DX+DY|=1.


% Servie points:
service((X,Y)) :- vertex((X,Y)), X>7, X<x-6, Y>7, Y<y-6, not vertex((X+X2,Y+Y2)), X2=-1..1, Y2=-1..1, |X2|+|Y2|=1.


% Emitter:
%% left:
emitter((2,Y)) :- vertex((2,Y)), Y>5, Y<y-4, not vertex((2,Y+1)), vertex((2,Y-1)).
emitter((2,Y)) :- vertex((2,Y)), Y>5, Y<y-4, not vertex((2,Y-1)), vertex((2,Y+1)).

%% right:
emitter((x-1,Y)) :- vertex((x-1,Y)), Y>5, Y<y-4, not vertex((x-1,Y-1)), vertex((x-1,Y+1)).
emitter((x-1,Y)) :- vertex((x-1,Y)), Y>5, Y<y-4, not vertex((x-1,Y+1)), vertex((x-1,Y-1)).

%% top:
emitter((X,2)) :- vertex((X,2)), X>5, X<x-4, not vertex((X+1,2)), vertex((X-1,2)).
emitter((X,2)) :- vertex((X,2)), X>5, X<x-4, not vertex((X-1,2)), vertex((X+1,2)).

%% bottom:
emitter((X,y-1)) :- vertex((X,y-1)), X>5, X<x-4, not vertex((X+1,y-1)), vertex((X-1,y-1)).
emitter((X,y-1)) :- vertex((X,y-1)), X>5, X<x-4, not vertex((X-1,y-1)), vertex((X+1,y-1)).


#show vertex/1.
#show edge/2.
#show emitter/1.
#show service/1.
