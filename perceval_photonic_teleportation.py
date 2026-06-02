import numpy as np
import perceval as pcvl
from perceval import catalog
import matplotlib.pyplot as plt


def squash_results(res, first_mode):
    """
    Keep only a 2-mode dual-rail qubit from a larger output distribution.
    first_mode=4 means keep Bob's qubit modes 4 and 5.
    """
    bsd = pcvl.BSDistribution()
    for state, prob in res.items():
        bsd[state[first_mode:first_mode + 2]] += prob
    return bsd


# ==========================================================
# 1) Alice's qubit to teleport
# ==========================================================
# Choose a simple known state:
# |psi> = (|0> + |1>) / sqrt(2)
# Dual rail:
# |0> = |1,0>
# |1> = |0,1>

to_transmit = (
    pcvl.BasicState([1, 0]) * (1 / np.sqrt(2))
    + pcvl.BasicState([0, 1]) * (1 / np.sqrt(2))
)

print("\nAlice's original qubit to teleport:")
print(to_transmit)


# ==========================================================
# 2) Create Bell state shared between Alice and Bob
# ==========================================================
sg = pcvl.StateGenerator(pcvl.Encoding.DUAL_RAIL)
bell_state = sg.bell_state("phi+")

print("\nShared Bell state between Alice and Bob:")
print(bell_state)


# Full 3-qubit input:
# q0 = Alice's unknown qubit
# q1 = Alice's half of Bell pair
# q2 = Bob's half of Bell pair
input_state = to_transmit * bell_state


# ==========================================================
# 3) Build photonic teleportation processor
# ==========================================================
# 3 dual-rail qubits = 6 optical modes
p = pcvl.Processor("SLOS", 6)

# Alice performs CNOT(q0 -> q1)
p.add(0, catalog["postprocessed cnot"].build_processor())

# Alice applies Hadamard on q0
p.add(0, pcvl.BS.H())


# ==========================================================
# 4) Feed-forward X correction
# ==========================================================
# If Alice's second measured qubit is logical |1>,
# Bob needs an X correction.
# In dual rail, X = swap the two modes.

ff_X = pcvl.FFCircuitProvider(2, 0, pcvl.Circuit(2))
ff_X.add_configuration([0, 1], pcvl.PERM([1, 0]))

# Detectors for Alice's second qubit modes 2 and 3
p.add(2, pcvl.Detector.pnr())
p.add(3, pcvl.Detector.pnr())

# Apply X correction on Bob depending on measurement
p.add(2, ff_X)


# ==========================================================
# 5) Feed-forward Z correction
# ==========================================================
# If Alice's first measured qubit is logical |1>,
# Bob needs a Z correction.
# In dual rail, Z = phase shift pi on the |1> mode.

phi = pcvl.P("phi")
ff_Z = pcvl.FFConfigurator(
    2,
    3,
    pcvl.PS(phi),
    {"phi": 0}
).add_configuration([0, 1], {"phi": np.pi})

# Detectors for Alice's first qubit modes 0 and 1
p.add(0, pcvl.Detector.pnr())
p.add(1, pcvl.Detector.pnr())

# Apply Z correction on Bob depending on measurement
p.add(0, ff_Z)


# ==========================================================
# 6) Run simulation
# ==========================================================
p.min_detected_photons_filter(3)

# The postprocessed CNOT introduces 2 herald modes.
# Since we are using a StateVector input, we append empty herald modes.
input_state *= pcvl.BasicState([0, 0])

p.with_input(input_state)

res = p.probs()

print("\nFull teleportation output:")
print(res)

bob_distribution = squash_results(res["results"], 4)

print("\nBob's final qubit distribution after teleportation:")
for state, prob in bob_distribution.items():
    print(f"{state}: {float(prob):.4f}")

print("\nGlobal success probability:")
print(res.get("global_perf", "N/A"))


# ==========================================================
# 7) Save photonic teleportation circuit figure
# ==========================================================
print("\nPhotonic teleportation processor:")
pcvl.pdisplay(p, output_format=pcvl.Format.MPLOT, recursive=True)
plt.savefig("photonic_teleportation_processor.png", dpi=300, bbox_inches="tight")
plt.show()


# ==========================================================
# 8) Save Bob's output distribution
# ==========================================================
states = [str(s) for s in bob_distribution.keys()]
probs = [float(p) for p in bob_distribution.values()]

plt.figure(figsize=(6, 4))
plt.bar(states, probs)
plt.title("Bob's Final Qubit After Photonic Teleportation")
plt.xlabel("Bob dual-rail state")
plt.ylabel("Probability")
plt.ylim(0, 1.05)
plt.tight_layout()
plt.savefig("photonic_teleportation_bob_distribution.png", dpi=300)
plt.show()
