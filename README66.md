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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8167a52-67da-3d31-835f-1e164373b0ce | -1.20401 | -53.86577 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 48478f58-c4a6-334b-a5eb-830c99ba0335 | -1.67684 | -52.52456 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b85fdad-0148-34ba-8e37-bd8d44395382 | -2.67499 | -46.10101 | 2024-11-30 04:40:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a405035-4f4e-30a3-85eb-2caf1432244d | -2.14948 | -48.49915 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0da4c38-7cf2-3c27-8f63-f1a8f438aad5 | -1.26514 | -54.54992 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 3a8ef953-cc66-3163-b98b-4341bd82927a | -2.43797 | -47.12944 | 2024-11-30 04:40:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c0a2722-79c4-3911-9af8-0ad5a87874f8 | -4.35995 | -43.70203 | 2024-11-30 04:40:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fae9ffe6-345f-3974-8ef1-7c546c6a531d | -3.82192 | -46.55598 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6ab086f2-d76f-379a-89e7-bf2f675383a7 | -2.46824 | -50.3789 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59936faf-132b-3065-bdaf-bb2ef275fad6 | -3.00863 | -53.23475 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 39e118b9-11fa-3d24-b05c-b227be9c8d4a | -3.3602 | -50.51731 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b3f0d7c-3fcd-381a-b098-3b7b6bbd4f0f | -2.79112 | -43.33785 | 2024-11-30 04:40:00 | NOAA-21 | PRIMEIRA CRUZ | MARANHÃO | Brasil | 2109403 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 288aceec-5a07-321d-80e6-dadacaa021f1 | -3.25857 | -53.6396 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 25ba55a3-d095-3ca4-8431-2ab3e33ff2ac | -5.91432 | -43.84215 | 2024-11-30 04:40:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f780363-557b-389c-80cb-e74a42001aed | -1.27059 | -54.55902 | 2024-11-30 04:40:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| c25e2d22-04f8-3e33-badc-e2bdca7cc6de | -2.40193 | -48.23199 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c2fcc61-73a6-3ce7-afff-39cbab0dbd68 | -3.07518 | -50.96411 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 421afb90-f42f-3aca-8038-ef9b5363cc8f | -1.07396 | -53.63327 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 60f4772a-093f-3504-9186-76aa92f3eae4 | -3.07448 | -50.99071 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f57f62b5-e6cb-335b-96e7-e87f77fb9fe6 | -3.6026 | -49.9742 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 64f0df79-3f57-31b7-a46a-710160ea4da8 | -2.03101 | -52.08099 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| b54416c9-32d9-329a-9200-204806c301be | -3.91326 | -49.92302 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3bf74264-b46d-3b01-a9e2-eb04e92f28ee | -2.44525 | -49.30607 | 2024-11-30 04:40:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a66bf5b-7e62-3b2f-b6da-ac5682a02438 | -3.4885 | -53.81036 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| b8e3b721-21d8-3b06-99d1-1bac3404ccf3 | -2.84385 | -46.61315 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b90d816d-8095-3228-a73f-c1eac4912463 | -2.58423 | -47.02847 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49912dbe-bf80-3112-b1a8-ff9feecff72e | -3.39025 | -50.1103 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c223a9a-da27-3a78-aaf4-e7c58fc004b8 | -3.04028 | -48.52224 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73271e0d-a224-3888-8e8e-41bc10aafe05 | -3.02635 | -54.03187 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ee59f5ff-722b-3093-9cfb-724fd317eeca | -1.68614 | -46.77673 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 12804412-2aa8-3004-8d57-9b35d778eb7f | -1.62848 | -52.37006 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f6363c4-644a-310e-a95c-2684c4846921 | -3.24984 | -51.34708 | 2024-11-30 04:40:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6ce8ea64-4871-3908-898d-e1cea5f1d4dc | -1.57914 | -53.84294 | 2024-11-30 04:40:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8ed647dd-a062-3f77-9f0e-e23613ac34dc | -3.72574 | -50.20605 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8358bacf-c198-3dcb-bd23-a4ea41b461ef | -3.28546 | -50.63111 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e72fe1b6-3868-32b7-84f9-99154bf1f412 | -3.27931 | -50.58191 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e14d2c3d-f521-3b37-90b6-24ee9cc26df9 | -2.57458 | -51.8368 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| beca58db-13b3-317e-ac4b-9a1251755b14 | -3.9698 | -49.95323 | 2024-11-30 04:40:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cef6eebd-ecde-33a7-957d-aa7dabe6b18a | -3.94268 | -40.97386 | 2024-11-30 04:40:00 | NOAA-21 | IBIAPINA | CEARÁ | Brasil | 2305308 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1658ec80-60fd-3419-9565-271a3cff2da9 | -2.65196 | -51.7108 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c922c50c-ad19-3477-b241-12a95c2b89f1 | -3.5954 | -49.97666 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1ac2d8a2-181f-394b-8247-65e25df0e0f1 | -1.76022 | -50.8867 | 2024-11-30 04:40:00 | NOAA-21 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54c72ec8-891f-352a-a076-ed2a4eca7d30 | -1.71525 | -52.77341 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5b56925-e5fd-3597-ada4-868c417ab9e9 | -3.59039 | -50.37317 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 295aa5e7-2d2b-33fd-904e-fc3f91e04987 | -3.39478 | -43.12483 | 2024-11-30 04:40:00 | NOAA-21 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 96ec5734-fcbe-3aa0-b60d-5e7c8c32ea1e | -1.53028 | -52.66755 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 39dc10f3-c598-3c3d-adaf-4b9d330f00a5 | -3.2486 | -53.92436 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29344d5c-0af9-3150-b272-ab0cbe7c17cf | -1.44479 | -55.21603 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 27e4ed22-a7e7-3374-8060-596cf132a0cf | -3.94791 | -46.68528 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15986aba-f767-38d2-9361-35631a52e991 | -2.69747 | -52.9174 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be63ffea-946f-3e4a-99c8-c99069ab1afa | -3.43682 | -59.28699 | 2024-11-30 04:40:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5f248eb0-f047-306b-9f53-7d374e81abf0 | -3.59485 | -49.98015 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f85736be-b8f8-31c8-8179-879bed452503 | -1.26462 | -51.75558 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b554e993-e526-30ba-bf6b-cd0aa028aa47 | -3.30532 | -50.24128 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 465076b9-15d9-349e-a607-9e8ae83462c3 | -3.10548 | -49.45562 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e271e663-74f5-32e0-bf8e-8811110773b6 | -2.02736 | -52.08043 | 2024-11-30 04:40:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 804ae7e3-a420-3e03-8053-93d3dba47fb3 | -3.02403 | -54.02055 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd6b7481-f25f-3feb-9879-0eaa050c0912 | -5.49502 | -46.77222 | 2024-11-30 04:40:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76e06575-c1d0-3663-8ee0-d0d7573c0423 | -1.6816 | -46.78352 | 2024-11-30 04:40:00 | NOAA-21 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d3f4434-dd9c-3351-8647-ad6b1a2d17dc | -7.22229 | -39.0527 | 2024-11-30 04:40:00 | NOAA-21 | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| dd6f9bed-feaa-3222-b0a1-78e45a5f3839 | -3.93858 | -46.69986 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 81dbd69c-14ee-3834-8da0-f9fa8ec1af13 | -3.12412 | -50.29343 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8916d255-6320-36cc-9b5d-0292e996ade2 | -6.91689 | -43.53553 | 2024-11-30 04:40:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 322377f0-3001-3a21-ba49-4a93b6f2ccc8 | -3.48373 | -50.25119 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 762021d8-f368-3ae3-bf89-54a2c23b2993 | -2.60069 | -47.03476 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 49c5cdd8-2a7b-3585-827c-207c9a9bee53 | -6.07585 | -48.04351 | 2024-11-30 04:40:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| a6e72bcd-2e0a-34b1-a6c9-cd7329cadd84 | -2.10927 | -48.21099 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b22f4a11-ffa5-36e2-94ad-393b0e2deb68 | -2.43947 | -50.43 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fc4156e-2e81-352e-8393-cf5233ac420d | -3.59932 | -49.9952 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0661ab04-02b3-33e7-b545-66d4e5b75aa7 | -0.82047 | -51.60195 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 462155f2-6414-3c7b-a9fe-59f209daa257 | -1.13736 | -53.39643 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 806edbd6-a67e-37d4-a5b9-cc5abb8a59cf | -3.81153 | -46.68066 | 2024-11-30 04:40:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b551777d-5bbe-31d9-b4e5-4107dca138db | -4.08843 | -47.02872 | 2024-11-30 04:40:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42651831-bda3-3f16-a56a-69f9d14c02c3 | -2.6193 | -46.7994 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ccc4f52-c591-35d7-b608-b083431c4e4c | -3.02646 | -47.80085 | 2024-11-30 04:40:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1961984-77d5-32fd-aacb-27da3914882d | -2.05151 | -48.20917 | 2024-11-30 04:40:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 52bcc4a6-0a29-36f9-838d-e291b0d55446 | -2.87089 | -48.10242 | 2024-11-30 04:40:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aa7e525c-6e09-30c5-aa53-887aa88bb043 | -3.24363 | -45.37823 | 2024-11-30 04:40:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1cd247a2-4c13-3d6f-b4e1-b28e3b07ea49 | -0.96325 | -51.71656 | 2024-11-30 04:40:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1b2ec8fd-6ff1-3a65-b2c9-7d365d44b961 | -3.97521 | -41.52716 | 2024-11-30 04:40:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 93de4200-b66c-3dae-a870-4a57d0cad49f | -2.71635 | -48.65817 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f90d0425-2610-3108-adf7-ff933eb97ca6 | -3.93083 | -47.97929 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c005a02c-747b-3c25-8586-074828b20acc | -3.10678 | -50.36023 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f61df380-02f1-347a-81bb-02918980ec35 | -2.31145 | -49.07307 | 2024-11-30 04:40:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 42a95dc7-5229-359d-b254-976560f464c7 | -4.25614 | -46.37166 | 2024-11-30 04:40:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f295c81c-af04-3ca4-9576-b5a2d34d3785 | -2.78905 | -51.71538 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d1e76cb-78fb-32ad-8d59-882a883d34b3 | -1.36347 | -54.65436 | 2024-11-30 04:40:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e700ebf8-4b0c-3643-a71a-371a40b06528 | -3.09977 | -54.0444 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaa006a1-7ba9-3eea-adc1-a338ee599e82 | -5.12629 | -45.10785 | 2024-11-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 01ded931-dec4-320a-ad90-0f491c5ced05 | -4.86772 | -41.30735 | 2024-11-30 04:40:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a3528799-d8b2-3674-b284-878a730e5681 | -3.74462 | -53.38863 | 2024-11-30 04:40:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c21ce08e-d50b-367f-8a40-fa62cf5a23c1 | -3.23257 | -50.31749 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49d31a58-da1a-3e5f-b7cf-91fee5a5b406 | -4.10441 | -50.98247 | 2024-11-30 04:40:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c0847ed3-e7b0-3425-acec-cec7efff08d7 | -3.14386 | -48.53468 | 2024-11-30 04:40:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b528158-d438-3d18-8eaf-39eb45f7ab88 | -2.97957 | -53.29407 | 2024-11-30 04:40:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487238ae-6bec-32c1-9b5e-6f87987bca75 | -2.62488 | -54.21418 | 2024-11-30 04:40:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b6cff5c-0d73-3973-9eda-369da14acde3 | -4.00378 | -48.29621 | 2024-11-30 04:40:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8ed2df6-8565-33c4-a3ce-36bba0a9e027 | -2.04306 | -51.18399 | 2024-11-30 04:40:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f07cb91c-7604-3ef9-9510-e6bef8bd8a3d | -1.36973 | -52.55487 | 2024-11-30 04:40:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 113af2ca-4b81-3e8e-bebd-4629ea4f5ed3 | -1.29312 | -51.72453 | 2024-11-30 04:40:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README67.md)
