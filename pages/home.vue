<template>
  <YandexMap :settings="{ location: { center: [55.75, 37.57], zoom: 10 } }">
    <YandexMapMarker :settings="{ coordinates: [55.75, 37.57] }" />
  </YandexMap>
</template>