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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f443139a-976e-3b2b-80a5-6d344e5381dc | -7.52053 | -46.86312 | 2025-06-01 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7f3a2add-0eca-32ec-8dd8-8177d886a82a | -3.36848 | -49.16056 | 2025-06-01 04:34:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7508e58-0fb0-316a-9b22-bc3c462556a0 | -10.46366 | -47.94553 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8ffee84a-d57a-39c0-bc46-5c808df8a2e2 | -10.67351 | -44.41138 | 2025-06-01 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8400f44c-ee61-3f0a-b2b5-a3d8e8371f52 | -10.11838 | -47.19975 | 2025-06-01 04:34:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46278f93-ad19-33a8-99ee-8799bf49e701 | -2.58461 | -51.92086 | 2025-06-01 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2e68c51e-04ed-324e-bf48-0ae079cb3aa0 | -8.81444 | -49.83116 | 2025-06-01 04:34:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 46ed8539-b64d-3669-bb64-1d2273361e41 | -8.67703 | -46.6424 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8aa1a9be-8f34-3fb8-90b3-351305aad0ca | -9.70853 | -49.4641 | 2025-06-01 04:34:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c6734cf-e120-312a-a4a0-5a7bfe2e7602 | -5.21714 | -47.50191 | 2025-06-01 04:34:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fdab3ad-be73-3aa6-a0be-b7d65c9aaa1f | -7.87592 | -46.48014 | 2025-06-01 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dc90364-f835-344e-9a2d-a5435d4afea1 | -4.64721 | -47.95897 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3238812-98eb-313b-a4d0-5cc1db1cf761 | -4.80987 | -43.22186 | 2025-06-01 04:34:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c3be8a2-f002-35e5-8f6e-12bd8be1b4af | -9.67215 | -49.73243 | 2025-06-01 04:34:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cb96a4aa-cb22-30dd-b731-80528ff0237b | -10.0505 | -49.65816 | 2025-06-01 04:34:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bbd07dbc-cde7-38fc-b3ee-cc409329712f | -10.47372 | -47.94712 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 6e95c13a-1379-3c72-b0f3-262c51831b28 | -7.00977 | -44.6208 | 2025-06-01 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 48065102-33a1-3a9f-b798-867b106ea606 | -9.40156 | -48.42059 | 2025-06-01 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 260ffb0f-6f95-34df-996e-ea5fc2378fbc | -4.25008 | -47.58756 | 2025-06-01 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11321015-29be-3690-a803-261641af36fc | -9.3246 | -49.18073 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 491cda65-b1f5-311f-b123-512428d1c825 | -7.22035 | -43.1283 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1868db0d-4fdb-39d2-887e-fbcba2351224 | -6.45071 | -45.72709 | 2025-06-01 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bec7f937-8aa7-32d1-989e-6c19e8769b89 | -6.44375 | -45.72606 | 2025-06-01 04:34:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 116fe253-f9d7-381d-be75-41de2e600364 | -9.35418 | -47.81528 | 2025-06-01 04:34:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 999052f9-246e-3c05-8be5-a0105513a741 | -10.12519 | -47.20082 | 2025-06-01 04:34:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2242ce10-ddeb-3912-b829-ac7f9ee97b0c | -9.13688 | -47.5782 | 2025-06-01 04:34:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 552bc9c9-530a-3d8d-993f-f4e41a13a6e0 | -7.24819 | -43.24747 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 2a0bbfbb-f47c-3a14-acd2-acd035947b6e | -4.24676 | -47.58704 | 2025-06-01 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3190bb86-39e0-3a57-ae52-6ae210a8a41e | -7.22943 | -43.12248 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 42c805a8-318e-3bfc-a88a-36fa62bbdabc | -11.3116 | -41.88868 | 2025-06-01 04:34:00 | NPP-375D | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dcd16b86-1484-320d-97c6-200a4c06e842 | -8.39914 | -43.8531 | 2025-06-01 04:34:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8b8ec0d3-5c54-3c30-9ee7-ce96262a2847 | -9.32794 | -49.18127 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 34b900f7-44dc-3f92-9114-40cd3e576984 | -8.68445 | -46.6397 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5a248605-1c17-354f-93dc-8f64d1856648 | -9.13352 | -47.57768 | 2025-06-01 04:34:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a4df9e81-aaf5-3e06-8926-5c2fcebecf28 | -2.5806 | -51.92023 | 2025-06-01 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79727f05-9968-3218-857b-b83876750874 | -7.22438 | -43.12891 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| da2918cb-46f7-33f8-969b-6af52d5d7251 | -9.3999 | -48.94415 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 507d87c8-82c2-39da-a953-ada43ea294d1 | -8.13026 | -49.58742 | 2025-06-01 04:34:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 3189a6a1-103e-3ef1-8ab5-df447433f186 | -7.21682 | -43.12414 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a8988fa0-1d3a-368c-b604-1b69938e9074 | -4.27432 | -48.09636 | 2025-06-01 04:34:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dea92ca6-249b-3bec-825a-730499d86587 | -7.00913 | -44.62513 | 2025-06-01 04:34:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 73fc5945-baa7-34b1-82fa-3dacdd875095 | -8.73997 | -48.86015 | 2025-06-01 04:34:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0703a3fe-8757-30f4-9f37-af84dc3bad7c | -3.89445 | -47.17724 | 2025-06-01 04:34:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fdee15f-61eb-3a46-b598-da0ec5f8540f | -10.46087 | -47.94143 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d44ef5b5-ea73-3916-9851-d5890df85575 | -10.67432 | -44.40809 | 2025-06-01 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5931a43e-b86e-332a-996e-93888728bcd1 | -8.39943 | -43.84993 | 2025-06-01 04:34:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| e94a3299-85f8-323a-a45a-f16c370006fc | -7.63475 | -46.11454 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 097ef578-d6b2-3eee-a82c-e929270535a9 | -9.67551 | -49.73298 | 2025-06-01 04:34:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b6b7ac-96db-3608-9fbd-fd51a54e8910 | -10.46981 | -47.95016 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ab18af9b-08c2-3e30-9120-547078c87081 | -7.09913 | -43.16427 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 554651e8-2bfa-3a1e-88ea-12ee62935d97 | -10.47478 | -47.95053 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67d49efd-34c3-35ca-8aaf-e66977d4831e | -4.51398 | -43.69083 | 2025-06-01 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2358ed60-20fc-3362-a52d-3f55661318bc | -8.72985 | -47.98447 | 2025-06-01 04:34:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f23c9b5b-00b1-38f6-8830-2e92fdb5d9de | -7.26228 | -49.51155 | 2025-06-01 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 608cdc53-1e54-3e09-a91e-d927549d1669 | -5.84926 | -47.88962 | 2025-06-01 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6724e4e8-d6b0-36e1-9edf-b4e8153bee01 | -10.12235 | -47.19661 | 2025-06-01 04:34:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| da4ede7a-cb24-385f-ae7a-3b8185169e7e | -9.33521 | -40.29378 | 2025-06-01 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e9a43995-3437-3796-ae3d-8332a06db32a | -9.33487 | -40.2885 | 2025-06-01 04:34:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 1507a744-9641-3e7b-8e7a-b8cb6da1cbc7 | -7.2589 | -49.51101 | 2025-06-01 04:34:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| cc34f3a2-86b0-3313-9a40-96346da78861 | -10.11895 | -47.19608 | 2025-06-01 04:34:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f83caec3-213b-33c5-be10-749c13c06070 | -4.41756 | -42.10393 | 2025-06-01 04:34:00 | NPP-375D | BOA HORA | PIAUÍ | Brasil | 2201770 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8a1f785e-c7c9-3065-b48f-9963e5654363 | -6.63444 | -47.35027 | 2025-06-01 04:34:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5085824b-a18d-3438-94c8-52df11de9e88 | -8.68045 | -46.64293 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c366d9e-a4e4-3aad-8b65-029cf7c05419 | -7.22086 | -43.12476 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 189ba9ad-d574-320f-b34f-d3c0f52cebdf | -10.67424 | -44.40642 | 2025-06-01 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1062c841-8cdc-3109-9633-f194e5a8f9dc | -4.67407 | -48.15581 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e723d43-77c0-3293-9f80-bd5586303097 | -7.51715 | -46.86261 | 2025-06-01 04:34:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 423f417d-2aa5-3bed-a0f9-eda7724ce5b5 | -4.8207 | -44.35662 | 2025-06-01 04:34:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9a7261e-d17a-31ad-9458-a3b82a9563dd | -9.12962 | -47.58072 | 2025-06-01 04:34:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bace4c8d-2e4f-3d6f-9ddf-6de78565d176 | -4.48565 | -48.86189 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09b2f397-b009-3e5a-b6af-36e8a40695d8 | -9.34496 | -48.94609 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d0683f56-cf70-316f-92b9-daa576ab8bf4 | -6.63833 | -47.34729 | 2025-06-01 04:34:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ffbf563-4149-3b86-800e-baab3af636e9 | -8.68103 | -46.63919 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d1eb40f3-dd37-39a0-b5b1-34f776da3dbb | -8.67018 | -46.64132 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a47ff5e-3ad2-33e2-9ca1-1559a6a6ad27 | -6.63732 | -55.01019 | 2025-06-01 04:34:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 738186c0-ae14-39ea-b593-2b7124b6f759 | -3.7609 | -49.92673 | 2025-06-01 04:34:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 16e8a610-4909-3019-9c43-e7daf77a06de | -4.48507 | -48.86549 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 366d0389-31cb-384c-9184-92317eac846c | -10.46422 | -47.94196 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec52341f-eb9b-3b8c-bd97-47b689f0f6f9 | -10.47316 | -47.95068 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| f53d5c47-4605-3df8-aef3-6524aa45bd86 | -2.58568 | -51.92115 | 2025-06-01 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f0baca3-79c9-308e-8c7a-d06541249e5f | -4.64666 | -47.96244 | 2025-06-01 04:34:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 25e20232-558c-3ba4-b279-84f32ec9f3f2 | -7.08204 | -46.55972 | 2025-06-01 04:34:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 801d13aa-30c3-3e08-a1a6-7805ae3a876b | -7.22387 | -43.13244 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 97ff1a89-b268-3a7e-8999-3c7ecf759a70 | -9.3419 | -48.94931 | 2025-06-01 04:34:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4f63ce50-fc2a-37ec-8090-d632f57d672f | -7.22842 | -43.12952 | 2025-06-01 04:34:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d6010d4b-9c13-35f9-addd-08b6ad541c49 | -9.40102 | -48.42405 | 2025-06-01 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99ffc7b1-2836-3fe0-b2f6-61b952595cbf | -8.6776 | -46.63866 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65a2c43f-b7e2-31c6-9d0e-984cd274251b | -9.39823 | -48.42006 | 2025-06-01 04:34:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0ab826c8-4b4c-31d1-9fc0-584ff2adb257 | -7.58266 | -45.86098 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6ea5703-d2cb-362c-874c-3a5275ab974e | -6.86107 | -47.84308 | 2025-06-01 04:34:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e3da18b7-2d21-3458-a45f-14f4c59ed178 | -9.04767 | -47.02264 | 2025-06-01 04:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 22f10118-b427-31c3-8c03-3f3bbf06cadc | -10.46925 | -47.95374 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3418e9a-ba78-322d-96a4-1f67249105e0 | -10.46701 | -47.94607 | 2025-06-01 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| da52c77e-2d18-3f5d-9cd8-918103eb361d | -5.84981 | -47.88615 | 2025-06-01 04:34:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f11cab13-54de-3eca-a61f-0f0301e67f99 | -11.41714 | -55.09027 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c18d534a-ba2b-35b2-8757-7d78bad15e2b | -13.91145 | -54.66457 | 2025-06-01 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0d1aa78f-69b3-35c7-9adb-b2ca471fab59 | -10.13817 | -50.69606 | 2025-06-01 04:36:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 4a99f46f-3df9-38be-8a09-6a938e65b371 | -10.82166 | -56.94423 | 2025-06-01 04:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88b2c39c-4d3d-3ef3-af2b-12b9789d6d04 | -14.57489 | -58.74924 | 2025-06-01 04:36:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6066970f-604b-381c-8a04-bbfa7c8537a8 | -11.43718 | -55.00189 | 2025-06-01 04:36:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README8.md)
