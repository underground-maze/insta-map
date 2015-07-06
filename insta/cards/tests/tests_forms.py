import unittest

from decimal import Decimal

from helpers.tests import InstaTransactionTestCase
from cards.forms import AddCardForm
from cards.models import Card


class AddCardFormTestCase(InstaTransactionTestCase):

    """ Tests for add card form check """

    form_class = AddCardForm

    def get_form(self, data):
        return self.form_class(data=data)

    def test_field_description(self):
        """ Check correct field description work """
        # check is required field not provided
        form = self.get_form(dict())
        self.assertEqual(form.errors['description'], ['Обязательное поле.'])
        # check is required field empty value
        form = self.get_form(dict(description='                          '))
        self.assertEqual(form.errors['description'], ['Обязательное поле.'])
        # check is very long field value
        form = self.get_form(dict(description='a' * 1001))
        self.assertEqual(form.errors['description'], [
            'Убедитесь, что это значение содержит не более 1000 символов (сейчас 1001).'])
        # check correct
        form = self.get_form(dict(description='test description'))
        self.assertNotIn('description', form.errors)

    def test_field_radius(self):
        """ Check is correct radius initial work """
        form = self.get_form(dict())
        self.assertNotIn('radius', form.errors)
        self.assertEqual(form.cleaned_data['radius'], 3)

    def test_field_position(self):
        """ Check correct field position work """
        # check is required field not provided
        form = self.get_form(dict())
        self.assertEqual(form.errors['position'], ['Обязательное поле.'])
        # check is required field empty value
        form = self.get_form(dict(position='                          '))
        self.assertEqual(form.errors['position'], ['Обязательное поле.'])
        # check correct
        form = self.get_form(dict(position='(44.61979915773973, 33.52958679199219)'))
        self.assertNotIn('position', form.errors)
        self.assertEqual(form.cleaned_data['position'], [Decimal('44.61979915773973'), Decimal('33.52958679199219')])

    def test_field_email(self):
        """ Check correct field email work """
        # check is required field not provided
        form = self.get_form(dict())
        self.assertEqual(form.errors['email'], ['Обязательное поле.'])
        # check is required field empty value
        form = self.get_form(dict(email='                          '))
        self.assertEqual(form.errors['email'], ['Обязательное поле.'])
        # check is very long field value
        form = self.get_form(dict(email=('a' * 1001) + '@e.co'))
        self.assertEqual(form.errors['email'], [
            'Убедитесь, что это значение содержит не более 200 символов (сейчас 1006).'])
        # check invalide email
        form = self.get_form(dict(email='not_email@dddd'))
        self.assertEqual(form.errors['email'], ['Введите корректный адрес электронной почты.'])
        # check correct
        form = self.get_form(dict(email='user@e.co'))
        self.assertNotIn('email', form.errors)

    @unittest.skip('incorrect work on travis ci, db conn error')
    def test_form_save_correct(self):
        """ Check is correct create new instance of card """
        form = self.get_form(dict(
            position='(44.61979915773973, 33.52958679199219)', description='test description', email='user@e.co'))
        form.fields['video'].required = False
        self.assertTrue(form.is_valid())
        # check is no card created
        self.assertEqual(Card.objects.all().count(), 0)
        # save form and check card created
        form.save()
        self.assertEqual(Card.objects.all().count(), 1)
        # check card
        card = Card.objects.first()
        self.assertEqual(card.radius, 3)
        self.assertEqual(card.description, 'test description')
        self.assertEqual(card.user.email, 'user@e.co')
        self.assertEqual(str(card.position.latitude), '44.61979915773973')
        self.assertEqual(str(card.position.longitude), '33.52958679199219')
