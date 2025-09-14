import os.path
from selene import browser, have

'''
    Вопросы: 

    1.  В строке 38 #subjectsInput название предмета вводится в строку через enter, но по пользовательским шагам при клике открывается dropdown. 
    Исследовать его html не получается,так как при нажатии на inspect в devtools список сразу закрывается. Как такие элементы проверять? 
    Можно ли отключить автоматическое закрытие списка? 
        Тоже самое и в списках #state и #city. 
    Хотел сделать проверку именно кликом по элементу из списка, но срабатывает автозакрытие.

    2. Как правильно делать ввод текста в строку? Я делал сначала клик по строке (чтобы строка стала активна),
    потом уже вводил текст, опирался на пользовательский сценарий. 
    Пользователь при вводе текста сначала делает клик, а потом, с клавиатуры вводит текст. 
    Можно же еще вводить текст напрямую без клика (через type). 
    Как будет правильно ? Какой из способов и когда стоит применять ?

    '''

def test_sending_form (open_browser):

    browser.open('/')
    browser.execute_script("window.scrollBy(0, 250);") #Поставил скролл вниз тк,
    # на моем экране не находится элемент #submit

    browser.element('#firstName').click().send_keys('Иван')
    browser.element('#lastName').click().send_keys('Иванов')
    browser.element('#userEmail').click().send_keys('IIvanon23@gmai.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[placeholder="Mobile Number"]').click().send_keys('1234567891')

    browser.element('#dateOfBirthInput').click()
    browser.element('[value="4"]').click()
    browser.element('[value="1940"]').click()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').send_keys('Maths').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('фото.jpg'))

    browser.element('#currentAddress').send_keys('Улица Пушкина, дом Колотушкина')
    browser.element('#state').click()
    browser.element('//*[text()="Uttar Pradesh"]').click()
    browser.element('#city').click()
    browser.element('//*[text()="Agra"]').click()
    browser.element('#submit').click()

    browser.element('#example-modal-sizes-title-lg').should(have.exact_text
                                                            ('Thanks for submitting the form'))
    browser.all('table tbody tr').should(have.exact_texts('Student Name Иван Иванов',
                                                          'Student Email IIvanon23@gmai.com',
                                                          'Gender Male',
                                                          'Mobile 1234567891',
                                                          'Date of Birth 15 May,1940',
                                                          'Subjects Maths',
                                                          'Hobbies Sports',
                                                          'Picture фото.jpg',
                                                          'Address Улица Пушкина, дом Колотушкина',
                                                          'State and City Uttar Pradesh Agra'))
    browser.element('#closeLargeModal').click()








