#include <incmode>.

#program base.

at(R,P,0) :- start(R,P).

#program check(t).

% - query -----------------------------------------------------------------

:- goal(R,P), not at(R,P,t), query(t).

#program step(t).

% - vertex collision ------------------------------------------------------
 :- { at(R,V,t) : agent(R) }  > 1, vertex(V).

% - edge collision --------------------------------------------------------
 :- move(_,U,V,t), move(_,V,U,t), U < V.

% - auxiliaries -------------------------------------------- redundant ----
 :- { at(R,V,t) } != 1, agent(R).

{ move(R,U,V,t) : edge(U,V)} 1 :- agent(R).

% - move ------------------------------------------------------------------
at(R,V,t) :- move(R,_,V,t).
:- move(R,U,_,t), not at(R,U,t-1).

% - inertia ---------------------------------------------------------------
at(R,V,t) :- at(R,V,t-1), not move(R,V,_,t), agent(R).

% - acyclic ---------------------------------------------------------------
#edge ((A,U),(A,V)) : move(A,U,V,_), agent(A), acyclic=1.

#show.
#show move/4.
