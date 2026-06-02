import perceval as pcvl
import matplotlib.pyplot as plt
import math


def save_top_distribution_plot(distribution, filename, top_k=15):
    items = sorted(
        [(str(state), float(prob)) for state, prob in distribution.items()],
        key=lambda x: x[1],
        reverse=True
    )[:top_k]

    states = [x[0] for x in items]
    probs = [x[1] for x in items]

    plt.figure(figsize=(12, 5))
    plt.bar(states, probs)
    plt.title("Large Interferometer Output Distribution")
    plt.xlabel("Output photon state")
    plt.ylabel("Probability")
    plt.xticks(rotation=35, ha="right")
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.show()


# ==========================================================
# Large 8-mode, 4-photon linear optical interferometer
# ==========================================================

circuit = pcvl.Circuit(8)

# Layer 1: pairwise beam splitters
circuit.add(0, pcvl.BS())
circuit.add(2, pcvl.BS())
circuit.add(4, pcvl.BS())
circuit.add(6, pcvl.BS())

# Layer 2: phase shifters
for mode, phase in enumerate([
    math.pi / 5,
    math.pi / 7,
    math.pi / 3,
    math.pi / 4,
    math.pi / 6,
    math.pi / 8,
    math.pi / 9,
    math.pi / 11
]):
    circuit.add(mode, pcvl.PS(phase))

# Layer 3: shifted beam splitters
circuit.add(1, pcvl.BS())
circuit.add(3, pcvl.BS())
circuit.add(5, pcvl.BS())

# Layer 4: more phase shifters
for mode, phase in enumerate([
    math.pi / 13,
    math.pi / 10,
    math.pi / 12,
    math.pi / 14,
    math.pi / 15,
    math.pi / 16,
    math.pi / 17,
    math.pi / 18
]):
    circuit.add(mode, pcvl.PS(phase))

# Layer 5: another pairwise mixing layer
circuit.add(0, pcvl.BS())
circuit.add(2, pcvl.BS())
circuit.add(4, pcvl.BS())
circuit.add(6, pcvl.BS())

# Layer 6: shifted mixing again
circuit.add(1, pcvl.BS())
circuit.add(3, pcvl.BS())
circuit.add(5, pcvl.BS())

# Input: 4 photons across 8 modes
input_state = pcvl.BasicState([1, 1, 1, 1, 0, 0, 0, 0])

backend = pcvl.BackendFactory().get_backend("SLOS")
backend.set_circuit(circuit)
backend.set_input_state(input_state)

distribution = backend.prob_distribution()

print("Large 8-mode Photonic Interferometer:")
pcvl.pdisplay(circuit, output_format=pcvl.Format.MPLOT)
plt.savefig("large_interferometer_circuit.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nInput State:")
print(input_state)

print("\nNumber of output states:")
print(len(distribution))

print("\nTop Output States:")
for state, prob in sorted(distribution.items(), key=lambda x: float(x[1]), reverse=True)[:15]:
    print(f"{state}: {float(prob):.4f}")

save_top_distribution_plot(
    distribution,
    "large_interferometer_distribution.png",
    top_k=15
)
