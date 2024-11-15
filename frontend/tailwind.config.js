/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./public/**/*.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  future: {
    hoverOnlyWhenSupported: true,
  },
  theme: {
    extend: {
      screens: {
        origin: "800px",
      },
      keyframes: {
        'dot-flashing': {
          '0%': { backgroundColor: '#333' },
          '50%': { backgroundColor: '#ccc' },
          '100%': { backgroundColor: '#ccc' },
        },
      },
    },
  },
  plugins: [],
}

