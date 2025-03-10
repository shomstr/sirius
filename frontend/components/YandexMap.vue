<template>
  <div class="w-full h-screen">
    <YandexMap
      :settings="{
        location: {
          center: userCoords,
          zoom: 17,
        },
      }"
      width="100%"
      height="100%"
    >
      <YandexMapDefaultSchemeLayer />
      <YandexMapDefaultFeaturesLayer />

      <!-- Маркер пользователя -->
      <YandexMapMarker
        :settings="{
          coordinates: userCoords,
          id: 'user-location',
        }"
      >
        <div class="w-[20px] h-[20px] relative bg-blue-500 opacity-80 rounded-full"></div>
      </YandexMapMarker>

      <!-- Дополнительные маркеры -->
      <YandexMapMarker
        v-for="marker in markers"
        :key="marker.id"
        :settings="{
          coordinates: marker.coordinates,
          id: marker.id,
        }"
        @click="handleMarkerClick(marker)"
      >
        <img :src="ImagePath" class="object-cover" />
        <div class="marker">{{ marker.content }}</div>
      </YandexMapMarker>
    </YandexMap>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapMarker,
  YandexMapDefaultFeaturesLayer,
} from 'vue-yandex-maps';

const userCoords = ref([55.751574, 37.573856]); // Начальные координаты (Москва)
const ImagePath = '/station.svg';

const markers = [
  {
    coordinates: [51.789682128109, 55.140428698122], // Координаты первого маркера
    id: 'marker-1',
    content: 'Маркер 1',
  },
  {
    coordinates: [54.76778893634, 57.108481458691], // Координаты второго маркера
    id: 'marker-2',
    content: 'Маркер 2',
  },
];

const handleMarkerClick = (marker) => {
  console.log('Маркер кликнут:', marker.content);
};

onMounted(() => {
  getUserLocation();
});

function getUserLocation() {
  ymaps.geolocation
    .get({ provider: 'yandex', mapStateAutoApply: true })
    .then((result) => {
      result.geoObjects.options.set('preset', 'islands#redCircleIcon');
      result.geoObjects.get(0).properties.set({
        balloonContentBody: 'Мое местоположение',
      });
      userCoords.value = result.geoObjects.get(0).geometry.getCoordinates();
    });

  ymaps.geolocation
    .get({ provider: 'browser', mapStateAutoApply: true })
    .then((result) => {
      result.geoObjects.options.set('preset', 'islands#blueCircleIcon');
      userCoords.value = result.geoObjects.get(0).geometry.getCoordinates();
    });
}
</script>

<style>
html,
body,
#__nuxt {
  height: 100%;
  margin: 0;
  padding: 0;
}

.marker {
  position: relative;
  width: 20px;
  height: 20px;
}
</style>