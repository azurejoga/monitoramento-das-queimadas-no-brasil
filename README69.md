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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d768da75-cd96-3a35-9200-7b99556d6686 | -2.71326 | -46.7304 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9432569b-88a7-348c-a7e7-a2dcd6afe0f2 | -2.56131 | -47.30574 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 65fe686e-f2c8-3c92-b25d-b7d755980938 | -2.56083 | -47.30904 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9410c7b-0f14-31ec-8af3-c9c20abc58b4 | -2.5577 | -47.30503 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f43f773-6420-3765-90ca-d8b7d33819c5 | -2.55719 | -47.30835 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd9ac23f-1138-3a2b-b2ce-f3979acf874e | -2.55597 | -47.30503 | 2024-09-28 05:08:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4c3d5843-94f8-343b-99b5-479b22748fb8 | -2.3817 | -46.53456 | 2024-09-28 05:08:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aeae2a62-f123-3ee9-9ab9-d025df7882d9 | -2.38115 | -46.53827 | 2024-09-28 05:08:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29d0e2e2-1d64-363c-acf5-589a2745ac85 | -2.1081 | -47.11678 | 2024-09-28 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6a84f1ca-74bb-3918-b1fb-a9891913403d | -2.10759 | -47.12013 | 2024-09-28 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 88de8fad-4731-384c-b20a-1b7bc37ead96 | -2.10709 | -47.12346 | 2024-09-28 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 55e7cdee-58cc-35ab-bf34-e22cbf1cad13 | -2.10658 | -47.12679 | 2024-09-28 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f319c3b1-3b8e-32fe-9777-e4cb9d7d5d76 | -2.10224 | -47.1193 | 2024-09-28 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0c7eca2c-693a-347e-b66d-042fb6323cd5 | -2.10174 | -47.12264 | 2024-09-28 05:08:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 40ea1360-03f1-3336-9f39-63e8e59736fe | -4.56008 | -46.40941 | 2024-09-28 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8fca63ab-3149-3924-82f9-e6ce5f343a4e | -4.55947 | -46.41366 | 2024-09-28 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0eada5b9-1ca7-3864-9fc3-e7cdefbe4082 | -4.53166 | -46.5672 | 2024-09-28 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 88ee4513-9819-3c94-a47a-d246a1750e73 | -4.53106 | -46.5714 | 2024-09-28 05:08:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a1301fa-8072-397f-ac37-fa1711eeb4f1 | -4.4332 | -46.34136 | 2024-09-28 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 438f7fdd-6fbd-3086-9ad8-f4e7dc97b3d7 | -4.43261 | -46.34548 | 2024-09-28 05:08:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ea14afa-0358-346b-8fd8-a9e0732f8b59 | -4.13907 | -46.69028 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b48573ed-59ad-390e-a8c0-89bcb8527ac7 | -4.13854 | -46.69389 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b997d84f-2adf-3b48-b67f-60930be58485 | -3.92107 | -46.44092 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62402a41-a1ac-39c6-9608-99aa8011e2a7 | -3.92048 | -46.44499 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d8f6bd3a-aa53-3d8a-aa5c-e1c789b11869 | -3.9199 | -46.44902 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 559ee65b-dd62-30bb-b363-0fbe5cf2ce1f | -3.91931 | -46.45303 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8eff3550-f635-3f54-a9f0-fe223df1e39b | -3.91815 | -46.46099 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 538d1eac-606d-3ff0-bb36-3f905b6eeaeb | -3.91762 | -46.46466 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5d40b1fc-e844-33f5-819c-07484e69b025 | -3.91711 | -46.46814 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| d1949d17-da38-341a-bfcf-0d5f9019cdaa | -3.9159 | -46.43611 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ce3563d-eb36-31b6-9b94-e4bd8f3ac6e3 | -3.91531 | -46.44016 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 886f0a93-1903-334e-b682-021b7efc5d11 | -3.91299 | -46.45616 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c45a6343-ec58-31a8-8f77-46069d61a491 | -3.9124 | -46.46021 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8ae9e739-5dbf-3270-9932-d6affd60ebc5 | -3.91184 | -46.46411 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| dbddd26b-7197-3ae0-9cf4-1dcc129413ee | -3.91129 | -46.46787 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 466e883a-a577-3c8d-9a46-1250b6fd5fe6 | -3.90667 | -46.45926 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 35fe7eee-83a3-3726-85d4-426830f2c70e | -3.90609 | -46.46333 | 2024-09-28 05:08:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7b809f94-7aff-3f9f-922f-ce0734821da2 | -3.70104 | -47.61262 | 2024-09-28 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9fdbe625-318e-376e-aebb-74a2dca5e421 | -3.69686 | -47.61098 | 2024-09-28 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c69a363a-8dd9-35b5-be07-55f9c0a82843 | -6.08166 | -47.65636 | 2024-09-28 05:08:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4a64f885-d516-3d0b-b368-85c1e5bcdd59 | -6.08117 | -47.6599 | 2024-09-28 05:08:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b9652be4-9975-38bb-8ee4-82037a9fc0d4 | -6.08068 | -47.66342 | 2024-09-28 05:08:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 74f0174f-8655-32fa-b230-a37dfbc43477 | -6.0802 | -47.6669 | 2024-09-28 05:08:00 | NOAA-20 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f3c7a1f-0f94-30a4-b8c5-269b95b492dc | -5.34337 | -46.61066 | 2024-09-28 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89632b2b-257d-3d5e-a9cf-8bb435313208 | -5.3428 | -46.61321 | 2024-09-28 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| adf2368b-f9a3-3453-ab5b-05ccdcf24660 | -5.34279 | -46.61483 | 2024-09-28 05:08:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8d9ee87d-f16c-31b7-998a-625ec163b0a3 | -5.32627 | -47.70461 | 2024-09-28 05:08:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8e6fca3-5cd1-3344-b188-1f57648fdcc6 | -5.32578 | -47.70804 | 2024-09-28 05:08:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 019e195c-5a08-3d72-a529-21aabeb6e750 | -8.35644 | -47.57354 | 2024-09-28 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74fcaba1-2abb-3dbb-98c1-b3a5564e3e72 | -8.35591 | -47.57756 | 2024-09-28 05:08:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d23900b-011b-301f-8746-9f533815d479 | -1.97594 | -48.6927 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a1e6040-d7c7-317f-8705-22ec5cdbb0c0 | -1.97515 | -48.69785 | 2024-09-28 05:08:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f4bdd5f-dabc-3827-81dc-cb7d1112fc7a | -2.91978 | -48.8932 | 2024-09-28 05:08:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7fb3f354-5073-36df-9fcb-2f7aea4f07c5 | -2.63595 | -48.05883 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5d7e53fb-3886-355d-a02f-e0cb87994a2e | -2.63089 | -48.05806 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| def874d0-1b88-3e44-993a-46f7375a91c5 | -2.62659 | -48.32479 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6ba7ecc3-9f62-3ed8-8c28-c4edd305b376 | -2.62608 | -48.32346 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 58bae451-0538-3988-8e50-266eb67fca05 | -2.62162 | -48.32404 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d5c44f0-7136-3928-acf6-3e1df0ff4ab0 | -2.48168 | -48.05956 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34827bd3-6f18-32f6-acb1-e3f579c864a1 | -2.4775 | -48.05296 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| df1e5c12-8140-303c-84ab-283555948348 | -2.47706 | -48.0559 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29db103f-3d27-3dde-90e1-2515cc5e0e4f | -2.47662 | -48.05883 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9fcbffa2-8464-38f1-8cf7-fccb0b74a695 | -2.46079 | -48.43465 | 2024-09-28 05:08:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39045f4f-f6f2-3efb-a20e-b5c2a4615dd4 | -2.34104 | -47.97855 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa9da01a-0a33-3462-80c3-77dfe24d080b | -2.336 | -47.97765 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 704e57b5-6883-30b5-8bdf-4caf214c348d | -2.33554 | -47.9806 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ffae96e8-16e1-3826-addc-8963a2cce340 | -2.36217 | -47.59972 | 2024-09-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 256d9f4b-89b4-33bd-a218-4e8e16bfc522 | -2.3617 | -47.60287 | 2024-09-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff5c0b33-0122-3041-a898-a4616d7b7e1c | -2.36123 | -47.60598 | 2024-09-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b78c2a6-a05d-3f91-bbf8-32b1f7929435 | -2.36076 | -47.60906 | 2024-09-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4de797f2-666a-3f42-9631-529862ecff14 | -2.36029 | -47.61213 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a78b6b1-f5b8-31c8-9e92-bacf3694ee84 | -2.35697 | -47.59898 | 2024-09-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e2acc4f0-2a00-37f4-b81a-6dc8a00bc015 | -2.3565 | -47.6021 | 2024-09-28 05:08:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 28693c04-f9cc-367d-8049-86ab9d1008d6 | -2.35603 | -47.6052 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 21864780-3ebd-3dba-9987-405ccdf1da5e | -2.35556 | -47.60827 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 30f0c0b8-1b73-3295-b40e-7624545cc476 | -2.3551 | -47.61135 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ff74ec5-eedb-3150-8750-1e3d914dc987 | -2.35463 | -47.61445 | 2024-09-28 05:08:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36a60a56-b6d3-3663-97bc-31bbb2d40fc1 | -3.70167 | -47.61501 | 2024-09-28 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e8142a-0f38-3116-9bb7-e45d4457ee1e | -3.70057 | -47.61589 | 2024-09-28 05:08:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6d2d1d0-19b3-3379-87ea-09f74beb68fa | -3.46849 | -47.66465 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 9884a9e6-5306-312e-b066-40a161c731e9 | -3.46838 | -47.66679 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 546342b0-72f5-3f97-b31e-fc4652424b5c | -3.46802 | -47.66797 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 35a5589d-a8fe-3b10-a4d2-18b989ce1c4e | -3.46788 | -47.6701 | 2024-09-28 05:08:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bec6f836-c2b2-30df-9cf1-2d23f3b0aece | -4.91203 | -48.61123 | 2024-09-28 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0871aa0f-fa1b-304a-9dfc-2a3826c3693a | -4.91161 | -48.61412 | 2024-09-28 05:08:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43177e0e-814a-38dc-b2a0-7c900ab743f0 | -4.7929 | -49.35648 | 2024-09-28 05:08:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de2aaa4a-f119-3847-8f36-4364f3dfb8f1 | -4.63168 | -48.53606 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 43422780-6a7b-37be-a0f0-c40132463a2c | -4.63125 | -48.53893 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 26e522c6-4db5-3c46-83aa-2fe5d1a9e075 | -4.63109 | -48.53474 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ce727ec9-48ca-3311-a4f4-96fcff8315f2 | -4.63068 | -48.53759 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7f93a381-398d-392f-81dc-729892314093 | -4.58174 | -48.00786 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6990c9ac-e43e-3f14-995d-9146f43aac6b | -4.58127 | -48.01104 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 61edda17-05f8-301f-8c12-f78784d60dea | -4.5808 | -48.01421 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| bd44ebc9-d2f8-3acc-92a1-e1c8bfee3fe0 | -4.57849 | -48.02988 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0be881b1-6e72-3b1e-9720-4509864ebb76 | -4.57804 | -48.03295 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0fb47f83-7b0d-30cb-97e6-cb909723af1c | -4.57484 | -49.30964 | 2024-09-28 05:08:00 | NOAA-20 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 0882acbf-8ebc-3c5f-877a-6edb928fb00e | -4.28414 | -48.56816 | 2024-09-28 05:08:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6c18d5a-ee29-323b-90c5-7c5c742d2a69 | -4.2776 | -48.0661 | 2024-09-28 05:08:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5301a76-f7e2-3575-aae1-ee04ef93c118 | -6.544 | -48.70774 | 2024-09-28 05:08:00 | NOAA-20 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2c4d4f4d-7013-3642-87ed-7f4e9562ab96 | -6.30865 | -49.45386 | 2024-09-28 05:08:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README70.md)
