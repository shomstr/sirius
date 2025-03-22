<template>
  <div class="overlay-rectangle">
    <img src="/profile.svg" alt="Профиль" class="overlay-image" @click="handleProfileClick" />
    <img src="/map_icon.svg" alt="Карта" class="overlay-image" @click="handleMapClick" />
  </div>
</template>

<script setup>
import { defineEmits } from 'vue';

const emit = defineEmits(['profile-click', 'map-click']);

const handleProfileClick = () => {
  emit('profile-click');
};

const handleMapClick = () => {
  emit('map-click');
};
</script>

<style scoped>
.overlay-rectangle {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(55, 52, 52, 0.9);
  border-radius: 10px;
  padding: 10px 20px;
  display: flex;
  gap: 10px;
  box-shadow: 0 4px 8px rgba(255, 255, 255, 0.65);
}

.overlay-image {
  width: 60px;
  height: 60px;
  cursor: pointer;
}
</style>