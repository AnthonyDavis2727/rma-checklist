from django import forms
from django.forms import ModelForm
from .models import RmaRecords

class InputForm(ModelForm):

    class Meta:
        model = RmaRecords
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'other': forms.Textarea(),
            'recommended_action': forms.Textarea(),
        }
        labels = {

            # Inspector Info
            'inspector': 'Inspector Name',
            'date': 'Date',

            # RMA Info
            'ticket_number': 'Ticket Number',
            'rma_number': 'RMA Number',
            'serial_number': 'Serial Number',

            ###### RMA Inspections ######

            # Visual Inspection
            'screen_condition': 'Screen Condition',
            'mount_condition': 'Mount Condition',
            'other': 'Other Notes',

            # Initial Boot
            'powers_on': 'Powers On',
            'qr_code': 'QR Code Present',
            'matching_serial': 'Matching Serial Number',
            'serial_is_unique': 'Serial Number is Unique',
            'can_be_registered': 'Can Be Registered',
            'stays_registered': 'Stays Registered',
            'logs': 'Logs Present',

            ###### Testing ######

            # Setup
            'emi_filter_board_setup': 'EMI Filter Board (Setup)',
            'yes_button_setup': 'Yes Button (Setup)',
            'no_button_setup': 'No Button (Setup)',
            'call_button_setup': 'Call Button (Setup)',
            'harnesses_continuity': 'Harnesses Continuity',
            'microphone_setup': 'Microphone (Setup)',
            'speaker_setup': 'Speaker (Setup)',
            'camera_setup': 'Camera (Setup)',

            # Live Call
            'yes_button_live': 'Yes Button (Live)',
            'no_button_live': 'No Button (Live)',
            'call_button_live': 'Call Button (Live)',
            'microphone_live': 'Microphone (Live)',
            'speaker_live': 'Speaker (Live)',
            'camera_live': 'Camera (Live)',
            'sd_card': 'SD Card',

            # BOM Check
            'emi_filter_board_bom': 'EMI Filter Board (BOM)',
            'three_button_harnesses': 'Three Button Harnesses',
            'two_foam_inserts': 'Two Foam Inserts',
            'permanent_setup_hand_off': 'Permanent Setup Hand Off',
            'inspection_guide': 'Inspection Guide',
            'quick_start_guide': 'Quick Start Guide',
            'phoenix_plugs': 'Phoenix Plugs',
            'firmware_updated': 'Firmware Updated',

            # Closeout Tasks
            'updated_rma_notes': 'Updated RMA Notes',
            'device_repackaged': 'Device Repackaged',
            'form_uploaded': 'Form Uploaded',
            'tracking_sheet_updated': 'Tracking Sheet Updated',
            'recommended_action': 'Recommended Action',
        }