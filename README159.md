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

## Dados Diários - Página 159

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 36b7fb76-df3a-3b94-8642-1df467f8b7c2 | -9.2477 | -57.0697 | 2026-08-28 18:20:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 2c9b974f-65c0-3996-bb1c-72569907a24a | -9.406 | -60.5711 | 2026-08-28 18:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| de321838-63e6-33e0-8b04-74fe979349df | 1.4373 | -55.6491 | 2026-08-28 18:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 9e76d615-a621-360f-bd63-b06e4f654b86 | -7.5478 | -61.3056 | 2026-08-28 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 239.3 |
| 462ab8f1-ec72-340b-967a-ee4c24dda904 | -9.1713 | -49.9622 | 2026-08-28 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e4e4105b-c29f-3452-a89c-51684ce6671c | -9.1525 | -49.9639 | 2026-08-28 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 130.8 |
| 7230ce1f-5591-3983-bec0-d36e3239f1ba | -6.0005 | -57.6689 | 2026-08-28 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c478239e-405f-3a97-890f-90275b600732 | -13.8752 | -54.1153 | 2026-08-28 18:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| caeeb401-87ad-3122-a678-dc827a774e1a | -9.2475 | -57.0894 | 2026-08-28 18:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 9ae97b10-c6af-3036-9354-4371f85be8d5 | -6.9521 | -58.9506 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.9 |
| 534b2aa9-71f8-3c0b-80ec-91cfb4496167 | -6.8018 | -59.4201 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 8f48f146-2784-3c8a-b5e5-13537d25f418 | -11.006 | -49.6461 | 2026-08-28 18:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 77.0 |
| f9d207c6-392e-388d-b1b9-d3a0443e311e | -6.5323 | -55.2378 | 2026-08-28 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 164.3 |
| 837684c1-2979-3aac-83be-05e0832e1749 | -8.093 | -45.8128 | 2026-08-28 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.8 |
| b3065190-242c-3038-9b79-1f72cf649976 | -6.605 | -55.4337 | 2026-08-28 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 8bd3d848-d689-3fbb-9571-a47c020ce60c | -6.8358 | -59.9379 | 2026-08-28 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| baf8409d-ef44-3a66-a1f8-f0626de112ce | -8.7955 | -49.996 | 2026-08-28 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.0 |
| 2f4c7206-1bdb-335e-9aab-fe3b9c6ec96a | -7.4734 | -61.4037 | 2026-08-28 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 31455391-d36a-352e-b3fe-db1e3e8368da | -9.7878 | -43.5506 | 2026-08-28 18:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 9f4848bf-e618-3b0c-aa58-63c2fb7e8d5a | -4.3021 | -59.4826 | 2026-08-28 18:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 104.3 |
| b19aee28-8ea9-3df5-b6b5-8afd3a5e338e | -6.5865 | -55.4346 | 2026-08-28 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 93.8 |
| fe78d22b-944d-3b42-81cd-7a376fd99401 | -7.3663 | -55.1734 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| fcc3b9d1-c5c3-332a-8f0f-fa8fae5adb22 | -8.795 | -50.0387 | 2026-08-28 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 14f2f86c-87dd-36ad-ab6e-bb215bd76bac | -6.7645 | -59.4794 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.8 |
| a5a53f85-1ee4-3c94-af00-08a51723945a | -9.9708 | -53.9419 | 2026-08-28 18:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 179.0 |
| 9641ad09-94cb-3296-a0f4-e70e2a34cd00 | -8.1432 | -64.0053 | 2026-08-28 18:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| ca40e7ca-d684-3ba7-adb3-e4d7ae287d46 | -8.8184 | -49.6308 | 2026-08-28 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 57e25ff7-a5f4-33bf-bea9-409ed9e7c3a0 | -8.5365 | -55.2826 | 2026-08-28 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 7ffa162b-f181-3bff-8597-cf97b79257a4 | -9.1711 | -49.9835 | 2026-08-28 18:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 3e6c7b62-53f0-3fad-9307-bfee83ce95d2 | -14.1645 | -52.8269 | 2026-08-28 18:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 91.5 |
| bdeff1ae-ab65-3f0f-b358-31aabecb829b | -11.2128 | -53.9976 | 2026-08-28 18:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.0 |
| bdea1c0f-0070-3d62-afa6-746c0137ab54 | -6.1744 | -53.4631 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| c54b8533-2cd8-3b5d-ac89-92f87548ee55 | -6.8571 | -59.4179 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| a87324ea-e839-33fe-bbf2-bcb9f5765cf9 | -14.1784 | -48.7703 | 2026-08-28 18:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 2f690cd2-1e0a-3c4d-a692-1913e6165dd3 | -8.0739 | -45.8372 | 2026-08-28 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| bb5d2504-c903-3467-8f51-1c0eb4df562e | -9.4702 | -51.7103 | 2026-08-28 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 64938f85-5d72-3d75-bf7b-7b14f6d4dcc8 | -9.1976 | -61.1 | 2026-08-28 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 22eb625a-ee1d-3f8f-b88b-9c8f96f7ef73 | -9.4517 | -51.6909 | 2026-08-28 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 0c9ce271-fdfe-353c-89f5-cadb716a2197 | -8.631 | -66.5473 | 2026-08-28 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.5 |
| f0675a7a-f1e3-3771-ae7b-14e00a290a08 | -3.2178 | -61.2362 | 2026-08-28 18:30:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 651d5f13-8834-353f-9343-b191b66ed97f | -4.3022 | -59.4634 | 2026-08-28 18:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 96.1 |
| 549f6ca6-778f-3f36-ac84-db1680b5624c | -4.3205 | -59.4821 | 2026-08-28 18:30:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 94b34244-1135-39f0-89c2-bc9365676b86 | -11.025 | -49.644 | 2026-08-28 18:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 407ef01c-3ba3-3aa9-984e-60f4261697c7 | -10.8801 | -50.5179 | 2026-08-28 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 48.4 |
| f5d5a148-bae6-3d48-95b2-c23455d51cde | -8.3785 | -70.8456 | 2026-08-28 18:30:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 7a29ca3f-a253-3dd9-b889-c1af294469e6 | -8.5977 | -54.6948 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| a10e141f-d466-3152-a3f8-7fdb0380056b | -3.2361 | -61.2359 | 2026-08-28 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 89.3 |
| 07a1d32e-e024-33f6-8944-d2f5b2808da0 | -15.6139 | -56.4103 | 2026-08-28 18:30:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 74.7 |
| f1b306e3-6359-39fe-8b25-ce3d7c2f8d4a | -6.1795 | -45.9097 | 2026-08-28 18:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 53.1 |
| fb6ea5f1-05cb-38c5-a011-b4305796a23b | -11.1995 | -55.1008 | 2026-08-28 18:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| bfb8a6b2-76d4-31c8-b33b-a730cd5373d2 | -6.7832 | -59.4401 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 37800b64-32c9-3318-8fd7-987666ef5e1e | -7.3478 | -55.1744 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 6936e8ac-f258-3cb8-8cac-5e86c26c1227 | -8.5975 | -54.715 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| efbc807d-fb99-377b-92e2-fe11be88023c | -9.2477 | -57.0697 | 2026-08-28 18:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 610dad68-d85d-3750-9149-7aca7e7a110f | -12.7603 | -44.2608 | 2026-08-28 18:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 192.2 |
| aefccd29-ebf2-3e53-9c4b-2ebf982b2f9b | -3.2361 | -61.2548 | 2026-08-28 18:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| fe1a8aeb-3bf2-3ce3-9d37-ee79d4d0ebdd | -14.8821 | -52.608 | 2026-08-28 18:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 214.0 |
| 8b651c09-792b-3d6d-a7db-c992a9b9185d | -10.3205 | -49.9567 | 2026-08-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 63e77dfe-90b0-3b53-a464-3007ad3bf759 | -7.5289 | -61.3825 | 2026-08-28 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 65c9985a-bec4-3425-a930-2882ee3613a6 | -6.3322 | -54.7473 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 62af3e79-08f7-3ef4-a3c8-dc8f8881e013 | -8.87 | -66.8935 | 2026-08-28 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| bd323f8c-1d07-35da-a813-f9fe23498a1b | -7.5479 | -61.2866 | 2026-08-28 18:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 29e3cfbc-c39f-35e4-922d-52ec7c097307 | -10.3391 | -49.9762 | 2026-08-28 18:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| 0a6b7cb8-8339-3fae-aac5-35bb242c7891 | -8.6311 | -66.5287 | 2026-08-28 18:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.8 |
| f780cd5c-3004-3436-bcd1-a6f1b8a6a771 | -6.8542 | -59.9372 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| fd49285e-7697-3408-98d5-e0693b390b0b | -11.2489 | -45.0732 | 2026-08-28 18:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8088f18b-62c5-362c-911c-2dc8ba75faa3 | -6.8569 | -59.4564 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 61f38418-2537-36d0-94c7-a44dbf33f3cd | -6.8019 | -59.4008 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ed6fd3c3-26e5-3342-a5a5-a1f52200b0b3 | -9.1895 | -59.6364 | 2026-08-28 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 7b39af6d-f42c-388c-a430-290fee20f167 | -7.3665 | -55.1534 | 2026-08-28 18:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 2395055a-b52e-30e3-a4c6-b4d4bba46a51 | -9.2093 | -59.4803 | 2026-08-28 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| c123072a-f9fc-37ab-8216-9559275ed103 | -6.7279 | -59.4423 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 3fcd816d-bb56-32de-bd44-ad93ceb71c49 | -12.9244 | -59.8843 | 2026-08-28 18:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 32f3e139-66de-322a-a405-931090d3dd40 | -6.9336 | -58.9514 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 185.5 |
| 9078f4b8-ebed-3c91-86c5-9c3545f5e5d9 | -3.8947 | -60.9399 | 2026-08-28 18:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 137.7 |
| 14543977-f395-3314-bc03-3f9edc42dc78 | -12.9054 | -59.8857 | 2026-08-28 18:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 93.9 |
| fc3fc82a-04af-3a1d-a3c3-fe5053f9e052 | -9.1978 | -61.0809 | 2026-08-28 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.5 |
| 539aeafe-ca6c-321c-9e06-eda41516fd16 | -9.4331 | -51.6716 | 2026-08-28 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| a2ae9352-bb87-30ac-a5d1-44dbf2fff00f | -11.7167 | -54.5244 | 2026-08-28 18:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 126.5 |
| d3532b7c-f8fc-3f89-bf53-74819334d841 | -8.776 | -50.0616 | 2026-08-28 18:30:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 8e0c18b4-61f1-3f48-8122-e5a28469fd20 | -7.3818 | -73.2449 | 2026-08-28 18:30:00 | GOES-19 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 21d41866-5467-3b2a-a04d-70cee6b578b1 | -8.0548 | -45.8616 | 2026-08-28 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 79.9 |
| d9c3d598-af3a-30ae-aac0-71d374e49d2a | -6.7648 | -59.4408 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| b01c394a-e799-3af0-9819-2bdf69601881 | -7.0289 | -55.6909 | 2026-08-28 18:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 7f211b10-402b-390a-aa6b-3eed86852e62 | -9.1714 | -59.5793 | 2026-08-28 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| e84c0c09-0a0b-3dd7-8200-0a443cdac4a7 | -8.0928 | -45.8354 | 2026-08-28 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 146.0 |
| 2ba39bca-5af3-3325-9278-7d2afc2dd4ed | -7.529 | -61.3635 | 2026-08-28 18:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| f601bd52-7131-3c7c-a3ed-5019718d4208 | -6.8386 | -59.4379 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| d40755a6-989c-3c69-8353-83f88377e674 | -13.471 | -57.0373 | 2026-08-28 18:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5a6c1364-68b1-332b-b526-8129a2e64106 | -5.7616 | -57.5612 | 2026-08-28 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| fb577b97-b75f-3c8f-9bec-1e0feba416e6 | -8.0737 | -45.8598 | 2026-08-28 18:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 68.4 |
| aec89cb5-adf4-3c41-be37-ad73b4c2512c | -6.1841 | -57.7786 | 2026-08-28 18:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| f9e10e76-4898-3e7e-bf60-0bc3e34533d4 | -6.7833 | -59.4208 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 4b21894e-7247-3043-87df-3050099e0444 | -12.9052 | -59.9053 | 2026-08-28 18:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 56.1 |
| d127357a-e6e2-33d6-a887-df7841b0630e | -10.8463 | -50.2224 | 2026-08-28 18:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 33bc6005-a4de-34bc-9b7c-1eefcf7b0f0d | -9.8742 | -60.2569 | 2026-08-28 18:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ad9bc743-2eb5-3491-a210-965f4df121a0 | -9.1711 | -59.618 | 2026-08-28 18:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| afd71a1e-8fd5-304e-b40d-588ab10c8cf0 | -6.8756 | -59.4171 | 2026-08-28 18:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| b73edc8b-ae0b-3371-8522-027123b3ad60 | -6.5138 | -55.2387 | 2026-08-28 18:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 862969ca-c276-3b15-94ad-964950b12803 | -9.4329 | -51.6926 | 2026-08-28 18:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 150.2 |


[Clique aqui para ver as próximas entradas](README160.md)
