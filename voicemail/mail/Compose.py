from TextToSpeech import TextToSpeech
from Audio import Audio
from SpeechToText import SpeechToText
from config import LanguageConfig

from difflib import SequenceMatcher


class Compose:

    def __init__(self, language=LanguageConfig.speech_to_text_english):
        self.subject = ''
        self.body = ''
        self.language = language
        self.options = ["retry", "continue", "append"]

        print("What is the Subject of this e-mail?")
        TextToSpeech("What is the Subject of this e-mail?").speak_out_loud()
        self.prepare_subject()

        print("What is the body of the email?")
        TextToSpeech("What is the body of the email?").speak_out_loud()
        self.get_user_input_for_body()
        self.validate_email()

    def prepare_subject(self):
        self.get_user_input_for_subject()

    def get_user_input_for_subject(self):
        response = self.get_text_response_via_speech_recognition()
        print("You said : " + str(response))
        TextToSpeech("You said : " + str(response)).speak_out_loud()
        self.validate_choice_for_subject(response)

    def validate_choice_for_subject(self, response):
        print("Do you want to continue? retry? append?")
        TextToSpeech("Do you want to continue? retry? append?").speak_out_loud()
        choice = self.get_text_response_via_speech_recognition()
        if choice is None:
            self.validate_choice_for_subject(response)
        else:
            validated_choice = self.validate_choice_of_subject_for(choice)
            if validated_choice is True:
                choice = self.similar(choice)
                self.take_action_for_subject_on(choice, response)
            if validated_choice is False:
                print("Invalid choice :" + choice)
                self.validate_choice_for_subject(response)

    def get_user_input_for_body(self):
        response = self.get_text_response_via_speech_recognition()
        print("You said : " + response)
        TextToSpeech("You said : " + response).speak_out_loud()
        self.validate_choice_for_body(response)

    def validate_choice_for_body(self, response):
        print("Do you want to continue? retry? append?")
        TextToSpeech("Do you want to continue? retry? append?").speak_out_loud()
        choice = self.get_text_response_via_speech_recognition()
        if choice is None:
            TextToSpeech("I didn't get what you said, Say again").speak_out_loud()
            print("I didn't get what you said, Say again")
            self.validate_choice_for_body(response)
        else:
            validated_choice_boolean = self.validate_choice_of_body_for(choice)
            if validated_choice_boolean is True:
                choice = self.similar(choice)
                validated_choice_boolean = self.take_action_for_body_on(choice, response)
            if validated_choice_boolean is False:
                TextToSpeech("I didn't get what you said, Say again").speak_out_loud()
                print("I didn't get what you said, Say again")
                self.validate_choice_for_body(response)

    def get_text_response_via_speech_recognition(self):
        response = SpeechToText(Audio().record(), language=self.language).convert_to_text()
        if isinstance(response, str) and not None:
            return response.strip()
        print("Something went wrong, retrying.")
        self.get_text_response_via_speech_recognition()

    def validate_choice_of_subject_for(self, choice):
        # if choice.strip().lower() in self.options:
        #     return True
        # return False
        if self.similar(choice) is not False:
            return True
        return False

    def take_action_for_subject_on(self, choice, response):
        if choice == "retry":
            self.get_user_input_for_subject()
        elif choice == "continue":
            self.subject += response
            return
        elif choice == "append":
            self.subject += response
            self.get_user_input_for_subject()

    def validate_choice_of_body_for(self, choice):
        return self.validate_choice_of_subject_for(choice)

    def take_action_for_body_on(self, choice, response):
        if choice == "retry":
            self.get_user_input_for_body()
        elif choice == "continue":
            self.body += response
            return
        elif choice == "append":
            self.body += response
            self.get_user_input_for_body()
        else:
            return False

    def validate_email(self):
        print("Before sending the email do you want to listen it out? Say yes or no")
        TextToSpeech("Before sending the email do you want to listen it out? Say yes or no").speak_out_loud()
        bool_response = self.get_boolean_response()
        if self.validate_choice_for_confirmation(bool_response) is True:
            print("Subject is :")
            TextToSpeech("Subject is : " + self.subject, language=self.language).speak_out_loud()
            print("Body is :")
            TextToSpeech("Body is :" + self.body, language=self.language).speak_out_loud()

    def validate_choice_for_confirmation(self, bool_response):
        if bool_response is not None:
            if bool_response.lower() == "yes":
                return True
            elif bool_response.lower() == "no":
                return False
        print("I didn't get what you said, Say again")
        TextToSpeech("I didn't get what you said, Say again").speak_out_loud()
        self.validate_choice_for_confirmation(self.get_boolean_response())

    def get_boolean_response(self):
        response = self.get_text_response_via_speech_recognition()
        if response.lower() in ["yes", "no"]:
            return response
        self.get_boolean_response()

    def similar(self, choice):
        for option in self.options:
            if SequenceMatcher(None, choice, option).ratio() > 0.6:
                return option
        return False
