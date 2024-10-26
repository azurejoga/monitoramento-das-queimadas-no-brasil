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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 332c6973-a0d4-324a-a534-474f8e3f0fc5 | -18.14161 | -57.37172 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| af7167fa-6425-3850-87b1-07f9ce5269a8 | -18.14082 | -57.37622 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| bb7b5049-883e-334b-bdf1-ab0058bcfe73 | -18.13795 | -57.37101 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 0a825e4b-f154-39ca-bd96-d3cbda071de5 | -18.13716 | -57.37551 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 836a3054-c618-3e2e-bcd3-a7d4c3e976ff | -18.13017 | -57.35096 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f255e352-4c10-3c91-9230-5870055256f7 | -18.12113 | -57.31683 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 7dbc2abd-0d9a-3d53-8d49-0ce884087917 | -18.12033 | -57.3213 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 83071a2a-d79a-3db7-9acb-befe1417e4a5 | -16.093 | -60.12562 | 2024-10-26 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f607cedc-9e15-3b74-b74d-bc5a265361ef | -16.09212 | -60.13023 | 2024-10-26 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f81070f6-b0db-3f09-a9f1-464ea56747e3 | -16.08943 | -60.12013 | 2024-10-26 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f391dadf-d71a-3d6c-b0a5-1cbb53f205da | -16.08855 | -60.12472 | 2024-10-26 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c25210e-bf70-3b04-a4d3-35673ff85711 | -15.66724 | -59.7635 | 2024-10-26 04:46:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 51dc1115-0bf3-3515-8ab1-d6dbc797592e | -16.0246 | -41.19249 | 2024-10-26 04:46:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| e68bc545-da62-3c8c-9155-61755f9a9c5e | -16.01882 | -41.18634 | 2024-10-26 04:46:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1d54effb-62aa-3e9f-a955-088033ed18e6 | -16.01832 | -41.19131 | 2024-10-26 04:46:00 | NOAA-20 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 3c3f5a5d-a2d1-3f97-a3d2-0f9db18141a4 | -17.77405 | -42.25996 | 2024-10-26 04:46:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1049b7c2-f5f9-38cd-a21e-7afdba1b5b47 | -17.68775 | -42.11498 | 2024-10-26 04:46:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 62ac6314-0aab-33fe-9edf-137b19cb893f | -17.68253 | -42.11109 | 2024-10-26 04:46:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 554ef494-91a5-3133-877c-f37ac3023ca0 | -17.68206 | -42.11602 | 2024-10-26 04:46:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 74b74cb0-b71a-34de-87e3-1b88c19dc495 | -17.68169 | -42.11397 | 2024-10-26 04:46:00 | NOAA-20 | SETUBINHA | MINAS GERAIS | Brasil | 3165552 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 44cf10a8-5a7b-39a0-977d-ecc20fe48e59 | -18.75185 | -42.14133 | 2024-10-26 04:46:00 | NOAA-20 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2a04cb99-c5ce-3c78-a2ae-e27ab34251cc | -14.55316 | -42.97745 | 2024-10-26 04:46:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db352b7f-5c14-3998-b53a-b967988b8f49 | -14.55272 | -42.98129 | 2024-10-26 04:46:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 29736ec3-fdcc-357a-a5fe-549956f65d24 | -14.54714 | -42.98084 | 2024-10-26 04:46:00 | NOAA-20 | SEBASTIÃO LARANJEIRAS | BAHIA | Brasil | 2930006 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c9e411d-20c5-32e7-bcb0-2836db574326 | -16.04176 | -43.72755 | 2024-10-26 04:46:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1528dd18-a035-3cd6-9ca1-108e43aebf75 | -15.29945 | -43.71037 | 2024-10-26 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1505a83-9374-384a-b941-590635c50b24 | -15.30136 | -43.71003 | 2024-10-26 04:46:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| a6aaa39c-e424-3fd7-98cc-c99804c66fe4 | -13.35715 | -44.26322 | 2024-10-26 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa3fa705-b951-3737-9e9d-a5945b7240df | -13.35678 | -44.26617 | 2024-10-26 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 626ad375-f73c-3ce2-ac17-36ba9b65369a | -13.35175 | -44.26559 | 2024-10-26 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a899ea69-9874-3a0e-9aa0-aaae00bc82c7 | -13.29239 | -43.96193 | 2024-10-26 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f4a1e8d-b2d4-3b6e-a5c1-3143791b5002 | -13.28726 | -43.96136 | 2024-10-26 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3346d67-627e-39d8-b6fc-5a6f0b48d39b | -13.28212 | -43.96083 | 2024-10-26 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b1e972be-3907-3ee0-bcc8-6d6d0c03888f | -13.23328 | -44.63764 | 2024-10-26 04:46:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d8d3018e-0d54-3280-a2a2-87db4d311bf8 | -13.0185 | -43.75626 | 2024-10-26 04:46:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3bfcff9-451e-346d-b399-e1df449f8761 | -12.7092 | -44.39403 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 473f0215-c763-3b40-879d-cad3691fd7d2 | -12.70849 | -44.39968 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9b699205-81d6-3a3e-87aa-ccc6255f4694 | -12.59125 | -43.83823 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8bf2b34d-73e7-3022-a426-1fb12a6f8bde | -12.58614 | -43.83754 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b72b5c5d-37c1-3776-983b-70669e39c63a | -12.58576 | -43.84056 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72a4aed5-51ad-32d3-86e4-b0635aa8c733 | -12.47849 | -43.71836 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1d046eb-2371-39d0-9ad6-456c0da6854b | -12.47811 | -43.72145 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4ec26bce-1a12-318a-9dff-d31cb2365963 | -12.46913 | -43.79297 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9748c367-da21-3559-9b76-6633732b7ffd | -12.4644 | -43.78924 | 2024-10-26 04:46:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ecaa3caf-3e7a-36b7-b2ad-e0ae68f0b5ae | -12.44708 | -44.4188 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 25c2fb8f-5b1d-378d-b759-ffe85998b6e7 | -12.44486 | -44.41667 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a77d99ff-06dc-36cb-a2e5-edfc9793c01f | -12.44215 | -44.39937 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7ab0f3b3-a859-3448-9988-b7bc15e04c74 | -12.44142 | -44.40494 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4f1312b7-19d0-3a67-8f93-d72b2719f86f | -12.43933 | -44.40084 | 2024-10-26 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5b133fa1-e5b7-3286-8cb7-c055a7ccc9a5 | -14.25213 | -44.14407 | 2024-10-26 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e24fc1ed-28b7-3da6-9494-7d863e3ce234 | -14.24663 | -44.14654 | 2024-10-26 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 924f4dee-157c-3093-9e35-b1e5e8b9bdcf | -14.12018 | -44.38968 | 2024-10-26 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 062f0fe3-68bb-3b63-b367-e0e79d67908f | -14.11478 | -44.39201 | 2024-10-26 04:46:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bab848fd-7094-3b8d-bdc7-b612779ae376 | -12.26422 | -45.66101 | 2024-10-26 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3c0f19eb-40ae-373e-972b-bec22b130058 | -12.26361 | -45.66557 | 2024-10-26 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 67900127-91db-3107-babd-e9f3dccc3948 | -12.25973 | -45.66045 | 2024-10-26 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2854fd6b-e3cd-3c5d-9be1-7920326c9d26 | -12.25911 | -45.66501 | 2024-10-26 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f101f628-0833-30d2-8133-305cb17bb25f | -13.33289 | -46.37743 | 2024-10-26 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 429a6ada-e110-36e5-8fca-4adae2fc4f34 | -13.33233 | -46.38164 | 2024-10-26 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9dd6de4e-8512-30da-bb94-2b6fc4adc8d0 | -18.61709 | -46.92937 | 2024-10-26 04:46:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3a813a54-ac3b-3fca-be51-15af870a21a8 | -13.16392 | -47.9032 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcc03f78-8710-37d6-987b-7abf2e83b665 | -12.21608 | -47.24197 | 2024-10-26 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5f06cdbf-1c63-3397-99bb-aacb767e4468 | -12.14956 | -47.00291 | 2024-10-26 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51c70675-f3d6-3998-9b9a-9e5b6a9e4c7e | -12.14909 | -47.00636 | 2024-10-26 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 81e325c0-f8e8-3e79-b9a7-94390f7c63fa | -12.14545 | -47.00245 | 2024-10-26 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94806815-ec31-36fb-a6d6-81a5e74f8e9e | -11.9431 | -47.56732 | 2024-10-26 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2d0a6e6b-4f7e-315f-833e-1f6d2efe7b4e | -11.93916 | -47.56675 | 2024-10-26 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9c83ab49-1a8d-3827-b5b5-bb1e52821eb7 | -13.24208 | -47.23204 | 2024-10-26 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96a304a5-004c-3262-a11d-ff79fa8cdcce | -13.16809 | -47.90049 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56e8e49b-1a16-3e31-bae6-6507a0060014 | -13.16348 | -47.90497 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 820c89f5-5be8-317f-963c-7cf4b6226a84 | -13.15999 | -47.90274 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f08d278c-8ea6-3269-ad77-d549e65b6fde | -13.15955 | -47.9045 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 79a95e4f-eea2-361d-ae81-52903202f4f8 | -12.62543 | -47.54975 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2622920d-d57f-3670-9822-e36afe9028ac | -12.33523 | -47.00751 | 2024-10-26 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1b30a77e-14e6-3958-941d-ecb17416b922 | -12.33061 | -47.01068 | 2024-10-26 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bd07be5d-ee3a-398b-b787-30efe9968a63 | -15.56926 | -47.85725 | 2024-10-26 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7b395080-654c-33c5-9fdd-d3a6bb776fc2 | -18.25675 | -56.0099 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| a153699f-b36b-327c-a8fd-553e7ab3ee85 | -11.95836 | -48.73262 | 2024-10-26 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6e208620-014a-3819-92ee-f3d86ac64ab2 | -11.95769 | -48.73058 | 2024-10-26 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c8961e27-f167-3978-bd65-93b92b3cecc4 | -11.95707 | -48.73498 | 2024-10-26 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f2204d7-27ac-31e7-9a0e-beecba0b4e42 | -13.29482 | -49.57965 | 2024-10-26 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3796400e-cd5c-3ce4-8c92-e02c1a350672 | -13.29124 | -49.57911 | 2024-10-26 04:46:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89138542-876d-3a21-8fb3-94eb83d647f4 | -12.86774 | -49.56334 | 2024-10-26 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b98c361c-6b54-314a-974e-83c626c24730 | -12.66602 | -49.28388 | 2024-10-26 04:46:00 | NOAA-20 | TALISMÃ | TOCANTINS | Brasil | 1720978 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5f1d2640-de1b-3d46-9a27-7287ecd19920 | -12.59849 | -48.77071 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 65e9b38d-a73a-3e38-b32a-c57508865c21 | -12.59784 | -48.77517 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dda39bb-b267-33c5-b086-1f6ae7e5c1ad | -12.5972 | -48.76847 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 8a4fc223-ae24-3f7c-9b12-23c99d6d1885 | -12.59658 | -48.77295 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 53ef0642-4d14-315d-88c2-2440d8979b29 | -12.59479 | -48.77017 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4c9b14b5-768d-3768-aa03-633138aff702 | -12.59414 | -48.77464 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7dfdcbfb-ae11-3a5f-b899-972f4b5534fc | -12.59108 | -48.76965 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e9ae1b34-5fed-3233-a024-8c18ebecbdde | -12.8166 | -48.60111 | 2024-10-26 04:46:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 15e5f3d3-3f37-3274-9ba9-3573a8dec901 | -12.81337 | -48.18491 | 2024-10-26 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 826b24d6-cf07-39b0-bb98-e4e7830b267e | -12.71842 | -48.53099 | 2024-10-26 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fd8b2b8b-b753-3386-b041-2bb60ab3215c | -12.38104 | -48.59504 | 2024-10-26 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a559cc24-4dc2-3858-a01b-5495c9bd867a | -15.76675 | -49.24908 | 2024-10-26 04:46:00 | NOAA-20 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51d59dc7-e334-3697-9dfe-77248374c817 | -18.25465 | -56.00136 | 2024-10-26 04:46:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 039b8c2f-6d1a-3fd1-942c-73298f571f2c | -12.96361 | -49.62292 | 2024-10-26 04:46:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b13f3031-20dc-3735-8c53-37fb4f8f256f | -12.49878 | -49.56594 | 2024-10-26 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 93146dd4-37a1-374e-83a6-241f5831473a | -12.4503 | -49.9002 | 2024-10-26 04:46:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README90.md)
