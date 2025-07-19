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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89fcc42d-b80d-3719-b672-9fcb8975ca1f | -12.98816 | -46.93877 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57296e07-18b4-3801-ac73-e1574fd37b3f | -17.76768 | -44.57354 | 2025-07-19 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 98322ff9-2d68-3ca3-9ab4-0e582ffa5736 | -11.82468 | -48.21741 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9eb65b6c-c8ce-34ee-a79b-f2a3077d39b6 | -10.37826 | -49.90031 | 2025-07-19 04:10:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 807d0494-22a5-3236-b68a-8a66d207b283 | -11.4713 | -47.32292 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b6a79723-f199-339b-b7f7-673691250830 | -15.89184 | -43.45637 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| f342b354-f545-3182-8866-f8e57850ee7b | -17.76654 | -44.58076 | 2025-07-19 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d8de55a-f826-3df5-b130-10a1f239ee7d | -17.69421 | -44.26128 | 2025-07-19 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 55413b7c-8704-34e9-b918-3b4803141597 | -12.06482 | -47.34764 | 2025-07-19 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45ad8136-32c5-3286-8b54-47f687298e2f | -12.3765 | -50.33469 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d748fff-ce51-36c4-8674-f36018252b2d | -11.56205 | -47.08199 | 2025-07-19 04:10:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58f79f38-8ad5-3e2d-bc23-dd91f815a0ae | -12.98752 | -46.92039 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b839106-aad7-3aa3-8365-4bba7a30ccb9 | -12.43182 | -45.37092 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a3b96ec-2cd2-39e0-9d53-b0a8e4015b35 | -11.96634 | -47.0157 | 2025-07-19 04:10:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc4a6b35-cdd8-3316-8892-035e7a542f54 | -13.52909 | -44.2904 | 2025-07-19 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6a2cf56e-d5c8-31a9-b2e2-841f7a772ba2 | -10.75874 | -52.76405 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 60b33482-feee-3247-8c32-495372536615 | -15.92733 | -43.5133 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ef8e801c-db3f-3e6d-8689-2844d1161fc1 | -14.70595 | -45.07193 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a05290c-aed1-3060-a6f1-4653de0eb7c8 | -12.9919 | -46.93917 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 642ab960-a2c2-39c6-a166-d089b65d7e04 | -12.99496 | -46.92145 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b00c18ea-57f2-36d6-afe2-8dd33e704567 | -12.42144 | -45.36916 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 81a0685a-5739-3626-ab24-cc7ec3b0eb85 | -11.48461 | -47.32277 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 9c5015aa-dc7b-348b-88bf-f9ae0dc6e253 | -14.47966 | -46.3584 | 2025-07-19 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f6b903d-aa99-373c-a7a4-799543907731 | -13.60342 | -45.64113 | 2025-07-19 04:10:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80537699-2304-33d2-9b3e-84ee08a78f61 | -11.52578 | -48.95433 | 2025-07-19 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b25958a-ae1d-33b3-9977-ab4c86883f0c | -15.92074 | -43.92657 | 2025-07-19 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 0.4 |
| f9745a8a-98d0-3452-be10-6d6b44c3d9a2 | -14.12972 | -44.23919 | 2025-07-19 04:10:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 55a5e15e-15a4-3f71-a94a-aac27c0f3d2b | -16.37747 | -43.0361 | 2025-07-19 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fde5737-a596-3f1c-bcb8-56303b9088dd | -12.06397 | -47.35253 | 2025-07-19 04:10:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e438d5b0-d572-3bba-9390-b8d3595906e9 | -13.12323 | -43.48552 | 2025-07-19 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27c5998a-a0fb-354b-a406-479f43d8fd55 | -12.03473 | -48.7566 | 2025-07-19 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba69276c-6318-3e6f-9340-40c2502d7a7c | -15.54496 | -42.65728 | 2025-07-19 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| e9aa0899-7b50-3c3f-9a4c-3f6fc36fbd76 | -10.82041 | -49.28769 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca39ff4e-052c-3b43-b1c1-cee9eae24e98 | -11.46142 | -48.16365 | 2025-07-19 04:10:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 81cb6e8c-5ed3-398a-acfb-a8b6145c7743 | -14.48319 | -46.35901 | 2025-07-19 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbce96df-d34d-3bb8-825d-d001c20146b7 | -15.72741 | -46.86292 | 2025-07-19 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a6aebe4d-2cf3-3014-b708-98d09af1c9ac | -11.48593 | -47.33058 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f90d4f4f-9b9b-3021-b568-560c50d9552a | -15.50942 | -47.84243 | 2025-07-19 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 56955f0d-fc1d-3ace-80e5-2510d860c4b5 | -11.83474 | -48.20776 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 235b04fa-4344-3750-973d-fdd9dd1eda3a | -11.37176 | -54.34299 | 2025-07-19 04:10:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 528012e4-7245-3939-ab8a-fbb2b4ac2214 | -13.67969 | -44.22288 | 2025-07-19 04:10:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 055809b6-a86f-3cc7-bbe4-4d229eca6a1a | -17.69146 | -44.25711 | 2025-07-19 04:10:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71eeefe5-67a1-31c9-86eb-e331c70d92f0 | -14.7807 | -48.29488 | 2025-07-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6a48ff8c-6c81-3ee0-9546-49ad58cf9662 | -11.49062 | -47.32636 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a7c90149-b83c-35de-9dca-ac07b7f0318d | -11.73668 | -48.19437 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 35.2 |
| 689c248a-6df4-39d4-bae3-4c1e4c6c8362 | -15.2379 | -47.9479 | 2025-07-19 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bc4cd780-4d2c-3fb1-8c27-d65cd48a1f9b | -14.75219 | -48.27417 | 2025-07-19 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 643e31a4-e0f8-34a6-bb62-2bc7679dc947 | -11.5236 | -48.9571 | 2025-07-19 04:10:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34cdb83f-0080-34d4-ba21-00d1011f45ed | -14.83623 | -49.11788 | 2025-07-19 04:10:00 | NOAA-21 | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f4dd1b8-a322-31ad-a440-21b6cfd38594 | -13.39431 | -44.13521 | 2025-07-19 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d02e4665-6ef8-3c17-9f02-90ca209ab53a | -16.77186 | -49.38046 | 2025-07-19 04:10:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa573dad-4768-389f-aacd-2a506cb71f96 | -11.82939 | -48.21442 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 46ffed79-e945-32c4-bfa8-26aa6bb2b21e | -12.46782 | -46.92836 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 402587c9-043e-39bd-ad55-ec71828a69f2 | -11.96467 | -46.39669 | 2025-07-19 04:10:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b44f15de-3582-3af0-a2ee-e4c2d5fa38c7 | -14.70318 | -45.06768 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 50b2432c-2cdf-3c65-a479-671bfbec7570 | -12.36725 | -50.33296 | 2025-07-19 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 220489b9-c085-31a4-8918-6b6e8dd979f7 | -10.88064 | -47.15084 | 2025-07-19 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ef54625c-a416-3c7e-9ec5-2bd7afd9ad43 | -16.2235 | -41.78787 | 2025-07-19 04:10:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| db227202-3414-303b-aa0c-89a3f6ead513 | -12.42773 | -45.37421 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b39a03e-b93b-3095-ab09-59b6dd26fb06 | -12.5756 | -44.75221 | 2025-07-19 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 257b4fa4-5567-3d4d-971c-4d13f65d187b | -11.8341 | -48.21144 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2d2b9a22-8d51-3d45-be87-a51687094ffb | -11.47213 | -47.31803 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e324fd5e-1088-38cc-a1eb-78e44d79e210 | -11.73255 | -48.52262 | 2025-07-19 04:10:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e84c2174-aba7-3f68-9a31-5cec508c0280 | -11.8388 | -48.2085 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 52d84534-8984-3d45-bd00-8c859c5bcc19 | -13.04809 | -49.1768 | 2025-07-19 04:10:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 170ead17-89a8-3aea-8060-f1ccfc111b11 | -11.47903 | -47.32428 | 2025-07-19 04:10:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bea77a95-27ee-355b-b947-6e6de03e173e | -11.73387 | -48.18642 | 2025-07-19 04:10:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 669abcbb-3cdc-3b00-9158-129743c4cf38 | -16.89839 | -52.67725 | 2025-07-19 04:10:00 | NOAA-21 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f731b8c1-be0e-30fa-9c87-0d69a0a811a7 | -14.70776 | -45.06091 | 2025-07-19 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cb750d6c-0b36-3191-8c8d-acfa33f0ad75 | -12.96465 | -46.9205 | 2025-07-19 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a0f3bcc-160a-3e8e-9c7d-1a33c2669e0b | -10.80292 | -46.76701 | 2025-07-19 04:10:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b8a3b809-78d7-3f1d-bee3-a0c7ef0ed190 | -15.92347 | -43.51633 | 2025-07-19 04:10:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98833ad7-c9e4-328d-b0f7-78c275b7c5e7 | -22.98845 | -48.64375 | 2025-07-19 04:12:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6429f349-536c-3857-be2c-439972cf3ffb | -22.70219 | -47.25206 | 2025-07-19 04:12:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fdfae26-ba8d-328a-92b4-ddf56bdb87b4 | -22.70535 | -47.21215 | 2025-07-19 04:12:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 63280006-7f18-30ab-8300-6a5621c87da5 | -22.50628 | -47.11903 | 2025-07-19 04:12:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b4ebb1e4-5915-37fc-adde-489cbce2f9cf | -21.7507 | -52.44228 | 2025-07-19 04:12:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ad0371b-2c12-3cd9-a496-66f329a189f1 | -23.16745 | -47.39638 | 2025-07-19 04:12:00 | NOAA-21 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47d3c503-1e0e-38b5-9a21-eae735c4c5f7 | -20.99465 | -49.76724 | 2025-07-19 04:12:00 | NOAA-21 | JOSÉ BONIFÁCIO | SÃO PAULO | Brasil | 3525706 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b815e846-0375-3c40-b9e5-b0372e4b73c4 | -23.76495 | -49.63185 | 2025-07-19 04:12:00 | NOAA-21 | SANTANA DO ITARARÉ | PARANÁ | Brasil | 4124004 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| f6ff8965-d02d-3f65-bc91-c6727147c24d | -22.05696 | -48.16328 | 2025-07-19 04:12:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4445f6ec-2757-3f96-a219-cf01acf81a7f | -21.03958 | -55.98334 | 2025-07-19 04:12:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6840e2f-7bdf-3cc3-a054-b90104b2b285 | -21.86874 | -56.73753 | 2025-07-19 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8180926b-ca77-39e1-831a-0dc047c36b8d | -22.83699 | -46.84554 | 2025-07-19 04:12:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| b18d70ca-561d-3a60-8fda-62ce1d48c579 | -23.60832 | -49.01255 | 2025-07-19 04:12:00 | NOAA-21 | ITAÍ | SÃO PAULO | Brasil | 3521804 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 78ed5576-c176-3fcd-a50b-8a41bee676c5 | -21.03867 | -55.98737 | 2025-07-19 04:12:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6655553-c435-305b-a0d4-0c1198231808 | -22.58794 | -47.40968 | 2025-07-19 04:12:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a19af55-3a81-3a81-9051-d940e582d398 | -23.4873 | -45.37026 | 2025-07-19 04:12:00 | NOAA-21 | NATIVIDADE DA SERRA | SÃO PAULO | Brasil | 3532306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 07e5b4b0-0e62-3f82-b5b9-f0c109023b2c | -23.5458 | -47.06909 | 2025-07-19 04:12:00 | NOAA-21 | SÃO ROQUE | SÃO PAULO | Brasil | 3550605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97192ce5-1a99-3f5d-9cd7-25bfc684dca2 | -22.70623 | -47.24879 | 2025-07-19 04:12:00 | NOAA-21 | AMERICANA | SÃO PAULO | Brasil | 3501608 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8926702b-60f7-35d3-8b00-159fc5520759 | -21.86775 | -56.74183 | 2025-07-19 04:12:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85a89f2b-908e-3290-be50-666ae16f0a54 | -22.56352 | -45.23481 | 2025-07-19 04:12:00 | NOAA-21 | DELFIM MOREIRA | MINAS GERAIS | Brasil | 3121100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1280a1b6-1a3f-3a84-97de-161e341fedd7 | -22.50965 | -47.11969 | 2025-07-19 04:12:00 | NOAA-21 | ENGENHEIRO COELHO | SÃO PAULO | Brasil | 3515152 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43490b71-d60d-36a4-ae89-8d9f4b7145ff | -21.777 | -44.33137 | 2025-07-19 04:12:00 | NOAA-21 | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e762ed3-a736-36a7-98f9-f30beee65952 | -24.11856 | -49.11051 | 2025-07-19 04:12:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ba49c3d2-4e4a-30c9-8af1-c0654050202f | -23.34852 | -46.10559 | 2025-07-19 04:12:00 | NOAA-21 | GUARAREMA | SÃO PAULO | Brasil | 3518305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 44b4d80d-6c46-309e-89a3-73675b5e0d7a | -22.98382 | -49.17958 | 2025-07-19 04:12:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c0675dfe-e730-3262-812d-b59e08c64a47 | -23.32426 | -50.13483 | 2025-07-19 04:12:00 | NOAA-21 | SANTO ANTÔNIO DA PLATINA | PARANÁ | Brasil | 4124103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bad8c398-4918-39c3-8e0d-cea7eb5d2805 | -22.06046 | -48.16402 | 2025-07-19 04:12:00 | NOAA-21 | RIBEIRÃO BONITO | SÃO PAULO | Brasil | 3542909 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a54a05ca-7771-3097-8735-a9ad5aaceb66 | -22.83366 | -46.84483 | 2025-07-19 04:12:00 | NOAA-21 | PEDREIRA | SÃO PAULO | Brasil | 3537107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |


[Clique aqui para ver as próximas entradas](README16.md)
