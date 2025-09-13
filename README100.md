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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1fc135bc-2110-349b-a126-ec57527b3b6f | -3.21841 | -47.1349 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| c68e78f9-0f00-35fd-9e72-a552e033e3d9 | -3.22894 | -47.62425 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| de7775c0-0aea-3936-b544-351ac702af20 | -3.22878 | -47.13058 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1dd334d0-d8fd-3eaf-ae91-2434f9174593 | -3.22021 | -47.12297 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cd897097-e8cf-372a-a026-c541c780bbb6 | -3.22984 | -47.62931 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 245e0c8a-bccd-3faf-aebf-0402c967ebfd | -3.23482 | -46.79347 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 086782ff-7851-3e93-9afc-78a2414e6e4f | 4.33215 | -60.32928 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b3d3f233-0f5b-3141-884e-1c59aa778226 | -3.22602 | -47.13008 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b5f282c9-01ac-31a8-a022-5924a271d1ad | 4.3334 | -60.32938 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 317c5363-90e4-36cf-ba66-7cb1d37c1a45 | 4.33283 | -60.32568 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 763ab623-8fd6-3bb4-b980-86ea3622a3f0 | 3.84036 | -59.93463 | 2025-09-13 05:23:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a303c1f-e05d-3e65-b775-70e12c8a7018 | -2.95262 | -48.59729 | 2025-09-13 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fe89661-2c6f-384d-931d-ab405d360a1c | 4.3363 | -60.32513 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 32530938-d566-3493-8c73-ebc98287fcd7 | -3.22011 | -47.6394 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 9f7dec85-ef88-38c6-bd75-24a3fca3f70d | -3.23723 | -46.78061 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4c196fa5-7de1-3144-8f28-3b2256528e21 | -3.22169 | -47.63917 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| e6f910dd-2857-338d-a1a9-d25d8d014cee | -3.24321 | -46.7879 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 54e0a5d4-6063-3a2a-a40c-795ae3b9f44d | -3.22121 | -47.13535 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8263efd-8125-3ff8-b2a9-17c138f8ee36 | -3.51802 | -47.21828 | 2025-09-13 05:23:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 05c81dbe-24f6-3687-9b95-7cd68990cd98 | -2.85274 | -49.50291 | 2025-09-13 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4864166-2e3c-39d0-aee1-210b8c3ee169 | -3.22817 | -47.62965 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 51c9ce70-d604-3903-b9da-99d90384ff8c | -1.77871 | -55.69675 | 2025-09-13 05:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4b3e915-7db0-3d60-8a8e-d06102802643 | -3.22691 | -47.12416 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5376dfd7-db53-3734-b3a8-5e6553210869 | -3.22164 | -47.62864 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| f52b1e48-097b-3ed6-80d6-f445ca1ce32b | 3.83694 | -59.93507 | 2025-09-13 05:23:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f21b98e-33ec-3b9b-89e8-898fdd9c6cc1 | -1.97863 | -47.98052 | 2025-09-13 05:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e0501469-7578-363c-b153-decd2b6c6d87 | -1.97789 | -47.98538 | 2025-09-13 05:23:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 057111a7-09dd-38e6-bc69-cb7bd18ed3bb | -3.21622 | -47.12227 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5ada85ad-98cc-3ca2-b1f0-45239a8df850 | -3.24262 | -46.78823 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 9d8c6cbb-0e27-3e2e-a1b0-ffe68ab2bfbb | -2.85766 | -49.50542 | 2025-09-13 05:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 934f5e2a-6a37-3101-9125-b3c000a84f89 | -3.24231 | -46.79424 | 2025-09-13 05:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 64084cb7-5b1e-3305-8ac0-c691fee30e8e | -3.22087 | -47.63408 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 5cc2f97f-fb75-3677-84c7-02bac9b0947f | -2.94649 | -48.59641 | 2025-09-13 05:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3b1cee91-5e3a-3724-ac3d-fb030122df44 | -3.22249 | -47.63381 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| af636108-2976-3012-9af2-d41e2beae73a | 4.32936 | -60.32622 | 2025-09-13 05:23:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58d89d54-22d9-3f84-8369-a6cc65b89abd | -3.2274 | -47.63504 | 2025-09-13 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0a7e9e03-56e3-3d7d-8312-42ebf40ed885 | -11.15427 | -50.7113 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b1a25b5-9ed0-33f0-bdcc-b26045147b52 | -11.10453 | -51.43361 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| f6279e58-b738-3a3c-b20f-2e3512022290 | -9.06225 | -47.0386 | 2025-09-13 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c4a1144-a888-3edb-9f59-a74381d90390 | -11.12487 | -50.70305 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70066804-39a1-3245-9796-e2ec46b1e303 | -5.29496 | -60.10354 | 2025-09-13 05:25:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b7a592b-eade-3ffb-a01a-cd64a1d5d215 | -8.27205 | -64.0431 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 78e6aae0-b252-3dd0-a049-1c8fcb2aa0c5 | -11.81956 | -50.55437 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c7bc42a0-b3f3-33cf-99db-ba5ce4aca241 | -11.11289 | -51.33216 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 20.2 |
| e76df690-77df-3b29-9746-3d58b358e72b | -10.27636 | -57.79877 | 2025-09-13 05:25:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f72ed441-fac9-3334-abcc-3d6c22413d22 | -9.23824 | -51.25629 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| decfd110-2d45-3b72-91e0-8ab7d22e78e7 | -9.27557 | -59.41452 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bd27063d-4481-303c-979a-276b27a81de1 | -7.90946 | -55.26701 | 2025-09-13 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dd9adeba-e0ec-323b-a1ae-ede9f3cd550b | -9.50285 | -50.89359 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cfc8bf7e-4047-36e5-862d-3d7d5b96b864 | -9.25708 | -51.24379 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3d9840e-fe1a-3cce-9e05-345a8ff7d4f9 | -10.35281 | -50.50482 | 2025-09-13 05:25:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34d28c8a-41c4-3c0b-b12d-298a5956b7d9 | -11.80182 | -50.54745 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8a93a8d7-50f9-3e24-b9ca-980e1d128ac3 | -11.8447 | -50.55656 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29cf727e-34d8-3997-920a-aae74e436037 | -9.26 | -57.07073 | 2025-09-13 05:25:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc00cb4a-c8c6-30e0-898a-44b20e041fa5 | -9.91173 | -63.18924 | 2025-09-13 05:25:00 | NPP-375D | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3df996d3-f69d-3cee-a58d-d15dfc5e0988 | -11.76119 | -51.51158 | 2025-09-13 05:25:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9e3700a-5fc6-30ca-b4b1-219be0e6634e | -9.25756 | -51.24005 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6c3c0fd-71de-3a10-896a-0b216e285897 | -10.23779 | -48.63313 | 2025-09-13 05:25:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 858ef5b4-c26a-371f-a14b-99b64113569d | -7.54501 | -52.51736 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 88959a22-cc9d-3994-b0f5-04b335cee594 | -11.1632 | -50.70965 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5ba10cad-cf3d-364d-ae11-3c271a2096bb | -11.12438 | -51.33373 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb690fb8-1965-3ac1-bc7c-2d250788d7f6 | -10.33983 | -48.82044 | 2025-09-13 05:25:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 37509d13-4be8-3fd4-839e-2d227a95a0c5 | -5.09449 | -56.16238 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bebe38d3-b360-3737-8c1d-d70c8e2ff41a | -11.31962 | -55.22726 | 2025-09-13 05:25:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 747e5701-037f-39e4-a344-0f6e8964d4e3 | -11.17338 | -51.40894 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 0a0e00c1-36ef-3a6b-9691-9df1bbabe546 | -8.27071 | -64.04885 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 21f7de64-2e6b-3b64-beb6-9ce236570964 | -10.77273 | -50.52736 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e9d369d6-0088-38c5-b9bf-a3edaa85dadf | -10.76841 | -50.52862 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8fa7353e-25a2-3308-899d-ef18a65c0151 | -9.71856 | -64.92932 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4d6ef9f6-ba58-3aee-a415-21fb052f3b12 | -10.65021 | -48.97114 | 2025-09-13 05:25:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 53dd9997-5ed6-36ac-8852-a735c63e3216 | -9.50239 | -55.96464 | 2025-09-13 05:25:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d3ebfbfe-0926-3cb1-a15a-fb0ff3284ffd | -9.62236 | -64.18304 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dde3d16-1bf5-3338-a8a2-62368730e6bb | -4.93033 | -55.78573 | 2025-09-13 05:25:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 093c6d5f-654a-3e90-a879-f44493585bf4 | -11.18905 | -51.42306 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 64cd2357-3269-3a0a-bf0f-1685eba10a1b | -11.1053 | -51.33698 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ab75fec0-c255-30ac-9cc3-3152dc01b9e9 | -10.42108 | -60.80008 | 2025-09-13 05:25:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ca47af5-062d-3a7a-bd2f-2a8ca8a9b20a | -11.57492 | -50.5765 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 186f2e3b-9e1a-36ba-8169-0c54ede0ac65 | -3.15334 | -59.16378 | 2025-09-13 05:25:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f517e7c-b61f-39b8-b908-d81df48eb2f1 | -9.90447 | -51.89511 | 2025-09-13 05:25:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c6bc79f2-21fe-31a7-a401-a69551fe0bd5 | -11.8569 | -50.55812 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53c05eb8-d077-354d-ab92-908743e7d5bd | -10.52083 | -51.53783 | 2025-09-13 05:25:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 74062f1a-3df0-328a-9696-6993a9fc09cd | -9.90816 | -57.05863 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1489f36-462c-3580-9711-fd26d720ce1e | -9.26759 | -59.42088 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ddd98bd6-ea11-3952-8013-3ad4fe75bfed | -11.8142 | -50.55266 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e8355028-737d-3981-a6b3-7d980e428b4d | -9.90429 | -57.05811 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa9dcca8-8270-3ed0-bd2e-db3759bf19bc | -9.22698 | -51.25472 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 897153ae-7ee2-3d3e-83f1-868808e2cbe8 | -9.7361 | -65.01378 | 2025-09-13 05:25:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 25477ff0-2a50-38ac-ae30-e76df57103d5 | -9.91014 | -57.05604 | 2025-09-13 05:25:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e858b87a-710f-3f01-8204-afb2a1277020 | -11.79517 | -50.55133 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8cc837e0-c8b0-3fdd-93cb-c744a0a1475f | -3.90476 | -59.65117 | 2025-09-13 05:25:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ae76564-6ee2-328a-844a-58836e108380 | -7.54401 | -52.51778 | 2025-09-13 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4563a50-8198-38a1-b850-9f8e82c0e597 | -9.49606 | -50.90067 | 2025-09-13 05:25:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf4716bd-ff23-36b2-9be6-9a1dce912e7b | -11.18327 | -51.43006 | 2025-09-13 05:25:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bb7f7546-6527-302c-82fd-8be943d7a4af | -9.02517 | -47.03988 | 2025-09-13 05:25:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2e918b1b-5b51-31bf-b915-9bbfcbfdf060 | -8.27365 | -64.05363 | 2025-09-13 05:25:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c0c4d5a-bde4-3989-8b58-bdd4eb706e38 | -9.16352 | -60.29812 | 2025-09-13 05:25:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a7feeadb-b5dc-3c72-a065-2b3ecfbe2022 | -9.23359 | -51.24792 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4301c61-d3c8-3c15-ba6d-79c0d7f959c1 | -11.81459 | -50.54434 | 2025-09-13 05:25:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| da2184de-9556-3524-a577-50800189a811 | -9.25659 | -51.24753 | 2025-09-13 05:25:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8e0df35e-8ff3-3e71-a8cc-d05cf3e00d48 | -10.7733 | -50.52287 | 2025-09-13 05:25:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README101.md)
