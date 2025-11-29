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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1edb5db3-8029-342d-b72b-a9c1c6b25af8 | -20.98192 | -48.63159 | 2025-11-29 05:08:00 | NOAA-20 | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6f85f46a-d339-37a6-82b6-a63be9cca0ed | -20.41649 | -47.22173 | 2025-11-29 05:08:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8a7306f2-b1a7-36fa-930e-7264227840ec | -16.67841 | -46.65329 | 2025-11-29 05:08:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dd13d175-5809-3667-8422-5e5d5393d36f | -17.61436 | -46.66258 | 2025-11-29 05:08:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 953c2282-c0f5-3665-a94a-88b20576977a | -8.1633 | -43.2055 | 2025-11-29 05:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| f92a3613-2d51-35b3-8769-3b3370d08658 | -20.1813 | -52.3754 | 2025-11-29 05:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 202.4 |
| 2e08e5c2-c87b-3238-9cdd-b7af32dd9509 | -2.7845 | -47.4343 | 2025-11-29 05:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| f4b97a4f-f90e-31f5-9d78-9eabb536323a | -2.7845 | -47.4125 | 2025-11-29 05:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b56b2c69-2ea0-3bd7-9b41-a0ec4f62adc5 | -20.2016 | -52.3717 | 2025-11-29 05:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 703f27b0-2feb-3472-8292-0031663dd37e | -20.1807 | -52.3975 | 2025-11-29 05:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 90.4 |
| f06de030-c806-3bcf-bde1-021982ce3faa | -28.00129 | -54.65652 | 2025-11-29 05:10:00 | NOAA-20 | CÂNDIDO GODÓI | RIO GRANDE DO SUL | Brasil | 4304309 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 71f1f5a8-5200-3baa-a7bf-9dda8c3348c1 | -2.6322 | -48.542 | 2025-11-29 05:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 66d22d86-8e09-3237-9221-7962ca543b07 | -8.1633 | -43.2055 | 2025-11-29 05:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 3ac14fca-ea71-3b0f-848a-f993fa44529c | -4.35018 | -43.16004 | 2025-11-29 05:29:00 | AQUA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| f40345fc-7726-3939-99ee-6ad72b63084c | -8.66828 | -44.21388 | 2025-11-29 05:29:00 | AQUA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.6 |
| bed7e768-ff18-3973-b4db-1fd7bcd57287 | -4.84835 | -38.73716 | 2025-11-29 05:29:00 | AQUA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 9dd97a0c-04f0-3aac-98e3-76807e7bccef | -3.17077 | -45.22502 | 2025-11-29 05:29:00 | AQUA_M-M | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e7bbe479-1688-3988-862c-59b2cd9bf833 | -4.99947 | -38.53886 | 2025-11-29 05:29:00 | AQUA_M-M | IBICUITINGA | CEARÁ | Brasil | 2305332 | 23 | 33 | nan | nan | nan | Caatinga | 12.6 |
| 4f17b1c7-95ab-3db8-bece-8dd70169a9ed | -9.96166 | -42.3246 | 2025-11-29 05:29:00 | AQUA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ec4650ee-7dff-38d6-8d39-30efc0b67635 | -4.62538 | -43.97753 | 2025-11-29 05:29:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3aa81d69-8c1b-3f79-b85a-79f2a47998a5 | -4.93338 | -37.9959 | 2025-11-29 05:29:00 | AQUA_M-M | RUSSAS | CEARÁ | Brasil | 2311801 | 23 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 55adef0b-a0bb-3cdb-9f23-a30ae1890076 | -8.1633 | -43.2055 | 2025-11-29 05:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.7 |
| 49948121-a9aa-3633-afc7-5b2f49dc80cd | -2.6322 | -48.542 | 2025-11-29 05:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.0 |
| f44a7c7d-8886-356f-96fb-3508beaba618 | -17.60464 | -46.65728 | 2025-11-29 05:31:00 | AQUA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 486505d3-bc84-3da8-9681-433825a3a57d | -2.6526 | -48.0244 | 2025-11-29 05:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 0589a7e2-c10d-3e56-9741-36cc6c1a1658 | 0.45981 | -60.43482 | 2025-11-29 05:52:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 86232c98-0160-3fae-a69a-215b7a555fca | 0.61646 | -59.63962 | 2025-11-29 05:52:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8901e7c7-25d0-301b-8086-8075098b18c0 | -9.41463 | -66.66518 | 2025-11-29 05:57:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 34101ba5-2489-3e49-9f89-3d657fde7203 | -9.84299 | -67.38676 | 2025-11-29 05:57:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dd93cab5-6546-34fe-ac50-5901bb72e22f | -9.41405 | -66.66908 | 2025-11-29 05:57:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc7b507a-aa91-33f9-a6d6-ef7c52460788 | -4.4538 | -44.5763 | 2025-11-29 06:00:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 74.4 |
| d1496572-2da7-3395-a8bc-221e4fda441f | -2.6526 | -48.0244 | 2025-11-29 06:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 46.0 |
| c2474b02-7e52-30cf-bd7f-7ed4b519028c | -4.4725 | -44.5752 | 2025-11-29 06:00:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 194.8 |
| 2de4fd67-c8a1-3e56-86e2-20c7f6c1155b | -4.4723 | -44.598 | 2025-11-29 06:00:00 | GOES-19 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 53.0 |
| 9dcd5227-6436-39b0-9d5c-dc83f9dfd40c | -4.4726 | -44.5524 | 2025-11-29 06:00:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| c0fdf815-808d-3dba-a9c8-84b2875080b1 | -2.7845 | -47.4343 | 2025-11-29 06:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fd27c90d-ee7f-3897-8725-edf6cabbfc2e | -2.6526 | -48.0244 | 2025-11-29 06:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 7140fe8b-f1c6-3d5d-ad8d-a38b1b42e20a | -4.4725 | -44.5752 | 2025-11-29 06:10:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 62.5 |
| adb2c001-6eee-3500-ae0a-b7c6d7ed0da2 | -2.6322 | -48.542 | 2025-11-29 06:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| d5015c89-97af-3e27-a80c-197183b39438 | -2.7845 | -47.4343 | 2025-11-29 06:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 58b8a449-a89e-36e2-96c8-5bd333d72b85 | -2.7845 | -47.4125 | 2025-11-29 06:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 1c361469-c932-3078-b2fa-6526a7473ac0 | -2.7845 | -47.4343 | 2025-11-29 06:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| f3eb0336-0d8f-35c9-8ab6-b9e5a43ada21 | -2.6322 | -48.542 | 2025-11-29 06:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 8ed23252-4554-363a-b79a-bd3aa0974146 | -2.7845 | -47.4125 | 2025-11-29 06:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 9a897bce-4b07-3c99-a3bf-8139b8be8a41 | -2.7845 | -47.4125 | 2025-11-29 06:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 1dec27ba-c3d8-3dba-b330-a46e36092876 | -2.6322 | -48.542 | 2025-11-29 06:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| dfcfe01c-9554-3e48-8696-a66cb1b98aea | -2.6322 | -48.542 | 2025-11-29 07:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c781a575-bd31-3e01-80e7-314f9ccff994 | 1.28692 | -60.43573 | 2025-11-29 07:05:00 | AQUA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 830248d2-5db1-3266-9c93-ec0a6bb74e0d | 0.46265 | -60.43353 | 2025-11-29 07:05:00 | AQUA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 89778dcc-47c8-3ee6-acc8-450dffa4813d | -2.7845 | -47.4343 | 2025-11-29 07:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 50.6 |
| b80b56b2-62b3-37fd-bed9-8b2491ab24e5 | -2.6322 | -48.542 | 2025-11-29 07:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 717d3206-4c56-3dc3-9dcb-2535cfdda8b9 | -2.7845 | -47.4343 | 2025-11-29 07:20:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 49.8 |
| b21fadec-36ce-382f-a17d-4a2a20588077 | -4.0221 | -42.1114 | 2025-11-29 07:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 50.2 |
| 3c478e46-1bb8-35f7-b747-6b127433ec90 | -2.7845 | -47.4343 | 2025-11-29 07:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 8b2963d2-1d1f-3092-812b-d425bbfb1582 | -4.0221 | -42.1114 | 2025-11-29 07:40:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 58.9 |
| 1caa2094-577b-30e8-aec0-ebeb4320de8d | -3.4138 | -43.9186 | 2025-11-29 07:40:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 74a1ab2d-7b1b-3308-bccf-c0fc956d7199 | -3.4138 | -43.9186 | 2025-11-29 07:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 78e665b9-68eb-332c-bcf5-0c9da2c8804e | -3.221 | -45.2249 | 2025-11-29 07:50:00 | GOES-19 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 51.2 |
| b63f6b07-3d89-3278-a13d-b3e5c4619ca8 | -20.1813 | -52.3754 | 2025-11-29 08:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 359bb5df-ea2b-371c-8bd5-1488497eb48b | -2.848 | -45.5086 | 2025-11-29 09:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 142.6 |
| 0266f541-8eb6-3daf-bd98-50b09bdf06a7 | -2.848 | -45.5086 | 2025-11-29 09:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 146.6 |
| 6ae53973-ba15-387a-86f3-c6a5a601050f | -2.8481 | -45.4862 | 2025-11-29 09:50:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| ff49f200-83eb-3fac-9bc6-574329dbaf85 | -2.848 | -45.5086 | 2025-11-29 09:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 217.2 |
| 4f72c8e1-8f30-3064-8201-c6687927144d | -2.848 | -45.5086 | 2025-11-29 10:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 268.4 |
| fd6349fa-0de8-3704-adf5-88bacd5bc477 | -2.8481 | -45.4862 | 2025-11-29 10:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 127.5 |
| 927c2499-9593-3d2c-9d79-ea2cef847b4e | -20.1813 | -52.3754 | 2025-11-29 10:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 116.0 |
| d05903e2-c149-3088-95e8-03618d6ca29b | -2.848 | -45.5086 | 2025-11-29 10:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 250.2 |
| 60c20a15-c4a0-3d92-bcd1-69c3af52f48d | -20.1813 | -52.3754 | 2025-11-29 10:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 122.2 |
| d6054a0a-3705-35a9-8ebc-fc068592345c | -2.8481 | -45.4862 | 2025-11-29 10:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 1d65964b-43dc-3d8b-9bf1-b05f39b46188 | -2.8666 | -45.508 | 2025-11-29 10:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 6797c221-c39e-304b-b9c4-071709d328ec | -2.848 | -45.5086 | 2025-11-29 10:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 304.8 |
| d48f7729-cf8a-33ec-b111-2272a92cb4c6 | -2.8481 | -45.4862 | 2025-11-29 10:20:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 149.5 |
| ce4ac633-61bb-34ae-8774-2ab85861d1c3 | -20.1813 | -52.3754 | 2025-11-29 10:20:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 130.7 |
| 8a7d54b2-10fe-36f8-a0ee-bda5f34ab48e | -20.1813 | -52.3754 | 2025-11-29 10:30:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d43c8e2f-e98f-3dd3-a1e7-76bb1129764c | -2.848 | -45.5086 | 2025-11-29 10:30:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 462.5 |
| a94f80fb-0ef0-3507-99fe-fa5ce43378bb | -2.8666 | -45.508 | 2025-11-29 10:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 138.4 |
| 3101b93b-8b6f-3eca-be8c-64c60226bfa9 | -2.8481 | -45.4862 | 2025-11-29 10:30:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 192.2 |
| 564e0fad-4c9e-33d1-8b0f-d56844e160dd | -2.8666 | -45.508 | 2025-11-29 10:40:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 226.2 |
| 545f52d2-d834-39c7-b168-7e2dce167180 | -2.8481 | -45.4862 | 2025-11-29 10:40:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 142.4 |
| c7c9ddc1-15ed-3e00-a8a1-a8db66913d7d | -2.8667 | -45.4855 | 2025-11-29 10:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 3397eb86-3f73-3e0e-9ecd-b27f76b40fa6 | -2.848 | -45.5086 | 2025-11-29 10:40:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 292.7 |
| f9aa4613-f02d-3cea-9bd8-fa0bf01e783f | -20.1813 | -52.3754 | 2025-11-29 10:50:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 119.0 |
| 4d439fb0-9107-306e-96fb-0f711660754a | -2.8481 | -45.4862 | 2025-11-29 10:50:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 147.9 |
| cee5ef66-01a8-3bd9-afcb-0d1beeaca490 | -2.8666 | -45.508 | 2025-11-29 10:50:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 167.1 |
| d76cc141-7387-3940-8d84-89533c25e4a7 | -2.848 | -45.5086 | 2025-11-29 10:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 386.4 |
| bfecf31d-35c7-3d1c-bdec-7e8b77631cc7 | -2.8666 | -45.508 | 2025-11-29 11:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 161.7 |
| fc761fb4-08be-3465-812e-548db27f6966 | -20.1813 | -52.3754 | 2025-11-29 11:00:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 511553c1-9e2a-3ce9-8b48-eadd03fd0340 | -2.848 | -45.5086 | 2025-11-29 11:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 487.7 |
| 2435e442-9dde-3829-9616-8215437df182 | -20.1813 | -52.3754 | 2025-11-29 11:10:00 | GOES-19 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 16d0f0c4-62a7-3815-9d02-4350a1475f56 | -2.8666 | -45.508 | 2025-11-29 11:10:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 229.9 |
| 003888ec-095b-32a2-ab48-a83b88d72e2f | -2.848 | -45.5086 | 2025-11-29 11:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 659.6 |
| cabdd3da-ef6b-3c8f-bf8f-f6c3da2ba846 | -6.7373 | -37.17244 | 2025-11-29 11:17:00 | TERRA_M-M | SÃO JOÃO DO SABUGI | RIO GRANDE DO NORTE | Brasil | 2412104 | 24 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5fa4b974-6ac0-37bf-af6f-e3a278d58569 | -7.6497 | -37.80479 | 2025-11-29 11:19:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 70.5 |
| 476d6491-577b-3be5-8fc7-36a9ccf75134 | -7.26019 | -37.89539 | 2025-11-29 11:19:00 | TERRA_M-M | PIANCÓ | PARAÍBA | Brasil | 2511301 | 25 | 33 | nan | nan | nan | Caatinga | 9.5 |
| d59479d4-3e62-3022-ad62-47ff2e09b3e3 | -7.56067 | -38.69984 | 2025-11-29 11:19:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 13.8 |
| 32ff093c-bc93-3647-90e4-d9a94aff4e8c | -7.65357 | -37.81124 | 2025-11-29 11:19:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 102.2 |
| 047c52cf-559d-3853-acf4-50a374f6ef86 | -9.33827 | -35.74703 | 2025-11-29 11:19:00 | TERRA_M-M | FLEXEIRAS | ALAGOAS | Brasil | 2702801 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 183370a9-1565-32c0-b0d8-89e5575bc67d | -7.64775 | -37.81785 | 2025-11-29 11:19:00 | TERRA_M-M | QUIXABA | PERNAMBUCO | Brasil | 2611533 | 26 | 33 | nan | nan | nan | Caatinga | 49.7 |
| 55815ffe-8c31-384f-86fd-97f34a6d9f12 | -7.79573 | -37.23328 | 2025-11-29 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 31.3 |
| 82597d22-be8c-336a-801b-17c0e4a7f379 | -7.83138 | -37.39719 | 2025-11-29 11:19:00 | TERRA_M-M | IGUARACY | PERNAMBUCO | Brasil | 2606903 | 26 | 33 | nan | nan | nan | Caatinga | 15.6 |


[Clique aqui para ver as próximas entradas](README31.md)
