CREATE TABLE friends (
  id INTEGER,
  name TEXT,
  birthday DATE
);

INSERT INTO friends (id, name, birthday)
  VALUES (1, 'Ororo Munroe', '1940-05-30'),
  (2, 'Lily Sandstrom', '1992-04-22'),
  (3, 'Marcus McLain', '2001-11-18')
;

UPDATE friends 
SET name = 'Ororo Storm'
WHERE name = 'Ororo Munroe';

ALTER TABLE friends
ADD COLUMN email TEXT;

UPDATE friends
SET email = 'storm@codecademy.com'
WHERE id = 1;

UPDATE friends
SET email = 'lily.sandstrom@gmail.com'
WHERE id = 2;

UPDATE friends
SET email = 'marcusml@gmail.com'
WHERE id = 3;

DELETE FROM friends
WHERE id = 1;

SELECT *
FROM friends;
