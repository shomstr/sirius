<template>
  <div id="map" class="w-full h-screen"></div>
</template>

<script>
export default {
  name: 'YandexMap',
  mounted() {
    this.initMap();
  },
  methods: {
    initMap() {
      ymaps.ready(() => {
        const geolocation = ymaps.geolocation;
        const myMap = new ymaps.Map('map', {
          center: [55, 34], // Центр карты по умолчанию
          zoom: 10,
        }, {
          searchControlProvider: 'yandex#search',
        });

        // Получение местоположения через IP (Yandex)
        geolocation.get({
          provider: 'yandex',
          mapStateAutoApply: true,
        }).then((result) => {
          // Красный маркер для местоположения по IP
          result.geoObjects.options.set('preset', 'islands#redCircleIcon');
          result.geoObjects.get(0).properties.set({
            balloonContentBody: 'Мое местоположение (по IP)',
          });
          myMap.geoObjects.add(result.geoObjects);
        });

        // Получение местоположения через браузер (GPS)
        geolocation.get({
          provider: 'browser',
          mapStateAutoApply: true,
        }).then((result) => {
          // Синий маркер для местоположения через браузер
          result.geoObjects.options.set('preset', 'islands#blueCircleIcon');
          myMap.geoObjects.add(result.geoObjects);
        });
      });
    },
  },
};
</script>

<style scoped>
#map {
  width: 100%;
  height: 100vh;
}
</style>