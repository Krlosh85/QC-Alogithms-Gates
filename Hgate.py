import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

## for display
from IPython.display import display

# Create a Quantum Circuit 
qc = QuantumCircuit(1,1)

# Add a H gate on qubit 0
qc.h(0)

# Map the quantum measurement from qubit 0 to the classical bit 0 
qc.measure(0,0)

# Draw the circuit
display(qc.draw())


# Use Aer's qasm_simulator
simulator = QasmSimulator()

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(qc, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal counts:",counts)

