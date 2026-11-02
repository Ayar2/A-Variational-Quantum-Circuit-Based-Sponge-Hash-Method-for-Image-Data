# ======================================================================
# QUANTUM SPONGE HASH (QSH) – FULL WORKING CODE
# ======================================================================
# Title: Quantum Sponge Hash: A VQC-Based Hash Function for Image Data
# Author: Aya Rafii
# Supervisor: Prof. Zhang Yong
# Affiliation: School of Computing and AI, JUFE
# Date: August 2026
# ======================================================================

import streamlit as st
import numpy as np
import pennylane as qml
import torch
from PIL import Image
import hashlib
import time
import matplotlib.pyplot as plt

# ======================================================================
# 1. PAGE CONFIGURATION
# ======================================================================

st.set_page_config(
    page_title="Quantum Sponge Hash - Aya Rafii",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ======================================================================
# 2. CSS – ENHANCED SIDEBAR + CLEAN MAIN PAGE
# ======================================================================

st.markdown("""
<style>
    /* ===== SIDEBAR ===== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
        border-right: 1px solid rgba(255,255,255,0.05);
    }
    
    section[data-testid="stSidebar"] .st-emotion-cache-1wivap2 {
        color: #ffffff !important;
    }
    
    section[data-testid="stSidebar"] .st-emotion-cache-10trblm {
        color: #a8b5ff !important;
        font-weight: 600;
        font-size: 1.1rem;
        border-bottom: 2px solid rgba(102, 126, 234, 0.3);
        padding-bottom: 0.5rem;
        margin-bottom: 0.5rem;
    }
    
    section[data-testid="stSidebar"] .st-emotion-cache-1r6slb0 {
        color: #c8d0ff !important;
    }
    
    section[data-testid="stSidebar"] .st-emotion-cache-1avcm0n {
        color: #8899bb !important;
        font-size: 0.85rem;
    }
    
    section[data-testid="stSidebar"] hr {
        border-color: rgba(255,255,255,0.08);
    }
    
    section[data-testid="stSidebar"] label {
        color: #c8d0ff !important;
    }
    
    section[data-testid="stSidebar"] .stFileUploader > div {
        border: 2px dashed #667eea !important;
        border-radius: 14px !important;
        background: rgba(102, 126, 234, 0.04) !important;
        padding: 1.5rem !important;
    }
    
    section[data-testid="stSidebar"] .stFileUploader > div:hover {
        border-color: #764ba2 !important;
        background: rgba(118, 75, 162, 0.06) !important;
    }
    
    /* ===== MAIN PAGE BUTTONS ===== */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.35) !important;
        font-size: 1rem !important;
        letter-spacing: 0.3px !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5) !important;
    }
    
    .stButton > button[data-testid="baseButton-secondary"] {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%) !important;
        box-shadow: 0 4px 15px rgba(245, 87, 108, 0.35) !important;
    }
    
    .stButton > button[data-testid="baseButton-secondary"]:hover {
        box-shadow: 0 8px 25px rgba(245, 87, 108, 0.5) !important;
    }
    
    /* ===== MAIN PAGE TITLE ===== */
    .main-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #1a1a2e;
        text-align: center;
        padding: 1.5rem 0 0.5rem 0;
        font-family: 'Segoe UI', 'Helvetica Neue', sans-serif;
        letter-spacing: -0.5px;
    }
    
    .sub-title {
        font-size: 1.1rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 300;
        font-family: 'Segoe UI', sans-serif;
        letter-spacing: 1px;
    }
    
    /* ===== MAIN PAGE METRICS ===== */
    .stMetric {
        background: rgba(255,255,255,0.8) !important;
        padding: 0.8rem 1.2rem !important;
        border-radius: 12px !important;
        box-shadow: 0 2px 10px rgba(0,0,0,0.04) !important;
    }
    
    .stMetric .stMetricLabel {
        color: #555 !important;
        font-weight: 500 !important;
    }
    
    .stMetric .stMetricValue {
        color: #1a1a2e !important;
        font-weight: 700 !important;
    }
    
    /* ===== MAIN PAGE EXPANDER ===== */
    .streamlit-expanderHeader {
        background: rgba(102, 126, 234, 0.06) !important;
        border-radius: 10px !important;
        font-weight: 500 !important;
        color: #333 !important;
    }
    
    .streamlit-expanderHeader:hover {
        background: rgba(102, 126, 234, 0.12) !important;
    }
    
    /* ===== MAIN PAGE IMAGE ===== */
    .stImage img {
        border-radius: 14px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08) !important;
    }
    
    /* ===== MAIN PAGE PROGRESS BAR ===== */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea, #764ba2) !important;
        border-radius: 10px !important;
    }
    
    /* ===== MAIN PAGE ALERTS ===== */
    .stAlert {
        border-radius: 12px !important;
    }
    
    .stAlert[data-testid="stSuccess"] {
        border-left: 5px solid #2e7d32 !important;
    }
    
    .stAlert[data-testid="stInfo"] {
        border-left: 5px solid #1565c0 !important;
    }
    
    /* ===== FOOTER ===== */
    .footer {
        text-align: center;
        padding: 2rem 0 1rem 0;
        color: #8888aa;
        font-size: 0.85rem;
        border-top: 1px solid rgba(0,0,0,0.06);
        margin-top: 2rem;
        font-weight: 300;
        letter-spacing: 0.5px;
    }
    
    .footer span {
        color: #667eea;
        font-weight: 600;
    }
    
    hr {
        margin: 1.5rem 0 !important;
        border-color: rgba(0,0,0,0.06) !important;
    }
</style>
""", unsafe_allow_html=True)

# ======================================================================
# 3. QUANTUM SPONGE HASH CLASS
# ======================================================================

class QuantumSpongeHash:
    """
    Proposed QSH - Singleton Pattern.
    Absorbs 64 complete 128-bit blocks and updates both state halves
    using two fixed-parameter VQC readouts per block.
    """
    
    _instance = None
    _params = None
    _qnode = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(QuantumSpongeHash, cls).__new__(cls)
        return cls._instance
    
    def __init__(self, n_qubits=8, n_layers=6, seed=42):
        if hasattr(self, '_initialized'):
            if (n_qubits, n_layers, seed) != (self.n_qubits, self.n_layers, self.seed):
                raise ValueError("The singleton already uses a different circuit configuration.")
            return

        if n_qubits != 8:
            raise ValueError("Proposed QSH requires exactly 8 qubits for its 256-bit encoding.")
        if not isinstance(n_layers, (int, np.integer)) or n_layers < 1:
            raise ValueError("n_layers must be a positive integer.")

        self.n_qubits = n_qubits
        self.n_layers = n_layers
        self.seed = seed
        self.hash_bits = 128
        self.rate = 128
        self.capacity = 128
        self.state_size = 256
        self.image_size_bits = 8192
        self.num_blocks = 64
        self.rotation_bits = 97
        
        # Legacy NumPy generator reproduces seed=42 parameter values without
        # changing the application's global random state.
        rng = np.random.RandomState(seed)
        
        # Initialize parameters once (singleton)
        if QuantumSpongeHash._params is None:
            scale = np.sqrt(2.0 / (self.n_qubits * self.n_layers))
            QuantumSpongeHash._params = rng.randn(self.n_layers, self.n_qubits, 2) * scale
        
        self.params = QuantumSpongeHash._params
        # Reuse one float64 tensor throughout all 128 evaluations per hash.
        # No optimization or gradient tracking is needed for this fixed map.
        self._params_tensor = torch.tensor(self.params, dtype=torch.float64)
        
        # Create quantum device
        self.dev = qml.device('default.qubit', wires=n_qubits, shots=None)
        
        # Build quantum circuit
        @qml.qnode(self.dev, interface='torch', diff_method=None)
        def circuit(inputs, params):
            # Encoding layer: RY gates
            for i in range(self.n_qubits):
                qml.RY(inputs[i], wires=i)
            
            # Variational layers: RY + RZ + CNOT
            for layer in range(self.n_layers):
                for i in range(self.n_qubits):
                    qml.RY(params[layer][i][0], wires=i)
                    qml.RZ(params[layer][i][1], wires=i)
                for i in range(self.n_qubits - 1):
                    qml.CNOT(wires=[i, i + 1])
                qml.CNOT(wires=[self.n_qubits - 1, 0])
            
            # Measurement: Pauli-Z
            return [qml.expval(qml.PauliZ(i)) for i in range(self.n_qubits)]
        
        self.qnode = circuit
        self._initialized = True
    
    def _encode_state_to_inputs(self, state_bits):
        """
        Encode 256-bit state to 8 angles for VQC input
        """
        if len(state_bits) != self.state_size:
            raise ValueError("State encoding requires exactly 256 bits.")
        chunks = [state_bits[i:i+32] for i in range(0, 256, 32)]
        angles = []
        for chunk in chunks:
            value = 0
            for bit in chunk:
                value = (value << 1) | int(bit)
            angle = np.pi * (value / (2**32 - 1))
            angles.append(angle)
        return angles
    
    def _measurements_to_bits(self, measurements):
        """
        Convert 8 measurement values (-1 to 1) to 128 bits
        Each measurement → 16 bits
        """
        bits = []
        for m in measurements:
            if isinstance(m, torch.Tensor):
                m = float(m.detach().cpu().item())
            else:
                m = float(m)
            if not np.isfinite(m):
                raise ValueError("The circuit returned a non-finite expectation value.")
            # Clamp to [-1, 1]
            m_clamped = max(-1.0, min(1.0, m))
            # Map to [0, 65535]
            value = int(((m_clamped + 1.0) / 2.0) * 65535)
            # Convert to 16-bit binary
            binary = format(value, '016b')
            bits.extend([int(b) for b in binary])
        return bits
    
    def _xor_state_with_block(self, state, block):
        """
        XOR one complete 128-bit message block into the rate only.
        """
        if len(state) != self.state_size or len(block) != self.rate:
            raise ValueError("Absorption requires a 256-bit state and a 128-bit block.")
        rate = state[:self.rate]
        capacity = state[self.rate:]
        new_rate = [int(rate[i]) ^ int(block[i]) for i in range(self.rate)]
        return new_rate + capacity

    def _rotate_state(self, state_bits):
        """Return a new 256-bit list rotated RIGHT by 97 bit positions.

        output[j] = state_bits[(j - 97) % 256].
        This is a circular bit rotation, not a zero-filled shift.
        """
        if len(state_bits) != self.state_size:
            raise ValueError("State rotation requires exactly 256 bits.")
        return np.roll(np.asarray(state_bits, dtype=np.uint8), self.rotation_bits).tolist()

    def _quantum_readout(self, state_bits):
        """Q(T): encode, evaluate the fixed VQC, and quantize to 128 bits."""
        inputs = self._encode_state_to_inputs(state_bits)
        with torch.no_grad():
            measurements = self.qnode(
                torch.tensor(inputs, dtype=torch.float64),
                self._params_tensor
            )
        return self._measurements_to_bits(measurements)
    
    def _bits_to_hex(self, bits):
        """
        Convert 128 bits to hex string
        """
        if len(bits) > 128:
            bits = bits[:128]
        elif len(bits) < 128:
            bits = bits + [0] * (128 - len(bits))
        
        byte_array = bytearray()
        for i in range(0, 128, 8):
            byte = 0
            for j in range(8):
                byte = (byte << 1) | bits[i + j]
            byte_array.append(byte)
        return byte_array.hex()
    
    def hash_image(self, image_bits):
        """
        Generate the Proposed QSH digest for an 8192-bit canonical image.

        For each of 64 blocks: T = S XOR (m || 0^128), a = Q(T),
        d = Q(rotate_right_97(T)), then S = T XOR (a || d).
        Both readouts use the SAME pre-feedback T. Return the final rate.
        """
        start_time = time.perf_counter()

        image_array = np.asarray(image_bits)
        if image_array.ndim != 1 or image_array.size != self.image_size_bits:
            raise ValueError("hash_image requires exactly 8192 bits (32x32 grayscale pixels).")
        if not np.all((image_array == 0) | (image_array == 1)):
            raise ValueError("image_bits must contain only binary values 0 or 1.")
        image_bits = image_array.astype(np.uint8).tolist()

        state = [0] * self.state_size
        
        # Absorb every image bit exactly once, in 64 rate-sized blocks.
        for b in range(64):
            block = image_bits[b * self.rate:(b + 1) * self.rate]
            intermediate_state = self._xor_state_with_block(state, block)

            # Compute BOTH views before updating either the rate or capacity.
            a = self._quantum_readout(intermediate_state)
            rotated_T = self._rotate_state(intermediate_state)
            d = self._quantum_readout(rotated_T)

            # S_new = T XOR (a || d): additive feedback to both state halves.
            feedback = a + d
            state = [t ^ f for t, f in zip(intermediate_state, feedback)]
        
        # Squeeze phase
        hash_bits = state[:self.hash_bits]
        hash_hex = self._bits_to_hex(hash_bits)
        hash_binary = ''.join(map(str, hash_bits))
        
        elapsed_time = time.perf_counter() - start_time
        
        return {
            'hex': hash_hex,
            'binary': hash_binary,
            'bits': hash_bits,
            'time': elapsed_time
        }
    
    def avalanche_test(self, image_bits, pixel_index=0):
        """
        Test avalanche effect by flipping one pixel (8 bits)
        """
        # Ensure pixel_index is within bounds
        max_pixel = (len(image_bits) // 8) - 1
        if pixel_index > max_pixel:
            pixel_index = max_pixel
        if pixel_index < 0:
            pixel_index = 0
        
        # Generate original hash
        original = self.hash_image(image_bits)
        
        # Make a copy and flip the selected pixel
        modified_bits = image_bits.copy()
        start_bit = pixel_index * 8
        
        # Flip all 8 bits of the selected pixel
        for i in range(8):
            idx = start_bit + i
            if idx < len(modified_bits):
                modified_bits[idx] = 1 - modified_bits[idx]
        
        # Generate modified hash
        modified = self.hash_image(modified_bits)
        
        # Calculate Hamming distance
        hamming_dist = 0
        for a, b in zip(original['bits'], modified['bits']):
            if a != b:
                hamming_dist += 1
        
        avalanche_percentage = (hamming_dist / self.hash_bits) * 100
        
        # Debug output (visible in terminal)
        print(f"Pixel index: {pixel_index}")
        print(f"Start bit: {start_bit}")
        print(f"Hamming Distance: {hamming_dist}")
        print(f"Avalanche Effect: {avalanche_percentage:.1f}%")
        
        return {
            'original_hash': original,
            'modified_hash': modified,
            'hamming_distance': hamming_dist,
            'avalanche_percentage': avalanche_percentage
        }


# ======================================================================
# 4. IMAGE PREPROCESSOR
# ======================================================================

class ImagePreprocessor:
    """
    Image preprocessing pipeline for QSH
    Converts any image to 8192 bits (32×32 grayscale)
    """
    
    @staticmethod
    def preprocess(image, target_size=(32, 32)):
        metadata = {}
        
        # Convert to grayscale
        if image.mode == 'RGB':
            img_gray = image.convert('L')
        elif image.mode == 'RGBA':
            img_rgb = image.convert('RGB')
            img_gray = img_rgb.convert('L')
        else:
            img_gray = image.convert('L')
        
        metadata['original_mode'] = image.mode
        
        # Resize to target size
        img_resized = img_gray.resize(target_size, Image.Resampling.LANCZOS)
        metadata['resized_size'] = target_size
        
        # Flatten pixels
        pixels = np.array(img_resized, dtype=np.uint8).flatten()
        metadata['num_pixels'] = len(pixels)
        metadata['pixel_stats'] = {
            'min': int(pixels.min()),
            'max': int(pixels.max()),
            'mean': float(pixels.mean()),
            'std': float(pixels.std())
        }
        
        # Convert each pixel (0-255) to 8 bits
        bits = []
        for p in pixels:
            binary = format(int(p), '08b')
            bits.extend([int(b) for b in binary])
        
        metadata['total_bits'] = len(bits)
        metadata['blocks_128'] = len(bits) // 128
        
        return bits, metadata
    
    @staticmethod
    def preprocess_from_upload(uploaded_file):
        image = Image.open(uploaded_file)
        bits, metadata = ImagePreprocessor.preprocess(image)
        return image, bits, metadata


# ======================================================================
# 5. SHA-3 BASELINE
# ======================================================================

def sha3_baseline(image_bits):
    """
    SHA-3 baseline for comparison
    """
    start_time = time.time()
    
    # Convert bits to bytes
    byte_array = bytearray()
    for i in range(0, len(image_bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(image_bits):
                byte = (byte << 1) | image_bits[i + j]
            else:
                byte = byte << 1
        byte_array.append(byte)
    
    # Compute SHA-3 (256-bit)
    sha3_bytes = hashlib.sha3_256(bytes(byte_array)).digest()
    
    # Take first 128 bits (16 bytes) for fair comparison
    hash_bytes = sha3_bytes[:16]
    hash_hex = hash_bytes.hex()
    hash_binary = ''.join(format(b, '08b') for b in hash_bytes)
    
    elapsed_time = time.time() - start_time
    
    return {
        'hex': hash_hex,
        'binary': hash_binary[:128],
        'time': elapsed_time
    }


# ======================================================================
# 6. QUANTUM CIRCUIT VISUALIZATION
# ======================================================================

def draw_quantum_circuit():
    return """
    QUANTUM SPONGE HASH – VQC Circuit Diagram
    
    Input: 8 angles (θ₀, θ₁, ..., θ₇)
    Parameters: 6 layers × 8 qubits × 2 angles
    Per block: evaluate this same circuit on T and on rotate_right_97(T).
    Full hash: 64 blocks, 128 circuit evaluations, 256-bit state feedback.
    
    Legend:
        RY(α) = Y-rotation by angle α
        RZ(β) = Z-rotation by angle β
        CNOT  = Controlled-NOT gate
        M     = Pauli-Z measurement
    
    ┌─────────────────────────────────────────────────────────────────────┐
    │                        ENCODING LAYER                              │
    ├─────────────────────────────────────────────────────────────────────┤
    │                                                                     │
    │ q0: ─── RY(θ₀) ────────────────────────────────────────────────     │
    │ q1: ─── RY(θ₁) ────────────────────────────────────────────────     │
    │ q2: ─── RY(θ₂) ────────────────────────────────────────────────     │
    │ q3: ─── RY(θ₃) ────────────────────────────────────────────────     │
    │ q4: ─── RY(θ₄) ────────────────────────────────────────────────     │
    │ q5: ─── RY(θ₅) ────────────────────────────────────────────────     │
    │ q6: ─── RY(θ₆) ────────────────────────────────────────────────     │
    │ q7: ─── RY(θ₇) ────────────────────────────────────────────────     │
    │                                                                     │
    ├─────────────────────────────────────────────────────────────────────┤
    │                    REPEAT FOR 6 LAYERS                              │
    ├─────────────────────────────────────────────────────────────────────┤
    │                                                                     │
    │     ┌─────────────────────────────────────────────────────────┐     │
    │     │              VARIATIONAL LAYER (Layer L)               │     │
    │     ├─────────────────────────────────────────────────────────┤     │
    │     │                                                         │     │
    │     │  q0: ── RY(α₀) ── RZ(β₀) ── CNOT ──                   │     │
    │     │  q1: ── RY(α₁) ── RZ(β₁) ── CNOT ──                   │     │
    │     │  q2: ── RY(α₂) ── RZ(β₂) ── CNOT ──                   │     │
    │     │  q3: ── RY(α₃) ── RZ(β₃) ── CNOT ──                   │     │
    │     │  q4: ── RY(α₄) ── RZ(β₄) ── CNOT ──                   │     │
    │     │  q5: ── RY(α₅) ── RZ(β₅) ── CNOT ──                   │     │
    │     │  q6: ── RY(α₆) ── RZ(β₆) ── CNOT ──                   │     │
    │     │  q7: ── RY(α₇) ── RZ(β₇) ── ──── CNOT ──             │     │
    │     │                                                         │     │
    │     │  (Cyclic CNOT: q7 ── CNOT ── q0)                       │     │
    │     └─────────────────────────────────────────────────────────┘     │
    │                                                                     │
    ├─────────────────────────────────────────────────────────────────────┤
    │                        MEASUREMENT                                 │
    ├─────────────────────────────────────────────────────────────────────┤
    │                                                                     │
    │  q0: ─── M ───→ ⟨Z₀⟩                                              │
    │  q1: ─── M ───→ ⟨Z₁⟩                                              │
    │  q2: ─── M ───→ ⟨Z₂⟩                                              │
    │  q3: ─── M ───→ ⟨Z₃⟩                                              │
    │  q4: ─── M ───→ ⟨Z₄⟩                                              │
    │  q5: ─── M ───→ ⟨Z₅⟩                                              │
    │  q6: ─── M ───→ ⟨Z₆⟩                                              │
    │  q7: ─── M ───→ ⟨Z₇⟩                                              │
    │                                                                     │
    │  Each measurement → 16 bits → Total: 128 bits                     │
    └─────────────────────────────────────────────────────────────────────┘
    """


# ======================================================================
# 7. STREAMLIT APPLICATION
# ======================================================================

def main():
    
    # Header
    st.markdown('<div class="main-title">🔐 Quantum Sponge Hash (QSH)</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">VQC-Based Image Hash Function | Aya Rafii · JUFE 2026</div>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("📤 Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=["png", "jpg", "jpeg", "bmp", "tiff", "webp"]
        )
        
        st.divider()
        
        st.header("⚙️ Configuration")
        hash_method = st.radio(
            "Hash Method:",
            ["Quantum Sponge Hash (QSH)", "SHA-3 Baseline"],
            index=0
        )
        
        st.divider()
        
        st.header("🧪 Avalanche Test")
        enable_avalanche = st.checkbox("Enable Avalanche Test", value=False)
        
        if enable_avalanche:
            pixel_idx = st.slider(
                "Pixel to Flip",
                min_value=0,
                max_value=1023,
                value=0,
                help="Select pixel (0-1023) to flip"
            )
        
        st.divider()
        
        st.caption("🔬 **Qubits:** 8")
        st.caption("🧠 **Layers:** 6")
        st.caption("📏 **Hash Size:** 128 bits")
        st.caption("🧽 **State:** 256 bits (R=128, C=128)")
        st.caption("📦 **Absorption:** 64 blocks (128 bits each)")
        st.caption("🔄 **Dual View:** 97-bit right rotation")
        
        st.divider()
        
        st.caption("© 2026 · Aya Rafii · JUFE")
    
    # Main panel
    if uploaded_file is not None:
        # Preprocess
        image, bits, metadata = ImagePreprocessor.preprocess_from_upload(uploaded_file)
        
        # Image info
        st.subheader("📷 Image Information")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Size", f"{image.size[0]}×{image.size[1]}")
        with col2:
            st.metric("Mode", image.mode)
        with col3:
            st.metric("Format", image.format or "Unknown")
        with col4:
            st.metric("Pixels", metadata['num_pixels'])
        
        col_img, col_info = st.columns([1, 2])
        with col_img:
            st.image(image, caption="Uploaded Image", width=250)
        with col_info:
            st.caption(f"**Resized:** 32×32 grayscale")
            st.caption(f"**Total Bits:** {metadata['total_bits']:,}")
            st.caption(f"**128-bit Blocks:** {metadata['blocks_128']}")
            st.caption(f"**Pixel Range:** {metadata['pixel_stats']['min']}–{metadata['pixel_stats']['max']}")
            st.caption(f"**Pixel Mean:** {metadata['pixel_stats']['mean']:.1f}")
        
        with st.expander("🔧 Preprocessing Details"):
            st.caption("First 256 bits of image data:")
            st.code(''.join(map(str, bits[:256])) + '...', language="text")
        
        # Generate Hash
        st.divider()
        st.subheader("🔑 Generate Hash")
        
        if st.button("🚀 Generate Hash", type="primary", use_container_width=True):
            with st.spinner("Generating hash..."):
                if hash_method == "Quantum Sponge Hash (QSH)":
                    qsh = QuantumSpongeHash()
                    result = qsh.hash_image(bits)
                else:
                    result = sha3_baseline(bits)
            
            st.success(f"✅ {hash_method} completed in {result['time']:.4f} seconds")
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("**Hex Hash** (32 chars)")
                st.code(result['hex'], language="text")
            with col2:
                st.markdown("**Binary Hash** (128 bits)")
                st.code(result['binary'], language="text")
            
            if 'bits' in result:
                st.caption("**Hash Bitmap** (8×16 grid, white = 1, dark = 0):")
                grid = np.array(result['bits']).reshape(8, 16)
                fig, ax = plt.subplots(figsize=(10, 3))
                ax.imshow(grid, cmap='binary', aspect='auto')
                ax.set_xticks(range(16))
                ax.set_yticks(range(8))
                ax.set_xlabel('Bit Position')
                ax.set_ylabel('Row')
                st.pyplot(fig)
                plt.close(fig)
            
            if hash_method == "Quantum Sponge Hash (QSH)":
                with st.expander("🔬 View Quantum Circuit"):
                    st.text(draw_quantum_circuit())
        
        # Avalanche Test
        if enable_avalanche:
            st.divider()
            st.subheader("🧪 Proposed QSH Avalanche Effect Test")
            st.caption("Complements all eight bits of one canonical pixel and tests Proposed QSH.")
            
            if st.button("🔥 Run Avalanche Test", type="secondary", use_container_width=True):
                with st.spinner("Testing avalanche effect..."):
                    qsh = QuantumSpongeHash()
                    av_result = qsh.avalanche_test(bits, pixel_idx)
                
                # Display results
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(
                        "Hamming Distance",
                        av_result['hamming_distance'],
                        delta=f"{av_result['hamming_distance'] - 64:.0f} vs target"
                    )
                with col2:
                    st.metric(
                        "Avalanche Effect",
                        f"{av_result['avalanche_percentage']:.1f}%"
                    )
                with col3:
                    status = "✅ Good" if 45 <= av_result['avalanche_percentage'] <= 55 else "⚠️ Check"
                    st.metric("Status", status)
                
                st.progress(min(av_result['avalanche_percentage'] / 100, 1.0))
                
                # Hash comparison
                st.caption("**Hash Comparison:**")
                col1, col2 = st.columns(2)
                with col1:
                    st.caption("Original Hash:")
                    st.code(av_result['original_hash']['hex'])
                with col2:
                    st.caption("Modified Hash (1 pixel flipped):")
                    st.code(av_result['modified_hash']['hex'])
                
                # Bit changes visualization
                diff_bits = []
                for a, b in zip(av_result['original_hash']['bits'], av_result['modified_hash']['bits']):
                    diff_bits.append(1 if a != b else 0)
                
                diff_grid = np.array(diff_bits).reshape(8, 16)
                fig, ax = plt.subplots(figsize=(10, 2.5))
                ax.imshow(diff_grid, cmap='Reds', aspect='auto')
                ax.set_title('Bit Changes (red = changed)')
                ax.set_xticks(range(16))
                ax.set_yticks(range(8))
                st.pyplot(fig)
                plt.close(fig)
    
    else:
        st.info("📤 Please upload an image from the sidebar to begin.")
        
        st.markdown("""
        ### 🔐 What is Quantum Sponge Hash?
        
        **Quantum Sponge Hash (QSH)** is a novel quantum-enhanced hash function for image data.
        
        #### How it works:
        1. **Image → 32×32 grayscale → 8192 bits**
        2. **Sponge absorbs 64 blocks (128 bits each)**
        3. **VQC (8 qubits, 6 layers) mixes two state views per block**
           - Compute readouts from T and its 97-bit right rotation.
           - XOR both readouts into the rate and capacity: S = T XOR (a || d).
        4. **Squeeze → 128-bit hash**
        
        #### Key Properties:
        | Property | Description |
        |----------|-------------|
        | **Reported Mean Avalanche** | 48.9% over 200 pixel-complement trials; individual edits vary |
        | **Sample Uniqueness** | 200 distinct digests on 200 test images; not a security proof |
        | **Security Scope** | Noiseless diffusion experiment; no proven post-quantum resistance |
        | **Image-Aware** | Hashes a canonical 32×32 grayscale representation |
        
        #### Original Contribution:
        This implementation is part of the research:
        *"Robust Image Hash Code Generation Algorithm Based on Quantum Machine Learning"*
        
        **Aya Rafii · Prof. Zhang Yong · Jiangxi University of Finance and Economics**
        """)
    
    # Footer
    st.divider()
    st.markdown("""
    <div class="footer">
        🔐 Proposed QSH v2.0 &nbsp;·&nbsp; 
        <span>Original Work</span> &nbsp;·&nbsp; 
        © 2026 Aya Rafii · JUFE
    </div>
    """, unsafe_allow_html=True)


# ======================================================================
# 8. ENTRY POINT
# ======================================================================

if __name__ == "__main__":
    main()
