-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE players (
	id serial primary key,
	name varchar(20) NOT NULL
);

CREATE TABLE matches (
	id serial primary key,
	winner int references players(id),
	loser int references players(id)
);

-- using self join to get winner view
CREATE VIEW winners AS
SELECT players.id, players.name, count(matches.winner) AS wins
   	FROM players LEFT JOIN matches
        ON players.id = matches.winner
   	GROUP BY players.id
   	ORDER BY wins DESC;

-- using self join to get losers view
CREATE VIEW losers AS
SELECT players.id, players.name, count(matches.loser) AS losses
   	FROM players LEFT JOIN matches
        ON players.id = matches.loser
   	GROUP BY players.id
   	ORDER BY losses DESC;

-- using winners and losers views to create standings view
CREATE VIEW standings AS
SELECT winners.id, winners.name, winners.wins, winners.wins + losers.losses as played 
	FROM winners, losers
	WHERE winners.id = losers.id
	ORDER BY wins DESC;



