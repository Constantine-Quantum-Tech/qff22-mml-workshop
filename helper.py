from qiskit import Aer, transpile
def execute(circuit, shots):
    backend = Aer.get_backend("qasm_simulator")
    results = backend.run(transpile(circuit, backend), shots = shots).result()
    return results.get_counts()