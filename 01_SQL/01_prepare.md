# Prepare your environment


1. Open a duckdb file `01_sql.db`:
- you can use Python:

```
>>> import duckdb
>>> con = duckdb.connect("01_sql.db")
```

- [Dbeaver](https://duckdb.org/docs/guides/sql_editors/dbeaver.html)
- or any other client

The database should contain following data:

```sql
CREATE TABLE if not exists courses(student_id int, event_type varchar(8), course_id int, event_timestamp datetime);
    
INSERT INTO courses
    (student_id, event_type, course_id, event_timestamp)
VALUES
    (1, 'start', 1, '2019-01-01 22:00:00'),
    (1, 'end', 1, '2019-01-01 22:30:00'),
    (1, 'start', 1, '2019-01-02 21:00:00'),
    (1, 'end', 1, '2019-01-02 21:10:00'),
    (1, 'start', 2, '2019-01-03 21:00:00'),
    (1, 'end', 2, '2019-01-03 22:00:00'),
    (1, 'display', NULL, '2019-01-02 21:00:00'),
    (1, 'finished', 4, '2019-01-03 22:00:00'),
    (2, 'start', 1, '2019-01-01 22:00:00'),
    (2, 'end', 1, '2019-01-01 22:30:00'),
    (3, 'start', 1, '2019-01-02 21:00:00'),
    (3, 'end', 1, '2019-01-02 21:10:00'),
    (3, 'start', 2, '2019-01-03 21:00:00'),
    (3, 'end', 2, '2019-01-03 22:00:00'),
    (5, 'display', NULL, '2019-01-02 21:00:00'),
    (5, 'finished', 1, '2019-01-03 22:00:00'),
    (6, 'start', 1, '2019-01-01 22:00:00'),
    (6, 'end', 1, '2019-01-01 22:30:00'),
    (7, 'start', 1, '2019-01-02 21:00:00'),
    (7, 'end', 1, '2019-01-02 21:10:00'),
    (9, 'start', 2, '2019-01-03 21:00:00'),
    (9, 'end', 2, '2019-01-03 22:00:00'),
    (1, 'display', NULL, '2019-01-02 21:00:00'),
    (1, 'finished', 3, '2019-01-03 22:00:00'),
    (3, 'start', 1, '2019-01-01 22:00:00'),
    (3, 'end', 1, '2019-01-01 22:30:00'),
    (2, 'start', 1, '2019-01-02 21:00:00'),
    (2, 'end', 1, '2019-01-02 21:10:00'),
    (8, 'start', 2, '2019-01-03 21:00:00'),
    (8, 'end', 2, '2019-01-03 22:00:00'),
    (1, 'display', NULL, '2019-01-02 21:00:00'),
    (3, 'finished', 4, '2019-01-03 22:00:00'),
    (4, 'start', 1, '2019-01-01 22:00:00'),
    (4, 'end', 1, '2019-01-01 22:30:00'),
    (7, 'start', 1, '2019-01-02 21:00:00'),
    (7, 'end', 1, '2019-01-02 21:10:00'),
    (1, 'start', 2, '2019-01-03 21:00:00'),
    (1, 'end', 2, '2019-01-03 22:00:00'),
    (1, 'display', NULL, '2019-01-02 21:00:00'),
    (3, 'finished', 2, '2019-01-03 22:00:00'),
    (3, 'finished', 4, '2019-01-03 22:00:00'),
    (6, 'finished', 4, '2019-01-03 22:00:00'),
    (10, 'finished', 1, '2019-01-03 22:00:00')
;

CREATE TABLE if not exists students (student_id int, name varchar(28), is_active bool, student_type varchar(3));
    
INSERT INTO students
    (student_id, name, is_active, student_type)
VALUES
    (1, 'Bill Blackbeard', true, 'b2b'),
    (2, 'Long Bill Ginger', true, 'b2c'),
    (3, 'Large Bill', true, 'b2b'),
    (4, 'Dreadful John', true, 'b2c'),
    (5, 'Cutthroat Bill The Long', true, 'b2b'),
    (6, 'Pete Greyhate', true, 'b2b'),
    (7, 'John Largeparrot', true, 'b2b'),
    (8, 'First Mate John The Dreadful', false, 'b2c'),
    (9, 'Dread Pirate Pete', false, 'b2b'),
    (10, 'Captain John', false, 'b2c')
;
```
2. Go to [02_assignment.md](02_assignment.md) and try to answer the questions.