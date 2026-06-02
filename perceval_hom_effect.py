import perceval as pcvl

# Create a 2-mode photonic circuit
circuit = pcvl.Circuit(2)
circuit.add(0, pcvl.BS())

# Input state: one photon in each mode
input_state = pcvl.BasicState([1, 1])

# Use SLOS backend
backend = pcvl.BackendFactory().get_backend("SLOS")

# Set circuit and input state first
backend.set_circuit(circuit)
backend.set_input_state(input_state)

# Now compute probability distribution with NO arguments
output_distribution = backend.prob_distribution()

print("Perceval Photonic Circuit:")
print(circuit)

print("\nInput State:")
print(input_state)

print("\nOutput Probability Distribution:")
for state, prob in output_distribution.items():
    print(f"{state}: {prob:.4f}")
