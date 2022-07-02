# from rest_framework import generics
#
# from balance.models import Account
# from balance.serializers import AccountSerializer
#
#
# class AccountList(generics.ListCreateAPIView):
#     """Get a list, put and patch are not allowed"""
#     # authentication_classes = (TokenAuthentication,)
#     # permission_classes = (IsAuthenticated,)
#     queryset = Account.objects.all()
#     serializer_class = AccountSerializer
#
#     def perform_create(self, serializer):
#         """Create a new account"""
#         serializer.save(user=self.request.user)
#
#     def get_queryset(self):
#         """Return object for current authenticated user only"""
#         return self.queryset.filter(user=self.request.user)
