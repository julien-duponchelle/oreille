import openai


def transcribe(model, audio_file, response_format="json", **kwargs):
    """
    Transcribe the audio content to text.
    All arguments of openai.Audio.transcribe are supported

    :param file: The audio file object (not file name) to transcribe, in one of these formats: mp3, mp4, mpeg, mpga, m4a, wav, or webm.
    :param model: ID of the model to use.
    :param prompt: An optional text to guide the model's style or continue a previous audio segment. The prompt should match the audio language.
    :param response_format: The format of the transcript output, in one of these options: json, text, srt, verbose_json, or vtt. (default json)
    :param language: The language of the input audio. Supplying the input language in ISO-639-1 format will improve accuracy and latency.
    """
    return openai.Audio.transcribe(model, audio_file, response_format=response_format, **kwargs)
