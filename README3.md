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
| e435dd81-b60b-3765-8da8-ede4a40347ed | -11.0553 | -49.574001 | 2026-06-23 01:03:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 79c07dda-cb4a-3a9a-94df-711246f88e2b | -12.8492 | -44.324699 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 982c4d35-e187-321f-b4e2-f647f2737901 | -13.501 | -56.570801 | 2026-06-23 01:03:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0c85136-0c07-36a5-bc9b-b6470413ef3b | -12.8445 | -44.345901 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5beea2ef-308e-3782-9ad9-e4bbe91f5afa | -12.9212 | -49.467999 | 2026-06-23 01:03:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 00f85e88-ce16-3c6f-a43d-eb3e70ce21bc | -8.983 | -47.9739 | 2026-06-23 01:03:00 | METOP-C | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf3e5a04-7112-318f-afae-6fa3131543f0 | -16.0333 | -43.412498 | 2026-06-23 01:03:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a6b71fe2-fdb7-384d-a6b5-6326a25d0ea7 | -6.3706 | -43.579899 | 2026-06-23 01:03:00 | METOP-C | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3d030986-c30a-395c-92fe-486833a78f9a | -12.9233 | -49.476799 | 2026-06-23 01:03:00 | METOP-C | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3d4ee076-4c8e-31a1-8cdf-9f56ce362afb | -5.8281 | -45.043098 | 2026-06-23 01:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d2ade452-86cd-32a8-bf3a-512fcb9fbccb | -11.8081 | -52.5187 | 2026-06-23 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b77b9af-85a3-31bb-9b77-1a95b2f4410c | -6.9365 | -51.932701 | 2026-06-23 01:03:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9502fbac-e496-3985-9a15-66bcce8e4b0f | -11.7991 | -47.332699 | 2026-06-23 01:03:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddcb612b-6f4e-3b5d-a482-01bd4cbba646 | -12.8493 | -44.3643 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 73132cfc-dae3-378b-b97c-384c0f5081ee | -12.5126 | -48.2953 | 2026-06-23 01:03:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1ee27874-cee6-3705-989c-4ebcf2447a35 | -11.8097 | -52.525799 | 2026-06-23 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93ac90c5-0773-3aa5-a21b-9bf1f3255c4e | -5.8238 | -45.067101 | 2026-06-23 01:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 339b9088-fb7f-3eff-9676-8cb4e71ee78e | -10.567 | -46.2108 | 2026-06-23 01:03:00 | METOP-C | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a4ac9e98-a2bd-35fb-9b21-d00ca30b746f | -12.5076 | -48.274502 | 2026-06-23 01:03:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7987234a-3c67-30c0-b109-eabd14f94028 | -21.8461 | -47.237099 | 2026-06-23 01:03:00 | METOP-C | SANTA CRUZ DAS PALMEIRAS | SÃO PAULO | Brasil | 3546306 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 41a993c4-6f91-30f1-97a2-05a3ea14b8e5 | -11.5101 | -56.125702 | 2026-06-23 01:03:00 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63d00ba3-d43f-366b-a7a5-5df18c455c1f | -12.8589 | -44.361599 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 680b33f1-bbc3-3b5c-9f4f-60fd4e34c23b | -12.8782 | -44.3564 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d60548e2-43e3-3faf-884d-207cc4624227 | -11.7999 | -52.528099 | 2026-06-23 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a3079524-b34e-37de-84b5-eaea53abd9bc | -10.7766 | -54.105801 | 2026-06-23 01:03:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0dcd0488-2cf2-3ba1-9038-de8488ed1715 | -11.5748 | -47.428501 | 2026-06-23 01:03:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 47833ba0-d71b-345b-abb0-35fdebf37349 | -11.0543 | -52.4702 | 2026-06-23 01:03:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2c00a7ca-b106-3110-b758-2d209b98018a | -6.9383 | -51.940498 | 2026-06-23 01:03:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca1f204-15b8-3c08-961d-c33f24ebf3d6 | -10.8814 | -49.538601 | 2026-06-23 01:03:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78873f3f-0577-3a8c-9ed2-097e905081b3 | -11.283 | -55.7896 | 2026-06-23 01:03:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| be18ae71-ed44-3f7f-8297-fdccc5dd066f | -10.3851 | -56.709999 | 2026-06-23 01:03:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7fb67ea-a5eb-32e0-b416-e19db5f635bd | -12.8686 | -44.359001 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f08ed12-d84b-3f2c-ae08-3afcb2a32953 | -12.547 | -57.191101 | 2026-06-23 01:03:00 | METOP-C | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 05659b4d-aa1b-38ee-bec3-6cd54f789884 | -12.425 | -58.418201 | 2026-06-23 01:03:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 009c9c44-7260-3e0b-8a1e-41d1b75d1fd7 | -11.0511 | -52.456001 | 2026-06-23 01:03:00 | METOP-C | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aaa89a86-f53b-3227-9a80-967e19ad53a4 | -11.3033 | -54.713699 | 2026-06-23 01:03:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8e3861a3-d060-34c4-b7b4-4b3405504309 | -11.7983 | -52.521 | 2026-06-23 01:03:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 55594065-bbb0-3cc7-ac1d-ea667b6dc9dc | -5.8184 | -45.045502 | 2026-06-23 01:03:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d41e3214-e712-3afb-8ebc-4dc5880a9c97 | -12.505 | -48.264099 | 2026-06-23 01:03:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3abbfb2-fc56-30dc-bdcc-4f61cdee69f4 | -12.4227 | -58.407299 | 2026-06-23 01:03:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 71d4467d-d19e-344b-a93d-79d90b06dfd8 | -12.8541 | -44.343201 | 2026-06-23 01:03:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d6085de-f088-341f-a770-5347f549684a | -12.4303 | -58.394402 | 2026-06-23 01:03:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8ca19f14-2352-33b5-b50c-5ef1b3eef3da | -11.8742 | -57.8326 | 2026-06-23 01:03:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| aa7439dd-3780-32c2-ad05-fcf42ee27736 | -12.662 | -47.684299 | 2026-06-23 01:03:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b3aad95e-5ab7-3d93-8310-c1c7c864f702 | -10.9067 | -54.135201 | 2026-06-23 01:03:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bab9af4d-4d60-3571-bfcb-4ecd3a4092d4 | -10.8836 | -49.547798 | 2026-06-23 01:03:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7b2ca37a-f85c-316b-a817-9acbb9268207 | -12.5223 | -48.292801 | 2026-06-23 01:03:00 | METOP-C | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 078f658a-d9d9-3b5a-bad0-ad2dcc798b25 | -11.5778 | -47.440498 | 2026-06-23 01:03:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cae513c7-323d-384f-8748-b231220eb4d7 | -10.9769 | -48.145302 | 2026-06-23 01:03:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f9a0a664-a850-300c-b904-1702ee0953b5 | -9.2278 | -45.322399 | 2026-06-23 01:03:00 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1e1cedab-41d6-3013-8efc-0ea5793f7abf | -13.5028 | -56.579601 | 2026-06-23 01:03:00 | METOP-C | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1de01f04-9975-3572-8f86-7081d9c2556a | -8.8715 | -46.9375 | 2026-06-23 01:03:00 | METOP-C | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b43d5faf-d58e-35f0-8246-cfb800a36e24 | -12.0379 | -47.795101 | 2026-06-23 01:03:00 | METOP-C | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 755d3a9f-2163-3ca8-8a9c-63f07b6b41e0 | -12.6592 | -47.673 | 2026-06-23 01:03:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cace1b2e-7aaf-32bd-bb43-9aa43492802f | -16.0282 | -43.3936 | 2026-06-23 01:03:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| f5c08aad-b5b0-3ea3-9ade-9740f2919c4b | -9.4623 | -49.823601 | 2026-06-23 01:03:00 | METOP-C | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92ed03ba-c55d-3233-b86d-006afa374ebd | -12.8741 | -44.3593 | 2026-06-23 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 264.4 |
| a4b1ada9-900d-3847-bcee-a7ee5e45a2ed | -12.4283 | -58.4048 | 2026-06-23 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 29fcb30f-555c-32c1-b27e-8307920e38b8 | -12.8548 | -44.3625 | 2026-06-23 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 263.1 |
| f0aa152d-a01a-399f-8f68-19a50f9700b4 | -12.8552 | -44.3389 | 2026-06-23 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.6 |
| f66ed7f4-cfe4-3d13-b74d-55ab8cf47901 | -12.8746 | -44.3357 | 2026-06-23 01:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 27bdbb3a-35d9-31be-ac49-450096aa8933 | -5.8319 | -45.0559 | 2026-06-23 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.7 |
| 128188e5-b5ac-31d2-a582-5fe29886d31a | -12.8552 | -44.3389 | 2026-06-23 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 2fe362f7-33cc-3686-bf93-c772f5f576cf | -12.8548 | -44.3625 | 2026-06-23 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 252.5 |
| a04e2c8b-ef3f-32cc-82a0-dacc0b4a7896 | -12.8741 | -44.3593 | 2026-06-23 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 253.4 |
| 8f6c45c7-b9cb-34d8-8951-22e42e86a7bd | -12.8746 | -44.3357 | 2026-06-23 01:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 056e92b5-4f25-397d-a1ad-a5138f0fcf94 | -12.4283 | -58.4048 | 2026-06-23 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 0ff7fa9a-90f4-3f05-baa7-2ce19bf541e9 | -12.8548 | -44.3625 | 2026-06-23 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 237.8 |
| 453c5d28-796f-353b-8221-33a12a501dba | -12.8746 | -44.3357 | 2026-06-23 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 1de4f2d7-59b7-34e5-b5bb-e4724e42457a | -12.8741 | -44.3593 | 2026-06-23 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 270.2 |
| 317b0c0a-54a1-3d74-bc8a-60c4e747ff10 | -12.8552 | -44.3389 | 2026-06-23 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| d1dcd1ae-8ae9-3d65-b068-5d517d443def | -5.8319 | -45.0559 | 2026-06-23 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| ec2d8266-a595-3449-b4fc-0a7d293ced8d | -12.8746 | -44.3357 | 2026-06-23 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| 87cfec8c-239c-3bc9-974d-4ee5b32f8930 | -12.4283 | -58.4048 | 2026-06-23 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 72cb1b1f-10b4-3250-a0ec-a37fd6419e74 | -12.8552 | -44.3389 | 2026-06-23 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 123.5 |
| bb41878b-b7a6-31d3-8a3b-6c22572cf68a | -12.8548 | -44.3625 | 2026-06-23 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 222.6 |
| 6b1616a7-89e5-3e95-9467-926965858748 | -12.8741 | -44.3593 | 2026-06-23 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 240.9 |
| cf680958-53fa-3970-9dca-68097d927dcf | -5.8319 | -45.0559 | 2026-06-23 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 9dfa9348-2033-3c2e-afa1-38260cb47f7a | -9.2309 | -45.3299 | 2026-06-23 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 57.2 |
| 74b93a49-4151-319e-9f2c-8a048cf047ac | -12.8552 | -44.3389 | 2026-06-23 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 126.1 |
| de8aed1f-40f2-3d6a-8280-b83eb6357c48 | -12.8548 | -44.3625 | 2026-06-23 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 237.4 |
| 0e8655e6-e195-3e53-b2cb-fbd1fc60c5bf | -12.4283 | -58.4048 | 2026-06-23 01:50:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 0a376578-1581-31dc-b351-b924dee91c4d | -12.8746 | -44.3357 | 2026-06-23 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.6 |
| a04e1362-ab84-31b0-b484-674edcffaa72 | -12.8741 | -44.3593 | 2026-06-23 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 193.4 |
| 33010bfd-5ff5-3ff8-928d-6faf4c7d5016 | -9.2309 | -45.3299 | 2026-06-23 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 8f01396e-49e1-3e4a-9253-0f1c119b6d06 | -12.8548 | -44.3625 | 2026-06-23 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 195.1 |
| 00f00ca6-efae-317e-8986-5717b395d1d8 | -12.8746 | -44.3357 | 2026-06-23 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 1616b342-7ba3-3f65-9447-37accd54fe29 | -12.8552 | -44.3389 | 2026-06-23 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 18e0d57e-1953-3a3d-8db0-c1c3537dbe6e | -12.8741 | -44.3593 | 2026-06-23 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 206.9 |
| 8ea704bf-92cb-3122-8372-33fd54dc1544 | -9.2309 | -45.3299 | 2026-06-23 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 58.1 |
| aeed9a80-f804-3886-bc03-9f91129fb486 | -12.8548 | -44.3625 | 2026-06-23 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 235.3 |
| 9fcc2f83-0c23-306f-9e1b-d2e47e3d70ba | -12.8741 | -44.3593 | 2026-06-23 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 205.9 |
| 51b6dc46-9332-3b63-99da-133d75773a55 | -12.8552 | -44.3389 | 2026-06-23 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 35bd9587-6ac4-32bc-aa9e-1c1ce29ab3c4 | -9.2309 | -45.3299 | 2026-06-23 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 90bf32f1-df0e-3752-8d5a-455679c3f77e | -12.8746 | -44.3357 | 2026-06-23 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d102a63b-4a42-3e78-b997-2de5e07b27c2 | -12.8552 | -44.3389 | 2026-06-23 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 105.7 |
| ec1e0748-58d5-3092-86a1-dfcf460c53c7 | -12.8548 | -44.3625 | 2026-06-23 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 197.0 |
| a8b2bea7-ce4f-31c8-9dda-3d767b7ebadd | -12.8746 | -44.3357 | 2026-06-23 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 5c5a3d9c-0a12-3842-b337-5b8c15d47be4 | -12.8741 | -44.3593 | 2026-06-23 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 200.5 |
| 88fa1be3-47c6-39c9-b3ca-a7b3412e9357 | -12.8746 | -44.3357 | 2026-06-23 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 118.4 |


[Clique aqui para ver as próximas entradas](README4.md)
