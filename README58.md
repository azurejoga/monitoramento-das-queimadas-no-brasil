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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b988e375-009e-37e4-8893-50123946f0af | -9.20385 | -45.93332 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5cdb566-6c45-3d1e-b2f0-ecfcc6fefafd | -13.78485 | -47.94825 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2910e2f1-6045-396b-8b5d-414e79ad57fe | -11.8981 | -48.04849 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f74d26d3-4c29-3b5b-b955-3947d9f5870a | -7.92897 | -44.62837 | 2025-09-30 04:40:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f20da66a-0cf4-331e-9748-8363d3217e67 | -11.66438 | -47.48642 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 950e3305-94fc-356f-86da-ea1c4e79e0b2 | -7.83258 | -47.0056 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 48f616d0-2bd6-36f2-b9d6-419902646821 | -13.22482 | -50.93499 | 2025-09-30 04:40:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 33.4 |
| 0b4a4041-ecb8-332b-a3ca-69a3b32782e9 | -8.5438 | -44.66352 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4891c787-297d-3c8f-982a-c87ae619eb59 | -12.95671 | -46.40709 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5229f2ed-0410-3ce7-841c-0d18b592c0a6 | -8.06281 | -54.86312 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05a5466c-6c50-394c-bc2d-c6de120e7bc1 | -8.09661 | -48.00895 | 2025-09-30 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d25d3e8-bd8a-365f-8fd0-2fee15210610 | -11.24842 | -47.22792 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cf8ffdb9-a964-3b18-8ab3-b998f020a796 | -10.83558 | -47.96753 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bd3d09a8-4d24-3d48-87a4-0cbd067516fb | -10.66036 | -53.71186 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f452d983-53a9-3a8f-aae4-6f386c22d902 | -8.08905 | -48.00847 | 2025-09-30 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa8abbf3-6a2f-3c10-9f8a-25f00618fa92 | -9.30681 | -54.51011 | 2025-09-30 04:40:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| defd9657-4fb0-3950-9002-bcbf9006bdbf | -10.83774 | -45.40791 | 2025-09-30 04:40:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3c0eb797-1875-39b7-ab82-59b2cb6602b4 | -11.1565 | -54.11893 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 314903c5-e244-3306-9aa7-6a42124087d1 | -11.22251 | -47.20163 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 2bef93ad-c2f6-34bb-8138-f0e1bc8f44b1 | -10.65933 | -48.54513 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 1fa91f53-20fe-364a-9d88-0fddc044a0f4 | -11.70673 | -44.43254 | 2025-09-30 04:40:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87246374-be9c-37e0-b7f2-f3626ac44d75 | -11.41936 | -44.89748 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a2a7754-6566-37c0-9808-f04056e04b62 | -10.39338 | -48.14147 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6a4dd6b-c23d-3701-8995-41abc86ebf98 | -9.13005 | -47.63192 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0b9e148d-0a36-3821-95f0-8747859ab690 | -7.70094 | -46.82172 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3fb4be7-1283-3b97-b218-61080e7ab2e4 | -8.82694 | -46.18811 | 2025-09-30 04:40:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cdc5df9e-6132-330b-ad93-a72a9370d3d2 | -12.84653 | -46.97289 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca721b4b-72ae-38bc-8f21-02fa8dcc2216 | -8.14374 | -46.38816 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c49ca329-9345-3021-9b18-210b8e0b9d28 | -12.89962 | -47.08462 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 27d82075-06a9-3e8a-9471-47add26eb871 | -7.11967 | -45.5489 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 990f4652-a9aa-3d69-9e6f-136468eacf26 | -13.74177 | -47.90347 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe113141-7a2e-3103-8ec3-4281ebe83bc0 | -10.19039 | -44.89088 | 2025-09-30 04:40:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 9d6d6732-ea7b-3e13-a752-bdeb52e3ba49 | -12.83953 | -46.99559 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fbf5dcac-e94a-391b-8145-734cf8cd5759 | -9.06097 | -47.6305 | 2025-09-30 04:40:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2db704f4-689a-3a81-b98f-aa77fff81ea3 | -10.89262 | -53.74793 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bac6322a-fad6-3c92-be35-a30e04034ac4 | -8.25214 | -45.54029 | 2025-09-30 04:40:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 64cfa3bd-d153-380d-a524-0817d8dd4f3f | -13.07143 | -47.07717 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 288521de-9f56-33a7-abbf-abf6c9bf1968 | -7.01717 | -45.21449 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b376755-6b36-3cae-8233-336de1456f75 | -7.04932 | -45.18398 | 2025-09-30 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1aadb73-940c-3292-97ee-497590957a13 | -9.32571 | -50.62846 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c83a7ce-2f3c-3e7c-8c6e-3a2e55f678e8 | -8.09643 | -48.00583 | 2025-09-30 04:40:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d4d4b338-53be-3a89-af56-6b70a4c3b2a2 | -12.79566 | -46.89276 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1b874109-eb7c-35db-936f-cb969c05b84d | -10.62937 | -53.69786 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2868e1d-6bcb-36df-9c99-894762b6cd58 | -7.23546 | -46.7616 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d5e77172-18be-3f9b-8ae7-95a5897d2c2e | -11.63802 | -46.84162 | 2025-09-30 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d3c1d19-ffd0-3d27-aa52-aa21e5a6c78f | -13.84755 | -47.97367 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 232903ec-d791-36a2-b5d6-ac3f209b65e4 | -10.84188 | -47.80062 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5b590cfd-c545-377e-ab75-e327be46fe2c | -11.19752 | -47.22013 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 702cbbf4-155e-3671-86e0-52b29adefaf0 | -8.47077 | -46.8545 | 2025-09-30 04:40:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| dede2fa6-9037-3ce8-8199-3bf1fa87cf12 | -13.56834 | -48.20102 | 2025-09-30 04:40:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5f7aeb9-dd59-3e41-873c-bd9db963ecce | -12.81953 | -47.00143 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0a6252bd-930f-3ce6-b75f-c8a99aba3c65 | -7.02649 | -45.49899 | 2025-09-30 04:40:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79602b1a-1cd7-3c3e-b8d3-91fffbcb5523 | -8.92881 | -49.83927 | 2025-09-30 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 47691e6c-97f2-38f0-9f82-dd46f70a03ed | -12.88755 | -44.69819 | 2025-09-30 04:40:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a3dcab03-07b4-3a2b-a184-f0907a4adc0e | -10.835 | -47.97144 | 2025-09-30 04:40:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d17910bd-1d70-325c-bed6-17bacd5df218 | -13.75377 | -47.92256 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 491187ec-3365-3033-97bf-a9373ddfe8d8 | -8.99182 | -51.73988 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 771253a2-edde-3fd7-aabc-8f00ed5d9c41 | -9.44941 | -50.89943 | 2025-09-30 04:40:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aac25ead-32e0-3c04-93ec-eeb36e0e248e | -11.30759 | -47.07904 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aed79f8-4913-32e8-a84c-49b9bce4eb4b | -13.22353 | -47.31894 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 57959137-7250-3bce-bc77-2d73b2b276aa | -7.47342 | -49.46257 | 2025-09-30 04:40:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc093bea-9932-3de1-987c-2e3f6f6a041e | -9.04846 | -46.69886 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| baa47091-4164-3dea-92f2-5da29f698604 | -10.03986 | -50.19442 | 2025-09-30 04:40:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e38b7b0d-8420-307c-93da-d6c039d077c0 | -11.46365 | -51.50595 | 2025-09-30 04:40:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10c2ae49-fa8d-3450-a00b-4eba46b31e3b | -14.71965 | -45.2418 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1fb332ce-0123-3ee3-974c-51d64b349710 | -10.89404 | -53.73956 | 2025-09-30 04:40:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03fcc7b1-2bb4-3ec8-90d1-047c2b8d3b96 | -8.85046 | -46.64555 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 495a6c1d-4777-33a8-a6b6-e84cbacc60e9 | -10.38424 | -48.15544 | 2025-09-30 04:40:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a2b6b301-0f8a-3460-a218-b3e399719fbe | -11.28412 | -47.81788 | 2025-09-30 04:40:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a957a5f5-7763-311e-aa8a-5154ab924db3 | -13.35222 | -47.83851 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c2ca04c6-064c-3ea9-be19-c3a712aff530 | -11.20483 | -53.29757 | 2025-09-30 04:40:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8eb96d25-7f6f-3020-8b83-ced7c9666a9e | -13.73117 | -48.67083 | 2025-09-30 04:40:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d95c4698-7b5e-3046-88b6-448c2c3ec96e | -11.1969 | -47.22441 | 2025-09-30 04:40:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| cd056f21-06f6-3b6c-bc1a-cc0d0e93e927 | -8.16331 | -46.38252 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db8bcbd5-033c-3e38-91a8-3951806a61ae | -6.72397 | -47.20463 | 2025-09-30 04:40:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 355f5286-3f19-3ade-bf1f-990b2fcf7a2e | -12.22795 | -47.79565 | 2025-09-30 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 9ca04669-a920-30e7-933f-d115db4907ff | -11.46072 | -44.97821 | 2025-09-30 04:40:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d82977c2-835f-30ec-9ed8-2e4be9cf0656 | -11.8863 | -48.05203 | 2025-09-30 04:40:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8410c65a-2f42-3ac7-a25c-cfef15fb7790 | -13.82232 | -47.49381 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07ec44f3-0a20-31d2-84ca-2aef796abc4e | -11.99409 | -46.59874 | 2025-09-30 04:40:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcac5c46-092e-32c2-98ab-3c6052b4fb9c | -8.65396 | -43.97906 | 2025-09-30 04:40:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f2be9c-1a96-30aa-957b-912f06c43600 | -8.71029 | -47.86663 | 2025-09-30 04:40:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0679d874-2708-35c2-8417-8614e8ba40d3 | -11.78502 | -47.60571 | 2025-09-30 04:40:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7788b073-b649-364a-98a1-ad934192a87b | -7.36979 | -47.04667 | 2025-09-30 04:40:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b68bb3b-e7f7-3e50-9037-a17930160719 | -10.64977 | -48.58582 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 181a64dc-244a-36d5-92d8-cab7a7988a99 | -7.04411 | -46.41386 | 2025-09-30 04:40:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 81c9fbc6-ac51-3d71-9d2f-dd778292b887 | -10.6554 | -48.57147 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f6d3bda-b503-3e6f-82d6-1b98bdee3d78 | -14.72729 | -45.21661 | 2025-09-30 04:40:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea952f8c-24d7-3513-b77c-5e79c1b89e26 | -13.63241 | -42.53342 | 2025-09-30 04:40:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d7b8c245-0304-3895-9c22-3e177dea848c | -10.64921 | -48.58949 | 2025-09-30 04:40:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ece8a121-03f6-3213-b8fe-7cd57c2f210b | -13.65441 | -48.05103 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fd274486-d6b0-3ff9-a159-a7b9c91e52d1 | -12.66752 | -46.86997 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 454f9dab-fde0-3d07-884b-fcec55d866fa | -8.54433 | -44.65981 | 2025-09-30 04:40:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8275d8de-8cfd-3cd6-aed6-939fcb4849d9 | -8.79414 | -46.72216 | 2025-09-30 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dde35d4-ba51-3d97-8813-0327fd640238 | -9.5756 | -40.35673 | 2025-09-30 04:40:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 90571b33-6ad1-3b5e-ad83-0106e7c86a9b | -9.96269 | -48.79519 | 2025-09-30 04:40:00 | NOAA-21 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40d74cba-edbe-33e8-89cd-ce76c8c0ffdf | -13.81305 | -47.47897 | 2025-09-30 04:40:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 191f2b6f-9efb-3dd8-826e-50c60b24c07c | -11.21745 | -49.86241 | 2025-09-30 04:40:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d115fb2d-293c-3864-acce-cc3a2b703bc1 | -8.04735 | -49.70604 | 2025-09-30 04:40:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fd246476-6d20-3bcd-8256-eb983afd720a | -12.85455 | -46.99788 | 2025-09-30 04:40:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 15.4 |


[Clique aqui para ver as próximas entradas](README59.md)
