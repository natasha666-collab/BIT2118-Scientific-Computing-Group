# Task 9: Eigenvalues and Eigenvectors

---

##  what are eigenvalues and eigenvectors?

For a square matrix **A**, an eigenvector **v** is a non-zero vector whose direction is unchanged when A is applied to it. It is only scaled:

```
A v = λ v
```

The number **λ** is the eigenvalue. If |λ| > 1 the vector is stretched, if |λ| < 1 it is compressed, and if λ is negative its direction is reversed.

When **A** is the adjacency matrix of a network (entry `1` if two nodes are connected, `0` if not), the eigenvector for the **largest** eigenvalue gives every node a score that depends on:

1. how many connections the node has, and
2. how important those connections are.

This is **eigenvector centrality**, the idea behind Google PageRank. A node is important if it is connected to other important nodes.

---

## A. Input values and mathematical operation

### Original program (`Task_09_eigenvalues.py`)

**Input:** the adjacency matrix **A** of a small undirected network with four nodes A, B, C, D:

```
      A  B  C  D
A  [  0  1  1  0 ]
B  [  1  0  1  1 ]
C  [  1  1  0  1 ]
D  [  0  1  1  0 ]
```

The links are A–B, A–C, B–C, B–D and C–D. The matrix is symmetric because the links work in both directions, and the diagonal is zero because no node links to itself.

**Mathematical operations performed:**

| Step | Code | What it does |
|------|------|--------------|
| 1 | `np.linalg.eig(A)` | Solves det(A − λI) = 0 to find every eigenvalue and its eigenvector |
| 2 | `np.argmax(np.real(eigenvalues))` | Finds the position of the largest (dominant) eigenvalue |
| 3 | `np.abs(np.real(eigenvectors[:, index]))` | Extracts the dominant eigenvector. The absolute value removes an arbitrary ± sign, because NumPy may return v or −v |
| 4 | `dominant_vector / dominant_vector.sum()` | Normalizes the scores so they add up to 1 (each score becomes a share of total influence) |
| 5 | `np.linalg.norm(A @ v - λ * v)` | Verifies that A v = λ v. The result should be close to zero |

### Output of the original program

```
Dominant eigenvalue: 2.561552812808829
Eigenvector-based importance:
A: 0.2192
B: 0.2808
C: 0.2808
D: 0.2192
Verification error: 1.5e-15
```

---

## B. Parameter change

Changing the adjacency matrix (for example, adding or removing a connection between nodes) changes the eigenvalues and eigenvectors. This alters the centrality scores, so different nodes become more or less "important".

### Change 1: add a link between A and D (original network)

```python
A[0, 3] = A[3, 0] = 1
```

| | Original | After adding A–D |
|---|---|---|
| Dominant eigenvalue | 2.5616 | **3.0000** |
| A | 0.2192 | **0.2500** |
| B | 0.2808 | **0.2500** |
| C | 0.2808 | **0.2500** |
| D | 0.2192 | **0.2500** |

**Explanation:** every node is now connected to every other node (a complete network), so each node has exactly 3 links. No node has an advantage any more, so all four scores equal 0.25. The dominant eigenvalue becomes exactly 3, the number of links per node. Nodes A and D gained influence, while B and C lost their advantage.

### Change 2: changes in the social network (real-world program)

These are explained in Section D, where the two changes tested are adding an A–E friendship and removing all of C's friendships.

### General rule observed

The dominant eigenvalue always lies between the **average** number of connections and the **maximum** number of connections per node. In the original network the average is 2.5, the maximum is 3 and the eigenvalue is 2.56. Adding links raises the eigenvalue, and removing links lowers it.

---

## C. Meaning of the output

- The **dominant eigenvalue** indicates the strength of the most influential connectivity pattern in the network. A larger value means the network is more densely and strongly connected overall.
- The **dominant eigenvector**, after normalization, gives an importance score for each node (eigenvector-based centrality). The scores add up to 1, so each can be read as that node's share of the total influence.
- A higher centrality value means the node is more structurally central in the network.
- The **verification error** (about 10⁻¹⁵) is not a real error. It is floating-point round-off, which shows that the computed eigenpair satisfies A v = λ v.

### Reading the original output

- **B and C (0.2808)** are the most central. Each has 3 links, and their neighbours are also well connected.
- **A and D (0.2192)** are less central. Each has only 2 links.
- B and C have identical scores, and so do A and D, because the network is symmetric: swapping B with C and A with D gives the same network.
- B and C are the critical nodes. If either one failed, the network would lose the most connectivity.

---

## D. Modified real-world case

### Case: influence in a student friendship network

**Problem:** Model a small social network (students in a class) where edges represent friendships. Which student is the most influential, meaning the key connector or hub in the social graph? Simply counting friends is useful, but eigenvector centrality also takes into account how well connected each friend is.

### New assumptions

1. Nodes are 5 students: A, B, C, D and E.
2. Friendship is mutual, so the adjacency matrix is symmetric.
3. All friendships carry equal weight (no strong or weak friendships).
4. No student is friends with themselves, so the diagonal is zero.
5. Influence depends only on the pattern of friendships, not on personality, popularity or activity.
6. The friendships are invented for this exercise.

### Input data

Adjacency matrix of friendships (program: `Task_09_real_world.py`):

```
      A  B  C  D  E
A  [  0  1  1  0  0 ]    A is friends with B, C
B  [  1  0  1  1  0 ]    B is friends with A, C, D
C  [  1  1  0  1  1 ]    C is friends with A, B, D, E
D  [  0  1  1  0  1 ]    D is friends with B, C, E
E  [  0  0  1  1  0 ]    E is friends with C, D
```

| Student | Number of friends |
|---------|-------------------|
| A | 2 |
| B | 3 |
| C | 4 |
| D | 3 |
| E | 2 |

### Output

```
Eigenvector Centrality (Influence Scores):
A: 0.1593
B: 0.2136
C: 0.2541
D: 0.2136
E: 0.1593

Verification error: 2.2e-15
```

The dominant eigenvalue is **2.9354**.

### Interpretation

- **Student C (0.2541) is the most influential.** C is friends with every other student, so C is the central hub of the class. About 25% of the total influence in the network belongs to C.
- **Students B and D (0.2136 each)** are in the middle. Each has 3 friends, including the hub C.
- **Students A and E (0.1593 each)** are the least influential. Each has only 2 friends and they sit at opposite ends of the network, with no direct link to each other.
- **B and D have identical scores, and so do A and E**, because the network is symmetric: reversing the order of the students (A↔E, B↔D) gives the same friendship pattern.
- **The scores are a share of influence.** C's score is about 1.6 times that of A or E (0.2541 / 0.1593), even though C has only twice as many friends. Having well-connected friends adds to a student's influence.
- **The dominant eigenvalue of 2.94** lies between the average number of friends (2.8) and the maximum (4), as expected.
- **Practical meaning:** a message, announcement or rumour started by C would reach the whole class fastest. If C were absent, the class would become much less connected (see the test below).

### Parameter changes tested on the real-world case

#### Test 1: add a friendship between A and E

```python
A[0, 4] = A[4, 0] = 1
```

| Student | Friends (before → after) | Score before | Score after |
|---------|--------------------------|--------------|-------------|
| A | 2 → 3 | 0.1593 | **0.1910** |
| B | 3 → 3 | 0.2136 | 0.1910 |
| C | 4 → 4 | 0.2541 | 0.2361 |
| D | 3 → 3 | 0.2136 | 0.1910 |
| E | 2 → 3 | 0.1593 | **0.1910** |

Dominant eigenvalue: 2.9354 → **3.2361**

**Explanation:** the new friendship closes the loop of the network, so A and E are no longer at the ends. A and E gain influence (0.1593 → 0.1910). B and D lose some share, because the total of the scores must stay equal to 1. C is still the most influential, but its lead is smaller (0.2541 → 0.2361). A, B, D and E now all have the same score (0.1910). The eigenvalue rises because the network is better connected overall.

#### Test 2: remove all of C's friendships

```python
A[2, :] = 0
A[:, 2] = 0
```

| Student | Friends (before → after) | Score before | Score after |
|---------|--------------------------|--------------|-------------|
| A | 2 → 1 | 0.1593 | 0.1910 |
| B | 3 → 2 | 0.2136 | **0.3090** |
| C | 4 → 0 | 0.2541 | **0.0000** |
| D | 3 → 2 | 0.2136 | **0.3090** |
| E | 2 → 1 | 0.1593 | 0.1910 |

Dominant eigenvalue: 2.9354 → **1.6180**

**Explanation:** with C isolated, the remaining students form a chain A–B–D–E. C scores 0 because it has no connections, and the dominant eigenvalue drops sharply from 2.94 to 1.62. B and D become the most influential because they are now in the middle of the chain. Note that A and E score higher than before even though they have fewer friends. Scores are shares of a total of 1, and C's share was redistributed to the others. The result shows that C is a critical hub: the network's connectivity drops by almost half when C is removed.

### Summary of all tests

| Network | Dominant eigenvalue | Most influential |
|---------|--------------------|------------------|
| Original 4-node network | 2.5616 | B and C (0.2808) |
| 4-node network with A–D added | 3.0000 | All equal (0.2500) |
| 5-student network (original case) | 2.9354 | C (0.2541) |
| 5-student network with A–E added | 3.2361 | C (0.2361) |
| 5-student network with C removed | 1.6180 | B and D (0.3090) |

---

## Files in this folder

| File | Description |
|------|-------------|
| `README.md` | This documentation: inputs, operations, parameter changes, output meaning and the real-world case |
| `Task_09_eigenvalues.py` | Original program: eigenvector centrality of a 4-node network |
| `Task_09_real_world.py` | Modified program: influence of students in a 5-student friendship network |
