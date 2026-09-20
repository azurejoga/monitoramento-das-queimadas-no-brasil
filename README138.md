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

## Dados Diários - Página 138

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 58bdc356-7c6b-3feb-8dac-86a0fa377405 | 2.1818 | -50.8985 | 2026-09-20 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 9e9266aa-3ab3-3950-a8c9-883bc051a47d | -11.0614 | -49.7477 | 2026-09-20 15:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 192.5 |
| f2aa3852-1c77-33e2-b672-e13652274d22 | -3.331 | -59.8292 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| e1833219-e5be-38dc-9114-efbb55603966 | -3.1444 | -61.4074 | 2026-09-20 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 610cd042-27ee-30eb-a934-76bd3d43f98e | -3.1444 | -61.3885 | 2026-09-20 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 925fd298-8aca-3c0a-bc42-b22ddd2a6a51 | -9.8313 | -48.4073 | 2026-09-20 15:30:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 157.1 |
| 495bc6cc-86f5-3053-9d1c-286d87fa46d9 | -6.8216 | -59.1686 | 2026-09-20 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 597e6804-975a-3ed1-9bfc-609961c8e268 | -1.7316 | -54.9518 | 2026-09-20 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 8b2b2203-c816-3a8f-b378-dd04481dfee8 | -11.1183 | -54.0062 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 212.8 |
| ad50c9a6-77a0-3610-920f-ff9b8237b11c | -3.3359 | -58.1191 | 2026-09-20 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 31af6a8e-119c-3bad-a982-cef8a97e6e4a | -11.1225 | -49.4601 | 2026-09-20 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 124.5 |
| ee2377a7-3a97-3612-b877-260adcb4c5e6 | -9.9956 | -50.2675 | 2026-09-20 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8d1725c3-707f-3d6c-946f-8928f32f3c9b | -9.9328 | -53.9859 | 2026-09-20 15:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 8adbb600-df4c-39f8-8770-34ae00314c1b | -3.1261 | -61.4077 | 2026-09-20 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d9649500-070e-3959-9131-58c3e0fd34b0 | -13.2798 | -51.7312 | 2026-09-20 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 243b3824-7722-348b-9d31-d83c0dfaad49 | -6.8433 | -55.7602 | 2026-09-20 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.3 |
| a8cd34d2-de13-3cb7-b730-6023dc1fde01 | -6.3471 | -58.2973 | 2026-09-20 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 29364231-a4d3-35e4-b4ab-e641af53a0bc | -8.3774 | -47.1917 | 2026-09-20 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| dd72467d-c325-387b-a9ef-0a4a08b4e9d2 | -9.2606 | -45.9164 | 2026-09-20 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| fc5b0484-b701-3083-aefc-b1e6e24ed0ae | -13.2414 | -51.7359 | 2026-09-20 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 102.0 |
| 1c2c81de-a87f-38c1-80ea-8fe2440290db | -2.9143 | -58.3401 | 2026-09-20 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 2f83df36-54be-3f5c-93f5-e94761e6b777 | -11.6621 | -50.2169 | 2026-09-20 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.9 |
| 046a5212-7ab3-3c35-bc04-4eaf170f7ded | -5.9814 | -57.7867 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| c7946ac7-0147-3ee7-adeb-3c7103a74487 | -6.2026 | -57.7778 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| aabb9cca-a0e8-318f-8465-17dd46b4e39a | -13.2027 | -51.7618 | 2026-09-20 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 0f412c0e-cac0-37be-9dad-85883b46d7d2 | -11.0412 | -54.1362 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| f32343ef-30bd-32ec-b45e-d749a27612ae | -7.3289 | -55.2155 | 2026-09-20 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| d88e9f43-69d5-3df1-96c3-a0b2dde0ead3 | -11.4732 | -45.3635 | 2026-09-20 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 121.1 |
| cc814529-3f4b-3dc8-ad18-5917e9bb12c1 | -11.3612 | -51.3374 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.4 |
| 159a467f-a09f-3399-8c3e-3c0cd8978e5e | -3.3321 | -59.4469 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| f8dc21a2-d41f-3895-b454-c3719a7f3d83 | -11.0617 | -49.7261 | 2026-09-20 15:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 1ae33568-f6ac-39c9-8baa-2464677fea47 | -2.9326 | -58.3397 | 2026-09-20 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 5eb708d3-ec1c-3ee5-a466-ea8ab8eae981 | -10.8757 | -57.1554 | 2026-09-20 15:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 136.2 |
| c0f8e85f-78c8-3328-b0af-7845b096ae40 | -8.6171 | -54.6126 | 2026-09-20 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| aee56a5e-4fcd-3887-9d03-44bf75c41d71 | -6.1981 | -55.4534 | 2026-09-20 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| b84a6891-b70e-3d42-aaaa-325bc1733541 | -8.5984 | -54.6139 | 2026-09-20 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 3e1f6466-42a2-36cd-b160-81236e151de5 | -6.4671 | -59.9711 | 2026-09-20 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 179.9 |
| 42fe3fdf-aa56-3b30-9623-7c02c59e6743 | -11.1222 | -49.4818 | 2026-09-20 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 141.6 |
| f1cefcbd-7cd2-38f1-816d-0897d76fb96e | -11.379 | -51.42 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 227.3 |
| a2f5802c-1a36-35b6-aa24-02d8bed7f1de | -11.4545 | -45.3432 | 2026-09-20 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 71700063-1606-34b7-9391-374f6423da37 | -10.0956 | -48.4226 | 2026-09-20 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 119.1 |
| 3d624903-bc1f-36b7-bdc1-142d7bc0b888 | -3.3492 | -59.867 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 17f68ed0-5cdf-32b9-9208-75645046c8f9 | -10.4547 | -51.2405 | 2026-09-20 15:30:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 4509c89b-5aac-35f8-a693-118a222a5951 | -3.1079 | -61.408 | 2026-09-20 15:30:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 9d954230-fb1b-31ce-9c43-5c6046f37c1b | -10.9665 | -49.7583 | 2026-09-20 15:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| bccfab29-1930-39e6-a6d8-70d1a5154e39 | -8.3581 | -47.2378 | 2026-09-20 15:30:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0fc4c9e4-63a0-3a9c-872b-5e05c86ff9df | -3.331 | -59.8483 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 2445c5f9-419d-3abe-8338-f9b853211443 | -2.8779 | -58.2828 | 2026-09-20 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| fadae9e1-453e-3275-9a9d-6bba4406110b | -9.5695 | -45.4729 | 2026-09-20 15:30:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 89.6 |
| a5f30d78-2ac4-3699-b309-f8edd6e3e915 | -13.2606 | -51.7335 | 2026-09-20 15:30:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 01f017ad-cdbb-3acd-ba12-8fd9cd0461c0 | -11.9352 | -49.7752 | 2026-09-20 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 229.4 |
| d7ad8808-ae0f-351e-b745-af71b35a540d | -11.4736 | -45.3405 | 2026-09-20 15:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 124.7 |
| 06df2e70-9737-33e2-9dea-53262d5b3654 | -3.3358 | -58.1384 | 2026-09-20 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 4b81d804-e0e2-3322-8a17-cb19b68ddb0f | -11.9349 | -49.7968 | 2026-09-20 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 262.8 |
| f1607773-e7c0-37e9-b5eb-d2d29da0f71d | -6.5444 | -44.9327 | 2026-09-20 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 6d915df9-45f1-3a58-ad92-24c13fd09067 | -6.1109 | -57.684 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| be86e17e-ec69-3d99-a447-a5d7d35255f2 | -9.6668 | -54.3129 | 2026-09-20 15:30:00 | GOES-19 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 9de4dd3c-3e1d-3090-9b31-f6561e21f883 | -11.1372 | -54.0045 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 231.3 |
| 6ec116c1-62f7-3804-ada8-1a1dd2279a76 | -6.0928 | -57.6262 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 5426022e-72fc-3a47-8eb4-3c3f99718781 | -11.0611 | -49.7693 | 2026-09-20 15:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 129.0 |
| e9b43784-3ac4-3593-9dae-ac389c264eda | -7.6449 | -57.6141 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 8027e643-ce8a-31b1-beec-8f94e960b604 | -6.4402 | -58.138 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.8 |
| bb17fe1c-643d-319e-aefd-fcbbe966276e | -5.7429 | -57.6009 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 30a552ae-b4fe-3cec-ba15-917ab2e01d02 | -8.0894 | -55.331 | 2026-09-20 15:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 131eb294-3f2f-3770-8bb3-1e9189aff315 | -3.4049 | -59.5794 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 9c0685bd-aa5b-31a8-bb28-42b0cdc01e2c | -3.2955 | -59.4476 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| dcef3a16-53ef-3f95-a770-4b0a669bc3d0 | -3.2955 | -59.4284 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 0ca7a1f9-61da-3bff-99a7-a9cd641d59eb | -5.9815 | -57.7672 | 2026-09-20 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| cd968cb9-63ca-321c-b37b-1a694efc1d25 | -6.7483 | -59.0943 | 2026-09-20 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.6 |
| 0a7603df-8f49-3e2d-9853-17433a491766 | -9.0353 | -48.7704 | 2026-09-20 15:30:00 | GOES-19 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 0d048de6-3df1-39a7-bd53-de932618539d | -7.0286 | -45.2554 | 2026-09-20 15:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 113.1 |
| 50fd0551-f897-3707-b709-f1f3d9ad018b | -6.1231 | -55.6359 | 2026-09-20 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| c15e9641-86f6-3276-9079-11b25d4b9ce7 | -1.75 | -54.9317 | 2026-09-20 15:30:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 5af60e5e-9d4a-37c2-a9eb-d6d69486f154 | -11.0221 | -54.1584 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.1 |
| a2c9dbe2-6258-3abb-9e27-8ca978bd945c | -3.7347 | -59.4002 | 2026-09-20 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 56cfb65c-db2d-3018-9ef8-3472ee909bfd | -10.41 | -48.933 | 2026-09-20 15:30:00 | GOES-19 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| f05e9031-9923-3079-8215-fd86156764f2 | -3.5894 | -59.0581 | 2026-09-20 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 6d47a66f-5885-3f2f-89cb-37619a9c4b81 | -10.7463 | -50.6172 | 2026-09-20 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 154.2 |
| b09327de-00e5-34ae-a4cf-e4365467f50d | -11.08 | -54.0507 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 1128c015-3584-3d04-a381-9de6f474606e | -11.9543 | -49.7728 | 2026-09-20 15:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 189.0 |
| e947e2b4-4fd8-355f-8ec2-c4d959a81dbe | -8.7919 | -48.6851 | 2026-09-20 15:30:00 | GOES-19 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 7c8ba9df-e94a-3c1c-bb47-f135c58967f7 | -10.2598 | -50.2624 | 2026-09-20 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.5 |
| ebac954d-af85-32fc-843e-057be8a98511 | -11.3986 | -51.3757 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 86.0 |
| 0941e196-4b31-3dd7-a252-4a118e70778a | -3.5356 | -58.6939 | 2026-09-20 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 74d6d9d4-e57a-3957-9f9f-6c9e39ca6771 | -6.001 | -51.7903 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 3be99ad6-f1a1-3e1f-93cb-9e2dab00a50b | -3.5893 | -59.0773 | 2026-09-20 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 00fe42ca-8e72-31bc-927b-a64b0bae2c44 | -10.279 | -50.2391 | 2026-09-20 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| d4eda4c6-7582-3cde-b0e3-0c68b5ad3a94 | -2.8961 | -58.3018 | 2026-09-20 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| a13820ec-2e64-3620-bca7-45e78c77169c | -2.9709 | -57.7197 | 2026-09-20 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5f62846c-684b-3d5f-8580-f264183e76e9 | -11.0259 | -48.2944 | 2026-09-20 15:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 4bfab390-0a26-32d3-a36a-05c9f4d8fcb9 | -8.4737 | -47.0053 | 2026-09-20 15:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f726c62c-6230-3e6f-b089-11e326c7befb | -10.2793 | -50.2177 | 2026-09-20 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 4e22d6d9-f20c-3ab1-b17b-db4c1669bb98 | -8.7917 | -48.7068 | 2026-09-20 15:30:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 95.9 |
| f9c260b0-d5a8-367c-824d-5f15678cb3bf | -2.8962 | -58.2825 | 2026-09-20 15:30:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 0b45dfca-e23a-3185-9a7e-e7b05f641bc6 | -6.737 | -55.0674 | 2026-09-20 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 202.5 |
| be3188d0-df86-3c42-9b68-fdccbab497f2 | -11.0223 | -54.1379 | 2026-09-20 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| caf88ada-105b-3272-9bc6-ded0268f4959 | -6.3286 | -55.2877 | 2026-09-20 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| c23aa31b-5df5-3a5f-94b2-e49c8150b352 | -11.398 | -51.418 | 2026-09-20 15:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 100fdfa9-9417-3cd8-a5c2-878b66cdc6dd | -6.7185 | -55.0684 | 2026-09-20 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 162.2 |
| a789f289-61fe-39fa-9e9b-ffdb9ca7e058 | -3.3866 | -59.5797 | 2026-09-20 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |


[Clique aqui para ver as próximas entradas](README139.md)
