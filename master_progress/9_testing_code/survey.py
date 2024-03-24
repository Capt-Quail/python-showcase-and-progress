# Testing classes classes similar to testing functions, but with distinct
# differences. We'll build it out for example.
class AnonymousSurvey:
    """Collect anynymous answers to a survey question."""

    def __init__(self, question):
        """store a question, and prepare to store response."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")