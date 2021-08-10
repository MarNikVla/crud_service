from rest_framework import serializers

from companies.models import Company


class AdminCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # image field exclude
        exclude = ['avatar']


class ModeratorCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # image field exclude
        exclude = ['avatar']
        read_only_fields = ['id', 'title', ]


class UserCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        # image field exclude
        exclude = ['avatar']
        read_only_fields = ['id', 'title', 'description', 'foundation_date', 'avatar', ]
