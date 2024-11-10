def segments_to_vtt(segments):
    """
    Convert a list of segments to a VTT text

    :param list segments: list of OpenAI segments
    :return str: VTT text
    """
    out = "WEBVTT\n\n"
    for segment in segments:
        out += f"{segment.id}\n"
        out += f"{_seconds_to_vtt_time(segment.start)} --> {_seconds_to_vtt_time(segment.end)}\n"
        out += f"{segment.text}\n\n"

    return out


def _seconds_to_vtt_time(seconds):
    # Output format: 00:00:00,000
    return f"{int(seconds // 3600):02}:{int(seconds // 60):02}:{(seconds % 60):06.3f}"


def segments_to_srt(segments):
    """
    Convert a list of segments to a SRT text

    :param list segments: list of OpenAI segments
    :return str: SRT text
    """
    out = ""
    for segment in segments:
        out += f"{segment.id}\n"
        out += f"{_seconds_to_srt_time(segment.start)} --> {_seconds_to_srt_time(segment.end)}\n"
        out += f"{segment.text}\n\n"

    return out


def _seconds_to_srt_time(seconds):
    # Output format: 00:00:00,000
    # The comma is used to separate the fractional part from the integer part of the second.
    return f"{int(seconds // 3600):02}:{int(seconds // 60):02}:{(seconds % 60):06.3f}".replace(
        ".", ","
    )
