#include <incmode>.

#program base.

at(R,P,0) :- start(R,P).



#program check(t).

% - query -----------------------------------------------------------------

:- goal(R,P), not at(R,P,t), query(t).

% - vertex collision ------------------------------------------------------
 :- { at(R,V,T) : agent(R) }  > 1, vertex(V), time(T).

% - edge collision --------------------------------------------------------
 :- move(_,U,V,T), move(_,V,U,T), U < V.

% - auxiliaries -------------------------------------------- redundant ----
 :- { at(R,V,T) } != 1, agent(R), time(T).



#program step(t).

time(t).

{ move(R,U,V,t) : edge(U,V)} 1 :- agent(R).%, time(T).

% - move ------------------------------------------------------------------
at(R,V,t) :- move(R,U,V,t), at(R,U,t-1), edge(U,V).

% - inertia ---------------------------------------------------------------
at(R,V,t) :- at(R,V,t-1), not move(R,_,_,t), agent(R).%, time(T).

% - acyclic ---------------------------------------------------------------
#edge ((A,U),(A,V)) : move(A,U,V,_), agent(A), acyclic=1.

#show.
#show move/4.
