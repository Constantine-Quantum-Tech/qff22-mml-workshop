from qiskit import Aer, transpile
from qiskit.visualization import plot_bloch_multivector

def execute(circuit, shots):
    backend = Aer.get_backend("qasm_simulator")
    results = backend.run(transpile(circuit, backend), shots = shots).result()
    return results.get_counts()

def visualize_the_system(circuit):
    backend = Aer.get_backend("statevector_simulator")
    results = backend.run(transpile(circuit, backend)).result()
    display(plot_bloch_multivector(results.get_statevector()))