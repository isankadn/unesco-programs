from django.db import models
from django.utils.text import slugify
from opaque_keys.edx.django.models import CourseKeyField
from organizations.models import Organization
from django.utils.translation import gettext_lazy as _
from openedx.core.djangoapps.content.course_overviews.models import CourseOverview

class UnescoProgram(models.Model):
    class Meta:
        permissions = [
            ("can_add_program", "Can add program"),
            ("can_edit_program", "Can edit program"),
        ]
        
    name = models.CharField(max_length=255, blank=False, null=True, default=None, help_text='Name of the program', unique=True)  
    slug = models.SlugField(unique=True, blank=True, help_text='Auto-generated slug for the program') 
    organizations = models.ManyToManyField(Organization, blank=True,
                                           help_text=_("Organizations under which the program is allowed"))
    courses = models.ManyToManyField(CourseOverview, blank=True,
                                     help_text=_("Courses that are part of the program"), related_name='unesco_programs', 
                                     related_query_name='unesco_program', db_table='unesco_programs_program_courses')
    description = models.TextField(max_length=500, blank=True, null=True, default=None, help_text='Description of the program')
    banner_image = models.ImageField(upload_to='program_banners/')

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from the name
            original_slug = slugify(self.name)
            queryset = UnescoProgram.objects.all()
            new_slug = original_slug
            counter = 1
            
            # Ensure the slug is unique
            while queryset.filter(slug=new_slug).exists():
                new_slug = "{}-{}".format(original_slug, counter)
                counter += 1
                
            self.slug = new_slug
            
        super(UnescoProgram, self).save(*args, **kwargs)