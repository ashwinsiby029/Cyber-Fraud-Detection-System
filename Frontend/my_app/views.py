import requests
from django.shortcuts import render


def submit_fraud_report(request):
    score = None
    error = None
    submitted = False

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        description = request.POST.get("description", "").strip()
        category = request.POST.get("category", "Other")

        if title and description:
            api_url = "http://backend:8000/report/"

            params = {
                "title": title,
                "description": description,
                "category": category,
            }

            try:
                response = requests.post(
                    api_url,
                    params=params,
                    timeout=5
                )

                print("Status Code:", response.status_code)
                print("Response:", response.text)

                if response.status_code == 200:
                    result = response.json()
                    score = result.get("risk_score")
                    submitted = True
                else:
                    error = f"Backend error {response.status_code}: {response.text}"

            except requests.exceptions.ConnectionError:
                error = "❌ Cannot connect to backend. Check Docker networking."

            except requests.exceptions.Timeout:
                error = "⏳ Backend timeout. Try again."

            except Exception as e:
                error = f"⚠ Unexpected error: {str(e)}"

        else:
            error = "⚠ Title and Description are required."

    context = {
        "score": score,
        "error": error,
        "submitted": submitted,
    }

    return render(request, "report_form.html", context)