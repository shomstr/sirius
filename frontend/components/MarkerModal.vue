<template>
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
</template>

<script setup>
const props = defineProps({
  selectedMarker: {
    type: Object,
    default: null,
  },
});

const emit = defineEmits(['close']);

const formatOpeningTimes = (openingTimes) => {
  if (!openingTimes) return 'Нет информации';
  return openingTimes.always_open ? 'Круглосуточно' : 'По расписанию';
};

const closeModal = () => {
  emit('close');
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

.close_button {
  background-color: #196dff;
  height: 35px;
  width: 100%;
}

.close_button:hover {
  background-color: green;
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