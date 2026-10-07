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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a9eb9f45-f1e3-3988-bc80-48919d387de4 | -11.72 | -43.69 | 2026-10-07 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 59c62d4f-80cc-3f72-ad88-16a52ea71bdd | -11.09 | -45.73 | 2026-10-07 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a051840e-5ac5-3b5b-bee2-8b1e6a34f545 | -3.29 | -54.01 | 2026-10-07 01:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd32a63d-3223-31a0-a0c5-f70cc6ff44e9 | -8.7 | -45.19 | 2026-10-07 01:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0796d027-c8ca-327b-ac4a-0ef5acb9a1ee | -11.12 | -45.74 | 2026-10-07 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f3f02319-9bd7-30f0-a8cf-9d06cc6912a2 | -3.6762 | -60.6219 | 2026-10-07 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 79.7 |
| d3d81272-5ef0-3cbf-8b44-58e11ef50c2b | -3.1787 | -50.5597 | 2026-10-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.5 |
| d20c5d48-7777-38ac-a39a-c735957a1f75 | -8.2865 | -50.2731 | 2026-10-07 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 144.1 |
| e88b6859-9d8a-3011-a2c2-a5215673c22b | -3.6205 | -55.2907 | 2026-10-07 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 4dc8fb2b-c2fe-3e0a-9509-d24ca92e0cb2 | -13.5117 | -44.368 | 2026-10-07 01:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 91f9cc4c-eabf-377c-b42a-6b4f68a5f71e | -2.9264 | -54.1505 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 854e4f90-c629-3dcd-8b79-219159912b2f | -8.7036 | -45.2061 | 2026-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 167.6 |
| 09b4f2ae-6ec4-3b05-9018-cce65c926188 | -9.1517 | -65.9554 | 2026-10-07 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 20728bf7-5949-345d-881a-cfb939462d81 | -11.2333 | -44.8678 | 2026-10-07 01:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 7ffb9f51-9446-3418-b2ed-013932453179 | -5.7187 | -45.1773 | 2026-10-07 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.4 |
| b9554a40-388c-3057-89e2-3a9451413aa1 | -3.5515 | -59.4807 | 2026-10-07 01:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 04441959-631b-36ad-87db-a61904dcd8fb | -2.9448 | -54.1501 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| ca028eb0-e1c0-3285-b70b-f9d9572af601 | -3.0001 | -54.1086 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 415b0767-29ba-3341-b6b8-4a5e1beff222 | -14.2531 | -41.6256 | 2026-10-07 01:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 156.9 |
| 8744b413-b66b-3af0-8b07-aa64d9c99f91 | -3.8567 | -55.9769 | 2026-10-07 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 93.2 |
| 7b734d48-0674-3440-911c-2dd540604864 | -3.0373 | -53.9469 | 2026-10-07 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 3e689966-7aca-3391-8913-9b18472d1464 | -9.4621 | -67.0817 | 2026-10-07 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a8fcf39e-bd04-35a4-9346-7a6dc7f493b4 | -3.0 | -54.1287 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 192c061c-a767-34e5-9c94-67af74f7f769 | -11.014 | -45.4272 | 2026-10-07 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.8 |
| bcfbc548-43b2-3602-9499-3030a08eb3b7 | -2.7796 | -54.0937 | 2026-10-07 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 186.0 |
| f2178a8b-7bd0-37a2-b9b8-9fc9ce160456 | -2.7612 | -54.1142 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 5330902c-fc0a-3ce5-be96-4bc267f22a55 | -12.1742 | -44.7284 | 2026-10-07 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.2 |
| bd0ec814-5391-3958-aa7f-bb2317eabf34 | -2.7796 | -54.1138 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 71e1e045-c9a9-33ab-ae3c-ede7a56733b9 | -6.766 | -56.2402 | 2026-10-07 01:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d524a0d3-c3d9-3cd0-9292-0a301f92f988 | -2.7797 | -54.0736 | 2026-10-07 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 40046d5c-1f89-3bcd-b320-9b1a9a874f87 | -3.2728 | -50.1372 | 2026-10-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 1d25f001-3fd4-3515-8966-7765426435b2 | -5.9835 | -40.9367 | 2026-10-07 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| f98d64a7-59be-39c8-95b8-b036353c5c8e | -1.2922 | -54.5585 | 2026-10-07 01:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 7531a6ea-abae-3402-9871-84cdee71f429 | -2.7613 | -54.0941 | 2026-10-07 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 218.4 |
| 65427a71-6f54-375d-8333-85baf4520806 | -3.4577 | -50.089 | 2026-10-07 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 7906f8fd-cda0-372a-b825-147035e7355b | -3.8566 | -55.9967 | 2026-10-07 01:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 123.0 |
| 60215794-aaca-3f5d-9514-480b313a186a | -5.9838 | -40.9123 | 2026-10-07 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 31d8cdde-bda1-39b0-9eda-c4f450ebb720 | -10.9953 | -45.4068 | 2026-10-07 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 0ef482d0-61b0-3aab-97b7-7f85eb966341 | -11.7335 | -43.649 | 2026-10-07 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 99cf8c59-326e-3960-9c70-3ed6f5fa2c55 | -8.7228 | -45.1812 | 2026-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 1dd15c06-662a-3f0e-95b9-c81249cc2ba8 | -3.1115 | -53.7637 | 2026-10-07 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| b6d51d92-7255-3acd-bc77-ab895e84db65 | -1.801 | -57.1161 | 2026-10-07 01:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 45291bfd-16ca-3c51-9f42-ef04d5ce01aa | -3.6762 | -60.6409 | 2026-10-07 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 172c3f71-80e8-3d49-82b9-18827584b534 | -3.0375 | -53.9066 | 2026-10-07 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 2bc4dbf4-7452-3266-8d86-0537ab1d8a2b | 3.1463 | -60.5937 | 2026-10-07 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 301bf98d-7df0-3acc-b88d-b99e2e74655f | -3.1787 | -50.5807 | 2026-10-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 5bc279fe-3e2e-3486-909e-9e323959d32b | -12.1939 | -44.7021 | 2026-10-07 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| afa66053-f560-3019-9b7f-b02903840867 | -3.1114 | -53.7839 | 2026-10-07 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 56d4d244-b1ed-3467-a4e8-807302de2a3b | -1.8011 | -57.0967 | 2026-10-07 01:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 02ad4386-c926-3636-a25a-350e9750edf7 | -3.1972 | -50.5592 | 2026-10-07 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 5e27b487-fc9e-3c88-80bf-da1be7100a54 | -8.7033 | -45.2289 | 2026-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 3d37beee-f80e-34f8-a08f-458f51af51f6 | -8.7225 | -45.204 | 2026-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 3b6f7164-0bc0-32ff-ae4a-d27ec4fb6370 | -3.4762 | -50.0883 | 2026-10-07 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 135.3 |
| 9feecf30-2315-3b40-a4b2-6a249d2c73bf | -11.0137 | -45.4501 | 2026-10-07 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 149.0 |
| 5756be19-3e5b-3a0c-a84d-2dd4889d916a | -3.0374 | -53.9268 | 2026-10-07 01:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 7a76645d-b4df-3f8d-8e72-ae116edd70bd | -3.1101 | -54.1661 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| afbbaf0d-9587-3cf8-a77a-9fb1a852fed2 | -3.0184 | -54.1282 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 9066d760-d6f8-32ec-91d3-0a1f7222c665 | -2.7613 | -54.074 | 2026-10-07 01:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| d7532b0b-40ec-3cf9-b3f2-2639d09aab82 | -5.9647 | -40.9383 | 2026-10-07 01:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 57.0 |
| aad20818-baf0-3d38-b8b4-1c6399e09a37 | -5.7189 | -45.1547 | 2026-10-07 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 128.3 |
| 37095ed1-4f14-3ce8-b738-84c6a7873030 | -5.7374 | -45.176 | 2026-10-07 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 1e1d7a25-d7c9-3807-8ab8-952eec95c082 | -8.2868 | -50.2519 | 2026-10-07 01:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9809d354-769a-301f-96e5-4029273da363 | -10.9949 | -45.4298 | 2026-10-07 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 205.4 |
| db178e2b-08c8-3c0a-8f00-09a0d731c791 | -14.2537 | -41.6007 | 2026-10-07 01:20:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 97ef1665-8a71-3c3b-b927-545936ee2dc4 | -3.055 | -54.1474 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 9f08a01f-5095-3880-a280-232013607232 | -2.9447 | -54.1702 | 2026-10-07 01:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 42dbc6f6-d155-3cad-ae92-df85a48fecd4 | -3.6579 | -60.6412 | 2026-10-07 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 127.5 |
| cadc0ad4-e8a9-3446-9538-a411e727403c | -12.1746 | -44.7051 | 2026-10-07 01:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 510a9575-9948-3b20-b1d7-0b35b2b9b640 | -10.9946 | -45.4527 | 2026-10-07 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 108.8 |
| e0ad2574-74c8-3c91-8173-dbc91cc5e161 | -3.4763 | -50.0673 | 2026-10-07 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a6d713d8-6a25-3625-8c72-cc1a6aaf7b3c | -3.658 | -60.6222 | 2026-10-07 01:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 181.3 |
| 5e8b1c88-fd75-3135-93cb-a8c9c499ae99 | -8.7039 | -45.1832 | 2026-10-07 01:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 25a6f01e-e8ef-3637-865a-651a51b7ada3 | -5.7376 | -45.1533 | 2026-10-07 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 662c18d9-8a4e-33a1-b5d0-a42c1db918fb | -11.7774 | -46.5726 | 2026-10-07 01:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 73.5 |
| c7f9474b-65e4-37cc-b5ab-00b2ff79d33c | -3.2728 | -50.1372 | 2026-10-07 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 47d57ff3-38d4-3678-8839-0ab2c7d7b8ae | -3.1101 | -54.1661 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| d3bf00cd-7395-3e40-9993-93d8dd6535d2 | 3.1463 | -60.5937 | 2026-10-07 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 8b45c1ab-5583-31a4-ad9b-6821ecb29288 | -2.7612 | -54.1142 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| d278a0dd-ad93-351f-9c04-e6f3a803f2f4 | -3.0001 | -54.1086 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 97d118dd-ed32-384a-9b1b-f2f48b8779c0 | -8.7036 | -45.2061 | 2026-10-07 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 239.2 |
| f64003d9-6956-347e-bdb5-be2635e0b39f | -3.1972 | -50.5592 | 2026-10-07 01:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| da2314db-0a14-3e36-8c76-613255690e89 | -3.8567 | -55.9769 | 2026-10-07 01:30:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 989deed0-9133-3915-a92f-8e0bf5fd8c6e | -2.7796 | -54.1138 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 135.4 |
| 94a518ae-d2eb-35fe-86cf-ebaf64994861 | -2.9447 | -54.1702 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| abcf936f-1984-3d09-9511-5e3f59ea800a | -3.1115 | -53.7637 | 2026-10-07 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| ac802dd4-3a0f-3733-9ddc-2e20da51f03a | -5.9835 | -40.9367 | 2026-10-07 01:30:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 63.2 |
| 088b4db8-047b-33b4-b36e-57200c748f5f | -11.7335 | -43.649 | 2026-10-07 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 430960bd-77f8-3ad8-9b00-323690e59e55 | -10.8989 | -46.6667 | 2026-10-07 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 63.5 |
| b256c1ab-0403-3709-9618-e015a5f09fa0 | -3.5515 | -59.4807 | 2026-10-07 01:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 5fc85e3c-d7ce-33ea-af09-ed2d79a6c7c9 | -3.6762 | -60.6409 | 2026-10-07 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6addaffa-468b-3bd2-a3cb-36526ea8f58a | -2.9448 | -54.1501 | 2026-10-07 01:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| c5451176-59d0-386d-acf9-4ab7876f7d4a | -5.7189 | -45.1547 | 2026-10-07 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 78.7 |
| da798103-b19f-3f2f-85ce-4c7393b7ef30 | -3.1114 | -53.7839 | 2026-10-07 01:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 3cce4c20-3699-34fe-99b8-5ab0f8f1e6ce | -3.658 | -60.6222 | 2026-10-07 01:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 33ecc412-8a9e-3456-b134-acc193e74362 | -2.7613 | -54.0941 | 2026-10-07 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 213.3 |
| 57ebae80-8b46-3f25-86a7-90afccb0c9b1 | -8.7033 | -45.2289 | 2026-10-07 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9c8dbe6a-8995-3508-99e4-e1b935cbd045 | -2.7613 | -54.074 | 2026-10-07 01:30:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| e132bbdf-a00d-3e5d-8048-1821b4059de3 | -14.2537 | -41.6007 | 2026-10-07 01:30:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 92.4 |
| 2adb3a89-ff3e-3bf7-8f2d-ce58e4166e4b | -5.7187 | -45.1773 | 2026-10-07 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 1f80d750-b052-3cfd-87b8-394365cc03fb | -8.7228 | -45.1812 | 2026-10-07 01:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 97.2 |


[Clique aqui para ver as próximas entradas](README25.md)
