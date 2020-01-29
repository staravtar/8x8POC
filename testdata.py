from datetime import datetime


class TestData:
    # Login page data
    Log_in_button_xpath = "//button[@data-id='BUTTON' and text()='Login']"
    Email_box_xpath = "//input[@id ='1-email' and @placeholder = 'yours@example.com']"
    Pwd_box_xpath = "//input[@name='password' and @placeholder = 'your password']"
    log_in_xpath = "//button[@name = 'submit' and @aria-label = 'Log In']"
    enter_name_meeting_joining_xpath = "//input[@name='displayName']"
    button_to_setName = "//button[@class='sc-bwzfXH iuZaWk']"
    user_name = "ayush.andprod@gmail.com"
    password = "Tester@123"
    user_name_1 = "ayush.andprod@gmail.com"

    # Home page locators
    join_button_xpath = "//div[@class='sc-LKuAh AkHBX'][1]"
    start_button_xpath = "//button[@data-id = 'BUTTON' and text()='Start']"
    large_video_xpath = "//video[@id='largeVideo']"
    sync_calender_xpath = "//button[@data-id='BUTTON' and text()='Sync Calendar']"
    setting_btn_css = "svg.sc-htpNat.byYkqd"
    calender_and_schedule_xpath = "//div[text()='Calendar & Scheduling']"
    delete_mail_xpath = "//*[@class = 'sc-jGxEUC lpvsxK sc-htpNat kfxoqY']"
    sharescreen_xpath = "//div[@aria-label='Toggle screenshare']"

    # google page locators
    google_app_xpath = "//a[@aria-label= 'Google apps']"
    # Sync calender outside window path
    google_xpath = "//li/a[text()='Google']"
    terms_checkbox_xpath = "//input[@id='account_profile_accept_terms']"
    link_google_acc_xpath = "//input[@name='commit' and @value = 'Link Google Account']"
    gmail_email_input_xpath = "//input[@id='identifierId' and @type = 'email']"
    gmail_email_next_xpath = "//div[@id = 'identifierNext' and @role ='button']"
    gmail_pwd_xpath = "//input[@name='password' and @type = 'password']"
    gmail_pwd_next_xpath = "//div[@id ='passwordNext' and @role= 'button']"
    gmail_allow_xpath = "//div[@id='submit_approve_access' and @role = 'button']"
    gmail_accept_xpath = "//input[@type='submit' and @value= 'Accept']"
    no_schedule_event_xpath = "//li[text()='No scheduled events']"

    current_hour = datetime.today().time().microsecond
    create_btn_xpath = "//div[text()='Create']"
    add_title_xpath = "//input[@type='text' and @aria-label='Add title']"
    save_button = "//span[text()='Save']"

    meeting_title = "demo_" + str(current_hour)
    meeting_title_homepage_xpath = "//div[contains(text(),{})]".format(meeting_title)

    #my_call_box_xpath = "//span[text()='ayush.andprod@gmail.com (me)']"
    my_call_box_xpath = "//span[contains(text(),'(me)')]"
    states_icon_xpath = "//div[@class='indicator-container show-connection-indicator' and @id]"
    connection_info_container_xpath = "//table[@class='connection-info__container]"
    iframe_css = "iframe#jitsiConferenceFrame0"
    connection_xpath = "//table[@class='connection-info__container']/tbody/tr[1]/td[2]"
    bitrate_xpath = "//table[@class='connection-info__container']/tbody/tr[2]/td[2]"
    packet_loss_xpath = "//table[@class='connection-info__container']/tbody/tr[3]/td[2]"
    resolution_xpath = "//table[@class='connection-info__container']/tbody/tr[4]/td[2]"
    frame_rate_xpath = "//table[@class='connection-info__container']/tbody/tr[5]/td[2]"

    meeting_title = "demo_"+str(current_hour)
    meeting_title_homepage_xpath = "//div[text()="+meeting_title+"]"

    # Audio video mute unmute
    unmute_audio_btn_xpath = "//div[@aria-label='Toggle mute audio']//div[@class='toolbox-icon  ']"
    non_video_btn_xpath = "//div[@aria-label='Toggle mute video']//div[contains(@class,'toolbox-icon  ')]"

    mute_audio_btn_xpath = "//div[@aria-label='Toggle mute audio']//div[contains(@class,'toolbox-icon toggled')]"
    mute_video_btn_xpath = "//div[@aria-label='Toggle mute video']//div[contains(@class,'toolbox-icon toggled')]"

    class_value_for_unmute = "toolbox-icon  "  # do not remove spaces
    class_value_for_mute = "toolbox-icon toggled "


    #WEBRTC LOCATORS
    webrtc_url = "chrome://webrtc-internals/"
    tab_heads_xpath = "//span[@class='tab-head']"
    audiosourcehead = "//summary[contains(text(),'RTCAudioSource')]"
    tab_audio_level = "//tr[contains(@id,'audioLevel')]/td[2]"
    videosourcehead = "//summary[contains(text(),'RTCVideoSource')]"
    tab_video_width = "//tr[contains(@id,'RTCVideoSource')][4]/td[2]"
    tab_video_height = "//tr[contains(@id,'RTCVideoSource')][5]/td[2]"
    VideoOutboundhead = "//summary[contains(text(),'RTCOutboundRTPVideoStream')]"
    tab_videobytes_persec = "//tr[contains(@id,'RTCOutboundRTPVideoStream')][19]/td[2]"
    tab_videobytes_persec_after_off = "//table[contains(@id , 'table-RTCOutboundRTPVideoStream')]/tbody/tr[contains(@id,'-[bytesSent/s]')]/td[2]"

    vdo_track_sender_xpath = "//summary[contains(text(),'RTCMediaStreamTrack_sender_2 (track)')]"
    vdo_farme_width_xpath = "// table[contains( @ id, 'table-RTCMediaStreamTrack_sender_2')]/tbody/tr[9]/td[2]"
    vdo_frame_hight_xpath = "//table[contains(@id,'table-RTCMediaStreamTrack_sender_2')]/tbody/tr[10]/td[2]"


