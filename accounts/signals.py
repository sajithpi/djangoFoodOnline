from . models import User, UserProfile
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


@receiver(post_save, sender = User)    
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("created user profile")
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print("User is updated")
        except:
            UserProfile.objects.create(user=instance)
            print("User profile does't exist, created profile")
            
@receiver(pre_save, sender = User)
def pre_save_user(sender, instance, **kwargs):
    print(f"{instance.username} User is being created")