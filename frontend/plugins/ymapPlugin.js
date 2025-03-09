export default defineNuxtPlugin((nuxtApp) => {
    nuxtApp.provide('ymap', () => {
      return new Promise((resolve, reject) => {
        const script = document.createElement('script');
        script.src = 'https://api-maps.yandex.ru/2.1/?apikey=8ba27128-1da0-440b-a8c4-a55608c42593&lang=ru_RU';
        script.onload = () => {
          window.ymaps.ready(() => {
            resolve(window.ymaps);
          });
        };
        script.onerror = (error) => {
          reject(error);
        };
        document.head.appendChild(script);
      });
    });
  });