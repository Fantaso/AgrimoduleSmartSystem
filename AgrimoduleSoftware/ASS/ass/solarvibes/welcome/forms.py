from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, NumberRange


class FarmForm(FlaskForm):
    farm_name                   = StringField('Farm name', validators=[DataRequired(), Length(min=2, max=30, message='''Your name needs at least 2 characters.''')])
    farm_location               = StringField('Farm location', validators=[DataRequired(), Length(min=2, max=30, message='''Your name needs at least 2 characters.''')])
    farm_area                   = FloatField('Farm Cultivation Area', validators=[DataRequired(), NumberRange(min=1, max=5000, message='Area between 1 and 5000 m2')])
    farm_cultivation_process    = SelectField('Farm Cultivation Process', validators=[DataRequired()], choices=[('Organic','Organic'),('Chemical','Chemical')])


class FieldForm(FlaskForm):
    field_name                    = StringField(label='Field name', validators=[DataRequired(), Length(min=2, max=30, message='''Your name needs at least 2 characters.''')])
    field_cultivation_area       = FloatField(label='Field Cultivation Area', validators=[DataRequired(), NumberRange(min=1, max=5000, message='Cultivation area should be maximum as big as your farm')],render_kw={"placeholder":"500.50"})
    field_cultivation_crop        = SelectField(label='Cultivation Crop', validators=[DataRequired()], coerce = int)
    field_cultivation_start_date  = DateField(label='Cultivation Start Date', format='%Y-%m-%d', validators=[DataRequired()])
    field_cultivation_state       = SelectField(label='Cultivation State', validators=[DataRequired()], choices=[('new','New'),('already growing','Already Growing')])
    field_cultivation_type        = SelectField(label='Cultivation Type', validators=[DataRequired()], choices=[('mono','Mono'), ('mix','Mix'), ('multi','Multi')])

class AddAgrisysForm(FlaskForm):
    agrimodule_name              = StringField('Agrimodule name', validators=[DataRequired(), Length(min=2, max=20, message='Give it a name for sanity MAX 30.')])
    agrimodule_identifier        = StringField('Agrimodule code', validators=[DataRequired(), Length(min=2, max=30, message='Your agrimodule system identifier is in the back of your agrimodule.')])

class InstallAgrisysForm(FlaskForm):
    agm_lat                 = FloatField('Agrimodule latitude location',       validators=[DataRequired(), NumberRange(min=-90, max=90, message='write the lat coordinates')])
    agm_lon                 = FloatField('Agrimodule longitude location',      validators=[DataRequired(), NumberRange(min=-180, max=180, message='write the lon coordinates')])
    ags_lat                 = FloatField('Agrisensor latitude location',       validators=[DataRequired(), NumberRange(min=-90, max=90, message='write the lat coordinates')])
    ags_lon                 = FloatField('Agrisensor longitude location',      validators=[DataRequired(), NumberRange(min=-180, max=180, message='write the lon coordinates')])
    agp_lat                 = FloatField('Agripump latitude location',         validators=[DataRequired(), NumberRange(min=-90, max=90, message='write the lat coordinates')])
    agp_lon                 = FloatField('Agripump longitude location',        validators=[DataRequired(), NumberRange(min=-180, max=180, message='write the lon coordinates')])

class PreAddPumpForm:
    def __init__(self, pump_name, pump_brand, pump_flow_rate, pump_head, pump_watts):
        self.pump_name       = pump_name
        self.pump_brand      = pump_brand
        self.pump_flow_rate  = pump_flow_rate
        self.pump_head       = pump_head
        self.pump_watts      = pump_watts

class AddPumpForm(FlaskForm):
    pump_name               = StringField('Pump name',                              validators=[DataRequired(), Length(min=2, max=30, message='Give it a name for sanity MAX 30.')])
    pump_brand              = StringField('Pump brand',                             validators=[DataRequired(), Length(min=2, max=30, message='Your pump supplier or brand name')])
    pump_flow_rate          = FloatField('Pump flow rate (liters per sec)',         validators=[DataRequired(), NumberRange(min=1, max=500, message="Your pump's water capacity or water turn over")])
    pump_head               = FloatField('Pump head (meters)',                      validators=[DataRequired(), NumberRange(min=1, max=500, message="Your pump's max head pressure or height power")])
    pump_watts              = FloatField('Pump power consumption (kilo Watts)',     validators=[DataRequired(), NumberRange(max=1000, message="Your pump's wattage consumption")])