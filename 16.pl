% Facts
parent('Hasib', 'Rakib').
parent('Rakib', 'Sohel').
parent('Rakib', 'Rebeka').
parent('Rashid', 'Hasib').

male('Hasib').
male('Rakib').
male('Rashid').


% Grandparent rule
grandparent(X, Z) :-
    parent(X, Y),
    parent(Y, Z).


% Brother rule
brother(X, Y) :-
    parent(Z, X),
    parent(Z, Y),
    male(X),
    X \= Y.


% Father rule
father(X, Y) :-
    parent(X, Y),
    male(X).


% Sample Queries

% Is Hasib a grandparent of Rebeka?
% ?- grandparent('Hasib', 'Rebeka').

% Who are the parents of Rebeka?
% ?- parent(X, 'Rebeka').

% Who are parents?
% ?- parent(X, _).

% Is Hasib a parent?
% ?- parent('Hasib', _).

% Is Hasib a parent of Rebeka?
% ?- parent('Hasib', 'Rebeka').

% Who have parents?
% ?- parent(_, X).

% Who are parents of whom?
% ?- parent(X, Y).

% Is there anybody who is a grandparent of somebody?
% ?- grandparent(_, _).

% Does Sohel have a grandparent?
% ?- grandparent(X, 'Sohel').

% Who is a parent and also has a parent?
% ?- parent(X, _), parent(_, X).

% Who either is a parent or has a parent?
% ?- parent(X, _); parent(_, X).

% Who is Rebeka's parent?
% ?- parent(X, 'Rebeka').

% Who is Sohel's grandparent?
% ?- grandparent(X, 'Sohel').