from rest_framework.serializers import ModelSerializer

from balance.serializers import AccountSerializer
from marketplace.models import Post, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PostSerializer(ModelSerializer):
    account = AccountSerializer()
    product = ProductSerializer()

    class Meta:
        model = Post
        exclude = ('description',)
        read_only_fields = ('id',)

    def create(self, validated_data):
        post = Post.objects.update_or_create(
            product=validated_data.get('product')

        )