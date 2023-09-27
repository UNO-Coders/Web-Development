/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      boxShadow: {
        custom: "rgba(0, 0, 0, 0.2) 0px 5px 30px",
      },
    },
  },
  plugins: [],
}
