======
Oreille
======


.. image:: https://img.shields.io/pypi/v/oreille.svg
        :target: https://pypi.python.org/pypi/oreille


Oreille is a wrapper on OpenAPI Whisper API. It provides support for long audio files.


OpenAPI Whisper support only files that are less than 25 MB. Oreille will break the audio file into chunks of 25 MB's or less.
https://platform.openai.com/docs/guides/speech-to-text/longer-inputs

Oreille will also compute the correct timing of the subtitle when merging the output of Whisper. So once you export the subtitle the timestamp of the subtitle will be right.

You can open and save WAV files with pure python. For opening and saving non-wav files – like mp3 – you'll need ffmpeg or libav.


Features
--------

* Mostly Drop-in replacement to the OpenAPI *audio.transcriptions.create*
* Support for large audio file
* Export as text, srt, vtt, json

Usage
-----

You need to set your OPENAI_API_KEY environment variable first.

.. code-block:: bash
        
        export OPENAI_API_KEY=sk-xxxxx
        pip install oreille


Then you can use it like this:

.. code-block:: python
        
        import openai

        import oreille

        client = openai.OpenAI()

        print("Processing wav")
        print(
        oreille.transcribe(
                client,
                file=open("examples/test.wav", "rb"),
                model="whisper-1",
                language="fr",
                prompt="Test son",
                response_format="verbose_json",
                audio_format="wav",
        )
        )

See more examples in the examples directory.

License
--------
Free software: Apache Software License 2.0


FAQ
----

Why Oreille?
************

Oreille is the french word for ear. The original author of Oreille is french.


