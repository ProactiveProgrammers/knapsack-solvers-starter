# Knapsack Solvers

## Assigned: Tuesday, May 10, 2022
## Due: Wednesday, May 18, 2022

After cloning this repository to your computer, please take the following steps:

- Follow the instructions on the Proactive Programmers web site for this project
- Use the `cd` command to change into the directory for this repository.
- Change into the program directory by typing `cd source`.
- Run both of the provided Python scripts by typing the following:
  - `python demonstrate_knapsack_solvers.py`: run all of the various knapsack solvers
- Add all of the missing source code by reading the content in the book
- You may also find some of the missing source code in the Jupyter Notebooks on Proactive Programmers Live
- Ensure that you know how to calculate the powerset of a set in Python, reading the referenced web site
- Make sure that you regularly commit to your GitHub repository, using short descriptive commit messages
- Use a `docker run` command for your operating system to run GatorGrader
- Provide all of the required responses in the `writing/reflection.md` file
- The program should ultimately produce the following output:

```text
Running all of the knapsack solvers!

Using greedy-by-value to fill knapsack of size 20
Total value of items taken is 200.0
   (Computer, 200, 20)

Using greedy-by-weight to fill knapsack of size 20
Total value of items taken is 170.0
   (Book, 10, 1)
   (Vase, 50, 2)
   (Radio, 20, 4)
   (Painting, 90, 9)

Using greedy-by-density to fill knapsack of size 20
Total value of items taken is 255.0
   (Vase, 50, 2)
   (Clock, 175, 10)
   (Book, 10, 1)
   (Radio, 20, 4)

Generating the powerset of all items!

Using exhaustive enumeration to fill a knapsack of size 20
Total value of items taken is 275.0
   (Clock, 175, 10)
   (Painting, 90, 9)
   (Book, 10, 1)
```
