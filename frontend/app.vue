<script setup>
import { ref, onMounted } from 'vue';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapMarker,
  YandexMapDefaultFeaturesLayer,
  YandexMapGeolocationControl,
} from 'vue-yandex-maps';

// Состояние для хранения координат пользователя
const userCoords = ref(null);

// Функция для получения геолокации
const getUserLocation = () => {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        // Успешно получены координаты
        userCoords.value = [position.coords.latitude, position.coords.longitude];
      },
      (error) => {
        // Ошибка при получении координат
        console.error('Ошибка при получении геолокации:', error);
        alert('Не удалось получить ваше местоположение. Пожалуйста, разрешите доступ к геолокации.');
      },
      {
        enableHighAccuracy: true, // Высокая точность
        timeout: 5000, // Максимальное время ожидания
        maximumAge: 0, // Не использовать кэшированные данные
      }
    );
  } else {
    console.error('Геолокация не поддерживается вашим браузером');
    alert('Ваш браузер не поддерживает геолокацию.');
  }
};

// Получаем геолокацию при монтировании компонента
onMounted(() => {
  getUserLocation();
});

const ImagePath = '/station.svg';
// Массив маркеров
const markers = [
  {
    coordinates: [51.789682128109, 55.140428698122], // Координаты первого маркера
    id: 'marker-1',
    content: 'ma',
  },
  {
    coordinates: [54.76778893634, 57.108481458691], // Координаты второго маркера
    id: 'marker-2',
    content: 'Маркер 2',
  },
];

// Обработчик клика на маркер
const handleMarkerClick = (marker) => {
  console.log('Маркер кликнут:', marker.content);
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