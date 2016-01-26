
from decimal import Decimal


def get_match(user_a, user_b):
    a = user_a.useranswer_set.all().values_list("question")
    b = user_b.useranswer_set.all().values_list("question")
    matches_b = user_b.useranswer_set.filter(question=a).order_by("question")
    matches_a = user_a.useranswer_set.filter(question=b).order_by("question")
    questions_match_num = matches_b.count()
    if questions_match_num:
        a_points = 0
        b_points = 0
        a_total_points = 0
        b_total_points = 0
        for question_a, question_b in zip(matches_a, matches_b):
            if question_b.their_answer == question_a.my_answer:
                a_points += question_b.their_points
            a_total_points += question_b.their_points
            if question_a.their_answer == question_b.my_answer:
                b_points += question_a.their_points
            b_total_points += question_a.their_points
        if a_total_points == 0:
            a_decimal = 0.000001
        else:
            a_decimal = a_points / Decimal(a_total_points)
        if b_total_points == 0:
            b_decimal = 0.000001
        else:
            b_decimal = b_points / Decimal(b_total_points)
        match_percentage = (Decimal(a_decimal) * Decimal(b_decimal)) ** (1/Decimal(questions_match_num))
        return match_percentage, questions_match_num
    else:
        return None, False
