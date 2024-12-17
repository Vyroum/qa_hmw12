from pages.practice_form_page import PracticeFormPage
import allure



@allure.title("Успешное заполнение формы")
def test_practice_form(browser_set):

    with allure.step("Открытие формы регистрации"):
        practice_form_page = PracticeFormPage()
        practice_form_page.open()

    with allure.step("Заполнение полного имени"):
        practice_form_page.fill_first_name("Andrei")
        practice_form_page.fill_last_name("Monichev")

    with allure.step("Заполнение email"):
        practice_form_page.fill_email("testmail@test.ru")

    with allure.step("Выбор пола"):
        practice_form_page.select_gender("Male")

    with allure.step("Заполнение номера телефона"):
        practice_form_page.fill_user_number("1231231234")

    with allure.step("Выбор даты рождения"):
        practice_form_page.pick_date_of_birth("1995", "September", "13")

    with allure.step("Выбор интересующих предметов"):
        practice_form_page.fill_subject("Maths")

    with allure.step("Выбор хобби"):
        practice_form_page.choose_interest_sport()
        practice_form_page.choose_interest_music()
        practice_form_page.choose_interest_reading()

    with allure.step("Добавление картинки"):
        practice_form_page.upload_picture("image.jpg")

    with allure.step("Заполнение полного адреса"):
        practice_form_page.fill_address("City Name, Street Name")
        practice_form_page.choose_state("NCR")
        practice_form_page.choose_city("Noida")

    with allure.step("Отправка формы регистрации"):
        practice_form_page.submit_button()

    with allure.step("Сравнение отправленных и переданных значений"):
        practice_form_page.should_registered_user_with(
            "Andrei Monichev",
            "testmail@test.ru",
            "Male",
            "1231231234",
            "13 September,1995",
            "Maths",
            "Sports, Music, Reading",
            "image.jpg",
            "City Name, Street Name",
            "NCR Noida"
        )
