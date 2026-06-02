from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# 3 qubits:
# q0 = unknown state to teleport
# q1 = Alice's entangled qubit
# q2 = Bob's entangled qubit
qc = QuantumCircuit(3, 3)

# Prepare the unknown state on q0
# Here we create |+> = (|0> + |1>) / sqrt(2)
qc.h(0)

qc.barrier()

# Create entangled Bell pair between q1 and q2
qc.h(1)
qc.cx(1, 2)

qc.barrier()

# Alice applies teleportation operations
qc.cx(0, 1)
qc.h(0)

qc.barrier()

# Alice measures q0 and q1
qc.measure(0, 0)
qc.measure(1, 1)

qc.barrier()

# Bob applies correction operations
qc.cx(1, 2)
qc.cz(0, 2)

# Measure Bob's qubit
qc.measure(2, 2)

print("Quantum Teleportation Circuit:")
print(qc)

# Run simulation
simulator = AerSimulator()
job = simulator.run(qc, shots=1024)
result = job.result()
counts = result.get_counts()

print("\nMeasurement Results:")
print(counts)

plot_histogram(counts)
plt.title("Quantum Teleportation Measurement Results")
plt.savefig("quantum_teleportation_results.png")
plt.show()
