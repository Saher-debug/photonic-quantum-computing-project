# From Quantum Entanglement to Photonic Teleportation

## A Comparative Study Using Qiskit and Perceval

### Author

**Saher Zayed**  
M.Sc. Computer and Systems Engineering  
Alexandria University

---

## Overview

Quantum computing can be approached from two complementary perspectives:

- **Gate-Based Quantum Computing**, where information is manipulated using logical quantum gates.
- **Photonic Quantum Computing**, where photons, beam splitters, phase shifters, and detectors physically implement quantum information processing.

This project explores both paradigms through a sequence of experiments that progressively build from fundamental quantum concepts to advanced photonic communication protocols.

The implementation combines:

- Qiskit
- Perceval
- NumPy
- Matplotlib

---

## Project Flow

```text
Bell State Generation
        ->
Quantum Teleportation
        ->
Hong-Ou-Mandel Interference
        ->
Photonic CNOT Gate
        ->
Boson Sampling
        ->
Large Photonic Interferometer
        ->
Photonic Quantum Teleportation
```

Each experiment introduces a new quantum concept while building toward scalable photonic quantum computing architectures.

---

## Experiment 1 - Bell State Generation

### Objective

Generate a Bell state and demonstrate quantum entanglement.

The Bell state implemented is:

```text
|Phi+> = (|00> + |11>) / sqrt(2)
```

This state represents one of the most fundamental entangled states in quantum information theory.

### Concepts Demonstrated

- Superposition
- Entanglement
- Quantum correlations

### Result

The experiment successfully generated an entangled Bell pair, providing the foundation required for quantum communication protocols and teleportation.

![Qiskit Bell State Measurement Histogram](quantam-circuit-simulation-figures/qiskit_bell_state/displayed_figure_01.png)

*Figure 1. Qiskit Bell State Measurement Histogram*

![Qiskit Bell State Saved Result](quantam-circuit-simulation-figures/qiskit_bell_state/qiskit_bell_state_results.png)

*Figure 2. Qiskit Bell State Saved Result*

---

## Experiment 2 - Quantum Teleportation (Qiskit)

### Objective

Demonstrate the transmission of an unknown quantum state using:

- Entanglement
- Classical communication
- Quantum corrections

Quantum teleportation does not transport matter. Instead, it transfers quantum information from one qubit to another.

### Protocol

1. Generate an entangled Bell pair.
2. Entangle the unknown state with Alice's qubit.
3. Perform Bell-basis measurements.
4. Send two classical bits to Bob.
5. Apply correction operations.
6. Reconstruct the original state.

### Measurement Results

The teleportation experiment produced approximately uniform measurement counts across the expected output states. The near-uniform distribution confirms the correct operation of the teleportation circuit and the successful reconstruction of the teleported quantum information.

![Qiskit Quantum Teleportation Measurement Histogram](quantam-circuit-simulation-figures/qiskit_quantum_teleportation/displayed_figure_01.png)

*Figure 3. Qiskit Quantum Teleportation Measurement Histogram*

![Qiskit Quantum Teleportation Saved Result](quantam-circuit-simulation-figures/qiskit_quantum_teleportation/quantum_teleportation_results.png)

*Figure 4. Qiskit Quantum Teleportation Saved Result*

---

## Experiment 3 - Hong-Ou-Mandel (HOM) Interference

### Objective

Demonstrate quantum interference using identical photons.

Two photons are injected into a 50/50 beam splitter simultaneously.

### Observation

Classically, one would expect the photons to randomly separate.

Quantum mechanically, the photons interfere and always exit together. This phenomenon is known as the **Hong-Ou-Mandel Effect**.

### Terminal Output

```text
Perceval Photonic Circuit:
<perceval.components.linear_circuit.Circuit object>

Input State:
|1,1>

Output Probability Distribution:
|2,0>: 0.5000
|0,2>: 0.5000
```

### Importance

The HOM effect is one of the most important interference phenomena in photonic quantum computing and serves as the basis for many optical quantum gates.

---

## Experiment 4 - Photonic CNOT Gate

### Objective

Implement a Controlled-NOT gate using photonic hardware primitives.

The implementation utilizes:

- Dual-rail encoding
- Beam splitters
- Heralded measurements
- Postselection

### Truth Table Verification

The simulated photonic processor produced the expected CNOT behavior:

| Input | Output |
| ----- | ------ |
| 00    | 00     |
| 01    | 01     |
| 10    | 11     |
| 11    | 10     |

### Figures

![Perceval HOM Beam Splitter Circuit Used Before the CNOT Processor](quantam-circuit-simulation-figures/perceval_cnot_gate/displayed_figure_01.png)

*Figure 5. Perceval HOM Beam Splitter Circuit Used Before the CNOT Processor*

![Perceval Postprocessed Photonic CNOT Processor](quantam-circuit-simulation-figures/perceval_cnot_gate/displayed_figure_03.png)

*Figure 6. Perceval Postprocessed Photonic CNOT Processor*

### Importance

The CNOT gate is a universal two-qubit gate and serves as a fundamental building block for quantum algorithms and communication protocols.

---

## Experiment 5 - Boson Sampling

### Objective

Study large-scale multi-photon interference in optical networks.

Boson Sampling is one of the most significant photonic quantum computing models because the resulting output distributions rapidly become difficult to simulate classically.

### Concepts Demonstrated

- Multi-photon interference
- Large optical networks
- Quantum computational complexity

### Result

The experiment generated a complex probability distribution across multiple photonic output states, demonstrating the combinatorial growth of interference effects in optical systems.

![Perceval Mini Boson Sampling Optical Circuit](quantam-circuit-simulation-figures/perceval_mini_boson_sampling/displayed_figure_01.png)

*Figure 7. Perceval Mini Boson Sampling Optical Circuit*

![Perceval Mini Boson Sampling Output Distribution](quantam-circuit-simulation-figures/perceval_mini_boson_sampling/displayed_figure_03.png)

*Figure 8. Perceval Mini Boson Sampling Output Distribution*

![Perceval Mini Boson Sampling Saved Distribution](quantam-circuit-simulation-figures/perceval_mini_boson_sampling/mini_boson_sampling_distribution.png)

*Figure 9. Perceval Mini Boson Sampling Saved Distribution*

---

## Experiment 6 - Large 8-Mode Photonic Interferometer

### Objective

Scale the photonic system beyond simple quantum gates.

The implemented interferometer contains:

- 8 optical modes
- Multiple beam splitter layers
- Multiple phase shifter layers
- 4-photon input states

### Results

The simulation generated:

```text
Number of output states: 183
```

The large number of output states highlights the rapidly increasing complexity of photonic quantum systems.

![Perceval Large 8-Mode Photonic Interferometer Circuit](quantam-circuit-simulation-figures/perceval_large_interferometer/displayed_figure_01.png)

*Figure 10. Perceval Large 8-Mode Photonic Interferometer Circuit*

![Perceval Large Interferometer Output Distribution](quantam-circuit-simulation-figures/perceval_large_interferometer/displayed_figure_03.png)

*Figure 11. Perceval Large Interferometer Output Distribution*

![Perceval Large Interferometer Saved Distribution](quantam-circuit-simulation-figures/perceval_large_interferometer/large_interferometer_distribution.png)

*Figure 12. Perceval Large Interferometer Saved Distribution*

### Significance

This experiment demonstrates how scalable photonic processors evolve from simple beam-splitter networks into architectures related to modern photonic quantum computing platforms.

---

## Experiment 7 - Photonic Quantum Teleportation

### Objective

Implement quantum teleportation using photonic hardware components.

The experiment combines:

- Dual-rail photonic qubits
- Bell states
- Photonic CNOT gates
- Photon detectors
- Feed-forward corrections

### Teleportation Architecture

The processor contains:

- Bell-state generation
- Entanglement distribution
- Photonic CNOT operations
- Measurement stages
- Conditional correction circuits

### Results

The simulation successfully reconstructed Bob's final qubit from Alice's original state through a purely photonic implementation.

The experiment demonstrates the physical realization of quantum teleportation using optical components rather than abstract logical gates.

![Perceval Photonic Quantum Teleportation Processor](quantam-circuit-simulation-figures/perceval_photonic_teleportation/displayed_figure_01.png)

*Figure 13. Perceval Photonic Quantum Teleportation Processor*

![Perceval Photonic Teleportation Bob Qubit Distribution](quantam-circuit-simulation-figures/perceval_photonic_teleportation/displayed_figure_03.png)

*Figure 14. Perceval Photonic Teleportation Bob Qubit Distribution*

![Perceval Photonic Teleportation Saved Bob Distribution](quantam-circuit-simulation-figures/perceval_photonic_teleportation/photonic_teleportation_bob_distribution.png)

*Figure 15. Perceval Photonic Teleportation Saved Bob Distribution*

### Importance

Photonic teleportation represents the culmination of the project, combining all previously introduced concepts:

```text
Entanglement
    ->
Quantum Gates
    ->
Photonic Logic
    ->
Quantum Communication
    ->
Photonic Teleportation
```

---

## Gate-Based vs Photonic Quantum Computing

| Feature             | Qiskit          | Perceval                    |
| ------------------- | --------------- | --------------------------- |
| Information Carrier | Abstract Qubits | Photons                     |
| Single-Qubit Gates  | Native          | Beam splitters              |
| Two-Qubit Gates     | Native          | Heralded optical gates      |
| Teleportation       | Circuit-based   | Physical optical components |
| Focus               | Algorithms      | Hardware realization        |

---

## Future Directions

This work establishes the building blocks required for more advanced photonic quantum computing architectures:

- GHZ state generation
- Quantum key distribution (QKD)
- Bell-state analysis
- Gate teleportation
- KLM optical quantum computing
- Fault-tolerant photonic architectures

---

## Conclusion

This project demonstrates how quantum information can be created, manipulated, transmitted, and physically realized through both gate-based and photonic quantum computing paradigms.

Starting from Bell-state generation and quantum teleportation in Qiskit, the work progressively transitions into photonic implementations using Perceval, including HOM interference, photonic CNOT gates, large interferometric networks, and photonic teleportation.

Together, these experiments illustrate the path from fundamental quantum information protocols to the optical architectures that underpin modern photonic quantum computing research.

---

## Technologies Used

- Python
- Qiskit
- Perceval
- NumPy
- Matplotlib

---

## References

1. IBM Qiskit Documentation
2. Perceval Documentation (Quandela)
3. Bennett et al., Quantum Teleportation (1993)
4. Knill-Laflamme-Milburn (KLM) Optical Quantum Computing
5. Quantum Computing: An Applied Approach
