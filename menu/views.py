from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import viewsets


from .serializers import *
from .models import *



class MenuCategoryView(viewsets.ModelViewSet):
    queryset= MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer

    # def get_permissions(self):
    #     # Your logic should be all here
    #     if self.request.method == 'GET':
    #         self.permission_classes = [AllowAny, ]
    #     else:
    #         self.permission_classes = [IsAdminUser, ]
    #
    #     return super(MenuCategoryView, self).get_permissions()

class MenuItemView(viewsets.ModelViewSet):
    queryset= MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    # def get_permissions(self):
    #     # Your logic should be all here
    #     if self.request.method == 'GET':
    #         self.permission_classes = [AllowAny, ]
    #     else:
    #         self.permission_classes = [IsAdminUser, ]
    #
    #     return super(MenuItemView, self).get_permissions()



class ShowMenuCategory(APIView):
    def get(self,request):
        query=MenuCategory.objects.all()
        #print(query)
        serializers=MenuCategorySerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)


class AddMenuCategory(APIView):
    def post(self,request):
        serializers=MenuCategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)




class ShowMenuItem(APIView):
    def get(self,request):
        query=MenuItem.objects.all()
        #print(query)
        serializers=MenuItemSerializer(query,many=True,context={ 'request' : request})
        #print(serializers.data)
        return Response(serializers.data,status=status.HTTP_200_OK)



class AddMenuItem(APIView):
    # def get(self,request,pk):
    #     query=MenuCategory.objects.get(pk=pk)
    #     serializers=MenuCategorySerializer(query)
    #     return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request,pk):
        query = MenuCategory.objects.get(pk=pk)
        print(query)
        # dataa=request.data
        # dataa['category']=query
        # print(dataa)

        serializers=MenuItemSerializer(query,data=request.data)
        print(request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)





class MenuList(viewsets.ModelViewSet):
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer


    # def get_permissions(self):
    #     # Your logic should be all here
    #     if self.request.method == 'GET':
    #         self.permission_classes = [IsAuthenticated, ]
    #     else:
    #         self.permission_classes = [IsAdminUser, ]
    #
    #     return super(MenuList, self).get_permissions()


