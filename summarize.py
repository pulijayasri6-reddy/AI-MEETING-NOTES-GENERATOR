def summarize_text(text):
    if not text:
        return "No text to summarize."

    sentences = text.split('.')
    summary = '.'.join(sentences[:2]).strip()

    return summary + "."