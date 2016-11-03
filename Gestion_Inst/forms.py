from crispy_forms.bootstrap import StrictButton, FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.forms import forms
from django import forms
from Gestion_Inst.models import Alumno


class AlumnoForm(forms.ModelForm):
    # helper = FormHelper()
    # helper.form_class = 'form-horizontal'
    # helper.label_class = 'col-lg-2'
    # helper.field_class = 'col-lg-8'
    # helper._form_method = 'post'
    # helper._form_action = '/crear/'
    # helper.layout = Layout(
    #     'apellido', 'nombres', 'fecha_nac', 'domicilio', 'telefono', 'dni', 'sexo', 'legajo', 'estado',
    #     StrictButton('Sign in', css_class='btn-default'),
    # )


    class Meta:
        model = Alumno
        fields = ('apellido', 'nombres', 'fecha_nac', 'domicilio', 'telefono', 'dni', 'sexo', 'legajo', 'estado')

    def __init__(self,*args,**kwargs):
        super(AlumnoForm,self).__init__(*args,*kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout.append(
            FormActions(
                Submit('Guardar','Guardar'),
            )
        )
