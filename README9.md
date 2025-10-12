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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26864f4a-64b2-381f-a6da-2ee27006a9d0 | -3.5152 | -45.8634 | 2025-10-12 02:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 4615e04c-6b02-3b37-9c7b-0fae436d1100 | -19.0515 | -57.5564 | 2025-10-12 02:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 51.7 |
| 6333fd3b-6400-301d-bc88-6b1f64f3abb2 | -3.5152 | -45.8634 | 2025-10-12 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 45b30150-b094-3a64-b307-dfb0bde68051 | -17.2701 | -52.2627 | 2025-10-12 02:50:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 0e287c74-aea5-34df-8366-8d2b67ded541 | -4.271 | -46.9369 | 2025-10-12 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b5dcd4d8-bc03-3ce6-8765-ac0a8a548183 | -19.0319 | -57.5382 | 2025-10-12 02:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 67.5 |
| 859818a7-2aa4-382b-9f20-d6f83eec2005 | -12.2051 | -64.367 | 2025-10-12 02:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 1f47fdf4-101b-355a-b1fa-41e2b66c7d92 | -14.0155 | -43.4943 | 2025-10-12 02:50:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 3ba6ed72-fc83-3c7c-b370-b30ee26a0076 | -3.5153 | -45.8411 | 2025-10-12 02:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ce2ff1a9-3076-3010-b497-e77e77448025 | -17.2504 | -52.2658 | 2025-10-12 02:50:00 | GOES-19 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 74.8 |
| af924a6d-7f4d-3591-9933-5c0a0aed84aa | -2.5423 | -47.811 | 2025-10-12 02:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| 79639c1f-9fd2-3c0a-9ab1-e17c003e40d8 | -19.0519 | -57.5356 | 2025-10-12 02:50:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| abacab0b-2401-3be7-91d6-a6353f5d4e18 | -4.271 | -46.9369 | 2025-10-12 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 784fe0bf-71e0-32c5-80b5-04c0e6a0940a | -19.0319 | -57.5382 | 2025-10-12 03:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 97.5 |
| 4f3d1b5c-5176-37d9-8725-08b096666e35 | -3.5152 | -45.8634 | 2025-10-12 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| b4f963b6-0acc-3e89-940e-6b02b6701283 | -19.0519 | -57.5356 | 2025-10-12 03:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 97.4 |
| 87a26eff-400a-39f0-ae9f-075cfebb386e | -12.2051 | -64.367 | 2025-10-12 03:00:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| b2e72933-0b4d-34c8-86a5-b40378e9f478 | -19.0515 | -57.5564 | 2025-10-12 03:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 79.8 |
| 4d7579bf-9661-3996-b860-002f19594b14 | -19.0316 | -57.5589 | 2025-10-12 03:00:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 53.7 |
| 52bb1d23-173b-3929-8332-6500a590715e | -2.5423 | -47.811 | 2025-10-12 03:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 67afe85b-634f-3eea-b873-c06146921609 | -7.5212 | -46.538 | 2025-10-12 03:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| d8680cdc-dce9-3054-a2f8-4dcc63fb9a82 | -3.5153 | -45.8411 | 2025-10-12 03:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 14d9a879-2858-3843-98c0-808a5b9c60f9 | -19.77665 | -42.39838 | 2025-10-12 03:06:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 29954de0-6e29-3e62-aebf-2799f534f366 | -19.77785 | -42.3956 | 2025-10-12 03:06:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b342677a-57ec-3351-ad38-2579575697d1 | -19.7626 | -42.42563 | 2025-10-12 03:06:00 | NPP-375D | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 966fe7db-ca02-3b82-9b83-214efdba828e | -19.7849 | -42.39796 | 2025-10-12 03:06:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| c8464cca-bc7e-3329-b225-310a9bedb670 | -19.76968 | -42.42796 | 2025-10-12 03:06:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 42af04cf-9738-3b7a-ab76-d463e70b0e8d | -19.78373 | -42.40068 | 2025-10-12 03:06:00 | NPP-375D | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| d946a649-ba22-35fc-9ab0-752ba14dbc4c | -12.2051 | -64.367 | 2025-10-12 03:10:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e7880924-c05d-3cf4-b2f3-1457051cbb01 | -3.5153 | -45.8411 | 2025-10-12 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 73e7782a-5668-3929-8c65-17a9402538d8 | -2.5423 | -47.811 | 2025-10-12 03:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| 982a6c51-fc06-3121-991c-b00ef14cefac | -7.5212 | -46.538 | 2025-10-12 03:10:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 0b3ba802-5f8b-3563-b887-f31de6e3095f | -19.0319 | -57.5382 | 2025-10-12 03:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 54.7 |
| 1c6b6f51-a50a-39fa-bf94-56f2fc44e86b | -14.0351 | -43.4906 | 2025-10-12 03:10:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 534f5538-2044-3cca-8b96-c827db3ddc3f | -3.5152 | -45.8634 | 2025-10-12 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 93.3 |
| 913942f8-bda1-3662-b907-efbc814b4578 | -4.271 | -46.9369 | 2025-10-12 03:10:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 10483511-e7a4-3783-8db9-56a08a2b4ca4 | -14.9572 | -46.7327 | 2025-10-12 03:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 97eecb00-cc3e-3378-8909-97113553095d | -2.5423 | -47.811 | 2025-10-12 03:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 7d3ca755-3454-3821-ae7f-ab14707b16f2 | -3.5153 | -45.8411 | 2025-10-12 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 9e05233c-f1e8-3cae-8fcf-16e32ce4d374 | -19.0319 | -57.5382 | 2025-10-12 03:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 46.6 |
| 1303b036-7dbf-36f1-8ed7-b8666dd90d69 | -14.0155 | -43.4943 | 2025-10-12 03:20:00 | GOES-19 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 89cbf194-3903-39b0-b61d-2c6459abf16e | -4.271 | -46.9369 | 2025-10-12 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ace1f410-b914-31fd-9d8b-1a49f3c782c6 | -3.5152 | -45.8634 | 2025-10-12 03:20:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 64.0 |
| b937e271-467c-371a-a6c7-5606b4399a62 | -12.2051 | -64.367 | 2025-10-12 03:20:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 64974fb9-ec85-35dc-ba9c-16c0e57ee47a | -7.49335 | -42.76791 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 380c7deb-08bf-383a-8a3c-ba8ada58bd5d | -6.7423 | -42.80737 | 2025-10-12 03:21:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 727b3243-f8c3-3676-aca7-47b263774d18 | -5.05758 | -40.46254 | 2025-10-12 03:21:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 321c411c-b2bb-3a57-90c4-62e797232afb | -5.08997 | -38.83162 | 2025-10-12 03:21:00 | NOAA-20 | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ad95c125-f79b-310f-91f7-2507587ea208 | -5.49306 | -43.07568 | 2025-10-12 03:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 335be0aa-681e-3baf-b475-79d3db52fe43 | -7.50619 | -42.15084 | 2025-10-12 03:21:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 527f6c91-bc04-3692-b190-96ec3773d0fb | -5.92482 | -40.88638 | 2025-10-12 03:21:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 7febb70e-787b-3d22-a9f0-6cfc7c3b0896 | -5.47039 | -43.39864 | 2025-10-12 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 927bf2d1-1e6c-3311-ad73-eea997957369 | -7.79741 | -42.43828 | 2025-10-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b138101a-fc29-3349-a066-8e37533b96cf | -7.49235 | -42.77311 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 8b6e86cb-93ec-3bdd-aa6b-e2026ca29f87 | -4.42726 | -43.47436 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4bcbc959-a3b2-3a37-963f-044bf8b8fad0 | -4.67146 | -43.26024 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9fc21a5d-c220-326e-ba69-821728256c96 | -6.95908 | -42.4384 | 2025-10-12 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 8a501d44-5bd8-3db4-bed3-7d33cf2e2f94 | -7.213 | -39.91164 | 2025-10-12 03:21:00 | NOAA-20 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 5.2 |
| f2547904-d204-34c2-b4b7-21d345c06e53 | -7.64899 | -42.58428 | 2025-10-12 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| a0afa851-b4ba-3a3c-bb86-f0fcf640ee72 | -6.36432 | -39.10282 | 2025-10-12 03:21:00 | NOAA-20 | ORÓS | CEARÁ | Brasil | 2309508 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9da197e2-60b5-363c-a70b-802052381176 | -4.82068 | -43.1412 | 2025-10-12 03:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9a3c68bf-3a66-3a11-8ee0-d3e4c14dd82b | -5.7374 | -40.76764 | 2025-10-12 03:21:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 71685eac-fb7b-34c3-ad01-94a09245c0e1 | -7.48587 | -42.77199 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 958f00f0-72bf-3f08-b656-25e4b237e953 | -6.7642 | -42.83512 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 1314b1e2-49ff-30ea-834c-35821733b9e0 | -7.65517 | -42.57826 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 75a14788-ac69-3501-9c9e-0153c7a13eea | -6.25049 | -43.03468 | 2025-10-12 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 294356d2-ce0a-3f4e-94f4-e765fca04151 | -5.90014 | -38.47245 | 2025-10-12 03:21:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c7a2bed-ea46-3948-852d-baf67e5616ec | -7.40802 | -42.97107 | 2025-10-12 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 22fc6fd5-c134-30b4-ba7c-2efe1a8365de | -6.76304 | -42.84129 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 4246522d-4e61-366a-b55f-ef080bcea059 | -3.61091 | -42.7584 | 2025-10-12 03:21:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54597bd2-58d7-39df-8967-e78b5c144192 | -7.42772 | -42.9744 | 2025-10-12 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8933480e-480a-34b2-9a10-85c181da6f7a | -5.74329 | -40.7686 | 2025-10-12 03:21:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b98a77e9-d8e3-32f4-98e5-d8282c3f934c | -6.24831 | -43.03055 | 2025-10-12 03:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f961238c-5fa9-3b21-bc6f-d913fd39f92d | -3.34723 | -42.16132 | 2025-10-12 03:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 11c22141-8f37-3d65-8016-41415b8fcd92 | -3.87375 | -42.51265 | 2025-10-12 03:21:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 8a061203-e193-3db7-9fcf-68b651ee7c66 | -5.47645 | -43.40182 | 2025-10-12 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b767de92-1974-36d4-9f85-bc56438a87b7 | -3.34622 | -42.16712 | 2025-10-12 03:21:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7bef9385-2ec6-31fc-baaf-abbbffb13332 | -4.41612 | -43.47078 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1850d5c1-99a6-3d6d-b1ae-3daa359510a1 | -6.75997 | -42.8215 | 2025-10-12 03:21:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| fcf4c2a1-d0c8-341d-a148-a0de37dd9da4 | -8.9072 | -38.41314 | 2025-10-12 03:21:00 | NOAA-20 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0e9b5101-effb-3eac-a071-510d09488aad | -9.05312 | -38.95139 | 2025-10-12 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| be6f01a6-201e-3444-a360-1434e328ef19 | -7.48712 | -42.76403 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3305177b-65d4-35fe-94d2-e4f681dcf950 | -7.49165 | -42.77567 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| adebf6d9-1fd4-3f21-83aa-aa05be6c0dee | -7.42225 | -42.96744 | 2025-10-12 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 894ab2b3-8f1e-3b70-a011-e0d370b85bcd | -5.23345 | -35.59854 | 2025-10-12 03:21:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 435f7972-ed0d-3110-a9fa-5decfbca1356 | -6.9601 | -42.43298 | 2025-10-12 03:21:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 901199ef-66f0-311a-8891-fdfe588e3db6 | -6.49639 | -42.44303 | 2025-10-12 03:21:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 4cc1525e-cc25-3f00-8325-d9378bf28abf | -7.4879 | -42.76146 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5256b7d0-1098-3abb-bbbb-48a63afab369 | -7.85642 | -44.53531 | 2025-10-12 03:21:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5d95c16-f14b-361f-90c8-6b75ba635336 | -7.40041 | -42.97545 | 2025-10-12 03:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 591b653d-4b98-348d-9b48-a0b50ec3a669 | -5.73955 | -40.76443 | 2025-10-12 03:21:00 | NOAA-20 | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9aae7aa3-70c4-39fe-a515-589ec546942a | -9.05209 | -38.95715 | 2025-10-12 03:21:00 | NOAA-20 | MACURURÉ | BAHIA | Brasil | 2919900 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ff7736ab-1892-3f6b-b99c-60b0f2c2ed89 | -8.19046 | -43.32512 | 2025-10-12 03:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 653a53a8-a509-3c05-beb7-ff155f1e670c | -4.419 | -43.47983 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f75ba369-8b4a-3b6e-b2ee-ca887e8c2868 | -7.80374 | -42.43932 | 2025-10-12 03:21:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dea2f76e-8373-3e3f-88c9-134b05f447dc | -4.42023 | -43.473 | 2025-10-12 03:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f8d0f24b-357b-370d-9eb2-2e300686c161 | -7.48688 | -42.76677 | 2025-10-12 03:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 42f31c8d-2f01-3c9a-a9f0-5a4f0aa065a5 | -5.90454 | -38.47714 | 2025-10-12 03:21:00 | NOAA-20 | PEREIRO | CEARÁ | Brasil | 2310803 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ee642042-a3f2-38aa-915b-05588e819c13 | -7.65008 | -42.57858 | 2025-10-12 03:21:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 27d07e74-4d9e-3f5d-8aff-a7b0acda59a6 | -5.46956 | -43.4004 | 2025-10-12 03:21:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README10.md)
