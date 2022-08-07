#show.
#show init(object(node, 1), value(at, V)) : vertex(V).

#show init(object(robot,R), value(at, S)) : start(R,S).
#show init(object(shelf,R), value(at, G)) :  goal(R,G).

#show occurs(object(robot,R),action(move,(XX-X,YY-Y)),T) : move(R,(X,Y),(XX,YY),T).
