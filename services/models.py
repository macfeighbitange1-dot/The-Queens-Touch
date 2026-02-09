from django.db import models

class HairStyle(models.Model):
    """
    Represents a specific hair service offered by The Queens Touch.
    Includes pricing, description, and visual representation.
    """
    title = models.CharField(max_length=100, unique=True)
    price = models.IntegerField(help_text="Price in Kenyan Shillings (KES)")
    description = models.TextField(
        blank=True, 
        help_text="Details about the service (e.g., duration, requirements)"
    )
    image = models.ImageField(
        upload_to='hairstyles/', 
        blank=True, 
        null=True,
        help_text="Upload a professional photo of this style"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['price'] 
        verbose_name = "Hair Style"
        verbose_name_plural = "Hair Styles"

    def __str__(self):
        return f"{self.title} — KES {self.price}"

class Comment(models.Model):
    """
    Stores customer reviews and comments left on The Queens Touch website.
    """
    name = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Customer Review"
        verbose_name_plural = "Customer Reviews"

    def __str__(self):
        return f"Comment by {self.name} on {self.created_at.strftime('%Y-%m-%d')}"

class SiteAnalytics(models.Model):
    """
    A single-row model to track key performance indicators (KPIs) 
    for The Queens Touch website.
    """
    total_visits = models.PositiveIntegerField(default=0)
    whatsapp_clicks = models.PositiveIntegerField(default=0)
    review_submissions = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Site Analytics"
        verbose_name_plural = "Site Analytics"

    def __str__(self):
        return f"Analytics (Visits: {self.total_visits}, Clicks: {self.whatsapp_clicks})"