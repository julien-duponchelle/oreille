#!/usr/bin/env python

"""Tests for `oreille` package."""

from unittest.mock import Mock

import pydub
import pytest
from openai.types.audio.transcription_segment import TranscriptionSegment
from openai.types.audio.transcription_verbose import TranscriptionVerbose

from oreille import oreille


@pytest.fixture
def openai_client():
    return Mock()


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
    result = TranscriptionVerbose(
        text="Hello World",
        duration="10",
        language="en",
    )
    result.segments = [
        TranscriptionSegment(
            id= 0,
            seek= 0,
            start= 0.0,
            end= 2.8000000000000003,
            text= "Hello",
            tokens= [50364, 8257, 53],
            temperature= 0.0,
            avg_logprob= -0.32106150751528534,
            compression_ratio= 0.9402985074626866,
            no_speech_prob= 0.03250369429588318,
        ),
        TranscriptionSegment(
            id= 1,
            seek= 0,
            start= 2.9,
            end= 3.5,
            text= "world",
            tokens= [50364, 8257, 53],
            temperature= 0.0,
            avg_logprob= -0.32106150751528534,
            compression_ratio= 0.9402985074626866,
            no_speech_prob= 0.03250369429588318,
        ),
    ]
    return result


@pytest.fixture
def openai_object2():
    result = TranscriptionVerbose(
        text="Bonjour le monde",
        duration="10",
        language="en",
    )
    result.segments = [
        TranscriptionSegment(
            id= 0,
            seek= 0,
            start= 0.0,
            end= 2.8000000000000003,
            text= "Bonjour",
            tokens= [50364, 8257, 53],
            temperature= 0.0,
            avg_logprob= -0.32106150751528534,
            compression_ratio= 0.9402985074626866,
            no_speech_prob= 0.03250369429588318,
        ),
        TranscriptionSegment(
            id= 1,
            seek= 0,
            start= 2.9,
            end= 3.5,
            text= "le monde",
            tokens= [50364, 8257, 53],
            temperature= 0.0,
            avg_logprob= -0.32106150751528534,
            compression_ratio= 0.9402985074626866,
            no_speech_prob= 0.03250369429588318,
        ),
    ]
    return result


def test_transcribe_verbose_json(openai_client, mocker, empty_audio, openai_object):
    openai_client.audio.transcriptions.create.return_value = openai_object
    transcribe = oreille.transcribe(
        openai_client,
        empty_audio,
        "whisper-1", response_format="verbose_json"
    )

    assert isinstance(transcribe, TranscriptionVerbose)
    assert transcribe.text == "Hello World"
    assert transcribe.segments == openai_object.segments
    assert transcribe.duration == "10"


def test_transcribe_verbose_json_long(openai_client,
    mocker, long_empty_audio, openai_object, openai_object2
):
    openai_client.audio.transcriptions.create.side_effect = [openai_object, openai_object2]

    transcribe = oreille.transcribe(
        openai_client, long_empty_audio, model="whisper-1", response_format="verbose_json"
    )
    assert isinstance(transcribe, TranscriptionVerbose)
    assert transcribe.text == "Hello World Bonjour le monde"
    assert transcribe.segments is not None
    assert len(transcribe.segments) == 4
    assert transcribe.segments[0].id == 0
    assert transcribe.segments[0].start == 0
    assert transcribe.segments[0].end == 2.8000000000000003
    assert transcribe.segments[2].id == 2
    assert transcribe.segments[2].start == 600
    assert transcribe.segments[2].end == 602.8
    assert transcribe.segments[3].id == 3
    assert transcribe.segments[3].start == 602.9
    assert transcribe.segments[3].end == 603.5
    assert transcribe.duration == "20.0"


def test_transcribe_text(openai_client, mocker, empty_audio, openai_object):
    openai_client.audio.transcriptions.create.return_value = openai_object

    transcribe = oreille.transcribe(openai_client,  empty_audio, model="whisper-1", response_format="text")
    assert transcribe == "Hello World"


def test_transcribe_text_long(openai_client, mocker, long_empty_audio):
    o1 = TranscriptionVerbose(text="Hello World", duration="25", language="en")
    o2 = TranscriptionVerbose(text="Bonjour le monde", duration="15", language="fr")
    openai_client.audio.transcriptions.create.side_effect=[o1, o2]

    transcribe = oreille.transcribe(
        openai_client,
        long_empty_audio, model="whisper-1", response_format="text"
    )

    assert transcribe == "Hello World Bonjour le monde"
