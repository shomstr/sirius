<script setup>
import { ref, onMounted } from 'vue';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapMarker,
  YandexMapDefaultFeaturesLayer,
  YandexMapGeolocationControl,
} from 'vue-yandex-maps';

const userCoords = ref(null);

const isModalOpen = ref(false);

const selectedMarker = ref(null);

const getUserLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        userCoords.value = [position.coords.latitude, position.coords.longitude];
      },
      (error) => {
        console.error('Ошибка при получении геолокации:', error);
        alert('Не удалось получить ваше местоположение. Пожалуйста, разрешите доступ к геолокации.');
      },
      {
        enableHighAccuracy: true,
        timeout: 5000,
        maximumAge: 0, 
      }
    );
  } else {
    console.error('Геолокация не поддерживается вашим браузером');
    alert('Ваш браузер не поддерживает геолокацию.');
  }
};

onMounted(() => {
  getUserLocation();
});

const ImagePath = '/station.svg';

const markers = [
  {
    coordinates: [51.789682128109, 55.140428698122],
    id: 'marker-1',
    content: 'Маркер 1',
  },
  {
    coordinates: [54.76778893634, 57.108481458691],
    id: 'marker-2',
    content: 'Маркер 2',
  },
];

const handleMarkerClick = (marker) => {
  console.log('Маркер кликнут:', marker.content);
  selectedMarker.value = marker;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  selectedMarker.value = null;
};
</script>

<template>
  <div class="w-full h-screen">
    <YandexMap
      v-if="userCoords"
      :settings="{
        location: {
          center: userCoords,
          zoom: 17,
        }
      }"
      width="100%"
      height="100%"
    >
      <YandexMapDefaultSchemeLayer />
      <YandexMapDefaultFeaturesLayer />
      
      <YandexMapMarker
        :settings="{
          coordinates: userCoords,
          id: 'user-location',
        }"
      >
        <div class="w-[20px] h-[20px] relative bg-blue-500 opacity-80 rounded-full"></div>
      </YandexMapMarker>

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
    
    <div v-if="isModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div class="bg-white p-6 rounded-lg shadow-lg">
        <h2 class="text-xl font-bold mb-4">Информация о маркере</h2>
        <p>{{ selectedMarker.content }}</p>
        <button @click="closeModal" class="mt-4 px-4 py-2 bg-blue-500 text-white rounded">Закрыть</button>
      </div>
    </div>
  </div>
</template>

<style>
html, body, #__nuxt {
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