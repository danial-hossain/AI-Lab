% parent fact
parent('Rashid','Hasib').
parent('Rashid','Rima').

parent('Hasib','Rakib').
parent('Hasib','Karim').

parent('Rakib','Sohel').
parent('Rakib','Rebeka').

% gender fact
male('Rashid').
male('Hasib').
male('Rakib').
male('Karim').
male('Sohel').

female('Rima').
female('Rebeka').

%rule
sibling(X,Y):-
    parent(P,X),
    parent(P,Y),
    X\= Y.

brother(X,Y):-
    sibling(X,Y),
    male(X).

sister(X,Y):-
    sibling(X,Y),
    female(X).

uncle(X,Y):-
    brother(X,P),
    parent(P,Y).

aunt(X,Y):-
    sister(X,P),
    parent(P,Y).

% procedure

findBrother:-
    write('Person: '), read(P), write('Brother: '), brother(B,P), write(B), tab(5),fail.
findBrother.

findSister:-
    write('Person: '), read(P), write('Sister: '), sister(S,P), write(S), tab(5), fail.
findSister.

findUncle:-
    write('Person: '),  read(P), write('Uncle: '), uncle(U,P), write(U), tab(5), fail.
findUncle.

findAunt:-
    write('Person: '), read(P), write('Aunt: '), aunt(A,P), write(A), tab(5), fail.
findAunt.
