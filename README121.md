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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cca51f50-42c0-3699-8071-c036ad0d1b45 | -3.49254 | -50.49354 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e56d6ad-1b41-3fad-b4f9-242936f297eb | -3.48892 | -50.493 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6f96805-3209-35df-b63d-83cfc7a722f9 | -6.93919 | -59.10516 | 2026-10-10 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a4ecfcf7-cf7a-3d7a-9e0e-afd61f996be8 | -4.11967 | -59.89433 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 829107f6-114d-308a-ae4f-8897af7620ab | -3.99064 | -54.45674 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8d606e7-4ddc-3712-b30e-ed7012f1b613 | -3.01726 | -54.23161 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f95422e-8349-371b-9236-6f535d4dcd4d | 0.00437 | -60.5729 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4084d35f-3503-3a9f-86fb-e6f7feb5367b | -7.46187 | -54.97819 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 848218cb-144b-3d88-8edb-59be4a36df1a | -3.04028 | -54.10766 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 36c55b36-a2d1-393c-9423-ff97c27654dd | -3.0104 | -54.0393 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f8bb542-0106-3ac9-8db8-a4aa680e0003 | -2.52246 | -58.07166 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54575368-625f-3171-8c35-3831e90fb718 | -2.58508 | -56.13985 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0affa067-6985-3a86-a7ba-e39a649c7369 | -3.23834 | -53.88792 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 495e658a-5fe7-396b-bb16-71235a5019a2 | -4.1343 | -50.82369 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 285fe45f-08ac-33f7-b789-f2525a41b450 | -3.18812 | -58.64016 | 2026-10-10 05:04:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78ec48a0-2596-319a-b339-6472948de312 | -2.97406 | -54.1185 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 89309503-e591-310a-abd9-f21d7a495b11 | -4.59576 | -54.92398 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e097e19d-3abf-376a-9a18-4b1703929e84 | -2.98733 | -54.14182 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61427b91-4dcb-313b-beff-0da7e8bb4a6f | 0.2204 | -60.60681 | 2026-10-10 05:04:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fb437d9-897c-3343-a6c8-463b65107d05 | -5.22167 | -60.04716 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 974bd4ee-c462-3bcc-a255-8bdfce0894c6 | -2.99698 | -53.88893 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 83787695-2a56-30eb-b32e-c9a606fac93d | -6.13135 | -53.10093 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1b0bd59b-9507-3cea-877b-0be97f6688e9 | -5.08516 | -60.21836 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4ca518cc-218b-3f58-ab20-c073a13a8560 | -3.60022 | -54.6049 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c814abbd-fa53-32a8-9e10-f024ce966787 | -3.54072 | -54.7427 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f119a391-2b0e-378c-afba-aad216b4d95b | -7.21938 | -55.0715 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e19cd687-943d-3c50-be9b-43d629b1c397 | -6.33883 | -46.03274 | 2026-10-10 05:04:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e76fb044-3ae7-3552-b15e-c3f715613848 | -3.63408 | -59.31923 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 48bc2e9f-22d3-38c5-a398-3e4aeffbdcf5 | -3.42981 | -54.54287 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 15d41e42-452e-3946-b369-12b3ef13ed1a | -2.37649 | -47.60927 | 2026-10-10 05:04:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47fb6cd0-3145-365c-bc12-43f07197d61f | -3.87314 | -52.25936 | 2026-10-10 05:04:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2cb570df-3f61-33af-a03a-fc701b04a77c | -3.10576 | -53.78253 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 27324f16-acde-397b-9646-c72f473ce62a | -8.21747 | -45.79965 | 2026-10-10 05:04:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b397748f-36c5-39d2-9f6e-1635d641f8dc | -3.52714 | -59.49322 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d3636cb-71e0-3744-9584-7f77485391a4 | -2.88999 | -56.67552 | 2026-10-10 05:04:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 131a9d8f-6b20-3de2-a8ab-f59588067a18 | -3.24703 | -54.66795 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c543cbbf-89f6-3a43-a6fd-34deeff787d7 | -0.97954 | -52.44595 | 2026-10-10 05:04:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5562d30d-25e1-3c84-911d-aeb27fc93520 | -4.13971 | -54.03098 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3107cc54-3e72-3eda-a01d-ca9c2ac2292e | -3.92407 | -55.85421 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa15e2b7-1337-32a4-9bc2-4d91e245f469 | -9.01014 | -44.37503 | 2026-10-10 05:04:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d6a1cec-3fb7-349f-8a06-443eac5ade2e | -5.7977 | -53.79536 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 24aee757-8ec3-3cf9-a091-5a1d3fc79a2c | -6.43664 | -55.27183 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5bc4e11e-49ee-3df5-84e2-84846cdafb29 | -3.01107 | -54.14201 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6edcc31e-3f8b-3d85-82d4-880d2b394445 | -3.28892 | -53.99858 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 404c0831-1362-3196-a351-65df749fcfc8 | -2.8554 | -54.1387 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 816d60ba-7dde-3a91-9cf8-55eb7fea0a67 | -5.7166 | -53.49051 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb319c33-6869-3e00-82df-d7996aa49151 | -2.87091 | -54.19078 | 2026-10-10 05:04:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 49b4d2c4-2985-3d73-902a-88e5ffb52c68 | -3.74381 | -50.00727 | 2026-10-10 05:04:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e590cce-f336-38c1-8c77-8f83bc7e8f01 | -1.63912 | -54.39329 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9138b2e4-56fe-3890-91f8-be6cc9a26f7e | -3.20568 | -50.56234 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 93b7fa62-3b2e-3af9-bdc4-c3ff35507131 | -7.23373 | -55.17341 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8e7af56-25c4-3fb7-8bab-8a4fefe0e41e | -3.10798 | -53.78992 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5ed94bc3-5ae6-386a-aaaa-eb81dc55e5e8 | -2.50235 | -56.06688 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 93783f87-d9b4-3fc0-b8fa-530e2ab1b493 | -2.563 | -57.42422 | 2026-10-10 05:04:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7315cde2-4ef4-3e67-a248-115a032e8b3e | -2.22517 | -51.91052 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 709bff22-6ec8-39db-aa80-a431f1655db8 | -3.32204 | -54.04614 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f06a053f-8940-39e0-95d7-d372a466a662 | -6.24383 | -53.31081 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9f910aec-0cf9-3b73-b18f-cc7118db26b5 | -3.9912 | -54.45327 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2cedd788-49ef-347c-83d2-8b41b047076f | -3.87397 | -52.30662 | 2026-10-10 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 321dae60-639c-3717-96f0-525423b001e2 | -4.72735 | -55.6548 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1bab501c-6d4a-311d-9241-8ef04d790614 | -3.18139 | -50.60067 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 971304a0-e5e6-34fc-bc0a-07aa0c7158b5 | -3.20138 | -53.86457 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c1b79ba-3760-3015-8bb6-c58b56753b88 | -3.83176 | -59.2972 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41030ccc-98da-3bc7-8b46-bd59d9666841 | -3.50117 | -54.2021 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b3ac8d40-aebd-3e73-bd56-d97e8a05da4b | -1.64191 | -54.39732 | 2026-10-10 05:04:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46b35222-4bb6-3605-bfa1-9a5c717af69b | -5.87623 | -43.40878 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9c62d87-a465-3e3b-83fa-b5c01262e118 | -3.78018 | -59.19605 | 2026-10-10 05:04:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1dcb9587-959b-3ba6-8712-46195b480a27 | -3.93581 | -55.71516 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 073f9bc5-8e75-3742-b8a1-6937e12eaabd | -3.31251 | -57.48872 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40c76fdb-f83d-3359-9431-cf529c59adcd | -2.41733 | -58.00027 | 2026-10-10 05:04:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24aa8cc7-b88e-358b-84fd-5b3e892f8bce | -2.89724 | -54.02497 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5bd42938-a7ef-3291-a1d5-93337356dccf | -2.93591 | -54.05933 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1ebcb283-42c2-3d73-bd3c-5cabe4759b7e | -4.28484 | -55.72475 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 793016ef-7165-3a7a-ab65-325e7e6fd4ee | -3.95196 | -56.1137 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 156c2130-2829-3e0a-945a-d8f26ba542ea | -3.54405 | -54.74323 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fe3da8bf-6bd2-37a4-9212-a4ad4cfe8a89 | -6.43695 | -52.6754 | 2026-10-10 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b01f55e0-ede0-37c8-b730-02d472de7b25 | -3.22174 | -54.29204 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c411a213-f864-394a-b8eb-887e7cabea90 | -2.82411 | -51.0388 | 2026-10-10 05:04:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b915e51c-538e-316c-b51e-0d5c3fded344 | -3.56745 | -54.6822 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 20fd7a5a-2480-32c9-90bc-9aea3513e0b6 | -5.06713 | -60.21957 | 2026-10-10 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d0cb4449-ab23-355e-ab3b-9e50c832702d | -3.00306 | -54.77003 | 2026-10-10 05:04:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cb0a6080-0cd5-327e-9c09-880bd55a08c6 | -3.02367 | -57.7854 | 2026-10-10 05:04:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4cbe5f2-cc40-3c20-bf13-d4acc8f32ca4 | -3.42586 | -59.58268 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de88925a-cb63-3ecd-b09b-82d777358856 | -1.20223 | -55.68255 | 2026-10-10 05:04:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8c27bf17-7284-32b7-8d5b-50f2a2998cbf | -3.52688 | -59.57431 | 2026-10-10 05:04:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ad8b265d-e5f6-3d3c-b03f-6bdcaee04279 | -3.84336 | -55.78862 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| a9288ad0-6a8e-3eb6-8352-0e338729bbe3 | -4.82678 | -56.08326 | 2026-10-10 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0c1d2e7e-246d-301b-a18c-86af29ac3845 | -6.49424 | -55.31343 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fdd69da-b53d-34ac-b62b-4f7307325f50 | -3.69511 | -55.48577 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9fa54beb-af85-359e-910b-2545733753a8 | -2.43997 | -55.98508 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e8a397e6-e1fb-357b-87c3-5c51d62fbcee | -3.95315 | -55.34753 | 2026-10-10 05:04:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d374eaa-6596-34e6-ad5d-fc9b57f56be0 | -4.36881 | -54.74834 | 2026-10-10 05:04:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0d58a0-7f2e-389a-bcd0-1cc4022b6744 | -1.09116 | -54.14168 | 2026-10-10 05:04:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47dc4b5f-b09b-3e92-b85a-27496a774ade | -5.88759 | -43.41479 | 2026-10-10 05:04:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f3a08113-c8e0-3a65-9483-6ef8ebca8591 | -5.97278 | -55.34575 | 2026-10-10 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac8357ff-9cd0-3c1e-b200-a0ffd63677ee | -2.93539 | -54.08401 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c6f96d60-f2d0-3d31-ad5e-c6afe282f1f4 | -2.73437 | -54.10866 | 2026-10-10 05:04:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ccd4ed35-cadd-3f5a-ae76-dc824828cdba | -2.49884 | -56.06633 | 2026-10-10 05:04:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ff8ee9fd-c0c7-3dd4-99a7-7584e857545d | -3.77413 | -58.52671 | 2026-10-10 05:04:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3895c04b-dbc7-32cf-bf3f-9702e10e6ac3 | -3.30436 | -54.00806 | 2026-10-10 05:04:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README122.md)
