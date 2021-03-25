from django.core.mail import send_mail
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

admin_mail = "e.kondr01@gmail.com"
mail_from = 'noreply@e-kondr01.ru'


def email_order(serializer):
    to = serializer.validated_data['email']
    data = serializer.validated_data
    subject = 'Ваш заказ на сайте Femas'
    msg = (f'Уважаемый {data["name"]} {data["surname"]}!\n'
           f'Детали по вашему заказу номер {data["id"]} с сайта Femas:\n'
           f'Общая стоимость заказа: {data["total_price"]}\n'
           f'Состав заказа:\n')
    for product in data["products"]:
        msg += (f'{product.name}, стоимость {product.price}, '
                f'количество {product.quantity}\n')
    for option in data["option"]:
        msg += (f'{option.name}, стоимость {option.price}, '
                f'количество {option.quantity}\n')
    msg += ('Детали доставки\n'
            f'Телефон: {data["phone"]}, '
            f'город: {data["city"]}, '
            f'адрес: {data["delivery_address"]}, '
            f'подъезд: {data["entrance"]}\n'
            '\nЭто сообщение было автоматически сгенерировано.')
    send_mail(
        subject,
        msg,
        mail_from,
        [to]
    )

    to = admin_mail
    subject = 'Через сайт Femas был совершён заказ'
    msg = (
        f'{data["name"]} {data["surname"]}'
        f'оставил заказ на сайте Femas под номером {data["id"]}.\n'
        f'Общая стоимость заказа: {data["total_price"]}\n'
        f'Состав заказа:\n')
    for product in data["products"]:
        msg += (f'{product.name}, стоимость {product.price}, '
                f'количество {product.quantity}\n')
    for option in data["option"]:
        msg += (f'{option.name}, стоимость {option.price}, '
                f'количество {option.quantity}\n')
    msg += ('Детали доставки\n'
            f'Телефон: {data["phone"]}, '
            f'город: {data["city"]}, '
            f'адрес: {data["delivery_address"]}, '
            f'подъезд: {data["entrance"]}\n'
            '\nЭто сообщение было автоматически сгенерировано.')
    send_mail(
        subject,
        msg,
        mail_from,
        [to]
    )


class CreateRetrieveModelMixin(CreateModelMixin):
    def perform_create(self, serializer):
        #res = serializer.save()
        # email_order(serializer)
        return serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        serializer = self.retrieve_serializer_class(instance)
        #  email_order(serializer)

        return Response(serializer.data, status=status.HTTP_201_CREATED,
                        headers=headers)


class CreateRetrieveAPIView(CreateRetrieveModelMixin, GenericAPIView):

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
