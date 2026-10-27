# CSCE 2120 Lab Portfolio

CSCE 2120-001 Vectors and Matrices, Fall 2026, University of North Texas.
Author: Seokhyeon Jang.
EUID: sj1304.

## About

This repository collects my completed zyLab code from Modules 1-9 of CSCE 2120.
It is the portfolio for Course Project Part 1, backed up here on GitHub and
cloned onto a UNT CSE CELL machine.

## Contents

Each module folder holds the Python lab code for that module. All labs use
standard Python lists, loops, and functions (no NumPy).

- M01 (Lab 1.5): Basic Vector Operations in Python. Vector creation and
  representation, vector operations, direction and magnitude.
- M02 (Lab 2.4): Vector Products, Projection, and Plane Distance. Dot and
  cross products, vector projection, point-to-plane distance.
- M03 (Lab 3.6): Row Operations, Echelon Form, and Gaussian Elimination.
- M04 (Lab 4.4): Matrix Algebra and Matrix Equations.
- M05 (Lab 5.5): Matrix Inverses and Block Multiplication.
- M06 (Lab 6.3): Weather Markov Model with LU and Cholesky.
- M07 (Lab 7.5): Span, Independence, and Feature Bases.
- M08 (Lab 8.6): Change of Coordinates and Four Subspaces.
- M09 (Lab 9.6): Determinants, Invertibility, and Triangle Geometry.

## Setup and Backup

This section documents how the portfolio was assembled and backed up.

### Open CELL

Log in to a UNT CSE CELL machine from a local terminal:

```
ssh <EUID>@<CELL machine>
```

To log in without typing the password each time, set up an SSH key:

1. On the local machine, generate a key with `ssh-keygen` and accept the
   defaults (just press Enter at each prompt).
2. On CELL, make sure `~/.ssh` exists with the correct permissions:
```
mkdir -p ~/.ssh && chmod 700 ~/.ssh
touch ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys
```
3. Copy the public key to CELL. On macOS/Linux:
```
ssh-copy-id <EUID>@<CELL machine>
```
4. Test it by logging in again. It should not ask for a password.

### Upload files to CELL

Run scp from the local terminal, not from inside the CELL session. One file:

```
scp <local file> <EUID>@<CELL machine>:~/CSCE2120/zylab/M01/
```

A whole folder:

```
scp -r <local folder> <EUID>@<CELL machine>:~/CSCE2120/zylab/
```

### Push to GitHub and clone onto CELL

From the local CSCE2120 folder:

```
git init
git add .
git commit -m "CSCE 2120 lab portfolio"
git branch -M main
git remote add origin <repository address>
git push -u origin main
```

On CELL, clone the repository:

```
git clone <repository address>
```

This repository is cloned onto a UNT CSE CELL machine as a backup, as required
for Part 1. This workspace will be the starting point for Part 2.

### Verify

On CELL, list all files and check line counts:

```
find ~/CSCE2120 -type f | sort
find ~/CSCE2120 -name "*.py" -exec wc -l {} +
```
