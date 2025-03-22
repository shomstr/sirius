<template>
  <div class="container">
    <div class="temperature-display">
      <h1>{{ temperature }}°C</h1>
    </div>
    <div class="car-number">
      <h2>Номер машины: {{ carNumber }}</h2>
    </div>
    <div class="divider"></div>
    <div class="order-history">
      <h3>История заказов</h3>
      <ul>
        <li v-for="(order, index) in orders" :key="index">{{ order }}</li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const temperature = ref(25); // Пример температуры
const carNumber = ref('А123БВ 777'); // Пример номера машины
const orders = ref([
  'Заказ 1: Замена масла',
  'Заказ 2: Проверка тормозов',
  'Заказ 3: Замена шин',
  'Заказ 4: Ремонт двигателя',
]); // Пример истории заказов
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
</style>