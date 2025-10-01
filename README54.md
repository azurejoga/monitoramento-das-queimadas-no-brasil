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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 54ced633-5e16-323e-b16f-f2cf6d8ef193 | -14.01161 | -44.99361 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09c29800-1728-33c4-8339-3ab89b22bf8b | -14.23588 | -49.79254 | 2025-10-01 04:21:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e090197-c499-374f-bfbc-6a248ab16e73 | -10.83802 | -45.40741 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 70265d0e-1ecc-3d84-8f07-8d7610a2d4ff | -15.47645 | -48.07534 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c79a23f-77a6-3e86-bd5a-3ce8802bef51 | -13.61995 | -47.61627 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1c6c09a0-cca1-3bbd-9eda-75be928e6eea | -13.94263 | -48.10295 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1396acfa-74f3-318f-b4b6-16d50752513f | -13.67253 | -48.07351 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71216499-344c-3044-b3da-ff5b43dd45ca | -16.39663 | -47.04292 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2efd37d0-9d16-3492-9f96-fb9e66c143fe | -11.8336 | -44.96942 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 421c12a3-6345-3ec3-aeff-bab7365809af | -15.28389 | -52.89605 | 2025-10-01 04:21:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc603483-c0f0-3e27-82a2-e8ed5c9d1a4c | -12.97123 | -48.42856 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76922baf-3ca4-307b-82f6-6b1731f311b7 | -13.918 | -48.08395 | 2025-10-01 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8eab09f4-300c-38b9-abd8-a5482e419352 | -12.76999 | -50.55923 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 999769c2-769b-31a3-a61b-2db75c4894e4 | -13.05873 | -47.08066 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7dc299e7-c9b5-3990-967f-f09ea08ff48d | -15.6122 | -46.53185 | 2025-10-01 04:21:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66d1eec9-6bd8-3a52-8129-90c124e29b31 | -15.36626 | -56.97105 | 2025-10-01 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7b35af6b-c9f4-380b-b918-2a6bb2748df4 | -12.01523 | -46.62074 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 186fe61c-2875-3681-bca7-d256c822a383 | -13.81057 | -43.81465 | 2025-10-01 04:21:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a5ae92cf-0957-3ef6-9fe1-0651d650fd22 | -14.019 | -46.3215 | 2025-10-01 04:21:00 | NOAA-21 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 73869064-06cf-3e24-830e-4abd7bd68b39 | -10.90137 | -45.72178 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 66972916-4143-3907-a3c6-6435729bbee2 | -11.12332 | -49.78905 | 2025-10-01 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6616dd05-5552-3ba2-97ab-b07f369da3bd | -13.54149 | -47.25574 | 2025-10-01 04:21:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| e9fdbb2d-6894-333f-ba2f-f758fd56db7a | -15.78376 | -43.68409 | 2025-10-01 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 67f186bb-6bd1-3cf1-b7ec-d40a6417b30a | -11.28232 | -39.22337 | 2025-10-01 04:21:00 | NOAA-21 | SANTALUZ | BAHIA | Brasil | 2928000 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a0c263b1-1f8c-33ca-94b9-defa6d833377 | -13.70401 | -48.63368 | 2025-10-01 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 33e079ce-7df2-35ce-91ba-de53c4af47af | -11.49952 | -43.50952 | 2025-10-01 04:21:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4195b071-e1a6-33a6-8322-2ab040494852 | -13.37885 | -47.31357 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8fed6fa-bb0a-368c-b8fc-1018e0232d18 | -14.70117 | -48.2579 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c0bfbdde-9e7f-36fd-9892-b67bf6e5b0c9 | -11.47055 | -45.07602 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 745374e4-538a-3545-878f-3ad150f77848 | -13.77697 | -47.97256 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d93153e3-63b5-3d21-ba24-0db15323bf75 | -15.26453 | -49.27461 | 2025-10-01 04:21:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2fa36412-77b0-32b0-b7c0-421664a14b84 | -13.56874 | -48.19791 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87dc0d7e-504d-3caf-85a0-1b3b2c070ac6 | -16.24831 | -50.93488 | 2025-10-01 04:21:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| fa10f60f-8b78-3ff1-8f7e-33aa8f28455e | -14.35429 | -45.93634 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 0ecd8cab-ecbb-3af9-aec7-8eed43d6a0e3 | -15.14885 | -48.01598 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 888ee316-0fca-3578-9073-084a678a830a | -13.98202 | -45.05292 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5da9ba2-6e94-3f60-96ac-4de5fcd99bf3 | -12.68963 | -48.56073 | 2025-10-01 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ad6e550b-5142-35a0-a6e7-ddc63012736d | -13.67354 | -46.79004 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a8b84a03-933b-3819-a512-6b976b0c0ba1 | -17.39095 | -47.16569 | 2025-10-01 04:21:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bb3f256-dd79-3351-b4a0-f0855f59fde6 | -12.4199 | -43.20396 | 2025-10-01 04:21:00 | NOAA-21 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2a0a192-279c-331f-a7fa-ff0a1111f7e3 | -12.89387 | -45.2607 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe6d4823-0fee-3a58-98f0-afe89e360178 | -16.37951 | -47.06572 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 65478711-9bb4-3022-ae93-a9ddd5986a34 | -12.00098 | -46.58223 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| de9c1bab-b7fb-3c41-8039-71fc83d29814 | -11.85035 | -45.01582 | 2025-10-01 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0951cf93-7752-323e-a39a-47d861ec072c | -16.08164 | -51.04515 | 2025-10-01 04:21:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7bd4af83-3581-309a-a72e-c9c25ccd19f8 | -14.6816 | -45.27825 | 2025-10-01 04:21:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a1136719-6d66-32b9-a449-1c01d63fbb4c | -15.48052 | -48.54849 | 2025-10-01 04:21:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dcf38959-30f4-38c3-9343-77244aa4a811 | -15.36532 | -46.10345 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f94d1d6a-179d-3939-bfb6-a99e71f67777 | -12.01196 | -47.99676 | 2025-10-01 04:21:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b1420e6-9e20-363d-899e-c9a6ef8f543f | -15.33945 | -46.27164 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f7da3504-0d90-3269-a82d-e510d1040318 | -15.37196 | -47.06886 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e701a769-6442-380f-969f-1e7aa632bd09 | -13.32415 | -47.33768 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 09f1a469-20fb-3a67-bd83-535967d63cd9 | -15.84864 | -46.25547 | 2025-10-01 04:21:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f2cd81-cb01-3110-b5c9-f51557b386fb | -14.90765 | -47.20684 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6cc33315-4870-3794-ad56-0da362e1be03 | -16.00636 | -50.8735 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5cbde3a6-d42f-3921-b7d6-50a53192767d | -14.83123 | -48.12775 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74848e00-86f9-354e-8a3e-ef98b885f488 | -10.79117 | -45.35695 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 469adc66-5914-3bd6-a3f0-6f5ce9f7f519 | -16.01299 | -50.87951 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b221fbb5-169d-3864-91a3-904c501e48e3 | -13.05711 | -47.0694 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 93fe2fb3-473c-3f75-9d5e-384cdd15da0f | -11.57475 | -47.64105 | 2025-10-01 04:21:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7ec4dff7-c58e-3180-a9e3-f96e2f620d56 | -16.0194 | -50.90892 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 681a623f-acbd-311f-8f48-288a07a26d97 | -12.90997 | -46.81885 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5b03fa49-591e-39fd-b676-c952c823665f | -11.76395 | -46.87388 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3e41c60-67a7-3b5d-b619-3d69e3fe8cf1 | -12.24077 | -47.823 | 2025-10-01 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ae8f9595-2b58-31b8-943e-c7c51ab35d07 | -15.53458 | -45.22393 | 2025-10-01 04:21:00 | NOAA-21 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| bca1711b-4137-34b2-a94b-fe5fa9d73e09 | -14.89921 | -48.10485 | 2025-10-01 04:21:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ab90b373-7dd0-3e5f-ad1d-38cec2e109fb | -12.85147 | -47.03524 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6f049321-0d2e-3f49-b0f5-01141b8d19c6 | -9.43289 | -54.56831 | 2025-10-01 04:21:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5ad0ab1e-6c2f-35e8-8c70-031196dad15c | -16.02756 | -50.90615 | 2025-10-01 04:21:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4855aafd-ad70-396e-ae1f-f6277ce926e1 | -13.36023 | -48.09752 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a195fcf4-0fae-3238-a3b0-cca171e3eff4 | -14.02058 | -44.97987 | 2025-10-01 04:21:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5604385c-63da-312b-9563-d86e82a530f5 | -14.99002 | -46.96505 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bfdc0c7f-fd0d-3ebf-9436-fe22cac3d798 | -15.3375 | -47.94323 | 2025-10-01 04:21:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6da09c15-c390-3557-a3a8-1a817f1f193e | -13.20906 | -47.33307 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4668fea-8319-3ec8-9c58-ceab5c0b49e6 | -10.84547 | -47.25347 | 2025-10-01 04:21:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c2b98a3f-3e72-3f56-a2df-0990512d5ec4 | -16.38403 | -47.01514 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09084e5c-2de6-38f8-9239-77c89793f6bf | -15.0131 | -46.96893 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af2d998c-ef77-3fd0-a9a0-057872fafad1 | -12.95624 | -46.4147 | 2025-10-01 04:21:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ea0d982a-3f30-3730-938f-61cdd2994097 | -15.61171 | -46.9077 | 2025-10-01 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 599b9def-16f5-3f37-9af0-5791edef421e | -14.35316 | -45.92156 | 2025-10-01 04:21:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9c64f9c-dec1-3159-b893-61a30e8d04f8 | -14.19226 | -46.12523 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 9518f556-97ac-321e-a9f1-e23146853e80 | -13.33615 | -47.81107 | 2025-10-01 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ac65d300-3d01-3af0-b6b8-40965589dc86 | -14.98728 | -46.96092 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ebda025-2ca4-3e31-92b3-c8c04b516d61 | -10.90815 | -46.54056 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 345af366-d244-3740-8e63-374f53f374b7 | -11.73694 | -44.4247 | 2025-10-01 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 68e5afe0-820d-3061-b339-e41435cd6878 | -12.94825 | -48.4211 | 2025-10-01 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2808428-5d68-3d5b-8359-783f4742540c | -10.97964 | -46.54128 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad6a7b0e-6c5d-3105-b76e-c6891ef3a3af | -13.22126 | -47.34224 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 662671f6-139f-30b7-b9bd-460b35ac92db | -11.74403 | -46.87056 | 2025-10-01 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73279431-b20e-3c9a-bd2a-43247f94a9d7 | -13.301 | -47.22674 | 2025-10-01 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2aa808d8-0ac0-3423-b660-17f06110ff4a | -10.91303 | -46.57394 | 2025-10-01 04:21:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 809ed79d-fa87-30db-9212-51832fc4521c | -13.55733 | -48.20366 | 2025-10-01 04:21:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3086aef5-b547-3f9c-9d22-068c2a084782 | -12.88444 | -45.25552 | 2025-10-01 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4df290c1-85ee-3db0-9bb5-a5fd9df6eeac | -12.87641 | -46.94407 | 2025-10-01 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5bb644b-65b1-3126-9e84-9eb22fcfd273 | -15.63026 | -49.17218 | 2025-10-01 04:21:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 374825e9-56e8-3b56-839a-bb15a9e53e10 | -14.995 | -46.9549 | 2025-10-01 04:21:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b4ad8c46-f919-30e0-b67e-984d6c0455dc | -14.21357 | -46.09953 | 2025-10-01 04:21:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 204d578a-f528-35a1-9447-0075a0c60425 | -16.37901 | -47.04731 | 2025-10-01 04:21:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e67f963-2eed-3008-b6f0-debf6ccfe837 | -14.91237 | -51.67763 | 2025-10-01 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 424b3922-0b98-31c7-80d0-b05d1f297be9 | -14.76368 | -48.09786 | 2025-10-01 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README55.md)
