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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1f74fc01-1564-3391-944b-6beea8a77611 | -9.1837 | -59.5154 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ea64f5ce-be8c-3e2a-878c-e4479d4697fd | -9.1961 | -59.429001 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 46da1ccc-3509-31ec-bf9f-adfcbbeb7595 | -17.601801 | -46.688499 | 2025-08-26 00:42:00 | METOP-B | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fca3e488-fc69-399a-aace-199d7f8deff5 | -9.1596 | -60.756199 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c2b18697-c2d8-36a4-aaf9-ad6d7b59e1aa | -7.4391 | -60.599602 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bf009617-3f14-3156-bba3-c6f5531be80c | -6.2551 | -60.003899 | 2025-08-26 00:42:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 8923b939-ca3c-306d-91a1-e84a69464919 | -3.1347 | -58.993099 | 2025-08-26 00:42:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2bf50825-1d97-3552-b1f2-47c875dc2d59 | -8.3505 | -62.8922 | 2025-08-26 00:42:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 35dc3e9e-36c8-3320-abfc-2c7b5a53f771 | -6.9225 | -59.345501 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| de4ee543-b1d1-35d8-82ad-8df5fe54ac73 | -9.2243 | -59.657902 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8147ddef-666e-3026-beb4-18ee5189fb8c | -10.3988 | -57.673199 | 2025-08-26 00:42:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 49848cfb-11ae-3eaf-97dd-3501c4787e17 | -7.5235 | -50.519501 | 2025-08-26 00:42:00 | METOP-B | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54db27d0-8539-356d-93ed-8e1d72e66319 | -18.8424 | -46.994999 | 2025-08-26 00:42:00 | METOP-B | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| affee00d-f04a-3164-b9d1-ad62c8294158 | -7.7355 | -50.285 | 2025-08-26 00:42:00 | METOP-B | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a95e9bd9-15a9-3003-bbd8-2ac8c5efdf20 | -9.1661 | -59.528599 | 2025-08-26 00:42:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c0fb6a36-5147-33f8-8a99-ebaa43d24412 | -6.7847 | -59.655499 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d9972cd-5356-30b6-a2ea-17092b18e0b6 | -6.9207 | -59.3372 | 2025-08-26 00:42:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 93396639-a0c0-308b-ac6e-fd8531356309 | -6.7635 | -59.6718 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 2959f8b2-1b9b-35e1-8db1-2eaccf29d34d | -9.1724 | -59.4436 | 2025-08-26 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 1aaab03b-df55-3253-8f91-3410eca443a1 | -8.8364 | -62.4321 | 2025-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 77c26f38-8fb0-385e-b153-ea3d4ad33a5d | -6.766 | -62.8659 | 2025-08-26 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| 4e4a98e0-e61c-393e-b176-45b1facd4c1e | -14.6567 | -49.0729 | 2025-08-26 00:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 25ec3b69-ea3b-326f-b04a-c468c88314e5 | -6.7144 | -58.5732 | 2025-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 247e6496-1442-3e23-bf06-cdeb1bb8d41a | -11.559 | -52.117 | 2025-08-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 561.8 |
| 1fbd348a-a775-3338-92da-248966799ac7 | -13.4425 | -51.1566 | 2025-08-26 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cf600b60-9c84-3141-ab4a-dc553d0a446a | -6.2459 | -60.0174 | 2025-08-26 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 168.2 |
| a3ffd589-0e0a-338c-a8cb-782652a7f033 | -7.3669 | -64.3667 | 2025-08-26 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| e54c49a8-6cbc-34b1-addd-191e2242aff8 | -7.3541 | -59.6669 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.1 |
| 81eef915-a4e0-3dc8-9c8f-8ca13156d904 | -6.7145 | -58.5539 | 2025-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.7 |
| e0959c50-2b90-33b8-ab86-96c7a67d441a | -11.1779 | -44.76 | 2025-08-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| ac07ccbd-5b4b-35cb-9704-293563af0fda | -6.2458 | -60.0365 | 2025-08-26 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 9a6a29f0-b645-3d8c-8ca5-e73175a7430d | -11.5587 | -52.138 | 2025-08-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 698.0 |
| c084bd72-b707-3143-b979-56c7194da664 | -11.2937 | -55.1129 | 2025-08-26 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 43556d6b-3776-311c-88fd-47afd5f95307 | -7.4224 | -60.6236 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 9f73e380-3513-3360-a67c-b03016f33f10 | -6.246 | -59.9982 | 2025-08-26 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 78.7 |
| 9e2ce1b1-45d1-3b40-8e20-946e8eea8732 | -8.8918 | -62.4677 | 2025-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 0c5b940a-da66-3532-8b97-836bd2798193 | -10.7597 | -47.0648 | 2025-08-26 00:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.9 |
| f281a336-8afb-3ce8-a1a6-1aae8276040f | -9.236 | -60.9256 | 2025-08-26 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 2485776e-69f0-3b3b-8427-8b148efe8202 | -11.5397 | -52.14 | 2025-08-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 407.6 |
| 6ee9dee0-9391-32e8-a2d2-0f8949ec2990 | -8.8734 | -62.4495 | 2025-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 29742b68-befd-342d-b6ef-31ca812b022c | -11.14 | -44.7422 | 2025-08-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 4b3caf23-3796-3d30-a749-91222ed41552 | -6.6961 | -58.5546 | 2025-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.4 |
| bec3f294-0cc6-3b93-8d45-c10587cbe74c | -6.2275 | -60.018 | 2025-08-26 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| b2e6712b-233b-3b8b-a097-5445c151ae6a | -11.5584 | -52.159 | 2025-08-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 33.8 |
| cc2e1499-985a-3178-8bfb-f561f47fe861 | -8.9688 | -65.4385 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| fe5f9029-68d4-3366-9dc1-7ad05366096b | -8.855 | -62.4313 | 2025-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 134.9 |
| 5ff16363-3521-3db0-8f2e-7e619dad38f3 | -7.3854 | -64.3662 | 2025-08-26 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 55bb6ddb-fd6c-3291-882b-9518e24158c6 | -9.191 | -59.4425 | 2025-08-26 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1bbe94ef-2124-335a-b294-1b805a750864 | -6.782 | -59.6519 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.0 |
| d0e19e31-48a3-34a1-8210-21a0e95db046 | -9.181 | -60.8131 | 2025-08-26 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| c7a7cea3-7cb2-3ed8-8bb9-62b6a8980722 | -9.023 | -65.7355 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 1df3f2bc-7ff3-3707-9065-d98d5c16b512 | -9.1909 | -59.4619 | 2025-08-26 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 1c0e7c93-61e6-3e14-970b-034f795b5eba | -6.7476 | -62.8664 | 2025-08-26 00:50:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 21096d22-4411-3b62-9fb3-cb1fcd109c61 | -4.9606 | -55.8028 | 2025-08-26 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| aff638ef-153b-3273-a41f-2a3da097f408 | -6.7819 | -59.6711 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 53b73ae4-6447-3da3-9e20-8eba2c7982a7 | -11.1583 | -44.7859 | 2025-08-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5c5d2c3b-b327-3584-8b8c-a6a355190ffe | -8.3209 | -50.5667 | 2025-08-26 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 87f09322-9273-3170-afd9-64b1fdd02e6e | -9.1722 | -59.4629 | 2025-08-26 00:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 6989ef4b-4464-3711-bf8e-9863e056b44b | -7.3854 | -64.3475 | 2025-08-26 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 145.8 |
| e9721e8e-acf7-3b88-a137-f792ee7bf1c2 | -9.2677 | -56.91 | 2025-08-26 00:50:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| cc958ed3-5926-319a-8387-c5a6b8433eb5 | -8.8548 | -62.4503 | 2025-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 260.7 |
| 322a6e03-75a4-31ce-9a86-b1a2cf79e172 | -8.9689 | -65.4198 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 07c32154-fde1-39a5-b1df-9f51a9ec6160 | -6.2276 | -59.9989 | 2025-08-26 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 38615d5b-fe2a-3863-9644-01e55560d14e | -6.9127 | -59.3771 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 11da0e83-cad2-31a6-b5a2-66fd94fdcd1c | -11.54 | -52.119 | 2025-08-26 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 329.9 |
| bfc8878b-f2d1-35cd-a9cb-4b61984fc7c0 | -6.6959 | -58.574 | 2025-08-26 00:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 51.2 |
| f88e1b13-9a07-3eb2-93d0-f29e872c59d0 | -13.4618 | -51.1541 | 2025-08-26 00:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| d37f5bf4-2677-386e-b9f4-e88f8294da33 | -13.1837 | -45.2865 | 2025-08-26 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 73f57612-e0d2-354b-ba23-f48696c194e2 | -7.367 | -64.348 | 2025-08-26 00:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 109.0 |
| e6d9d2d4-538d-3968-a90f-499014a10e21 | -11.1587 | -44.7627 | 2025-08-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 245.8 |
| 4e6ac464-962a-3bfd-aa40-9df56b54540f | -8.8363 | -62.451 | 2025-08-26 00:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 93.3 |
| fd819323-01b0-34bb-8465-0ed28aeba433 | -9.0415 | -65.7349 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 108d6c7f-a5a6-38c3-95cb-749eeedff976 | -9.0231 | -65.7169 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.4 |
| e44a976a-b6a3-353a-aedb-16fe9bb5181d | -6.9128 | -59.3578 | 2025-08-26 00:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 23d22161-acd2-3bee-88b8-c81eb436ac10 | -11.1396 | -44.7654 | 2025-08-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 4c16dcf0-e4cc-3d23-ab14-5d6bdc72a36e | -8.3396 | -50.5652 | 2025-08-26 00:50:00 | GOES-19 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 64.5 |
| f602372c-6f1a-30e1-8710-2d13e4667354 | -8.9873 | -65.4379 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 44.0 |
| d29fbefb-91c3-31ed-ae2e-aa1aa9b73a15 | -4.9605 | -55.8226 | 2025-08-26 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 98.6 |
| 9a1e4590-6354-34b7-ae49-96757e2ff4ff | -8.9874 | -65.4192 | 2025-08-26 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 3f365420-2571-337b-8a19-c11f4d729e50 | -11.1591 | -44.7395 | 2025-08-26 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 127.1 |
| eaf3b777-63fb-3447-b56a-4c3ed351fe4e | -11.3126 | -55.1112 | 2025-08-26 00:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 97427030-119f-3c4e-b043-dd67c4fbfb93 | -13.1644 | -45.2897 | 2025-08-26 00:50:00 | GOES-19 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 6aff581b-a557-3ef0-83ac-ed76dea670aa | -14.6372 | -49.0759 | 2025-08-26 00:50:00 | GOES-19 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 88.2 |
| 0132bafe-1a08-3271-9b60-6448ab9e0a5c | -8.8734 | -62.4495 | 2025-08-26 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 167441d6-3eed-34ba-92b8-9d68b39ec911 | -6.7145 | -58.5539 | 2025-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 80332f57-2ad1-394f-9851-23bfbdf40a4b | -8.9874 | -65.4192 | 2025-08-26 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 35d7e5b8-5df8-37d1-83b5-1e1d5b71f191 | -6.246 | -59.9982 | 2025-08-26 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| d235735e-3958-38c2-b2c4-98c5671a7ed7 | -6.7635 | -59.6718 | 2025-08-26 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| b865ba94-b77b-322e-b00c-04c662c11a61 | -9.191 | -59.4425 | 2025-08-26 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.2 |
| dae231f4-61b7-3dec-aec8-7d6a165dea17 | -7.3854 | -64.3662 | 2025-08-26 01:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 86.1 |
| 4e522f43-bb2a-33b3-a095-e142684280e0 | -11.1591 | -44.7395 | 2025-08-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| dc3ec781-cd2a-310a-9ae1-a140e71fed8d | -5.5281 | -60.2133 | 2025-08-26 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 929fedc6-d973-3a36-92a6-36d41924014d | -9.1722 | -59.4629 | 2025-08-26 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 7050aacb-3e1b-332e-af11-1e4f60a7ac08 | -8.855 | -62.4313 | 2025-08-26 01:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 3b12748c-79af-3632-a4ea-5f0c730b271b | -9.1724 | -59.4436 | 2025-08-26 01:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 14de52dd-cb44-38da-92dc-0509b27833e9 | -4.9606 | -55.8028 | 2025-08-26 01:00:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 0c270531-4331-33b7-a4ca-4246f1a94fd0 | -11.1396 | -44.7654 | 2025-08-26 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 120.0 |
| 295235c2-5368-3e53-8fc9-64056b48d4f2 | -6.6961 | -58.5546 | 2025-08-26 01:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 99d5213f-b0c2-3823-8a3c-04f9e07d41ab | -7.3541 | -59.6669 | 2025-08-26 01:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 10d9e4f2-936d-3b7b-afcc-db3d0c0be588 | -6.7476 | -62.8664 | 2025-08-26 01:00:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |


[Clique aqui para ver as próximas entradas](README13.md)
