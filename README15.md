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
| 81045c49-aeb1-3571-b1cd-f584c2b077b9 | -5.7376 | -45.1533 | 2026-10-03 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 69.1 |
| c95b6e1f-0a78-3c77-8b9d-51212a747e1a | -3.1299 | -53.7633 | 2026-10-03 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 39.8 |
| c98a23b0-9b96-378c-a9b8-8c92c474bb76 | -15.2314 | -43.2784 | 2026-10-03 03:30:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 75.3 |
| a0883607-1a6c-32d9-9d43-0a2ec2225b15 | -3.1116 | -53.7436 | 2026-10-03 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 322008b4-6072-3372-bc8b-f4ca7f1359a1 | -3.1299 | -53.7431 | 2026-10-03 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| cd2ebd93-e563-3c22-becd-d571f5ba034b | -5.9571 | -43.6467 | 2026-10-03 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 38efb941-50c9-33be-8fad-79c0a249c601 | -3.13 | -53.7229 | 2026-10-03 03:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| fc7d9cbf-ec99-37f0-bb4d-5570fe52861a | -5.9384 | -43.6482 | 2026-10-03 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 1686e2cd-ded2-3804-aacf-b54f311bba66 | -5.9569 | -43.67 | 2026-10-03 03:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 71.5 |
| f1d87ba8-4237-3cbf-a973-54176572f9fe | -5.9381 | -43.6714 | 2026-10-03 03:30:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 56.3 |
| d6076e08-ebd3-340c-b3eb-1b40c62b6321 | -3.1299 | -53.7431 | 2026-10-03 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 101.1 |
| bba5edf6-36de-3f68-8eb6-8f6dc5089e3f | -5.9381 | -43.6714 | 2026-10-03 03:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| e3354782-874e-3d03-99f6-03d07fd04159 | -15.2314 | -43.2784 | 2026-10-03 03:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 93.0 |
| 94e8fcd2-b2fe-3e79-aaa6-1085b91237e6 | -3.2951 | -53.8395 | 2026-10-03 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.8 |
| e76fc4bc-3a91-3c4a-9977-2e003ba0c5db | -3.1116 | -53.7436 | 2026-10-03 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| b3bd8218-28a6-3262-977d-4adc39f3b2cb | -5.9569 | -43.67 | 2026-10-03 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 101.9 |
| dd266100-85a9-35cd-a57a-6c9a401a957b | -15.2511 | -43.2743 | 2026-10-03 03:40:00 | GOES-19 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 69.4 |
| a9b037f9-a64a-37a1-a64b-ee0810077d56 | -5.7376 | -45.1533 | 2026-10-03 03:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 44f62d9a-e18a-32e5-b6a4-4592f23bd413 | -3.13 | -53.7229 | 2026-10-03 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 9e677d56-490c-3868-8691-dd0d4465cdb1 | -12.8676 | -44.6878 | 2026-10-03 03:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 0c4748c9-ef5f-3e29-aa4f-99555a7e621a | -9.7221 | -36.1077 | 2026-10-03 03:40:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 113.3 |
| d9ec0e62-ae31-370d-a850-08de5ba23343 | -5.9571 | -43.6467 | 2026-10-03 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 6b0482eb-7209-3372-b8a6-24b4680b8a57 | -5.9384 | -43.6482 | 2026-10-03 03:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c57e4091-4611-3f24-afbf-43274e48a29c | -3.1299 | -53.7633 | 2026-10-03 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 38caedba-6368-303e-a264-1cae05c7bc29 | -3.2767 | -53.84 | 2026-10-03 03:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| ddc49be4-b342-3f91-925b-e7650186ef4a | -5.9571 | -43.6467 | 2026-10-03 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| a17dfab9-d15c-3252-91e1-f8b9417ebcf1 | -3.2767 | -53.84 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 2d55a448-a117-37c5-b2ae-fed880a4786e | -3.1116 | -53.7436 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 476ca6c1-b146-342c-956c-11324ec1f764 | -3.2951 | -53.8395 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2fcaef80-3f99-315c-84c4-b3a09fac32cf | -3.1483 | -53.7426 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 88fef1ba-83ac-3780-a69c-8eeb6447b590 | -5.9384 | -43.6482 | 2026-10-03 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.8 |
| fdfcb0f9-0d72-3c79-bd83-8c882c5f4c2c | -12.8676 | -44.6878 | 2026-10-03 03:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 68.7 |
| db9af20b-a938-3240-996c-c877e2a0ad24 | -5.9381 | -43.6714 | 2026-10-03 03:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 53.2 |
| c4d1baf2-28f2-3f04-94f5-d24f3c97b7e7 | -3.1299 | -53.7633 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4d8e29f0-555a-3699-95dc-cc4907b44a77 | -3.13 | -53.7229 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| bb35bcc4-5cec-3a46-80bb-12dca11187c6 | -9.4574 | -40.3641 | 2026-10-03 03:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 65.8 |
| f654d5e2-72b1-394c-8047-2ece28893d15 | -3.1299 | -53.7431 | 2026-10-03 03:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 5900012a-5ab8-39ce-aaa4-e0d948e5f0c0 | -9.7221 | -36.1077 | 2026-10-03 03:50:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 147.9 |
| 0810a20d-d49f-34a6-9311-528faecb4e29 | -5.9569 | -43.67 | 2026-10-03 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 3d0e38b5-afc2-33a5-97ac-00a9b817645d | -5.7376 | -45.1533 | 2026-10-03 03:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| e8f8531d-d2ef-32fa-9a76-d6170484a986 | 1.8037 | -55.5854 | 2026-10-03 03:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| c547314c-908e-3d71-a4b0-94d4a471d021 | -5.18632 | -39.74138 | 2026-10-03 03:53:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 96798331-7d77-3be1-a01f-b8f606fdf64c | -4.44799 | -47.92682 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 95feb31c-7b09-3746-9d70-c1e65e158528 | -4.3597 | -47.7802 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b5d38bac-7493-3683-92be-3c50cd30f417 | -5.75576 | -35.20727 | 2026-10-03 03:53:00 | NOAA-20 | NATAL | RIO GRANDE DO NORTE | Brasil | 2408102 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0f9898bf-e9ac-32eb-a4c6-ed6e5e08838d | -4.44701 | -47.92589 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 74cc2155-2616-3e78-9b6a-e3b73bf06090 | -3.35392 | -43.38044 | 2026-10-03 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f565b36-0b51-339f-ba3e-44740c978ef2 | -4.36404 | -43.83595 | 2026-10-03 03:53:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12c4f776-4495-3351-a897-092e59dbec67 | -4.35992 | -47.77886 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 8565f800-3226-3543-8e35-edd4bfa66bac | -2.88873 | -45.41264 | 2026-10-03 03:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 351435b2-2f65-3802-a388-a08d9a248b3f | -3.69218 | -39.57771 | 2026-10-03 03:53:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| a4498906-11cf-3a01-a229-63b42c00fb2e | -3.35312 | -43.38531 | 2026-10-03 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fe9783c2-9f95-3aa0-8aae-16422898d214 | -4.56699 | -46.58319 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e438891e-c91c-3333-9adf-fa7c97598a2b | -4.73155 | -43.27205 | 2026-10-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa573ba1-f554-3bb8-ae5c-41eaf21cfbef | -1.68549 | -48.2086 | 2026-10-03 03:53:00 | NOAA-20 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a092ec9c-99e0-3846-bdd4-9dbce157efd0 | -4.56633 | -46.58696 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| cf50a9cf-d32d-3bc0-b7a9-6a575954efa0 | -1.32831 | -47.59139 | 2026-10-03 03:53:00 | NOAA-20 | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9eb6ea1e-df9c-32b1-bf6c-8f90daabd558 | -4.44717 | -47.93163 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f5cc8f22-f9ae-3c49-8957-d1bb2595f854 | -2.17413 | -49.77681 | 2026-10-03 03:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe683923-48b1-3bc5-8602-da9dbdb3a7eb | -4.36049 | -47.7756 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7d1dcb18-4bcb-33ab-8312-662e98ee1645 | -4.73684 | -43.26825 | 2026-10-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8e10c3be-b1a4-3ee3-af62-d1b695b2e7e9 | -3.35232 | -43.39019 | 2026-10-03 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1f5e745d-1ede-365d-9ba6-49d045c4176a | -2.8893 | -45.40924 | 2026-10-03 03:53:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa10f517-1bbe-31e9-bceb-04984ab23fc1 | -5.18457 | -39.7397 | 2026-10-03 03:53:00 | NOAA-20 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 50cc1e3b-983c-38ba-8d7f-634ed3aa2e8e | -5.82744 | -38.95244 | 2026-10-03 03:53:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d49adbcc-4600-3f50-b913-5ea516fa0c33 | -4.35911 | -47.78339 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 984ef36c-bb4c-30b0-9845-63aadd50d607 | -5.89516 | -35.7276 | 2026-10-03 03:53:00 | NOAA-20 | SÃO PAULO DO POTENGI | RIO GRANDE DO NORTE | Brasil | 2412609 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 197555ac-e495-32a4-9244-783098c9d829 | -4.35381 | -47.77771 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d9ea1d41-a7d2-309e-9dbe-cd5c10be0fc8 | -5.824 | -38.95184 | 2026-10-03 03:53:00 | NOAA-20 | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 99339d9b-3909-3076-a78c-4de99ea20400 | -4.98673 | -45.64495 | 2026-10-03 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63164634-f86b-3504-a7d0-0e348b926bd2 | -4.89043 | -45.45425 | 2026-10-03 03:53:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ca8052b1-3f15-3dc3-9f18-e4846baa2e6b | -4.35439 | -47.77441 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 41dc0f69-f1a4-3d6f-bfb7-77f8662d21a0 | -4.46052 | -38.919 | 2026-10-03 03:53:00 | NOAA-20 | CAPISTRANO | CEARÁ | Brasil | 2302909 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c870d9fc-1fd3-36b9-a9cd-c309fc074d4b | -4.73232 | -43.26754 | 2026-10-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6cd9dec1-c0b9-3c76-83ca-2b713e6c9e29 | -3.34847 | -43.38454 | 2026-10-03 03:53:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f37475b0-2064-30b8-9141-d34dd8601292 | -4.56939 | -46.5871 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f54ea147-36e2-34a1-802b-59cf081e6524 | -4.73607 | -43.27275 | 2026-10-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f91c775b-a3a9-348c-8c06-2cfc4f958967 | -5.27148 | -43.36214 | 2026-10-03 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c64b5d1-0edd-3464-9d4d-6b136f4900e2 | -4.56298 | -46.59057 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd26da92-263d-39d8-bce0-f72913b90744 | -2.16821 | -49.76845 | 2026-10-03 03:53:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f509ecc0-18fd-3f1c-8b6b-c9641fc58afd | -4.45415 | -47.92797 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 08327612-8063-3d29-94b0-d66a0d09d2d7 | -4.66308 | -40.56226 | 2026-10-03 03:53:00 | NOAA-20 | NOVA RUSSAS | CEARÁ | Brasil | 2309300 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4eecc903-3bcf-32dd-908e-63395b4de523 | -4.90578 | -45.71015 | 2026-10-03 03:53:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa38bbe7-9864-3cb2-b00f-c95101f62afa | -4.98423 | -44.8872 | 2026-10-03 03:53:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 533777cd-2c8b-3839-9d6d-e5d2af58c60e | -3.69252 | -39.57976 | 2026-10-03 03:53:00 | NOAA-20 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6da80e8f-d16a-3cff-baff-b82f3b37091b | -3.74962 | -45.94712 | 2026-10-03 03:53:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 63e53ec4-de31-3f66-aba2-5f6c165f3539 | -4.56872 | -46.59104 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 510992a6-5f35-3e89-b7bf-c143cbb4c002 | -4.45317 | -47.92704 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 21c4df64-e103-3250-af83-54698b8e6ce8 | -4.8899 | -45.45732 | 2026-10-03 03:53:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4cd9d66-1941-371e-a08a-a11375d92ba1 | -4.19016 | -40.32311 | 2026-10-03 03:53:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 66c2e5cf-fa8a-39ea-8755-bfddb6ffa846 | -4.73309 | -43.26303 | 2026-10-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0da29150-be23-385e-904a-a1f52a42ff03 | -4.56563 | -46.59085 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| b8c52fa1-37d5-3aed-bb37-73b2b0e4ef76 | -4.74059 | -43.27346 | 2026-10-03 03:53:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bdff0c22-4fb4-3308-88c0-d48fee9545c6 | -4.56363 | -46.58672 | 2026-10-03 03:53:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3270ee1-43be-39a8-bf3a-61f9cb72f17d | -4.45333 | -47.93277 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 65d46c9d-eeae-33ad-ac45-75ada78d0d8c | -5.27072 | -43.3666 | 2026-10-03 03:53:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 781f27c2-c5b6-3880-8211-2bb3ae009f9d | -4.35359 | -47.77905 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2d2b55b9-4dcf-3c47-9f95-0c05a6d9867b | -2.49063 | -48.53035 | 2026-10-03 03:53:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f9c94203-b030-3dc8-a7d2-d6d6bcdbe3ba | -4.44615 | -47.93069 | 2026-10-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d87e45a-0947-368b-b885-3247a1177197 | -3.01169 | -41.14162 | 2026-10-03 03:53:00 | NOAA-20 | BARROQUINHA | CEARÁ | Brasil | 2302057 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |


[Clique aqui para ver as próximas entradas](README16.md)
