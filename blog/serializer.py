from rest_framework import serializers
from .models import SavedEmbeds


class EmbedSerializer(serialisers.ModelSerializer):
	class Meta:
		model = SavedEmbeds




