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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb3146e2-9563-3865-b78e-a67c2349fc8b | -7.6149 | -46.552 | 2025-11-15 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| c1d94cc9-19ee-3914-8efd-3762b5c08fd4 | -8.1778 | -45.0332 | 2025-11-15 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 261.1 |
| bc0a5943-d384-3fca-986c-5e5a2a94e4d7 | -7.492 | -42.5452 | 2025-11-15 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| c55324fe-ea97-3b8f-a702-e1f1a349aeda | -8.5607 | -46.0588 | 2025-11-15 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| b131903f-1b74-368b-86e7-ebc1ac4658bc | -8.662 | -45.5061 | 2025-11-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 1d457b50-5e01-3b9e-95b4-35343a1be301 | -3.9897 | -44.2584 | 2025-11-15 13:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 78e32a1b-44bc-38d4-a905-e18181b052b5 | -3.59 | -42.4421 | 2025-11-15 13:40:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 157.5 |
| 5cdfe556-c8b2-36f7-896f-4f0af58c6cd4 | -3.6511 | -44.7994 | 2025-11-15 13:40:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a99dd11e-07b1-3ab4-be6b-b2abe3371e50 | -8.5604 | -46.0813 | 2025-11-15 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| cc96f818-94fb-327e-9dbd-0c7a97ea58e0 | -7.4417 | -45.2411 | 2025-11-15 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 67f5fa8a-130d-31cf-9c95-6e02e609194f | -6.1233 | -48.0532 | 2025-11-15 13:40:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 250.1 |
| 8f73d87c-485a-3b2a-95fb-52a8eb39800d | -8.7543 | -45.655 | 2025-11-15 13:40:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b7723932-497c-357d-baff-cd709f0e1633 | -7.442 | -45.2184 | 2025-11-15 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 170.2 |
| a750c8a3-6a8c-317a-9862-e0e70ff2ac0b | -7.3868 | -48.6545 | 2025-11-15 13:40:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 3f58bad9-3320-3556-8254-553a253c840a | -3.3658 | -42.4529 | 2025-11-15 13:40:00 | GOES-19 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 9c25912b-f8c0-32c0-b9a0-9a2a367175cb | -6.4113 | -41.4552 | 2025-11-15 13:40:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 69.1 |
| 3ac4d309-abbd-3f32-a814-96cdc18a6398 | -8.5795 | -46.0568 | 2025-11-15 13:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| 8b76d681-6819-3812-a3cf-692796d5e1d4 | -8.1967 | -45.0312 | 2025-11-15 13:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 168aa36e-c648-3ccd-b310-f15dfe790987 | -7.9789 | -38.6541 | 2025-11-15 13:40:00 | GOES-19 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 142.4 |
| ffc83646-73ea-3228-b126-44a28870442c | -3.651 | -44.8221 | 2025-11-15 13:40:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 538de06e-a1f6-3de9-8836-62c7f66c2425 | -7.4328 | -42.7644 | 2025-11-15 13:40:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 230.8 |
| aa980782-a6b0-3d50-b385-1567cae9a0e2 | -6.1421 | -48.0302 | 2025-11-15 13:40:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 175.2 |
| 7ac21a2a-66cd-3d3c-b182-a2210aa0c5b5 | -6.0496 | -45.8072 | 2025-11-15 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 63.1 |
| cfc9ed1a-d3a2-3941-aa89-d52edba71fa5 | -4.5779 | -42.8808 | 2025-11-15 13:40:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 101.3 |
| 23599f32-1ada-3246-8208-38b35a26f881 | -4.7342 | -47.1547 | 2025-11-15 13:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 60fae433-899b-317d-b9d9-6e5016d026c6 | -3.8196 | -44.655 | 2025-11-15 13:50:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8a96d073-b18e-3097-9d2f-33303966495f | -3.6698 | -44.7985 | 2025-11-15 13:50:00 | GOES-19 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 0bc803bd-ecd9-3f95-9858-11d7547bc98d | -8.5675 | -45.5161 | 2025-11-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 86.5 |
| c7ba9998-5a9f-34e6-99ea-3b8cf13a278d | -8.662 | -45.5061 | 2025-11-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.3 |
| e14967cf-63ad-378e-8bee-bdbd93864f20 | -1.3191 | -49.1462 | 2025-11-15 13:50:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| cda580df-1b56-386e-b196-724a31cbd24b | -8.7543 | -45.655 | 2025-11-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 124.1 |
| 9f6fd579-0a99-3a48-a81e-6e0a97869d5e | -6.1608 | -48.0289 | 2025-11-15 13:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 61a36362-e3cd-3a80-879d-f3bac71c8c36 | -3.6835 | -42.4374 | 2025-11-15 13:50:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| 1454ac1a-b2c3-31c3-8a91-da8a06e77452 | -3.6511 | -44.7994 | 2025-11-15 13:50:00 | GOES-19 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 97.8 |
| ea148a82-2f87-38bc-a3df-5dac04ec725b | -7.4417 | -45.2411 | 2025-11-15 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 92.8 |
| c92b2790-832b-3f73-a28c-60a28b5bbb0a | -8.159 | -45.0351 | 2025-11-15 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 156.6 |
| 8c531f0c-66ce-32b4-8ad8-bb60e0551f46 | -7.1129 | -42.7254 | 2025-11-15 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 83.8 |
| afe87e21-c12e-3c38-a191-7cdec4443a5d | -7.3868 | -48.6545 | 2025-11-15 13:50:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 482f741b-23db-3048-9e30-861a92b92a87 | -6.1421 | -48.0302 | 2025-11-15 13:50:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 6e72211f-5554-3e94-9ce7-c64c534f149b | -8.1967 | -45.0312 | 2025-11-15 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.9 |
| e6594252-5a10-31df-a96b-940ab2dfee6d | -7.442 | -45.2184 | 2025-11-15 13:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 151.5 |
| 9ee450b9-e49e-3fd9-a0a3-9e1e56ce6bcc | -5.4753 | -40.9553 | 2025-11-15 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 112.0 |
| da164e4d-8a8c-3865-bb34-2578dd7c3b5b | -7.4517 | -42.7624 | 2025-11-15 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 319.9 |
| 333ea4fb-6274-3de0-b9e1-44aea7f7b6aa | -8.7355 | -45.657 | 2025-11-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 258de4f3-33e2-366b-9f56-338fc4828660 | -7.492 | -42.5452 | 2025-11-15 13:50:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 120.9 |
| e3c69b77-2ecc-38f0-b7bf-b4741f4ef878 | -7.4139 | -42.7663 | 2025-11-15 13:50:00 | GOES-19 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 3b11f12c-e507-3857-97a5-b9dca4f849ca | -6.0496 | -45.8072 | 2025-11-15 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| c77e6607-1380-39a0-9af8-03d850f51c98 | -5.5127 | -40.9765 | 2025-11-15 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 133.3 |
| 4b0b9549-0ae6-3c4f-87aa-ec5e5e0b8b06 | -5.2701 | -47.6496 | 2025-11-15 13:50:00 | GOES-19 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 67.4 |
| cd88d1d8-2b15-3b46-a968-f0e6f54fbcf9 | -8.6623 | -45.4834 | 2025-11-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.7 |
| c1797da3-608c-3363-8354-ce17e90f0547 | -6.1233 | -48.0532 | 2025-11-15 13:50:00 | GOES-19 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 0adf1017-d0f6-37d8-8f0d-657d24310c80 | -5.4751 | -40.9796 | 2025-11-15 13:50:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 107.6 |
| 5905535b-a11a-3fe2-9bf8-06c387811485 | -3.9897 | -44.2584 | 2025-11-15 13:50:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 2c699079-fc52-3daf-a918-6301ad6883e8 | -8.6808 | -45.5041 | 2025-11-15 13:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 128.5 |
| c0cb2f5d-7509-3144-8483-035eef213342 | -8.5607 | -46.0588 | 2025-11-15 13:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 0286e099-2aaf-3acd-959a-41cb98d74cbd | -6.0309 | -45.8085 | 2025-11-15 13:50:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| 1bbc2c53-2274-39da-820f-d7f78c576438 | -3.4459 | -41.4975 | 2025-11-15 13:50:00 | GOES-19 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 142.3 |
| 028d201a-80d4-3768-9af7-843732bd9214 | -8.1778 | -45.0332 | 2025-11-15 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 259.3 |
| b7cb4058-c06f-382d-962e-e76c4660db0c | -3.59 | -42.4421 | 2025-11-15 13:50:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 189.1 |
| 751be0bb-cd0c-37a3-88ec-6c040b73303f | -3.1561 | -43.282 | 2025-11-15 14:00:00 | GOES-19 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| af6205fc-6ad7-3a31-b274-cefc937f878a | -6.0309 | -45.8085 | 2025-11-15 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e867c577-65db-32f2-8493-124f529d913a | -10.3037 | -44.6017 | 2025-11-15 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 131.6 |
| 73155907-6ea5-3ce4-980b-fb60ef2088a6 | -4.8125 | -41.6084 | 2025-11-15 14:00:00 | GOES-19 | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 98.4 |
| 475d2265-b716-311b-a07e-027c95004769 | -5.4753 | -40.9553 | 2025-11-15 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 110.3 |
| a3292ea6-5146-3218-8d73-ed93c9d569d0 | -3.971 | -44.2594 | 2025-11-15 14:00:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 35b633f6-b866-38cc-8114-68be0b2f5c2e | -7.4417 | -45.2411 | 2025-11-15 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| b29e30f2-d5a6-33ac-a7a0-bf5c13b46e34 | -6.4113 | -41.4552 | 2025-11-15 14:00:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 72.2 |
| 1cc4d8f2-862e-395a-8938-3c90ae0b5208 | -8.662 | -45.5061 | 2025-11-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.9 |
| eb5c956d-e6fa-3a65-9d83-8ad4406cbb6f | -10.3041 | -44.5785 | 2025-11-15 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 120.5 |
| f3789716-51ee-3f47-8ca1-a06cbf45d6b1 | -3.7899 | -43.3688 | 2025-11-15 14:00:00 | GOES-19 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| d56eebb9-fc97-3623-b091-c5f1006ebc95 | -7.3868 | -48.6545 | 2025-11-15 14:00:00 | GOES-19 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 63.9 |
| cf8a9f07-3ace-3125-a69f-c3f60d04c74d | -8.7355 | -45.657 | 2025-11-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 167.0 |
| a857ed91-2018-327b-a240-b88d48906b14 | -8.159 | -45.0351 | 2025-11-15 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 68e18788-7c0e-39fc-bd89-c279db2fe3c6 | -1.4895 | -47.0723 | 2025-11-15 14:00:00 | GOES-19 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| 7891fa0a-14fb-332b-90a4-e47ab453a689 | -10.3232 | -44.576 | 2025-11-15 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 276.2 |
| cb9844cc-abf0-3b9a-8727-26aebd0abfdd | -5.4939 | -40.9781 | 2025-11-15 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 91.2 |
| 80a264dc-1620-3263-9a9d-db6290a5289e | -3.2626 | -40.8065 | 2025-11-15 14:00:00 | GOES-19 | URUOCA | CEARÁ | Brasil | 2313906 | 23 | 33 | nan | nan | nan | Caatinga | 103.4 |
| 07574f70-b585-3786-bbbd-0c767b4d9db2 | -4.4246 | -43.4038 | 2025-11-15 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 6b1985d2-18e8-3b5a-a6c7-de42d5641e82 | -5.5316 | -40.975 | 2025-11-15 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 104.3 |
| 7cca5735-4359-345a-94ac-8ce567741c9f | -8.1778 | -45.0332 | 2025-11-15 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 240.8 |
| f221cd14-d216-3f44-92dd-5ad1ad46d497 | -7.7681 | -37.4158 | 2025-11-15 14:00:00 | GOES-19 | INGAZEIRA | PERNAMBUCO | Brasil | 2607109 | 26 | 33 | nan | nan | nan | Caatinga | 129.7 |
| fdbb723b-4732-34ee-99b5-308a7ed92c08 | -3.6835 | -42.4374 | 2025-11-15 14:00:00 | GOES-19 | LUZILÂNDIA | PIAUÍ | Brasil | 2205805 | 22 | 33 | nan | nan | nan | Caatinga | 201.0 |
| e3ad3b65-61c3-3e0d-b401-49ef71e49384 | -3.59 | -42.4421 | 2025-11-15 14:00:00 | GOES-19 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 234.1 |
| 2eaacea4-22bd-37d5-881f-ae60d2b12a32 | -7.38 | -44.0554 | 2025-11-15 14:00:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 67.9 |
| 771ddb83-6339-36b5-b420-68d0fa8a997e | -7.2567 | -40.1725 | 2025-11-15 14:00:00 | GOES-19 | ARARIPE | CEARÁ | Brasil | 2301307 | 23 | 33 | nan | nan | nan | Caatinga | 180.0 |
| bf61f9df-f244-30a4-be3c-0797807d5ead | -6.1421 | -48.0302 | 2025-11-15 14:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 365.7 |
| f0aebd7b-7a63-390c-924b-4a5c95716b18 | -8.5795 | -46.0568 | 2025-11-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c9651b32-1627-38c1-980f-4ea9c34c219f | -10.3228 | -44.5992 | 2025-11-15 14:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 369.1 |
| 43f1e265-ae07-359b-a053-028225456d0f | -8.1967 | -45.0312 | 2025-11-15 14:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 517394c5-bca0-3b2e-af02-db1d9fe656c1 | -9.7305 | -48.8966 | 2025-11-15 14:00:00 | GOES-19 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| c5e6c9bd-1197-3265-b155-4081602dcc9b | -8.6808 | -45.5041 | 2025-11-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| f4a54d40-95d0-3025-abf7-34f0ca186360 | -4.5568 | -43.2096 | 2025-11-15 14:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 6fb7b6ef-0f77-3b7f-a3cd-3853cc37ee56 | -9.1247 | -49.1511 | 2025-11-15 14:00:00 | GOES-19 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| a693472c-dc5b-301a-b311-d25f99fde577 | -6.0496 | -45.8072 | 2025-11-15 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 0b513b71-7586-3635-a9ba-a91127275872 | -7.492 | -42.5452 | 2025-11-15 14:00:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 97.1 |
| 72d42d90-423a-39b7-8550-1d2235d81e2e | -5.4942 | -40.9537 | 2025-11-15 14:00:00 | GOES-19 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 89.5 |
| 75dbc102-f1cf-390b-821a-8b7a00d1527b | -8.7543 | -45.655 | 2025-11-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 59a2da37-a89f-38df-b3b1-382d7fa51012 | -6.1608 | -48.0289 | 2025-11-15 14:00:00 | GOES-19 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 56.6 |
| 18fa0586-2643-3159-884c-52851c61c9b9 | -8.5607 | -46.0588 | 2025-11-15 14:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 3538a0c1-f8f8-3759-9a92-484f5947b645 | -8.5675 | -45.5161 | 2025-11-15 14:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 169.5 |


[Clique aqui para ver as próximas entradas](README63.md)
