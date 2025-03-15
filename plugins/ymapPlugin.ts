import { defineNuxtPlugin } from '#app';
import { YandexMap, YandexMapMarker } from 'vue-yandex-maps';

export default defineNuxtPlugin((nuxtApp) => {
  nuxtApp.vueApp.component('YandexMap', YandexMap);
  nuxtApp.vueApp.component('YandexMapMarker', YandexMapMarker);
});