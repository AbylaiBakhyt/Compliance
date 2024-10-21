import streamlit as st
import requests
import json
from model import send_message
from prompt import f_system_prompt, s_system_prompt
from rag import cid_rag, ipd_rag
import warnings
warnings.filterwarnings("ignore")

import logging

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Инициализация переменных в session_state
if "form_submitted" not in st.session_state:
    st.session_state.form_submitted = False
    # logging.debug("Инициализировано 'form_submitted' в session_state.")

if "form_data" not in st.session_state:
    st.session_state.form_data = {}
    # logging.debug("Инициализировано 'form_data' в session_state.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    # logging.debug("Инициализировано 'chat_history' в session_state.")

# Заголовок приложения
st.title("Завяка на перевод")

# Если форма не была отправлена, показываем её
if not st.session_state.form_submitted:
    with st.form("transaction_form"):
        fio = st.text_input("ФИО", placeholder="Введите ваше ФИО",value='Абылай')
        country = st.text_input("Страна", placeholder="Введите страну",value='Германия')
        resident = st.radio("Резидент", ("Да", "Нет"))
        recipient_fio = st.text_input("ФИО Получателя", placeholder="Введите ФИО получателя",value='Иван Иванович')
        amount = st.text_input("Сумма перевода", placeholder="Введите сумму перевода",value='100000')
        knp = st.text_input("КНП", placeholder="Введите КНП",value='Оплата обучения')
        
        submit_button = st.form_submit_button("Подтвердить")

    if submit_button:
        # logging.debug("Нажата кнопка 'Подтвердить'.")
        if fio and country and resident and amount and knp:
            st.session_state.form_data = {
                "ФИО клиента": fio,
                "Страна получателя": country,
                "Резидент Республики Казахстан": resident,
                "ФИО получателя": recipient_fio,
                "Сумма перевода": amount,
                "Цель перевода": knp
            }
            st.session_state.form_submitted = True
            st.success("Данные успешно сохранены! Вы можете начать общение с чатом.")
            # logging.debug(f"Данные формы сохранены: {st.session_state.form_data}")
        else:
            st.error("Пожалуйста, заполните все обязательные поля.")
            # logging.debug("Ошибка валидации формы: не все обязательные поля заполнены.")

# Конвертация данных формы в JSON
if st.session_state.form_data:
    form_data_json = json.dumps(st.session_state.form_data, ensure_ascii=False, indent=4)
    # logging.debug(f"Данные формы в JSON: {form_data_json}")

# Функция проверки наличия слова "готово/"
def check_if_done(messages):
    for message in messages:
        if message["role"] == "assistant" and "DONE//" in message["content"]:
            return True
    return False

# Логика работы чата
if st.session_state.form_submitted:
    # logging.debug("Форма отправлена. Запуск логики чата.")
    st.title("Compliance Bot")

    # Стартовое сообщение для клиента
    start_message = f"""
    Здравствуйте {st.session_state.form_data['ФИО клиента']}! Мы получили вашу заявку на перевод денежных средств на сумму {st.session_state.form_data['Сумма перевода']}. Для рассмотрения и подтверждения перевода нам необходимо задать вам несколько вопросов, чтобы запросить необходимые документы.
    """

    if "messages" not in st.session_state:
        # logging.debug(f"Состояние session_state до вывода start_message: {st.session_state}")
        st.session_state.messages = [{"role": "system", "content": f_system_prompt(form_data_json)}]
        # st.session_state.messages = [{"role": "system", "content": 'ты просто бот'}]
        st.session_state.messages.append({"role": "assistant", "content": start_message})

    # Отображение истории сообщений
    unique_messages = set()
    for message in st.session_state.messages:
        if message["role"] != "system" and message["content"] not in unique_messages:
            unique_messages.add(message["content"])
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
                # logging.debug(f"Отображено сообщение от {message['role']}: {message['content']}")

    if user_message := st.chat_input("Введите ваше сообщение"):
        with st.chat_message("user"):
            st.markdown(user_message)
        
        # Добавляем сообщение пользователя в историю
        st.session_state.messages.append({"role": "user", "content": user_message})

        # Отправляем сообщение в API и получаем ответ
        # logging.debug(f"session_state: {st.session_state}")
        response = send_message(user_message, st.session_state.messages)

        # Добавляем ответ ассистента в историю
        st.session_state.messages.append({"role": "assistant", "content": response})

        with st.chat_message("assistant"):
            st.markdown(response)

        if check_if_done([{"role": "assistant", "content": response}]):
            info_from_user = st.session_state['messages'][-1]['content'].split("DONE//")[-1].strip()
            # logging.debug(f'info_from_user:{info_from_user}')
            st.session_state.chat_history = st.session_state.messages.copy()
            # logging.debug("Сообщение с 'DONE//' найдено. История чата сохранена.")
            # logging.debug(f"Состояние session_state после копирования: {st.session_state}")
            
            # Обнуляем messages и устанавливаем новое системное сообщение
            print(st.session_state.chat_history)
            st.session_state.messages = [{"role": "system", "content": s_system_prompt(
                st.session_state.chat_history,
                info_from_user,
                ipd_rag,
                cid_rag,
                form_data_json)}]
            # logging.debug(f"Состояние session_state с новым промптом: {st.session_state}")

