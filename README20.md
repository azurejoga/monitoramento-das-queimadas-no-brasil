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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 09564d40-addf-3dd6-841b-1762390e726c | -2.82 | -52.9409 | 2024-11-07 02:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 44534ce3-5fa6-34da-8d46-154561572a12 | -5.0154 | -46.8531 | 2024-11-07 02:10:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 50.2 |
| e298bb6d-0b9b-31e5-9510-aff2654d8b7a | -1.2014 | -53.8983 | 2024-11-07 02:10:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 7c6a7fe4-4989-3aa5-b526-144c94def390 | -2.6044 | -51.3043 | 2024-11-07 02:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.3 |
| 9b762270-6175-37ff-aecc-793c8c0cca3a | -5.034 | -46.8521 | 2024-11-07 02:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b1c36762-c4a9-3229-8adb-1b893be007ed | -4.522 | -42.8608 | 2024-11-07 02:20:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 1554e354-5a0b-38d1-838b-b6d6823ef40f | -11.8446 | -43.8674 | 2024-11-07 02:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| fa2022d5-2246-3eda-878a-bdb6c8aec176 | -2.8537 | -48.6642 | 2024-11-07 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 99.9 |
| 85f8ca53-5555-3e8d-970a-18bbac008a27 | -1.1831 | -53.8985 | 2024-11-07 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 165c1dec-ee4c-3f7f-9b99-95f027cc303d | -1.2014 | -53.8983 | 2024-11-07 02:20:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 29ae8a07-2fce-396d-afe7-95d29e9e4e82 | -2.82 | -52.9613 | 2024-11-07 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 81fbd348-aa1e-3518-a3a6-d11cbae36c6b | -3.7033 | -48.9986 | 2024-11-07 02:20:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 062a5a9d-84e3-3226-9abe-08a5485151a9 | -2.8536 | -48.6856 | 2024-11-07 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 62d1435b-9e68-3262-b447-bb4c42e2d19a | -11.8442 | -43.891 | 2024-11-07 02:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| e813e076-7893-3775-83fa-b20cf541368f | -3.0023 | -53.4434 | 2024-11-07 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 05f85f35-133c-3a82-8d2d-ca2ef582b1f1 | -3.0207 | -53.443 | 2024-11-07 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| f364f044-73cb-392a-b789-7704c19f1758 | -2.82 | -52.9409 | 2024-11-07 02:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 90c50002-126b-356b-b447-e4ec93418859 | -5.1395 | -47.7008 | 2024-11-07 02:20:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 29184736-a4f4-3010-95c1-703a40951bee | -2.5009 | -49.1228 | 2024-11-07 02:20:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 381fafb5-af62-3209-bc31-3f77864dd149 | -4.5033 | -42.862 | 2024-11-07 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 542882da-1ab6-37b8-a758-61a56be1b6d3 | -2.8352 | -48.6648 | 2024-11-07 02:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 39.5 |
| f64adcd6-4968-38da-b366-0000ab7d13a0 | -4.5218 | -42.8843 | 2024-11-07 02:20:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| b1588826-5add-3194-b78a-8f75ea75666a | -1.1466 | -53.7177 | 2024-11-07 02:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 2b3bc1b7-6501-3500-9054-1f5401f3ae91 | -11.8639 | -43.8644 | 2024-11-07 02:20:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 2ffb8b6c-db01-3a4f-af0b-220cf6a37f0e | -5.0342 | -46.83 | 2024-11-07 02:20:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f0a21052-e2b4-350c-acea-1a479a0d3abf | -5.1581 | -47.6997 | 2024-11-07 02:20:00 | GOES-16 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 41.4 |
| 78369a19-43db-3494-a2ab-1d0c453d334f | -3.5864 | -50.2317 | 2024-11-07 02:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 9107fa59-f8ed-35b3-a1ee-8f9fcaf9e68d | -3.1617 | -50.2038 | 2024-11-07 02:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 1716e0e5-e63b-38c8-a52f-93a7b50c8546 | -2.8352 | -48.6648 | 2024-11-07 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 40d55f5a-6e2f-3cab-8bc6-28993977b566 | -2.82 | -52.9409 | 2024-11-07 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| a2994bff-20cf-3b76-b8f0-86e889038ba0 | -4.5033 | -42.862 | 2024-11-07 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 53df1b79-6f3e-3f08-bdbe-515595aef78e | -3.7218 | -48.9979 | 2024-11-07 02:30:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| 29b98b3f-758f-327b-81cb-abd2cbc39407 | -2.8351 | -48.6862 | 2024-11-07 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 33459c7c-9b26-3b79-87b2-69a3fd1abdde | -5.034 | -46.8521 | 2024-11-07 02:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 409a98c9-0feb-3ef8-9a7c-cce9799c1581 | -3.6602 | -50.2501 | 2024-11-07 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| f1852049-b497-34cb-8aa6-5215f286b9f2 | -5.9975 | -45.3607 | 2024-11-07 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 24db6b1a-f3d1-341f-99d9-7947aa9c5cd3 | -4.5218 | -42.8843 | 2024-11-07 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 39fb11c2-a630-338f-9d5b-1d5bbb25ee1f | -3.0207 | -53.443 | 2024-11-07 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 4e88d476-c25b-3566-bfce-3cfa334e07b6 | -3.4564 | -50.3832 | 2024-11-07 02:30:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 5ef0376f-2b5e-3a50-9b40-42e270172445 | -2.6044 | -51.3043 | 2024-11-07 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 3d82cfa8-35d7-3bf6-9b14-c1fb0605578f | -5.0342 | -46.83 | 2024-11-07 02:30:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 7cd29143-39ab-394d-84c0-961086d52df0 | -5.9788 | -45.3621 | 2024-11-07 02:30:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 157.4 |
| 06d38654-498d-3626-8e1f-4275963017c5 | -1.2014 | -53.8983 | 2024-11-07 02:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| e27e1133-afeb-34cf-ae34-939bc50b7ab5 | -4.522 | -42.8608 | 2024-11-07 02:30:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 64.7 |
| ac78c267-37c8-3c0c-911c-3abebb83bf28 | -11.8639 | -43.8644 | 2024-11-07 02:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 73.6 |
| ad375588-d2ae-3cc8-99e3-33166087abec | -2.8537 | -48.6642 | 2024-11-07 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 96.2 |
| d97230b5-7398-3e9f-8beb-7e1ef817eeaf | -2.6228 | -51.3038 | 2024-11-07 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| d329b3e0-65fe-30a2-98ca-8e8e9183bcda | -11.8446 | -43.8674 | 2024-11-07 02:30:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 87.1 |
| e991afe5-2c11-3791-b4fe-313b3139f218 | -2.8536 | -48.6856 | 2024-11-07 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| 2cb5c477-7a8e-3263-bb0a-7000b984f81b | -2.7639 | -53.2265 | 2024-11-07 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 64d101c5-1ca4-34be-adbf-230f3d3df971 | -2.82 | -52.9613 | 2024-11-07 02:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 7d0039f4-864d-38f7-bdc7-ac54c4d8a7e5 | -2.8722 | -48.6636 | 2024-11-07 02:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| acc61b21-ac64-3c71-8aef-9e39ee6a843b | -1.1831 | -53.8985 | 2024-11-07 02:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| f98a633b-0e6a-3bea-87cb-721af3e50f11 | -3.1617 | -50.2038 | 2024-11-07 02:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d8a88324-44c4-3335-ae44-7e2b5de73598 | -4.5031 | -42.8854 | 2024-11-07 02:30:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| 050dae41-9c6e-3285-b032-8172fcbe652e | -1.1466 | -53.7177 | 2024-11-07 02:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a5d284d1-1777-35b5-80d4-db506cca7e84 | -1.1831 | -53.8985 | 2024-11-07 02:40:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 75.2 |
| fc947912-3a8d-3254-9e82-dc01b8663296 | -2.5009 | -49.1228 | 2024-11-07 02:40:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 7963afe9-7222-3bf8-b4c0-982eedbd21dc | -4.5033 | -42.862 | 2024-11-07 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 14479ac7-a756-354e-9d1a-3b568a303e03 | -2.8537 | -48.6642 | 2024-11-07 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 14eee73c-2715-397f-9196-24f25e00c290 | -3.0207 | -53.443 | 2024-11-07 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 7752f22a-1d07-359f-b704-2b3f3e68ec01 | -4.522 | -42.8608 | 2024-11-07 02:40:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 84.9 |
| b3f92324-fc43-3355-98f4-1152a4de9374 | -3.6787 | -50.2494 | 2024-11-07 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 9c993e5d-fc1a-3a5b-8c58-5907fbabf64c | -2.6229 | -51.2831 | 2024-11-07 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 37.3 |
| 6f18b26a-3685-35b1-80d1-2e4b14fb461c | -5.034 | -46.8521 | 2024-11-07 02:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 6c211757-5750-377d-83fb-a0b8460b139c | -2.8536 | -48.6856 | 2024-11-07 02:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| a011f93e-3ae7-3540-8807-05b2d57b0d34 | -2.82 | -52.9409 | 2024-11-07 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 781cf417-0d1d-3f35-92bb-cafc55134a21 | -2.82 | -52.9613 | 2024-11-07 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 1379b5a5-fab3-3016-bfee-f03895445685 | -3.0396 | -53.2805 | 2024-11-07 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 9de15ee1-4401-3829-9324-6224acb3a21a | -3.0023 | -53.4434 | 2024-11-07 02:40:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d40c205a-da86-39d1-a395-572538fddd58 | -3.1617 | -50.2038 | 2024-11-07 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 5d302048-e07a-3f53-870b-9d0422a5601d | -4.5218 | -42.8843 | 2024-11-07 02:40:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.7 |
| efdaefbc-1fc3-3a04-a042-325a1edd0ad6 | -3.7033 | -48.9986 | 2024-11-07 02:40:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 3b7854d5-2f53-3187-b313-5efa0ed40033 | -2.6228 | -51.3038 | 2024-11-07 02:40:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 75.4 |
| b981464e-aa23-3f6c-9686-b694003e4182 | -11.8446 | -43.8674 | 2024-11-07 02:40:00 | GOES-16 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9050bb4d-8f45-31bc-8909-0c8b1b1905f4 | -3.6602 | -50.2501 | 2024-11-07 02:40:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 72.8 |
| c43a2a6a-1276-3c2d-a037-5f0f8aa483a1 | -5.0342 | -46.83 | 2024-11-07 02:40:00 | GOES-16 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 4bbcadce-5e48-3fba-b7c1-f88d00d99b85 | -3.0207 | -53.443 | 2024-11-07 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 10cb4a0c-a7ca-374b-8bbe-0cb360ad3147 | -4.5031 | -42.8854 | 2024-11-07 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 60.8 |
| f2aa0a20-81ef-3706-bf68-d743f43f43fc | -3.9669 | -48.1716 | 2024-11-07 02:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 58f6e21a-d006-378e-af54-088bbeeeab9e | -5.9975 | -45.3607 | 2024-11-07 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 52725e4f-ca00-399f-acf3-b487f6607bb3 | -3.6787 | -50.2494 | 2024-11-07 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| c7e7a5f4-37b2-3d64-ab9b-787bf1e7e971 | -2.6228 | -51.3038 | 2024-11-07 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| b0b04973-39f5-3040-94a5-bf8ca5da5752 | -2.8536 | -48.6856 | 2024-11-07 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 103.6 |
| 36692ac8-d3b9-37c4-afdf-0c96502920eb | -2.82 | -52.9409 | 2024-11-07 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 408ff55a-7f9d-3df4-97ec-bd19071133d3 | -2.8537 | -48.6642 | 2024-11-07 02:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 115.2 |
| 0181aa9e-4bd3-3fcc-b7a8-2858cd92a109 | -2.82 | -52.9613 | 2024-11-07 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| c2a97622-18ba-3e29-8197-e16ac14a6dbb | -3.7218 | -48.9979 | 2024-11-07 02:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 9444bcf6-2703-3875-8e2e-a5437e2d59c4 | -4.522 | -42.8608 | 2024-11-07 02:50:00 | GOES-16 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 5d23b83d-2e6e-39e2-a893-40357f7c2cf6 | -1.1831 | -53.8985 | 2024-11-07 02:50:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| 35dd5ef4-ccc4-3183-bb14-e011daf9aeb6 | -3.1617 | -50.2038 | 2024-11-07 02:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| efbcc169-caf5-373b-b4c7-5cf6954ad842 | -3.0023 | -53.4434 | 2024-11-07 02:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 54b925f6-5de0-38cb-9a41-0d3fc3654576 | -4.5218 | -42.8843 | 2024-11-07 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.0 |
| c036efb7-a71f-3dc7-a69e-d65c7951d873 | -3.6602 | -50.2501 | 2024-11-07 02:50:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| ab5dce1b-cbc8-311d-bb84-6b525865cf1a | -5.9788 | -45.3621 | 2024-11-07 02:50:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 129.7 |
| cd46b42e-60f3-35b9-910e-374053b19ef6 | -1.1466 | -53.7177 | 2024-11-07 02:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 7480fed6-a1d7-3a9c-9bc2-2a754b4ca195 | -3.7033 | -48.9986 | 2024-11-07 02:50:00 | GOES-16 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 487964ba-945e-3ed4-8e7c-da9adbf8901e | -4.5033 | -42.862 | 2024-11-07 02:50:00 | GOES-16 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| ef41c79d-2b9d-36b6-b4dc-3cfa04477d0f | -2.82 | -52.9613 | 2024-11-07 03:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| aa229328-2db7-3652-a0fd-777fb5b92ef9 | -2.8537 | -48.6642 | 2024-11-07 03:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 133.2 |


[Clique aqui para ver as próximas entradas](README21.md)
