#!/usr/bin/env python

"""Tests for `ecoute` package."""

import pytest
import pydub
import openai
from openai.openai_object import OpenAIObject

from ecoute import ecoute


@pytest.fixture
def empty_audio(tmp_path, scope="module"):
    """
    An empty audio file
    """
    with open(tmp_path / "empty.wav", "wb+") as f:
        empty_audio = pydub.AudioSegment.empty()
        empty_audio.export(f, format="wav")
    return tmp_path / "empty.wav"


@pytest.fixture
def long_empty_audio(tmp_path, scope="module"):
    """
    An audio file of 11 minutes
    """
    with open(tmp_path / "long_empty.wav", "wb+") as f:
        empty_audio = pydub.AudioSegment.silent(11 * 60 * 1000)
        empty_audio.export(f, format="wav")
    return tmp_path / "long_empty.wav"


def test_transcribe_json(mocker, empty_audio):
    result = OpenAIObject(response_ms=100)
    result.text = "Hello World"

    mocker.patch("openai.Audio.transcribe", return_value=result)

    transcribe = ecoute.transcribe(
        "whisper-1", empty_audio, response_format="json")

    openai.Audio.transcribe.assert_called_with(
        "whisper-1", empty_audio, response_format="json")
    assert transcribe.text == "Hello World"
    assert result.response_ms == 100


def test_transcribe_text(mocker, empty_audio):
    mocker.patch("openai.Audio.transcribe", return_value="Hello World")

    transcribe = ecoute.transcribe(
        "whisper-1", empty_audio, response_format="text")

    openai.Audio.transcribe.assert_called_with(
        "whisper-1", empty_audio, response_format="text")
    assert transcribe == "Hello World"


def test_transcribe_text_long(mocker, long_empty_audio):
    o1 = OpenAIObject(response_ms=100)
    o1.text = "Hello World"
    o2 = OpenAIObject(response_ms=200)
    o2.text = "Bonjour le monde"
    mocker.patch("openai.Audio.transcribe", side_effect=[o1, o2])

    transcribe = ecoute.transcribe(
        "whisper-1", long_empty_audio, response_format="text")

    assert transcribe == "Hello World Bonjour le monde"
