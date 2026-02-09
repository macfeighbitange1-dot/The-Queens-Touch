from django.shortcuts import render, redirect
from .models import HairStyle, Comment, SiteAnalytics

def home(request):
    # 1. Initialize Analytics and track unique visits
    analytics, created = SiteAnalytics.objects.get_or_create(id=1)
    
    # Check if this is a new session to record a unique visit
    if not request.session.get('has_visited'):
        analytics.total_visits += 1
        analytics.save()
        # Mark the session so we don't count them again until the session expires
        request.session['has_visited'] = True

    # 2. Logic to handle saving a new comment
    if request.method == "POST":
        name = request.POST.get('name')
        message = request.POST.get('message')
        
        if name and message:
            Comment.objects.create(name=name, message=message)
            # Track that a review was successfully submitted
            analytics.review_submissions += 1
            analytics.save()
            return redirect('home')

    # 3. Fetching data for the page
    hairstyles = HairStyle.objects.all().order_by('price')
    comments = Comment.objects.all().order_by('-created_at')

    context = {
        'hairstyles': hairstyles,
        'comments': comments,
        'analytics': analytics  # Pass this to the template if you ever want to see it
    }
    
    return render(request, 'services/index.html', context)

def track_whatsapp(request):
    """
    Increments the click counter before redirecting to WhatsApp.
    Updated with "The Queens Touch" branding.
    """
    analytics, created = SiteAnalytics.objects.get_or_create(id=1)
    analytics.whatsapp_clicks += 1
    analytics.save()
    
    # Redirect to the actual WhatsApp booking link with updated brand message
    whatsapp_url = "https://wa.me/254116248944?text=Hello%20The%20Queens%20Touch,%20I%20would%20like%20to%20make%20an%20inquiry."
    return redirect(whatsapp_url)