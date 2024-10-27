class AITutor:
    def __init__(self, user):
        self.user = user

    def provide_feedback(self, answer, correct_answer):
        if answer == correct_answer:
            return "Great job!"
        else:
            return "Try again!"
