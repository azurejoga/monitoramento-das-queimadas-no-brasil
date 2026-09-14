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

## Dados Diários - Página 95

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24dec614-fa1e-324a-b3f1-3a5d88405257 | -10.66 | -54.19 | 2026-09-14 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f89ec659-8215-3300-b13a-7f298ce9fc1c | -11.51 | -45.79 | 2026-09-14 17:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64f3e045-fef1-351b-aaef-a8e44fdf8e3d | -14.41 | -45.3 | 2026-09-14 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a5475d17-244e-33cf-9dc8-eaa9d7ab20e8 | -14.38 | -45.24 | 2026-09-14 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ed39661d-4c90-3479-9c1a-b3588b9ce16c | -14.41 | -45.25 | 2026-09-14 17:15:00 | MSG-03 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 539d6aae-4be6-3846-9191-2bc63e3b4777 | -10.69 | -54.13 | 2026-09-14 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db7c2fd0-7f3d-3c4a-a5dd-a0014c7c9771 | -14.24 | -47.42 | 2026-09-14 17:15:00 | MSG-03 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f38f9f31-fd07-3b8b-8fd7-f94546e7bbfa | -14.21 | -47.41 | 2026-09-14 17:15:00 | MSG-03 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4c10bfd9-86b4-373f-acf0-57c5f0ebbd32 | -7.2 | -46.16 | 2026-09-14 17:15:00 | MSG-03 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36c07261-17a9-39bb-b26c-97b0af3a5a02 | -10.66 | -54.12 | 2026-09-14 17:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2259d504-3aa2-3110-a808-7bd2cfe1f542 | -1.3007 | -49.1464 | 2026-09-14 17:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 535dd11b-2082-32ff-bd0b-5ad3d1ec17e4 | -13.2867 | -51.3046 | 2026-09-14 17:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 263.1 |
| 27775cfe-a735-3d17-9c22-02af2add726e | 1.3634 | -56.1031 | 2026-09-14 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| db3354b1-f58a-3070-9eb3-4290c30eafe5 | 1.2243 | -50.7683 | 2026-09-14 17:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2db00cb7-38c7-38b4-9c61-52c34dab5e69 | -2.6786 | -57.4921 | 2026-09-14 17:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| a415ced5-a940-38c2-a691-adcdedf35269 | -3.4374 | -61.0812 | 2026-09-14 17:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 45.1 |
| cb7b0e63-df10-3f01-8a7d-95fd85065c9a | -13.5526 | -51.4629 | 2026-09-14 17:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 7f675d96-72ec-32df-b317-3e3c4cfa8d18 | -9.3763 | -50.1139 | 2026-09-14 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 40b24c59-596e-3491-9eef-b3a09fd9388c | -6.1111 | -57.6645 | 2026-09-14 17:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 164.6 |
| cbdc544e-43a0-34d8-9bce-8566b6b3d1fb | -9.8511 | -48.3397 | 2026-09-14 17:20:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| 6fb924c0-f014-3b2a-aecd-b5468b7ee3e5 | -13.3059 | -51.3022 | 2026-09-14 17:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 167.9 |
| 5733806f-84d9-3c6e-9f6f-41e89aeca047 | 1.3634 | -56.1228 | 2026-09-14 17:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 7fdef153-4ef0-3acf-909c-836dbd944c65 | -9.3765 | -50.0925 | 2026-09-14 17:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| 7790df99-e8cc-3ba6-8e7c-cf8fd822a991 | -6.3436 | -55.8243 | 2026-09-14 17:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 114.7 |
| fa1ac5b2-e18c-36d3-9081-df22c6375370 | -6.1111 | -57.6645 | 2026-09-14 17:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 118.5 |
| 3c5a334c-4262-39dc-a5f8-1620c1871c07 | -3.4186 | -61.3084 | 2026-09-14 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 41eb3b55-d926-37a3-9269-aba4e1b01735 | -13.2867 | -51.3046 | 2026-09-14 17:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 131.1 |
| 97b60d63-d03f-3faa-9b44-e36f8e2137f1 | -3.3639 | -61.2715 | 2026-09-14 17:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 7fa94734-b77d-39f0-ae04-0f6927bd4331 | -13.3059 | -51.3022 | 2026-09-14 17:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 106.3 |
| 461311e0-9be9-38db-8d1e-f26ded392ed3 | -13.5526 | -51.4629 | 2026-09-14 17:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 150.9 |
| c40fda9b-c2e9-31a3-a344-d5c8d2e4c526 | -3.1266 | -61.2188 | 2026-09-14 17:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 8f91da7f-3f15-3fc0-96b5-264cdc34964f | -11.2488 | -54.1378 | 2026-09-14 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 73d122b3-1bf6-3618-b598-61bfe4548f6e | -9.8072 | -43.5246 | 2026-09-14 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 116.9 |
| 2fc7ff80-94f3-380b-8394-38d9197412f3 | -3.7129 | -60.6022 | 2026-09-14 17:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 66588cb5-5672-3f08-b86e-31b179f577c6 | -3.7311 | -60.6018 | 2026-09-14 17:40:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 42.2 |
| a3ecf69b-396a-3656-83ad-9fa115c4e5f7 | -13.2993 | -51.7075 | 2026-09-14 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0a45b26f-65c1-30fd-8602-e5a965ff5519 | -3.4374 | -61.0812 | 2026-09-14 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 79f67c95-ddcc-39f3-9978-58b693d0ed11 | -6.277 | -41.6841 | 2026-09-14 17:40:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 137.0 |
| fb76979a-063e-3279-b405-29a03390fcf5 | -6.018 | -57.8242 | 2026-09-14 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 0ee14456-77f7-3729-820a-84fb16047b00 | -13.3059 | -51.3022 | 2026-09-14 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 95ca33b8-d864-3a8d-84d9-e4b8a788ea7e | -2.6786 | -57.4921 | 2026-09-14 17:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| c4a81662-3795-3801-bca1-2047865cb926 | -6.1111 | -57.6645 | 2026-09-14 17:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 17157c51-1829-39e4-ae66-eda73db86e98 | -13.5526 | -51.4629 | 2026-09-14 17:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 159.0 |
| 15cbd63e-6066-3bc2-9f54-79c688cfc7c1 | -13.3251 | -51.2997 | 2026-09-14 17:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| 2c9f4a5f-b1d1-3ff9-840b-ed683bc696fc | -7.1578 | -42.1032 | 2026-09-14 17:40:00 | GOES-19 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 122.3 |
| 0b8a6f9d-e810-3d44-869a-5e6ad936b11d | -3.4003 | -61.3087 | 2026-09-14 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| f15fa2ce-cef4-34b4-945e-83e5564049d4 | -13.2867 | -51.3046 | 2026-09-14 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 47841df3-8dbc-3a62-a423-37d24124c66a | -9.8075 | -43.5011 | 2026-09-14 17:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 246.7 |
| 1614e31f-5ce5-3e65-8b91-245a4e3148f5 | -6.6512 | -43.6587 | 2026-09-14 17:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 191.3 |
| cce629d7-b024-3039-b5c5-b685f641b2bd | -12.4901 | -41.4012 | 2026-09-14 17:40:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 170.2 |
| b68eb051-404a-3784-9eb8-9b1af2cefa6b | -13.3185 | -51.7051 | 2026-09-14 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 22b4613d-39f7-39cb-a2a5-c9141ab70a1b | -3.3639 | -61.2715 | 2026-09-14 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| eaa19a1d-0d9a-37ce-ba7a-441f2d1c316c | -6.8445 | -55.581 | 2026-09-14 17:40:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| d1508fb1-822e-3a93-8d09-0d0db67b4446 | -3.1816 | -61.1045 | 2026-09-14 17:40:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 5d4b1377-505f-35bf-90eb-1c8c0b1abc3a | -7.1012 | -42.1088 | 2026-09-14 17:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| 99269c04-b089-34e1-b57d-2ced720cf539 | -3.4186 | -61.3084 | 2026-09-14 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b3019e38-11dd-3a82-a9ce-39071cd17bfc | -7.7824 | -46.6705 | 2026-09-14 17:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 69.2 |
| a0aaf3d0-8889-34c4-acba-9c9309dae689 | -13.3199 | -51.62 | 2026-09-14 17:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| d82c40a0-7ad9-3b7a-adc7-7f5d4ea36bd4 | -3.3639 | -61.2715 | 2026-09-14 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 0cd617e0-a232-3cab-8d99-f6b34f3752c4 | -3.4003 | -61.3087 | 2026-09-14 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 86.0 |
| 332c2418-85e1-3c98-9647-52001006cab0 | -13.3199 | -51.62 | 2026-09-14 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 78cfee45-4ac2-3b5c-b72a-5a45cbb0c10c | -15.5121 | -43.8455 | 2026-09-14 17:50:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 5c2f6d07-fe6e-3dc3-9a6d-49afcb95da49 | -3.1462 | -60.6317 | 2026-09-14 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 74cd9376-8894-3e22-a030-e11e99115363 | -6.67 | -43.657 | 2026-09-14 17:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 114.6 |
| 52c8f75a-cba6-329a-922e-5f817f52423d | -13.2867 | -51.3046 | 2026-09-14 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.7 |
| 455fae9d-efe8-3c05-8139-11d3cb357736 | -6.1111 | -57.6645 | 2026-09-14 17:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.0 |
| b6efea3b-47aa-3b0d-890b-1ce1c06e3184 | -7.1012 | -42.1088 | 2026-09-14 17:50:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 142.7 |
| b087b9d4-d27f-3b3b-a333-5b169eec36bc | -13.3007 | -51.6223 | 2026-09-14 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 60f9b30f-0f81-3457-a173-d3d38083b2e3 | -8.8081 | -45.8753 | 2026-09-14 17:50:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| b0dbb9cd-727b-3594-964e-67e2bdff18bf | -13.5526 | -51.4629 | 2026-09-14 17:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e81aeaf4-12da-3d43-a285-9f6905755ccd | -11.193 | -42.8065 | 2026-09-14 17:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 213.5 |
| ed2c6377-4e48-39e6-9fad-bfc67e1772fe | -7.1051 | -41.7731 | 2026-09-14 17:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 157.7 |
| f9a7fc4e-66b7-3210-b0dd-e25fc5e6aafe | -13.3003 | -51.6436 | 2026-09-14 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.2 |
| a8157f1e-f61c-3edc-9d1d-8bc45e1a3f79 | -9.3768 | -50.0712 | 2026-09-14 17:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 188.3 |
| 59504f2b-3538-37e6-a3a5-2a5727174ba3 | -9.1339 | -51.5927 | 2026-09-14 17:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 7fecedc4-bfe0-3390-860c-01dc4f32dfdc | -3.4186 | -61.3084 | 2026-09-14 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5877c154-db22-3ac5-aa63-4011225ea079 | -13.5719 | -51.4605 | 2026-09-14 17:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 10614276-b340-3230-9942-0da6731d5f1e | -14.205 | -47.4039 | 2026-09-14 17:50:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 34d45a96-4f54-37cf-8a1f-863a3f258c8e | -13.3391 | -51.6176 | 2026-09-14 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 173c4b99-c098-3e2a-8f73-a740a886a935 | -6.8445 | -55.581 | 2026-09-14 17:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| ef108f37-d72e-3c7f-a174-f4d8a65ce267 | -10.6958 | -47.5175 | 2026-09-14 17:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 274.3 |
| 95ef5c53-ca10-3501-8c29-d0eb77541fc2 | -12.1093 | -50.8499 | 2026-09-14 17:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 138.9 |
| ca83803c-a97c-39e6-9bb4-c29226dc37bf | -11.2488 | -54.1378 | 2026-09-14 17:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 16266e0e-af6f-3fbe-b77e-5089c2bb94f3 | -12.4901 | -41.4012 | 2026-09-14 17:50:00 | GOES-19 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 409.7 |
| 230aa30f-e088-34e5-8bdf-ee34d6b0c367 | -3.1633 | -61.1238 | 2026-09-14 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| e6b1ca65-e0e1-36d6-96f3-ca5fde610d49 | -11.1738 | -42.8095 | 2026-09-14 17:50:00 | GOES-19 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 145.4 |
| 31f017aa-a5dd-32d7-a1e2-751008c94b5e | -3.0352 | -61.2392 | 2026-09-14 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 7ff26908-bc6d-3043-95ca-10a2f739ab1b | -3.4374 | -61.0812 | 2026-09-14 17:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| b3a810cd-8dfe-3726-bc34-bf8fd8144212 | -7.1048 | -41.7971 | 2026-09-14 17:50:00 | GOES-19 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 139.3 |
| 6e9cab1d-271a-32e4-a328-f702954221a3 | -13.3059 | -51.3022 | 2026-09-14 17:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 6f0e85ba-42a7-3334-8eef-7cccd572451e | -9.8075 | -43.5011 | 2026-09-14 17:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| ca312026-866c-3fe0-a220-dc93d77224b2 | -9.8511 | -48.3397 | 2026-09-14 17:50:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| eba0ee77-adde-3aa9-af34-a389c39ffdb7 | -9.4137 | -50.1317 | 2026-09-14 17:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| d37cccde-619d-3c2e-9892-9d3e39979a8a | -3.1816 | -61.1045 | 2026-09-14 17:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 93.3 |
| c8faf076-0c7e-358b-a7b4-1ce29189bf40 | -6.6512 | -43.6587 | 2026-09-14 17:50:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 119.2 |
| c99bee05-a835-3817-9dae-eb11e20e7ac6 | -8.031 | -39.0035 | 2026-09-14 17:50:00 | GOES-19 | VERDEJANTE | PERNAMBUCO | Brasil | 2616100 | 26 | 33 | nan | nan | nan | Caatinga | 139.5 |
| 0fc5ad6e-3855-300e-a6b1-04e00f0b2f1f | -10.6641 | -54.1491 | 2026-09-14 18:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 478.4 |
| 88f18398-9f10-3526-a82d-046ee3cd3b5d | -14.1856 | -47.407 | 2026-09-14 18:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 86d23aee-6356-3ea2-ad6e-92f5db9a4b92 | -3.3638 | -61.2904 | 2026-09-14 18:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 57.3 |
| 3367d9e3-4fd7-38f8-86b7-6b281e0ad1ae | -3.1633 | -61.1238 | 2026-09-14 18:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 67.3 |


[Clique aqui para ver as próximas entradas](README96.md)
