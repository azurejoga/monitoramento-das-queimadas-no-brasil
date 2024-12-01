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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fd97ede9-e7f7-3b39-bd21-96d635cd2c4e | -1.50794 | -52.62988 | 2024-12-01 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0caa0fc8-829e-3707-8820-948a45d74f81 | -2.9861 | -45.57933 | 2024-12-01 05:08:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 22.2 |
| dfb94828-8d3d-3e43-b71c-8cf549979be8 | -2.53314 | -54.04135 | 2024-12-01 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea5ba638-b096-3ff0-8031-900e856bd1fb | -4.49488 | -49.63829 | 2024-12-01 05:08:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 893858b9-ab28-335f-8713-a0e9fc18c8be | -3.27047 | -50.56599 | 2024-12-01 05:08:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 39829bf2-444d-3a0f-be40-1ca8dc1b1764 | -4.26018 | -50.84334 | 2024-12-01 05:08:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f18468f7-f0c7-34d7-b2cc-1af3e9232e65 | -5.66419 | -49.7578 | 2024-12-01 05:08:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0c1218b-8642-3290-a389-2803d2e8eed9 | -3.259 | -53.6388 | 2024-12-01 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e7b6d684-8134-3b2c-ad83-356dadaa7339 | -2.8196 | -53.0629 | 2024-12-01 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| a6626647-5a05-32fd-b9bf-ceaf364cd836 | -2.8197 | -53.0425 | 2024-12-01 05:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d53d2b73-562e-3878-8019-be1259169020 | -4.5562 | -43.3028 | 2024-12-01 05:10:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 164.3 |
| b214f4a4-6b70-3af2-9f97-a57dee32c217 | -3.2591 | -53.6186 | 2024-12-01 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9b9428fd-4b6c-3f8c-b927-67cc1f85509b | -3.146 | -45.3629 | 2024-12-01 05:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 355e655c-7b05-3c79-b558-30944c7cb41d | -3.2774 | -53.6383 | 2024-12-01 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 088254a1-6240-3aac-ba92-df48e77d6a3a | -3.4974 | -53.8339 | 2024-12-01 05:10:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b55339aa-fcfe-3798-a4aa-905f40bb2bc6 | 1.1438 | -56.0067 | 2024-12-01 05:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3df46835-e7b1-34fb-ae0c-b2c530aaed6d | 1.1439 | -55.9871 | 2024-12-01 05:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 4b481cc5-9946-3c19-b219-d88026359181 | -4.5578 | -45.7232 | 2024-12-01 05:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d93d9e1d-0581-3257-8600-a4209edc46f5 | -10.6674 | -44.4835 | 2024-12-01 05:10:00 | GOES-16 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| ef7c3078-d408-33e8-ae17-f295ef788504 | -3.1459 | -45.3854 | 2024-12-01 05:10:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |
| bf80cd00-833e-37db-99f2-b4bc7819d4f2 | 1.1622 | -55.9869 | 2024-12-01 05:10:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6227334c-d8c2-37f9-838c-1105e3bb71f6 | -9.16994 | -62.38309 | 2024-12-01 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7b1bb22f-6ec5-3aab-b0bc-969bc1c9f84b | -15.5409 | -60.10908 | 2024-12-01 05:10:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 97c8da8a-8a3d-3b31-9121-deb94a34f2fb | -10.6607 | -44.49154 | 2024-12-01 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e6b4a2a5-8ddd-3ba1-b0d4-910764eda997 | -10.88285 | -54.31858 | 2024-12-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db4c86dc-f0d3-334a-a9a5-0730def3bd10 | -10.65361 | -44.49069 | 2024-12-01 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a42af73d-222b-3ad4-937f-c8553d133394 | -10.65988 | -44.49857 | 2024-12-01 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 46caafe5-1821-3444-bc59-a77065f33331 | -10.60672 | -52.82003 | 2024-12-01 05:10:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8c124c3f-db5f-3bf7-ad81-a6936311f9f1 | -12.22184 | -64.35899 | 2024-12-01 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 427db660-3147-3011-a5cc-58f98226d3a8 | -12.24671 | -52.68455 | 2024-12-01 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53be525c-5dd3-360a-925b-e020b0c1e86c | -10.60516 | -52.81911 | 2024-12-01 05:10:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f7096101-4652-3fd2-a57c-db25ae496826 | -9.07334 | -63.58162 | 2024-12-01 05:10:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4ce6940d-ec47-3eb1-a915-d92971710ab3 | -10.65279 | -44.49773 | 2024-12-01 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b834e34e-9d56-3d6f-a036-7e02529929d2 | -2.8013 | -53.043 | 2024-12-01 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 337c3b15-0d7c-369c-b818-e3095440702e | 1.1438 | -56.0067 | 2024-12-01 05:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 44788b27-3bbf-3d0e-ad3a-1ed0113a6ead | -3.1273 | -54.5264 | 2024-12-01 05:20:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| a5533b54-b833-3d5b-b0bf-fe7efea470f3 | -3.1459 | -45.3854 | 2024-12-01 05:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 77.2 |
| faa8cd4c-7267-3813-954d-133c64b0ab3c | -4.5562 | -43.3028 | 2024-12-01 05:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 118.8 |
| 1e7b17f0-cb3b-318d-b3a8-016421e944e7 | -3.2774 | -53.6383 | 2024-12-01 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| d38ad192-c210-350f-a0ad-881758ffb4bd | -3.1645 | -45.3622 | 2024-12-01 05:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 315f9e03-2bd9-3c86-98ef-19cbf9078e37 | 1.1439 | -55.9871 | 2024-12-01 05:20:00 | GOES-16 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6bc48fd1-0004-3e8c-85ff-f3cb37fbbf76 | -3.2591 | -53.6186 | 2024-12-01 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 17e9d513-e236-343c-b2f5-bce5b6f9d351 | -2.8197 | -53.0425 | 2024-12-01 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| aad41932-b166-380c-ba59-631dc3ba9a09 | -3.259 | -53.6388 | 2024-12-01 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 7b778f69-faef-3f29-97d1-7d386fcda78a | -3.146 | -45.3629 | 2024-12-01 05:20:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 66186ada-00e2-3a74-bc50-611370053b92 | -3.4974 | -53.8339 | 2024-12-01 05:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| c49a82cd-7b1d-393d-aaa9-e6061b965747 | -4.5375 | -43.304 | 2024-12-01 05:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 79059488-c9f4-3190-8c90-f684b42400db | -2.8196 | -53.0629 | 2024-12-01 05:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f7d3f394-083c-3a29-8525-b7dbea9e44ea | -4.5578 | -45.7232 | 2024-12-01 05:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 23e536f9-455d-3e63-91b5-e24c43923528 | -4.17789 | -48.62599 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 5d2bddcf-d037-3429-9e3e-0c5669c81144 | -4.5426 | -43.30426 | 2024-12-01 05:25:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| faf34001-1933-32fa-8f5f-88f64080cd9c | -3.21064 | -53.1179 | 2024-12-01 05:25:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 20a47e13-9971-3e62-8d2f-edd42907571a | -3.02944 | -51.53432 | 2024-12-01 05:25:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| a8db7e6f-2869-30f6-a87e-02d36603bad8 | -2.74363 | -51.75676 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 05dcb7bc-cd3d-34cd-93d1-dfc93a579b51 | -2.28474 | -45.59704 | 2024-12-01 05:25:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 41.6 |
| 2b087682-3d4e-3eea-8c27-f6e373990ffe | -3.99197 | -46.64867 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 5fa267ad-c763-3874-8bd8-a724914cb1c1 | -2.83398 | -46.85757 | 2024-12-01 05:25:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 38b0890e-e4b3-3879-8f92-456cddf894cb | -2.67916 | -46.59885 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 66947c60-6df1-3c6c-a2d9-0b7cb9e95b9d | -5.58281 | -45.20884 | 2024-12-01 05:25:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 58b6e86c-9e0d-3dd5-aacf-10fb182c8cdf | -3.98441 | -46.63844 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 1550d0bc-1fb0-3669-b055-964e9abed6c0 | -4.18122 | -48.60469 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 61353602-9602-365a-83ed-debad4ffa13e | -4.55223 | -43.30562 | 2024-12-01 05:25:00 | AQUA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 129.6 |
| 83f0b14a-4bef-3ca1-a8d2-445d9e9465df | -2.62721 | -54.19767 | 2024-12-01 05:25:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| ae36aea4-bfc3-3394-a134-78a8a27a38fe | -3.12382 | -45.97906 | 2024-12-01 05:25:00 | AQUA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 94ffdf07-d061-387c-ade7-a613867f71d3 | -4.17658 | -48.60914 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| b136c115-097b-3c23-be3c-1ee9936b91ae | -3.13738 | -54.5094 | 2024-12-01 05:25:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 41.3 |
| a7c5e75b-ec44-3553-85a9-03ffa5e492bd | -2.51006 | -51.82663 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 75ebf1bc-0c61-3b16-a387-b1390bfc4c1d | -4.00417 | -46.9335 | 2024-12-01 05:25:00 | AQUA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 116d1d3f-6891-3a2d-8769-81b280baecba | -1.70307 | -46.1494 | 2024-12-01 05:25:00 | AQUA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f0859408-de94-384e-afe2-ae240fd91714 | -4.17498 | -48.61978 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| bc9e1d83-819f-34ef-85c6-4712ad579def | -3.1409 | -45.36552 | 2024-12-01 05:25:00 | AQUA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.0 |
| c4adaec3-78b7-3fe2-a68a-1e01ac833a13 | -3.20699 | -53.10991 | 2024-12-01 05:25:00 | AQUA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| f628b863-9e3c-3d0a-a7ac-8c9aebc2931a | -4.04883 | -46.81969 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 03b154d4-7fc5-3492-a3ea-acea43a00e7e | -4.2552 | -50.83577 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 92f058a2-b4c5-370c-ba48-8e847d9a0cce | -3.3156 | -50.13539 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 22d9a19f-efbd-3dc7-9524-9fa27aeb3405 | -6.71458 | -47.27284 | 2024-12-01 05:25:00 | AQUA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 4eba786c-7d60-3983-888f-f556e77d4d84 | -2.66365 | -51.85536 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 483e3a73-5708-3dc4-9180-7bc984701d72 | -2.7532 | -46.10735 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5d5b958e-7164-3e9f-891e-e2952996ea8c | -2.68391 | -51.72123 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| b16bf697-a087-37aa-9ec3-6027e3eb869f | -3.46744 | -50.27113 | 2024-12-01 05:25:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 70ee55f8-fddb-3af7-bfed-91f7a83d1f8d | -2.4631 | -46.56395 | 2024-12-01 05:25:00 | AQUA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 48f10234-8ea1-37d7-a178-d532d124c41d | -3.49192 | -53.83619 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 74db0dc7-aab6-3103-9d0a-169aa9513fad | -2.75187 | -46.1162 | 2024-12-01 05:25:00 | AQUA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3df6f821-0928-3337-a611-7f3694f79336 | -4.5419 | -45.6959 | 2024-12-01 05:25:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 2af1bc24-3702-3a4c-a1a9-852a44459f7c | -2.29357 | -45.59832 | 2024-12-01 05:25:00 | AQUA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ceb7f273-a359-3d7a-b2fe-cf222e5c5ebd | -1.00576 | -51.71538 | 2024-12-01 05:25:00 | AQUA_M-M | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 173ed680-caa0-3f48-9b70-afb6add1daf0 | -4.89479 | -41.31476 | 2024-12-01 05:25:00 | AQUA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 223ff5f8-1d99-3f62-9c5a-dd089ae3af2b | -4.40066 | -49.7606 | 2024-12-01 05:25:00 | AQUA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 72218dfc-0bee-325b-b542-c45bfbf7ce62 | -1.70442 | -46.14047 | 2024-12-01 05:25:00 | AQUA_M-M | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e94fa130-66ca-3f39-8639-4d70b23d7f77 | -3.30757 | -50.02863 | 2024-12-01 05:25:00 | AQUA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ba97be33-e0a7-3303-96bd-ddbf16e32b54 | -3.26776 | -53.61767 | 2024-12-01 05:25:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| f0e946ad-3672-3bf1-9d8d-aa236589a40a | -3.45722 | -44.92287 | 2024-12-01 05:25:00 | AQUA_M-M | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3d12e9cb-74bc-300e-8748-e17c0ffa1bb5 | -3.4559 | -44.93182 | 2024-12-01 05:25:00 | AQUA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 446c24e0-ae0a-3dd2-ae85-08e19d46f766 | -4.17337 | -48.6305 | 2024-12-01 05:25:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2d3de36b-1e2f-3f27-a5c8-f940dfb300f7 | -2.60833 | -46.5734 | 2024-12-01 05:25:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f553a88-f848-3f6d-b47d-37513a12482a | -4.06915 | -46.68488 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5f8a3e4-495b-351b-9361-c1d4e47e2f6a | -4.53306 | -45.69461 | 2024-12-01 05:25:00 | AQUA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| db40aa37-e90e-3799-bd51-ae4ca1ac08be | -3.84434 | -46.52309 | 2024-12-01 05:25:00 | AQUA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9173366a-643d-313f-b0e6-37750a9ad68b | -3.85336 | -40.97038 | 2024-12-01 05:25:00 | AQUA_M-M | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 10.1 |
| b27845a0-6a65-3d22-8f06-ce684ca2bc14 | -3.69557 | -51.79285 | 2024-12-01 05:25:00 | AQUA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README98.md)
