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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 871d06cd-21c7-3eee-8b12-301cf854b431 | -1.3451 | -53.093399 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7186e35-b6df-3256-93a5-8c3b5150abb0 | -3.8351 | -50.1805 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5652e867-e9aa-3117-bb35-ecfd9841cc0c | -3.2267 | -50.1315 | 2025-11-27 01:08:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 327c3f26-a9b5-3f5c-adb0-fbc05032ad7a | -3.3126 | -50.059898 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2fa0417-e53e-39a3-8c59-5e3bfedac398 | -2.7423 | -54.588299 | 2025-11-27 01:08:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93ad4564-1545-3a6b-8236-0b3e3e16dab0 | -3.8295 | -50.1567 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d222fc8-103d-3e56-9a81-0cacec0fd189 | -3.8807 | -54.201698 | 2025-11-27 01:08:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e67521e8-6bb7-326f-92a8-149c9eb8ff16 | -2.9328 | -48.205299 | 2025-11-27 01:08:00 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 14f0a6ab-e467-3930-bfd6-844d0f5cc84a | -1.3431 | -53.084801 | 2025-11-27 01:08:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe4850cc-7198-3367-be17-7f4c967c5512 | -3.053 | -54.548599 | 2025-11-27 01:08:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da43d660-048c-3e53-b26c-67b22e5c68e2 | -2.808 | -45.776699 | 2025-11-27 01:08:00 | METOP-C | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ea8188e3-65c4-3ea8-bf32-cfef2fa4f68e | -3.0546 | -54.555801 | 2025-11-27 01:08:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8532132a-3dc4-3783-8c6e-7baf5f7744b0 | -3.8323 | -50.168598 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56fdf506-63d3-3a37-97a7-b28f5071e0c7 | -3.7764 | -50.757999 | 2025-11-27 01:08:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b24b889-95c6-319b-b57d-6ce551fe692e | -20.4076 | -57.9577 | 2025-11-27 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.4 |
| a7314897-ab62-3e8a-8b59-02ca1dcb71dc | -8.0321 | -43.1257 | 2025-11-27 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 130.1 |
| a475cc16-41ea-3ee8-a2f3-3a2a95a64d5b | -4.7018 | -46.4508 | 2025-11-27 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 79.5 |
| ab66c2e0-7cb1-3492-8711-a33c2ed8976a | -5.703 | -47.0532 | 2025-11-27 01:10:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| dcde0d0d-d237-3daa-86f7-dfa80410f62c | -3.8269 | -50.1809 | 2025-11-27 01:10:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 91.6 |
| 549ab59d-d5dd-3ad9-ae19-15eafd5c5b72 | -8.0318 | -43.1493 | 2025-11-27 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 174.1 |
| 0efd7254-2f23-3cbd-babe-998768936122 | -4.7203 | -46.4719 | 2025-11-27 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 903a7824-5959-3a42-bd5b-42b07228cf32 | -8.051 | -43.1237 | 2025-11-27 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 2846b6e7-3665-3a03-8de6-6fd44f773bb3 | -3.5269 | -43.6828 | 2025-11-27 01:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| db4158a9-1cc2-38fd-94dc-9bb2ea34189a | -3.2195 | -45.5398 | 2025-11-27 01:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 5424fff6-00d3-3c22-922f-b5864398720a | -3.5083 | -43.6837 | 2025-11-27 01:10:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ea0d49ce-bef2-3a8c-bee6-32dc3edaf7db | -1.3494 | -53.0891 | 2025-11-27 01:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| f447f6e9-6100-3278-87d8-9417f3f95426 | -20.408 | -57.9368 | 2025-11-27 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 6a66d104-2e4d-3f55-af52-e0074d0e7b0c | -4.5749 | -43.3017 | 2025-11-27 01:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3e1e7d1a-d898-3a26-a5e9-4680132479ba | -1.3494 | -53.1094 | 2025-11-27 01:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 72a4a4f9-ba15-30eb-9497-8c8085b24149 | -8.1633 | -43.2055 | 2025-11-27 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 1f907192-d329-3995-ac30-316d567f71e7 | -8.0507 | -43.1472 | 2025-11-27 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| a5a36694-b653-3a27-b5da-650b54427c2e | -4.7204 | -46.4497 | 2025-11-27 01:10:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 151.2 |
| adad68bf-dc20-3a14-abab-1f34fd664ff4 | -3.5269 | -43.6828 | 2025-11-27 01:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 6bc274eb-ae62-3761-a8f1-da7b507a54a7 | -8.051 | -43.1237 | 2025-11-27 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 144.0 |
| aec8b45c-ffbd-3d1e-9e8a-be3b4ec425bf | -7.5116 | -45.7099 | 2025-11-27 01:20:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 51.5 |
| dc2187c9-5ab1-3218-85be-3c837a7a5259 | -8.0318 | -43.1493 | 2025-11-27 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 208.6 |
| cf8f4dfa-b6bb-31d5-bdb9-1b6781f79378 | -3.8269 | -50.1809 | 2025-11-27 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 10d8a79e-ea3f-3e07-98be-80239258d3ae | -8.0321 | -43.1257 | 2025-11-27 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 188.6 |
| e4abb2fd-9b16-3357-93e2-f58ee140e7a0 | -3.5083 | -43.6837 | 2025-11-27 01:20:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 55.3 |
| 06c6d8ec-c897-3b21-8f1a-02d9bd1dc565 | -1.3494 | -53.1094 | 2025-11-27 01:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 3262a012-93fc-3442-bbae-1cc6198f1cc1 | -3.827 | -50.1598 | 2025-11-27 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 0d580961-d6ce-3d8f-a4e4-8333016f82a6 | -8.1633 | -43.2055 | 2025-11-27 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.6 |
| e5b46b31-3367-37ad-820f-b287dea521d5 | -4.7017 | -46.4729 | 2025-11-27 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 48.0 |
| db6d22f1-8d0b-3a34-a103-5b42af81d21e | -4.7204 | -46.4497 | 2025-11-27 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 139.0 |
| dde65ab6-d356-3f44-992f-7edff15502ff | -5.703 | -47.0532 | 2025-11-27 01:20:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 3f4ceeb1-2e0c-3e40-9a84-a1e9526677b0 | -1.3494 | -53.0891 | 2025-11-27 01:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 81a8bc74-e797-35f7-a1bb-6a27771adb07 | -4.5749 | -43.3017 | 2025-11-27 01:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 77.2 |
| 7516f5a0-bf27-3792-85e4-39997e76375d | -3.8084 | -50.1816 | 2025-11-27 01:20:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 47.3 |
| dc9eeea3-107e-3a9b-8dd8-826c7491d610 | -3.2195 | -45.5398 | 2025-11-27 01:20:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| ed1d7ef8-6898-34d1-841d-bc1891975806 | -4.7018 | -46.4508 | 2025-11-27 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.2 |
| f6a13708-e811-30cf-94f1-f35b4f13cf9a | -8.0507 | -43.1472 | 2025-11-27 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| 4dbbe9ee-29b4-30af-a735-518b6f8c5138 | -4.7203 | -46.4719 | 2025-11-27 01:20:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 77.4 |
| cf1927a8-55ba-3902-9be1-e4c31ca15d0f | -1.3678 | -53.0889 | 2025-11-27 01:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 48.3 |
| 70098cb8-18b4-3f8f-8131-9f4ef8c408c4 | -2.7588 | -49.3285 | 2025-11-27 01:30:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| ea5d7d63-83fc-3329-bd73-9cc374c91285 | -8.0321 | -43.1257 | 2025-11-27 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 232.8 |
| 56193967-932b-356e-a373-bd2592d84196 | -1.3494 | -53.0891 | 2025-11-27 01:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| e33229a3-3291-36f7-bf40-d39bcff78358 | -3.8269 | -50.1809 | 2025-11-27 01:30:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 115.3 |
| 59a600b1-a1a1-3eab-b5b4-d835692d31d4 | -1.3494 | -53.1094 | 2025-11-27 01:30:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6f0710ac-fd8b-3eaf-b112-ae3885959694 | -8.0507 | -43.1472 | 2025-11-27 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 207.1 |
| 8d1d5c3b-212a-3654-bae6-4ba4854af4f8 | -4.7203 | -46.4719 | 2025-11-27 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fa901577-ced7-3c40-bae1-97552826025d | -9.5691 | -42.9421 | 2025-11-27 01:30:00 | GOES-19 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 78.9 |
| dca041c4-ab4f-3619-9a23-0be83485a351 | -5.703 | -47.0532 | 2025-11-27 01:30:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 0c998f59-84a0-3a90-8bf8-b3d11eacf072 | -8.1633 | -43.2055 | 2025-11-27 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.5 |
| 71bc537b-abc9-36bf-9586-bb9c3b562c30 | -8.0318 | -43.1493 | 2025-11-27 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 240.1 |
| 6fc01d24-621a-3f34-aa40-69ee8e82b4a3 | -4.7018 | -46.4508 | 2025-11-27 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 5b6bb59a-1f14-3a42-adfe-2b0ee98a8180 | -8.051 | -43.1237 | 2025-11-27 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 210.5 |
| 7c2b0d8a-29fd-319f-8ade-7e6717c28c61 | -4.7204 | -46.4497 | 2025-11-27 01:30:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 126.0 |
| f4c2e065-4b41-3329-99a9-db9369331427 | -4.7018 | -46.4508 | 2025-11-27 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 931dac01-127f-3b67-8373-2a7b699af745 | -8.0321 | -43.1257 | 2025-11-27 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 180.8 |
| a3f2464f-abed-3e98-83df-854910b3208d | -9.9731 | -36.0634 | 2025-11-27 01:40:00 | GOES-19 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 74.0 |
| e436232f-a4d0-3389-85e6-fa2552ae3181 | -1.3494 | -53.0891 | 2025-11-27 01:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 62.0 |
| d4c206bf-8072-3cc7-9e86-7adeb355a4d7 | -3.8269 | -50.1809 | 2025-11-27 01:40:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 89a69a29-2d02-3b7e-8d33-346d58f93a7b | -8.051 | -43.1237 | 2025-11-27 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 177.3 |
| 4a6b77ad-c91b-36ce-89a1-77c9b8df6ad8 | -8.1633 | -43.2055 | 2025-11-27 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| addf3e7b-dc2e-3758-a059-dbf92c470771 | -4.7204 | -46.4497 | 2025-11-27 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 160.5 |
| a4669f89-2a5a-3eeb-bc87-2d29455aee15 | -5.703 | -47.0532 | 2025-11-27 01:40:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| ab3460cd-815e-379a-b192-45da3fec6287 | -4.7203 | -46.4719 | 2025-11-27 01:40:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 30e2811a-5b2a-3e32-99f6-dbbc55bd74d1 | -1.3494 | -53.1094 | 2025-11-27 01:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 50.3 |
| dbf14bfe-c791-39f1-8216-f4b0cfa15eaa | -8.0507 | -43.1472 | 2025-11-27 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 219.5 |
| 477e780e-4c58-335d-b6eb-623242bab493 | -8.0318 | -43.1493 | 2025-11-27 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 237.1 |
| 2f539732-6a8c-3463-8e34-3bb9c0ba8046 | -20.408 | -57.9368 | 2025-11-27 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 86.5 |
| ccd3c490-0d62-39e1-978a-8ae3727c86d7 | -20.4076 | -57.9577 | 2025-11-27 01:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.0 |
| acbbff98-389b-38b1-b25e-5a95cd801936 | -4.7203 | -46.4719 | 2025-11-27 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 80.7 |
| 5383f893-9f35-328a-9336-80b1a905d1cd | -3.5269 | -43.6828 | 2025-11-27 01:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 118.0 |
| fd17e2ae-dbb8-36c6-93ab-8682ebb8dc86 | -3.8269 | -50.1809 | 2025-11-27 01:50:00 | GOES-19 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ab2d364f-f6ca-35f6-80e1-ef5bcf582f28 | -4.7018 | -46.4508 | 2025-11-27 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 17d58079-1abf-3974-bb4a-07c40bd9835b | -8.051 | -43.1237 | 2025-11-27 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 164.2 |
| 54c9f48c-5818-38a4-b170-2390acdac08d | -3.5268 | -43.7059 | 2025-11-27 01:50:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b8b7fed1-4184-3831-85a5-21a2ff90a590 | -1.3494 | -53.0891 | 2025-11-27 01:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f99eb7cb-8186-3445-b5b6-b555a7ebb741 | -8.0318 | -43.1493 | 2025-11-27 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 194.2 |
| 8096b3a3-9f7a-3bb9-9315-a7b9bd2c94a1 | -8.0321 | -43.1257 | 2025-11-27 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 163.1 |
| d6d8a55f-e4d1-38f2-8b4c-a2919c6fb759 | -4.7204 | -46.4497 | 2025-11-27 01:50:00 | GOES-19 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 121.8 |
| 9634bf4b-f309-3ab1-8901-dbbb470c3ee5 | -2.7588 | -49.3285 | 2025-11-27 01:50:00 | GOES-19 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 135aad22-52b8-3798-9740-a019c1dbc5a6 | -5.703 | -47.0532 | 2025-11-27 01:50:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 8eecff7f-bdc7-30f4-8b93-d3918810ff61 | -8.0507 | -43.1472 | 2025-11-27 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 190.1 |
| 72d00e7f-ddef-3f27-9062-0219b6592b58 | -20.3878 | -57.9396 | 2025-11-27 02:00:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 90.8 |
| a98a023f-d5a8-3ad9-92eb-6eb38c2afb95 | -8.0318 | -43.1493 | 2025-11-27 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 205.2 |
| cb47a2d1-2c34-3a3b-b13a-5f95edddf729 | -5.703 | -47.0532 | 2025-11-27 02:00:00 | GOES-19 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 8d6b492f-8626-3c48-88fd-87d578ce0525 | -8.051 | -43.1237 | 2025-11-27 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 152.3 |
| 4fae3c7b-c2ef-3f56-a6ec-fc9275ff4fc7 | -3.5269 | -43.6828 | 2025-11-27 02:00:00 | GOES-19 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 77.8 |


[Clique aqui para ver as próximas entradas](README4.md)
