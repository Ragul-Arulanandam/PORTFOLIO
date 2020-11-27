from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField, SubmitField
from wtforms.validators import DataRequired



class PredictForm(FlaskForm):
    AREA = StringField('AREA',validators=[DataRequired()])
    INTSQFT = IntegerField('INTSQFT',validators=[DataRequired()])
    BHK = IntegerField('BHK',validators=[DataRequired()])
    BATHROOMS = IntegerField('BATHROOMS',validators=[DataRequired()])
    PREDICT = SubmitField('PREDICT')


 
    