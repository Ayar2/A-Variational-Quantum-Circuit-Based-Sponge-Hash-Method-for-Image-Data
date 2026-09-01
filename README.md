# 🔐A-Variational-Quantum-Circuit-Based-Sponge-Hash-Method-for-Image-Data
 

📖 OVERVIEW

Quantum Sponge Hash (QSH) is a novel quantum-enhanced hash function for image data. It combines:

- Sponge Construction: Absorbs image data block by block
- VQC Permutation: 8-qubit Variational Quantum Circuit as nonlinear transformation
- Image Preprocessing: 32x32 grayscale → 8192 bits
- 128-bit Hash: Secure output for image authentication

Key Innovation: First VQC-based sponge hash specifically designed for image data.


👤 AUTHOR

- Name: Aya Rafii
- Supervisor: Prof. Zhang Yong
- Affiliation: School of Computing and Artificial Intelligence, Jiangxi University of Finance and Economics (JUFE)
- Thesis: Robust Image Hash Code Generation Algorithm Based on Quantum Machine Learning
- Date: August 2026


🚀 FEATURES

- Quantum Hash Generation: 8 qubits, 6 layers, RY/RZ rotations + CNOT entanglement
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
- Result: 8192 bits (16 blocks of 512 bits)

Step 3: SPONGE ABSORB
- For each of the 16 blocks:
  - XOR block into state (256 bits)
  - Encode state to 8 angles
  - Apply VQC (8 qubits, 6 layers)
  - Convert measurements to bits
  - Update state

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
├── README.md               # This file
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

Metric                 | QSH (Ours) | SHA-3    | Target
-----------------------|------------|-------   |--------
Avalanche Effect       | ~49.5%     | ~50.0%   | 50%
Collision Rate         | 0%         | 0%       | 0%
Hamming Distance       | ~64        | ~64      | 64
Time per Image         | ~70ms      | ~0.001ms | -


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
- Blocks: 16 blocks of 512 bits

Security Properties:
- Avalanche Effect: 1-pixel change → ~50% hash bits change
- Collision Resistance: Zero collisions on 10,000 image pairs
- Quantum Resistance: Designed to resist Grover's algorithm


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

@mastersthesis{rafii2026qsh,
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


🔐 Quantum Sponge Hash v1.0 | Original Work © 2026 Aya Rafii · JUFE