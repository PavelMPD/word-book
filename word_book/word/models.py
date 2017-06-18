from django.db import models
from django.utils.translation import ugettext_lazy as _


class Word(models.Model):
    name = models.CharField(
        verbose_name=_("Word"), max_length=1024, primary_key=True)


class SpeechPart(models.Model):
    NOUN = "noun"
    PRONOUN = "pronoun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"
    PREPOSITION = "preposition"
    CONJUNCTION = "conjunction"
    INTERJECTION = "interjection"

    TYPE_CHOICES = (
        (NOUN, _("Noun")),
        (PRONOUN, _("Pronoun")),
        (VERB, _("Verb")),
        (ADJECTIVE, _("Adjective")),
        (ADVERB, _("Adverb")),
        (PREPOSITION, _("Preposition")),
        (CONJUNCTION, _("Conjuction")),
        (INTERJECTION, _("Interjection"))
    )

    name = models.CharField(
        verbose_name=_("Part of Speech"), max_length=50, blank=False,
        choices=TYPE_CHOICES)
    word = models.ForeignKey(to="Word", on_delete=models.CASCADE, blank=False)

    class Meta:
        unique_together = ("name", "word")


class Meaning(models.Model):
    value = models.TextField(verbose_name="Meaning", blank=False)
    speech_part = models.ForeignKey(
        to="SpeechPart", on_delete=models.CASCADE, blank=False)
