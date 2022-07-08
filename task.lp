% number of robots:
#const r=1.
% min plan length:
%#const min=2.
% max plan length:
%#const max=2.

node(N) :- edge(N,_).
node(N) :- edge(_,N).

1{task(R,S,G) :  node(S), node(G)}1 :- R=1..r.

:- task(R,S,_), task(R2,S,_), R<R2.
:- task(R,_,G), task(R2,_,G), R<R2.
:- task(_,V,_), task(_,_,V).

% TODO: get plan lengths and ensure plan lenghts between min and max 

#show edge/2.
#show task/3.
