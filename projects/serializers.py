from rest_framework import serializers
from .models import Project
import re

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

    def validate_projectName(self, value):
        if not re.match(r"^[A-Za-z0-9_-]+$", value):
            raise serializers.ValidationError("Only letters, digits, hyphen, underscore allowed")
        if len(value) < 4 or len(value) > 30:
            raise serializers.ValidationError("Length must be 4–30 characters")
        return value
