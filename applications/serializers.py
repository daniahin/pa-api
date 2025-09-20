from rest_framework import serializers
from .models import Application, CONTACT_CHOICES, TECH_CHOICES

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

    def validate_contactMethod(self, value):
        choices = [c[0] for c in CONTACT_CHOICES]
        if value not in choices:
            raise serializers.ValidationError(f'contactMethod має бути одним із {choices}')
        return value

    def validate(self, data):
        method = data.get('contactMethod')
        # Перевірка залежних полів
        if method == 'phone' and not data.get('phone'):
            raise serializers.ValidationError({'phone': 'Обов’язково якщо contactMethod=phone'})
        if method == 'email' and not data.get('email'):
            raise serializers.ValidationError({'email': 'Обов’язково якщо contactMethod=email'})
        if method == 'telegram' and not data.get('telegram'):
            raise serializers.ValidationError({'telegram': 'Обов’язково якщо contactMethod=telegram'})

        # Валідація technologies
        techs = data.get('technologies') or []
        if not (1 <= len(techs) <= 3):
            raise serializers.ValidationError({'technologies': '1–3 items required'})
        allowed = [c[0] for c in TECH_CHOICES]
        for t in techs:
            if t not in allowed:
                raise serializers.ValidationError({'technologies': f'“{t}” не в {allowed}'})
            if not (3 <= len(t) <= 50):
                raise serializers.ValidationError({'technologies': 'Length each 3–50'})
        return data
