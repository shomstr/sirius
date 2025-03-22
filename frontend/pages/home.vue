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
        <p>
          Статус:
          <span :class="{'status-active': selectedMarker.active, 'status-inactive': !selectedMarker.active}">
            {{ selectedMarker.active ? 'Активна' : 'Неактивна' }}
          </span>
        </p>
        <p>
          Режим работы:
          <span :class="{'status-active': selectedMarker.details.opening_times?.always_open}">
            {{ formatOpeningTimes(selectedMarker.details.opening_times) }}
          </span>
        </p>
        <p>Коннекторы:</p>
        <ul>
          <li v-for="connector in selectedMarker.details.connectors" :key="connector.id">
            {{ connector.connector }} ({{ connector.power }} кВт)
            <br>
          </li>
        </ul>
        <p>Описание: {{ selectedMarker.details.description || 'Нет описания' }}</p>
        <button class="close_button" @click="closeModal">Закрыть</button>
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

const formatOpeningTimes = (openingTimes) => {
  if (!openingTimes) return 'Нет информации';
  return openingTimes.always_open ? 'Круглосуточно' : 'По расписанию';
};

const formatChangedAt = (changedAt) => {
  if (!changedAt) return 'Нет информации';
  const date = new Date(changedAt);
  return date.toLocaleString('ru-RU', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
  });
};

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
    const response = await axios.get('http://localhost:8000/point/get_all_points_coordinates/');
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

.close_button {
  background-color: #196dff;
  height: 35px;
  width: 100%;
}

.close_button:hover {
  background-color: green;
}

.modal {
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
}

.modal-content {
  background-color: rgba(40, 40, 40, 1); 
  color: white;
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

.button close_button {
  float: right;
  margin-right: 10px;
}

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

.status-active {
  color: green;
  font-weight: bold;
}

.status-inactive {
  color: red;
  font-weight: bold;
}
</style>