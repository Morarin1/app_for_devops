from rest_framework.serializers import ModelSerializer

from balance.models import Account


class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'first_name', 'last_name')
        read_only_fields = ('id',)
