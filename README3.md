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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e3c921-12f6-3fa0-b1b5-956859339e46 | -8.09414 | -43.15131 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| ccb51feb-f396-38b3-828a-2ab603bfa0c8 | -12.20202 | -49.62709 | 2025-06-23 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92b841d6-26a5-387c-954a-9267f44ebb40 | -7.44125 | -45.54426 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a26b701b-ba1e-3088-a91c-d6c5cda723d5 | -7.31769 | -43.21488 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 921a182a-f7d6-36b7-ab1e-e0e2dad29705 | -7.36416 | -43.37112 | 2025-06-23 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f66624f2-decf-3e51-bfc5-96e3fc4ccc68 | -8.71332 | -36.2401 | 2025-06-23 03:55:00 | NOAA-21 | LAJEDO | PERNAMBUCO | Brasil | 2608800 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77316d51-d404-32ca-be10-92afab2b925c | -7.44333 | -45.55902 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| adfdca2a-4221-362a-98a8-c7217cacb331 | -8.06834 | -43.11762 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 66e50f3f-8a81-3de5-a79c-cc5e4ca2a0a8 | -10.15225 | -48.98525 | 2025-06-23 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 629c8ca4-7049-3901-98df-2d2270599337 | -13.02951 | -42.6755 | 2025-06-23 03:55:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a80374e5-15ad-3b84-b9e0-eb45a9b32f4e | -8.06532 | -43.11223 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 2c8d7a5c-06df-3c4e-8d42-e87d49c17d9d | -7.46765 | -45.55328 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 578db16f-48b9-37b2-88fc-ffadcc66c0ea | -7.44705 | -45.56446 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 39710455-20fa-3408-b8f2-5fb4197f38e0 | -7.36498 | -43.36609 | 2025-06-23 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c02c4ee-2dbb-31db-aef7-bfeccb46ac08 | -7.36444 | -43.36825 | 2025-06-23 03:55:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8b88a297-62b0-3016-aa3b-265049190bb5 | -8.40199 | -47.14255 | 2025-06-23 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d191c11f-d54c-3506-8ff6-1334593a0253 | -12.89575 | -43.79132 | 2025-06-23 03:55:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fab5348-6fe1-3fc4-9d1b-b9ea813dc7a5 | -9.8258 | -39.4948 | 2025-06-23 03:55:00 | NOAA-21 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cb534c4d-221a-346e-a4f6-f5ba62bb15f5 | -7.45241 | -45.56047 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 51d542b3-0825-32c0-aa8f-f5aabceb35e6 | -8.09797 | -43.15194 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c86840e2-cda2-37a2-a5c6-5fedea2cab70 | -7.35744 | -47.75098 | 2025-06-23 03:55:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02bdd965-57dd-340a-968d-beb0562f2303 | -9.41686 | -48.417 | 2025-06-23 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e133dcac-6dfc-3b2e-9ee7-caf10121fc72 | -8.09877 | -43.14716 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 5bf57d8a-b9f3-345c-9038-58381bfdf25f | -11.10149 | -46.66603 | 2025-06-23 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f33c4145-661e-308b-90df-49f527ce039b | -8.48438 | -47.51355 | 2025-06-23 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6382f215-6642-376e-a3c2-29b846fba051 | -7.44951 | -45.55033 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0a01185a-55a5-3564-b59a-85ad4e5eb21e | -7.46231 | -45.55719 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33f3366d-5ba9-3df3-9e32-1f57dfc35c39 | -11.58435 | -44.65834 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72879425-10cd-30d8-b3ae-2cc55ebac3aa | -7.32241 | -43.21059 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6623eb6a-f628-3d89-a5a3-cf23f9f9a112 | -12.19655 | -49.626 | 2025-06-23 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 25292f60-aeaa-318a-b213-5d266e3f94c9 | -11.10236 | -46.66116 | 2025-06-23 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e6c014f4-ba4d-3c9c-a768-d75aa284434d | -6.60545 | -43.89759 | 2025-06-23 03:55:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 76aea821-df6d-3670-b544-8c044c355acc | -7.31462 | -43.20934 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9c18908e-ecfb-3a31-a1e9-e75c061ac806 | -8.71743 | -48.01209 | 2025-06-23 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f0c6ac3-d859-376b-a010-552f99883584 | -8.38534 | -47.44201 | 2025-06-23 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4dcfcb4f-dc8d-3dcd-af5d-5ab374c0c978 | -7.87509 | -47.88335 | 2025-06-23 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0ad5022d-78a4-3c05-b431-ecc5829c5cfe | -11.93115 | -44.81365 | 2025-06-23 03:55:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e8647d1-da1c-3b16-97c1-55e3738ef097 | -8.48629 | -47.51275 | 2025-06-23 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7c2d8772-4207-3fc4-9792-dde67d87033a | -13.026 | -42.67488 | 2025-06-23 03:55:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ee7c132b-a9ef-3466-ab49-bb9f8eac440c | -11.51042 | -48.95522 | 2025-06-23 03:55:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dbc58d75-91f9-3536-a961-de01813ce5f5 | -10.14614 | -48.98786 | 2025-06-23 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f74fe896-490d-3718-b1ee-8b9b99a182ef | -9.08587 | -49.62694 | 2025-06-23 03:55:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 30b44d56-8e7e-330c-97a0-49733d95b60a | -8.06069 | -43.11635 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 69bbc382-2b95-38c3-947e-8f09f01bf3e6 | -8.06451 | -43.11698 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 6bd8d786-721a-3a2d-849c-8f8224ecafc1 | -9.42155 | -48.42132 | 2025-06-23 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7bfe3719-de3a-3dda-ba67-a40e7e1b2051 | -7.44416 | -45.55428 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 38198bfc-23be-3adb-b236-02f7351e7a2c | -8.39704 | -47.14157 | 2025-06-23 03:55:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ea341460-a593-3b55-a0f5-9732b1582447 | -12.20273 | -49.62689 | 2025-06-23 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 436b91e3-6da0-3a92-8a0b-07ba718f3ed6 | -9.35015 | -40.48074 | 2025-06-23 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| a383cb70-c6c8-35c3-abdd-b6e2e83cafe8 | -10.9877 | -47.40672 | 2025-06-23 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5ac4d55-cf47-39aa-a789-ac031faff4d9 | -7.45033 | -45.5456 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d35ff864-bae2-3735-a45c-0b9fd1eb15ee | -7.4516 | -45.56512 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| fdbb541c-5a59-33b7-8bf5-f1a72b31200c | -10.69597 | -37.04969 | 2025-06-23 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f3363bc9-ba62-39ca-83a6-255df9341b3d | -8.07075 | -43.10339 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| bf5591a3-280a-37df-a7f7-79ea74d1085a | -8.06693 | -43.10275 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 8d7fd264-2c83-37b7-ab75-d7aa3b9823db | -7.31851 | -43.20997 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| da8692a2-edc9-3fb0-b692-ec1797369351 | -7.87441 | -47.88421 | 2025-06-23 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cedd4507-525c-3724-9644-3a8f9ecb35f9 | -7.46683 | -45.558 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ceceab7e-ebba-3726-84fe-ef45f17cfb60 | -7.44786 | -45.55976 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1896ee7e-9361-3dd7-89d8-5956e6b8e622 | -10.98608 | -47.40831 | 2025-06-23 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f6b0efb-0f1f-37ef-8fd8-79ce9f982ff7 | -6.85631 | -43.15157 | 2025-06-23 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cf885fce-48f5-342d-8ab7-44ef21cdffb4 | -10.07035 | -49.65938 | 2025-06-23 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ffaa2dee-6c76-3ad2-96c4-3a33f7b9b169 | -12.43938 | -44.75134 | 2025-06-23 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e8946ede-db55-3c1e-a963-aa0564a18628 | -13.0269 | -42.674 | 2025-06-23 03:55:00 | NOAA-21 | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| a349ecd2-9746-3ef2-9b84-2d7d9432df2f | -9.41748 | -48.41371 | 2025-06-23 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8e7fce30-f17e-3376-88bb-e481c3bda328 | -7.3138 | -43.21428 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| cbc5bf91-6b7a-3ddf-9939-5d4f60f96368 | -9.42217 | -48.41801 | 2025-06-23 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08e51b50-2bf6-393b-a1ea-232d682bd306 | -8.40853 | -44.60788 | 2025-06-23 03:55:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f982969a-a4f0-3f41-8038-19b1c60bdce6 | -9.42279 | -48.41469 | 2025-06-23 03:55:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 676a89ae-de3b-345a-8058-dfad21ee358a | -7.31297 | -43.21921 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 148ec441-aa93-3bdd-83ec-953087bfb147 | -7.30907 | -43.2186 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 947f64da-49cb-3f4b-acf9-c454b3024198 | -8.07454 | -34.97855 | 2025-06-23 03:55:00 | NOAA-21 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5091d89d-853a-3a53-b480-53cbfb27e28d | -11.57637 | -44.65693 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d94de99c-29de-3c74-aab9-7957b6175a70 | -13.76386 | -42.97973 | 2025-06-23 03:55:00 | NOAA-21 | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2ecac2bc-aa8e-32d9-b5dc-3c296d441e36 | -11.58157 | -44.65059 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97e6aa0e-d9b0-3d53-8154-368bda0048e0 | -12.19726 | -49.62582 | 2025-06-23 03:55:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a779ee4-a427-3c0b-b2ca-d117030c03ce | -11.31905 | -47.1847 | 2025-06-23 03:55:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb561159-7c51-3a0d-81da-d9ca13fc8e42 | -7.44869 | -45.55504 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c0d421b9-5e98-3a42-9006-5f4075b3d4f9 | -7.45322 | -45.5558 | 2025-06-23 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bc2f034e-a946-34cc-b5e1-49c7e9e70399 | -8.06612 | -43.10748 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 8aacaf24-4846-3e28-a8a6-7fc68b683c93 | -8.11488 | -43.14492 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 4ab6d33c-ff43-3332-abf8-c0009435b688 | -7.31073 | -43.20871 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 4ccf9504-6330-3ab5-af20-df3960134768 | -7.45809 | -45.52784 | 2025-06-23 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dde30ab7-718b-3c57-8f65-826a5309bc76 | -6.85726 | -43.1497 | 2025-06-23 03:55:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 03573ad5-a188-31e4-8c4e-04347df6b444 | -8.48549 | -47.50755 | 2025-06-23 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6a72e80c-2ce2-30b4-8704-a763819ce8ea | -10.06389 | -49.66229 | 2025-06-23 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2eccf5c6-0e42-3872-bbd2-1396a1fd6b3f | -10.15328 | -48.98704 | 2025-06-23 03:55:00 | NOAA-21 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 81111b91-907c-3468-a2e0-3c579b132e49 | -8.48494 | -47.51052 | 2025-06-23 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f535be02-c1c6-3d9c-a614-a83692335477 | -10.0582 | -49.66122 | 2025-06-23 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b9681c94-4821-3a1f-994d-c2465b5cac57 | -9.14713 | -48.97399 | 2025-06-23 03:55:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a8d6ccb2-3c7b-31f1-ba29-a8b568724a4d | -11.58036 | -44.65763 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9da1202c-ccd5-3d54-86c7-418ab9dd1eeb | -12.43581 | -43.77415 | 2025-06-23 03:55:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 841f0a0d-ccf7-3065-9047-ffc2a3af8378 | -12.2519 | -46.6861 | 2025-06-23 03:55:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| aa343759-6a92-3e20-bca7-fa729dcae2b3 | -13.66566 | -43.66354 | 2025-06-23 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9565c259-a6a7-3062-85cb-f7b75f8aa9e4 | -7.3099 | -43.21366 | 2025-06-23 03:55:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| 2c10a082-7006-3320-a1b7-be78fde8c2ba | -11.10698 | -46.66184 | 2025-06-23 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 73874212-7b8f-3989-a91a-b252a73e7055 | -8.0637 | -43.12174 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 38b3704e-af4d-3c39-a858-1b2c9f97ec4b | -8.48682 | -47.50975 | 2025-06-23 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 50f7b5ae-09a7-34df-8814-f146dd0ba590 | -11.58097 | -44.65411 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4b68eec-f0e0-38bd-8cff-4688258472f7 | -8.71691 | -48.0146 | 2025-06-23 03:55:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README4.md)
