#include <incmode>.

#const agent = 1.

#program base.

at(agent,P,0) :- start(agent,P).


#program check(t).

% - query -----------------------------------------------------------------

:- goal(agent,P), not at(agent,P,t), query(t).


#program step(t).

time(t).

{move(agent,U,V,t) : edge(U,V)}1.

% - move ------------------------------------------------------------------
at(agent,V,t) :- move(agent,U,V,t), at(agent,U,t-1), edge(U,V).

% - inertia ---------------------------------------------------------------
at(agent,V,t) :- at(agent,V,t-1), not move(agent,_,_,t).

#show.
#show move/4.
#show path_length(agent,T) : goal(agent,P), at(agent,P,T).
