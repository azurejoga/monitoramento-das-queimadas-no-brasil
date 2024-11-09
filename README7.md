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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad279c7f-9154-3bbb-b03f-a47718e97108 | -2.04182 | -46.08869 | 2024-11-09 00:39:00 | TERRA_M-M | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 83e16d2f-dab0-3efa-8a69-5975221f3fa2 | -2.90632 | -46.81213 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7c0c8453-7c3c-3771-bb51-d47ad4243061 | -4.06047 | -48.31081 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 270cdd57-d67c-32c8-b3f1-e3b85df29ecd | -2.37055 | -46.86447 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 887ed9d5-e9dd-3c77-a7b8-eafd859cfdaf | -2.23084 | -46.84751 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1504ee75-e487-36b2-929f-807007a1c119 | -4.70714 | -46.37999 | 2024-11-09 00:39:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1a934b59-20ae-3f8b-b53c-f0a0f9cd2c05 | -2.68113 | -46.77337 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c12ce272-48a2-3154-a0d8-9dfbbedf8fe0 | -2.54551 | -47.12109 | 2024-11-09 00:39:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 54ed4b4c-2408-37be-a472-d37490e7bb40 | -5.47223 | -43.66253 | 2024-11-09 00:39:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 57.0 |
| dc337e2e-7eeb-32ef-827c-12cf1d41d3b6 | -3.7214 | -49.35928 | 2024-11-09 00:39:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 32.2 |
| 4f03a4f5-a319-36c3-9851-c4a8d8024446 | -3.96924 | -45.37374 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 15.2 |
| c3c6a3e9-5f3b-3c25-94a1-817dbde7bdc8 | -3.19318 | -50.43731 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1e534986-48c0-34d8-be6c-d1802b967ce0 | -3.40105 | -46.05659 | 2024-11-09 00:39:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| bba013a9-856a-3a8b-9aa1-b191b9ccc9a9 | -2.19424 | -53.65615 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 68a08918-5702-3e55-9a20-8c8927de08cd | -2.79768 | -45.48508 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 81557cdd-00db-3f41-a392-992a9e2e7e4f | -3.30319 | -46.41587 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 21.5 |
| c363ec9c-fe33-3bea-b6b7-503843fb2c89 | -4.61065 | -49.06265 | 2024-11-09 00:39:00 | TERRA_M-M | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 4355a1a4-bede-3b65-a032-bffbd1d7745b | -3.64553 | -45.89232 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 11feb6a6-dcf7-3e6e-8485-e8d69af7c638 | -2.72668 | -45.77909 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 10aeba69-b4aa-3ff7-be17-70aa99d9fc37 | -4.10805 | -48.50451 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 07e2451f-57cb-36db-9f90-325139b2c06c | -2.24106 | -53.77066 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 182.3 |
| a146e9a7-b7a5-3ea6-ac81-817e649777e8 | -3.95755 | -48.9855 | 2024-11-09 00:39:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 961f4df3-29d4-36af-bdbe-6876e2711908 | -1.52432 | -52.18669 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 36db64ea-7f09-3e25-a1db-1b34d6d69832 | -3.38736 | -52.34806 | 2024-11-09 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| e538a6f2-d16d-30bd-9676-9b4f4aa654c9 | -4.39328 | -50.96873 | 2024-11-09 00:39:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| d3e6ff14-e114-3e14-9edd-983d6f254952 | -4.19568 | -48.55037 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 19.6 |
| f20230b2-d088-3796-a37b-eb3d49ae5d4a | -3.78838 | -47.73854 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 58151c73-2f7b-3d81-b409-db82c366ed8a | -1.85857 | -47.82666 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6d35ffbf-e8ce-3d87-81d0-1a81f5195e96 | -1.50193 | -47.17461 | 2024-11-09 00:39:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 39.4 |
| 1d77e8e1-79cb-3530-8d1a-46701eed93a9 | -2.80147 | -45.98259 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4bc61ef5-4fac-31e5-b856-30fc34513583 | -2.23549 | -46.55253 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 987d0142-7eed-3a1c-87c6-3b0291c7e629 | -2.13536 | -46.6968 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 94af01f1-c02e-3995-9feb-00b365f2e559 | -2.905 | -46.8025 | 2024-11-09 00:39:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2394a904-2393-3c34-ad19-f8afbcbd7300 | -2.29269 | -46.50074 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 45aa91d5-e575-35f0-ab1c-94d18ae0b7d2 | -2.24407 | -53.6792 | 2024-11-09 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| dba7b755-2b7d-3c4f-b889-8ad4a033c68a | -2.45926 | -46.3053 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 656d19d1-0bc8-3b91-adac-939646d1c698 | -4.21079 | -45.85082 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4d759637-1f6c-3756-a513-5164e456cc6a | -1.5765 | -46.8462 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 30a302c7-ab4d-3b4a-89b6-a43d5ccc7c2c | -6.26867 | -44.54049 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 5b756c16-b4e4-3ae7-aaf9-d5d69b0feda5 | -5.19546 | -44.91621 | 2024-11-09 00:39:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b217ca66-d113-3e83-9ae4-eb48b90b0c7f | -4.1908 | -44.17694 | 2024-11-09 00:39:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| afb671b3-87d1-3eba-924a-cfd9b6deaa80 | -4.11277 | -46.88458 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| e2d012bf-305c-3995-9f4c-309ff6da1156 | -2.16143 | -46.68359 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36af0de3-e7dc-3dc7-b953-352fad7c4e2f | -3.03082 | -50.36383 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 2c6b2059-d79d-33b5-9bba-31654f244587 | -6.27874 | -44.5481 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ab579186-7c02-3f91-849c-63fa5c40f2dc | -2.51592 | -46.3161 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f98ca680-0eb5-3dab-8481-3da4042d92e7 | -4.62695 | -46.53531 | 2024-11-09 00:39:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 8f33f40b-5da9-3df4-9d3c-091e81fa3ad1 | -1.64502 | -47.82583 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07d3d9cd-0188-33a5-b5f4-0230cdcaa37a | -3.01482 | -51.03885 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 18be36b4-e8da-37e3-94a0-795d2d1c7cfd | -6.49914 | -39.56458 | 2024-11-09 00:39:00 | TERRA_M-M | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 8.5 |
| be68b677-5477-3e16-8ae3-bc10b788a24e | -2.3522 | -46.66382 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f0ebeb6f-b614-3228-ab64-b939f1ea9727 | 0.04191 | -49.54007 | 2024-11-09 00:39:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 259141f2-1419-3f08-9d34-da1090f439d4 | -1.56327 | -52.27087 | 2024-11-09 00:39:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 8607512f-1a3b-39ca-b20f-e0b7a19668df | -3.60512 | -47.35526 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 158.6 |
| 1571bed9-0315-36db-880c-045c2c39577a | -4.49522 | -48.49082 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| ebbc87f2-35a8-34d6-9445-2328192dc45d | -3.03821 | -50.32935 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.9 |
| ec5f0297-6053-3750-ad2e-e2c8be231f50 | -3.60174 | -47.36213 | 2024-11-09 00:39:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 5c442517-b61e-3ea9-a369-2746e11b4f75 | -4.80218 | -44.93303 | 2024-11-09 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7f306904-d3e7-3e53-af38-b66e7c700fcf | -5.63542 | -44.83277 | 2024-11-09 00:39:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 69.3 |
| a88e78a8-77db-3681-a614-055ed5143881 | -3.5971 | -42.83954 | 2024-11-09 00:39:00 | TERRA_M-M | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 028984a1-1229-394d-9cca-bf6ac7f972e0 | -2.29926 | -46.74441 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 08d8b81b-2de7-3143-98c2-96d7813e5067 | -2.51196 | -47.47053 | 2024-11-09 00:39:00 | TERRA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0119b17e-79e9-30b1-bb8f-ada08471fe82 | -1.51119 | -47.17336 | 2024-11-09 00:39:00 | TERRA_M-M | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 137.6 |
| ca3c60ee-cad9-32a7-a64f-4b8c6529790b | -2.3483 | -46.63562 | 2024-11-09 00:39:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b1d331cb-1454-3082-a725-8d7f860b9a63 | -5.22079 | -47.90332 | 2024-11-09 00:39:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| d7bf6fe3-5646-30e8-bcb1-cbb3e637e3f8 | -4.20307 | -45.86124 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 543.4 |
| 419d83f5-a6c9-3fba-ae4e-8df6ae614ecd | -4.81103 | -44.93175 | 2024-11-09 00:39:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 8f77add7-b506-32af-bc48-e92e935a58f9 | -1.24654 | -51.77636 | 2024-11-09 00:39:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 185c8d3b-0586-37aa-b261-8ea9b6797ab6 | -2.19984 | -48.37748 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| 52a223ca-9775-32df-affa-fdbdbc2df8d2 | -2.4657 | -50.39981 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 473c663a-80c9-347d-b93e-b34b5f4237aa | -3.44707 | -45.98804 | 2024-11-09 00:39:00 | TERRA_M-M | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 75b52327-a005-3d31-832f-1322fac2cc91 | -2.41264 | -48.51401 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a361564b-5928-398d-a9da-17ba7a193a65 | -1.69843 | -48.14584 | 2024-11-09 00:39:00 | TERRA_M-M | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ac89522c-70a2-33c5-a233-3fbca9e86242 | -2.458 | -46.29614 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 24d10df9-2d73-35c7-b190-114049f3c020 | -2.67722 | -50.95306 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| fd74844f-8cd6-3c99-bc02-218d829b756a | -2.29598 | -48.56016 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b4b855cf-10a3-3352-a95b-f8a0ca89f114 | -2.42257 | -46.30698 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 02bd53ec-64ac-338b-8ac8-024101c54440 | -2.41425 | -48.52581 | 2024-11-09 00:39:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 65a90d1a-025b-305f-a0c2-18dad8a20477 | -2.19083 | -47.9473 | 2024-11-09 00:39:00 | TERRA_M-M | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6408d816-2db7-3cee-90db-d167f4d6e451 | -4.99126 | -44.17688 | 2024-11-09 00:39:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1fc5159e-5f62-3537-8373-86b73be09420 | -4.4167 | -45.94068 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9e644f5a-c93f-31c7-a78b-5fe66bf66e96 | -2.62449 | -46.16746 | 2024-11-09 00:39:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0aff3ea8-547d-39de-93e2-5880d05e8c39 | -2.90057 | -45.30261 | 2024-11-09 00:39:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c9d4fd31-aa6c-30a6-be47-0dcfe8b4a609 | -4.41919 | -43.37973 | 2024-11-09 00:39:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e676f8c4-2e4e-3983-b752-fc05d9fa298b | -6.53477 | -44.46613 | 2024-11-09 00:39:00 | TERRA_M-M | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| a9375bb7-b79a-3b10-9f2a-b6a496c461ef | -3.13557 | -44.40919 | 2024-11-09 00:39:00 | TERRA_M-M | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55ee0290-9555-3637-9e13-369a0ba58fda | -4.49213 | -48.49782 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ac766dfa-ecfd-3fb6-9579-d7833d0e0090 | -3.53515 | -51.10599 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 60a9755e-dd43-3b17-b7f2-93340ccb2579 | -6.10532 | -44.75683 | 2024-11-09 00:39:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 21.6 |
| 7e356611-ebf3-3d47-8007-05b84223ec1c | -4.21307 | -48.67762 | 2024-11-09 00:39:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5044b334-d326-36a4-96c7-baa7b698e164 | 0.0332 | -49.44821 | 2024-11-09 00:39:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 453c9b9d-e297-3d89-b169-1b7f19f6b51c | -3.01628 | -51.03221 | 2024-11-09 00:39:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 0ae051f7-7d5b-3aec-9380-52ea733639f4 | -2.27051 | -46.47195 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 6de2b933-0407-373f-b3c2-faab31174881 | -3.2704 | -52.73137 | 2024-11-09 00:39:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| c2840f22-6079-3f82-bb99-c0a127fdd242 | -3.24524 | -45.92659 | 2024-11-09 00:39:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 57993f43-db0a-3d7c-9034-e2fca2fe80fe | -2.09534 | -46.47099 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| d02f2b13-97a2-3c9f-a622-56210d6c3a0e | -3.34768 | -50.26303 | 2024-11-09 00:39:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| fe84300f-eefe-3d58-9232-d722647cf46c | -5.49701 | -46.30437 | 2024-11-09 00:39:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| c8089d02-a15d-3ad2-9a65-687c0811c254 | -2.09406 | -46.52776 | 2024-11-09 00:39:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| fda2358e-79f1-3eac-8a68-a61d4d6029cc | -4.23506 | -47.56815 | 2024-11-09 00:39:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |


[Clique aqui para ver as próximas entradas](README8.md)
