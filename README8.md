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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f082ccb9-730f-306a-92ae-98e48aa8e754 | 1.8766 | -55.8016 | 2026-10-05 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| f80c1ed7-da86-36dc-9361-98fa3b50bdf0 | -3.8448 | -50.3063 | 2026-10-05 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| efbfb3d4-85a6-332c-bdf7-349ba9726f0c | -2.6859 | -49.0325 | 2026-10-05 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 4d4376a4-1e4d-33b4-92b6-786405c40cf3 | -3.8447 | -50.3273 | 2026-10-05 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 21f2f28a-c7e3-3b71-a0d0-ea1bcd30e87c | -6.914 | -43.6816 | 2026-10-05 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 9f6cc861-b17f-3b9b-861c-a4de76317c69 | 1.7303 | -55.6456 | 2026-10-05 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 38b872f0-2b0d-3fff-b11f-d2be7656294a | -6.1781 | -52.9328 | 2026-10-05 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| ae74cb13-3ca4-3355-8e4f-af06f959fe70 | -3.0548 | -54.2277 | 2026-10-05 01:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 108.1 |
| 6c62b426-b5df-3e01-804e-1d4c6feca8c4 | -6.8952 | -43.6833 | 2026-10-05 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 74.7 |
| ee9c6750-5c1f-3d41-bfa3-7ec33bb91ddc | 3.1097 | -60.6133 | 2026-10-05 01:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 97.9 |
| d3e6e63a-397b-3839-8b3a-6b1811bab0a1 | -6.0067 | -53.634 | 2026-10-05 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 7e48247b-94b5-34d3-b258-5b6a0bad37e0 | -6.2529 | -52.847 | 2026-10-05 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 9694cc66-f601-35e8-a90b-5f5793edbbad | -5.9882 | -53.635 | 2026-10-05 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 8cdaf916-4f14-3c32-ab0a-d220265fe30e | -6.1974 | -52.8295 | 2026-10-05 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| c67a2a7e-25e7-3f42-9db0-ad962566df2d | -3.9859 | -55.8152 | 2026-10-05 01:50:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 9c6d1587-c88f-36aa-ba38-425fec547298 | -6.2159 | -52.8285 | 2026-10-05 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 4b67c92d-b956-3fb4-9993-218c51e868e2 | -7.4442 | -63.5589 | 2026-10-05 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 7ed122de-1190-3504-8fd8-ca5ac002ba2b | -7.4441 | -63.5777 | 2026-10-05 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f1e45442-a33a-3047-b406-b2ce33097bf8 | -6.2158 | -52.849 | 2026-10-05 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 6f0ca5ef-e820-30fc-8792-ad6c72724ca4 | -6.2527 | -52.8675 | 2026-10-05 01:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1e650cf2-6776-3d08-8d26-b8e1a8a95a3a | 1.8583 | -55.8018 | 2026-10-05 01:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 9d2cf907-bd89-3a9c-a8c6-4e9a498bb7a4 | 3.1042 | -60.604 | 2026-10-05 01:50:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0c9791a0-16dc-3671-8d16-24f0a4fff9c2 | -11.7676 | -62.722301 | 2026-10-05 01:50:00 | METOP-C | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7f95e9fa-93ac-33e2-a346-473ebc2fd9ea | -9.1296 | -68.219704 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5c7e7da7-87c5-3b7b-bcf5-53e6a53c18d4 | -7.4384 | -63.5476 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2929052f-f827-3807-aa96-8e031a99303f | -9.6721 | -66.827499 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b4d92e05-0877-338a-b549-55c5ea2a7d2e | -7.4539 | -63.569599 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ceb099c5-5ba1-3593-88d5-78bb76b9666c | -9.1351 | -65.915604 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dc976b0b-6fae-3f51-93d5-99e6ec5fe756 | -9.1477 | -68.254997 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2e0d2bcc-64f1-35cb-9bbc-7a8fc8cedb3a | -9.1494 | -68.262497 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82f73223-5e08-3061-8950-56b84a0727bd | -9.1104 | -65.3591 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46e64335-99ec-336a-9b78-b1eeb2c594ee | -12.8825 | -61.720699 | 2026-10-05 01:50:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1a6e4eab-1bb5-3a6b-950b-7b88adfccb9b | -9.1575 | -68.252899 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8eed67fd-7cd4-3506-8527-dea1f5353a08 | -7.4324 | -63.566101 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 11c354f3-6e3c-3add-beb7-983bbd06b15a | -7.4403 | -63.555698 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 97f2f29f-c7e5-3411-a58e-c3fe9fcabf34 | -9.1401 | -65.892601 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 406827e1-f672-39be-9779-ff78a1fb5d1b | -8.668 | -70.039803 | 2026-10-05 01:50:00 | METOP-C | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 49ec876d-2770-326c-a1f9-566da43b16bb | -9.1609 | -68.267899 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8a15c2d5-15bf-371b-9bc1-906a17789c5a | -9.1171 | -64.364502 | 2026-10-05 01:50:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7b2f2c89-7437-333e-89c1-27a87ef55648 | -8.621 | -69.498001 | 2026-10-05 01:50:00 | METOP-C | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 2a0ea91f-6a8d-39f8-b400-ec0da71b46b1 | 3.1139 | -60.606201 | 2026-10-05 01:50:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 3d9644ad-8503-39b0-9f25-63c24f25ebbf | -3.9785 | -55.8088 | 2026-10-05 01:50:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8278a3d-ff24-3652-b0dc-d65fd91cbdec | 3.1081 | -60.586399 | 2026-10-05 01:50:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d50160cf-a620-39fa-8a15-bebf6a1376b9 | -7.4501 | -63.553398 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1aa54ed1-27a7-3019-9877-83a7aafba060 | 3.1099 | -60.623699 | 2026-10-05 01:50:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 142c2a0f-590b-388c-a7ef-ec30f03c1656 | -9.3978 | -65.891899 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 71503e2c-0290-3f02-ad22-ae51fa3b35a2 | -9.1181 | -68.214401 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ea7de124-99ee-3ba8-a014-143c2624d772 | -9.1153 | -64.357101 | 2026-10-05 01:50:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87c8bbd9-c05b-3a20-9547-b3d3a8bcb045 | -7.452 | -63.561501 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff78769d-6e39-342d-b939-cf3ff7a0733b | -9.2209 | -68.167999 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf575c3-c791-34ec-b3a7-07183bcbc774 | -9.1433 | -65.906403 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b55705f6-9d9b-343f-8ac4-bfa11577aeca | -9.169 | -68.258202 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| e1f81f5b-f3c9-31b8-a32a-7edaf1682723 | -9.3994 | -65.898804 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0b16353c-ab4c-3d1c-95fb-6de421a05a5c | -10.2191 | -61.4398 | 2026-10-05 01:50:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec0b9d51-173d-3057-9c3c-4d41fc651b16 | -9.4076 | -65.889702 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7aaf2d2c-4bb0-332e-8461-8a7d2b0f5295 | -12.8803 | -61.711899 | 2026-10-05 01:50:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 66fc92ab-8c47-3c3d-98e3-4b0a6e031cfe | -9.1279 | -68.212196 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa348569-4660-342c-9844-b6db0ada0b75 | -9.1525 | -68.2304 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 080523f1-4ccf-3032-b73d-84385da2682d | -9.1673 | -68.250702 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cdb1ec5c-9040-3bd6-9126-a18e1d5b4825 | -2.5429 | -65.871002 | 2026-10-05 01:50:00 | METOP-C | FONTE BOA | AMAZONAS | Brasil | 1301605 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 583ef334-d2d0-3d17-83cd-832432a36481 | 0.4464 | -60.524399 | 2026-10-05 01:50:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| fe2cc0fa-97aa-3196-b60d-3e3096531d92 | -8.3522 | -62.828499 | 2026-10-05 01:50:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fcdac996-6f4b-3ec0-bbc4-b120b2cf2836 | -9.1511 | -68.269997 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 609f08d5-a79e-3490-ab47-ae1d7e74b876 | -7.4422 | -63.563801 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7dc877ef-ad2b-34a3-9aa5-d8f038af3398 | -9.1707 | -68.265701 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bdfa28ab-e39d-3405-8532-ce937d845a6c | -8.5176 | -67.007103 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4293110a-03b8-3a5d-8017-b0b75afcb143 | -9.1319 | -65.901802 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d35d4e47-dcc8-3da5-a7be-1b150ba004ac | -9.101 | -64.383698 | 2026-10-05 01:50:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 277331d9-9a9c-374b-86ef-3206363f24b2 | -9.1417 | -65.899498 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c2cc02d3-a783-3320-adce-729d58ca45bb | -7.4305 | -63.557999 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4ee6a471-9314-3009-a82f-09881c12defd | -9.1335 | -65.908699 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 49826dca-3796-3008-916f-574f0b9dc34b | -9.1542 | -68.2379 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 05ed5c7a-af29-3c8b-be55-49a97597aef6 | -11.9774 | -63.6119 | 2026-10-05 01:50:00 | METOP-C | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ccde6288-da60-32b4-8d2e-afbc1a882ff5 | -9.0332 | -67.557701 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3e6c9710-2da7-3dfe-95d7-2cb905b17175 | -7.4441 | -63.571899 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c4804de2-89c3-3432-a082-ab6955102487 | -9.0993 | -64.376404 | 2026-10-05 01:50:00 | METOP-C | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2f13e0d1-ee9a-3efc-a2c2-f62d28745efe | -9.1592 | -68.260399 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cf05646d-18b9-325f-ad65-ac9d8b975799 | -9.1262 | -68.204697 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9c306b27-11d9-3237-9885-a595e0248c47 | 3.1002 | -60.621498 | 2026-10-05 01:50:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| ff92e225-5479-36d6-a8f1-73cb03bbdfc0 | -9.4092 | -65.896599 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8c832705-a57a-3052-bd11-f7a4627c66c7 | -7.45 | -64.431801 | 2026-10-05 01:50:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 0fe7f00f-d412-3f9c-a186-4fb358f7b01f | -10.4783 | -68.6035 | 2026-10-05 01:50:00 | METOP-C | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| a7b1f576-46f1-3669-9c2f-bf6d6861bff6 | -10.2214 | -61.449501 | 2026-10-05 01:50:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba5cdb5d-db1a-32c9-b538-efc70760a01d | -9.0315 | -67.550499 | 2026-10-05 01:50:00 | METOP-C | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2a91705-4a63-3ef7-af32-8c9fbd4273e1 | -8.516 | -67.000099 | 2026-10-05 01:50:00 | METOP-C | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e7cf3fa-925e-364e-81f5-cce01874a7f6 | 0.4427 | -60.540501 | 2026-10-05 01:50:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e701e8da-811c-3940-8943-bfa380392c54 | -9.1334 | -65.9 | 2026-10-05 02:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 38.9 |
| 1412fcce-646b-3465-b306-e4a8696e3523 | -3.0548 | -54.2277 | 2026-10-05 02:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| f73625e5-dabd-34cc-92f6-350ba360ac8d | 3.1097 | -60.6133 | 2026-10-05 02:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 506f47f4-36eb-38db-9262-b224166765b5 | -6.0075 | -53.5122 | 2026-10-05 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| e4e31ab2-8d5b-397b-8770-c736b6482616 | -6.8952 | -43.6833 | 2026-10-05 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 603993d3-c3e8-3698-a4f2-d56c990dcdb6 | -3.9032 | -49.7137 | 2026-10-05 02:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 24bffb8b-e97f-33f9-bb7f-e09ca8b37313 | -3.9217 | -49.713 | 2026-10-05 02:00:00 | GOES-19 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 0e05c0f5-6eb0-3e8e-af4c-1c1f6c82cd0e | -6.2159 | -52.8285 | 2026-10-05 02:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 122.8 |
| 70aaf056-3b4e-3d27-b0d8-bdbb61101abb | -7.4442 | -63.5589 | 2026-10-05 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 100.0 |
| f3a4d182-9f85-39df-902d-cd27daff0f41 | -3.8447 | -50.3273 | 2026-10-05 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 4106e663-caf4-3b22-a2fc-49625b82f17b | -6.0067 | -53.634 | 2026-10-05 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 541b1154-c37c-31a0-881d-b2a949dfe071 | -5.9882 | -53.635 | 2026-10-05 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| e8bc3803-eaa5-3c3a-b002-f0ead4dc7107 | -3.9859 | -55.8152 | 2026-10-05 02:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 94.1 |
| dbde1deb-12f3-373b-ad3b-f5687d05bc76 | -3.8448 | -50.3063 | 2026-10-05 02:00:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |


[Clique aqui para ver as próximas entradas](README9.md)
