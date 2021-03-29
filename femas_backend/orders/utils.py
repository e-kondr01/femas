from collections import OrderedDict

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

admin_mail = "e.kondr01@gmail.com"
mail_from = 'noreply@e-kondr01.ru'


def format_consumer_message(data):
    msg = (f'Уважаемый {data["name"]} {data["surname"]}!\n'
           f'Детали по вашему заказу номер {data["uuid"]} с сайта Femas:\n'
           f'Общая стоимость заказа: {data["total_price"]}р.\n'
           f'Состав заказа:\n')
    for product in data['products']:
        product_data = dict(OrderedDict(product))
        msg += (f'{product_data["name"]}, стоимость {product_data["price"]}р.,'
                f' количество {product_data["quantity"]}\n')
    msg += ('Детали доставки:\n'
            f'Телефон: {data["phone"]}, '
            f'город: {data["city"]}, '
            f'адрес: {data["delivery_address"]}, '
            f'подъезд: {data["entrance"]}\n'
            '\nЭто сообщение было автоматически сгенерировано.')
    return msg


def format_admin_message(data):
    msg = (
        f'{data["name"]} {data["surname"]} '
        f'оставил заказ на сайте Femas под номером {data["uuid"]}.\n'
        f'Общая стоимость заказа: {data["total_price"]}р.\n'
        f'Состав заказа:\n')
    for product in data["products"]:
        product_data = dict(OrderedDict(product))
        msg += (f'{product_data["name"]}, стоимость {product_data["price"]}р.,'
                f' количество {product_data["quantity"]}\n')
    msg += ('Детали доставки:\n'
            f'Телефон: {data["phone"]}, '
            f'город: {data["city"]}, '
            f'адрес: {data["delivery_address"]}, '
            f'подъезд: {data["entrance"]}\n'
            '\nЭто сообщение было автоматически сгенерировано.')
    return msg


def email_order(data):
    to = data['email']
    subject = 'Ваш заказ на сайте Femas'
    msg = format_consumer_message(data)
    send_mail(
        subject,
        msg,
        mail_from,
        [to]
    )

    to = admin_mail
    subject = 'Через сайт Femas был совершён заказ'
    msg = format_admin_message(data)
    send_mail(
        subject,
        msg,
        mail_from,
        [to]
    )


class CreateRetrieveModelMixin(CreateModelMixin):
    def perform_create(self, serializer):
        # added return
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        retrieve_serializer = self.retrieve_serializer_class(instance)
        email_order(retrieve_serializer.data)

        return Response(retrieve_serializer.data,
                        status=status.HTTP_201_CREATED,
                        headers=headers)


class CreateRetrieveAPIView(CreateRetrieveModelMixin, GenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
