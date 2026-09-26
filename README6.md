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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 604a7e63-86df-3ef5-824b-83d42cde765e | -5.52775 | -39.86097 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5ef3e874-089f-3e1a-ad3d-70ddea57f66b | -5.52294 | -39.85984 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d659e821-7e0d-32b9-aa30-b36abcad8b27 | -5.73804 | -45.07774 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 46443376-89b0-3b97-82a2-8f588cddbf19 | -5.77876 | -45.08437 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| c21d3936-1511-3833-a26c-adccd473b164 | -7.35205 | -42.08926 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 945f1065-d441-3d86-99c8-bb8ac5f1fc54 | -7.2732 | -43.29482 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c7bdda9b-91da-3d85-8e44-ab19aff3e1ad | -7.71162 | -34.90764 | 2026-09-26 03:30:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95ef60a6-52a3-3bc1-9374-2fe9a728e0e2 | -5.77196 | -45.08332 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f8644388-7bc7-3e05-9978-41a2248e49da | -7.27991 | -43.29157 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2982c4a7-e841-3207-8fd4-dc615db37e7b | -5.52349 | -39.8686 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a10eb889-a83f-3786-8318-0c2241bf7ddc | -4.3752 | -42.9933 | 2026-09-26 03:30:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9e14f11-5be6-332f-a8d2-2d06a5fe1d39 | -8.51813 | -40.23222 | 2026-09-26 03:30:00 | NOAA-21 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 44746430-038c-3be6-989b-4d598bb2c9a9 | -7.4037 | -39.78434 | 2026-09-26 03:30:00 | NOAA-21 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 27.1 |
| 0d67f2ca-195e-3e11-b764-7aaa7c5e2747 | -3.94036 | -42.98922 | 2026-09-26 03:30:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 250c581b-7c29-3809-badb-45bd2d8af3be | -3.2404 | -43.22488 | 2026-09-26 03:30:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f7582313-54ba-3106-a8e1-d41ae9e475d0 | -5.77273 | -45.09086 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 9bc61df9-ea62-3c2b-bc49-655b20aa06e2 | -6.36574 | -40.17003 | 2026-09-26 03:30:00 | NOAA-21 | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4fb72ccc-c20e-3965-8267-3dc2fb4d7de1 | -5.74813 | -45.06065 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| b79cb17e-bbac-34f6-b4fd-b74bacb0f4b0 | -6.02635 | -35.4394 | 2026-09-26 03:30:00 | NOAA-21 | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25772037-690a-384f-81bc-4a8f4c4a3263 | -7.36852 | -42.09209 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d739a316-ceea-3f09-ad85-94d32ef6b2a1 | -7.35883 | -42.08298 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 965a2c92-5c13-307a-aa08-ad03565a226f | -5.76968 | -45.09604 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 40de7c91-510f-3abf-bcc9-9685ddf17875 | -5.74139 | -45.0593 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 22adb076-ae32-38e5-9392-ec88bdabfc06 | -5.74698 | -45.06697 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| d034ad17-6006-3649-b861-9330066c24f6 | -5.77535 | -45.10339 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9f5171c-872d-3aaa-8e9b-1219fec96f71 | -5.77084 | -45.08955 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ac73ef70-7775-38b1-a732-e83c399c315f | -6.37205 | -39.84907 | 2026-09-26 03:30:00 | NOAA-21 | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34d1bea4-549a-333c-8e06-3b17ef48d320 | -5.7391 | -45.0719 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 156819f2-0d21-3ab6-96f1-c2cdc1dafe49 | -7.35754 | -42.09023 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 26e58fea-f097-3303-9698-aea9658e6ac1 | -3.93597 | -40.59327 | 2026-09-26 03:30:00 | NOAA-21 | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 46cf6162-0390-3640-b116-e7d3f484e80e | -8.8505 | -36.53054 | 2026-09-26 03:30:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0298bccd-a5dc-3fb0-b3f4-e87287c02737 | -7.35947 | -42.07938 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cea62ecf-5ee1-35ea-9570-cb38586c158d | -3.237 | -43.2263 | 2026-09-26 03:30:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 045b1428-7e5d-3d5e-9ef2-4dbe70c0ebc7 | -7.36302 | -42.09119 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 628329a3-3621-31b3-b753-7bb3118ee6e0 | -5.781 | -45.11085 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 24b1e891-6c84-3de4-b0b6-078a69ab9434 | -5.74473 | -45.07936 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 613d62ec-ffc6-342b-bfb8-4f1542bf5ee3 | -5.52515 | -39.85859 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1a40dbdd-6e2d-3bd8-a7b8-c4bd0f25700c | -5.7739 | -45.08459 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| d5d58ae3-6737-3e00-81d6-00411322129c | -3.94649 | -42.99028 | 2026-09-26 03:30:00 | NOAA-21 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 1f3e75c4-63ef-308c-92ba-fef3f57ac787 | -7.2705 | -43.29494 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c954bff6-98f4-35e7-895f-7e1836cc1967 | -5.78217 | -45.10432 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b1e59947-65f4-3853-a26f-f1bfa06d0498 | -7.7151 | -34.90822 | 2026-09-26 03:30:00 | NOAA-21 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 399c7a52-9d67-3a16-be90-c4ccd8862ab8 | -7.25898 | -43.3057 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6179ad37-5900-3987-a4c5-ec16778c423d | -7.25977 | -43.30135 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6aacd440-07f9-35c6-a2e9-e023d2211af3 | -5.74024 | -45.06564 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 5b3b81db-b186-3896-a059-77ece1f0783a | -7.26726 | -43.29378 | 2026-09-26 03:30:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b45dbc7-f1e3-3e7e-8ea3-d7463300213c | -5.73351 | -45.06424 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 508f664f-860c-3ce9-a650-b0240c7cbed0 | -8.12083 | -40.7501 | 2026-09-26 03:30:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9ee04b60-1827-30e6-9e90-cdc6e96ae558 | -5.77764 | -45.09061 | 2026-09-26 03:30:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a7185cb5-3a95-342f-a158-9071a8bfaf98 | -7.35334 | -42.08204 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c9cf9839-dcc5-37b3-9d73-48fd8acaebdd | -8.11584 | -40.74946 | 2026-09-26 03:30:00 | NOAA-21 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b6f067d-cb62-3a29-97c6-d222a00b0f0a | -7.3527 | -42.08562 | 2026-09-26 03:30:00 | NOAA-21 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 0e36b86e-fb0a-3086-9367-8f62d0644b84 | -5.52117 | -39.87005 | 2026-09-26 03:30:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3948597f-e2d4-3ce4-b0a9-483a0cfced17 | -6.02272 | -35.43882 | 2026-09-26 03:30:00 | NOAA-21 | VERA CRUZ | RIO GRANDE DO NORTE | Brasil | 2414803 | 24 | 33 | nan | nan | nan | Caatinga | 9.9 |
| 1b742781-870d-3ef6-b975-18e439a0333d | -12.64875 | -43.16305 | 2026-09-26 03:32:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e92be7f5-5cec-391a-9987-f88961fb30fc | -15.23932 | -43.27703 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.6 |
| d1c7adbd-94ea-3969-90af-1f1b10037e7c | -9.46736 | -40.33324 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.9 |
| c356d5c1-49b2-3f01-9b6f-debf24b8dc34 | -12.65411 | -43.16409 | 2026-09-26 03:32:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b05920d-af3a-32e5-9c5a-3b8ee0b2798c | -9.85657 | -36.019 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fab783c6-cb08-3c6e-ae56-490d43e98441 | -15.89492 | -43.47817 | 2026-09-26 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| f077f232-dc50-327f-8def-a284519ef5c4 | -9.46266 | -40.33243 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 70f8b959-bb83-344f-822b-00fc58260dc1 | -12.70504 | -47.29658 | 2026-09-26 03:32:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f4ed4f6a-1a1c-3184-b381-1d8f8dc64d57 | -9.8666 | -36.0249 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 4d41b1f3-61d0-3b35-b148-b8ba11718fc1 | -9.86128 | -36.02087 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| b9641954-fdd8-3d23-9751-169f46b9add2 | -9.85726 | -36.01487 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 37479182-1fc2-33b6-9fc2-ca10cc824dcd | -15.24121 | -43.26752 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 3b23e073-3e3c-3365-9ee8-c7707be6e1f0 | -11.10844 | -42.05747 | 2026-09-26 03:32:00 | NOAA-21 | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 8f66de18-45f6-323b-959d-5bd8b8446527 | -15.23544 | -43.26962 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0ce1dabe-ece3-31f3-993a-68df259a5720 | -15.24183 | -43.2644 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| b78ef53c-ceb2-3f6f-817c-c73e9f8b41a9 | -14.82267 | -43.32032 | 2026-09-26 03:32:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e8f77b04-4c9e-3322-bfc2-e39b80018548 | -11.94406 | -38.28926 | 2026-09-26 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 92542f1e-f0fb-3743-8448-175b8d73c98a | -9.46827 | -40.32818 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 40034c52-f8d7-3553-b50c-d9e57906492c | -9.46357 | -40.32737 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 57.9 |
| 5164e074-5de5-3828-8532-66efd942b166 | -9.8548 | -36.01554 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 91e99491-438d-32b8-ab5a-9d05cddf4f41 | -15.23995 | -43.27383 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 8d4a265a-ba35-3fc1-bc64-fb1e052526a7 | -14.82331 | -43.31705 | 2026-09-26 03:32:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b161f896-8069-3a8e-a73d-a75d068018fd | -9.86014 | -36.01959 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| cf7f83af-3fdd-3f83-8923-23ee4811822c | -13.47976 | -42.48161 | 2026-09-26 03:32:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ff2350c6-d598-3e11-9883-6834f9b2e27d | -9.46174 | -40.33747 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 150a5512-2ebd-3e44-97a6-cba3c2263c88 | -11.94012 | -38.28854 | 2026-09-26 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 7.3 |
| adddfb27-79e0-383c-b1e9-6fd112caac10 | -15.24636 | -43.26854 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 26.0 |
| b3dd0292-c75e-3601-8ad0-7ef22215fbcf | -11.85744 | -44.58438 | 2026-09-26 03:32:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f17c3ae-ac7a-38e4-8de6-0bf1051f1125 | -15.24446 | -43.27811 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 1c88779f-d0e7-328d-b507-95261dd6f883 | -15.24698 | -43.26541 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9bf5c1f0-6624-3173-86f1-c71033260aaa | -15.88977 | -43.47711 | 2026-09-26 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 3a9e1ede-4776-3aff-ae07-dacef3ccc357 | -11.13711 | -42.8276 | 2026-09-26 03:32:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5873b6c6-6303-368f-9c4d-d1e6d6bb2c88 | -9.8577 | -36.02027 | 2026-09-26 03:32:00 | NOAA-21 | ROTEIRO | ALAGOAS | Brasil | 2707800 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 301adc8a-65d5-38df-b7b2-6f2131064d26 | -13.47416 | -42.48352 | 2026-09-26 03:32:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 857fb9aa-af19-3e72-a06c-ba6433382423 | -14.82396 | -43.31377 | 2026-09-26 03:32:00 | NOAA-21 | GAMELEIRAS | MINAS GERAIS | Brasil | 3127339 | 31 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 87707b21-b77f-315d-b9dc-b48f354cd869 | -14.88099 | -47.14057 | 2026-09-26 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 4dda3e0f-a8f8-3345-8b48-cc56c8175580 | -12.58278 | -44.13747 | 2026-09-26 03:32:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0e8a0bfb-a530-33da-b94b-baac166cd62a | -12.65479 | -43.16058 | 2026-09-26 03:32:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4b63902a-d26d-3bab-a62d-bcf2c475ffbe | -13.47919 | -42.48465 | 2026-09-26 03:32:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9c60dfcd-ea6f-3305-8f90-00e5b3dbb388 | -9.47206 | -40.33406 | 2026-09-26 03:32:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 114.5 |
| 9f7f7d50-9ecc-32f7-b6e0-86ca49c8bca1 | -15.24059 | -43.27065 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 26.0 |
| a2959704-80ca-3a60-8afd-becd492dab8e | -15.89428 | -43.48142 | 2026-09-26 03:32:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4fc591a1-db78-3d9f-80f1-f133796cdf43 | -15.23481 | -43.27278 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 3e3e3991-195e-3382-af3e-bd56c0645bab | -14.8822 | -47.13499 | 2026-09-26 03:32:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 685e5785-7e42-32d1-9ce6-d4057183089f | -15.23668 | -43.26339 | 2026-09-26 03:32:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f5e69a5-3110-3c2f-9bac-f8d33607bdb3 | -11.9344 | -38.29815 | 2026-09-26 03:32:00 | NOAA-21 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Mata Atlântica | 20.0 |


[Clique aqui para ver as próximas entradas](README7.md)
