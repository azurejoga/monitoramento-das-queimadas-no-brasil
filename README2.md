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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0af0fb70-905d-3c9b-a71b-6430f0728971 | -21.045401 | -48.7981 | 2026-03-24 00:47:00 | METOP-C | PARAÍSO | SÃO PAULO | Brasil | 3535705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8a6f65ef-7e71-3ede-9fba-a21f5065afce | 3.3632 | -60.1208 | 2026-03-24 00:47:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 840a1f12-017d-3c19-8e29-b0c80f7cf604 | 3.3485 | -60.1339 | 2026-03-24 00:50:00 | GOES-19 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 54e8fee0-2052-39ff-9117-e5322625c161 | 2.032 | -61.1013 | 2026-03-24 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 7f83325a-2cd5-39db-98f3-f43b6df37418 | -20.1686 | -46.6738 | 2026-03-24 00:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 87.9 |
| e6930cfa-0d49-3487-bd1a-46f3df32a210 | -20.1693 | -46.6501 | 2026-03-24 00:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 786c42a0-e597-355f-b0a3-8e00d330a63e | -20.1481 | -46.6787 | 2026-03-24 01:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| e8683651-a31a-3eae-a0e8-df2bc0e7201d | -20.1693 | -46.6501 | 2026-03-24 01:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 3a450148-e765-3c91-be3c-65b7cf9c5c7e | -20.1686 | -46.6738 | 2026-03-24 01:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 3658fd25-06fc-3348-af87-84374cfba02d | -20.1488 | -46.655 | 2026-03-24 01:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 35ebf97d-348a-3de3-aa12-d04939a7a2f1 | -20.1693 | -46.6501 | 2026-03-24 01:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 116.6 |
| b12b5217-354c-3139-9050-25fdc71c162b | -20.1686 | -46.6738 | 2026-03-24 01:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 107.4 |
| c8e4af28-7740-3f95-b1ff-db28ecf1b5b6 | -20.1481 | -46.6787 | 2026-03-24 01:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 47f6779a-02a0-3887-91c1-059f18cc5241 | -20.1693 | -46.6501 | 2026-03-24 01:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 110.0 |
| d3fc5cae-68be-3523-a72b-78db86df132a | -20.1686 | -46.6738 | 2026-03-24 01:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 38f0704f-16ec-3e28-ba90-483b35503245 | -20.1488 | -46.655 | 2026-03-24 01:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 132c9273-6c7f-36af-8750-8e991fb1f6dc | -20.1481 | -46.6787 | 2026-03-24 01:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 91.1 |
| efef0220-8466-3f25-840c-6e7bfe7f330e | -20.1481 | -46.6787 | 2026-03-24 01:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e060c536-ef47-3c3f-9674-18a95c144058 | -20.1693 | -46.6501 | 2026-03-24 01:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 9e76f3e3-8d51-3a5e-a2d2-9a9248943e78 | -20.1488 | -46.655 | 2026-03-24 01:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 4d27e60f-8d22-35bb-8be8-0dfc00d3514b | -20.1686 | -46.6738 | 2026-03-24 01:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 111.8 |
| 19be1614-8737-342d-b998-c2fdb4fa84dc | -20.1481 | -46.6787 | 2026-03-24 01:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 9f6768e5-57a0-3dce-8bce-0b4620002576 | -20.1686 | -46.6738 | 2026-03-24 01:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 8d8d95e5-9e54-30ea-ae93-8b73c129ad22 | -20.1693 | -46.6501 | 2026-03-24 01:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 78c32bd1-455c-3081-bffa-8543a732892e | -20.1488 | -46.655 | 2026-03-24 01:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 6d79fefe-7194-32b5-907a-07255d8d6676 | -20.1693 | -46.6501 | 2026-03-24 02:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 9caf76ba-336b-3db0-8db7-8d00a295a7dd | -20.1686 | -46.6738 | 2026-03-24 02:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 17adc09e-a374-3a9b-9c3c-af0d9658b1e2 | -20.1481 | -46.6787 | 2026-03-24 02:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 039b370d-1884-3d53-8f11-bb399f67eeda | -20.1686 | -46.6738 | 2026-03-24 02:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8281dbad-3287-365d-b3e3-68ebb00935c7 | -20.1481 | -46.6787 | 2026-03-24 02:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 85.6 |
| d0a54a3d-877e-3092-8295-673a01e31ccc | -20.1481 | -46.6787 | 2026-03-24 02:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8703aaa6-376e-3094-a7a3-a1e7b0ff0d46 | -20.1481 | -46.6787 | 2026-03-24 02:30:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 84ce3310-7fef-3f2e-bd19-133015a6331a | -20.1481 | -46.6787 | 2026-03-24 02:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 413a41a7-9a39-3d15-b88a-327be3518168 | -20.1686 | -46.6738 | 2026-03-24 02:40:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 563e7d83-0f42-36d7-9e2c-5d44d72b7b3a | -20.1481 | -46.6787 | 2026-03-24 02:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 78.6 |
| fdd51cbf-5587-3084-9f3a-9c66598af07c | -20.1481 | -46.6787 | 2026-03-24 03:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 77.2 |
| ef7a667a-26cc-3ef5-85ef-d3680c7ea553 | -5.94096 | -35.62455 | 2026-03-24 03:17:00 | NOAA-21 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fe6a32e9-0aac-350c-8ecc-4c9238e03e84 | -7.72344 | -38.14719 | 2026-03-24 03:17:00 | NOAA-21 | MANAÍRA | PARAÍBA | Brasil | 2509008 | 25 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 9c145c10-09d5-352e-bc07-746c12165e78 | -6.82103 | -35.35271 | 2026-03-24 03:17:00 | NOAA-21 | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 521aad6b-3f50-35dc-8899-795914c3863e | -10.39178 | -36.98944 | 2026-03-24 03:19:00 | NOAA-21 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 99caf1e8-814c-3985-b7a0-a72fde3ee0d6 | -10.68397 | -37.12304 | 2026-03-24 03:19:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2233202d-e3ca-3ae5-8a71-c4a4f8d1377a | -10.68076 | -37.12405 | 2026-03-24 03:19:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0d71b4be-0683-3142-adee-7301c961422e | -12.24165 | -38.25537 | 2026-03-24 03:19:00 | NOAA-21 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0cbae29-0ad7-3add-b8a2-f3fc63b72b68 | -11.96238 | -37.95287 | 2026-03-24 03:19:00 | NOAA-21 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 20926e48-9454-342d-ac09-1f35691c46f1 | -11.06471 | -38.43923 | 2026-03-24 03:19:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 86ac0b44-79bd-3815-9b1e-98909e4f5291 | -10.68307 | -37.1279 | 2026-03-24 03:19:00 | NOAA-21 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 185df0f4-4b65-3fde-851c-ebad034e1f7b | -20.1481 | -46.6787 | 2026-03-24 03:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 50372ace-2e6c-319f-a67f-10cde7ef73f8 | -20.15522 | -46.69408 | 2026-03-24 03:21:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| c57651d5-bee8-3531-8be2-84dbcf9f73e7 | -21.72142 | -47.2494 | 2026-03-24 03:21:00 | NOAA-21 | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 734b66fb-8cfb-36e2-8ad7-e56c0e5137dc | -23.60521 | -48.25579 | 2026-03-24 03:23:00 | NOAA-21 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1d3fda2f-5293-31d0-a40a-d932dd1165b8 | -6.82027 | -35.35419 | 2026-03-24 03:47:00 | NPP-375D | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 6277afe9-9d63-3634-83b5-f1582b6d3621 | -6.02353 | -35.20951 | 2026-03-24 03:47:00 | NPP-375D | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4365a614-18f2-330f-a743-465dff9209a9 | -13.36565 | -39.9064 | 2026-03-24 03:49:00 | NPP-375D | SANTA INÊS | BAHIA | Brasil | 2927903 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ada4f1e4-00d4-3f3d-bfe8-8f53a83ff49b | -11.96398 | -37.95181 | 2026-03-24 03:49:00 | NPP-375D | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| a309c35f-aff3-3209-a4ab-e0c251850740 | -12.2426 | -38.25379 | 2026-03-24 03:49:00 | NPP-375D | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f1b40d89-c589-351b-b104-aae100e008e1 | -13.36927 | -39.90696 | 2026-03-24 03:49:00 | NPP-375D | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 587860d2-2666-35e1-8b16-bb442d54ff01 | -10.67948 | -37.12569 | 2026-03-24 03:49:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 743e782e-56c6-3bb1-9fb5-9f6e73c04a60 | -10.39425 | -36.98723 | 2026-03-24 03:49:00 | NPP-375D | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 211c0645-23d8-333f-996b-9cef1ac919fc | -10.68283 | -37.12626 | 2026-03-24 03:49:00 | NPP-375D | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1c6709b4-559d-3185-8f70-6bc719f8cc78 | -12.30941 | -38.54807 | 2026-03-24 03:49:00 | NPP-375D | TEODORO SAMPAIO | BAHIA | Brasil | 2931400 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9b74e5e6-06b8-3bae-9638-b6de49b469aa | -11.82178 | -38.26079 | 2026-03-24 03:49:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0e8f1f12-94d1-3001-8b85-2422a4ba0cba | -11.21395 | -38.36737 | 2026-03-24 03:49:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 06560bac-a9fa-3ead-9d08-6c2418c7d830 | -20.67729 | -48.79985 | 2026-03-24 03:51:00 | NPP-375D | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1fb8c272-9b87-32c9-b41b-af782cfbffe1 | -20.1684 | -46.54197 | 2026-03-24 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4603849a-ce77-3222-a0e4-51f95e760331 | -15.67538 | -40.88479 | 2026-03-24 03:51:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c7222f6e-f249-355d-925d-2d660bf4ab2b | -15.67681 | -40.88648 | 2026-03-24 03:51:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b62e920b-65b9-3ad3-9767-f1d3abc0b6a2 | -20.16636 | -46.69738 | 2026-03-24 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0e538abb-3a45-33d4-a224-f341629323b2 | -20.15986 | -46.65555 | 2026-03-24 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f2232db1-da21-3561-abd1-d29cfb09fa04 | -21.11402 | -47.46488 | 2026-03-24 03:51:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9b5bc14c-d285-3e73-8961-c63fa453f59a | -20.17343 | -46.54197 | 2026-03-24 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec60bbcb-182a-33a7-9411-a0e55f33140d | -19.22848 | -44.74842 | 2026-03-24 03:51:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e96c68be-a28e-313d-9842-9651118f8f26 | -19.22763 | -44.75276 | 2026-03-24 03:51:00 | NPP-375D | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccb09d34-53e9-39d3-be48-1479b4900e41 | -20.15874 | -46.66095 | 2026-03-24 03:51:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 17bd61ca-1ede-35cb-97d7-7e859a4a7a0f | -15.67906 | -40.88542 | 2026-03-24 03:51:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1cdffd10-a66b-30bd-9b29-d47ee5c870f4 | -23.60914 | -48.25961 | 2026-03-24 03:53:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6f18597a-cdf2-3806-b943-e3fc0d5f422f | -23.60415 | -48.25843 | 2026-03-24 03:53:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c221cf31-8e2c-39a9-b743-f5d95beedd9d | -21.71816 | -47.24956 | 2026-03-24 03:53:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddac0812-c76f-3df0-8840-51afa582c7c9 | -21.71692 | -47.2555 | 2026-03-24 03:53:00 | NPP-375D | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5253f726-780f-344b-ac04-289b8a75ca5f | -23.60831 | -48.2585 | 2026-03-24 03:53:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 168147fe-6685-32ee-aeca-5f572eb2f176 | -4.69792 | -38.16151 | 2026-03-24 04:08:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2dfc8e31-4735-3ade-aba3-c7e1d379f412 | -4.70009 | -38.16016 | 2026-03-24 04:08:00 | NOAA-20 | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 51c7aa3b-8ec3-39b2-b2f0-0ec6dfa6db1d | -5.94215 | -35.62513 | 2026-03-24 04:08:00 | NOAA-20 | SÃO PEDRO | RIO GRANDE DO NORTE | Brasil | 2412708 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| efffe103-7ae5-38d1-97bd-92a1f0d8746e | -10.68399 | -37.12657 | 2026-03-24 04:10:00 | NOAA-20 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 41efbc1d-84fc-3793-91da-2a26164e5a3a | -5.54161 | -40.57429 | 2026-03-24 04:10:00 | NOAA-20 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 1430496d-7549-34ff-bb0c-715c9680da30 | -10.39022 | -36.98884 | 2026-03-24 04:10:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1672d22a-4d7e-3770-b012-186ffe4bd27e | -10.67984 | -37.12604 | 2026-03-24 04:10:00 | NOAA-20 | DIVINA PASTORA | SERGIPE | Brasil | 2802007 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9f7b36e0-83ec-3191-b0b7-139aaff3eef9 | -11.96133 | -37.95208 | 2026-03-24 04:10:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b91efca2-4295-38fa-b8f3-c62aa3a96c47 | -10.39266 | -36.99 | 2026-03-24 04:10:00 | NOAA-20 | CAPELA | SERGIPE | Brasil | 2801306 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 16801524-fcb6-3977-9ae2-bd76d4d348fc | -11.2142 | -38.36603 | 2026-03-24 04:10:00 | NOAA-20 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0bcbb79-36b0-364c-af9a-76bdc88d472b | -11.96531 | -37.95274 | 2026-03-24 04:10:00 | NOAA-20 | CARDEAL DA SILVA | BAHIA | Brasil | 2907004 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d450aef8-96a8-30c8-9bd4-3d9be704d599 | -11.54139 | -38.25986 | 2026-03-24 04:10:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 55a2c1a6-a09e-364e-9cf1-9418ee7392fb | -12.24216 | -38.25413 | 2026-03-24 04:10:00 | NOAA-20 | ARAÇÁS | BAHIA | Brasil | 2902054 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5ab4c6a7-6dbc-3f49-870a-17f4623f2a25 | -11.5375 | -38.25926 | 2026-03-24 04:10:00 | NOAA-20 | CRISÓPOLIS | BAHIA | Brasil | 2909604 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8fc045c2-8eb0-3deb-ba44-7d18bd328f1e | -11.8207 | -38.26334 | 2026-03-24 04:10:00 | NOAA-20 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 2902398d-87af-39e5-9b65-18e9666c5709 | -17.12392 | -51.21202 | 2026-03-24 04:12:00 | NOAA-20 | MONTIVIDIU | GOIÁS | Brasil | 5213756 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 43deb83f-f836-311a-826a-f28a4daaa67d | -15.67769 | -40.8851 | 2026-03-24 04:12:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35b4ff24-321d-30d8-8050-55770a06691c | -15.67724 | -40.88361 | 2026-03-24 04:12:00 | NOAA-20 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6b00b19f-a902-39d4-be95-a9b3e4f2a85b | -14.04414 | -43.85212 | 2026-03-24 04:12:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1988c5de-edf1-3644-bfea-59cbaa5078aa | -16.84348 | -50.66768 | 2026-03-24 04:12:00 | NOAA-20 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 680a763c-d0c5-3edb-b136-a288b92f3b73 | -16.92373 | -43.59958 | 2026-03-24 04:12:00 | NOAA-20 | GLAUCILÂNDIA | MINAS GERAIS | Brasil | 3127354 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README3.md)
