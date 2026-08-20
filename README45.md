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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cfef92f-d217-3132-8654-6ef762f920c3 | -5.49166 | -60.12906 | 2026-08-20 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f42209ab-3378-32eb-9e15-788ad1f0d8b0 | -6.74215 | -59.04115 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75241824-1abb-331d-b28e-95cfa69b6d88 | -6.14323 | -47.22542 | 2026-08-20 05:04:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f2c99012-6ebf-3021-bf08-b8b993aad9a4 | -4.46274 | -55.45722 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bffe6f26-cbc1-30e2-b001-c9c236a8ea20 | -4.45943 | -55.45671 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9b1fd6e2-955d-3e49-b19b-5134eb6fc4d0 | -4.61985 | -55.73615 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0dfa2ea-16c0-3ce8-83b5-a63b992c5fd7 | -7.05416 | -56.52203 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05c1bacc-bfaf-35ac-a162-c48ae8dcc1c2 | -6.8903 | -56.43875 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e33e2e45-4584-37c1-9941-0630cf5134e8 | -6.70212 | -58.93443 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| e97d2c32-f4be-377f-a11f-f293eb30b2d7 | -6.41809 | -54.94966 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e07dc57a-da52-3e5e-b6d0-8176b3236d25 | -6.70457 | -59.09028 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5a09af82-efbf-3919-beed-2ed1939bb989 | -5.80141 | -55.72422 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d521157-18a6-3267-a237-06f88c716e13 | -6.70029 | -59.09381 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e3b4cba5-8514-31d7-80d0-c75989d26a65 | -3.47578 | -47.69917 | 2026-08-20 05:04:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ff1a4405-3950-3126-bbdf-362d66b96e35 | -6.52739 | -55.05634 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70299fe1-d065-34f8-afaf-baf47ed85a4d | -6.656 | -59.08367 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7e10de5a-ff75-3a6a-aa81-e8105b3cee17 | -6.35382 | -54.90396 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4ffec90-1b72-37c2-92f0-6695ad1d9b70 | -6.69432 | -59.09819 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b849c05c-58b2-30b6-8492-26e9aa923b0c | -4.43722 | -55.37916 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 359359af-7eb9-38b6-a317-c5fb417bdeca | -4.01541 | -48.96138 | 2026-08-20 05:04:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58efc69-0a37-3386-88d9-7970638476c2 | -6.11262 | -57.74411 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 72780693-f3e3-3fd7-afa3-0e4e189c40cd | -7.95898 | -46.91995 | 2026-08-20 05:04:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e484aab7-74d9-3a74-a4e5-6dd98cc6c40d | -6.52406 | -55.05582 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 30d8caca-f9da-3731-9d25-8e2d61de113f | -6.24014 | -55.41867 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa806c93-8647-3418-9dc8-4e9fb15ccd5c | -6.40808 | -54.94812 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d7774885-600e-3d13-837e-006fee75394f | -6.71243 | -59.08739 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e617c26a-d7e8-39f0-a664-8dcef0fb4719 | -7.97209 | -44.66635 | 2026-08-20 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.8 |
| cd297487-ee14-36da-9ec4-fc2caf11a500 | -6.29531 | -43.64439 | 2026-08-20 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 765a98eb-a79d-3a70-9d25-8a65b62d733b | -5.99943 | -57.86044 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7fbfca8b-f0ba-3da7-a12b-0279c502808d | -6.64656 | -56.41048 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 457f8603-c806-3174-abc3-eeabb2af2e17 | -7.29048 | -52.53715 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d60956f3-9dfa-331f-831f-c3392e5b6b12 | -6.09274 | -57.91335 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a84b2e1d-8ec7-3666-a0e5-48c134ac6b60 | -6.60125 | -56.37496 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c1b3bd2-8688-3e0d-97ec-b6389fa4bdc0 | -6.69855 | -58.93379 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0e3602e3-b1b6-3bb9-b914-e1265ff08285 | -6.69006 | -59.10171 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| cc43446d-1b2a-3278-91bd-41bdc0ab09ec | -5.80364 | -55.73163 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 1f4c992a-8e3e-38b6-afff-0ce3f6f65f51 | -6.34715 | -54.90292 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d1c1de0-88f4-3ac9-9ef6-72720a289431 | -6.69924 | -59.0905 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8aa891f8-0eeb-3674-acdf-a38c2a229881 | -6.00227 | -57.86475 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c71e096d-a1ed-3e50-9ba9-5047059954aa | -7.34287 | -45.83433 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| db061ec2-2236-3604-9aab-b56b0d95d73d | -6.00002 | -57.85672 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd69f8e0-de9d-3411-b255-3745271f255f | -6.44393 | -52.72313 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cc3583d-956a-3bf8-b52f-a31292e7f6d2 | -6.61989 | -56.32106 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 295814ae-7a71-3f59-a5db-63fe9512cd90 | -6.70611 | -59.10333 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 79f64bdf-a643-355b-9a0b-eba169efc237 | -2.04735 | -48.039 | 2026-08-20 05:04:00 | NOAA-21 | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 8dc18e61-88e0-347f-9d4a-fd728b8af5ab | -6.60179 | -56.37149 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d64766d3-7ad3-34e5-a46a-1188038cb437 | -6.39145 | -57.4686 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f7e02155-03db-3aa7-8e67-cb02e981ad38 | -6.44191 | -52.7612 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7e0e782-58fc-3053-94f6-3c83ae09b46c | -6.83736 | -56.45179 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 05efd5cd-33b0-3be7-a609-23f2ff7fc17d | -6.08989 | -57.90904 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5986b524-1562-3636-b145-e03f0b4f6629 | -4.28548 | -46.51509 | 2026-08-20 05:04:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fdf2bf2a-d5fa-337f-845a-2469a7589e81 | -7.76131 | -49.20703 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 121b61f3-c608-3d76-b68c-db0b8f16758f | -7.75671 | -49.20637 | 2026-08-20 05:04:00 | NOAA-21 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fa983183-0406-30b9-82ad-7bfb52c57e01 | -2.67712 | -51.88632 | 2026-08-20 05:04:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef81f0a2-0468-3956-a7e7-5dac98160877 | -5.79918 | -55.71681 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71b5f57e-864f-3712-9313-5a6a5b301bd6 | -3.10893 | -61.20837 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 907db701-87aa-3298-8e94-29c601fcdf4c | -6.6979 | -58.93785 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 539c8c20-4b78-399d-a1ff-7ae78e541788 | -6.59457 | -58.97241 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21137de4-8c3b-3c14-836a-9da73c895077 | -2.50731 | -51.82769 | 2026-08-20 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 508d2b6a-adc7-3d2f-adc1-a11b4cc0de40 | -6.34048 | -54.90188 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8ae59729-3a99-37d5-ad80-b32b8e9682bf | -3.01702 | -51.0621 | 2026-08-20 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8239721-1829-3056-91fe-c30cfebbdc41 | -6.58608 | -58.97946 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b9cae647-19f4-3fd9-8f00-bcaa107fbf77 | -6.14448 | -57.85248 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6814fe02-2833-3589-8ebc-f05f15d2d311 | -6.69725 | -58.94193 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 96cec9f0-ed2e-3e83-8b74-d0bd049b22c4 | 0.80935 | -59.86838 | 2026-08-20 05:04:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f460e698-815d-3c6c-aaaa-77ee3e943e83 | -7.04714 | -56.60994 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c9d7066-d443-3737-b617-705c4d233938 | -7.35973 | -45.83074 | 2026-08-20 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 8656cc9f-76be-3207-89dd-0a17128ce37d | -0.97959 | -47.50061 | 2026-08-20 05:04:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a2924bd9-ebf2-3137-8577-11647adf74c3 | -6.44912 | -52.76228 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7dd13ee3-3e13-3dcd-905b-2336b81327c2 | -6.70568 | -58.93506 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69c768ce-f207-39c3-b7af-f8b942d4f288 | -6.0881 | -57.92033 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dad88acb-e4bb-320c-abc3-949d0f9db29b | -6.14206 | -57.86745 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a7198c9e-af2b-317c-8c60-4c5a9e533aa7 | -6.47001 | -55.51455 | 2026-08-20 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ce479535-0520-3464-a2e0-9424ea3e751e | -6.84834 | -56.42506 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 617d08bb-b9b4-39b0-97cb-5442ad00d14a | -6.62266 | -56.32504 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49c2cd82-b561-3576-a5ff-f0d58a028a5b | -3.10192 | -61.22401 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d5eefe3-6cd8-3f86-ae60-ca9bcde892bf | -2.57433 | -47.20278 | 2026-08-20 05:04:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a5cfe39a-5fac-37b4-80bf-3942d0055ea9 | -6.7068 | -59.09916 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ba72f310-77c0-3b02-8cd8-f2273ce67e25 | -6.74282 | -59.03704 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3f12c27e-96f6-37d6-937b-b15e2ef0c16e | -6.71468 | -59.0962 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de5421db-e81a-3734-99ff-d6b0d481ca1c | -6.78206 | -42.88389 | 2026-08-20 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 87f7ad61-fbdf-3435-b342-cb993ab47b29 | -6.58966 | -58.98006 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce074158-ae86-3d16-8d86-9c47b3dae11d | -4.38914 | -55.47039 | 2026-08-20 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37278e83-32da-3513-ba57-26fdcc86e0d4 | -6.60828 | -58.39316 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8afd73a9-e6f1-30f8-adfd-b04b82933aea | -1.84137 | -54.49047 | 2026-08-20 05:04:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb8394e4-73f7-334f-a12f-57389fa53fcc | -6.0875 | -57.92409 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 388a48bd-01cf-3a50-b6ce-337acd9e45f2 | -5.79311 | -55.71233 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 95698df4-827a-3204-964b-55bad6091750 | -6.42025 | -54.9356 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6c2ff1f4-17a3-3bb9-8dd2-8d59aa509d87 | -6.70748 | -59.09499 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81d7fd8b-2c3b-3df2-b80b-9e776f60d4de | -3.09963 | -61.21102 | 2026-08-20 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c69c533-e269-3b75-b41f-2743c4edcacb | -6.43969 | -52.72676 | 2026-08-20 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e87792c7-8779-3223-ab1f-152862010380 | -6.58183 | -58.983 | 2026-08-20 05:04:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a66d498-4660-3dda-ba53-b5133eaf6345 | -6.3477 | -54.8994 | 2026-08-20 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 72657822-97ff-3d25-8b9b-7a5fd9546807 | -6.12417 | -57.71557 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ca8f8121-9cae-3ae4-beb2-a0af345ea6eb | -6.09154 | -57.92088 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64df89e1-cae2-3bba-80d7-b21743d85f5e | -6.09214 | -57.91711 | 2026-08-20 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d73e3cb3-a35b-3b22-bfb9-0b701afb5430 | -6.6515 | -56.4006 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5442a5ef-cb27-3bf6-8dce-64b77f010f65 | -6.2903 | -43.63208 | 2026-08-20 05:04:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d08a6b83-652a-32ba-a41b-e707f19e3030 | -6.24945 | -55.40237 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8aad5b92-23f6-3686-b446-27369a3a6593 | -5.79587 | -55.7163 | 2026-08-20 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README46.md)
