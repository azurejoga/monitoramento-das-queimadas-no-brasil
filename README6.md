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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ee45cab-ab72-3dd0-908e-b86fd4cdbbe6 | -12.9526 | -46.217602 | 2025-08-21 00:46:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a3b522a6-179b-393e-9178-5c9a04ec2dcf | -12.9334 | -46.2229 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 935bb0b8-96c7-3038-b919-17937c1fbafa | -8.6321 | -62.122299 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 931a0757-9419-3f0a-a37a-4bde096d3abb | -15.8923 | -49.011398 | 2025-08-21 00:46:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c1917dfe-2533-30b8-a40f-64bd2a4cc4e5 | -14.3645 | -51.969601 | 2025-08-21 00:46:00 | METOP-B | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3e8e7fb-4860-3e34-a209-256cc6cfa7b2 | -13.0052 | -45.130001 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| defe3653-7b68-354a-b53d-379205dc482a | -13.0149 | -45.2047 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b45ec4ab-acf4-38f1-a3d3-c8ef665d91bb | -7.0528 | -59.813599 | 2025-08-21 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5d9bae54-eeec-330a-bc4f-cf495e0551aa | -12.9579 | -46.237999 | 2025-08-21 00:46:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7ff35297-1aa8-301d-9119-29bc365adcf2 | -8.6666 | -62.091599 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bd2b583f-c372-3cfd-8146-20bfa706d58e | -14.751 | -56.000401 | 2025-08-21 00:46:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b88a9d95-c22a-3175-851a-e48ad74ae059 | -7.8528 | -46.7118 | 2025-08-21 00:46:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c879c360-e7fc-3126-91de-83c2dd12bac3 | -7.0203 | -44.6478 | 2025-08-21 00:46:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e03be990-a68c-3fc3-ac20-dfcabc4c7fb6 | -14.8476 | -47.948101 | 2025-08-21 00:46:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 25e9c280-4847-33e7-9615-9090634bf97c | -13.5417 | -47.0518 | 2025-08-21 00:46:00 | METOP-B | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e1af1a8a-66fb-383f-8ebf-6afaf3261048 | -7.2668 | -50.171398 | 2025-08-21 00:46:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef618023-8f11-3901-acb9-9d92d63d79d5 | -13.1445 | -54.923801 | 2025-08-21 00:46:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 52a27c8a-aa61-3748-b4d9-e32b0a1cac0f | -13.1429 | -54.916801 | 2025-08-21 00:46:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edbaa069-d603-3a71-8eb6-899b8f5ce55f | -8.8453 | -52.033199 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3229165-2377-3e10-8058-9c2a0966388c | -15.0075 | -54.824799 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4a5fc97-5137-384f-8608-df6b5243c890 | -15.0008 | -54.841301 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 905024fe-a197-32bf-a370-1daf67a9727f | -14.9993 | -54.834202 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e9150c6c-0f15-32c7-8764-734f9a18264c | -12.943 | -46.2202 | 2025-08-21 00:46:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56b89ea4-ea87-3682-8b79-6d7d2f30c2b1 | -13.0021 | -45.156799 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7a69ba66-69fc-3a85-b3d4-7d7ae3e158b8 | -8.8281 | -52.047699 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b54ae8e5-5554-3116-a876-f89f655aad2f | -10.9906 | -55.243198 | 2025-08-21 00:46:00 | METOP-B | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0d5cedca-aad3-326e-8098-67e1d2eeb3d8 | -6.9435 | -62.876202 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a98d89c3-5da3-3208-b3a1-b42dcd6e47ac | -6.3524 | -55.5602 | 2025-08-21 00:46:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ec16ea4-ee1e-3f38-838f-4f9e194814b0 | -15.0204 | -54.8367 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 70f18b55-ea5a-3f6b-940a-be51abdd8e47 | -8.6298 | -62.111 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1581639a-141c-3b67-8d4b-c4eec89b4d15 | -5.1339 | -56.960701 | 2025-08-21 00:46:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba91a8bc-9102-3d87-b7f2-562a2c90c337 | -14.4971 | -45.962002 | 2025-08-21 00:46:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71c10a2c-0cca-35d7-870a-eeda63f9655d | -7.0119 | -44.614799 | 2025-08-21 00:46:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 80c4b820-3fbb-3409-967b-451ce549c348 | -14.7526 | -56.0075 | 2025-08-21 00:46:00 | METOP-B | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 85eee26a-0003-365a-9944-89d6e2ba8d35 | -8.8355 | -52.0355 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59583b97-730d-3ca5-999e-6ee10e1b559c | -6.4463 | -53.367298 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f51140bc-e6a0-3068-abd0-0b6b35c179aa | -4.3098 | -48.082298 | 2025-08-21 00:46:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64a072fd-e90a-313f-ab25-cd0ba8c7de3a | -8.6224 | -62.124401 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 692a8199-13e8-36f9-b540-44f1edeff236 | -7.0546 | -59.821602 | 2025-08-21 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2954230e-09de-3fa7-87e3-ae17a094a96b | -7.0563 | -59.829601 | 2025-08-21 00:46:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 644af863-837d-39c0-a6a0-56901ef7afa9 | -14.6275 | -54.876202 | 2025-08-21 00:46:00 | METOP-B | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 829d77db-ea88-3d12-b186-90d3042a6888 | -9.9137 | -49.2813 | 2025-08-21 00:46:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6988f1c1-b132-3ed5-a95f-3141724b9e0c | -8.3773 | -54.992298 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6849bacb-32eb-3015-9626-3b5396947bb8 | -11.4959 | -50.517601 | 2025-08-21 00:46:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 675ce528-0507-33c1-8b4a-4aa9b4726fe0 | -16.0424 | -49.073601 | 2025-08-21 00:46:00 | METOP-B | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e7808e8b-58be-3b52-8b2b-12bac0cceb38 | -8.6372 | -62.097698 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 726410aa-226a-3493-ab48-0df0d7e9522c | -5.8862 | -57.7435 | 2025-08-21 00:46:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a033e8b4-7995-372e-a715-25211e181bd7 | -14.8499 | -47.916199 | 2025-08-21 00:46:00 | METOP-B | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b27cba62-b701-326c-88b4-1d231ef49e0c | -13.5275 | -47.0368 | 2025-08-21 00:46:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| dea900da-853b-3d35-8d4b-e510b149eb46 | -14.4917 | -45.941898 | 2025-08-21 00:46:00 | METOP-B | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b17c4252-aad6-3330-83e3-1325a1b32497 | -8.6861 | -62.087502 | 2025-08-21 00:46:00 | METOP-B | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b03f8633-09fe-3e0a-96b0-fc5eedc4777a | -12.9765 | -45.2155 | 2025-08-21 00:46:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7535ce28-1673-3256-ba12-c63817f0c201 | -10.7153 | -48.234402 | 2025-08-21 00:46:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e6f9fbe-5e8a-35ba-bbbe-e1eeff749ba9 | -13.1413 | -54.909698 | 2025-08-21 00:46:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93183c38-3886-3d99-971c-ed8ae5d75155 | -15.0091 | -54.831902 | 2025-08-21 00:46:00 | METOP-B | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3c2d44c-270d-32cf-9e62-58bc81bd6bd8 | -8.4298 | -49.575199 | 2025-08-21 00:46:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1eb5b07-a4ee-3555-9c95-03a92670cf9d | -8.379 | -54.999599 | 2025-08-21 00:46:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1c08b43-419b-37ac-8f74-f54eb8072135 | -8.8378 | -52.0453 | 2025-08-21 00:46:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3700f17a-7500-3a34-b06d-1bb632ec2913 | -16.0598 | -49.067 | 2025-08-21 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 9c6a5d9b-3e93-3f60-866b-4c65e4a2843f | -7.0166 | -44.6184 | 2025-08-21 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 181.1 |
| 40d33b60-ba56-33a9-8645-746759b20a88 | -13.1367 | -54.9171 | 2025-08-21 00:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 9cf9510b-b0bd-3e7f-bb1e-40c17d186111 | -8.8551 | -62.4123 | 2025-08-21 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.1 |
| 118eaa7e-96ec-3485-acba-5fff9bbaea2f | -7.0354 | -44.6167 | 2025-08-21 00:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 3ff5bf7c-1e3c-3c89-8606-4a5c1cfe3a67 | -15.9046 | -49.0043 | 2025-08-21 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 49.6 |
| 0ffb006f-0034-37c5-82d9-5f81c4331cc0 | -12.9533 | -46.2419 | 2025-08-21 00:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 0a5910b8-5164-3499-a0a7-494d2d7b5d0f | -8.8735 | -62.4305 | 2025-08-21 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 47c39ee8-014c-3d81-be48-a7daff6c0ebf | -15.0193 | -54.832 | 2025-08-21 00:50:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 85c5b53d-f211-38b1-b3e4-57fbf33850f5 | -8.8552 | -62.3933 | 2025-08-21 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 229b9c32-cd3d-3bf7-bd82-0276a5bf757a | -5.9526 | -44.1326 | 2025-08-21 00:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4f69e0ce-fc69-3cde-82ce-c455a483f6eb | -8.8737 | -62.3925 | 2025-08-21 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d55e3e71-a01f-3a24-9ad1-84cff69a5a03 | -15.8849 | -49.0076 | 2025-08-21 00:50:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 59d77195-0c58-3c30-9d34-2ab3ad2e097f | -12.9537 | -46.219 | 2025-08-21 00:50:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 4a12560a-e91e-39f6-834f-b914f827d5c7 | -8.8736 | -62.4115 | 2025-08-21 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 71e80679-af07-3420-bc46-6d46706bbe65 | -14.8543 | -47.9279 | 2025-08-21 00:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 64.3 |
| f55c9770-f100-3406-a809-8d2ca8bdd97b | -8.8922 | -62.4107 | 2025-08-21 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6ad00d00-3f05-398f-928e-12a95cf57085 | -14.8538 | -47.9504 | 2025-08-21 00:50:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 0b8f1d7b-807c-3836-b90e-99e9b7ea1717 | -8.3714 | -54.9919 | 2025-08-21 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| af57d128-c3d3-312e-b28a-1c1653c68f90 | -12.9533 | -46.2419 | 2025-08-21 01:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 133.1 |
| 7f1a792c-3404-3595-8706-cb6b49a4fad7 | -7.0354 | -44.6167 | 2025-08-21 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 9a3b0e68-50f0-3787-952b-076db490cab0 | -14.8543 | -47.9279 | 2025-08-21 01:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 65.1 |
| f4f77d2f-55f7-3f6b-a012-4d4a47c1e8a3 | -9.6446 | -40.5847 | 2025-08-21 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 82.2 |
| 904b2cdd-27b4-385e-83ff-0ea4098c62a8 | -12.9537 | -46.219 | 2025-08-21 01:00:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 269aa685-21e9-3afb-95a3-088d6aff1244 | -15.8849 | -49.0076 | 2025-08-21 01:00:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 949cc162-7f01-3377-b278-5137ba496697 | -7.0166 | -44.6184 | 2025-08-21 01:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 224.0 |
| d146ac99-22cf-319e-a4ff-cf89790883a7 | -8.6343 | -62.1367 | 2025-08-21 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 41.2 |
| 0da9e244-ca71-3d06-a6f5-ef2a6b4f1b61 | -14.8538 | -47.9504 | 2025-08-21 01:00:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cd2db017-4bb2-3b80-b893-d60d5bec775d | -14.8538 | -47.9504 | 2025-08-21 01:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.8 |
| daa63ea0-e5c6-358c-b2df-180b1233cad5 | -8.6716 | -62.0971 | 2025-08-21 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| eed0778d-c5fa-3e4e-abf0-0af6ccce2917 | -8.6157 | -62.1374 | 2025-08-21 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| a47264b2-87ca-34ee-a1a7-e5b5deed0226 | -8.6158 | -62.1184 | 2025-08-21 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| fa807a7a-aea3-3b21-b77f-7bfa19573047 | -7.0354 | -44.6167 | 2025-08-21 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 8187d140-88fc-36e4-85ab-2ef0c6e63bad | -7.0166 | -44.6184 | 2025-08-21 01:10:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 200.8 |
| 680916ec-43ee-39db-8a70-cc17079d3b74 | -14.8543 | -47.9279 | 2025-08-21 01:10:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 8ec3f949-2970-3278-86c8-4eb1cc00db8d | -9.6446 | -40.5847 | 2025-08-21 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.1 |
| 8880a6fb-0c24-3e0e-97ef-86aefcccad05 | -8.8737 | -62.3925 | 2025-08-21 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.4 |
| b6ad12da-7358-3ec6-916c-01ac80a24ed8 | -12.9925 | -45.202 | 2025-08-21 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 66fb0772-c5d8-3508-9ee5-4d3e8fa000bc | -8.6343 | -62.1367 | 2025-08-21 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 5799ca9a-2500-30e1-b08a-9e0d56f557d1 | -12.9533 | -46.2419 | 2025-08-21 01:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| fe721575-31e9-3d16-98fb-525a1f74d32b | -12.2196 | -45.3922 | 2025-08-21 01:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 59.7 |
| b0d81d56-95d3-3eec-a1fd-c0342256336f | -9.625 | -40.6122 | 2025-08-21 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |


[Clique aqui para ver as próximas entradas](README7.md)
