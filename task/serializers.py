from rest_framework import serializers
from task.models import Task


# class TaskSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Task
#         fields = '__all__'
#         read_only_fields = ('created_at', 'updated_at')

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, required=False)
    due_date = serializers.DateTimeField(required=False)
    completed = serializers.BooleanField(default=False)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)


class UpdateTaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(allow_blank=True, required=False)
    due_date = serializers.DateTimeField(required=False)
    completed = serializers.BooleanField(default=False)


    def validate_completed(self, value):
        if value and not self.initial_data.get('due_date'):
            raise serializers.ValidationError("Completed cannot be without due_date")
        return value

    def create(self, validated_data):
        task = Task.objects.create(
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            due_date=validated_data.get('due_date'),
            completed=validated_data.get('completed')
        )
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.due_date = validated_data.get('due_date', instance.due_date)
        instance.completed = validated_data.get('completed', instance.completed)
        instance.save()
        return instance