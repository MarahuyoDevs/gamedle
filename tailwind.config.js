/** @type {import('tailwindcss').Config} */
export default {
  content: ["./gamedle/routes/**/*.{html,js,py}"],
  theme: {
    extend: {},
  },
  /** @type {import('rippleui').Config} */
  rippleui: {
    themes: [
      {
        themeName: "light",
        colorScheme: "light",
        colors: {
          primary: "#FB923C",
          backgroundPrimary: "#964643",
          secondary: "#404040",
          light: "#F8FAFC",
        },
      },
      {
        themeName: "dark",
        colorScheme: "dark",
        colors: {
          primary: "#FB923C",
          backgroundPrimary: "#1a1a1a",
          secondary: "#404040",
          dark: "#27272A",
        },
      },
    ],
  },
  plugins: [require("rippleui")],
};
