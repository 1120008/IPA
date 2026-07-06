/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Abyssal Deep-Sea Theme
        'abyssal-base': '#030712',
        'abyssal-deep': '#0b1528',
        'abyssal-card': '#0f1b35',
        'biolum-cyan': '#00f0ff',
        'biolum-cyan-dark': '#00b8cc',
        'seafoam-green': '#00ffb3',
        'seafoam-muted': '#00cc8f',
        'deep-reef': 'rgba(11, 21, 40, 0.6)',
        'neon-alert': '#ff1744',
        'neon-success': '#00ffb3',
      },
      backgroundColor: {
        'glass-dark': 'rgba(11, 21, 40, 0.6)',
        'glass-darker': 'rgba(3, 7, 18, 0.8)',
      },
      backdropBlur: {
        'glass': 'blur(16px)',
      },
      boxShadow: {
        'glow-cyan': '0 0 20px rgba(0, 240, 255, 0.5)',
        'glow-green': '0 0 20px rgba(0, 255, 179, 0.5)',
        'glow-alert': '0 0 15px rgba(255, 23, 68, 0.6)',
        'submarine': '0 8px 32px rgba(0, 240, 255, 0.15)',
      },
      animation: {
        'pulse-glow': 'pulseGlow 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
        'float': 'float 3s ease-in-out infinite',
        'ripple': 'ripple 0.6s ease-out',
        'jellyfish-tentacle': 'jellyfish 3s ease-in-out infinite',
        'depth-descend': 'depthDescend 0.8s ease-out',
        'biolum-flicker': 'biolumFlicker 0.3s ease-in-out',
      },
      keyframes: {
        pulseGlow: {
          '0%, 100%': { 'box-shadow': '0 0 20px rgba(0, 240, 255, 0.5)' },
          '50%': { 'box-shadow': '0 0 30px rgba(0, 240, 255, 0.8)' },
        },
        float: {
          '0%, 100%': { transform: 'translateY(0px)' },
          '50%': { transform: 'translateY(-10px)' },
        },
        ripple: {
          '0%': { transform: 'scale(0)', opacity: '1' },
          '100%': { transform: 'scale(4)', opacity: '0' },
        },
        jellyfish: {
          '0%, 100%': { transform: 'scaleY(1)' },
          '50%': { transform: 'scaleY(0.95)' },
        },
        depthDescend: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        biolumFlicker: {
          '0%, 100%': { opacity: '1' },
          '50%': { opacity: '0.7' },
        },
      },
    },
  },
  plugins: [],
}
