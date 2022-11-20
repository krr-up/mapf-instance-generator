#include <incmode>.

#program base.

at(A,V,0) :- start(A,V).

#program check(t).

% - query -----------------------------------------------------------------

:- goal(A,V), not at(A,V,t), query(t).

#program step(t).

% - vertex collision ------------------------------------------------------
:- #count { A: at(A,V,t) } > 1, vertex(V).

% - edge collision --------------------------------------------------------
:- move(_,U,V,t), block_edge(U,V,S), move(_,V,U,t+S).

% - auxiliaries -------------------------------------------- redundant ----
:- { location(A,V,t) } != 1, agent(A).

{ move(A,U,V,t): edge(U,V,_) } 1 :- agent(A).

% - move ------------------------------------------------------------------
at(A,V,t) :- move(A,U,V,t-D+1), edge(U,V,D).
:- move(A,V,_,t), not at(A,V,t-1).

% - inertia ---------------------------------------------------------------
at(A,V,t) :- at(A,V,t-1), not move(A,V,_,t).

% ensure unique agent positions
location(A,V,t)     :- at(A,V,t).
location(A,(U,V),t) :- move(A,U,V,t-S), edge(U,V,D), S=0..D-2.

% handle arrival conflicts
:- at(A,V,t), move(A2,U,V,t+S), A!=A2, block_arrival(U,V,S).

% compute block offsets for arrivals
block_arrival(U,V,S-D) :- edge(U,V,D), S=1..D.

% compute block offsets for edge conflcits
block_edge(U,V,S) :- edge(U,V,D), S=0..D-1.

#show move/4.
