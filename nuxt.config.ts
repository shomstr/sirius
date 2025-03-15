import { defineNuxtConfig } from "nuxt/config";

export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: [
    "@nuxtjs/tailwindcss", 
    '@pinia/nuxt', 
    'vue-yandex-maps/nuxt',
  ],

  css: ['~/assets/css/tailwind.css'],

  postcss: {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  },

  yandexMaps: {
    apikey: '8ba27128-1da0-440b-a8c4-a55608c42593', 
    lang: 'ru_RU', 
  },

  plugins: [
    { src: '~/plugins/ymapPlugin.ts', mode: 'client' }, 
  ],

  routeRules: {
    '/': { redirect: '/home' }, 
  },

  typescript: {
    strict: true, 
    typeCheck: true,
  },

  build: {
    transpile: ['vue-yandex-maps'],
  },

  compatibilityDate: '2025-03-14',
});