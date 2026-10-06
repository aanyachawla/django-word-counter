import re
from django.shortcuts import render

def word_counter(request):
    text = ""
    result = {
        "word_count": 0,
        "character_count": 0,
        "character_no_spaces": 0,
        "sentence_count": 0,
        "paragraph_count": 0,
    }

    if request.method == "POST":
        text = request.POST.get("text", "")
        result["word_count"] = len(text.split())
        result["character_count"] = len(text)
        result["character_no_spaces"] = len(re.sub(r"\s", "", text))
        result["sentence_count"] = len(
            [s for s in re.split(r"[.!?]+", text) if s.strip()]
        )
        result["paragraph_count"] = len(
            [p for p in re.split(r"\n\s*\n", text) if p.strip()]
        )

    return render(
        request,
        "counter/index.html",
        {"text": text, **result}
    )
