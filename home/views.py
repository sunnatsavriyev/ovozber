from rest_framework import permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied ,ValidationError
from django.db.models import Count
from .models import OvozModel
from .serializers import OvozSerializer

class OvozApiView(ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = OvozSerializer
    queryset = OvozModel.objects.all()

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            vote_user = serializer.validated_data['user']
            if vote_user == self.request.user:
                raise ValidationError("Siz o'zingizga ovoz beraolmaysiz.")
            
            # Save the vote for the selected user
            serializer.save(user=vote_user)
        else:
            raise PermissionDenied("Ovoz berish uchun tizimga kiring.")

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
        if request.user.is_authenticated:
            # Hozirgi foydalanuvchiga tegishli ovozlar sonini hisoblash
            user_vote_count = OvozModel.objects.filter(user=request.user).count()
            
            # Har bir foydalanuvchi uchun ovozlar sonini hisoblash
            user_vote_counts = OvozModel.objects.values('user__username').annotate(ovozlar_soni=Count('user')).order_by('-ovozlar_soni')
            
            # Natijani qaytarish
            response.data = {
                "sizga ovoz berganlar": user_vote_count,
                "umumiy": user_vote_counts
            }
        else:
            # Autentifikatsiya qilinmagan foydalanuvchilar uchun faqat umumiy ovozlar
            response.data = {
                "umumiy": response.data
            }
        
        return response



class OvozDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = OvozSerializer

    def get_queryset(self):
        return OvozModel.objects.filter(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        vote_count = OvozModel.objects.filter(user=request.user).count()
        response_data = serializer.data
        response_data['sizga ovoz berganlar'] = vote_count
        return Response(response_data)