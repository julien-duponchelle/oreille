======
Écoute
======


.. image:: https://img.shields.io/pypi/v/ecoute.svg
        :target: https://pypi.python.org/pypi/ecoute


Écoute is a wrapper on OpenAPI Whisper API. It's provide support for long audio files.


OpenAPI Whisper support only files that are less than 25 MB. Écoute will break the audio file into chunks of 25 MB's or less.
https://platform.openai.com/docs/guides/speech-to-text/longer-inputs

Écoute will also fixe the timing of the subtitle. So once you export the subtitle the timestamp of the subtitle will be right.

You can open and save WAV files with pure python. For opening and saving non-wav files – like mp3 – you'll need ffmpeg or libav.

* Free software: Apache Software License 2.0


Features
--------

* Drop-in replacement to the OpenAPI *openai.Audio.transcribe*
* Support for large audio file
* Export as text, srt, vtt, json

Usage
-----

You need to set your OPENAI_API_KEY environment variable first.

.. code-block:: bash
    export OPENAI_API_KEY=sk-xxxxx
    pip install ecoute

.. code-block:: python
        import ecoute

        print(ecoute.transcribe("whisper-1", open("examples/test.wav", "rb"), language="fr",
                prompt="Test son", response_format="verbose_json", audio_format="wav"))


See more examples in the examples directory.

FAQ
----

Why Écoute?
************

Écoute is the french word for listen. The original author of Écoute is french.

Do I need to write Écoute with the accent? 
******************************************

No, it's the correct spelling but you can write Écoute, it's easier to type.


