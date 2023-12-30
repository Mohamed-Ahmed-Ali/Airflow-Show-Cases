# Airflow DAGs Showcase

## Overview
This repository contains a collection of Apache Airflow DAGs showcasing various tasks and functionalities. Each DAG is designed to demonstrate specific skills and features related to data pipeline orchestration and automation.

### Table of Contents
1. [Hello World Bash DAG](#hello-world-bash-dag)
2. [Hello World Python DAG](#hello-world-python-dag)
3. [SQL Operations DAG](#sql-operations-dag)
4. [Parameterized Python DAG](#parameterized-python-dag)
5. [XCom Push-Pull DAG](#xcom-push-pull-dag)
6. [XCom Function DAG](#xcom-function-dag)

## Hello World Bash DAG
- **Description:** Simple tutorial DAG using BashOperator.
- **Task:**
  - Task 1: Print "Hello, World!" using BashOperator.
- **DAG Structure:**
  - Start Date: 2023-10-31
  - Schedule: Hourly

## Hello World Python DAG
- **Description:** Simple tutorial DAG using PythonOperator.
- **Task:**
  - Task 1: Print "Hello, World!" using PythonOperator.
- **DAG Structure:**
  - Start Date: 2023-10-31
  - Schedule: Hourly

## SQL Operations DAG
- **Description:** Demonstrates SQL operations using PostgresOperator.
- **Tasks:**
  - Task 1: Create a Postgres table if not exists.
  - Task 2: Insert data into the table.
  - Task 3: Delete data from the table.
- **DAG Structure:**
  - Start Date: 2023-11-11
  - Schedule: Hourly

## Parameterized Python DAG
- **Description:** DAG with a parameterized Python function.
- **Task:**
  - Task 1: Print a personalized greeting using PythonOperator.
- **DAG Structure:**
  - Start Date: 2023-10-31
  - Schedule: Hourly

## XCom Push-Pull DAG
- **Description:** DAG demonstrating XCom push and pull functionalities.
- **Tasks:**
  - Task 1: Push first and last name to XCom.
  - Task 2: Push age and city to XCom.
  - Task 3: Pull data from XCom and print a personalized greeting.
- **DAG Structure:**
  - Start Date: 2023-10-31
  - Schedule: Hourly

## XCom Function DAG
- **Description:** DAG with XCom demonstrating a function.
- **Tasks:**
  - Task 1: Define a function to return a name.
  - Task 2: Pull the name from XCom and print a greeting.
- **DAG Structure:**
  - Start Date: 2023-10-31
  - Schedule: Hourly

## Getting Started
1. Clone this repository.
2. Install Apache Airflow (if not already installed).
3. Copy DAG files into your Airflow DAGs directory.
4. Start the Airflow webserver and scheduler.

Feel free to explore each DAG for detailed comments and explanations. Happy coding!

**Author:** Mohamed-Ali

**Contact:** Mohamed.ali.c2021@gmail.com
