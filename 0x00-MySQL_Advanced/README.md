Here's a sample `README.md` file for your project:

```markdown
# MySQL Advanced

This project involves various advanced tasks in MySQL, including creating tables with constraints, optimizing queries by adding indexes, implementing stored procedures, functions, views, and triggers.

## Table of Contents

1. [Introduction](#introduction)
2. [Resources](#resources)
3. [Learning Objectives](#learning-objectives)
4. [Requirements](#requirements)
5. [Tasks](#tasks)
    - [Task 0: We are all unique!](#task-0-we-are-all-unique)
    - [Task 1: In and not out](#task-1-in-and-not-out)
    - [Task 2: Best band ever!](#task-2-best-band-ever)
    - [Task 3: Old school band](#task-3-old-school-band)
    - [Task 4: Buy buy buy](#task-4-buy-buy-buy)
    - [Task 5: Email validation to sent](#task-5-email-validation-to-sent)
    - [Task 6: Add bonus](#task-6-add-bonus)
    - [Task 7: Average score](#task-7-average-score)
    - [Task 8: Optimize simple search](#task-8-optimize-simple-search)

## Introduction

This project explores advanced features of MySQL, a popular relational database management system. It focuses on enhancing database functionality, performance, and data integrity through the use of constraints, indexes, stored procedures, functions, views, and triggers.

## Resources

To complete this project, the following resources were used:
- [MySQL cheatsheet](https://example.com)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://example.com)
- [Stored Procedure](https://example.com)
- [Triggers](https://example.com)
- [Views](https://example.com)
- [Functions and Operators](https://example.com)
- [Trigger Syntax and Examples](https://example.com)
- [CREATE TABLE Statement](https://example.com)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://example.com)
- [CREATE INDEX Statement](https://example.com)
- [CREATE VIEW Statement](https://example.com)

## Learning Objectives

By the end of this project, you should be able to:
- Create tables with constraints in MySQL
- Optimize queries by adding indexes
- Implement stored procedures and functions in MySQL
- Implement views in MySQL
- Implement triggers in MySQL

## Requirements

- All files will be executed on Ubuntu 18.04 LTS using MySQL 5.7 (version 5.7.30)
- All files should end with a new line
- All SQL queries should have a comment just before them
- All files should start with a comment describing the task
- All SQL keywords should be in uppercase (e.g., SELECT, WHERE)
- A `README.md` file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using `wc`

## Tasks

### Task 0: We are all unique!
**File:** `0-uniq_users.sql`

Write a SQL script that creates a table `users` with the following requirements:
- `id` - integer, never null, auto increment and primary key
- `email` - string (255 characters), never null and unique
- `name` - string (255 characters)
- The script should not fail if the table already exists
- The script can be executed on any database

### Task 1: In and not out
**File:** `1-country_users.sql`

Write a SQL script that creates a table `users` with the following requirements:
- `id` - integer, never null, auto increment and primary key
- `email` - string (255 characters), never null and unique
- `name` - string (255 characters)
- `country` - enumeration of countries: US, CO, and TN, never null (default will be US)
- The script should not fail if the table already exists
- The script can be executed on any database

### Task 2: Best band ever!
**File:** `2-fans.sql`

Write a SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.
- Import the table dump: `metal_bands.sql.zip`
- Column names must be: `origin` and `nb_fans`
- The script can be executed on any database

### Task 3: Old school band
**File:** `3-glam_rock.sql`

Write a SQL script that lists all bands with Glam rock as their main style, ranked by their longevity.
- Import the table dump: `metal_bands.sql.zip`
- Column names must be: `band_name` and `lifespan`
- Use attributes `formed` and `split` for computing the lifespan
- The script can be executed on any database

### Task 4: Buy buy buy
**File:** `4-store.sql`

Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
- Quantity in the table `items` can be negative

### Task 5: Email validation to sent
**File:** `5-valid_email.sql`

Write a SQL script that creates a trigger that resets the attribute `valid_email` only when the email has been changed.

### Task 6: Add bonus
**File:** `6-bonus.sql`

Write a SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.
- Procedure `AddBonus` is taking 3 inputs (in this order): `user_id`, `project_name`, `score`
- The script can be executed on any database

### Task 7: Average score
**File:** `7-average_score.sql`

Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and stores the average score for a student.
- Procedure `ComputeAverageScoreForUser` is taking 1 input: `user_id`

### Task 8: Optimize simple search
**File:** `8-index_my_names.sql`

Write a SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.
- Import the table dump: `names.sql.zip`
- Only the first letter of `name` must be indexed

## Author
[Johnny](https://github.com/johnamet)
```

This `README.md` file provides an overview of the project, including the tasks, requirements, resources, and learning objectives. Each task is briefly described, along with the expected file name for the corresponding SQL script.
