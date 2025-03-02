#importing the qiskit libreary(its an opensource libreary by IBM)
from qiskit import QuantumCircuit

# Create a 2-qubit quantum circuit
qc = QuantumCircuit(2)

# Apply Hadamard gate on qubit 0
qc.h(0)

# Apply CNOT gate (controled not gate)
qc.cx(0, 1)

# This line helps to Draw the circuit
qc.draw('mpl')
