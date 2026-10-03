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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ebcc4b7a-6659-3e1a-8bd9-8ecb294f140d | -3.2951 | -53.8395 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| cb80b602-c12a-3840-9174-2c204792c9da | -5.7376 | -45.1533 | 2026-10-03 02:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 93.4 |
| db78a4a4-5429-35fd-9915-c85ce07a0f7c | -5.9384 | -43.6482 | 2026-10-03 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| dbbc00e3-cb87-361c-a090-817bad6f7076 | -6.4933 | -58.5242 | 2026-10-03 02:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f8163780-d713-3f09-b448-dd590f67587f | 1.7854 | -55.5856 | 2026-10-03 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 0aacc3d4-e021-3ec9-b1af-88eb097a0a6e | -3.13 | -53.7229 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 109478f6-f3ca-3a84-8b2d-c91351251f57 | -3.2767 | -53.84 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 2eec1427-2689-3312-bf7a-22a4bd97f4ae | -3.1115 | -53.7637 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| cc17b8ce-1781-35c1-bef3-f2628bb6b3bd | -5.9571 | -43.6467 | 2026-10-03 02:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 0deff568-0b08-3f38-9dd5-4c3b387012cd | -3.1299 | -53.7431 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 172.6 |
| 28b92e83-cf45-3a84-9ee3-a2c1740b158b | -2.8897 | -54.1313 | 2026-10-03 02:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d52c3efc-f96d-349d-9936-71a8876642b7 | -3.1116 | -53.7436 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a5caaa45-89c9-35d1-a273-7597d308394e | -3.1483 | -53.7426 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 3a4b74a4-6375-30e1-b320-e2394b287776 | -3.1299 | -53.7633 | 2026-10-03 02:40:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| b3194eed-a4da-3d36-8f1e-0f043b7cbf3a | -10.9879 | -59.1393 | 2026-10-03 02:40:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 66.3 |
| f78c67ed-97c7-396b-b722-eacba62afda4 | -5.9381 | -43.6714 | 2026-10-03 02:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 46319fb4-6f8e-3f62-b045-73e90109779b | 1.8037 | -55.5854 | 2026-10-03 02:40:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| f8432b96-f4a4-36df-8b7b-f5f9ed4e9e71 | -4.4506 | -47.9329 | 2026-10-03 02:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| e263769d-1cb8-300d-b014-6f8160407f79 | 1.7854 | -55.5856 | 2026-10-03 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 1e29fc4a-bfac-33f6-a532-599ed14f9584 | -3.1299 | -53.7633 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 4903d038-0c70-37c9-a628-eb36bafc0f98 | -5.8597 | -53.479 | 2026-10-03 02:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3b676a0a-cd26-3f83-a5a8-9e71e95dc4da | -3.2767 | -53.84 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 17a72b38-469f-3926-8378-865c5813405e | -10.9879 | -59.1393 | 2026-10-03 02:50:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 9cf5b8db-1f40-3c60-8d0b-dfb5348ef7b9 | -3.1116 | -53.7436 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e10c9ac3-170c-38fe-8932-093b9eb9fc3d | -3.1483 | -53.7426 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 85d20d2b-9f19-3add-9c95-1a78b5eed3ce | -3.13 | -53.7229 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 8caedfe5-d1a8-381c-a161-ae572b6b219e | -5.9571 | -43.6467 | 2026-10-03 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 1f13ba99-3c1f-3a0c-a6c0-1a9acd4abf2e | -5.9384 | -43.6482 | 2026-10-03 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 104.0 |
| a1bb0c03-d614-3413-9ec8-e9cd431dabd8 | -5.7376 | -45.1533 | 2026-10-03 02:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.0 |
| face6f1f-e809-349f-b88e-52d626964434 | 1.8037 | -55.5854 | 2026-10-03 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 5b19c16c-f1ba-3ae6-b2a3-8a6f7ed6ec4c | 1.9132 | -55.8208 | 2026-10-03 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 347182d9-af89-32ff-be38-9e0fdb59341b | -3.2951 | -53.8395 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| bb40c4c6-cbed-3066-a7c6-6aace404275c | -5.9381 | -43.6714 | 2026-10-03 02:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 82.2 |
| aaab0ac4-de60-34dc-87d9-ed10ac2de92a | -3.1299 | -53.7431 | 2026-10-03 02:50:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 155.6 |
| 3823034a-493f-3645-b93b-5d7edd098dd6 | -5.9569 | -43.67 | 2026-10-03 02:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 89.1 |
| e2bc3b4f-e16e-37a4-8841-8b786f40bea5 | -3.1483 | -53.7426 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 31b2813b-8818-3ab6-af65-6b8ce6103f46 | -3.1116 | -53.7234 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 40.9 |
| daebcfae-5112-3304-bdcf-055a9f51bb95 | -11.7935 | -43.5215 | 2026-10-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 116.8 |
| 1197620e-07ef-3f7b-aec9-6f13309f5439 | -4.2676 | -50.7506 | 2026-10-03 03:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 6849e03a-4dfc-3e9c-9d4e-3077dd552253 | -9.7414 | -36.1043 | 2026-10-03 03:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 73.4 |
| ed0778ac-1dd6-37d7-b585-a9ac8767774c | -3.2767 | -53.84 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| c74f12b4-9e73-365e-a08a-3f33145d1f4f | 1.9132 | -55.8011 | 2026-10-03 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 1034ecb3-e0ae-3679-9617-d627bd2f7af2 | -5.9571 | -43.6467 | 2026-10-03 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| f9d52ce9-0f21-3ad9-9a4b-8f1e31e7d57f | -15.1248 | -43.6369 | 2026-10-03 03:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 70.0 |
| 945eff51-f25e-3468-afc2-c32d8a022543 | -3.2768 | -53.8199 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| a2dc31aa-b8bc-387c-965f-9e5ebe7c7a3d | -3.1299 | -53.7431 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 1e36a108-8459-30e5-b318-30f3fca2dcd7 | -3.1299 | -53.7633 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e59cf2ab-db46-3513-a951-270ca52ddc67 | 1.9132 | -55.8208 | 2026-10-03 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 8584f7c5-a8d1-36f3-88c0-e42b2de075dc | -3.13 | -53.7229 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| b67bc295-a29d-32d8-95ee-fe36a9dd0de6 | -5.9569 | -43.67 | 2026-10-03 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| f21549f2-3138-3aa2-ac08-046c225af65a | -15.1254 | -43.6128 | 2026-10-03 03:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 75.7 |
| 3b52eb72-d714-3041-8f24-1740c340d6e2 | -3.1116 | -53.7436 | 2026-10-03 03:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 6340feb3-9458-37ca-a07c-6da7eaeee3b8 | -5.9384 | -43.6482 | 2026-10-03 03:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 118.4 |
| dc568813-8040-322f-ac74-6e8e385fc198 | -5.7376 | -45.1533 | 2026-10-03 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| ff94f480-7866-3aeb-9fc4-b9b10edd9b7b | 1.8949 | -55.8013 | 2026-10-03 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 14002970-c4b1-3571-bf14-275cd1d9c2b4 | -11.8123 | -43.5422 | 2026-10-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 77.8 |
| cc45c037-656e-36ea-b2a7-a01e46998e87 | -11.793 | -43.5452 | 2026-10-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 129.4 |
| 6863ccf2-0438-3101-b03e-c8d2e2f2e29d | -10.9879 | -59.1393 | 2026-10-03 03:00:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| ee8431bd-5df8-35f1-b416-ccbff2c3e469 | -11.8127 | -43.5184 | 2026-10-03 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 5f7fa403-ce8c-32b0-a434-17f4e3c806c7 | 1.8949 | -55.8211 | 2026-10-03 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 40.1 |
| 88c7973c-b10d-36a5-b33c-d9d4533d513b | -5.9381 | -43.6714 | 2026-10-03 03:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 269fb314-4724-32a7-bfe3-7f91e120131e | -9.7221 | -36.1077 | 2026-10-03 03:00:00 | GOES-19 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| 8f978a52-bbb1-35e2-9d9c-69ce9ff5b00e | -9.72791 | -36.11199 | 2026-10-03 03:00:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 25.9 |
| 23725b4e-5b6f-3d51-a335-17aebed1ce63 | -9.73208 | -36.10767 | 2026-10-03 03:00:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| cb533695-3e5b-3022-bffb-e9da9a36f80c | -9.73125 | -36.11214 | 2026-10-03 03:00:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| c547b298-8a8f-3e9b-b1eb-f697ac847b4f | -9.72531 | -36.11087 | 2026-10-03 03:00:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 8f23e0ef-8426-362e-afc5-85c0fcca1403 | -9.72614 | -36.10644 | 2026-10-03 03:00:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 20.3 |
| 60b2dae1-6d85-345e-8f1a-756e1f027baa | -9.72877 | -36.10756 | 2026-10-03 03:00:00 | NOAA-21 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 43.2 |
| b7ee24c1-bf97-34c6-b167-1b908cf8f069 | -16.52346 | -40.54105 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3fc01014-35eb-3da0-b0c9-a4bdabc24a31 | -16.53034 | -40.54242 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 3aaea596-44f3-32a5-8186-e85b4151651b | -16.5488 | -40.52446 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f9c0791c-eacf-3c17-baa3-8a7f4a0a198f | -16.54128 | -40.55753 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 76e2cea9-4367-33d7-938b-934688fc1a1d | -16.54117 | -40.55843 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 1b85f1ed-3672-3c74-ad37-979091cd9be2 | -16.53489 | -40.5225 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 56d4c2a6-4f71-3b80-b4cb-f1178cc79a41 | -14.9413 | -39.27196 | 2026-10-03 03:02:00 | NOAA-21 | BUERAREMA | BAHIA | Brasil | 2904704 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a37e9e77-f253-3563-b367-15e9426e810b | -17.2476 | -39.43229 | 2026-10-03 03:02:00 | NOAA-21 | PRADO | BAHIA | Brasil | 2925501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 1fe9cd98-6ca2-3146-950e-ad2519ab36f2 | -16.54184 | -40.52352 | 2026-10-03 03:02:00 | NOAA-21 | RUBIM | MINAS GERAIS | Brasil | 3156601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 952d7bf0-62bb-3183-bd30-de58d96977bf | -3.1299 | -53.7431 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 126.0 |
| d22d0a57-367a-3950-86d5-1bf22bbaf5fc | -5.7376 | -45.1533 | 2026-10-03 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 61737156-a9df-36de-ba32-865ffe8888da | -11.793 | -43.5452 | 2026-10-03 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4d1b81de-d88c-3a42-bc5c-0f8ab98a9bbd | -3.1299 | -53.7633 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 19cf17f6-51df-3bab-99c9-1cecf266465a | -10.9879 | -59.1393 | 2026-10-03 03:10:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 9f564e73-9eec-3f2c-a771-bdd4de0d14df | -3.2767 | -53.84 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 18569b68-61a2-34a1-8bf0-c2136e73275f | -3.13 | -53.7229 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 9c62d86a-d492-3fbb-bd1a-4684bb33009c | -3.1116 | -53.7436 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 9c54c1c8-c4e7-3c8f-8113-daf21ebfaa00 | -3.1483 | -53.7426 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 53b111b3-3b25-3b2f-8585-dc142410a7da | -3.2951 | -53.8395 | 2026-10-03 03:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 061075b4-d15d-3595-a1e9-3ab83b20b75e | -10.9879 | -59.1393 | 2026-10-03 03:20:00 | GOES-19 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 091d2267-6e30-36e3-86f8-7607c7b8a568 | -3.1299 | -53.7633 | 2026-10-03 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| d95e6e29-42fc-31e6-a5f2-8aedaf5d76b5 | -3.13 | -53.7229 | 2026-10-03 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 30abc4bb-8fba-3b16-9a38-dcc3e6a641a8 | -5.9384 | -43.6482 | 2026-10-03 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 6670a511-ed96-3fe9-a03c-fd2f28a6238a | -3.1299 | -53.7431 | 2026-10-03 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 130.2 |
| 9c31397e-04f3-3701-829b-cda89c79defe | -3.1483 | -53.7426 | 2026-10-03 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 20bc9dca-d9a3-32e1-88ae-14ea0c797841 | -3.1116 | -53.7436 | 2026-10-03 03:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4e87f85e-4505-3048-adfb-09626b2963a1 | -5.9569 | -43.67 | 2026-10-03 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| ddfd8690-0434-35d2-bdd7-433c329d42a5 | -5.9571 | -43.6467 | 2026-10-03 03:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| b2eb5efe-f70b-39b4-a8eb-45fb3aa6e934 | -5.9381 | -43.6714 | 2026-10-03 03:20:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| bb71aab9-2b35-3474-86a1-4f522aebfe6a | -6.4933 | -58.5242 | 2026-10-03 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 2679c664-f8c7-3e31-b057-03ee3a7df673 | -5.7376 | -45.1533 | 2026-10-03 03:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 6be63f66-5544-39cb-bec1-96e9f48ed79f | -5.7563 | -45.152 | 2026-10-03 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |


[Clique aqui para ver as próximas entradas](README15.md)
