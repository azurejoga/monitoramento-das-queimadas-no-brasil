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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21440281-f55a-3fd5-8db8-3fa026d70d74 | -7.24644 | -44.76918 | 2025-03-04 03:36:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1d5e259d-3eda-3097-8097-98885ee18549 | -8.51776 | -36.38554 | 2025-03-04 03:36:00 | NOAA-21 | SÃO BENTO DO UNA | PERNAMBUCO | Brasil | 2613008 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 61cea486-2904-32ec-8ac8-c9bb64d07fbe | -7.3788 | -34.88607 | 2025-03-04 03:36:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 4951c879-775f-3275-b6ae-f9ac7a7f10a2 | -13.98641 | -45.57671 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 079a4ca7-06b5-3ca4-ba1f-981c8a2e6cbd | -13.99999 | -45.5955 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f0c3036-8844-3730-b48a-8aecfbd88fa3 | -15.11204 | -42.49814 | 2025-03-04 03:38:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2f73312c-0265-32d6-aae6-5606ab7a0228 | -13.99442 | -45.59435 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fc8f2ff9-f020-35db-b1b6-5673d977097a | -15.11023 | -42.49572 | 2025-03-04 03:38:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 05d07e4a-9b06-3c99-912c-6195b2e1243f | -13.99364 | -45.59821 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a12b96fc-1ab8-312b-9042-6ec33d29160d | -14.01452 | -45.63861 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3ee7ca79-903c-31fc-811e-b0dcae2038c7 | -13.99921 | -45.59935 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3ef69309-ae1c-3cd8-abcc-e01dcf4f2241 | -14.02569 | -45.64091 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| de2075a8-5b02-3ec8-b89d-fbbd56cfd90a | -14.01685 | -45.62704 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71968627-e063-3434-8591-d382359524d0 | -14.02088 | -45.6359 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1d64b883-eab2-3969-9698-3b4691f99993 | -14.0184 | -45.61935 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ca8783e-6d2a-378a-94bd-cfb6840ef6fb | -13.98963 | -45.58935 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2c4f1486-b4ac-31a0-b934-26e3aa4964a2 | -14.03204 | -45.63822 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e6d98d7-31d7-3fcd-be5a-fe338ff873c5 | -13.98779 | -45.57765 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 70d29742-e6ad-33cb-a601-8f6b5602db0e | -14.02491 | -45.64477 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b96890a6-2740-369d-8f79-7ac64c75624e | -10.69692 | -37.0509 | 2025-03-04 03:38:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 5bcb417a-0173-3983-80de-98cce18e5273 | -13.99197 | -45.57787 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 595e44b9-2787-3a7b-ac9e-bc39e7f9f6a8 | -14.01529 | -45.63475 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dd6d7c98-e4cb-3475-a3ce-53e93307e7b7 | -14.01127 | -45.62589 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f403e7a-f023-308e-b918-52c0cc4da4fe | -14.028 | -45.62936 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 62fcb6fa-a622-3414-b06e-f25bd472a444 | -14.00077 | -45.59167 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e52c5f82-0abc-35a3-bf6d-b200e92b4d5d | -14.11918 | -41.67844 | 2025-03-04 03:38:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e06f05d4-4aee-37ec-85e3-4e931590ece1 | -14.02243 | -45.62819 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b71f438c-794c-3489-a668-a0b528302df6 | -14.0305 | -45.64592 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1bba8a08-0712-3b88-a6c4-bc3fa00e1bee | -13.99041 | -45.58551 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7c047e8-a51e-3b24-a230-8878ac60efeb | -14.02723 | -45.63321 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5f9d2682-41df-3fc2-8427-e701fa907417 | -13.99285 | -45.60207 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a1c589a9-e1b9-37a6-8b17-e58dfd7e7f87 | -14.01049 | -45.62975 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4721eb75-2de3-39f0-8e58-6c1efed14e0c | -13.98704 | -45.58148 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c2d6d899-7ace-35d8-b380-77cb645589ec | -14.01762 | -45.62319 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 121150e1-c6e9-3475-80b7-dcc80fc56cc4 | -13.99598 | -45.58666 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0d6a3038-540c-3d43-ad82-d14926702576 | -14.02878 | -45.62552 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a6f004a7-4ef0-32f6-8e72-24d807b5e8c8 | -14.03127 | -45.64207 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47947cfe-d603-331e-83d4-293f627959a9 | -15.11469 | -42.49659 | 2025-03-04 03:38:00 | NOAA-21 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 5abda854-f06a-3bfb-9c60-e1b7da95c9be | -14.00568 | -45.62476 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| beef7a02-f79e-3f2b-9812-11ce327fed03 | -12.24306 | -40.97624 | 2025-03-04 03:38:00 | NOAA-21 | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f394ed0e-9ddb-3035-a925-b992be717f92 | -13.9952 | -45.5905 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 82e95261-bd98-3659-ab61-f186d38158a7 | -14.01933 | -45.64361 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d69c6d41-e87d-385a-adf0-af9da3bd99e3 | -14.01855 | -45.64747 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e639a201-03f9-3cce-a201-2a3cc15cfb45 | -14.01607 | -45.63089 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 57eaa20c-440c-3264-ab9f-6445e48ed4ff | -13.4758 | -44.0198 | 2025-03-04 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fbdd38e5-a8b6-3020-9104-322b642d2cc9 | -14.01204 | -45.62203 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 06228a8d-2cad-3839-9ec7-beae27fe7833 | -11.463 | -48.01003 | 2025-03-04 03:38:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 600be7a9-dfc7-36d7-9d9d-0eeb5db5cfef | -13.99275 | -45.57405 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1e4589d9-8f08-3517-ae5c-1ab5757b3d8a | -13.47521 | -44.02287 | 2025-03-04 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ea816ba-7df8-3af7-a439-8b43af6d53de | -14.02165 | -45.63205 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2f12063a-a47e-3081-a0b2-25cbe734d63f | -14.0201 | -45.63976 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 388becee-4d48-34af-a909-1e54b172d88b | -14.02397 | -45.62051 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dcedadbb-06eb-3b54-8734-617f7e7c77ac | -13.99119 | -45.58169 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d201f69a-b2c4-3b16-8e6e-854b3880a38f | -13.98885 | -45.5932 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a4d7a3c4-4929-387b-803d-88f1de41683f | -13.98629 | -45.58532 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f2af3186-fadd-3f0d-b6ea-ce37ccb780a6 | -14.02414 | -45.64863 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e77ae676-7ef4-3875-a83f-c9ad0ed7ffcc | -13.99753 | -45.57904 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 47bf6ccb-4601-38d9-9c79-c70db87c9002 | -14.02646 | -45.63706 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9600c40e-7856-362d-b10a-14546809a14e | -14.0232 | -45.62435 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1e0b73b-c411-3baa-a6ef-deaeab80eefc | -13.48244 | -44.04029 | 2025-03-04 03:38:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3219edc8-1c1c-3308-99ba-0fa28a1edf95 | -13.99676 | -45.58285 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| be95d440-1197-3487-a14a-4e03329ea9e1 | -13.99843 | -45.6032 | 2025-03-04 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 95be77a2-a487-3277-93df-90a08fa5e081 | -23.33936 | -46.77219 | 2025-03-04 03:40:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e0d1ede5-6eb7-348e-9ca9-ec0458d1984c | -20.50136 | -41.87607 | 2025-03-04 03:40:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ed1ded4e-3ce0-372d-b670-a154be087995 | -22.54062 | -48.81513 | 2025-03-04 03:40:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8038602d-1dcb-36b2-848b-0c3ab86b94f5 | -21.63508 | -48.68564 | 2025-03-04 03:40:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 295d31f1-2f65-3297-8c79-dc3fbc8a0ca2 | -21.63023 | -48.6801 | 2025-03-04 03:40:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 46395644-76db-3a5e-b306-0d7f3126916f | -23.01037 | -50.40538 | 2025-03-04 03:40:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| a599083a-30ec-3102-afa9-466544b8b8db | -20.82245 | -48.92342 | 2025-03-04 03:40:00 | NOAA-21 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fc1612f4-5aa9-3e81-9c4d-ecb146a3729c | -23.01334 | -50.40856 | 2025-03-04 03:40:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| f76078fc-8d2c-36dc-972d-690fc18179d7 | -22.86974 | -43.11447 | 2025-03-04 03:40:00 | NOAA-21 | NITERÓI | RIO DE JANEIRO | Brasil | 3303302 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| b807b3b2-e90a-33e4-9759-2e8b60a92d8a | -20.76546 | -45.5752 | 2025-03-04 03:40:00 | NOAA-21 | CRISTAIS | MINAS GERAIS | Brasil | 3120201 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad6328ab-2f76-3b9d-ab06-dc0cf808ec99 | -22.85711 | -42.98274 | 2025-03-04 03:40:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8b58c43b-49e9-3941-8ffe-c7e3e31230df | -22.54126 | -48.81204 | 2025-03-04 03:40:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ff8901b2-bcdf-390a-aa0a-dcc591282892 | -22.78671 | -43.75587 | 2025-03-04 03:40:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 12929ca5-36cd-33c8-9e12-471dcdd8b03a | -21.43917 | -43.55599 | 2025-03-04 03:40:00 | NOAA-21 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd5bf9b7-f3c5-3a32-8986-695e8580629c | -20.74127 | -48.5405 | 2025-03-04 03:40:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5922ff93-995b-3a79-ae61-08836fcfb53f | -23.40745 | -46.5561 | 2025-03-04 03:40:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 68f7eb85-4db8-3669-89a2-00d7e3ce1dd4 | -22.16125 | -43.10173 | 2025-03-04 03:40:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8b384370-9c14-3639-9c67-cd827de8c8e0 | -20.74027 | -48.54498 | 2025-03-04 03:40:00 | NOAA-21 | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9382f8d2-fa0f-3176-b22f-3d632d7c9d56 | -17.67715 | -42.74191 | 2025-03-04 03:40:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4fafc40e-5bdd-3fa3-b05b-816734fd55f4 | -21.63608 | -48.6813 | 2025-03-04 03:40:00 | NOAA-21 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c315780a-0560-3215-96e1-2fd30b2fa7c1 | -20.83888 | -44.66792 | 2025-03-04 03:40:00 | NOAA-21 | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 4d80cd10-24d4-3054-ac38-47f736682f20 | -20.82943 | -48.92049 | 2025-03-04 03:40:00 | NOAA-21 | CAJOBI | SÃO PAULO | Brasil | 3509304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 791ae107-6e3e-3f53-84b6-ea7a81dad59d | -23.00719 | -50.40667 | 2025-03-04 03:40:00 | NOAA-21 | ITAMBARACÁ | PARANÁ | Brasil | 4111001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 84322569-81ab-3648-8451-bddf8ba3c561 | -21.61081 | -48.47464 | 2025-03-04 03:40:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cee1e9e9-3b56-309a-8020-40dfa5e6c8db | -21.61184 | -48.47023 | 2025-03-04 03:40:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e28ea3c-80c2-3fa4-8e5a-c5fc227d43e5 | -22.78912 | -42.80793 | 2025-03-04 03:40:00 | NOAA-21 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1486b1a9-f6d3-324a-87ff-b66ea04b79d1 | -23.5039 | -51.69444 | 2025-03-04 03:42:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 12e7bc0e-b4c4-3b99-b22e-99284dd326d9 | -23.5054 | -51.68857 | 2025-03-04 03:42:00 | NOAA-21 | MANDAGUARI | PARANÁ | Brasil | 4114203 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 4f44aec1-5ea1-3090-8592-b5e309fc8fb6 | 2.3421 | -61.06 | 2025-03-04 04:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 66e09b05-2d68-3e8b-8d28-507164eced67 | 1.121 | -60.5224 | 2025-03-04 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 79053a82-3535-36d1-bd5f-af153dc958b2 | 2.3604 | -61.0597 | 2025-03-04 04:00:00 | GOES-16 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 84.3 |
| cdda16e9-5a22-32e9-8b04-bed6ad5a18ae | 1.121 | -60.5034 | 2025-03-04 04:00:00 | GOES-16 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 6e906492-38ae-3348-99d9-b22dcfdde4c4 | -14.028 | -45.6304 | 2025-03-04 04:00:00 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 37c05932-b2ef-32a7-b3b7-6280181ad7a9 | -8.43552 | -36.34735 | 2025-03-04 04:01:00 | NPP-375D | CACHOEIRINHA | PERNAMBUCO | Brasil | 2603108 | 26 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c42a40c1-6fde-3884-adba-c347d948d28d | -10.5363 | -44.66726 | 2025-03-04 04:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c5d6f28-0433-3cc4-8b5c-6c6bd8532372 | -11.46047 | -48.00823 | 2025-03-04 04:01:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f49e68e3-4a7a-342b-8b49-fd88fb0ab86f | -10.53553 | -44.67174 | 2025-03-04 04:01:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e0190974-68aa-3fdd-8426-03d92c8079e9 | -11.97206 | -39.61646 | 2025-03-04 04:01:00 | NPP-375D | PÉ DE SERRA | BAHIA | Brasil | 2924058 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |


[Clique aqui para ver as próximas entradas](README3.md)
