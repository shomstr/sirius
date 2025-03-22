<template>
  <div class="modal">
    <div class="modal-content">
      <span class="close" @click="close">&times;</span>
      <h2>Информация об "{{ marker.name }}"</h2>
      <p>ID: {{ marker.id }}</p>
      <p>Адрес: {{ marker.address }}</p>
      <p>
        Статус:
        <span :class="{'status-active': marker.active, 'status-inactive': !marker.active}">
          {{ marker.active ? 'Активна' : 'Неактивна' }}
        </span>
      </p>
      <p>
        Режим работы:
        <span :class="{'status-active': marker.details.opening_times?.always_open}">
          {{ formatOpeningTimes(marker.details.opening_times) }}
        </span>
      </p>
      <p>Коннекторы:</p>
      <ul>
        <li v-for="connector in marker.details.connectors" :key="connector.id">
          {{ connector.connector }} ({{ connector.power }} кВт)
        </li>
      </ul>
      <p>Описание: {{ marker.details.description || 'Нет описания' }}</p>
      <button class="build-route-button" @click="buildRoute" :disabled="!marker">
        Построить маршрут
      </button>
      <button class="close_button" @click="close">Закрыть</button>
    </div>
  </div>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue';

const props = defineProps({
  marker: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(['close', 'build-route']);

const formatOpeningTimes = (openingTimes) => {
  if (!openingTimes) return 'Нет информации';
  return openingTimes.always_open ? 'Круглосуточно' : 'По расписанию';
};

const close = () => {
  emit('close');
};

const buildRoute = () => {
  emit('build-route');
};
</script>

<style scoped>
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
  background-color: rgba(40, 40, 40, 0.9);
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

.build-route-button {
  background-color: #4CAF50;
  color: white;
  width: 100%;
  height: 35px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  margin-bottom: 10px;
}

.build-route-button:hover {
  background-color: #45a049;
}

.close_button {
  background-color: #196dff;
  height: 35px;
  width: 100%;
}

.close_button:hover {
  background-color: green;
}
</style>