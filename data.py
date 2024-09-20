class Urls:
    URL_basic = 'https://qa-scooter.praktikum-services.ru/'
    URL_courier_create = f'{URL_basic}api/v1/courier/'
    URL_courier_login = f'{URL_basic}api/v1/courier/login'
    URL_orders_create = f'{URL_basic}api/v1/orders'

class Data:
    valid_login = 'Sergo2611'
    valid_password = 'qwerty'
    valid_firstname = 'Ser'
    valid_courier_data = {'login': 'Sergo2611', 'password': 'qwerty', 'firstName': 'Sergo'}
    courier_data_without_name = {'login': 'Sergo2611', 'password': 'qwerty'}
    courier_data_with_wrong_password = {'login': 'Sergo2611', 'password': '123456'}

class OrderData:
    order_data_grey_1 = {
        'firstName': 'Павел',
        'lastName': 'Пашин',
        'address': 'Открытое шоссе, 5к11',
        'metroStation': 8,
        'phone': '+78555555555',
        'rentTime': 3,
        'deliveryDate': '2024-09-16',
        'comment': 'Хорошая погодка :)',
        'color': [
            'GREY'
        ]
    }

    order_data_black_2 = {
        'firstName': 'Костя',
        'lastName': 'Костыгин',
        'address': 'Большая Семёновская улица, 24',
        'metroStation': 10,
        'phone': '+78888888888',
        'rentTime': 5,
        'deliveryDate': '2024-09-18',
        'comment': 'Ужаснено хочется покататься!',
        'color': [
            'BLACK'
        ]
    }

    order_data_two_colors_3 = {
        'firstName': 'Илья',
        'lastName': 'Илюшин',
        'address': 'площадь Рогожская Застава, 2/1с2',
        'metroStation': 15,
        'phone': '+70009999999',
        'rentTime': 1,
        'deliveryDate': '2024-09-10',
        'comment': 'Покатаемся!',
        'color': [
            'BLACK', 'GREY'
        ]
    }

    order_data_no_colors_4 = {
        'firstName': 'Баба',
        'lastName': 'Бабина',
        'address': 'Волгоградский проспект, 28А',
        'metroStation': 20,
        'phone': '+78777777778',
        'rentTime': 2,
        'deliveryDate': '2024-09-17',
        'comment': 'Едем',
        'color': []
    }
