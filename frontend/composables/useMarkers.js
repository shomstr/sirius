import { ref, onMounted } from 'vue';

export const useMarkers = () => {
  const markers = ref([]);
  const selectedMarker = ref(null);

  const handleMarkerClick = async (marker) => {
    try {
      const response = await $fetch('http://localhost:8000/point/${marker.id}'); 
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

  onMounted(async () => {
    try {
      const response = await $fetch('http://localhost:8000/get_all_points_coordinates/');
      console.log(response); // Проверка данных
      markers.value = response.data.map(point => ({
        coordinates: [point.latitude, point.longitude], // Исправлено
        id: point.point_id, 
      }));
    } catch (error) {
      console.error('Ошибка при загрузке маркеров:', error);
    }
  });

  return {
    markers,
    selectedMarker,
    handleMarkerClick,
  };
};