import pytest
from openai.types.audio.transcription_segment import TranscriptionSegment
from openai.types.audio.transcription_verbose import TranscriptionVerbose

import oreille.export


@pytest.fixture
def openai_object():
    result = TranscriptionVerbose(
        duration="15",
        language="en",
        text="Hello World"
    )
    result.segments = [
        TranscriptionSegment(
           id=0,
           seek=0,
           start=0.0,
           end=2.8000000000000003,
           text="Hello",
           tokens=[50364, 8257, 53],
           temperature=0.0,
           avg_logprob=-0.32106150751528534,
           compression_ratio=0.9402985074626866,
           no_speech_prob=0.03250369429588318,
        ),
        TranscriptionSegment(
           id=1,
           seek=0,
           start=2.9,
           end=3.5,
           text="world",
           tokens=[50364, 8257, 53],
           temperature=0.0,
           avg_logprob=-0.32106150751528534,
           compression_ratio=0.9402985074626866,
           no_speech_prob=0.03250369429588318,
        )
    ]
    return result


def test_segment_to_vtt(openai_object):
    segments = [
        TranscriptionSegment(
           id=0,
           start=0.0,
           seek=0,
           tokens=[50364, 8257, 53],
           end=2.8000000000000003,
           text="Hello World",
           temperature=0.0,
           avg_logprob=-0.32106150751528534,
           compression_ratio=0.9402985074626866,
           no_speech_prob=0.03250369429588318,
        ),
        TranscriptionSegment(
           id=1,
           start=2.9,
           end=3.5,
           text="Bonjour le monde",
           temperature=0.0,
           seek=0,
           tokens=[50364, 8257, 53],
           avg_logprob=-0.32106150751528534,
           compression_ratio=0.9402985074626866,
           no_speech_prob=0.03250369429588318,
        ),
    ]

    vtt = oreille.export.segments_to_vtt(segments)
    assert (
        vtt
        == """WEBVTT

0
00:00:00.000 --> 00:00:02.800
Hello World

1
00:00:02.900 --> 00:00:03.500
Bonjour le monde

"""
    )


def test_segment_to_srt(openai_object):
    segments = [
        TranscriptionSegment(
           id=0,
           start=0.0,
           end=2.8000000000000003,
           text="Hello World",
           temperature=0.0,
           seek=0,
           tokens=[50364, 8257, 53],
           avg_logprob=-0.32106150751528534,
           compression_ratio=0.9402985074626866,
           no_speech_prob=0.03250369429588318,
        ),
        TranscriptionSegment(
           id=1,
           start=2.9,
           end=3.5,
           text="Bonjour le monde",
           temperature=0.0,
           seek=0,
           tokens=[50364, 8257, 53],
           avg_logprob=-0.32106150751528534,
           compression_ratio=0.9402985074626866,
           no_speech_prob=0.03250369429588318,
        ),
    ]

    vtt = oreille.export.segments_to_srt(segments)
    assert (
        vtt
        == """0
00:00:00,000 --> 00:00:02,800
Hello World

1
00:00:02,900 --> 00:00:03,500
Bonjour le monde

"""
    )
