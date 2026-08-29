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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4baa0710-b82c-3937-a83d-03ce23797457 | -12.209 | -50.5601 | 2026-08-29 16:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| a4a22d41-d88d-3c3d-88d7-ab2ee04d5855 | -4.0574 | -56.2865 | 2026-08-29 16:00:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| 3daeabfe-b2f0-36d6-80ca-65fba65b4cd4 | -10.7598 | -54.0179 | 2026-08-29 16:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 55c4580c-6d7b-3d40-97ec-a25ce9f6ba4a | -9.9708 | -53.9419 | 2026-08-29 16:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 270.6 |
| 77b5d72a-056d-3181-8e95-24065715929b | -8.631 | -66.5473 | 2026-08-29 16:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 87.6 |
| adf33999-2924-30e8-b77f-6ad319cd5c42 | -3.2361 | -61.2359 | 2026-08-29 16:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 734f4702-b588-3195-8d9b-31f51fd5a8ea | -17.2938 | -46.0291 | 2026-08-29 16:00:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 37c496ec-6ea0-3712-b129-f1f0d5b23ddb | -9.971 | -53.9214 | 2026-08-29 16:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 274.9 |
| bac60b09-1227-3f5a-9d4f-acac1696f83b | -11.1913 | -51.292 | 2026-08-29 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 107.5 |
| 4680ece1-9a4f-3df5-ae98-80e3eec196cd | -12.2281 | -50.5578 | 2026-08-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 8be4739f-cbff-3fd8-bb85-a5418a5af359 | -10.76 | -53.9974 | 2026-08-29 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f9203350-ae90-34e8-a6ae-42089bdc29bd | 0.1549 | -60.393 | 2026-08-29 16:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 409e7519-8197-3682-813d-027678708572 | -11.7167 | -54.5244 | 2026-08-29 16:10:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 177.7 |
| 39b1bd74-7d6c-3995-8859-fc782b476d3d | -7.0219 | -59.6422 | 2026-08-29 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| f7afb00c-85c5-3879-abe6-c3bcdf6a62f1 | -10.4795 | -64.4824 | 2026-08-29 16:10:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.7 |
| d78631be-7faa-3475-b559-0a9dd643362a | -9.0059 | -65.4186 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 1df557b8-99c6-3a2e-a4c9-0b45ceba3419 | -11.1916 | -51.2708 | 2026-08-29 16:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.1 |
| f1f5f483-913e-3d10-aebb-0c3c2f84b74e | -8.6311 | -66.5287 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 3816d3ea-a84d-30ac-bba2-2e139f5fc8a8 | -8.9872 | -65.4566 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 54b87e04-e316-312c-869a-ca4ad5cc34b6 | -14.4444 | -53.3806 | 2026-08-29 16:10:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3e610739-d9ff-3dc1-862a-92406b22faff | -3.1815 | -61.1613 | 2026-08-29 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| a109f155-6390-38c7-a5d0-41eacbf82caa | -11.1998 | -55.0805 | 2026-08-29 16:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ffbf95c9-5525-32fc-9a81-42b4e5e8dd89 | -12.209 | -50.5601 | 2026-08-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| f471f298-479a-3a19-9674-7f01fd2cbb86 | -11.2128 | -53.9976 | 2026-08-29 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 1d29aa70-410f-3e6c-b5e1-72c048126fbe | -10.7598 | -54.0179 | 2026-08-29 16:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| a8ffa3a7-cfc7-3cdf-9492-0d295aa7293e | 1.785 | -55.8226 | 2026-08-29 16:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 0aae95c2-94fa-3294-b3df-9829e4429a90 | -8.6694 | -49.5369 | 2026-08-29 16:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 05abccc6-6ce9-3688-8564-32448b0db39d | -10.5593 | -50.4663 | 2026-08-29 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| f000e54e-7c8c-34ff-83e8-d7790ffe515c | -8.631 | -66.5473 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 94.6 |
| d39478e0-f7ea-3c7e-9c11-0f9d6b64776f | -3.2178 | -61.2362 | 2026-08-29 16:10:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| a0f44f9c-df36-368e-a93b-e3cae359de2f | -6.641 | -58.4987 | 2026-08-29 16:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 342461e2-4d97-3fab-8efe-436f5168755b | -17.2938 | -46.0291 | 2026-08-29 16:10:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 6f896661-afa5-37b9-a55f-e67f4c842d67 | -5.9819 | -57.6892 | 2026-08-29 16:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 24fd814b-b41b-3c47-8710-48af1dd2df6f | 0.1367 | -60.393 | 2026-08-29 16:10:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 103.2 |
| d798ed2b-36e3-3d39-8fc3-eead9b15a3e4 | -3.4002 | -61.3276 | 2026-08-29 16:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.0 |
| bd3f65bd-67e2-3ea4-b183-50f7d50e398e | -8.9873 | -65.4379 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| ec55f13e-0afa-36ca-b92c-a0a34166215c | -8.574 | -66.9569 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 369a9c5f-6118-3ac4-80bc-c70409cf7a5e | -8.7772 | -49.955 | 2026-08-29 16:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7eb43021-0306-3f2b-8a92-6330241435c2 | -8.6506 | -49.5386 | 2026-08-29 16:10:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| f5d91e21-cb1c-36ea-b1a6-381e51aef6ee | -9.2465 | -65.5043 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 26e38ad4-5738-3040-997f-db30e344505e | -9.7498 | -65.0938 | 2026-08-29 16:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| a9bf635f-7e2f-38dd-bb87-2f89d7d2d58b | -8.8184 | -49.6308 | 2026-08-29 16:10:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 4675d722-eb64-38ab-8f78-dc9a035fd275 | -12.2093 | -50.5386 | 2026-08-29 16:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 128.1 |
| 295fa255-e920-3e50-b42d-5d385fc3109c | -6.8357 | -59.9571 | 2026-08-29 16:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 70.8 |
| 944e515e-4dda-36ef-8e40-1453cfa240be | -9.0983 | -65.4717 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.7 |
| fff6f651-68d5-35cb-a9bd-0c7d84bda92d | -9.0058 | -65.4373 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 4c355441-0ad9-3e2c-962f-c83099437390 | -10.5404 | -50.4683 | 2026-08-29 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 7bb0fc0e-f509-3256-935b-2c59b8ac7a17 | -14.5445 | -52.0156 | 2026-08-29 16:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 32db35b3-2a0e-3cca-9c07-5883abfc835a | -10.8235 | -50.5026 | 2026-08-29 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 42cf6c84-068a-3321-ba76-88f3b2b0d068 | -6.8387 | -59.4186 | 2026-08-29 16:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| 03cc2410-2900-3990-a7b6-c1a4445e8c82 | -9.9288 | -60.4277 | 2026-08-29 16:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 90a5f9dd-ad0a-3f20-b907-5f8f3009620a | -10.8232 | -50.5239 | 2026-08-29 16:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| 94c54250-d836-3c32-87d2-9ed5cf87e972 | -13.471 | -57.0373 | 2026-08-29 16:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 201.3 |
| bd613a31-d630-334d-adfa-065a796bfe7f | -9.0982 | -65.4904 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 1426d4eb-b73a-3c00-b07f-d29139da6af8 | -8.6495 | -66.5468 | 2026-08-29 16:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| d3dc693e-5685-3e28-a184-bb265a766a03 | -10.5596 | -50.4449 | 2026-08-29 16:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| f35247ac-63b6-3621-90a4-a4160e6c8be1 | -12.91 | -45.89 | 2026-08-29 16:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92527149-43c6-3632-9662-da62fdbe1579 | -10.91 | -45.59 | 2026-08-29 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fcaac2df-5808-35a6-b3e2-39fa61522bfe | -10.91 | -45.54 | 2026-08-29 16:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3e9f87f6-462b-3cde-9c07-f2f4122de832 | -9.0983 | -65.4717 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 99.5 |
| 162f8d3b-2784-3e63-b8d5-d2b9a3b1f10a | -9.0198 | -57.5574 | 2026-08-29 16:20:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 0b721917-1b62-36de-8046-97be6c70b5e2 | -6.7652 | -63.054 | 2026-08-29 16:20:00 | GOES-19 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 1cb17762-c1b5-382e-b973-1566d9b21f35 | -6.7279 | -59.4423 | 2026-08-29 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 2cbe8ca4-d579-31dd-8f66-65a5fac17aad | -9.694 | -65.0958 | 2026-08-29 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 5f85d977-3b6e-35d9-9ae8-a0b2af290a85 | -6.6929 | -59.0966 | 2026-08-29 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 11fabf11-13cd-3085-84f6-bcd9299946e0 | 0.1549 | -60.393 | 2026-08-29 16:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 3a42936c-4dfb-3f3a-a57f-d30d32e5810b | -6.6726 | -59.4445 | 2026-08-29 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 526b02d9-74c8-3253-a0a7-cac51ad674ec | -3.6399 | -60.5466 | 2026-08-29 16:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 01c1e850-1c30-38e8-a44a-00ad545d9873 | 0.1914 | -60.5067 | 2026-08-29 16:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 71.8 |
| d42740bf-faaf-3387-9f54-7add2c6f4a4d | -10.7598 | -54.0179 | 2026-08-29 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.8 |
| 01672a38-4916-37c1-8d4d-2b83c853d20e | -11.2103 | -51.2899 | 2026-08-29 16:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 91.0 |
| cb0d2ca5-adfb-3050-9f18-f5c54e578dc3 | -19.0541 | -57.411 | 2026-08-29 16:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 50.4 |
| d43779dc-e1c8-3892-b466-342483fe25e2 | -10.7603 | -53.9769 | 2026-08-29 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 28c244db-9898-3c6f-b310-e07de1713a59 | -10.7791 | -53.9752 | 2026-08-29 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| f7807035-700a-3e00-9840-ae0a3dbf1aee | -8.6694 | -49.5369 | 2026-08-29 16:20:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 114.6 |
| e410cc87-da88-305b-aeff-82f2acd1ef5d | -8.631 | -66.5473 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 4db311da-913f-3f08-b5df-7a6aacc44a04 | 0.1367 | -60.393 | 2026-08-29 16:20:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 2527570e-5b80-3fd0-b192-b6ab6e2fdc3a | -12.2093 | -50.5386 | 2026-08-29 16:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| ff448c69-42c4-3902-8ac0-953e8d088eeb | -8.3717 | -62.716 | 2026-08-29 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b04e6f60-6dca-3033-943d-6627e7536d04 | -9.8617 | -65.0334 | 2026-08-29 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 56c1d0ed-2f98-3200-b696-c2249a9be98f | -15.3654 | -53.7887 | 2026-08-29 16:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| 0e1bab6d-3d4d-3104-9646-0b705ca86081 | -6.5053 | -45.095 | 2026-08-29 16:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 9408f5fe-ff18-30a2-8fa8-39e9caaf6503 | -4.1516 | -60.6878 | 2026-08-29 16:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 131.9 |
| 435ff8bb-5794-3f2f-b8e2-9245244a0e78 | -11.1939 | -53.9993 | 2026-08-29 16:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.0 |
| 5fca5a58-d187-3387-8d6f-a0054812b894 | -9.0061 | -65.3813 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| aef0f4f4-1ff1-3841-8961-070e70a96b18 | -10.9856 | -51.1019 | 2026-08-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.0 |
| d5021865-fb2d-3283-b558-dbe3fcd7ae76 | -10.4795 | -64.4824 | 2026-08-29 16:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 310601fc-4b01-31ea-803b-2621b9727065 | -8.9872 | -65.4566 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.5 |
| bc9464f9-66b5-3e38-b97b-26425ac53053 | -13.3038 | -51.4304 | 2026-08-29 16:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 69.0 |
| e9b3ec7d-a347-388a-a264-3afdda8e0fbe | -6.641 | -58.4987 | 2026-08-29 16:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 425f46a3-c9d9-302a-9366-3f0b8797d2e3 | -9.7498 | -65.0938 | 2026-08-29 16:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| 70026142-0000-3184-b8c0-787b48cb4d7a | -8.6495 | -66.5468 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 83528acd-51c4-33b7-a95d-375ad428b4a3 | -8.8184 | -49.6308 | 2026-08-29 16:20:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0666d6b3-1cea-3354-8887-a3e8d68dc88f | -9.0982 | -65.4904 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 6f86b7c7-8750-308c-b134-abfab1a4b59b | -7.0057 | -59.2575 | 2026-08-29 16:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 3604d467-d26b-301c-b293-2a8c2e3f3e4c | -10.8419 | -50.5433 | 2026-08-29 16:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b226d593-ef73-3e27-a526-75bee1662d55 | -10.5412 | -50.4042 | 2026-08-29 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 9a434fd2-37c9-3a85-923b-8fcf7e032d94 | -8.9873 | -65.4379 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 9e73dda5-5e29-3671-bede-de783c447379 | -10.5404 | -50.4683 | 2026-08-29 16:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 1e935c8a-614c-3dd3-9502-82c50d906a74 | -13.1648 | -55.6498 | 2026-08-29 16:20:00 | GOES-19 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 40.6 |


[Clique aqui para ver as próximas entradas](README89.md)
