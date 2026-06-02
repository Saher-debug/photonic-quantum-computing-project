import perceval as pcvl
import matplotlib.pyplot as plt
import math


def save_top_distribution_plot(distribution, filename, top_k=10):
    items = sorted(
        [(str(state), float(prob)) for state, prob in distribution.items()],
        key=lambda x: x[1],
        reverse=True
    )[:top_k]

    states = [x[0] for x in items]
    probs = [x[1] for x in items]

    plt.figure(figsize=(10, 5))
    plt.bar(states, probs)
    plt.title("Mini Boson-Sampling Output Distribution")
    plt.xlabel("Output photon state")
    plt.ylabel("Probability")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


# 6 optical modes
circuit = pcvl.Circuit(6)

# Layer 1: pairwise beam splitters
circuit.add(0, pcvl.BS())
circuit.add(2, pcvl.BS())
circuit.add(4, pcvl.BS())

# Layer 2: phase shifts
circuit.add(0, pcvl.PS(math.pi / 5))
circuit.add(1, pcvl.PS(math.pi / 7))
circuit.add(2, pcvl.PS(math.pi / 3))
circuit.add(3, pcvl.PS(math.pi / 4))
circuit.add(4, pcvl.PS(math.pi / 6))
circuit.add(5, pcvl.PS(math.pi / 8))

# Layer 3: shifted beam splitters
circuit.add(1, pcvl.BS())
circuit.add(3, pcvl.BS())

# Layer 4: more mixing
circuit.add(0, pcvl.BS())
circuit.add(2, pcvl.BS())
circuit.add(4, pcvl.BS())

# Input: 3 photons distributed across 6 modes
input_state = pcvl.BasicState([1, 1, 1, 0, 0, 0])

backend = pcvl.BackendFactory().get_backend("SLOS")
backend.set_circuit(circuit)
backend.set_input_state(input_state)

distribution = backend.prob_distribution()

print("Mini Boson-Sampling Circuit:")
pcvl.pdisplay(circuit, output_format=pcvl.Format.MPLOT)
plt.savefig("mini_boson_sampling_circuit.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nInput State:")
print(input_state)

print("\nTop Output States:")
for state, prob in sorted(distribution.items(), key=lambda x: float(x[1]), reverse=True)[:10]:
    print(f"{state}: {float(prob):.4f}")

save_top_distribution_plot(
    distribution,
    "mini_boson_sampling_distribution.png",
    top_k=10
)
