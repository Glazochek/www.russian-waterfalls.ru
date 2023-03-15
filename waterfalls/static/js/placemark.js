
function F5(crd) {
    ymaps.ready(init);

    function init() {
        var myMap = new ymaps.Map("map-2", {
            center: crd,
            zoom: 5,
            controls: ['smallMapDefaultSet']
        }, {
        })

        myMap.geoObjects

            .add(new ymaps.Placemark(crd, {
                balloonContent: 'водопад'
            }, {
                preset: 'islands#icon',
                iconColor: 'blueviolet'
            }))
    }
}
