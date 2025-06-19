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
| 01cf9884-7086-35e1-ab6e-5cbd2522a7d3 | -10.0988 | -52.736801 | 2025-06-19 00:47:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d009baf6-7257-344c-bf74-8b70fa8b09ba | -3.0299 | -49.434799 | 2025-06-19 00:47:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93415938-69db-3298-b935-c771e76b2bf4 | -16.3039 | -58.248699 | 2025-06-19 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5951a95f-05b6-3a1b-bab9-9b01b20dabd5 | -21.792801 | -52.753601 | 2025-06-19 00:47:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 01cba9fc-aeb4-33b1-8640-961c88a4103e | -17.5718 | -47.4776 | 2025-06-19 00:47:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ec21f073-49d5-36af-bc77-84b47100d8ef | -11.9674 | -58.7439 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 53a63981-dad7-3734-959e-f42046028075 | -11.954 | -58.729 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cf920aa6-c664-3dff-882a-06cec51ef693 | -11.6484 | -54.134701 | 2025-06-19 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d3d78195-650c-3a1b-a861-260d5ceeab01 | -11.8129 | -57.343201 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ca94f932-1dab-38a8-873b-916790d0c54b | -10.467 | -58.6758 | 2025-06-19 00:47:00 | METOP-B | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7ab14a5d-4ea7-3389-aff8-57260d0d90e6 | -11.5309 | -56.9897 | 2025-06-19 00:47:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 19cf7241-264b-3335-84fb-fdf518139d1d | -11.7723 | -54.362598 | 2025-06-19 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 785091c4-44a7-3519-9962-eb3401371453 | -11.6238 | -58.281898 | 2025-06-19 00:47:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb091520-c0bd-3387-8f09-c79a9421b655 | -13.583 | -59.184399 | 2025-06-19 00:47:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bf2ab6a9-225a-307f-b901-2ba21b0bd8d4 | -19.1301 | -52.690498 | 2025-06-19 00:47:00 | METOP-B | CHAPADÃO DO SUL | MATO GROSSO DO SUL | Brasil | 5002951 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| b6bd1275-73ef-36fd-afff-89b7d935da8c | -13.5869 | -59.203201 | 2025-06-19 00:47:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4112623-95e4-3bfa-9eef-1ed27a3e3096 | -17.575199 | -47.490898 | 2025-06-19 00:47:00 | METOP-B | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 2a574b98-0eea-3ee3-8210-5dcb4872a96b | -11.6255 | -58.290001 | 2025-06-19 00:47:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4659ed63-c917-3b33-bc1e-befea15188a9 | -11.1398 | -53.939098 | 2025-06-19 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8ec8972b-8c94-3d49-a6ee-f8ddeaaffa04 | -10.6539 | -49.440601 | 2025-06-19 00:47:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1394a685-2cde-312d-9309-6394fb3285b8 | -21.343901 | -48.618599 | 2025-06-19 00:47:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5d4ca0d-acad-39d7-b6f4-0d35eeb89982 | -12.5302 | -57.192902 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 45ee9e47-975e-39d3-bca7-329077a6e6f2 | -4.7688 | -47.580601 | 2025-06-19 00:47:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c875bba0-4b06-3fe3-b947-9237d229aec7 | -11.1283 | -53.934101 | 2025-06-19 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8badc5d2-afc6-3c10-a90e-af602a4fe5ac | -11.8225 | -54.493301 | 2025-06-19 00:47:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4a01b44b-76fa-3f0a-9b74-deaa76ba9725 | -10.7235 | -49.556301 | 2025-06-19 00:47:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be06c934-ff3c-3de7-92b9-dd687f412067 | -11.9656 | -58.735401 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 37b68c39-a432-3dcb-a1cf-4d99eee86390 | -11.946 | -58.739601 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1a0ce3bc-945d-3c9f-935b-79d4dd7ee202 | -11.9496 | -58.756599 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 87deada8-946c-3280-aaeb-9ae923439d6f | -13.9844 | -58.106602 | 2025-06-19 00:47:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 86753b60-1628-3f2c-8394-486ed2ca85a5 | -3.026 | -49.418098 | 2025-06-19 00:47:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3e98d64-1d45-3cb8-8be1-4f4ec1c1a485 | -18.665501 | -55.736099 | 2025-06-19 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 88539666-848a-3902-bdbc-ed14f2f29785 | -10.5114 | -53.583 | 2025-06-19 00:47:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec2baf56-f358-3488-912e-d4e5807eb391 | -12.4807 | -58.457001 | 2025-06-19 00:47:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3d34c92b-332d-3be6-8fb2-1c7bc3781527 | -13.293 | -57.0639 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f85ac521-9495-36ee-a02e-e476cc348890 | -12.5318 | -57.200401 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6f154e7d-443b-34a8-a8f2-4b087e69a35c | -10.087 | -52.730801 | 2025-06-19 00:47:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 57ea5627-42c2-37a5-8077-67ecc4f98cd9 | -10.5079 | -53.567799 | 2025-06-19 00:47:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f0e12a60-27f7-31e9-8162-3a113f98fef3 | -7.2801 | -49.9837 | 2025-06-19 00:47:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef28ed8f-3c49-3655-8894-cea344848bc2 | -10.657 | -49.453201 | 2025-06-19 00:47:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3deb4119-83c5-3f9e-a377-95a12f9d5857 | -8.9493 | -47.964901 | 2025-06-19 00:47:00 | METOP-B | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3288f061-a245-380d-b7e5-4260530dd356 | -12.0344 | -57.084801 | 2025-06-19 00:47:00 | METOP-B | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 624ec2eb-e30b-3482-825f-be4289810581 | -11.9638 | -58.726898 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ec76a66a-352f-3f0c-a819-321bbf0a358b | -23.3078 | -47.906101 | 2025-06-19 00:47:00 | METOP-B | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 208aead9-abc5-3156-9565-507115eaa133 | -12.9757 | -54.671799 | 2025-06-19 00:47:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31ee1e65-b607-3f11-8a58-c7e6a9da1d03 | -9.5004 | -56.0853 | 2025-06-19 00:47:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 367c3b69-83a4-35cc-8b1c-212319232914 | -9.3723 | -47.637699 | 2025-06-19 00:47:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e8883b33-a38e-3f29-a237-f5cd3b3eb4f6 | -11.1365 | -53.9245 | 2025-06-19 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2487fe21-570d-3499-85ab-dbcf2fc35067 | -8.1301 | -49.579498 | 2025-06-19 00:47:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b70ac5f6-a626-3db7-8980-83563578e676 | -10.6375 | -49.458099 | 2025-06-19 00:47:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f0699b7e-b3af-3cd2-b8f8-2507e728afdf | -13.585 | -59.193802 | 2025-06-19 00:47:00 | METOP-B | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 90080973-5744-3d2d-875e-bd56c88d5949 | -11.1381 | -53.931801 | 2025-06-19 00:47:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f39091a8-ad1b-304a-b4b6-13533d48d34b | -18.667101 | -55.743801 | 2025-06-19 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 2025dab0-21f4-3ef8-9c5d-a496e0ddced6 | -21.346399 | -48.6287 | 2025-06-19 00:47:00 | METOP-B | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 82896b82-28fc-3d32-99bb-d1cb5a30d702 | -11.9594 | -58.754501 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a3faccba-fad2-3cae-b255-c6fc14ce6387 | -11.5293 | -56.982399 | 2025-06-19 00:47:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 183e0f2f-7cf1-3a7f-b84a-3f647fa40d56 | -12.5851 | -56.970699 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec565a56-cf93-376f-9a59-513c8ef4239f | -20.021 | -45.749599 | 2025-06-19 00:47:00 | METOP-B | IGUATAMA | MINAS GERAIS | Brasil | 3130309 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4283ac74-2670-355c-8ab9-a61d03ef070e | -11.9558 | -58.737499 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cd1106a2-3e25-36cf-a9a6-1a479252f5f9 | -11.962 | -58.718399 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cbe4f57f-9f4e-31ed-a63b-63610634a4dd | -11.6221 | -58.273899 | 2025-06-19 00:47:00 | METOP-B | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35262dd7-c2ec-3f1d-994e-a9bcea4e60fd | -4.7734 | -47.557201 | 2025-06-19 00:47:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5a597852-56ae-3ded-b4b7-ca8e1bf09640 | -4.7785 | -47.5783 | 2025-06-19 00:47:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3174015e-1d3e-3c86-b68e-515e37068c64 | -21.791201 | -52.746201 | 2025-06-19 00:47:00 | METOP-B | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9ddbcf7d-eefb-35c0-95d5-5cdc594af2e3 | -13.9862 | -58.115002 | 2025-06-19 00:47:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 33b97684-e2c9-342a-ae4d-505c24d4b546 | -10.3078 | -57.132099 | 2025-06-19 00:47:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3a81f1-4bea-3663-a967-359987668723 | -10.2377 | -52.227402 | 2025-06-19 00:47:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8b9f0fcc-108f-3024-b60a-41e5fc9b4dde | -16.3137 | -58.246601 | 2025-06-19 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d8e787fe-fde4-3c91-a0c4-92924ec96b70 | -10.5096 | -53.575401 | 2025-06-19 00:47:00 | METOP-B | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 31c55f85-5937-38f8-a936-1a38446f4db9 | -9.4659 | -57.843201 | 2025-06-19 00:47:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbc9477f-2f81-359f-8507-b2014a12a8b9 | -8.718 | -47.987099 | 2025-06-19 00:47:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b60ec5ef-60db-3b00-90a3-95adaf077470 | -10.148 | -48.977299 | 2025-06-19 00:47:00 | METOP-B | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a0d780a1-a486-3e9a-98a2-2cbd7323daef | -12.3778 | -57.391998 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8a5d52e7-7392-367d-8caf-3cea290bdc09 | -10.2356 | -52.218601 | 2025-06-19 00:47:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b960e4b6-6cb2-3382-98eb-dc674c94c2a9 | -7.2833 | -49.996899 | 2025-06-19 00:47:00 | METOP-B | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50b924e3-c8b2-3115-ac31-574a5bc95389 | -10.089 | -52.739101 | 2025-06-19 00:47:00 | METOP-B | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5a64d635-56ae-3a2a-b786-cfa42a322fb2 | -11.9576 | -58.745998 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 54f8ee90-b781-36ee-8093-2eda34693675 | -9.4973 | -56.071499 | 2025-06-19 00:47:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9643de60-9e6e-3c1f-8ba7-e8afdf881c5b | -18.668699 | -55.751499 | 2025-06-19 00:47:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 8c207097-ae6d-36b9-9c0c-f0914ce058ed | -16.3155 | -58.255798 | 2025-06-19 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4624962f-109f-3dad-9795-972a1d36bd9a | -10.3062 | -57.124901 | 2025-06-19 00:47:00 | METOP-B | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 311b1b4f-c60c-3e5f-94df-1b5c01a5161b | -12.9773 | -54.678902 | 2025-06-19 00:47:00 | METOP-B | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46023eef-2878-3e89-8a8d-f89e4da0cc70 | -9.0086 | -49.589802 | 2025-06-19 00:47:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ed144e15-f9f3-308d-9004-0229f8a17f57 | -11.5278 | -56.975201 | 2025-06-19 00:47:00 | METOP-B | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 718be346-cc99-3fbb-9114-07accf2a4841 | -19.0016 | -52.0746 | 2025-06-19 00:47:00 | METOP-B | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3ba9c0f8-e72f-30e2-88b2-432a013565bc | -9.4988 | -56.0784 | 2025-06-19 00:47:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0521067-7534-3a93-aa6a-8246285544e2 | -12.9131 | -56.967899 | 2025-06-19 00:47:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a71fa5a6-f9f7-30f5-9ac2-7b0237eb23bc | -10.6442 | -49.443001 | 2025-06-19 00:47:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 92b21044-2c56-33a6-b4e3-e20ec8c14ed8 | -16.302099 | -58.239601 | 2025-06-19 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b7a02296-8b7a-38e5-aa1a-11f7de09a0f1 | -10.6344 | -49.445499 | 2025-06-19 00:47:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b37b51cc-4607-3c33-8cb9-8262cf692405 | -9.0055 | -49.576698 | 2025-06-19 00:47:00 | METOP-B | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e95d2c5-8176-34a4-b161-63e008461f3e | -9.8874 | -48.0089 | 2025-06-19 00:47:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38a481b1-9396-31c9-b419-f07e3c2aa788 | -16.311899 | -58.237499 | 2025-06-19 00:47:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 61db484f-c8f7-36ea-a287-e2d1a5e089c5 | -4.7637 | -47.559502 | 2025-06-19 00:47:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| acb71ccc-672f-361c-86c8-9a334c4ab8b2 | -8.7223 | -48.004101 | 2025-06-19 00:47:00 | METOP-B | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a5ab17cb-d604-3dbf-9949-cd2301b5fd1c | -9.8914 | -48.0252 | 2025-06-19 00:47:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03cbd822-f916-3ca8-bdbc-5f5aa9b29062 | -11.9478 | -58.7481 | 2025-06-19 00:47:00 | METOP-B | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0f2ef2d9-666a-3e0d-9b74-8fe567daf972 | -10.6473 | -49.4557 | 2025-06-19 00:47:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d797beed-c9dc-3ec3-af2a-225ecbc7230c | -7.2594 | -43.0881 | 2025-06-19 00:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 59.4 |
| cbf76566-ab75-3fed-a0a4-e10cc7cadf73 | -4.7686 | -47.5686 | 2025-06-19 00:50:00 | GOES-19 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 72.5 |


[Clique aqui para ver as próximas entradas](README4.md)
