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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 498ee28c-2d9c-3edc-b301-b963f6398cd5 | -13.3346 | -54.4233 | 2025-08-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| a97ce86b-44fe-3edf-b973-2fa9492c0827 | -13.3349 | -54.4027 | 2025-08-21 13:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 655ab0ad-7cc0-3b92-b6ae-540e2efb3fc9 | -14.3715 | -51.9747 | 2025-08-21 13:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| b02a56f4-bd1e-323b-82c2-8508b155912b | -13.1364 | -54.9376 | 2025-08-21 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 49051862-5d7c-3f4f-914a-0a8a87ad159b | -13.0123 | -45.1756 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 353.7 |
| 3412b9db-65a0-3d2b-8cf0-e9eae32800e2 | -6.5386 | -45.5224 | 2025-08-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3af0d1c6-6005-3e62-9cf1-b9c9bcae0e8f | -7.0164 | -44.6413 | 2025-08-21 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 4c2c005d-28c1-3681-ad17-3166c51197b5 | -7.0354 | -44.6167 | 2025-08-21 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 123.7 |
| 750de821-1f73-3369-9445-e5e4e81bef2e | -13.0307 | -45.2189 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 0d38673e-b60f-3129-b9e9-b536bce3f44f | -14.3321 | -52.0224 | 2025-08-21 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.0 |
| ae474774-83a0-351c-874f-a3bc8d63e861 | -13.1555 | -54.9357 | 2025-08-21 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 3f189b20-6089-3489-95e5-123b30bf5edb | -13.1558 | -54.9151 | 2025-08-21 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 532.4 |
| c3b36762-90e1-30ef-99a3-47dbdf748c7b | -14.9999 | -54.8343 | 2025-08-21 13:40:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 823974d1-1e42-39d3-90f1-05360ee8b847 | -13.1367 | -54.9171 | 2025-08-21 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 327.7 |
| 506bf189-de0d-3303-8586-437d7a234087 | -13.0505 | -45.1925 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 1b833c50-d715-3136-9eff-8e3e3c8f67fa | -5.2345 | -42.7193 | 2025-08-21 13:40:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 95.0 |
| f15b5896-8e95-3001-b8f4-96ec8b41cdce | -13.3154 | -54.4254 | 2025-08-21 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 25fc55fa-799a-3a12-a031-70fe22a357d6 | -13.1369 | -54.8966 | 2025-08-21 13:40:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 873b5684-55fa-3017-955f-933b31465f4a | -7.5641 | -44.4068 | 2025-08-21 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| cc53e45b-9aeb-3567-8470-e2f3c15c3cf4 | -6.4158 | -44.6695 | 2025-08-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| ed098273-aa5a-3af3-84c5-751416fd3f24 | -14.5843 | -51.9464 | 2025-08-21 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.6 |
| 31e1cf39-32f6-39b2-8700-fff2bd2b0869 | -13.0317 | -45.1724 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1139.7 |
| 744f35df-d1e1-374f-84c9-4669759bb032 | -7.0166 | -44.6184 | 2025-08-21 13:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 03053bea-bee9-3cae-be96-100ac0da30b2 | -13.3349 | -54.4027 | 2025-08-21 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| ef37e5f5-6145-3df4-b9fb-05222a28554e | -4.7152 | -47.2216 | 2025-08-21 13:40:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 172.8 |
| 1792eeaa-f367-3435-9468-02faf1548bc2 | -13.3346 | -54.4233 | 2025-08-21 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 101.3 |
| fcab8a15-3847-3b10-8634-7868ecdc1de2 | -7.6296 | -45.2464 | 2025-08-21 13:40:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 1779766c-768a-3d94-958f-64f19d3de304 | -13.0312 | -45.1957 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 705.8 |
| 0b28ac78-31c2-3bfa-b696-a0bdfa152252 | -8.8737 | -62.3925 | 2025-08-21 13:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 8d4d7ee3-4bb0-3c4a-a9a8-a30bc09ced15 | -13.051 | -45.1693 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 188.6 |
| 0116c757-1482-3651-bac8-03a9eb9a098f | -13.0321 | -45.1492 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 282.2 |
| d5f1e331-a0ad-3251-b621-9cb842bf41bd | -6.1 | -44.397 | 2025-08-21 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 74.5 |
| c820b7f7-f843-3d04-9329-6d1e08b661dd | -8.0152 | -47.6656 | 2025-08-21 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 725e3632-0148-35d1-8204-4e065d3e34b5 | -12.6694 | -44.9757 | 2025-08-21 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 778e8d18-154f-346d-81b7-4e05d3341ff4 | -11.3468 | -55.4124 | 2025-08-21 13:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 26cefd8f-5c8e-3dd9-96d9-b5db414e756a | -10.5229 | -50.3634 | 2025-08-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.8 |
| a6e6b906-4dce-3ecb-950c-ba252e4cfc11 | -6.2753 | -43.7139 | 2025-08-21 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 90.5 |
| 0c90847c-33be-3f8b-ae81-95b0a27b899b | -13.3349 | -54.4027 | 2025-08-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 42c5f56a-185e-3b12-9272-930f79a43743 | -8.7759 | -45.4486 | 2025-08-21 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9920b75d-63e6-3c12-8c26-a525808c00e5 | -15.0189 | -54.8528 | 2025-08-21 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| e9d7a815-3cf9-3cc7-93e5-89f712c55a79 | -13.1555 | -54.9357 | 2025-08-21 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 202.3 |
| edd8cacc-0b0c-362e-9102-83f951ca5e29 | -14.3127 | -52.0249 | 2025-08-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 293.4 |
| ad492158-457f-30f0-bcbe-2d5eddc13d38 | -13.3154 | -54.4254 | 2025-08-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 102.9 |
| cbf1e5a7-9ec9-3fcc-b98b-d7836526a9f6 | -6.275 | -43.7371 | 2025-08-21 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 69.9 |
| 2083d152-8aa1-3d79-880f-0bfdf9b87d31 | -8.8737 | -62.3925 | 2025-08-21 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 288d2f8b-049e-3462-b344-3420542403ee | -13.0307 | -45.2189 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| d3ed0377-fb44-315d-9ae2-a66d653a282e | -7.0354 | -44.6167 | 2025-08-21 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 1034bf79-effa-33db-b737-ebf8b0593457 | -12.6698 | -44.9525 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 91.6 |
| e4ec5d2c-6162-3292-ba80-f1e4f5367e5f | -6.5388 | -45.4998 | 2025-08-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| b44f7995-33bc-328c-bdbe-cc6c3c531f31 | -13.1364 | -54.9376 | 2025-08-21 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 94.7 |
| 2bf797da-8441-3d22-9dde-c3faf4a255ac | -7.0166 | -44.6184 | 2025-08-21 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 163b9e4c-3414-3973-a54c-27024c418807 | -11.6028 | -50.3739 | 2025-08-21 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 109.1 |
| 5cda360d-2ef8-3642-a3aa-3b3aabce139c | -13.051 | -45.1693 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 204.5 |
| b02d152e-c002-3840-b523-077a2426b8f3 | -4.7152 | -47.2216 | 2025-08-21 13:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 5eddb8f7-db63-3989-b8b1-25ac5d19948e | -8.8736 | -62.4115 | 2025-08-21 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.1 |
| fbdff697-4343-3dee-9e61-f763a0cc229a | -13.0321 | -45.1492 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 292.6 |
| 02024c15-1bec-3ccc-b82c-e7db7202b2b1 | -8.1687 | -47.3658 | 2025-08-21 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 044262ea-aae7-37e0-a5f7-aa3f2b51c0ad | -6.2924 | -43.8747 | 2025-08-21 13:50:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 3b5f64da-66d0-3d82-8de6-51540774e96d | -7.6296 | -45.2464 | 2025-08-21 13:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 81.0 |
| 5266ebdc-e63a-3726-abfe-25c34a27e7de | -8.0152 | -47.6656 | 2025-08-21 13:50:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 2c7a1f9b-5923-30c3-b3b4-d007fb11dbf7 | -5.2345 | -42.7193 | 2025-08-21 13:50:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 127.3 |
| d78df560-e547-3d1a-aad4-bc201405f5d5 | -12.6435 | -45.3269 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 25004f7f-ac32-35ee-8766-d016d90377e9 | -13.0515 | -45.146 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 8e2d6723-d9c0-3ec9-a1f5-6ebcfa3df993 | -7.0164 | -44.6413 | 2025-08-21 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| b8b9045a-ff00-31c5-94cd-bbeb5570bd03 | -13.0505 | -45.1925 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 164.6 |
| 868f6c46-25b3-3bf1-8b4d-2c2f512319bc | -5.2518 | -40.7296 | 2025-08-21 13:50:00 | GOES-19 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 8a29174f-829b-324f-97c0-da49321a83b1 | -13.3346 | -54.4233 | 2025-08-21 13:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 123.9 |
| 26517c0f-e929-337c-9483-da000a1d6084 | -13.0317 | -45.1724 | 2025-08-21 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1112.6 |
| aaef3270-b710-39a7-a46f-df4314c55995 | -14.9999 | -54.8343 | 2025-08-21 13:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 57.6 |
| acdf9dc8-9368-32e7-84b1-3e1c9cae9f86 | -8.8551 | -62.4123 | 2025-08-21 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 54.6 |
| dfa78c70-4e70-31ea-aa53-2f08158b9334 | -8.7567 | -45.4733 | 2025-08-21 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 146.8 |
| 395f1b54-6940-3b6d-90ee-110218a52eff | -14.3321 | -52.0224 | 2025-08-21 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 352.2 |
| 21ea8bfc-5ecf-3571-9f52-00c90a99e225 | -6.5386 | -45.5224 | 2025-08-21 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 4445ec6b-d929-370a-9bc2-e6cf7cba7e46 | -10.5231 | -50.3421 | 2025-08-21 13:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 134.6 |
| 13f35f85-8479-39f8-bde1-b17a9e8fed01 | -13.1367 | -54.9171 | 2025-08-21 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 263.9 |
| c1aa92e0-3be7-383d-af8b-4859f65565d4 | -8.7756 | -45.4713 | 2025-08-21 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.9 |
| d5ef874f-adc6-35ab-9f52-b2c4de91f6a9 | -13.1369 | -54.8966 | 2025-08-21 13:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 6649919a-6a42-375a-8281-7aae26edcf8b | -14.9999 | -54.8343 | 2025-08-21 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 102.3 |
| 45b627f4-0ac7-3923-b8a8-d9525bf4c43f | -13.0307 | -45.2189 | 2025-08-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 3a5edb5b-cca4-38f6-b6c8-d10fe9c5b2b6 | -13.0505 | -45.1925 | 2025-08-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 169.4 |
| 083bcebc-7535-386b-96a0-62b38979b7c7 | -9.7241 | -47.9588 | 2025-08-21 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 154.9 |
| 9b2fe6fc-e531-3d03-ace3-05c5e54bc417 | -17.3997 | -44.2518 | 2025-08-21 14:00:00 | GOES-19 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 2b44b905-3519-3c13-b799-15bdc5bf1628 | -14.3715 | -51.9747 | 2025-08-21 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| e66e339d-0466-30a4-80bc-40177b8161e5 | -6.4528 | -53.3872 | 2025-08-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.7 |
| fd023b5b-314a-3779-8ca7-11c55f10d060 | -8.6901 | -62.0963 | 2025-08-21 14:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0f4b38ea-caf7-3ddb-9142-8fc450aa6802 | -13.1364 | -54.9376 | 2025-08-21 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 108.4 |
| 938b5b1f-de7c-39c6-b9f1-87f7ef5a614d | -7.241 | -44.7126 | 2025-08-21 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 104.8 |
| d68eb13f-460f-3e0a-b029-7ec6ed0f44fd | -10.5231 | -50.3421 | 2025-08-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 15b74837-3053-3964-949e-0dcb40ade644 | -12.9533 | -46.2419 | 2025-08-21 14:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 93f1bb41-3c5a-34e8-a574-32a4ff157e0c | -14.9996 | -54.855 | 2025-08-21 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 8879022e-b186-397c-9e3a-cb42a46e6df3 | -13.0312 | -45.1957 | 2025-08-21 14:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 684.9 |
| 7210b916-e81f-3090-8cc1-c0676927adb5 | -8.7759 | -45.4486 | 2025-08-21 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 105.0 |
| ceaefe8c-c7c2-3dde-9689-ff016a2c53f5 | -15.0189 | -54.8528 | 2025-08-21 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 0a64e696-fa1f-324b-88dc-0bde197c5c49 | -9.7052 | -47.9609 | 2025-08-21 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 115.5 |
| 0313eace-9567-3487-930e-353aa5505c69 | -15.0193 | -54.832 | 2025-08-21 14:00:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| c61ba4f3-24db-3e28-b7ce-e50153b496a5 | -8.7567 | -45.4733 | 2025-08-21 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 138.6 |
| 9bbc9dd5-1dde-3d9b-80fa-3ef0afee7949 | -4.7152 | -47.2216 | 2025-08-21 14:00:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| c300574e-3137-3a8a-8aa1-09bacae3ee4f | -13.3346 | -54.4233 | 2025-08-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 162.1 |
| 5437a2ab-7b15-3e64-8ce5-b7f6b292ef1f | -13.1369 | -54.8966 | 2025-08-21 14:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 05db4586-dab7-36f1-ae02-0008c37c1c8b | -7.6369 | -46.2599 | 2025-08-21 14:00:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 82.0 |


[Clique aqui para ver as próximas entradas](README64.md)
