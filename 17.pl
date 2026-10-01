% Facts
parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').

% Rule
grandparent(X,Z) :-
    parent(X,Y),
    parent(Y,Z).

% Procedure
findGc :-
    write('Grandparent: '),
    read(Gp),
    write('Grandchildren: '),
    grandparent(Gp,Gc),
    write(Gc),
    tab(5),
    fail.

findGc.