<template>
  <div class="w-full h-screen">
    <YandexMap
      :settings="{
        location: {
          center: [55.75, 37.57],
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
        }"
        @click="handleMarkerClick(marker)"
      >
        <img :src="ImagePath" class="object-cover" />
        <div class="marker">{{ marker.id }}</div>
      </YandexMapMarker>
    </YandexMap>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';
import {
  YandexMap,
  YandexMapMarker,
  YandexMapDefaultSchemeLayer,
  YandexMapDefaultFeaturesLayer,
  YandexMapZoomControl,
  YandexMapScaleControl,
  YandexMapGeolocationControl,
  YandexMapControls,
} from 'vue-yandex-maps';

const markers = ref([]);
const ImagePath = '/station.svg';

const handleMarkerClick = async (marker) => {
  try {
    const response = await axios.get(`http://localhost:8000/point/${marker.id}`); 
    console.log('Информация о маркере:', response.data);
  } catch (error) {
    console.error('Ошибка при загрузке информации о маркере:', error);
  }
};

onMounted(async () => {
     try {
       const response = await axios.get('http://localhost:8000/get_all_points_coordinates/');
       console.log('Данные с сервера:', response.data); // Проверка данных
       markers.value = response.data.map(point => ({
         coordinates: [point.longitude, point.latitude], // Убедитесь, что latitude и longitude в правильном порядке
         id: point.point_id, 
       }));
       console.log('Маркеры:', markers.value); 
     } catch (error) {
       console.error('Ошибка при загрузке маркеров:', error);
     }
   });
</script>

<style scoped>
.marker {
  color: #196dff;
  font-weight: bold;
}
</style>