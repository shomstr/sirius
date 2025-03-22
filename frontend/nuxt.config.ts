// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: [
    "@nuxtjs/tailwindcss",
    '@pinia/nuxt',
    'vue-yandex-maps/nuxt', 
  ],

  yandexMaps: {
    apikey: '8ba27128-1da0-440b-a8c4-a55608c42593',
    lang: 'ru_RU',
  },

  plugins: [
    { src: '@/plugins/ymapPlugin.js', mode: 'client' },
  ],
  routeRules: {
    '/': { redirect: 'home' },
    '/profile': { redirect: 'user' },
  },
  
  compatibilityDate: '2025-03-09',
});