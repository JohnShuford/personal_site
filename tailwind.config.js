/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./core/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        'jet-black': '#0B0C10',
        'charcoal-gray': '#2E2E2E',
        'pine-green': '#2C6E49',
        'cedar-brown': '#7E5E60',
        'warm-sand': '#D7C9AA',
        'clay-beige': '#C1A57B',
        'rust-orange': '#C75B39',
        'muted-gold': '#A68A64',
        'floral-mist': '#D9EAD3',
      },
      fontFamily: {
        'sans': ['Segoe UI', 'Tahoma', 'Geneva', 'Verdana', 'sans-serif'],
      },
    },
  },
  plugins: [],
}