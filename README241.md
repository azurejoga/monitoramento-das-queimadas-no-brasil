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

## Dados Diários - Página 241

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89a5e2c2-8692-3d7a-9c48-a063da4a2bfd | -9.432 | -45.8293 | 2026-10-07 17:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 510.4 |
| 0b7caee4-9815-3f56-9168-47b5895c688a | -10.9762 | -45.4094 | 2026-10-07 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 100.7 |
| d8900ad1-29c8-3346-9db7-dd400d08029e | -9.4131 | -45.8314 | 2026-10-07 17:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 184.8 |
| 5fc55c05-4c30-3f73-85a8-ddfaec51e88a | -11.0863 | -45.6688 | 2026-10-07 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 772.1 |
| fa33058b-4884-39c2-8910-7f183bfba7e4 | -11.2337 | -44.8446 | 2026-10-07 17:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 1eb19620-52e4-30b4-8c01-0e05ca59c90d | -12.2136 | -44.6758 | 2026-10-07 17:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 252.2 |
| 2be81d60-22f7-31a4-995c-9194e217e70d | 1.6385 | -55.8047 | 2026-10-07 17:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| f3deb66c-3c9d-36f2-95da-58312d7fa0f2 | -12.2132 | -44.6991 | 2026-10-07 17:00:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 124.9 |
| da72fe45-f736-32a8-8c5a-2562d8d053d7 | -9.806 | -65.0167 | 2026-10-07 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 5ceca6fa-b876-34a2-a840-7025fc3a3806 | -11.0867 | -45.6459 | 2026-10-07 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 643.1 |
| 6e684306-5632-355d-aa4f-a9bff0e5274d | -11.1051 | -45.689 | 2026-10-07 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 203.3 |
| d34ee9ea-2f4e-360a-a9b0-d65c48dde287 | -11.3745 | -46.6948 | 2026-10-07 17:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 153.6 |
| cd36ee99-3548-3b27-88f6-061ad8387c37 | -12.1746 | -44.7051 | 2026-10-07 17:00:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 20551bd7-e847-3b45-81de-6dc1e69122e9 | -8.3391 | -72.6012 | 2026-10-07 17:00:00 | GOES-19 | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 113.5 |
| 2e0a062f-b9bd-34be-990c-027495bba17b | -10.9946 | -45.4527 | 2026-10-07 17:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 95ff2fd4-f353-3def-827f-78320f0da9f3 | -9.75 | -65.0562 | 2026-10-07 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 709815bb-e74b-3503-85b5-097293c53d4a | -9.6757 | -65.0401 | 2026-10-07 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 99.9 |
| b6a767de-21e3-3897-9d67-6fa44479a2bb | -9.8061 | -64.9979 | 2026-10-07 17:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 116.7 |
| e298fedc-b3ef-39ca-bda8-f19c237b5dba | 1.8038 | -55.5458 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 639b699d-f436-3138-8503-3d8e4df538de | -9.806 | -65.0167 | 2026-10-07 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| b3d4b969-e610-3d22-b41f-8e8e7ac97157 | -11.3745 | -46.6948 | 2026-10-07 17:10:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 105.8 |
| 11dea342-bd55-3ab9-8eab-3f28c0d86d26 | 1.7671 | -55.5661 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| f8e83fba-e60a-3000-9615-fead6b17c897 | -9.7126 | -65.0951 | 2026-10-07 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 6d3a8c34-41d6-331a-9c45-f8aaae22fc81 | 1.8768 | -55.7227 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 82.3 |
| f0ec787d-6bb2-3ece-9709-83973ac9ba98 | -1.1713 | -49.2969 | 2026-10-07 17:10:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 12afd378-a94f-3027-9641-d9b39019a8bb | -12.2136 | -44.6758 | 2026-10-07 17:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| a9eb156c-9ca6-3649-82ca-34f876a26433 | -11.2337 | -44.8446 | 2026-10-07 17:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 87.8 |
| 9ceaf52c-4af8-385e-908b-142d6f2c0903 | 1.8038 | -55.5261 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| ae90c79d-1232-346d-a788-629c3d55726e | 1.6937 | -55.6263 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 180.9 |
| 13dd87f0-ec5b-3492-80be-47e87e5c145a | 1.8767 | -55.7424 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 74.5 |
| a5c46e73-1df4-38bb-996f-861a80519f9d | -12.1742 | -44.7284 | 2026-10-07 17:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 956130c8-fab5-39c1-abcf-cb8d30a023af | -12.2132 | -44.6991 | 2026-10-07 17:10:00 | GOES-19 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 32be3988-a95f-349a-b1bd-c315c4f06f88 | 1.7671 | -55.5859 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 65d0c63c-59e1-31af-931c-419f4209aff0 | -7.8443 | -70.8705 | 2026-10-07 17:10:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 100.3 |
| 4b9ffea0-6463-367e-bcab-877f00c6c8cb | -10.9949 | -45.4298 | 2026-10-07 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 114.6 |
| b1b9dc38-1dd5-384c-9426-c58e5e8040cc | -11.0867 | -45.6459 | 2026-10-07 17:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 60f91d85-4eac-3267-b2dd-4c0aaa5eeb28 | -9.8061 | -64.9979 | 2026-10-07 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 40f2c2b1-9943-3f51-bcf4-cd4499eb1077 | -9.8246 | -65.016 | 2026-10-07 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 08ef44d8-c013-3c09-80f6-999a8f930cff | -9.6757 | -65.0401 | 2026-10-07 17:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 89.3 |
| ed493d74-2797-3e60-9e60-18c3e92dafb7 | 1.712 | -55.6459 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 121.6 |
| e5a55404-073e-3570-b644-f22c3334beaa | 1.7121 | -55.6063 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 905af592-4ea3-32e2-bbd6-4a928ff62484 | 1.7121 | -55.6261 | 2026-10-07 17:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 4eee7afd-e52a-3330-b6b8-b10ee5409912 | -12.1746 | -44.7051 | 2026-10-07 17:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 889c2d78-746d-3190-b5ac-bd385e73adde | -2.79 | -54.09 | 2026-10-07 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3775c28b-be60-3daf-bda9-0c2be640998e | -3.29 | -54.01 | 2026-10-07 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24df25ca-674e-35b5-ba1b-b588e0bc8bfc | -2.79 | -54.03 | 2026-10-07 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d039990-e226-3e8f-9cd6-53f24101d8de | -3.29 | -54.07 | 2026-10-07 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 795b8b48-7a2f-3f00-83b3-7fdf7da57a54 | -6.05 | -42.6 | 2026-10-07 17:15:00 | MSG-03 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 3ae44b9c-4c9f-34a8-9e21-cd0f52318579 | -5.95 | -46.35 | 2026-10-07 17:15:00 | MSG-03 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a17b37e0-d64b-3884-92a9-fb6626e67455 | -12.19 | -44.88 | 2026-10-07 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2d1e1c6f-fb40-3ec0-9f41-07e1e4665214 | -12.16 | -44.87 | 2026-10-07 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| de94c64e-194c-33b6-9e34-9947be64ecae | -2.82 | -54.09 | 2026-10-07 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2997cbda-9410-3dd4-b065-32c45f75f730 | -12.16 | -44.77 | 2026-10-07 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 269b3db4-9b1f-3f8d-9038-47a9bc0a12c7 | -5.76 | -45.19 | 2026-10-07 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2e04c7a5-86e8-30d1-88ac-f6f3694ca63c | -13.7 | -49.1 | 2026-10-07 17:15:00 | MSG-03 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 403ea54e-efea-3bb5-8f9c-187915ef7942 | -12.16 | -44.82 | 2026-10-07 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 697c3f69-ed93-3d8f-a608-9d9ce24f477d | -12.19 | -44.83 | 2026-10-07 17:15:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5b9a0964-4c8d-389f-a4a4-032d3c8c8070 | -5.76 | -45.14 | 2026-10-07 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cfc234b9-d84d-3fbc-83e0-96abaa846d7f | -3.2 | -42.95 | 2026-10-07 17:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9af81792-30fd-3bf0-bda8-1eb42e137b00 | -3.23 | -42.95 | 2026-10-07 17:15:00 | MSG-03 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1964f6a2-1180-3bca-898b-edd042d63022 | -5.73 | -45.18 | 2026-10-07 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9961e68e-63e5-3b70-910a-a64752882f75 | -3.32 | -53.83 | 2026-10-07 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c78b54d-04f2-391c-9450-98a08473a986 | -2.82 | -54.03 | 2026-10-07 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 080ac870-269f-3ba1-8c7d-03407c090ca3 | -5.98 | -46.35 | 2026-10-07 17:15:00 | MSG-03 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 86689e9a-c8b3-3e21-8aff-328f68237e53 | -3.05 | -53.93 | 2026-10-07 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5984d25e-b5e2-354d-b9f8-8bae7c232952 | -2.79 | -54.15 | 2026-10-07 17:15:00 | MSG-03 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85c81b8c-9bf5-35cf-8928-527e657c7221 | -3.32 | -53.89 | 2026-10-07 17:15:00 | MSG-03 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb36410-c61f-3def-8a41-4f6180218aa3 | -5.73 | -45.14 | 2026-10-07 17:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 990c7a54-1046-3551-8e88-6346e9b44e74 | -2.76 | -54.08 | 2026-10-07 17:15:00 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30353091-d7e8-343f-8697-f1efd21bf493 | -5.5 | -42.85 | 2026-10-07 17:15:00 | MSG-03 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d91060f5-b678-312a-a635-54012ae8f189 | -11.619 | -43.6196 | 2026-10-07 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 314.4 |
| 1d9629c1-7eda-31a3-ae72-0a44ce508fdd | -9.4565 | -64.3344 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.0 |
| b55afd2f-c471-3748-8d99-0e4b0b8ad85d | -9.6757 | -65.0401 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.0 |
| a75fa4b0-0a4e-36fb-b9b3-8bd93eafa886 | -7.0164 | -71.5907 | 2026-10-07 17:20:00 | GOES-19 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 255.7 |
| bf6680d0-1569-3681-a645-a8be8480213a | -9.7499 | -65.075 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 6996c988-fff9-3b5c-b81f-f455f67892d5 | 1.6937 | -55.6263 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| eb1da941-f8e7-3ee9-91fd-4adb0ad2434e | -11.8508 | -43.5361 | 2026-10-07 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 131.9 |
| a7db3790-0c3c-3b93-a468-77f55152e1c6 | 1.8951 | -55.7224 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 7119a5d1-facc-3cf3-9236-32fa44b81249 | 1.8767 | -55.7424 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 72e1ad69-f1ff-3b6f-a0e1-408cd906c1da | 1.7487 | -55.6059 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 6b40acdb-2ffb-3bfe-aa7b-e9ab5d46ff09 | -9.8061 | -64.9979 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 866b78d0-02bc-3e4a-b099-84dc38fe370e | -12.1742 | -44.7284 | 2026-10-07 17:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 143.8 |
| 06dd4598-a2ed-30fa-9443-bcdea51b8cd7 | 1.7671 | -55.5859 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 114.2 |
| de727164-856b-35a8-9605-6aee466b2c7d | 1.7121 | -55.6063 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 3498fd5b-d05a-3c0a-bf0e-088771c308a8 | -7.8234 | -72.7142 | 2026-10-07 17:20:00 | GOES-19 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 87.2 |
| dc84b403-3ca0-3683-8dd5-a669a24b71c3 | 1.8038 | -55.5458 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| a4bc7de1-7e05-3ca6-913a-ad7a4b01202f | -9.806 | -65.0167 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 929091e3-0751-37a9-8d70-136a76c885f9 | -9.8246 | -65.016 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 62668c0b-821d-3b86-8295-837a4766b079 | -9.6572 | -65.022 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 4c952e26-d78d-3d8b-9138-f4bd06bb56f4 | 1.6385 | -55.8047 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 93.7 |
| 372b38ae-259d-3db5-bff0-ca1209565bca | -9.7312 | -65.0944 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 656ef359-0c2a-396e-97f9-e0c58a503edb | -9.8059 | -65.0354 | 2026-10-07 17:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| a291c863-5123-319e-a51a-25c5f1d6eb40 | -0.3952 | -52.0152 | 2026-10-07 17:20:00 | GOES-19 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 65.8 |
| db169a70-7741-33c2-b54a-236ecef54ecd | 1.6937 | -55.6461 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 290.6 |
| 37981a8b-36c3-35b3-9779-bbb28a098801 | -11.7738 | -43.5482 | 2026-10-07 17:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 178.8 |
| eed6f3eb-86e5-38bc-9269-186a35dba3a4 | -11.0863 | -45.6688 | 2026-10-07 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 83c49cda-4199-3aae-9eba-04b50ced8cca | -9.4509 | -45.8271 | 2026-10-07 17:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 150.3 |
| 885322fa-b20f-32af-b64c-2bc833a7f0e4 | 1.7121 | -55.6261 | 2026-10-07 17:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| a12580af-3050-36b4-ba5e-a2e4586b8ebf | -10.9762 | -45.4094 | 2026-10-07 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 170.3 |
| 023e18a4-e277-3ccf-be55-596dd1fbd2c6 | -9.432 | -45.8293 | 2026-10-07 17:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |


[Clique aqui para ver as próximas entradas](README242.md)
