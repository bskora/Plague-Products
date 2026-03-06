import json
from django.db import models
# from ckeditor.fields import RichTextField
from django_quill.fields import QuillField
from django_quill.quill import QuillParseError

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    body = QuillField(blank=True, null=True)

    @property
    def body_html(self):
        # raw DB value (bypasses descriptor most of the time)
        raw = self.__dict__.get("body", "")

        if raw is None:
            return ""

        # Legacy HTML / plain string
        if isinstance(raw, str):
            s = raw.strip()
            if not s:
                return ""
            try:
                parsed = json.loads(s)
            except json.JSONDecodeError:
                return s  # treat as HTML
            if isinstance(parsed, dict):
                return parsed.get("html") or parsed.get("plain") or ""
            return s

        # If it’s a Quill-ish object, try html safely
        try:
            quill_html = getattr(raw, "html", None)
            if quill_html is not None:
                return quill_html
            return str(raw)
        except QuillParseError:
            # If Quill tries to parse legacy HTML and fails, fall back:
            return "<p>(Invalid Quill content)</p>"

    def __str__(self):
        # return self.title + " | " + str(self.date)
        return self.title + " | " + str(self.date)
