(function () {
  fetch("https://api.tukui.org/v1/addon/elvui")
    .then((response) => response.json())
    .then((data) => {
      return data.url;
    });
})();