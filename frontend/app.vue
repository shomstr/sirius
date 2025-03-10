<template>
  <div class="w-full h-screen">
    <YandexMap
      :settings="{
        location: {
          center: [55.45, 37.36],
          zoom: 10, 
        }
      }"
      width="100%"
      height="100%"
    >
      <yandex-map-default-scheme-layer/>
      <yandex-map-default-features-layer/>
      <yandex-map-controls :settings="{ position: 'right' }">
        <yandex-map-zoom-control/>
      </yandex-map-controls>
      <yandex-map-controls :settings="{ position: 'bottom' }">
        <yandex-map-zoom-control/>
        <yandex-map-scale-control/>
      </yandex-map-controls>
      <yandex-map-controls :settings="{ position: 'left' }">
    
        <yandex-map-geolocation-control/>
      </yandex-map-controls>

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

<script setup>
import { ref } from 'vue';
import {
  YandexMap,
  YandexMapDefaultSchemeLayer,
  YandexMapMarker,
  YandexMapDefaultFeaturesLayer,
  YandexMapZoomControl,
  YandexMapScaleControl,
  YandexMapGeolocationControl, YandexMapControls
} from 'vue-yandex-maps';

const isModalOpen = ref(false);
const selectedMarker = ref(null);

const handleMarkerClick = (marker) => {
  console.log('Маркер кликнут:', marker.content);
  selectedMarker.value = marker;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  selectedMarker.value = null;
};

const ImagePath = '/station.svg';

const markers = [
  {
    coordinates: [55.751244, 37.618423],
    id: 'marker-1',
    content: 'Маркер 1',
  },
  {
    coordinates: [54.76778893634, 57.108481458691],
    id: 'marker-2',
    content: 'Маркер 2',
  },
];
</script>

<style scoped>
.marker {
  color: #196dff;
  font-weight: bold;
}
</style>