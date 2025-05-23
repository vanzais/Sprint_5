class MainPageRegistrationPopup:
    email_input = '//input[@class= "input_inputStandart__JweLZ spanGlobal" and @name="email"]'
    password_input = '//input[@class= "input_inputStandart__JweLZ spanGlobal" and @name="password"]'
    submit_password_input = '//input[@class= "input_inputStandart__JweLZ spanGlobal" and @name="submitPassword"]'
    registration_button = '//div[@class="popUp_buttonRow__+W8JD"]/button[@type="submit"]'
    error_text = '//span[text()="Ошибка"]'
    border_input_error = "//div[@class='input_inputError__fLUP9'][descendant::input[@name='email']]"