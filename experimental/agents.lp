% agents:
#const a=1.
agent(1..a).

% start and goal:
1{start(A,S) :  vertex(S)}1 :- agent(A).
1{ goal(A,G) :  vertex(G)}1 :- agent(A).

:- 2{start(A,S) : agent(A)}, vertex(S).
:- 2{ goal(A,G) : agent(A)}, vertex(G).

%% start-goal overlap (0=allowed; 1=only for different agents; 2=not allowed):
#const sg=0.
:- start(A,V), goal(A,V), sg=1.
:- start(_,V), goal(_,V), sg=2.

% min. manhatten distance from start to goal:
#const d=0.
dist(D) :- D=|X-X2|+|Y-Y2|, start(A,(X,Y)), goal(A,(X2,Y2)), agent(A).
:- dist(D), D<d.

% agent distribution:
#const ad=0.
size(S) :- S=#max{X:vertex((X,_))}, ad>0.
%% cross sides:
:- start(_,(X,Y)), X<=S/2, size(S), ad=1.
:-  goal(_,(X,Y)), X> S/2, size(S), ad=1.

%% inside out:
:- start(_,(X,Y)), X<=   S/4,   size(S), ad=2.
:- start(_,(X,Y)), X> S-(S/4),  size(S), ad=2.
:- start(_,(X,Y)), Y<=   S/4,   size(S), ad=2.
:- start(_,(X,Y)), Y> S-(S/4),  size(S), ad=2.
:-  goal(_,(X,Y)), X>    S/4,
                   X<=S-(S/4),
                   Y>    S/4,
                   Y<= S-(S/4), size(S), ad=2.

%% tight to tight:
:- start(_,V), goal(_,V), ad=3.
:- start(_,(X,Y)), not start(_,(X+1,Y)), start(_,(X+2,Y)), ad=3.
:- start(_,(X,Y)), not start(_,(X,Y+1)), start(_,(X,Y+2)), ad=3.
:-  goal(_,(X,Y)), not  goal(_,(X+1,Y)),  goal(_,(X+2,Y)), ad=3.
:-  goal(_,(X,Y)), not  goal(_,(X,Y+1)),  goal(_,(X,Y+2)), ad=3.

:- start(A,(X,Y)), start(A2,(X2,Y2)), A>A2, (X-X2)**2>=a, ad=3.
:- start(A,(X,Y)), start(A2,(X2,Y2)), A>A2, (Y-Y2)**2>=a, ad=3.
:-  goal(A,(X,Y)),  goal(A2,(X2,Y2)), A>A2, (X-X2)**2>=a, ad=3.
:-  goal(A,(X,Y)),  goal(A2,(X2,Y2)), A>A2, (Y-Y2)**2>=a, ad=3.

%:- start(A,(X,Y)), start(A2,(X2,Y2)), A>A2, (X-X2)**2>=a, (Y-Y2)**2>=a, ad=3.
%:-  goal(A,(X,Y)),  goal(A2,(X2,Y2)), A>A2, (X-X2)**2>=a, (Y-Y2)**2>=a, ad=3.

%:- start(A,(X,Y)), start(A2,(X2,Y2)), A>A2, (|X-X2|+1)*(|Y-Y2|+1)>a, ad=3.
%:-  goal(A,(X,Y)),  goal(A2,(X2,Y2)), A>A2, (|X-X2|+1)*(|Y-Y2|+1)>a, ad=3.

%% swap sides:
:- start(A,(X,Y)), X<=S/2, size(S), A<=a/2, ad=4.
:- start(A,(X,Y)), X> S/2, size(S), A> a/2, ad=4.
:-  goal(A,(X,Y)), X> S/2, size(S), A<=a/2, ad=4.
:-  goal(A,(X,Y)), X<=S/2, size(S), A> a/2, ad=4.

%% outside in:
:-  goal(_,(X,Y)), X<=   S/4,   size(S), ad=5.
:-  goal(_,(X,Y)), X> S-(S/4),  size(S), ad=5.
:-  goal(_,(X,Y)), Y<=   S/4,   size(S), ad=5.
:-  goal(_,(X,Y)), Y> S-(S/4),  size(S), ad=5.
:- start(_,(X,Y)), X>    S/4,
                   X<=S-(S/4),
                   Y>    S/4,
                   Y<= S-(S/4), size(S), ad=5.
                   
%% tight to wide:


#show vertex/1.
#show agent/1.
#show edge/2.
#show start/2.
#show goal/2.
