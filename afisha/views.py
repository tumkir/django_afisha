from django.http import HttpResponse


def blank_start_page(request):
    http_code = """<!DOCTYPE html>
<html>
<head>
  <title>Стартовая</title>
</head>
<body>
  <h1>Здесь будет карта</h1>
</body>
</html>"""

    return HttpResponse(http_code)
