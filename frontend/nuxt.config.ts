// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  devtools: { enabled: true },

  modules: [
    "@nuxtjs/tailwindcss",
    '@pinia/nuxt',
    'vue-yandex-maps/nuxt', // Модуль для Яндекс.Карт
  ],

  yandexMaps: {
    apikey: '8ba27128-1da0-440b-a8c4-a55608c42593', // Ваш API-ключ
    lang: 'ru_RU', // Язык карты
  },

  plugins: [
    { src: '@/plugins/ymapPlugin.js', mode: 'client' }, // Плагин для Яндекс.Карт
  ],

  compatibilityDate: '2025-03-09',
});