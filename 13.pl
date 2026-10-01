% fact
parent('Hasib','Rakib').
parent('Rakib','Sohel').
parent('Rakib','Rebeka').
parent('Rashid','Hasib').

% rule
grandparent(X,Z):-
	parent(X,Y),parent(Y,Z).

% procedure
findGp:-
	write('Grandchild: '),read(Gc),write('Grandparent: '),
	grandparent(Gp, Gc),write(Gp),tab(5),fail.
findGp.