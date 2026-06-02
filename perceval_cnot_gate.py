import perceval as pcvl
import matplotlib.pyplot as plt

# ---------- HOM circuit ----------
hom_circuit = pcvl.Circuit(2)
hom_circuit.add(0, pcvl.BS())

pcvl.pdisplay(hom_circuit, output_format=pcvl.Format.MPLOT)
plt.savefig("hom_optical_circuit.png", dpi=300, bbox_inches="tight")
plt.show()

# ---------- CNOT processor ----------
cnot_processor = pcvl.catalog["postprocessed cnot"].build_processor()

pcvl.pdisplay(
    cnot_processor,
    output_format=pcvl.Format.MPLOT,
    recursive=True
)
plt.savefig("cnot_photonic_processor.png", dpi=300, bbox_inches="tight")
plt.show()