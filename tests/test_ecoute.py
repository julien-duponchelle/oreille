#!/usr/bin/env python

"""Tests for `ecoute` package."""

import pytest
import pydub
import openai
from openai.openai_object import OpenAIObject
from unittest.mock import ANY

import ecoute


@pytest.fixture
def empty_audio(tmp_path, scope="module"):
    """
    An empty audio file
    """
    with open(tmp_path / "empty.wav", "wb+") as f:
        empty_audio = pydub.AudioSegment.silent(1)
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

@pytest.fixture
def openai_object():
    result = OpenAIObject(response_ms=100)
    result.text = "Hello World"
    return result

def test_transcribe_verbose_json(mocker, empty_audio, openai_object):
    mocker.patch("openai.Audio.transcribe", return_value=openai_object)

    transcribe = ecoute.transcribe(
        "whisper-1", empty_audio, response_format="verbose_json")

    openai.Audio.transcribe.assert_called_with(
        "whisper-1", ANY, response_format="verbose_json")
    assert transcribe.text == "Hello World"
    assert transcribe.response_ms == 100


def test_transcribe_text(mocker, empty_audio, openai_object):
    mocker.patch("openai.Audio.transcribe", return_value=openai_object)

    transcribe = ecoute.transcribe(
        "whisper-1", empty_audio, response_format="text")

    openai.Audio.transcribe.assert_called_with(
        "whisper-1", ANY, response_format="verbose_json")
    assert transcribe.text == "Hello World"
    assert transcribe.response_ms == 100

def test_transcribe_text_long(mocker, long_empty_audio):
    o1 = OpenAIObject(response_ms=100)
    o1.text = "Hello World"
    o2 = OpenAIObject(response_ms=200)
    o2.text = "Bonjour le monde"
    mocker.patch("openai.Audio.transcribe", side_effect=[o1, o2])

    transcribe = ecoute.transcribe(
        "whisper-1", long_empty_audio, response_format="text")

    assert transcribe.text == "Hello World Bonjour le monde"
    assert transcribe.response_ms == 300