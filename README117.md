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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8247b6d-31b0-38df-814c-38d19b8cf00d | -15.23698 | -50.1274 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3f0ab514-78c3-35c1-b506-71b0d57b5ee0 | -15.93463 | -43.30261 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1a8d096-12d9-36c4-af9e-f1d3ce628710 | -18.16452 | -53.34694 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dcbe8415-2dbb-31b4-b3a0-8dbb3275b5d7 | -15.70146 | -48.30693 | 2025-10-03 04:34:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 144eb03a-acbf-3a57-8fa4-fb1f654534f5 | -15.32306 | -46.89762 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b1fc23aa-b9ae-3b69-9be7-ce02de70eb07 | -13.68127 | -48.03797 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0264c1e8-f881-34b5-8e08-fe5fc7ba09a8 | -13.23893 | -47.3484 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b994126-157d-374d-8875-e33babf5be51 | -12.86078 | -46.99891 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 121375c4-2b90-39b9-ba0e-1c6b3ccf0f95 | -14.30966 | -45.87651 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 83e98c01-c19a-3912-b8c5-186733081d38 | -12.93742 | -46.37632 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 236a2757-158a-3883-8840-d40774bfb487 | -12.62637 | -46.99901 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 535a622d-8a60-3349-b308-9422d00fa10c | -18.51154 | -44.04113 | 2025-10-03 04:34:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 211896a5-1233-3a89-bd69-2dc61789fa52 | -13.13752 | -47.8867 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 379aec37-5087-3100-8c20-3c99c552747f | -13.68097 | -48.63846 | 2025-10-03 04:34:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dd7ac93d-8c6a-385f-b0e0-7395902285d0 | -13.56149 | -47.29522 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a08491fe-2efd-3422-9797-4b5827a0ef29 | -19.3865 | -47.27658 | 2025-10-03 04:34:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3919bc4-89a3-3960-9575-59e7e31e325a | -14.86055 | -48.35805 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a6d20d3-2ea1-3b05-bf11-8fd672125e1c | -13.97632 | -48.17014 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 46da9c35-d46c-3427-93b3-8e61469c5b59 | -15.75705 | -47.7711 | 2025-10-03 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bc26ad88-6323-3da5-83e2-2c0ba6580b4a | -17.96531 | -45.01127 | 2025-10-03 04:34:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a4086adb-fd17-3952-b23c-006ea09d379a | -14.92222 | -48.3264 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 755ab598-ad21-3f15-8481-826bbd5d3e37 | -14.29586 | -46.02874 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 393296a1-46c0-3c7c-8191-63d075b92c8f | -12.38954 | -46.52121 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7f0a924f-b6cd-39b1-b910-25363553f974 | -14.72839 | -48.09536 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9fbaf115-e165-39e3-a4ff-13471762a8b8 | -15.22117 | -47.96309 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55f1b5a3-2463-33c6-9ae2-11ddc3c2056d | -14.44835 | -46.34278 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 86955cf3-339c-3c63-8f2b-3b8550f66759 | -14.63615 | -48.13313 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 80a8467d-45ac-37ba-ad2d-ed7184320731 | -15.83514 | -42.62753 | 2025-10-03 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c7663a19-98ae-3972-bec3-9e1943bfcf23 | -12.85789 | -46.9945 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61fcd45d-2aa3-3733-8d86-0d49dcde3378 | -14.74652 | -48.12105 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f8ecf88b-1783-35b1-850a-5c675f40538d | -12.61287 | -46.97902 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 5f363bd5-fa15-3635-bb2d-067df236a1b7 | -13.77259 | -47.54612 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39efef64-169c-3c53-b7fc-61209417c7c0 | -16.15884 | -45.1159 | 2025-10-03 04:34:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ce78b85-4b18-3a76-8eff-f42b2daac144 | -15.24196 | -49.29782 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9cfe41e4-db36-385d-b083-83a63c225a35 | -14.87546 | -50.24287 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e9cd6d9-1588-33e0-a139-eb9a3d75cd2d | -13.77194 | -47.52708 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 50e2bcda-8803-36cb-8da4-3daeb4cdf93b | -18.22794 | -53.35993 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1cd8bb1-004b-3487-8b5e-ad66abfbdcf8 | -13.68362 | -48.09068 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0c82f9e3-17fb-304e-ac81-0a03f8eb4d20 | -14.65364 | -48.29166 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b398fcb8-1ace-3afc-8ce1-730f8a42d8d2 | -13.25934 | -47.25832 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7d325db8-b344-3a90-a5ac-53a37339d851 | -15.23718 | -50.0834 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c68ad7ab-ba48-3430-8bda-e5359b548190 | -11.08169 | -54.78436 | 2025-10-03 04:34:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa8ea676-9bad-33e6-b019-f66cd2762af1 | -12.89704 | -47.18103 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2d1c124-879f-31e1-9a72-ce76fd3e93cf | -15.52312 | -46.80966 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 189fe1b1-31fb-38ac-add3-2b0710e0d7fb | -12.36846 | -46.5181 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ff0fa0f1-b086-3ee7-999a-85c26e6acfc7 | -14.72558 | -48.09106 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4171d2c3-d05b-3a7c-bc5e-ef27d920d122 | -13.77879 | -47.52806 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2b38c54b-2b74-3831-9e26-64b5c658edf0 | -14.90518 | -46.96679 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 360e0473-4d81-3a90-b595-38cb8bd9e0ac | -13.9381 | -48.09363 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 55b78a06-cd82-32da-9721-9df76c911df2 | -13.76813 | -47.57591 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 061362e3-64ed-3efd-887b-abfe0d777e7e | -13.78862 | -47.57906 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c57368fc-2822-30ea-b6ec-f634523d4ca7 | -12.78117 | -44.91966 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 453fd110-f239-36c2-a669-c358fff949c1 | -12.80322 | -46.87206 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 36e1e020-b3d3-322a-9c54-2ddf52f1ed91 | -15.17417 | -43.62515 | 2025-10-03 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 88476d7b-1350-3634-9e6c-363c254d41ce | -12.60861 | -49.90536 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8ea2313d-4b0d-3abb-ae33-fae95d4a5765 | -16.68486 | -53.02014 | 2025-10-03 04:34:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9e0394ab-076e-3330-86d6-f8bcb4a72f47 | -12.93857 | -48.43935 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bfa2b4cb-5470-36f5-9b3b-b3ac4bd2d5a6 | -18.65218 | -43.87299 | 2025-10-03 04:34:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed4b5eb1-5f91-3667-8902-eeffe7849aa5 | -13.77936 | -47.52419 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d0f0739-1c8a-3bdf-86d4-af54f6975634 | -16.40013 | -52.15761 | 2025-10-03 04:34:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c75466d-f65c-3b3e-866c-885565ad6929 | -14.1937 | -46.11951 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 55c7e3f4-0dd5-30c5-a2c3-6ab219c1cb66 | -12.93503 | -46.39288 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2c8f051-f451-3a9f-adfc-eb9a69900254 | -14.22974 | -46.1021 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eeebc26c-f062-3a4a-b5ef-98acf82adc46 | -15.28799 | -46.39423 | 2025-10-03 04:34:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30e617df-4915-363c-bb46-27e99eecccc1 | -13.81202 | -51.21485 | 2025-10-03 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| ee610c15-f7cf-385d-9258-7b38c89d1fe3 | -13.28664 | -47.1931 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 97cdce97-15b7-3325-8713-e5cd209bcc1e | -12.80501 | -46.86002 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 661de024-3238-3de0-906a-f31f36551a6d | -13.38242 | -48.13335 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67d07ed8-c431-3bd1-b6eb-38f335f5ba18 | -12.94628 | -46.39037 | 2025-10-03 04:34:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4fab8a0b-0be4-3d5e-9854-a71d3cf0aa25 | -14.95509 | -49.9996 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b0d71df-614e-37ac-abbe-9ee33d359f08 | -15.30734 | -46.28573 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f247cf5d-ebde-3c0c-a48f-30de6b1708b1 | -14.74539 | -48.10554 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 40f16363-3bba-346a-b18a-6bdbbf69e808 | -18.2492 | -53.31949 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ce65dffd-4a8a-3c90-8e43-133e2bfc482b | -13.31248 | -47.81296 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 704f3c72-f292-3a8d-bc51-633dd5b8907b | -18.1631 | -53.33409 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 770e9887-85a7-31b9-8a9c-b693678c7a71 | -12.36789 | -46.52205 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 279a82f4-4a15-314a-809b-d330639b96ad | -12.93249 | -48.43462 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31965050-3925-350e-9b12-7154eebe2d95 | -14.37961 | -45.94182 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d36d1faf-4148-3c4b-9b38-da5c9459f9a1 | -18.2032 | -53.35531 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 30a8a14c-747b-3d7d-8c92-5e6db392bb77 | -16.07106 | -51.0057 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d06c18b2-054f-3ab0-8890-0a14fe3b0345 | -15.61074 | -47.85931 | 2025-10-03 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5285c517-49f2-3d01-8de1-fa0f61183f92 | -13.31054 | -47.59581 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 23d551de-9726-3960-b97a-11f48dee32b7 | -14.42777 | -46.35724 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb4c0f47-c570-3537-8777-9419b6a0c86e | -14.35905 | -43.84303 | 2025-10-03 04:34:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4696c82-9aa3-3345-99a2-d364dad5279a | -18.19782 | -53.30177 | 2025-10-03 04:34:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fc8a2dda-f1cf-3c7a-ab7f-91d01cd8ff00 | -14.94329 | -46.8777 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 37c56fd4-ab4f-3cf0-81df-d32c324733f8 | -15.23026 | -47.97227 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5449b28-3337-355d-847b-be6809cf41d6 | -14.59383 | -48.34555 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ba5d7bc-c75f-3579-8ec6-045d30ac4520 | -14.77354 | -50.0934 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6e0ab09e-d37e-3564-9d0f-ddd037d331e6 | -18.24214 | -53.31923 | 2025-10-03 04:34:00 | NOAA-20 | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| d0845ff1-2ff2-34b9-bba1-c2ef5a02dc97 | -15.22911 | -47.95662 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 57911096-a80c-35ec-b600-15c5d345a114 | -13.05569 | -47.05066 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9d9490f-f0e2-3ed8-9692-80594e23f959 | -14.71581 | -48.21053 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4489e475-d095-304f-be8e-59df68c86ee3 | -19.89832 | -44.50737 | 2025-10-03 04:34:00 | NOAA-20 | FLORESTAL | MINAS GERAIS | Brasil | 3126000 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| f3cd53f4-9546-35b8-ab9f-513e5ae2add3 | -12.43582 | -46.47544 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5beeeeec-d1ea-3abf-8d81-3d24636848e0 | -12.89113 | -43.13391 | 2025-10-03 04:34:00 | NOAA-20 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 02696aa9-2795-3d00-9239-ac38006b6dc7 | -13.73906 | -47.99826 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 16bd7539-fab6-39b3-984a-172b6ab6062b | -14.44105 | -46.3749 | 2025-10-03 04:34:00 | NOAA-20 | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 40bbf16b-fb01-3291-a0e5-79f1ae28ae46 | -12.61632 | -46.97961 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| bd9ac7c0-33d4-3a51-881b-4957995f1205 | -13.67956 | -48.02645 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README118.md)
