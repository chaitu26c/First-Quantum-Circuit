# First-Quantum-Circuit

# **Quantum Entanglement Circuit**

## **Overview**
This repository contains a simple quantum circuit demonstrating **quantum entanglement** using **Qiskit**. The circuit creates a Bell state (a maximally entangled state) using a **Hadamard gate** and a **CNOT gate**.

## **Concept: Quantum Entanglement**
Quantum entanglement is a fundamental principle in quantum mechanics where two or more qubits become correlated such that the state of one qubit depends on the state of another, even if they are far apart. In this project, we create a Bell pair:



## **Code Explanation**
The circuit consists of:
1. A **Hadamard gate** (`H`): Applied to qubit 0 to create superposition.
2. A **CNOT gate** (`CX`): Applied between qubit 0 (control) and qubit 1 (target) to create entanglement.
