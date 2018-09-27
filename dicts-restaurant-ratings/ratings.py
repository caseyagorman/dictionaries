"""Restaurant rating lister."""
def process_scores():

    scores_txt = open('scores.txt')
    scores = {}
    for line in scores_txt:
        line = line.rstrip()
        restaurant, rating = line.split(":")
        print restaurant, rating
        scores[restaurant] = int(rating)
    return scores

process_scores()

def get_rating_from_user(scores):
    restaurant= raw_input("Enter restaurant name ")
    rating = raw_input("Enter restaurant score ")
    scores[restaurant] = int(rating)
    for restaurant in sorted(scores.iterkeys()):
        print "%s: %s" % (restaurant, scores[restaurant])
    return scores

scores = process_scores()
get_rating_from_user (scores)
