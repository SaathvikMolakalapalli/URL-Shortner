import qrcode
import io
import base64
from django.shortcuts import render, redirect, get_object_or_404
from .models import URL

def home(request):
    short_url = None
    error = None
    qr_code_base64 = None

    try:
        if request.method == 'POST':
            long_url = request.POST.get('long_url', '').strip()
            custom_code = request.POST.get('custom_code', '').strip()

            if not long_url:
                raise ValueError("Please enter a URL.")

            if custom_code:
                if URL.objects.filter(short_code=custom_code).exists():
                    raise ValueError("This custom code is already taken!")
                obj, created = URL.objects.get_or_create(original_url=long_url, short_code=custom_code)
            else:
                obj, created = URL.objects.get_or_create(original_url=long_url)

            short_url = request.build_absolute_uri('/') + obj.short_code

            # Generate QR code for the shortened URL
            qr = qrcode.QRCode(box_size=6, border=2)
            qr.add_data(short_url)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Convert QR code image to base64 for HTML embedding
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()

    except Exception as e:
        import traceback
        print("ERROR:", e)
        traceback.print_exc()
        error = str(e)

    last_urls = URL.objects.order_by('-created_at')[:5]

    return render(request, 'shortener/home.html', {
        'short_url': short_url,
        'error': error,
        'last_urls': last_urls,
        'qr_code_base64': qr_code_base64
    })


def redirect_url(request, code):
    url_obj = get_object_or_404(URL, short_code=code)
    url_obj.visits += 1
    url_obj.save()
    return redirect(url_obj.original_url)
