from flask import Flask, request, json, jsonify
from flask.views import MethodView

from models import Card

app = Flask(__name__)


class CardView(MethodView):

    def get(self, *args, **kwargs):
        cards = Card.select().dicts()
        return {'errors': False, 'cards': list(cards)}

    def post(self, *args, **kwargs):

        data = request.get_json(cache=False)
        if not data.get('number'):
            return {'errors': True, 'message': 'Not valid number'}
        if not data.get('person'):
            return {'errors': True, 'message': 'Not valid person'}
        if not data.get('end_data'):
            return {'errors': True, 'message': 'Not valid end data'}
        if not data.get('cvv'):
            return {'errors': True, 'message': 'Not valid cvv'}

        card = Card.create(
            number=data.get('number'),
            person=data.get('person'),
            end_data=data.get('end_data'),
            cvv=data.get('cvv'),
        )

        return {'errors': False, 'new_card_id': card.id}


# urls
app.add_url_rule('/cards/', view_func=CardView.as_view('card_view'))

if __name__ == '__main__':
    app.run()
