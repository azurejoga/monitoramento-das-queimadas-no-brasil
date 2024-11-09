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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0313a4af-07ec-3bc0-a730-0ad53f3653b8 | -3.11783 | -50.14804 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3e9096ab-e0a3-34b6-b89e-a3492a0a6e49 | -3.1562 | -54.48057 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a8517dda-486e-3f11-ac3e-3df10525003a | -3.3876 | -52.3555 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04873bfe-eb05-323e-ae05-d7b461f08228 | -1.36419 | -49.35206 | 2024-11-09 04:55:00 | NPP-375D | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd05d49-9cd7-301c-bbc9-f9d14ef9a1b9 | -4.25078 | -47.57667 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| a7a993e7-02ae-35f1-b309-10f347247a71 | -2.40311 | -48.49299 | 2024-11-09 04:55:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b53bf84e-4a4f-34bf-9804-404ab7bc06ee | -2.91955 | -54.19493 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1ce440cb-e4bc-3f73-96a4-bc737f255fc6 | -4.24497 | -48.02321 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5771adde-05bd-3602-8354-3522d7a0aebd | -2.87365 | -51.30345 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 44207919-0a9a-3392-91d5-d9f05c6788be | -2.61574 | -51.74492 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 056b43fc-c7b7-3d5d-bf9f-3bf0b3f1b987 | -3.53227 | -50.87249 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae755ca7-49ff-30f1-a1c3-889b515200bb | -3.07803 | -50.57306 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1cb9eb25-be23-33e8-b000-a90b46743353 | -4.70774 | -46.38065 | 2024-11-09 04:55:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c9b6a76-5538-31a2-aa25-1b22b64ebbe2 | -1.15656 | -52.00747 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd42235a-c5bf-3e0b-a55a-80bce9497b91 | -3.25069 | -53.40511 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f142cd8-9998-3ea5-8188-b9f8b81434da | -2.30585 | -53.81641 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cb4cf4e7-f114-37f4-88c8-61efec111baf | -3.06257 | -53.90994 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 491481c1-cdc7-3a09-9bb4-4e99beadc387 | -3.04047 | -48.04068 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 17538055-e91d-3e1b-a1ce-f58401c02f9f | -2.38557 | -53.74352 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c4e2ca4c-ba39-3a50-a635-30bc35a983e2 | -3.25078 | -51.12837 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25072627-9dff-3687-9fe4-73c6810beede | -2.69746 | -51.69429 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c281a201-6470-3e44-9ee9-b1b64c2fc348 | -1.05814 | -51.74744 | 2024-11-09 04:55:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ab8aeba4-d6f3-3315-802f-e4a61b83dc54 | -2.5437 | -58.06621 | 2024-11-09 04:55:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fa5271a4-4b28-3392-83f7-1f09d2b9425b | -1.2192 | -51.77187 | 2024-11-09 04:55:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1f1aa113-05f9-3374-8ad4-520b805ce5fa | -2.8661 | -49.2243 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d71168f-7abd-39dd-ba35-2913b533f3bf | -3.12211 | -50.14443 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9c9f472b-6fc8-30b0-8187-ef672acbb6d6 | -3.28018 | -53.67112 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14fa5fae-1c1e-3e87-8a5d-db7543c9c3b7 | -3.22068 | -50.20453 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c3379d2c-a08c-32de-9f3e-68eee77314c9 | -4.22241 | -48.60832 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 47227939-a1f1-32c7-ac55-c4aed59de9cc | -3.5498 | -43.57273 | 2024-11-09 04:55:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ecbccde2-7c89-3467-96a2-5eae13360cc4 | -1.56022 | -52.27346 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c24aa4d8-920d-3b05-b2a2-93a6c94c8c6d | -3.89844 | -50.30315 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51e9a095-0b85-3682-9954-aa7f1d7023f9 | -3.97531 | -48.4052 | 2024-11-09 04:55:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 71a44c47-5533-3158-a2b2-b6374fbe26f9 | -2.18792 | -47.95134 | 2024-11-09 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72dd531d-e844-3660-8acd-f044ffd292f7 | -2.98225 | -50.30186 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 18ff5511-0c45-31b1-b6f3-56dd93b19e4c | -3.09697 | -54.26908 | 2024-11-09 04:55:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3a723b8-2a12-35c6-b20b-8d89cf9feef9 | -3.03963 | -50.41871 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61ca9820-3212-34dd-bbce-d7917808284e | -2.31092 | -53.87063 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f0ce1447-3aeb-36a8-9fe1-85da0dbd337e | -3.23937 | -50.27563 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 34ca04ab-fada-31c3-ad50-7c03e394acf4 | -0.38309 | -51.44012 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b3cdb35-5a9a-3b52-8090-ab967bc20924 | -1.18929 | -53.66647 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df22e777-077a-316c-b315-a516f2632845 | -5.8383 | -46.23835 | 2024-11-09 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7958b95f-224a-333b-b621-597e90caddf3 | -2.57735 | -53.98748 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d31f330-c2c4-3fff-acf0-557ae0679322 | -4.2321 | -47.55299 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99d54258-c51f-369d-8a5d-ef3732aab727 | -3.79755 | -49.93959 | 2024-11-09 04:55:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d33c2ff5-5c69-3dbb-aeba-01d5a298065d | -2.21534 | -53.72407 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ed10ed68-93aa-3a96-b684-07588f1035e7 | -3.26595 | -46.31083 | 2024-11-09 04:55:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5917574-bd0e-37d6-8178-ab0c41f98e58 | -2.58069 | -53.988 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2f1be122-243f-308f-be5e-8e3b1b18209c | -2.96462 | -54.16975 | 2024-11-09 04:55:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d3286b0d-d2e3-36d9-842d-53d7980c67c2 | -2.7677 | -54.04553 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1c0360bc-a02f-3008-9e19-d0ca7ff4556f | -3.12147 | -50.1486 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 1311b69c-3bfc-3bf7-89b9-0e618bca7eca | -0.22059 | -51.62906 | 2024-11-09 04:55:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98181a35-6b81-300c-a09c-7d87f1e692a9 | -3.34627 | -50.26082 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e84d177c-ff19-366b-955a-64ffc3aa8227 | -2.18665 | -53.63095 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abe7ea68-ff14-3892-91ca-678ff4af64ba | -1.27093 | -52.17864 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ab42df0-94fa-3f25-8ba7-9654b835c1b5 | -2.46274 | -47.8418 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eea73536-d3cb-35ab-8efb-6d283c4a3730 | -3.30583 | -50.08701 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c2cb30e-b6e4-3aa4-befe-b919296570b3 | -3.62734 | -54.10902 | 2024-11-09 04:55:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8b5d310-55c5-3c85-8429-5b3c476f32f7 | -2.83992 | -51.81236 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63722c38-0994-372f-ad49-0299399da8d2 | -3.91504 | -47.95678 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a878831-fa13-33f1-b56b-9b62afa4b0fc | -2.43043 | -50.49551 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7369d800-457c-30f7-b682-4ac9e429cf3a | -4.2538 | -48.53748 | 2024-11-09 04:55:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 22cdbbf3-5827-351f-b2ec-7acfaad22b71 | -2.14395 | -50.80869 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3ba2f802-661d-3f09-8d59-92b25c767ec6 | -3.97432 | -46.16914 | 2024-11-09 04:55:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b5daeee3-07cb-3d76-b356-86c6f9a489cc | -3.88745 | -52.3892 | 2024-11-09 04:55:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a8713861-5bf9-3d4b-b277-f570e6a66181 | -2.67994 | -51.8282 | 2024-11-09 04:55:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 174c4fe7-19c8-3d8a-870e-c8d2a2d85db9 | -1.52133 | -51.31134 | 2024-11-09 04:55:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aaabecea-d674-3725-8304-59bfabf90e98 | -2.61847 | -54.02217 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 03edda6b-fdff-32a6-8c6e-bda527d17d41 | -2.40773 | -48.87703 | 2024-11-09 04:55:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9874cd0-4832-309b-b46b-382e89601d6f | -3.17334 | -51.30609 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 62c1b2bd-e419-3f00-8829-f2e5b233e154 | -2.21818 | -50.56211 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| faf86a7a-32c9-3f95-bc38-f4443f7de185 | -2.10033 | -46.20727 | 2024-11-09 04:55:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5400147-155c-3ae9-a7a5-69cc4d3eb16e | -3.06904 | -45.40106 | 2024-11-09 04:55:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1e2c6b92-79ca-3453-ab79-b7b7d777c187 | -4.60601 | -45.97998 | 2024-11-09 04:55:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6725a8e3-f309-3464-878d-309d3902e63e | -0.9128 | -52.56303 | 2024-11-09 04:55:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9335688b-61ba-3e6d-a3f3-c6fe3a8996db | -3.89364 | -50.23779 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9b0580ef-4c66-3f89-82f5-878f19381b29 | -3.30647 | -50.08278 | 2024-11-09 04:55:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 55642277-d917-3f98-b3b7-3900e4db6de2 | -3.1878 | -50.5844 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3eb80987-1294-3579-a750-af8e2113eef1 | -4.39586 | -50.97334 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ba04830-88ad-36b7-b3f5-9fa7604a8831 | -3.24514 | -53.39718 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0aafefd-8631-305c-8f59-465ef05dd8b7 | -2.18703 | -48.33551 | 2024-11-09 04:55:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6bb4700-4c80-3217-a596-a8be6663d999 | -4.05513 | -50.3504 | 2024-11-09 04:55:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88c4bbe0-8af5-3e8c-800a-34f732d244ba | -3.35794 | -53.38967 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e166e9ff-e225-3ef7-9643-08ccb4940e63 | -3.59132 | -47.34145 | 2024-11-09 04:55:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| c03b6ba1-031b-32ed-a042-ce1f7e5bf48b | -1.85468 | -54.47502 | 2024-11-09 04:55:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcfbcbd7-4a53-30db-8dba-76b3a6dfc4c6 | -3.03326 | -51.53226 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c3fb2a3a-8831-3a7d-a739-86170432eb9a | -2.57178 | -53.97947 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a66e42a-1df5-3959-84c0-e4f1fd3ab0ad | -2.46015 | -50.39796 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48526578-5d34-30d6-9706-06bbc9dad663 | -2.36455 | -46.86336 | 2024-11-09 04:55:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b2fac08-edf8-3a0e-a148-eca138eee72a | -3.01218 | -51.04274 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e424a424-802b-3874-83ed-dec71e36fb14 | -3.58663 | -51.20073 | 2024-11-09 04:55:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e7ff1e9-c66f-3a5a-8e3b-a3e220070d15 | -2.9871 | -50.29424 | 2024-11-09 04:55:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e4a19a5-bcea-39fe-b055-e5009fa78924 | -2.4277 | -54.01009 | 2024-11-09 04:55:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fdec1dea-0bbe-3546-8a90-a012e9248505 | -3.05696 | -48.04317 | 2024-11-09 04:55:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc6b6623-49e0-3014-bbc6-9e518bf38443 | -1.72432 | -52.46255 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27661782-b7bb-367e-8f21-cf2a6f8d939d | -1.97306 | -53.13772 | 2024-11-09 04:55:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38f491ce-16af-3c99-b3ae-4ca9690c4843 | -3.9603 | -48.17124 | 2024-11-09 04:55:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| bdb2af6c-91f1-3ee2-9a48-c06c509ab895 | -5.36202 | -44.14281 | 2024-11-09 04:55:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3090db4-5f95-3a07-a79b-ab014abdd2f6 | -3.20243 | -53.41156 | 2024-11-09 04:55:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f23b8c2-e08e-32c8-a46c-518bbf52e888 | -2.10666 | -47.9133 | 2024-11-09 04:55:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README91.md)
