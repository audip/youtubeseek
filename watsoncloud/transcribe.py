import sys
from watsoncloud.foo import high as high_foo
from watsoncloud.foo.project_settings import get_watson_creds, does_project_exist, project_dir, make_slug_from_path


def speech_to_text(filepath):
    pslug = make_slug_from_path(filepath.strip())
    if not does_project_exist(pslug):
        raise NameError(project_dir(pslug) + " does not exist")
    # transcribes audio
    print("Transcribing in progress")
    high_foo.transcribe_audio(pslug, creds=get_watson_creds())
    print("Transcribing complete")
