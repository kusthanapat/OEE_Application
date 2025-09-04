/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // สำคัญ!
<<<<<<< HEAD
    "./static/**/*.{js,css}", // ถ้ามี JS ที่ใช้ Tailwind classes
=======
    "./static/js/**/*.js", // ถ้ามี JS ที่ใช้ Tailwind classes
>>>>>>> 1efc0888d317b75d222fc46ccbbda82369f5f5c4
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
