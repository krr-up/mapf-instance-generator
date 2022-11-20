#include <incmode>.

#const agent = 1.

#program base.

at(agent,V,0) :- start(agent,V).

#program check(t).

% - query -----------------------------------------------------------------

:- goal(agent,V), not at(agent,V,t), query(t).

#program step(t).



{ move(agent,U,V,t): edge(U,V,_) }1.

% - move ------------------------------------------------------------------
at(agent,V,t) :- move(agent,U,V,t-D+1), edge(U,V,D).
:- move(agent,V,_,t), not at(agent,V,t-1).

% - inertia ---------------------------------------------------------------
at(agent,V,t) :- at(agent,V,t-1), not move(agent,V,_,t).

#show.
#show spath(agent,U,V,T) : move(agent,U,V,T).
#show spath_length(agent,T) : goal(agent,P), at(agent,P,T).
