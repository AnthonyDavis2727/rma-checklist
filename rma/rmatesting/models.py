from django.db import models

class RmaRecords(models.Model):

    # Inspector Info
    inspector = models.CharField(max_length=100)
    date = models.DateField(null=False, blank=False)

    # RMA Identification
    ticket_number = models.IntegerField(null=False, blank=False)
    rma_number = models.IntegerField(null=False, blank=False)
    serial_number = models.IntegerField(null=False, blank=False)

    ###### RMA Inspections ######

    # Visual Inspection
    screen_condition = models.BooleanField(default=False)
    mount_condition = models.BooleanField(default=False)
    other = models.TextField(blank=True)

    # Initial Boot
    powers_on = models.BooleanField(default=False)
    qr_code = models.BooleanField(default=False)
    matching_serial = models.BooleanField(default=False)
    serial_is_unique = models.BooleanField(default=False)
    can_be_registered = models.BooleanField(default=False)
    stays_registered = models.BooleanField(default=False)
    logs = models.BooleanField(default=False)

    ###### Testing ######

    # Setup
    emi_filter_board_setup = models.BooleanField(default=False)
    yes_button_setup = models.BooleanField(default=False)
    no_button_setup = models.BooleanField(default=False)
    call_button_setup = models.BooleanField(default=False)
    harnesses_continuity = models.BooleanField(default=False)
    microphone_setup = models.BooleanField(default=False)
    speaker_setup = models.BooleanField(default=False)
    camera_setup = models.BooleanField(default=False)

    # Live Call
    yes_button_live = models.BooleanField(default=False)
    no_button_live = models.BooleanField(default=False)
    call_button_live = models.BooleanField(default=False)
    microphone_live = models.BooleanField(default=False)
    speaker_live = models.BooleanField(default=False)
    camera_live = models.BooleanField(default=False)
    sd_card = models.BooleanField(default=False)


    # BOM Check
    emi_filter_board_bom = models.BooleanField(default=False)
    three_button_harnesses = models.BooleanField(default=False)
    two_foam_inserts = models.BooleanField(default=False)
    permanent_setup_hand_off = models.BooleanField(default=False)
    inspection_guide = models.BooleanField(default=False)
    quick_start_guide = models.BooleanField(default=False)
    phoenix_plugs = models.BooleanField(default=False)
    firmware_updated = models.BooleanField(default=False)

    # Closeout Tasks
    updated_rma_notes = models.BooleanField(default=False)
    device_repackaged = models.BooleanField(default=False)
    form_uploaded = models.BooleanField(default=False)
    tracking_sheet_updated = models.BooleanField(default=False)
    recommended_action = models.TextField(blank=False)

