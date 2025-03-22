<template>
  <div class="container">
    <div class="temperature-display">
      <h1>{{ temperature }}°C</h1>
      <div class="temperature-controls">
        <button @click="decreaseTemperature">-</button>
        <button @click="increaseTemperature">+</button>
        <button v-if="isTemperatureChanged" @click="applyTemperature">Применить</button>
      </div>
    </div>
    <div class="car-number">
      <h2>Номер машины: {{ carId }}</h2>
    </div>
    <div class="divider"></div>
    <div class="order-history">
      <h3>История заказов</h3>
      <ul>
        <li v-for="(order, index) in orders" :key="index">{{ order }}</li>
      </ul>
    </div>
    <div class="start-button">
      <button @click="startCar" :disabled="isCarStarted">Старт</button>
      <button @click="stopCar" :disabled="!isCarStarted">Стоп</button>
      <p v-if="isCarStarted">Машина уже запущена</p>
      <p v-if="!isCarStarted">Машина остановлена</p>
    </div>
    <OverlayRectangle @profile-click="handleProfileClick" @map-click="handleMapClick" />
  </div>
</template>

<script setup>

import OverlayRectangle from '../components/OverlayRectangle.vue';

import { ref, onMounted } from 'vue';
import axios from 'axios';

const temperature = ref(25);
const carNumber = ref('А123БВ 777');
const orders = ref([
  'Заказ 1: Замена масла',
  'Заказ 2: Проверка тормозов',
  'Заказ 3: Замена шин',
  'Заказ 4: Ремонт двигателя',
]);
const isCarStarted = ref(false);
const isTemperatureChanged = ref(false);
const carId = ref(5)

const fetchCarInfo = async () => {
  try {
    const response = await axios.post('http://127.0.0.1:8000/car_wash/get_car_info?car_id=5');
    const carInfo = response.data;
    temperature.value = carInfo.temperature;
    isCarStarted.value = carInfo.started;
  } catch (error) {
    console.error('Ошибка при получении информации о машине:', error);
  }
};

const startCar = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/car_wash/set_status?car_id=5&status=true');
    isCarStarted.value = true;
  } catch (error) {
    console.error('Ошибка при запуске машины:', error);
  }
};
const stopCar = async () => {
  try {
    await axios.post('http://127.0.0.1:8000/car_wash/set_status?car_id=5&status=false');
    isCarStarted.value = false;
  } catch (error) {
    console.error('Ошибка при остановке машины:', error);
  }
};
const increaseTemperature = () => {
  temperature.value += 1;
  isTemperatureChanged.value = true;
};

const decreaseTemperature = () => {
  temperature.value -= 1;
  isTemperatureChanged.value = true;
};

const applyTemperature = async () => {
  try {
    await axios.post(`http://127.0.0.1:8000/car_wash/set_temperature?car_id=${carId.value}&temperature=${temperature.value}`);
    isTemperatureChanged.value = false;
  } catch (error) {
    console.error('Ошибка при изменении температуры:', error);
  }
};

onMounted(() => {
  fetchCarInfo();
});
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  font-family: Arial, sans-serif;
}

.temperature-display {
  font-size: 48px;
  margin-bottom: 20px;
}

.temperature-controls {
  display: flex;
  gap: 10px;
  margin-top: 10px;
}

.car-number {
  font-size: 24px;
  margin-bottom: 20px;
}

.divider {
  width: 100%;
  height: 2px;
  background-color: #ccc;
  margin: 20px 0;
}

.order-history {
  width: 100%;
}

.order-history h3 {
  margin-bottom: 10px;
}

.order-history ul {
  list-style-type: none;
  padding: 0;
}

.order-history li {
  padding: 5px 0;
  border-bottom: 1px solid #ccc;
}

.start-button {
  margin-top: 20px;
}

.start-button button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>