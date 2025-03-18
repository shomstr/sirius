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

    <div v-if="selectedMarker" class="modal">
      <div class="modal-content">
        <span class="close" @click="closeModal">&times;</span>
        <h2>Информация об "{{ selectedMarker.name }}"</h2>
        <p>ID: {{ selectedMarker.id }}</p>
        <p>Адрес: {{ selectedMarker.address }}</p>
        <p>Активна: {{ selectedMarker.active ? 'Да' : 'Нет' }}</p>
        <p>Коннектор: {{ selectedMarker.connector || 'Нет информации' }}</p>
        <p>Описание: {{ selectedMarker.description || 'Нет описания' }}</p>
        <p>Обновлено: {{ selectedMarker.changed_at || 'Нет Инф' }}</p>
        <p>Details: {{ selectedMarker.details }}</p>
      </div>
    </div>
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
const selectedMarker = ref(null);
const ImagePath = '/station.svg';

const handleMarkerClick = async (marker) => {
  try {
    const response = await axios.get(`http://localhost:8000/point/${marker.id}`); 

    selectedMarker.value = { 
      id: marker.id, 
      name: response.data.name, 
      address: response.data.address, 
      details: response.data,
      active: response.data.active,
      description: response.data.description,
      connector: response.data.connector,
      changed_at: response.data.changed_at

    };
  } catch (error) {
    console.error('Ошибка при загрузке информации о маркере:', error);
  }
};

const closeModal = () => {
  selectedMarker.value = null;
};

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:8000/get_all_points_coordinates/');
    markers.value = response.data.map(point => ({
      coordinates: [point.longitude, point.latitude], 
      id: point.point_id, 
    }));
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

.modal {
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: #fefefe;
  margin: 15% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>