#const horizon=1.
#const acyclic=0.

% - vertex collision ------------------------------------------------------
 :- { at(R,V,T) : agent(R) }  > 1, vertex(V), time(T).

% - edge collision --------------------------------------------------------
 :- move(_,U,V,T), move(_,V,U,T), U < V.

% - auxiliaries -------------------------------------------- redundant ----
 :- { at(R,V,T) } != 1, agent(R), time(T).

% - query -----------------------------------------------------------------

:- goal(R,P), not at(R,P,horizon).

at(R,P,0) :- start(R,P).

% -------------------------------------------------------------------------

time(1..horizon).

{ move(R,U,V,T) : edge(U,V)} 1 :- agent(R), time(T).

% - move ------------------------------------------------------------------
at(R,V,T) :- move(R,U,V,T), at(R,U,T-1), edge(U,V).

% - inertia ---------------------------------------------------------------
at(R,V,T) :- at(R,V,T-1), not move(R,_,_,T), agent(R), time(T).

% - acyclic ---------------------------------------------------------------
#edge ((A,U),(A,V)) : move(A,U,V,_), agent(A), acyclic=1.

#show.
#show move/4.
