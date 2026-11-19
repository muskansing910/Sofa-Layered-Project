from model.feedback import Feedback
from dao.feedback_dao import FeedbackDAO


class FeedbackService:

    def __init__(self):
        self.feedback_dao = FeedbackDAO()

    def add_feedback(self, feedback_id, work_order_id, rating, comment):

        feedback = Feedback(
            feedback_id,
            work_order_id,
            rating,
            comment
        )

        self.feedback_dao.add_feedback(feedback)

    def display_all(self):
        feedbacks = self.feedback_dao.display_all()

        for feedback in feedbacks:
            print("----------------------------------------")
            print("Feedback ID   :", feedback.feedback_id)
            print("Work Order ID :", feedback.work_order_id)
            print("Rating        :", feedback.rating)
            print("Comment       :", feedback.comment)

        return feedbacks
    def display_by_customer_id(self, customer_id):

        feedbacks = self.feedback_dao.display_by_customer_id(
            customer_id
        )

        return feedbacks
 
    def update_feedback(self, feedback_id, rating, comment):
        self.feedback_dao.update_feedback(
            feedback_id,
            rating,
            comment
        )

    def delete_feedback(self, feedback_id):
        self.feedback_dao.delete_feedback(feedback_id)