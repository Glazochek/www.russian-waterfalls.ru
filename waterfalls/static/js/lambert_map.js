function F6(cord, name, id) {
    ymaps.ready(['projection.LambertConformalConic']).then(function init() {
        // Создаем проекцию Ламберта.
        var LAMBERT_PROJECTION = new ymaps.projection.LambertConformalConic();

        // Создаем карту.
        var map = new ymaps.Map('map', {
            center: [65, 100],
            zoom: 2,
            type: null,
            controls: ['zoomControl']
        }, {
            minZoom: 1,
            // Задаем проекцию Ламберта.
            projection: LAMBERT_PROJECTION,
            searchControlProvider: 'yandex#search'
        });
        map.controls.get('zoomControl').options.set({ size: 'small' });

        // Добавляем фон.
        var pane = new ymaps.pane.StaticPane(map, {
            zIndex: 100, css: {
                width: '100%', height: '100%', backgroundColor: '#000'
            }
        });
        map.panes.append('greyBackground', pane);

        // Загружаем и добавляем регионы России на карту.
        ymaps.borders.load('RU', {
            lang: 'ru'
        }).then(function (result) {
            regions = new ymaps.GeoObjectCollection(null, {
                fillColor: '#fff',
                strokeColor: '#000',
                hasHint: false,
                cursor: 'default'
            });
            for (var i = 0; i < result.features.length; i++) {
                regions.add(new ymaps.GeoObject(result.features[i]));
            }

            map.geoObjects.add(regions);
        });


        // Создаем геообъект с типом геометрии "Точка".
        myGeoObject = new ymaps.GeoObject({
            // Описание геометрии.
            geometry: {
                type: "Point",
                coordinates: [55.8, 37.8]
            },
            // Свойства.
            properties: {
                // Контент метки.
                iconContent: 'Я тащусь',
                hintContent: 'Ну давай уже тащи'
            }
        }, {
            // Опции.
            // Иконка метки будет растягиваться под размер ее содержимого.
            preset: 'islands#blackStretchyIcon',
            // Метку можно перемещать.
            draggable: true
        }),

        violetCollection = new ymaps.GeoObjectCollection(null, {
            preset: 'islands#violetIcon'
        }),

        violetCoords = cord
        violetText = name

//        url = url

        for (var i = 0, l = violetCoords.length; i < l; i++) {
            let url = `/waterfalls/${id[i]}/info/`

            myGeoObject = new ymaps.GeoObject({
                // Описание геометрии.


                geometry: {
                    type: "Point",
                    coordinates: violetCoords[i]
                },
                // Свойства.
                properties: {
                    // Контент метки.
                    hintContent: name[i]
                }

            }, {
                // Опции.
                // Иконка метки будет растягиваться под размер ее содержимого.
                preset: 'islands#violetStretchyIcon',
            }),
                myGeoObject.events.add('click', function () {
                    window.location.href = url
                });
            map.geoObjects.add(myGeoObject)

        }


    });



}