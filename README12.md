# Monitoramento de Queimadas na Amazônia

Este projeto tem como objetivo monitorar as queimadas na Amazônia e apresentar informações diárias atualizadas sobre os focos de incêndio detectados. Abaixo, você pode visualizar as queimadas mais recentes, com detalhes sobre localização, satélite que realizou a detecção, e outros fatores relevantes.

## Estrutura dos Dados

Cada entrada na tabela representa um foco de incêndio com as seguintes informações:

- **ID:** Identificador único do foco de incêndio.
- **Latitude/Longitude:** Coordenadas geográficas do foco detectado. Para visualizar o local exato, insira estas coordenadas no Google Maps ou outro aplicativo de mapas.
- **Data/Hora GMT:** Data e hora da detecção em formato GMT (Greenwich Mean Time).
- **Satélite:** Satélite responsável pela detecção do foco de incêndio.
- **Município, Estado e País:** Localização administrativa do foco detectado.
- **Dias sem Chuva:** Número de dias consecutivos sem precipitação na região, o que pode indicar um aumento no risco de incêndio.
- **Precipitação:** Quantidade de chuva (em milímetros) registrada no local.
- **Risco de Fogo:** Índice que indica a probabilidade de ocorrência de incêndio, baseado em fatores como condições climáticas e quantidade de combustível disponível.
- **Bioma:** Bioma onde o foco foi identificado, como Amazônia, Cerrado, ou Mata Atlântica.
- **FRP (Fire Radiative Power):** Potência radiativa do fogo, que mede a intensidade do incêndio. Focos com FRP mais alto indicam incêndios mais intensos.

## Visualização Gráfica

Se você deseja visualizar de forma gráfica onde as queimadas estão ocorrendo, copie as coordenadas de latitude e longitude mais recentes e cole no Google Maps. Isso permite uma compreensão espacial mais clara da distribuição dos focos de incêndio. Alternativamente, você também pode usar a descrição de localização (Município, Estado e País) para identificar a região afetada.

## Informação Adicional

As queimadas na Amazônia não apenas afetam a biodiversidade local, mas também têm implicações globais, contribuindo para o aquecimento global e a emissão de gases de efeito estufa. O monitoramento contínuo é essencial para entender e mitigar os impactos desses incêndios, além de auxiliar na gestão de políticas ambientais e ações de preservação.

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c0a03b1f-acf1-37dd-9f8b-47d559016337 | -9.13822 | -60.61615 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1ba80cd0-b7de-3cee-92dd-03b4a614809e | -1.84551 | -54.51409 | 2026-08-20 00:50:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 79e86b08-8d54-3d65-9451-e952cff836c6 | -8.57362 | -55.30783 | 2026-08-20 00:50:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f408b578-1d9e-3036-9a2d-21526d3b5d05 | -7.45153 | -60.01126 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| e2b49f18-3f1c-3ecd-b6e0-180bc6191c9a | -9.42665 | -60.42407 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 397e0280-9c38-3ff5-999a-aeb5f7c84942 | -6.70426 | -59.08833 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fcefb6b7-8351-3cb5-aa8c-0500f445dbbd | -8.57711 | -54.78045 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 90e42fc6-43fb-33bf-8f82-468e19fe9fc4 | -9.10898 | -60.92856 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d0c18619-c978-3d19-9d55-58d552ee9ffa | -8.66505 | -54.67081 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 5bff9c12-3e3e-3c33-a7f2-0894b96bbc5d | -7.43028 | -59.79417 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b0ad6201-d1ff-3fac-ab86-45f57985e894 | -8.58655 | -54.76121 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e2f6fceb-c6d1-3aa6-8765-1bde8c44fe11 | -9.39693 | -60.55174 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 839e1fc7-feb8-3992-9112-41c4ebd69514 | -7.44143 | -60.00359 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8ffbf9c1-0c6c-3165-89a9-5ae6469b62aa | -10.33041 | -57.56385 | 2026-08-20 00:50:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 42.4 |
| 6c420b17-f718-3860-b16b-0757664f2d44 | -8.56528 | -54.66833 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| d5b21133-32ce-349a-9b59-513c216b6c27 | -8.29459 | -62.90025 | 2026-08-20 00:50:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 173e10a2-ff92-3dee-9239-b524214354c9 | -8.66629 | -54.64583 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 227.1 |
| 6345e4d8-e245-34bc-9900-dbe38355f16c | -6.91553 | -59.346 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| e4c14676-662c-3831-91a9-f1c2e51526a1 | -5.79236 | -55.7157 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 41489354-19da-3d3b-b263-be926839b280 | -10.79411 | -50.30904 | 2026-08-20 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 65d46c00-3908-3cfe-9374-4b7ea37389a6 | -11.83411 | -58.85006 | 2026-08-20 00:50:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 04fe7830-d10e-3941-93c5-bffc70174c27 | -7.82972 | -61.62047 | 2026-08-20 00:50:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 10.2 |
| d427bd73-43eb-302e-89be-2f6d1c0819fd | -9.41785 | -60.42533 | 2026-08-20 00:50:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 320.6 |
| ad32ed79-0e41-37a0-90d6-f40c85a1537c | -7.45028 | -60.00234 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 1b128df3-c0c8-3787-a736-9724f74d7920 | -3.09901 | -61.20696 | 2026-08-20 00:50:00 | TERRA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 79e8b500-5eab-3c33-a121-c7ca6ef27e8e | -8.49458 | -54.88203 | 2026-08-20 00:50:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 37.4 |
| 77e4545f-6a7f-3fad-a843-55999280ed14 | -6.43087 | -52.73463 | 2026-08-20 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| a9d478c8-a5ad-323e-8a59-81fa4d5a5c0d | -6.43508 | -52.76225 | 2026-08-20 00:50:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| ce8981a4-2419-3b34-92e6-e96f8aab3b38 | -9.12445 | -51.12819 | 2026-08-20 00:50:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 513efa82-3243-3d41-9a89-a41b1b528eb9 | -4.95561 | -56.27467 | 2026-08-20 00:50:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| 399dfe10-7669-34f7-ab69-c7c43ab2e429 | -6.24594 | -55.42979 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e41b5504-d6f7-3c94-a01d-544d9252ebf2 | -11.20648 | -55.04441 | 2026-08-20 00:50:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 75476513-b3b5-3c4c-9641-6be5b9195248 | -7.81386 | -62.32406 | 2026-08-20 00:50:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| a376cd75-3030-3996-95a4-b5931a32e77a | -9.11728 | -61.6073 | 2026-08-20 00:50:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 6318350b-cd2c-3756-b7a7-9810936985f1 | -7.87648 | -63.76879 | 2026-08-20 00:50:00 | TERRA_M-M | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e11ef2af-8861-3c15-b29a-a01a685fa809 | -6.7023 | -58.94035 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c9010027-5e00-3d85-8328-ea60f096a876 | -5.80652 | -55.73009 | 2026-08-20 00:50:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 06a01da3-9fc1-396d-972a-d3ae3057df25 | -9.11019 | -60.93748 | 2026-08-20 00:50:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| d71005c6-addf-3b72-a265-c8dc3ebb3e48 | -10.78807 | -50.31538 | 2026-08-20 00:50:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 1f32e707-e701-32c4-849b-559ebd0b21e9 | -6.80538 | -59.01805 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 20.9 |
| f886e143-4c31-3e90-9223-118ce89c2f73 | -6.87137 | -59.03216 | 2026-08-20 00:50:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6640f434-c568-3b47-b580-c3abcf64f9f3 | 4.34169 | -61.33759 | 2026-08-20 00:52:00 | TERRA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 478a04c0-3fcb-3339-a52b-b8e6d217b6a4 | -7.9751 | -44.6648 | 2026-08-20 01:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| 0e5a416c-1db6-3884-98b5-1d93fd317392 | -14.18 | -53.0564 | 2026-08-20 01:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 96423045-1b4d-3df9-a8dc-c78cc11ad4fd | -14.4559 | -45.6019 | 2026-08-20 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 081f36f4-363d-3423-8aac-15f457b97fc8 | -6.7114 | -59.0958 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 61bd2cc1-4bd9-3ff2-9d86-58e00ce371ee | -7.3603 | -45.8136 | 2026-08-20 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 379.0 |
| f3df0edf-357c-3e43-b1de-cc1e946cfc10 | -6.3863 | -54.9451 | 2026-08-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 283699af-d77e-313e-979d-74520b3e820a | -10.3276 | -57.5517 | 2026-08-20 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 51687939-3121-3591-b99e-e08b3296d3fc | -6.4392 | -52.7138 | 2026-08-20 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 532da26e-4667-3b91-948d-a149686f6f6e | -17.3365 | -43.6383 | 2026-08-20 01:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 133.4 |
| ac9248d4-d889-3be2-bb5c-5bb10bccd7ba | -12.4916 | -54.7364 | 2026-08-20 01:00:00 | GOES-19 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 69bf6245-96d2-3595-b482-1817dfb61f4b | -1.8425 | -54.4917 | 2026-08-20 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| cef91c82-4cad-3f44-97ff-06409165f4a7 | -9.4254 | -60.4545 | 2026-08-20 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 84a51377-1a19-3c2e-8d12-93a526f1623f | -9.2071 | -59.771 | 2026-08-20 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 913e6087-b754-312d-877b-3c59e5077428 | -14.4554 | -45.6251 | 2026-08-20 01:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 4bf0fd0b-a0ed-3f00-9106-7b708d2d15f4 | -11.1939 | -53.9993 | 2026-08-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 1882cae7-c2a0-39bb-9474-a537c6717d0c | -6.4391 | -52.7343 | 2026-08-20 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 51eee936-4b83-3c8f-99d1-5eabd3919316 | -17.3372 | -43.6139 | 2026-08-20 01:00:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 198.9 |
| 05b06f28-7bf8-3485-8e9c-93974577f6ed | -8.6725 | -54.6695 | 2026-08-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| bea95455-176d-3191-9ac6-2f1d4ed05e69 | -23.0838 | -49.1511 | 2026-08-20 01:00:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 97.7 |
| 3318b060-840a-3f1c-9f07-015e45340ed7 | -11.8083 | -44.8072 | 2026-08-20 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 155.4 |
| c032b8b8-9433-3d24-9b51-97796cd1ae0a | -6.583 | -58.9658 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 991b4954-908d-3377-a597-02363583ec67 | -6.6929 | -59.0966 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 9b3ab03b-d1cb-30bf-a2ed-274a52b65dca | -8.6727 | -54.6492 | 2026-08-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 172.4 |
| 3d21468b-45ed-36ca-b13a-0f425c3a3632 | -11.1936 | -54.0199 | 2026-08-20 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 69664f31-a051-353c-98a0-4677656226fb | -8.654 | -54.6505 | 2026-08-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| faedeb6d-1552-39ac-87fb-bdba69c6bbdc | -6.7123 | -58.9412 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.6 |
| eab0a1fe-9545-34f7-b76e-f98453ef0249 | -5.8088 | -55.7095 | 2026-08-20 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| a050084f-4faf-392a-9c56-c22cc6cc28e6 | -6.5829 | -58.9851 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 1f15385b-57e5-3156-8d8e-7e176f563c25 | -11.8275 | -44.8044 | 2026-08-20 01:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b535f38e-0ea7-3255-9ccb-38e4ad537784 | -6.6015 | -58.9651 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 1cf0c94a-efb0-3b4e-8c0b-1afb077e753e | -7.3415 | -45.8152 | 2026-08-20 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 233.2 |
| a8becc64-107e-3b09-9efb-05806ccaa5e2 | -9.2258 | -59.77 | 2026-08-20 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| b1c227bd-26ff-3c92-8451-2b3873886b72 | -9.207 | -59.7903 | 2026-08-20 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 3ac0036f-8a26-3008-9e14-04a2ab51ca61 | -8.6729 | -54.629 | 2026-08-20 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6dfe5fb9-fe50-33d5-9d46-cd23974d4bc1 | -7.3413 | -45.8377 | 2026-08-20 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 247.6 |
| 4581b4f1-8f12-3fb7-afa8-feb4640e435e | -1.8242 | -54.492 | 2026-08-20 01:00:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6bf70960-2ec3-317b-8b49-6925b6d40e35 | -2.5629 | -47.2445 | 2026-08-20 01:00:00 | GOES-19 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 7df7ffb6-adde-31ae-b1df-b52744926e71 | -14.1797 | -53.0774 | 2026-08-20 01:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 0fd84d44-ec89-320c-aadf-cc8c3fe75a44 | -9.4071 | -60.417 | 2026-08-20 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 07e03422-667f-3adc-ba04-776f82305637 | -9.4257 | -60.416 | 2026-08-20 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.8 |
| f204764d-32a5-311d-a7ae-fab9d3ce95dc | -11.2189 | -55.0585 | 2026-08-20 01:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 08e35d9e-0b1e-3b52-82c2-35c483fef66b | -9.2256 | -59.7894 | 2026-08-20 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 61cf2da3-7a6d-3e69-a16c-720a876b0633 | -5.8087 | -55.7293 | 2026-08-20 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 57cc0000-33ca-3daa-97d1-dfbb2e71e69d | -5.7904 | -55.7103 | 2026-08-20 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| cc612af0-35e4-3ac9-91fd-1f8dbd9707e5 | -7.36 | -45.8361 | 2026-08-20 01:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 383.7 |
| c0d2c7f9-6f29-3a35-b1c1-1ad856d27a4a | -9.12 | -61.6011 | 2026-08-20 01:00:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 9ebc84fb-c67f-312b-81ff-273bf3f6d5d8 | -6.4389 | -52.7548 | 2026-08-20 01:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 0dc7ee01-3b1d-35ba-a085-42912c457a3d | -14.1607 | -53.0587 | 2026-08-20 01:00:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 45813414-8513-3be2-a867-e84075a99d65 | -9.4069 | -60.4362 | 2026-08-20 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| d386bbff-aaa6-3f18-9985-e40a79d87759 | -10.3274 | -57.5715 | 2026-08-20 01:00:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| b3cf8001-d150-3723-8b10-5dac5cb72998 | -9.4256 | -60.4353 | 2026-08-20 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 153.3 |
| d308a8ec-33fb-3793-9e50-5e78b8d56acd | -23.0831 | -49.1746 | 2026-08-20 01:00:00 | GOES-19 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 48357746-5a42-3680-8b96-ce29437dbe23 | -6.6938 | -58.942 | 2026-08-20 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4f6a4afa-f297-35ec-b398-84ad439b3f2e | -14.2123 | -52.886398 | 2026-08-20 01:02:00 | METOP-C | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 306aac28-e6e0-33d4-bf04-d2476d5afaa7 | -1.8315 | -54.486301 | 2026-08-20 01:02:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3eb1b0-02a9-3305-9380-c7014ec8440b | -15.0104 | -52.723202 | 2026-08-20 01:02:00 | METOP-C | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3eab096e-3af9-39ff-aa8b-03368a037d87 | -6.2332 | -55.612301 | 2026-08-20 01:02:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d007e65-19f4-31b3-9c95-7d047c0ad82a | -8.709 | -49.606899 | 2026-08-20 01:02:00 | METOP-C | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
