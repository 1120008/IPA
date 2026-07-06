# 🌊 IPA: Abyssal Submarine Laboratory

**Sistem Otomatisasi LMS & Streaming untuk Gen Alpha** dengan tema Deep-Sea yang imersif dan inovatif.

> **Website:** [ipa-psi.vercel.app](https://ipa-psi.vercel.app)

---

## 🚀 Quick Start

### Untuk Mengunjungi Website
1. **Akses langsung:** Buka browser dan kunjungi [ipa-psi.vercel.app](https://ipa-psi.vercel.app)
   - Tidak perlu setup lokal
   - Responsive di semua perangkat
   - Streaming langsung terintegrasi

### Untuk Pengembangan Lokal

#### Prerequisites
- **Node.js** v16+ atau **npm** v8+
- **Git** untuk cloning repository

#### Setup Steps

```bash
# 1. Clone repository
git clone https://github.com/1120008/IPA.git
cd IPA

# 2. Install dependencies
npm install

# 3. Jalankan development server
npm run dev

# 4. Buka browser ke
http://localhost:5173 (Vite)
# atau
http://localhost:3000 (Fallback)
```

---

## 📋 Fitur Utama

### 🎬 Streaming Video 7 Jam
- **Periscope Viewport** - Video container bergaya jendela kapal selam
- **YouTube API Integration** - Materi edukatif terstruktur
- **Zoom Streaming** - Live session dengan protokol ketat (Mic Muted, No Screen Share, No Annotation)
- **Ripple Effect Transition** - Animasi WebGL saat berpindah video

### 🤖 Aquabot AI Companion
- **Chatbot Sokratik** - Panduan pembelajaran interaktif
- **Jellyfish Animation** - Avatar digital dengan efek bioluminescent
- **Tentacle Wave Motion** - Animasi thinking state yang responsif

### 📊 Depth Meter Dashboard
- **Progress Gauge** - Visualisasi kedalaman pencapaian siswa
- **Live Analytics** - Real-time data dari Google Sheets
- **NotebookLM Integration** - Kelengkapan materi (87%)

### 🧪 Specimen Bay Discussion
- **AI-Filtered Forum** - Otomatis filter SARA, opini agama, asusila
- **Safe Discourse** - Ruang diskusi sains yang terlindungi
- **Message Moderation** - Sistem guardrails berbasis AI

### 🔒 Keamanan Data
- **Enkripsi Total** - Token dinamis di sisi server
- **Lockdown Overlay** - Notifikasi visual saat attempt bypass keamanan
- **Zero-Human Dashboard** - Sinkronisasi otomatis tanpa intervensi manual

---

## 🎨 Deep-Sea UI/UX Theme

### Palet Warna Abyssal
| Nama | Hex | Fungsi |
|------|-----|--------|
| **Abyssal Base** | `#030712` | Latar belakang utama |
| **Biolum Cyan** | `#00f0ff` | Aksen neon, teks aktif |
| **Seafoam Green** | `#00ffb3` | Indikator sukses |
| **Deep Reef** | `rgba(11, 21, 40, 0.6)` | Card glassmorphism |

### Komponen Teknis
- **Glassmorphism Cards** - Backdrop blur 16px untuk efek sekat kaca
- **Animated Jellyfish** - 3D floating companion dengan tentacle wave
- **Depth Gauge** - Progress indicator visual
- **Quantum Ripples** - WebGL water ripple saat transisi

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| **Frontend** | HTML5, CSS3, JavaScript (Vanilla) |
| **Styling** | Tailwind CSS + Custom Deep-Sea CSS |
| **Video** | YouTube API, Zoom SDK |
| **Chatbot** | NotebookLM API |
| **Analytics** | Chart.js + Google Sheets API |
| **Deployment** | Vercel |
| **Security** | JWT tokens, encrypted payloads |

---

## 📁 Struktur Folder

```
IPA/
├── index.html                 # Entry point utama
├── tailwind.config.js         # Tailwind theme config
├── styles/
│   └── deep-sea.css          # Deep-sea themed stylesheets
├── scripts/
│   ├── api.js                # YouTube, Zoom, NotebookLM API calls
│   ├── chatbot.js            # Aquabot logic
│   └── dashboard.js          # Analytics & charting
├── assets/
│   ├── icons/                # Neon-styled SVG icons
│   ├── animations/           # WebGL shaders, keyframes
│   └── branding/             # Logo, illustrations
└── README.md                 # This file
```

---

## 🔐 Environment Variables

Buat file `.env` di root directory:

```env
# YouTube API
VITE_YOUTUBE_API_KEY=your_key_here

# Zoom
VITE_ZOOM_CLIENT_ID=your_client_id
VITE_ZOOM_SECRET=your_secret

# Google Sheets
VITE_GOOGLE_SHEETS_API_KEY=your_key_here

# NotebookLM
VITE_NOTEBOOKLM_API_KEY=your_key_here

# Security
VITE_JWT_SECRET=your_jwt_secret
VITE_ENCRYPTION_KEY=your_encryption_key
```

---

## 🚢 Deployment ke Vercel

### Automatic Deployment (Recommended)
1. Push ke branch `main`
2. Vercel otomatis trigger build & deploy
3. Website live di [ipa-psi.vercel.app](https://ipa-psi.vercel.app)

### Manual Deployment
```bash
npm install -g vercel
vercel login
vercel --prod
```

---

## 📱 Browser Support

| Browser | Support |
|---------|---------|
| Chrome 90+ | ✅ Full |
| Firefox 88+ | ✅ Full |
| Safari 15+ | ✅ Full |
| Edge 90+ | ✅ Full |
| Mobile (iOS/Android) | ✅ Responsive |

---

## 🎓 Panduan Penggunaan untuk Siswa

### Sebagai Peserta Kelas
1. **Akses URL** → [ipa-psi.vercel.app](https://ipa-psi.vercel.app)
2. **Login** → Input NIS dan password
3. **Ikuti Streaming** → Periscope Viewport menampilkan video live
4. **Diskusi** → Ketik di Specimen Bay forum
5. **Tanya Aquabot** → Chat dengan AI companion untuk bimbingan
6. **Track Progress** → Lihat Depth Meter dashboard

---

## 🤝 Kontribusi

### Bug Report
Buat issue di: [GitHub Issues](https://github.com/1120008/IPA/issues)

### Feature Request
Silakan submit PR dengan deskripsi jelas dan testing evidence.

---

## 📜 License

Proprietary - Hak Cipta Sistem Edukasi Gen Alpha

---

## 📞 Support & Kontak

- **Email:** support@ipa-psi.id
- **Docs:** [Dokumentasi Lengkap](https://docs.ipa-psi.id)
- **Discord:** [Join Community](https://discord.gg/ipa-science)

---

## 🌊 Tentang Tema Abyssal

Konsep **Deep-Sea Laboratory** dipilih karena:
- ✨ Efek **bioluminescent** menjaga fokus siswa 7 jam tanpa kelelahan mata
- 🧬 Ekosistem laut memberikan nuansa "hidup" vs ruang angkasa yang hampa
- 🎮 Gamifikasi: Siswa menjadi "ilmuwan muda" di kapal selam riset
- 🔬 Immersive UI membuat pembelajaran terasa seperti petualangan eksplorasi

---

**Made with 🌊 by Gen Alpha Science Lab Team**
