<template>
  <div class="w-full h-screen">
    <YandexMap
      :settings="{
        location: {
          center: [55.75, 37.57],
          zoom: 10, 
        },
        scheme: 'dark'
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

const props = defineProps({
  markers: {
    type: Array,
    required: true,
  },
  handleMarkerClick: {
    type: Function,
    required: true,
  },
});

const ImagePath = '/station.svg';
</script>

<style scoped>
.marker {
  color: #196dff;
  font-weight: bold;
}
</style>