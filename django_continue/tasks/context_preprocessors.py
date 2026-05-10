
# core/context_processors.py

def global_data(request):
    return {
        "site_name": "My Portfolio",
        "year": 2026,
    }