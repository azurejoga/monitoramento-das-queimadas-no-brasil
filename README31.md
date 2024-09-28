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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69c82cfd-90ea-3a8b-ab86-12536d1e7537 | -13.25306 | -46.32404 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 341.3 |
| f8470890-e3bb-39e9-8135-b9d6745fb1de | -13.25291 | -46.31505 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 772d90ac-b626-341f-886f-3d78f7dc593b | -13.25247 | -46.35978 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f1fa744f-74bf-3d95-a497-7af0cb6e37b2 | -13.25206 | -46.35075 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| f261ac8e-b75b-3cb5-848d-1827c909405a | -13.25162 | -46.32099 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.8 |
| 6b78b094-c892-350d-ae04-2ec33c1bfc83 | -13.25079 | -46.35663 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9d3f6a96-a5da-3d45-8a42-d9dafdbdc38e | -13.25042 | -46.32654 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 465.2 |
| e4fad3eb-b2c7-3501-a8c6-978bfa2be485 | -13.25001 | -46.33866 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 152.6 |
| b21df9b9-dc0d-304e-8939-68861cf0d991 | -13.24871 | -46.33445 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 465.2 |
| 757b37d1-06e1-32bc-b595-0731756726bb | -13.2484 | -46.34639 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 23f1afd3-df8e-3599-8f2a-b0813918ba0e | -13.24717 | -46.35226 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6309e51f-8d39-3d3e-912f-78d1e25661b1 | -13.24687 | -46.34299 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 9e38c568-6111-34fa-8a3c-c3d1758e978d | -13.2459 | -46.35834 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ec6b8a0c-487a-3eb3-b8ae-62aaed77a8c6 | -13.2455 | -46.34935 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 209a4025-d37a-346d-b454-8c940a8abd82 | -13.24331 | -46.3379 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b9f9a0e9-69ee-38ea-a416-8325c06cdba7 | -13.23828 | -46.32919 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6f463bd-07ec-3261-8bd2-f633dd325155 | -12.74248 | -45.57335 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dac1e1d-8a84-32d9-b0e5-6ec9f7030e0a | -12.73723 | -45.56673 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c760fe3-6520-3067-9af7-6e712c7ff5e2 | -12.73615 | -45.57198 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0d369545-cc29-3bc9-a37f-526950ffdfbe | -12.73093 | -45.56524 | 2024-09-28 03:30:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b95b1d5b-dd0d-3b46-9c7c-1bb957dff32f | -17.00959 | -45.92699 | 2024-09-28 03:30:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a91bc50b-2f55-3d9c-97a4-38ee7088a1a2 | -17.00362 | -45.92553 | 2024-09-28 03:30:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6263980-58cb-3b1a-b8c9-9eeab55d587b | -17.00259 | -45.93028 | 2024-09-28 03:30:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46a991e4-b716-3744-9064-8f6a893895cc | -16.58062 | -46.93603 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3587f737-548c-3134-9e24-e91c6b5bac34 | -16.5803 | -46.93521 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0f3e7a8e-57ad-3097-ba19-d1fc4e8b00c6 | -16.57923 | -46.94011 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 580abf55-84d7-3aae-805c-851f541de636 | -16.57531 | -46.92976 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 17634707-a08a-3cbc-951d-74692abe1e12 | -16.57412 | -46.93501 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3e6e8a7a-bc68-3d42-8ada-c7a99d90a95f | -16.57382 | -46.93415 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0ab5f6df-ff8a-3a29-b714-d3e1267b7f06 | -16.57269 | -46.93925 | 2024-09-28 03:30:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 95ed20f1-b5d5-3402-9801-6cd9b6d0dfeb | -11.41989 | -47.25176 | 2024-09-28 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d1a594aa-a16c-3ff4-9129-f3e3a126bae1 | -11.41839 | -47.25891 | 2024-09-28 03:30:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 262dfe4c-7f3c-3d2e-bc71-86535ab70332 | -16.3036 | -48.78074 | 2024-09-28 03:30:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 825b05a3-86a6-37df-b715-53ea97d1813c | -16.30194 | -48.78803 | 2024-09-28 03:30:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e619357-10a0-3872-8f11-2b87ac136d42 | -16.14357 | -48.61897 | 2024-09-28 03:30:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 19e19c1b-9ac0-3943-9941-8856744964f0 | -16.14054 | -48.61654 | 2024-09-28 03:30:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0bd97710-93ae-3e49-8b6f-c22b8a2aaa26 | -16.13893 | -48.62365 | 2024-09-28 03:30:00 | NOAA-20 | CORUMBÁ DE GOIÁS | GOIÁS | Brasil | 5205802 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 748b064f-e25a-36fd-9984-57e3d222e022 | -15.6282 | -47.24182 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b4d6f1f-ed65-3d31-a2b9-b3f82238e9b2 | -15.62287 | -47.23445 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ded3e2b-ae83-3fda-a02f-812d8f07066b | -15.61621 | -47.23317 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2181e28-7833-36ec-80e6-77716851deb2 | -15.40983 | -47.45367 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbe41a97-4e45-3c37-8eba-72048fedea75 | -15.40843 | -47.45989 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 35fde030-a252-3661-8ae3-6f154cec877a | -15.40675 | -47.45966 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 61d0fe14-6385-36f7-bc79-262cdd353108 | -15.40297 | -47.45278 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34b56e96-0a85-3441-9063-18f77a401e6c | -15.40127 | -47.45244 | 2024-09-28 03:30:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 52383599-2791-3b64-a567-75152928630e | -15.30883 | -48.00473 | 2024-09-28 03:30:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| fbfcffef-7adc-3d87-a6a8-cbc611b77adb | -15.30747 | -48.01093 | 2024-09-28 03:30:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5ab7b4fa-427c-3dcf-96c7-f2e154d8be26 | -15.30714 | -48.00369 | 2024-09-28 03:30:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 5912221d-d735-368f-a0d9-281cf219632c | -15.30591 | -48.01803 | 2024-09-28 03:30:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e7a8ed09-f493-3da7-96a2-ddf13a5bba55 | -15.30573 | -48.0099 | 2024-09-28 03:30:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 0bb52179-e812-3c19-8ae6-464b63059e49 | -15.30416 | -48.01683 | 2024-09-28 03:30:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 16f3ca9f-83e4-3219-af81-e3c5bf06dac3 | -17.1412 | -47.62869 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce968984-c06a-3e51-99c7-585fd270a642 | -17.13985 | -47.63463 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b966a6da-4c8d-358f-94e6-efd6aa61232d | -17.1385 | -47.64058 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b3ad3e36-eedc-3268-bf2c-22e2e5f549c9 | -17.13331 | -47.63289 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cea99870-1184-352b-aa28-4dd93d2b2a32 | -16.83971 | -47.68204 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e5c0fd3b-a28c-3447-953e-68a8bb708185 | -16.83754 | -47.67503 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 8.3 |
| fc32ae00-4029-33ec-ae51-b36ba524662c | -16.83609 | -47.68129 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| b9919585-a943-3f51-8dc8-d2adf81eeb93 | -16.83313 | -47.68024 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8236c585-a9fe-38ca-a421-f675e321f750 | -16.83168 | -47.6867 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f373bf61-84f4-3234-863d-ae525d971b14 | -16.82515 | -47.68468 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1c62077-99fb-34f9-a237-2ce09a0fc6c2 | -16.8209 | -47.70346 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 56fdc77b-0a5e-3559-83e9-30f6629e8e76 | -16.81948 | -47.70975 | 2024-09-28 03:30:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2cbe2963-ee29-3de0-98cf-0d7079763353 | -19.39507 | -40.17171 | 2024-09-28 03:32:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3a18be4f-c12e-3adc-8813-1f31e916f0d8 | -19.39408 | -40.17149 | 2024-09-28 03:32:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 0fcf127a-6f42-39ec-aebd-e085d60aedc0 | -19.39007 | -40.17067 | 2024-09-28 03:32:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 7e5ad0f4-e740-3b65-8029-5a6c525b6fb8 | -20.3458 | -40.36097 | 2024-09-28 03:32:00 | NOAA-20 | CARIACICA | ESPÍRITO SANTO | Brasil | 3201308 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| dbf530f2-563b-3bbc-86f1-08b9058cfd57 | -19.00574 | -40.43691 | 2024-09-28 03:32:00 | NOAA-20 | VILA VALÉRIO | ESPÍRITO SANTO | Brasil | 3205176 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ab1503fb-2a2d-31ab-86a4-94d3b0a89464 | -18.76312 | -41.19794 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO DO MANTENINHA | MINAS GERAIS | Brasil | 3162575 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 30298577-fb68-3622-80f3-e16846353329 | -18.76044 | -41.19613 | 2024-09-28 03:32:00 | NOAA-20 | SÃO JOÃO DO MANTENINHA | MINAS GERAIS | Brasil | 3162575 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 671cc1fa-68c8-3181-a021-baab412960d4 | -18.79255 | -41.61742 | 2024-09-28 03:32:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a31f056b-799b-3398-9017-ca58eb804110 | -18.79165 | -41.62212 | 2024-09-28 03:32:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| f625cbd9-a960-35d0-a36c-f85be97833e9 | -18.79139 | -41.61465 | 2024-09-28 03:32:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 870ffedc-c936-30b0-b815-70ffa3b3f195 | -18.79045 | -41.6194 | 2024-09-28 03:32:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.2 |
| 796081a0-e19d-3424-bdcd-ae021e54ee6f | -18.7881 | -41.61657 | 2024-09-28 03:32:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 6267d915-5ea8-344e-bd9c-e63cb4af2603 | -20.86468 | -41.08168 | 2024-09-28 03:32:00 | NOAA-20 | CACHOEIRO DE ITAPEMIRIM | ESPÍRITO SANTO | Brasil | 3201209 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2f33cdc8-aa47-3e84-be70-fd54c7a00998 | -20.54397 | -40.93274 | 2024-09-28 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c9f8588a-4407-38a1-9c01-ca9b3a4a1f6a | -20.54323 | -40.9367 | 2024-09-28 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ced3b812-b3fe-33f9-b313-be9dfb824938 | -20.53988 | -40.93177 | 2024-09-28 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 8da20581-7541-3e84-8a14-1b0ea8eadc5e | -20.53914 | -40.93569 | 2024-09-28 03:32:00 | NOAA-20 | ALFREDO CHAVES | ESPÍRITO SANTO | Brasil | 3200300 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 0e0c24a1-0a3e-3b1d-829a-59f7b48a449d | -20.53596 | -41.1851 | 2024-09-28 03:32:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| aba99016-1d0d-3313-94b5-8b91a6faef29 | -20.53526 | -41.18866 | 2024-09-28 03:32:00 | NOAA-20 | CASTELO | ESPÍRITO SANTO | Brasil | 3201407 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c3dfc479-4060-323d-9be7-473a2406bf1b | -20.273 | -41.32776 | 2024-09-28 03:32:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| c66b2add-75fb-3e42-b66b-cdceb77bcdc4 | -20.2724 | -41.32644 | 2024-09-28 03:32:00 | NOAA-20 | MUNIZ FREIRE | ESPÍRITO SANTO | Brasil | 3203700 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 32847d7d-0d50-32ac-829a-525547b7f88f | -20.26257 | -41.29001 | 2024-09-28 03:32:00 | NOAA-20 | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7df44e7c-5dd6-3871-b04d-0197e0b05420 | -20.26016 | -41.30268 | 2024-09-28 03:32:00 | NOAA-20 | BREJETUBA | ESPÍRITO SANTO | Brasil | 3201159 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 38f1610b-2b6b-392f-9d05-78034aaf6333 | -20.03088 | -40.42636 | 2024-09-28 03:32:00 | NOAA-20 | SANTA LEOPOLDINA | ESPÍRITO SANTO | Brasil | 3204500 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ff353f3b-3e0b-392d-9291-47f149456858 | -19.71706 | -40.35394 | 2024-09-28 03:32:00 | NOAA-20 | JOÃO NEIVA | ESPÍRITO SANTO | Brasil | 3203130 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fdf380bb-c3f1-304b-94c3-3fd56ce83470 | -20.91316 | -41.58044 | 2024-09-28 03:32:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 87a29cf0-237f-3b4e-99db-b6d2d67e9836 | -20.82726 | -41.61983 | 2024-09-28 03:32:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 402ce3e2-c80e-3709-b20b-a6fb8508b09b | -20.82631 | -41.62472 | 2024-09-28 03:32:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 186c6ab3-321c-318b-a5e3-2c345aa15193 | -20.82295 | -41.61916 | 2024-09-28 03:32:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 2ee36478-9fe0-392e-ab6b-49be3551ca67 | -20.82204 | -41.62386 | 2024-09-28 03:32:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| dbf7cc53-85d3-3a0e-aa17-6b400e945443 | -20.8211 | -41.62869 | 2024-09-28 03:32:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 5becc533-0aae-31c9-bebe-fe8b3ca2120e | -20.81777 | -41.62296 | 2024-09-28 03:32:00 | NOAA-20 | ALEGRE | ESPÍRITO SANTO | Brasil | 3200201 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| dc569dc1-b4a5-398b-a939-33d7b60d886a | -20.70527 | -41.77897 | 2024-09-28 03:32:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| ff0e09b1-241f-3f1c-a824-c08fbd7359b0 | -20.70447 | -41.78307 | 2024-09-28 03:32:00 | NOAA-20 | GUAÇUÍ | ESPÍRITO SANTO | Brasil | 3202306 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 14ceaf61-ee53-3046-a1d4-ae8d5c34cef8 | -20.6189 | -41.73803 | 2024-09-28 03:32:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b09ae2ab-2896-3dcc-9e21-815eb56e1142 | -20.61803 | -41.7424 | 2024-09-28 03:32:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0464db0d-48cc-352a-9e73-a7cc4f9af562 | -20.61709 | -41.74018 | 2024-09-28 03:32:00 | NOAA-20 | DIVINO DE SÃO LOURENÇO | ESPÍRITO SANTO | Brasil | 3201803 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |


[Clique aqui para ver as próximas entradas](README32.md)
