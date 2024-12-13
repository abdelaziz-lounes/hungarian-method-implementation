# Hungarian Method Implementation in Python

This project implements the Hungarian Method (also known as the Méthode Hongroise) in Python for solving optimization problems such as assigning tasks or resources to minimize total costs.

## Features

- Calculates the cost matrix based on given flow and distance matrices.
- Performs row and column reductions to initialize the Hungarian method.
- Identifies and adjusts the matrix for optimal zero coverage.
- Computes the optimal assignment of tasks to resources.
- Calculates the minimal total cost for the assignment.

## How It Works

### Input Matrices

The algorithm requires two input matrices:
- **Flow matrix (F):** Represents the interaction or flow between tasks or resources, where `F[i][j]` is the flow between task/resource `i` and `j`.
- **Distance matrix (D):** Represents the distances or costs, where `D[i][j]` is the cost of assigning task/resource `i` to `j`.

### Steps

1. **Compute the Cost Matrix (C):**
   Each element of the cost matrix is calculated as `C[i][j] = F[i][j] * D[i][j]`.

2. **Row and Column Reductions:**
   - Subtract the minimum value of each row from all elements in the row.
   - Subtract the minimum value of each column from all elements in the column.

3. **Zero Coverage:**
   - Identify rows and columns needed to cover all zeros in the matrix.
   - Adjust uncovered elements to continue refining the matrix.

4. **Assignment:**
   - Find optimal zero positions in the adjusted matrix to assign tasks/resources.

5. **Calculate Total Cost:**
   - Compute the minimal total cost based on the optimal assignment.

## Code Example

### Input Example
```python
F = np.array([
    [0, 1, 0, 1],
    [1, 0, 0, 2],
    [0, 0, 0, 2],
    [1, 2, 3, 0]
])

D = np.array([
    [0, 4, 3, 5],
    [4, 0, 5, 4],
    [3, 5, 0, 4],
    [5, 4, 4, 0]
])
```

### Output Example
```
Assignation optimale des commerces aux emplacements :
Commerce c0 -> Emplacement e2
Commerce c1 -> Emplacement e0
Commerce c2 -> Emplacement e3
Commerce c3 -> Emplacement e1

Coût total minimal : 31
```

## Prerequisites

- Python 3.x
- Numpy

Install the required library with:
```bash
pip install numpy
```

## Usage

1. Clone this repository.
2. Replace the flow and distance matrices (`F` and `D`) with your data.
3. Run the script to compute the optimal assignment and total cost.

```bash
python hungarian_method.py
```

## Acknowledgments

This project is based on the Hungarian Method for solving assignment problems in optimization and is tailored to compute the minimal cost efficiently.

---
Feel free to contribute or modify this code for your specific use case!

