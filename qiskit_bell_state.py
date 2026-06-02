from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 2-qubit circuit with 2 classical bits
qc = QuantumCircuit(2, 2)

# Put qubit 0 in superposition
qc.h(0)

# Entangle qubit 0 with qubit 1
qc.cx(0, 1)

# Measure both qubits
qc.measure([0, 1], [0, 1])

print("Qiskit Bell-State Circuit:")
print(qc)

# Run simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

# Save histogram
plot_histogram(counts)
plt.title("Qiskit Bell State Measurement Results")
plt.savefig("qiskit_bell_state_results.png")
plt.show()
