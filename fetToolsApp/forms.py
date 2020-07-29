from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class UploadFetDataForm(FlaskForm):
    yearOfGraduation = StringField('Year of Graduation (YYYY)', validators=[DataRequired()])
    scheduleYear = StringField('Schedule Year (YYYY)', validators=[DataRequired()])
    scheduleSemester = StringField('Schedule Semester (Fall or Spring)', validators=[DataRequired()])
    csvFetStudentInputFile = FileField('FET Student Input File (*.csv format)', validators=[FileAllowed(['csv']),FileRequired()])
    csvFetTimetableInputFile = FileField('FET Timetable Input File (*.csv format)', validators=[FileAllowed(['csv']),FileRequired()])
    submit = SubmitField('Generate Schedule File')
