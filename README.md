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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6426338f-925d-3573-b582-75278345436f | -9.7553 | -36.3983 | 2026-01-13 00:00:00 | GOES-19 | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 122.1 |
| 1de06f47-9d13-3ebd-812a-b1b71cda3c55 | -5.118 | -43.2198 | 2026-01-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 138.6 |
| bf31eb33-22b6-3846-bc1f-61ee08c9066c | -3.2905 | -42.5507 | 2026-01-13 00:00:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| 05213914-873c-3818-86ce-30237c22d0ee | -4.4268 | -43.1007 | 2026-01-13 00:00:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 67.0 |
| e96936de-d8a4-345f-b62e-541506c3b516 | -5.0992 | -43.2211 | 2026-01-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 312.8 |
| cac630e6-d87c-3bb3-b719-db0b0b1d1837 | -5.099 | -43.2444 | 2026-01-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 147.6 |
| c81845d5-059a-3575-8d8c-a7678eb0f688 | -5.1126 | -39.4573 | 2026-01-13 00:00:00 | GOES-19 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 74.0 |
| c8f76f82-2ca7-3637-91e5-7848e803327b | -5.1178 | -43.2431 | 2026-01-13 00:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 8c295483-ac55-31f5-b3ad-79f04e5a50ed | -5.099 | -43.2444 | 2026-01-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 205.5 |
| b3709e9e-220b-38f9-ba71-f30ab0aae3a4 | -5.0992 | -43.2211 | 2026-01-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 412.0 |
| 5375811a-e3f3-333f-98f6-0a2ad4f8ad23 | -3.2905 | -42.5507 | 2026-01-13 00:10:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 5c3268c0-81d2-3fbc-a968-98fb6a473232 | -10.725 | -37.053 | 2026-01-13 00:10:00 | GOES-19 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 77.2 |
| d08ed2de-0d8d-3a50-bf2d-89afe7d95189 | -5.118 | -43.2198 | 2026-01-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 220.9 |
| 65c0ee23-1d4a-3ceb-bf17-700832922bfb | -5.1178 | -43.2431 | 2026-01-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 969062ab-05b0-3ff7-b309-7969f821f04b | -5.0805 | -43.2224 | 2026-01-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 113.2 |
| eb513394-3ab4-3bed-99d8-36be137cadb4 | -5.0803 | -43.2457 | 2026-01-13 00:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1e25fa3a-30a9-3e24-bb70-cc9fea9f6712 | -5.1178 | -43.2431 | 2026-01-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| ec5b35fc-2322-313b-aa6e-57e62d4b6474 | -5.0805 | -43.2224 | 2026-01-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 102.8 |
| c4702caa-005f-3d76-9ab5-a7c440471a50 | -4.4268 | -43.1007 | 2026-01-13 00:20:00 | GOES-19 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 8f2b5990-4f83-3915-8dbc-e4052afa0fbe | -5.099 | -43.2444 | 2026-01-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 270.5 |
| 23b42637-6aae-37d4-bf78-f8e15dd67aee | -3.2905 | -42.5507 | 2026-01-13 00:20:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| f5990082-5eb1-3abe-81d1-b6662d8bf7ef | -5.0992 | -43.2211 | 2026-01-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 471.3 |
| 83ca1269-be5c-3fe0-bea0-ce5bf2e06907 | -5.118 | -43.2198 | 2026-01-13 00:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 343f97d1-14d1-35a9-b3dc-2c41685dc121 | -17.7554 | -40.09629 | 2026-01-13 00:26:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| b89998f1-6cb2-3c7a-b9f4-98995a11e9cc | -22.68288 | -43.7212 | 2026-01-13 00:26:00 | TERRA_M-M | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| c44f51ce-9326-393c-a5d9-53bddbc41d9b | -21.5635 | -43.65972 | 2026-01-13 00:26:00 | TERRA_M-M | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 62.2 |
| 49f6ab5b-cc54-3869-b7f8-702e608fc722 | -20.88033 | -48.59655 | 2026-01-13 00:26:00 | TERRA_M-M | MONTE AZUL PAULISTA | SÃO PAULO | Brasil | 3531506 | 35 | 33 | nan | nan | nan | Cerrado | 7.6 |
| b8a9e8ea-8a62-351e-86ad-39075c03053e | -17.76231 | -40.11745 | 2026-01-13 00:26:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 35.6 |
| a62d698b-b318-3ed9-875c-a552da9ae78b | -21.28243 | -48.71723 | 2026-01-13 00:26:00 | TERRA_M-M | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 4cc41048-89ca-3789-bb6d-79979d546e70 | -17.76024 | -40.12322 | 2026-01-13 00:26:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 0319030a-9bfc-3f33-b2d4-499a8eeef2b6 | -20.84127 | -51.74677 | 2026-01-13 00:26:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 6.7 |
| 5b145928-11d5-3c8f-9e5b-536d49b59b04 | -21.3564 | -48.58142 | 2026-01-13 00:26:00 | TERRA_M-M | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| bc7e8217-0abb-30d2-b7e4-e3e0a169db33 | -17.64868 | -45.59644 | 2026-01-13 00:26:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 2b6c888c-cd49-3476-af6a-a230dd86c24d | -21.5656 | -43.67266 | 2026-01-13 00:26:00 | TERRA_M-M | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.0 |
| 9daf7001-1337-3a62-b138-819fdbc38dde | -20.06288 | -50.02334 | 2026-01-13 00:26:00 | TERRA_M-M | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 6fb6816e-2f0d-399e-9e87-e03c8160b563 | -17.75723 | -40.09028 | 2026-01-13 00:26:00 | TERRA_M-M | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 38.2 |
| 3006c5d5-be2d-3d35-bcbe-ebbf366e3e76 | -21.39895 | -44.55262 | 2026-01-13 00:26:00 | TERRA_M-M | CARRANCAS | MINAS GERAIS | Brasil | 3114600 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 62de3788-f485-3602-84e0-6c09185d8db0 | -19.81289 | -54.73366 | 2026-01-13 00:26:00 | TERRA_M-M | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 149d0903-f8ef-31c7-b644-7c19890e0b4e | -5.1178 | -43.2431 | 2026-01-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| a6a9309d-629b-3838-9422-ffd8464f180a | -5.0992 | -43.2211 | 2026-01-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 394.8 |
| 556a09c9-e039-323a-8b5a-22e6aff8abed | -5.0805 | -43.2224 | 2026-01-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| cf4354dd-ec51-3f5b-8d0d-e23493e49a1d | -5.099 | -43.2444 | 2026-01-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 209.3 |
| 1d62c2f2-0dcb-3d4e-99de-f5e8260494bb | -3.2905 | -42.5507 | 2026-01-13 00:30:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 76.7 |
| a0c553b1-8507-378b-8faf-9c3b52eb0aa3 | -21.5756 | -43.6567 | 2026-01-13 00:30:00 | GOES-19 | SANTOS DUMONT | MINAS GERAIS | Brasil | 3160702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 82.1 |
| 4b614559-122a-3ead-8e88-4d5a92a54aa1 | -5.118 | -43.2198 | 2026-01-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 214.9 |
| 36b941e6-34e7-3f88-9d91-8ed522f0b17c | -5.0803 | -43.2457 | 2026-01-13 00:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| c638bc62-3de5-31df-b686-30cc8728f57e | -3.17967 | -48.01978 | 2026-01-13 00:32:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 7168c05f-d175-35ef-8fa1-ff68c5d02990 | -5.11074 | -43.23915 | 2026-01-13 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.3 |
| 2eb4e397-f71f-3fd1-805f-6aab0d0119df | -3.18139 | -48.03163 | 2026-01-13 00:32:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 32cc81b8-af9d-367f-8774-d8d9cf23151e | -5.08999 | -43.22305 | 2026-01-13 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 215.3 |
| 08ed4ea7-e2ef-3d49-a54b-c895e22cbbda | -1.85339 | -54.02635 | 2026-01-13 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 10517846-4dba-3e09-a30d-cd4dfd3bdae2 | -1.28951 | -53.68603 | 2026-01-13 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| e71dae47-14c7-33cb-8bf1-a4bd583968d1 | -0.45468 | -51.78307 | 2026-01-13 00:32:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| db0c6581-d6e7-3056-bf5f-81f8e52338a2 | -3.44231 | -49.0001 | 2026-01-13 00:32:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ec107da-650b-3ade-88bd-bc26d82ee9f0 | -3.06155 | -51.74918 | 2026-01-13 00:32:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4eda736f-3bdb-32a7-9d5e-b682b37a2e8b | -5.0939 | -43.24867 | 2026-01-13 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 109.9 |
| f4c29d25-9deb-3885-a1fa-ae2b207e6d0e | -2.82147 | -52.95995 | 2026-01-13 00:32:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a430cdbe-5d9b-3c4f-8621-4b2ca77e3d9b | -4.26209 | -48.42159 | 2026-01-13 00:32:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| de1e8ef5-5c24-3395-b265-3183e65f575e | 1.21251 | -50.98835 | 2026-01-13 00:32:00 | TERRA_M-M | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 164ac6f0-f601-3f2f-bb49-ead95adcc21c | -3.5491 | -43.64897 | 2026-01-13 00:32:00 | TERRA_M-M | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 9668f8ac-52b1-3451-9f25-8d3f58cf0a9f | -5.10825 | -43.24621 | 2026-01-13 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.5 |
| c355aa67-d4ec-3d28-98d7-adb6584cca14 | -3.29389 | -42.55618 | 2026-01-13 00:32:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| fc8b0871-a0b9-3d88-98c8-f69887fe1d3c | -5.10435 | -43.22043 | 2026-01-13 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 455.6 |
| 2b601aa5-9d14-3d05-9c1b-f49a3ba48ca3 | -5.10664 | -43.21337 | 2026-01-13 00:32:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 09a11291-e111-3a37-a154-a57a88de64a6 | -0.09146 | -51.28527 | 2026-01-13 00:32:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8796f082-4b7d-3392-9915-b3b0611b6d6b | -1.85478 | -54.03636 | 2026-01-13 00:32:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c5cb9309-94c4-343f-8321-331bc0e8a0df | -1.98011 | -53.14107 | 2026-01-13 00:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| db62c3ec-ea0d-3fdd-b211-941e2369c87b | 0.62507 | -50.76893 | 2026-01-13 00:32:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8f18bada-c5bf-3f43-8e4d-ae86dcba5b9a | -1.29865 | -53.68468 | 2026-01-13 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 35de8828-f147-3a03-9de2-f61199db1fb8 | -2.28361 | -51.93106 | 2026-01-13 00:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 132be3cc-1b65-3c81-bd62-4cef47ebeae2 | -1.92355 | -53.4693 | 2026-01-13 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 0bdcd6f3-ac23-3127-85d5-6410e0710455 | -2.19486 | -52.02071 | 2026-01-13 00:32:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| d613a5dd-c3e6-35ab-81d0-c8c6cdd774d4 | 0.62379 | -50.77826 | 2026-01-13 00:32:00 | TERRA_M-M | ITAUBAL | AMAPÁ | Brasil | 1600253 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 36610264-6599-3636-8658-f47a699801b5 | -4.25876 | -48.83859 | 2026-01-13 00:32:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9bf64339-ca62-3a53-86ba-5740c7149702 | -3.28901 | -42.52449 | 2026-01-13 00:32:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 7f468ca7-7d9f-31c7-a2bf-da6e80cd80c9 | -3.44377 | -49.0104 | 2026-01-13 00:32:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 37204ede-ac5e-3bf9-85fe-219b761e405c | -3.28397 | -42.56309 | 2026-01-13 00:32:00 | TERRA_M-M | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 55c5dfe6-89b0-34bb-a41a-54c303fc6e95 | -1.93268 | -53.46804 | 2026-01-13 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| dfbbda1e-71e3-3090-b83a-21e6b29bf209 | -1.93398 | -53.47751 | 2026-01-13 00:32:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fe48ac34-bccc-3871-baf6-726e42e1e2ac | -3.29501 | -42.529 | 2026-01-13 00:32:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 32.1 |
| 6c18c225-406f-3a42-bbd2-76236f9e5cb0 | -3.29963 | -42.56068 | 2026-01-13 00:32:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 27.5 |
| fd9765ba-d584-39ee-aa31-cca05ef6ecd8 | -3.2905 | -42.5507 | 2026-01-13 00:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 766c277d-95a3-375b-8ff1-4d4ac5714828 | -5.1178 | -43.2431 | 2026-01-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| c21d5170-0847-3403-b479-e2d514891892 | -5.0992 | -43.2211 | 2026-01-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 70e97a0e-03d8-3700-a603-11657ea42f59 | -5.099 | -43.2444 | 2026-01-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 155.8 |
| e6df92ec-a299-3433-a80e-45a0cbc1c0c0 | -5.0805 | -43.2224 | 2026-01-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f33e6c51-218b-388a-8b95-db6fbe5d887f | -5.118 | -43.2198 | 2026-01-13 00:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| b7d2cf5a-b191-3e59-9318-346ea9ca4511 | -5.1178 | -43.2431 | 2026-01-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 93.9 |
| 10b27c6e-bc22-3fb2-88cd-24acd85e39cc | -5.099 | -43.2444 | 2026-01-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 262.4 |
| 90f7f09c-8978-3c9d-a5ce-7cc66f5c5a95 | -5.0805 | -43.2224 | 2026-01-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| 656a5e22-e2e2-3636-b55d-ae7589157bbc | -5.118 | -43.2198 | 2026-01-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 8d34298e-e8b5-3897-b07d-4285c17e9509 | -5.0992 | -43.2211 | 2026-01-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 379.9 |
| 5cd3f935-84b8-3ce8-8ff5-95123ad0c7ca | -7.3608 | -35.1958 | 2026-01-13 00:50:00 | GOES-19 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 71.4 |
| 2181ac1b-efd5-3108-ba8a-64c08fe9a7f1 | -5.0994 | -43.1977 | 2026-01-13 00:50:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| fef5d1af-18d7-396e-84fd-4448b08e6a99 | 3.9123 | -60.4417 | 2026-01-13 00:57:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 252c6719-cd55-3375-8094-d7603b3bef38 | 3.7213 | -60.375301 | 2026-01-13 00:57:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 101f8264-4624-3c14-bfc0-ad3cffbc89ae | 3.731 | -60.5616 | 2026-01-13 00:57:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 8e9363a9-520a-3cab-a37a-d18f4ff9e529 | 3.914 | -60.433998 | 2026-01-13 00:57:00 | METOP-B | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 265ad50b-8cc1-3d17-90a4-3f33de3ddcc5 | 4.4819 | -60.655701 | 2026-01-13 00:57:00 | METOP-B | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2d6ef2cd-90a5-3800-999c-7c408b280644 | 3.4328 | -60.6063 | 2026-01-13 00:57:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
