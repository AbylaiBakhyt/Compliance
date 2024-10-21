cid_rag = '''
1. Тип услуги: Перевод на свой счет в другом банке  
   Перечень документов:  
   1. Вид на жительство/Договор владения или аренды недвижимости/иной документ, подтверждающий место постоянного пребывания в стране, куда направляется перевод (при наличии).  

---

2. Тип услуги: Безвозмездный перевод/материальная помощь другому лицу  
   Перечень документов:  
   1. Документ, подтверждающий родственную связь (при необходимости).  

---

3. Тип услуги: Безвозмездный перевод на лечение  
   Перечень документов:  
   1. Договор/инвойс от лечебного учреждения, справка о диагнозе и т.п. (при наличии).  
   2. Документ, подтверждающий родственную связь (при необходимости).  

---

4. Тип услуги: Безвозмездный перевод на образование  
   Перечень документов:  
   1. Договор оказания образовательных услуг или инвойс.  
   2. Приложение к договору с условиями оплаты и обязательств и справки об оплате (при наличии).  
   3. Документ, подтверждающий родственную связь (при необходимости).  

---

5. Тип услуги: Алименты  
   Перечень документов:  
   1. Решение специального госоргана о выплате алиментов (при отсутствии решения — соглашение об уплате алиментов).  
   2. Свидетельство о расторжении брака (если применимо).  
   3. Документ, подтверждающий родственную связь.  

---

6. Тип услуги: Финансовый займ  
   Перечень документов:  
   1. Договор займа/соглашение о предоставлении займа.  
   2. Приложение к договору с условиями оплаты и обязательств и справки об оплате (при наличии).  
   3. План возврата.  

---

7. Тип услуги: Брокерское обслуживание  
   Перечень документов:  
   1. Договор брокерского счета.  
   2. Заявление о присоединении к договору.  
   3. Дополнительные соглашения к договору.  

---

8. Тип услуги: Сделки с недвижимостью в РК  
   Перечень документов:  
   1. Договор купли-продажи недвижимости.  
   2. Приложение к договору с условиями оплаты и обязательств.  
   3. Счета на оплату/инвойсы с реквизитами договора (при наличии).  

---

9. Тип услуги: Сделки с недвижимостью за границей  
   Перечень документов:  
   1. Договор купли-продажи недвижимости.  
   2. Приложение к договору с условиями оплаты и обязательств и справки об оплате (при наличии).  
   3. Документ, подтверждающий право иностранца на постоянное проживание (при наличии).  

---

10. Тип услуги: IT-услуги и программирование  
   Перечень документов:  
   1. Договор на оказание IT-услуг.  
   2. Дополнительные соглашения и платежные документы (например, счета-фактуры).  
   3. Договор с правообладателем технологии (если используется сторонняя технология).  
   4. Акт выполненных услуг/работ, инвойсы/счета.  

---

11. Тип услуги: Туристические услуги  
   Перечень документов:  
   1. Договор с туристическим агентством.  
   2. Дополнительные соглашения и платежные документы (например, счета-фактуры).  
   3. Инвойсы/счета за бронь билетов и гостиниц.  

---

12. Тип услуги: Аренда  
   Перечень документов:  
   1. Договор аренды недвижимости.  
   2. Дополнительные соглашения с условиями оплаты и коммунальными услугами (при наличии).  
   3. Счета на оплату/инвойсы с реквизитами договора.  

---

13. Тип услуги: Медицинские услуги  
   Перечень документов:  
   1. Договор на оказание медицинских услуг.  
   2. Дополнительные соглашения с условиями оплаты и справки об оплате (при наличии).  
   3. Акт выполненных услуг/работ, инвойсы/счета на оплату.  

'''


ipd_rag = '''
1. Вид источника происхождения денег: Заработная плата/премии  
   Перечень документов:  
   - Справка с места работы/НДФЛ/иная справка о доходах;  
   - Приказ о назначении/трудовой договор;  
   - Цепочка выписок через которые проходили деньги с момента поступления заработной платы от работодателя до их зачисления на счет в Банке
---

2. Вид источника происхождения денег: Продажа имущества (недвижимость, авто и прочее материальное имущество)  
   Перечень документов:  
   - Договор купли-продажи имущества/договор долевого участия/договор по коммерческому предложению выкупа недвижимости;  
   - Цепочка выписок через которые проходили деньги с момента поступления средств от покупатедя до их зачисления на счет в Банке 

---

3. Вид источника происхождения денег: Продажа доли в компании/акций компании и прочее нематериальное имущество  
   Перечень документов:  
   - Договор купли-продажи/договор отчуждения (уступки) права выбывающего участника товарищества на долю в имуществе (уставном капитале);  
   - Финансовая отчетность продаваемой компании/аудиторский отчет/договор об оценочной стоимости;  
   - Цепочка выписок через которые проходили деньги с момента поступления средств от покупатедя до их зачисления на счет в Банке 

---

4. Вид источника происхождения денег: Дарение, наследство, безвозмездная помощь  
   Перечень документов:  
   - Акт дарения, документы о наследстве;  
   - Документ, подтверждающий родственные отношения сторон;  
   - Цепочка выписок через которые проходили деньги с момента получение средств от дарителя до их зачисления на счет в Банке/расписка о получении наличных и подтверждение зачисления на счет в банке; 
   - Иные пояснения, раскрывающие, кем приходится даритель и каким способом получены средства.  

---

5. Вид источника происхождения денег: Дивиденды и прочее вознаграждение от компаний  
   Перечень документов:  
   - Решение/протокол о выплате дивидендов;  
   - Финансовая отчетность компании;  
   - Цепочка выписок через которые проходили деньги с момента получение средств от компании до их зачисления на счет в Банке 

---

6. Вид источника происхождения денег: Займы  
   Перечень документов:  
   - Договор займа/договор цессии/договор уступки прав требования;  
   - Полная цепочка выписок, показывающая получение средств от займодателя.  
   - Цепочка выписок через которые проходили деньги с момента получение средств от займодателя до их зачисления на счет в Банке 

---

7. Вид источника происхождения денег: Доход от сделок с ценными бумагами – без участия брокера  
   Перечень документов:  
   - Договор по сделке с ценными бумагами;  
   - Акт приема-передачи ценных бумаг/налоговые декларации/протоколы собраний акционеров или участников;  
   - Цепочка выписок через которые проходили деньги с момента получения средств от контрагента до их зачисления на счет в Банке  

---

8. Вид источника происхождения денег: Доход от инвестиционной деятельности, от спекулятивных сделок через иных брокеров  
   Перечень документов:  
   - Договор с брокером;  
   - Отчет по брокерским операциям;  
   - Цепочка выписок через которые проходили деньги с момента получение средств от брокера до их зачисления на счет в Банке  
---

9. Вид источника происхождения денег: Предпринимательская деятельность/частное оказание профессиональных услуг  
    Перечень документов:  
    - Договора с контрагентами;  
    - Налоговые декларации/документы, подтверждающие оплату налогов;  
    - Цепочка выписок через которые проходили деньги с момента получения средств от контрагентов до их зачисления на счет в Банке  

---

10. Вид источника происхождения денег: Иное  
    Перечень документов:  
    - Договор/соглашение/счет и иные документы, на основании которых получены средства;  
    - Цепочка выписок через которые проходили деньги с момента получения средств до их зачисления на счет в Банке  
'''

cid_rag_dict = {
    1: {
        "Тип услуги": "Перевод на свой счет в другом банке",
        "Перечень документов": [
            "Вид на жительство",
            "Договор владения или аренды недвижимости",
            "Иной документ, подтверждающий место постоянного пребывания в стране, куда направляется перевод (при наличии)"
        ]
    },
    2: {
        "Тип услуги": "Безвозмездный перевод/материальная помощь другому лицу",
        "Перечень документов": [
            "Документ, подтверждающий родственную связь (при необходимости)"
        ]
    },
    3: {
        "Тип услуги": "Безвозмездный перевод на лечение",
        "Перечень документов": [
            "Договор/инвойс от лечебного учреждения, справка о диагнозе и т.п. (при наличии)",
            "Документ, подтверждающий родственную связь (при необходимости)"
        ]
    },
    4: {
        "Тип услуги": "Безвозмездный перевод на образование",
        "Перечень документов": [
            "Договор оказания образовательных услуг или инвойс",
            "Приложение к договору с условиями оплаты и обязательств и справки об оплате (при наличии)",
            "Документ, подтверждающий родственную связь (при необходимости)"
        ]
    },
    5: {
        "Тип услуги": "Алименты",
        "Перечень документов": [
            "Решение специального госоргана о выплате алиментов (при отсутствии решения — соглашение об уплате алиментов)",
            "Свидетельство о расторжении брака (если применимо)",
            "Документ, подтверждающий родственную связь"
        ]
    },
    6: {
        "Тип услуги": "Финансовый займ",
        "Перечень документов": [
            "Договор займа/соглашение о предоставлении займа",
            "Приложение к договору с условиями оплаты и обязательств и справки об оплате (при наличии)",
            "План возврата"
        ]
    },
    7: {
        "Тип услуги": "Брокерское обслуживание",
        "Перечень документов": [
            "Договор брокерского счета",
            "Заявление о присоединении к договору",
            "Дополнительные соглашения к договору"
        ]
    },
    8: {
        "Тип услуги": "Сделки с недвижимостью в РК",
        "Перечень документов": [
            "Договор купли-продажи недвижимости",
            "Приложение к договору с условиями оплаты и обязательств",
            "Счета на оплату/инвойсы с реквизитами договора (при наличии)"
        ]
    },
    9: {
        "Тип услуги": "Сделки с недвижимостью за границей",
        "Перечень документов": [
            "Договор купли-продажи недвижимости",
            "Приложение к договору с условиями оплаты и обязательств и справки об оплате (при наличии)",
            "Документ, подтверждающий право иностранца на постоянное проживание (при наличии)"
        ]
    },
    10: {
        "Тип услуги": "IT-услуги и программирование",
        "Перечень документов": [
            "Договор на оказание IT-услуг",
            "Дополнительные соглашения и платежные документы (например, счета-фактуры)",
            "Договор с правообладателем технологии (если используется сторонняя технология)",
            "Акт выполненных услуг/работ, инвойсы/счета"
        ]
    },
    11: {
        "Тип услуги": "Туристические услуги",
        "Перечень документов": [
            "Договор с туристическим агентством",
            "Дополнительные соглашения и платежные документы (например, счета-фактуры)",
            "Инвойсы/счета за бронь билетов и гостиниц"
        ]
    },
    12: {
        "Тип услуги": "Аренда",
        "Перечень документов": [
            "Договор аренды недвижимости",
            "Дополнительные соглашения с условиями оплаты и коммунальными услугами (при наличии)",
            "Счета на оплату/инвойсы с реквизитами договора"
        ]
    },
    13: {
        "Тип услуги": "Медицинские услуги",
        "Перечень документов": [
            "Договор на оказание медицинских услуг",
            "Дополнительные соглашения с условиями оплаты и справки об оплате (при наличии)",
            "Акт выполненных услуг/работ, инвойсы/счета на оплату"
        ]
    }
}


ipd_rag_dict = {
    1: {
        "Вид источника происхождения денег": "Заработная плата/премии",
        "Перечень документов": [
            "Справка с места работы/НДФЛ/иная справка о доходах",
            "Приказ о назначении/трудовой договор",
            "Цепочка выписок через которые проходили деньги с момента поступления заработной платы от работодателя до их зачисления на счет в Банке"
        ]
    },
    2: {
        "Вид источника происхождения денег": "Продажа имущества (недвижимость, авто и прочее материальное имущество)",
        "Перечень документов": [
            "Договор купли-продажи имущества/договор долевого участия/договор по коммерческому предложению выкупа недвижимости",
            "Цепочка выписок через которые проходили деньги с момента поступления средств от покупателя до их зачисления на счет в Банке"
        ]
    },
    3: {
        "Вид источника происхождения денег": "Продажа доли в компании/акций компании и прочее нематериальное имущество",
        "Перечень документов": [
            "Договор купли-продажи/договор отчуждения (уступки) права выбывающего участника товарищества на долю в имуществе (уставном капитале)",
            "Финансовая отчетность продаваемой компании/аудиторский отчет/договор об оценочной стоимости",
            "Цепочка выписок через которые проходили деньги с момента поступления средств от покупателя до их зачисления на счет в Банке"
        ]
    },
    4: {
        "Вид источника происхождения денег": "Дарение, наследство, безвозмездная помощь",
        "Перечень документов": [
            "Акт дарения, документы о наследстве",
            "Документ, подтверждающий родственные отношения сторон",
            "Цепочка выписок через которые проходили деньги с момента получения средств от дарителя до их зачисления на счет в Банке/расписка о получении наличных и подтверждение зачисления на счет в банке",
            "Иные пояснения, раскрывающие, кем приходится даритель и каким способом получены средства"
        ]
    },
    5: {
        "Вид источника происхождения денег": "Дивиденды и прочее вознаграждение от компаний",
        "Перечень документов": [
            "Решение/протокол о выплате дивидендов",
            "Финансовая отчетность компании",
            "Цепочка выписок через которые проходили деньги с момента получения средств от компании до их зачисления на счет в Банке"
        ]
    },
    6: {
        "Вид источника происхождения денег": "Займы",
        "Перечень документов": [
            "Договор займа/договор цессии/договор уступки прав требования",
            "Полная цепочка выписок, показывающая получение средств от займодателя",
            "Цепочка выписок через которые проходили деньги с момента получения средств от займодателя до их зачисления на счет в Банке"
        ]
    },
    7: {
        "Вид источника происхождения денег": "Доход от сделок с ценными бумагами – без участия брокера",
        "Перечень документов": [
            "Договор по сделке с ценными бумагами",
            "Акт приема-передачи ценных бумаг/налоговые декларации/протоколы собраний акционеров или участников",
            "Цепочка выписок через которые проходили деньги с момента получения средств от контрагента до их зачисления на счет в Банке"
        ]
    },
    8: {
        "Вид источника происхождения денег": "Доход от инвестиционной деятельности, от спекулятивных сделок через иных брокеров",
        "Перечень документов": [
            "Договор с брокером",
            "Отчет по брокерским операциям",
            "Цепочка выписок через которые проходили деньги с момента получения средств от брокера до их зачисления на счет в Банке"
        ]
    },
    9: {
        "Вид источника происхождения денег": "Предпринимательская деятельность/частное оказание профессиональных услуг",
        "Перечень документов": [
            "Договора с контрагентами",
            "Налоговые декларации/документы, подтверждающие оплату налогов",
            "Цепочка выписок через которые проходили деньги с момента получения средств от контрагентов до их зачисления на счет в Банке"
        ]
    },
    10: {
        "Вид источника происхождения денег": "Иное",
        "Перечень документов": [
            "Договор/соглашение/счет и иные документы, на основании которых получены средства",
            "Цепочка выписок через которые проходили деньги с момента получения средств до их зачисления на счет в Банке"
        ]
    }
}
