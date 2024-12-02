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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b887c698-f47c-38ff-bbd7-c254ab827728 | -1.1157 | -53.74618 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f8237ac2-36c3-3652-ad0d-1f2853dd9b9c | -4.48796 | -46.05836 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ec44d89-25eb-3037-80e3-b7c33e220dd9 | -3.7497 | -52.267 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91bbca53-b04a-390b-b132-4bdfe75068c6 | -3.10211 | -53.75029 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b351979d-0a15-35c5-9eb3-a373f40b2b9c | -2.76603 | -54.12164 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d3a7241-81b8-3184-8f68-6cc7b21973d1 | -2.85245 | -54.19435 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8b9eb359-51e6-3cbd-8051-8ee1ba65c9bc | -3.10579 | -54.03593 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f91279b3-40fd-35d7-9839-7344051ddc24 | -1.37106 | -51.40746 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c27096ff-193b-3686-9974-1a943da694de | -3.1829 | -51.16199 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c51caafd-8fc4-3a50-bfd4-666fdf6f40a7 | -2.34143 | -53.92407 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7afe4047-378b-3f73-848b-9517d4ad0674 | -3.28279 | -50.62965 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa46bf4d-cb45-33aa-883b-055b3135a21a | -3.12398 | -45.98685 | 2024-12-02 04:48:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d6da4f7-c352-3599-8154-4f61a1553294 | -2.89613 | -53.9654 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| da05ea34-0634-36d8-8baf-edbdd7501940 | -2.7853 | -54.11282 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69462464-cef7-34cf-89f5-c7efd51949d3 | -3.11711 | -53.98711 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 367de253-8c49-34af-a983-a8ba8735df25 | -3.67901 | -50.24282 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 29adbc59-8501-3501-8c94-9f7f569dc045 | -1.52728 | -55.71415 | 2024-12-02 04:48:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 050971f4-0401-3530-a5c4-d8872a6fb17e | 1.94454 | -55.60558 | 2024-12-02 04:48:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87fa2eb7-2d5c-3415-b8bb-6f6f70d043d9 | -1.57511 | -52.26982 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aefc3202-01e2-3529-801b-f879b070bf96 | -3.24972 | -50.75449 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 054e4b34-559d-3a2f-8d8d-1401ecba2350 | -1.70485 | -52.43637 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9f0f142-76a9-3b67-925a-556bcf9cbe3b | -3.5405 | -51.02525 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0a9b752-6715-39fa-80f6-089ed390a010 | -1.73888 | -52.77796 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a19a1628-1e67-3844-9969-ffa4baeb80e1 | -2.83084 | -54.08413 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a49b630-2ba0-3e52-9888-dce293e700c6 | -3.75768 | -52.66926 | 2024-12-02 04:48:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 28728357-cc03-3abb-aec1-95439a53af00 | 0.64938 | -59.65972 | 2024-12-02 04:48:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22b28557-0afc-310e-b4a8-ad24074a621b | -3.77662 | -52.03147 | 2024-12-02 04:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f57ab6a0-7dd1-3b33-a0be-924785605775 | -2.55263 | -53.4135 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 274aea0f-4f08-3792-be6f-64d1f6c6cea6 | -3.77956 | -50.04447 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c2e2f73c-6cd4-3776-9f72-7c3f6bcd8562 | -1.98843 | -51.52192 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a506d526-0b48-3bba-a891-84433a0bc5a1 | -3.6423 | -51.11239 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c9fe0f6-9d90-3aae-8d83-de14d82e8c91 | -3.29361 | -53.67023 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df71d990-96c2-3e5f-b347-8fe7bd98eeba | -1.74699 | -46.21957 | 2024-12-02 04:48:00 | NOAA-20 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79bb2d14-4160-3bd4-a25f-444cab43b653 | -0.20182 | -51.54102 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef3fc8df-c661-36ae-8d64-62639de07699 | -1.01525 | -51.72472 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac687138-d1ee-3a46-94be-af4b769c9b27 | -2.25594 | -53.62489 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 49c81329-4184-3efd-8536-c4550096177d | -1.26055 | -51.63641 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e18a8572-b55f-33c9-a915-965e570760a0 | -1.70605 | -52.64552 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a53d0984-8008-3f79-8c68-cebee9b151e0 | -3.11651 | -53.9909 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1325687b-f663-3081-b46f-cde6d632bc1f | -2.95812 | -49.58287 | 2024-12-02 04:48:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1e9f339-12a9-33cc-8b54-628f88fc46e0 | -2.45979 | -53.70966 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b40a64d5-e663-3e04-85d3-2fd4a335c8f7 | -4.06459 | -51.06408 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 921dbe6d-5ddb-31d6-8137-2dd22f30b4c3 | -2.45442 | -53.80917 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f8f5ea3-0d93-3d93-9684-1d65a93157d2 | -2.01983 | -53.3016 | 2024-12-02 04:48:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eabccfdd-c98a-3277-ba4e-dcc824578e71 | -3.83046 | -46.55005 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af5f7c21-1798-3f11-9fb8-8bd60d42ca9f | -1.93094 | -53.44262 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1c77dfea-d558-3b19-b749-99438e7a7253 | -2.30844 | -53.89613 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31256a47-4b90-3112-a061-2dfa33ce3d78 | -4.32536 | -45.92143 | 2024-12-02 04:48:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbfc043b-0636-3e1d-a808-3fb3b890349d | -1.07343 | -53.39091 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0501c4d7-2233-3721-863c-90273f168cfa | -1.27751 | -54.55605 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f457063-4379-3ffa-8105-dcb594c52a4b | -3.95396 | -46.50315 | 2024-12-02 04:48:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a41655c-a6d0-3d33-b70e-9868c893e198 | -2.73651 | -54.10508 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e35e2a1-9cf5-32a1-b273-dbed79049281 | -1.93436 | -53.44315 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e05d3d64-ebee-31e4-885c-9591d918951f | -3.26149 | -54.11039 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c991f68-87df-3aa3-89ff-dce4dcd507de | -1.4981 | -52.32568 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 49ddfa29-7ad9-3533-b489-8c58ebbf2355 | -1.2486 | -54.55145 | 2024-12-02 04:48:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d50c4dfc-6b12-3654-9d8f-8b346f0f480d | -3.16302 | -51.11626 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1ca62c9-eac6-3607-accb-227239b173ef | -2.06673 | -51.19632 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8a9d4e08-dc47-34fd-b201-d80fd0a2ea41 | -2.36797 | -46.0721 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d8536701-5663-31da-8002-c05a61c1c42b | -2.86479 | -53.98381 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 590e5cf7-08b1-3fa3-b11b-9b6758a0bde9 | -3.33976 | -53.37878 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f1903e73-11ef-309c-84d3-3baf961a39a4 | -1.49754 | -52.32917 | 2024-12-02 04:48:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f3750d7-37b2-3658-9483-db2ce57df4fb | -3.65898 | -50.43925 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f6e7bd3-6412-37c6-865e-ccf24286ac04 | -3.8487 | -51.24793 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 80a36b51-d658-3d24-8b49-2d031bb169c2 | -3.67078 | -53.83416 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05700df2-8642-330a-92e2-92b4a8fe45bd | -2.76254 | -54.12109 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 059a0083-01d9-35e3-8f59-942aa1ba9351 | -2.0458 | -51.20012 | 2024-12-02 04:48:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 215332e2-5f78-3b72-a7bb-9a6d57cfc2a4 | -2.60825 | -45.25301 | 2024-12-02 04:48:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bef90fbd-aab3-307c-ba67-5bb55d222d30 | -3.17571 | -53.64076 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed311063-71a0-3dec-843b-37aa67d8eabc | -3.09927 | -53.7468 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fe68e0d-bcdd-36d5-914f-91ba255455cd | -2.8388 | -54.10113 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c798a85-f910-336a-94fb-ea181980ec2f | -2.45514 | -53.71666 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 227871b5-8159-356e-b93d-618191488f04 | 2.42726 | -60.65268 | 2024-12-02 04:48:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ad85c2e5-1ec5-3655-8a46-054f851e28be | -2.66112 | -46.12769 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4531d8ef-42a0-3b68-b85e-26a7e59c313d | -3.99573 | -51.04617 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a7b65617-29a4-3c96-8ee7-414712447dfb | -2.63815 | -54.19778 | 2024-12-02 04:48:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4895dbe8-3b5e-31a2-abea-665d4bc3fff2 | -3.0588 | -53.29109 | 2024-12-02 04:48:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9e46884-808b-397d-afd4-cb9e000285a7 | -3.71698 | -51.07042 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d41827e-481c-3797-8401-76ec54a88b0d | -2.97869 | -53.88488 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b8708e2-94bd-3f2d-8238-b987b5a7710e | -2.87194 | -54.02787 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4b716c42-407f-37e6-b0cc-f08596f04a6b | -1.36673 | -53.64388 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c73f06a9-5d46-3669-8354-bbb617e965a2 | -2.91286 | -45.35084 | 2024-12-02 04:48:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3d49d55-15bd-3c56-90da-e7882f302e8c | -2.10974 | -50.34036 | 2024-12-02 04:48:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e1878876-b6d1-3584-a6c9-c51a183b29f5 | -2.67565 | -46.61914 | 2024-12-02 04:48:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fee34fcd-4d70-3916-b753-b272ea49cac7 | -3.39333 | -50.2293 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fe24f4d-806a-3bc3-b55b-60de3f6daa7d | -0.62864 | -51.69997 | 2024-12-02 04:48:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d361409-1b51-3090-8428-fb68cc8cd40a | -2.56421 | -53.95712 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b5d79a0-0d58-3578-9e05-f2d13c443f67 | -1.4949 | -51.9378 | 2024-12-02 04:48:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89db8b39-e049-3a49-bfdf-5d2e5e3abc00 | -3.54328 | -51.02925 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6e1977a-0707-37f1-8cd9-5cdbf3992efe | -1.21516 | -52.09589 | 2024-12-02 04:48:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50c215d9-dd23-30f3-bb5f-d01f04f5f1e6 | -4.0226 | -49.94386 | 2024-12-02 04:48:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 24fe4540-a7c8-3395-99d9-7314af177ac9 | -4.08258 | -50.03312 | 2024-12-02 04:48:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a77349a-18a0-3342-993a-2b86f77980b5 | -2.80381 | -54.04095 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b765f4a-c3be-3947-855c-5bc203f822eb | -3.69671 | -47.1224 | 2024-12-02 04:48:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4d21f456-bb34-332d-9070-845e345f2334 | -2.83056 | -48.47707 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1dacaa18-e9f9-3cf0-bbbc-4dee9ebc3559 | -3.25915 | -53.62323 | 2024-12-02 04:48:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.7 |
| c2219edf-01fa-3577-a1cf-9ea83c695722 | -2.44607 | -48.45196 | 2024-12-02 04:48:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 219bb4ca-c16f-3a2c-836e-05ce22b7a824 | -1.49789 | -54.95675 | 2024-12-02 04:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbeb20b4-b9c4-346f-b49a-d28ebf4c746f | -2.84189 | -54.08196 | 2024-12-02 04:48:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8361f86b-eb27-3e62-8fe0-35053e18ad45 | -4.10383 | -50.98335 | 2024-12-02 04:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README62.md)
