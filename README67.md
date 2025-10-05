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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05d3c911-8dae-3d09-bfd9-f20c07564689 | -11.91382 | -46.2468 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0e3cad26-4e4c-3b40-a132-ef6342566e63 | -12.89973 | -47.31966 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 12dbef2f-f4b4-3f37-879b-f9d1ed589657 | -14.58463 | -52.45398 | 2025-10-05 03:55:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| aaa437de-388d-3c3d-9a44-11de0f6f15d7 | -13.38619 | -47.5648 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bcd836e3-2dae-36ba-81d6-989c00ae4615 | -11.53251 | -47.67957 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 10ad1a1c-e424-3b20-807e-fd737fec9197 | -11.24416 | -47.78436 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90186a59-5022-3258-bb10-d6ea02a5b6cc | -12.39688 | -44.82862 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 369090ec-0578-3b08-ad16-d73ea6695dc9 | -15.98327 | -50.90623 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3ce2c1f8-e1f9-3818-989d-4c67cc7d5cd5 | -16.97489 | -47.26609 | 2025-10-05 03:55:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| de1b1237-e0ce-31fe-b996-764e6723bae3 | -13.25046 | -47.23074 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 59721981-c77e-3851-bd21-5bda26832097 | -15.3423 | -47.33502 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 658aec60-0ccd-374b-aa66-036438686e40 | -14.91758 | -46.87352 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0d69f7fa-a030-3ebf-a041-fab4bdf7311b | -13.16715 | -50.87729 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 211da9da-33cf-3ad9-80a9-92d04628204e | -15.35385 | -47.96886 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d7fdae76-29ab-3a1b-be69-7078e6ea3f1f | -11.81635 | -45.05546 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0d3d084c-8c97-3fac-b0a5-7c8ae177cc03 | -14.94528 | -46.84744 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9591806b-a10e-31b7-b8e4-4746795a5434 | -15.29822 | -46.318 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0263a4d7-1b07-34f3-8c8b-15b1292e880c | -13.27907 | -47.61011 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 611c81e0-ea87-32a2-86fe-a15a5cda7f47 | -11.81645 | -45.07868 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0f51a30-0284-3f48-b2cd-edf202a8d0d3 | -11.23502 | -47.80539 | 2025-10-05 03:55:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3b20f809-1210-3b09-802f-e4c49268d051 | -12.12492 | -50.91782 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26206dbf-225a-3dea-bef8-97b92820544d | -17.01965 | -43.4486 | 2025-10-05 03:55:00 | NOAA-20 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f863a106-ed9b-3d7c-aa41-e615cbef7c0a | -13.25386 | -48.48047 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 16826cc1-71dd-3beb-9ed4-d457b412d3ed | -11.81094 | -48.8817 | 2025-10-05 03:55:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| def80e43-1448-3209-93e8-2f1f779f167a | -13.29598 | -47.62296 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f2e32059-9778-3b09-9b4a-6604cb251623 | -12.81838 | -46.85559 | 2025-10-05 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0fc13e2b-3731-3728-8320-c1efded95a8d | -13.08228 | -47.89426 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 004a75c4-8a9a-3b31-a3d4-20c99f460efb | -13.30469 | -48.08652 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b12a156a-54fb-3fe8-b2bf-2c70041b16b0 | -13.11967 | -43.84729 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 0bff0349-eaad-3666-9354-1b1f112a3991 | -13.29486 | -47.57723 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef02a85d-62ac-33f1-863a-3edd0223e456 | -11.09796 | -47.74116 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 78853939-61ea-38e1-8bb4-410a87ee7dfe | -13.44566 | -47.2708 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 36fcbd96-72f4-3e8a-94b3-8cf12cb6cf00 | -11.12054 | -47.17556 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 532faaff-e2ae-3ce1-8e07-1122b5ea3acc | -13.70171 | -47.35876 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43fc33e0-7fb0-3fff-a4db-f842cfb77f8c | -12.59297 | -48.16 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 978c39e7-6913-39ef-8b1f-cd9ede57a950 | -14.88747 | -48.26479 | 2025-10-05 03:55:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5f521a8e-86e0-3eb7-8b05-3829b8448892 | -13.24374 | -48.47839 | 2025-10-05 03:55:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb1fb023-321b-38a9-a180-36c10a9ff48b | -13.25551 | -47.20314 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5adf9fad-3a89-384f-9fd2-e2069533802d | -11.62288 | -47.74656 | 2025-10-05 03:55:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d0556194-1885-31fd-aa0c-1e27ac6a1b2c | -11.40364 | -47.16772 | 2025-10-05 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd97ddbc-6acc-3168-b91b-40f15d3f6522 | -15.76513 | -46.26696 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 006223df-e3df-3447-9d6f-688f0caf9d70 | -11.83015 | -45.07401 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4593511f-6f3a-34e2-931e-4b418453c09d | -15.81147 | -46.25085 | 2025-10-05 03:55:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c52cdf4d-ec3c-39ae-91fe-0fe85b3e5728 | -11.67503 | -47.49025 | 2025-10-05 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1deea173-4054-3639-83fb-52459656a0e2 | -15.50505 | -46.8581 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d236974e-258f-36c8-aed8-1fd58ba85c63 | -11.64721 | -42.76817 | 2025-10-05 03:55:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 479a16a2-b2b0-318f-97e0-d4acf39cec1c | -12.29293 | -45.35386 | 2025-10-05 03:55:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c7429900-09ba-3634-9d1d-3787ec4e0801 | -13.73565 | -51.27841 | 2025-10-05 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0e010c27-83af-3f39-aaaa-31daf67efe42 | -13.15649 | -47.96736 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cc86b785-e97d-31d1-8932-b2b31b25a9b4 | -14.68838 | -48.30295 | 2025-10-05 03:55:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94655ea3-be83-3b45-8296-ac5682e950d7 | -13.08423 | -47.91082 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 08572c85-9118-3f24-94d6-1f6726548d17 | -15.97749 | -50.86476 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2e93c5a4-a8cb-31bb-9a1d-5d53033707e3 | -10.57765 | -48.68894 | 2025-10-05 03:55:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9326afaa-6cad-3410-83ef-aaf4a1e38422 | -10.45965 | -47.8131 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 84d95fc0-71db-3753-9308-9edc244f2100 | -13.51628 | -47.29242 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3ff73e68-e977-3a50-ada7-4310ff689ee2 | -13.25741 | -47.20524 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07971182-e24c-391b-a7a7-3d678a5fe99e | -14.95174 | -46.85662 | 2025-10-05 03:55:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1dd1e6a8-e5f1-3d9d-8b0c-d55121353cb7 | -13.09433 | -47.83058 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| db9eb9ea-15d3-3a26-ab51-ebbaa25205b4 | -13.302 | -47.56646 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b449e7d-7d4a-3b82-ad40-69613aaf04ae | -16.39563 | -52.15324 | 2025-10-05 03:55:00 | NOAA-20 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f12380bb-e363-3dae-b208-74e83467fbbc | -11.91879 | -46.25599 | 2025-10-05 03:55:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17fdee8a-49d2-35ce-bd46-c0b0a680c69e | -13.07538 | -47.9039 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| d0a6bf1c-9a32-3e80-9c1a-54b01d55fa1c | -12.46587 | -45.53168 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ba9ba67-6a28-332b-b57d-bfafdbb7610e | -11.5741 | -46.77246 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c4f440bd-07f3-3d1c-a2a3-89004396986f | -12.59179 | -48.13878 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9c0d9f97-639e-326a-ad4e-0e7913379168 | -13.26745 | -47.61921 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 06898498-85d0-3656-b2c9-060616eac26a | -11.49374 | -46.78889 | 2025-10-05 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb7c5b93-dbb1-3fe2-9464-050305b9e6e9 | -11.12845 | -47.9086 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| addb07f5-28b2-3754-83ad-f2c44cebca3a | -13.3044 | -47.81427 | 2025-10-05 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d6bfe599-e501-304d-8f9d-a6d9931ad042 | -15.30105 | -47.32529 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bdd5338d-f50e-3a7e-90c0-29923479b36e | -17.95048 | -47.02378 | 2025-10-05 03:55:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4a5141d0-8076-3a79-8293-f6d69ec5f949 | -11.07232 | -47.87197 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d6416b19-ebab-34a0-a869-47357bd01c82 | -13.85693 | -43.98865 | 2025-10-05 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 588ae716-a958-39d0-9588-966bbb86fb03 | -11.82405 | -45.08416 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6e9476ca-ef66-3079-867f-9a7b7bcea527 | -15.52531 | -46.8709 | 2025-10-05 03:55:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b773cb45-f9ba-3b58-bf2c-b1cb7bb43013 | -13.32041 | -47.17814 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ece62e65-32e6-3b6a-a3af-94f3e8ef02b3 | -10.73395 | -47.90032 | 2025-10-05 03:55:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f19717b1-1de4-3e4e-aaf7-fe00cf515018 | -15.29717 | -47.95781 | 2025-10-05 03:55:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 840ddb17-0511-3112-a191-ef58c84609c9 | -13.27709 | -47.61788 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 199ff79d-ad32-3746-a765-d7c0a9096aa1 | -13.44839 | -47.26789 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 41a6e7c4-b027-37e7-9394-b8863346f763 | -12.46239 | -45.50199 | 2025-10-05 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 387fc888-3d82-3eb5-aa13-667d272dcb51 | -16.75614 | -43.97026 | 2025-10-05 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f5cf0eed-4bb4-32b1-ab4e-daa86ac4062d | -11.48633 | -45.02796 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2bce25c-be80-3e3f-b4c9-cb23ba038ca9 | -13.26082 | -47.22698 | 2025-10-05 03:55:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5c80035e-5f56-3dd7-8d62-a1a2bebeac29 | -13.11858 | -44.07761 | 2025-10-05 03:55:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d6869a83-821c-328d-ba9b-d710c8b0267f | -13.29907 | -48.11532 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8669c98b-a71a-3f20-bb51-7eda4349665a | -11.10024 | -47.75262 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 53cea77a-f07a-3829-bf89-6f04e38a70f2 | -11.14592 | -47.92778 | 2025-10-05 03:55:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9a51cf34-4936-310c-9d0c-cc15d5a1e9a6 | -16.00563 | -50.85632 | 2025-10-05 03:55:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7a2670d9-1bb9-3072-bf3a-b44124859f3d | -15.35754 | -47.97514 | 2025-10-05 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 42257cbc-bab3-30b7-91af-c651bbc1ef6f | -13.30185 | -48.12741 | 2025-10-05 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 121566b0-d2cb-3ea8-8159-18aca273310d | -15.12955 | -45.73941 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 57ecfc33-39db-3388-8ed1-c1a2c3f76a5d | -13.8242 | -48.06755 | 2025-10-05 03:55:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 136ad765-aa58-30f6-b6cd-0f0dae3fbe52 | -12.41113 | -51.10303 | 2025-10-05 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 48e42f88-881c-345d-b285-09de804bd18f | -15.14115 | -45.7456 | 2025-10-05 03:55:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 671fdfda-2e74-33bc-aace-5248605010b7 | -11.81825 | -45.04488 | 2025-10-05 03:55:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a9da774d-2d12-3be7-a6b3-77337507cb10 | -14.33748 | -52.973 | 2025-10-05 03:55:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 75b5611e-3415-365b-8526-c53e5c923fd9 | -13.6777 | -43.18677 | 2025-10-05 03:55:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| aa23fefc-e1ef-37c2-a5f7-5598c50f696f | -11.00201 | -46.52306 | 2025-10-05 03:55:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5c6440b8-ba8a-314e-ae9c-9b1dc40689bf | -13.648 | -47.29848 | 2025-10-05 03:55:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README68.md)
