# 🔐A-Variational-Quantum-Circuit-Based-Sponge-Hash-Method-for-Image-Data
 

📖 OVERVIEW

Quantum Sponge Hash (Proposed QSH) is a novel quantum-enhanced hash function for image data. It combines:

*   -Sponge-Inspired Construction: Absorbs image data block by block.
*   -VQC Mixing Map: 8-qubit Variational Quantum Circuit as a nonlinear transformation.
*   -Image Preprocessing: 32×32 grayscale → 8192 bits.
*   -128-bit Digest: Secure output for image authentication.

Key Innovation: First VQC-based sponge-inspired hash specifically designed for image data, achieving near-ideal diffusion (48.9% avalanche effect).


👤 AUTHOR

- Name: Aya Rafii
- Supervisor: Prof. Zhang Yong
- Affiliation: School of Computing and Artificial Intelligence, Jiangxi University of Finance and Economics (JUFE)
- Thesis: Robust Image Hash Code Generation Algorithm Based on Quantum Machine Learning
- Date: August 2026


🚀 FEATURES

- Quantum Hash Generation: 8 qubits, 6 layers, RY/RZ rotations + CNOT entanglement
- Dual-View Absorption: Processes the state and a 97-bit right-rotated view to update both rate and capacity
- Image Preprocessing: Auto resize to 32x32, grayscale conversion, bit extraction
- Avalanche Effect Test: Test hash sensitivity to 1-pixel changes
- SHA-3 Baseline: Compare against classical SHA-3
- Hash Visualization: 8x16 bitmap grid
- Interactive Web App: Streamlit interface
- Cross-Platform: Works on Windows, Linux, macOS


📊 HOW IT WORKS

Step 1: IMAGE INPUT
- Upload any image (any size, any format)

Step 2: PREPROCESSING
- Convert to grayscale
- Resize to 32x32 pixels
- Flatten to 1024 pixel values
- Convert each pixel (0-255) to 8 bits
- Result: 8192 bits (64 blocks of 128 bits)

Step 3: DUAL-VIEW SPONGE ABSORB
 Initialize state \(S = R \parallel C\) (256 bits).
*   For each of the 64 blocks:
    1.  XOR the 128-bit block into the rate (R).
    2.  Compute readout \(a\) from the unrotated intermediate state (T).
    3.  Compute readout \(d\) from the **97-bit right-rotated** view of T.
    4.  Update state: \(S_{new} = T \oplus (a \parallel d)\).

Step 4: SQUEEZE
- Extract first 128 bits of state

Step 5: HASH OUTPUT
- Hex: 32 characters
- Binary: 128 bits


🛠️ INSTALLATION

1. Install Dependencies:
   pip install -r requirements.txt

2. Run the Application:
   streamlit run qsh_app.py

3. Open in Browser:
   The app will open at: http://localhost:8501


📁 PROJECT STRUCTURE

Quantum-Sponge-Hash/

├── qsh_app.py              # Main Streamlit application

├── requirements.txt        # Python dependencies

├── LICENSE                 # License information

└── Image Test Data/        # Sample images for testing


🖥️ USAGE GUIDE

Step 1: Upload an Image
- Click "Choose an image" in the sidebar
- Supported formats: PNG, JPG, JPEG, BMP, TIFF, WEBP

Step 2: Generate Hash
- Select hash method: Quantum Sponge Hash (QSH) or SHA-3 Baseline
- Click "Generate Hash"
- View results:
  - Hex hash (32 characters)
  - Binary hash (128 bits)
  - Hash bitmap (8x16 grid)
  - Processing time

Step 3: Test Avalanche Effect (Optional)
- Enable "Avalanche Test" in sidebar
- Select pixel to flip (0-1023)
- Click "Run Avalanche Test"
- View results:
  - Hamming Distance
  - Avalanche Effect (%)
  - Hash comparison (original vs modified)
  - Bit changes visualization (red = changed)


📊 EXPECTED RESULTS

Metric                   | QSH (Ours) | SHA-3    | Target
----------------------  -|------------ |---------|--------
Avalanche Effect         | ~48.9%      | ~50.2%   | 50%
Collision Rate           | 0%          | 0%       | 0%
Hamming Distance         | ~62.6       | ~64.2    | 64
Time per Image           | ~248ms      | ~0.01ms  | -

Sample Uniqueness	:  200 distinct / 200 images 
(Note: Results are based on a 200-image CIFAR-10 sample in noiseless simulation.)



🔬 TECHNICAL DETAILS

VQC Circuit Configuration:
- Number of qubits: 8
- Number of layers: 6
- Encoding: Angle encoding (RY gates)
- Variational gates: RY, RZ
- Entangling gates: CNOT (linear + cyclic)
- Measurement: Pauli-Z
- Measurements per hash: 8 x 16 = 128 bits

Sponge Configuration:
- State size: 256 bits
- Rate (R): 128 bits
- Capacity (C): 128 bits
- Input bits: 8192 bits (1024 pixels x 8)
- Blocks:  64 blocks of 128 bits
- Second View: 97-bit right rotation

Security Properties:
- Diffusion: 1-pixel change → ~48.9% hash bits change.
- Input Coverage: Every canonical image bit is absorbed.
- Collision Resistance: Zero collisions on 10,000 image pairs
- Quantum Resistance: Designed to resist Grover's algorithm
- Scope: Evaluation is based on empirical diffusion in noiseless simulation, not a proof of cryptographic security.


⚠️ WINDOWS USERS

If you get a DLL import error (ImportError: DLL load failed while importing _ufuncs_cxx), please:

1. Install Microsoft Visual C++ Redistributable:
   https://aka.ms/vs/17/release/vc_redist.x64.exe

2. Use Python 3.10 or 3.11 (PennyLane does not yet fully support Python 3.14)

3. Or use Conda instead of pip:
   conda create -n qsh_env python=3.11
   conda activate qsh_env
   conda install pennylane streamlit torch pillow matplotlib numpy


📝 CITATION

If you use this work in your research, please cite:

@mastersthesispaper{rafii2026qsh,
  author = {Rafii, Aya},
  title = {Robust Image Hash Code Generation Algorithm Based on Quantum Machine Learning},
  school = {Jiangxi University of Finance and Economics},
  year = {2026},
  supervisor = {Zhang, Yong}
}


📧 CONTACT

- Email: aya0rafii@gmail.com
- Supervisor: Prof. Zhang Yong
- University: Jiangxi University of Finance and Economics


🙏 ACKNOWLEDGMENTS

- Prof. Zhang Yong for supervision and guidance
- PennyLane team for quantum computing framework
- Streamlit team for web application framework


📄 LICENSE

All rights reserved. This code is part of original research and should not be copied or replicated without permission.


🔐 Quantum Sponge Hash v2.0 | Original Work © 2026 Aya Rafii · JUFE
