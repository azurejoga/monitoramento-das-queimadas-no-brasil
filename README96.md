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

## Dados Diários - Página 96

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2acd93b1-428b-38b4-90bb-7ed889a0a8d3 | -8.74579 | -48.8744 | 2025-10-07 04:57:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6e7e7c02-9935-3411-8a4e-9c5de56e75a1 | -13.58932 | -48.15182 | 2025-10-07 04:57:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 00042452-8edf-31f7-b5bf-0067586b6788 | -11.1605 | -47.94957 | 2025-10-07 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc3fedb8-b731-3146-bf16-acb4ddc82165 | -13.2795 | -47.56847 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| de944d4d-8803-3f2b-83e8-88fe59294fef | -14.75129 | -46.02111 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d6cd9f9-a064-340e-9411-7656d8370f14 | -14.90807 | -46.86698 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f90f8ab8-9667-30ac-bea8-72dd1bbf62ee | -9.9676 | -43.78881 | 2025-10-07 04:57:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4e89651c-7a43-34e0-ac0c-4aaaad826df8 | -9.18671 | -47.83386 | 2025-10-07 04:57:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7cbc186b-bb4d-3f72-8423-29aa1cd8b127 | -10.55704 | -56.55338 | 2025-10-07 04:57:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21cde796-c214-3841-9505-7c33872de813 | -10.78868 | -48.59517 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80e75ae0-b4aa-3fc9-99de-9d195a2400b9 | -11.26526 | -48.84659 | 2025-10-07 04:57:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3eb0f457-81d2-3aae-8229-fb09fe870df5 | -11.83719 | -44.91341 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91f98467-8a47-3105-b51b-e9d0b13bb90c | -10.81068 | -48.59911 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5edea821-8d1d-3190-8bd1-9ded61ee13f7 | -14.93215 | -51.43736 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fae1884f-c495-3ae5-ad5e-00b9909dfddb | -15.51327 | -46.83704 | 2025-10-07 04:57:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2e9b4e0-6dbc-338d-88e3-18d7e31ebdd2 | -12.24698 | -47.76351 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d94da2dc-3dd5-32f4-a262-de7bc4dd68d3 | -14.90401 | -46.85637 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8032dac7-0aad-3d34-9f75-e1026bbed6a2 | -10.74626 | -50.49356 | 2025-10-07 04:57:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59a1333a-9337-3fed-9e1d-60614d0bdd91 | -13.53593 | -43.00204 | 2025-10-07 04:57:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| c0a70a20-25c0-37d3-87c0-bb3ba9a922ac | -11.15051 | -54.88241 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 852fde8c-c97f-323a-af64-1998cb280c01 | -10.58177 | -51.47016 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5ee0e8d2-7baa-3c0a-85fc-0a8a26118137 | -9.63565 | -54.32108 | 2025-10-07 04:57:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3007af27-0485-30a3-bfb8-0c56bb3d4823 | -10.38287 | -50.29124 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 97e7bb53-e33d-398b-b171-69fe612ea334 | -12.40282 | -51.13481 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1eb00696-c01d-3cd8-bfae-03fcb5948f4f | -6.738 | -63.06572 | 2025-10-07 04:57:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aeae8dd1-62e8-3795-944a-209d73db6b88 | -12.38668 | -51.08302 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05dc46dd-2d41-303a-ab7f-5fcde963e1f3 | -9.02926 | -50.59103 | 2025-10-07 04:57:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7df66e2-b5b3-3b08-9cc3-596f4cda5c3b | -12.89678 | -54.74166 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6760557f-c173-3ea5-b68c-d254205949bd | -8.17997 | -50.29686 | 2025-10-07 04:57:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 73ac0ee6-3a6f-300b-803d-edcf827d543a | -8.53546 | -54.85931 | 2025-10-07 04:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90308664-fa47-3f41-86a2-ffffe124ab62 | -14.50699 | -46.9219 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 52bfda44-6029-3bf5-989d-434196c0c98f | -13.18326 | -51.04769 | 2025-10-07 04:57:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4adb36d-cd4f-3fd3-af80-2939d291151c | -8.85261 | -62.37072 | 2025-10-07 04:57:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 92dbcf11-afdd-35f7-aed3-7e078c837a1c | -15.11965 | -43.87288 | 2025-10-07 04:57:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2c091e2b-d79e-3f9c-97e6-c8c7e2358725 | -12.61652 | -44.75987 | 2025-10-07 04:57:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4497dae7-601b-3561-9d27-9f5030eb324a | -10.38681 | -50.29181 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c1d3be25-bb18-3fe5-b4d4-c3b39e6c0be9 | -11.15521 | -47.95379 | 2025-10-07 04:57:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5776eceb-f250-3bb8-937d-efba027cc7a5 | -7.13682 | -63.13059 | 2025-10-07 04:57:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e61a2d39-154e-357b-9e52-48a69282826e | -12.39898 | -51.13425 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6c0a787-d0af-3b27-a42a-3509dc86be9e | -14.90479 | -46.84985 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fff7e065-02c3-37d6-bcd6-d297c8851604 | -10.45264 | -50.41935 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 76c283ec-91e1-3b43-ac47-413555af0d40 | -11.74843 | -51.49883 | 2025-10-07 04:57:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4e3633c-6b01-335b-a6f0-84b8cb355fbe | -14.91982 | -46.80537 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa13749d-0cbf-38bc-a8cc-6189586f51bd | -13.27545 | -48.05722 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85c59049-dcd7-3d27-9a76-453eac0e5380 | -13.32102 | -47.77321 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf5de9c1-a5a9-3aa1-b8a5-f5459c40f554 | -13.3274 | -47.76161 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f7a364c8-a410-359c-913d-4a48a77fab19 | -10.41709 | -48.09942 | 2025-10-07 04:57:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19e58d30-9f06-35ec-9074-ae3fc30e80bd | -10.42077 | -50.30711 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a7395a05-5079-327a-8787-423ec052acb4 | -10.41326 | -50.27497 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21d94baa-891f-3237-9115-f1034ce2cc07 | -13.27001 | -48.06182 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 14aa958b-3c8c-3cc1-b6a4-33f7b2440d2d | -11.38659 | -43.49885 | 2025-10-07 04:57:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d689bfc-11d7-3a3b-b80f-217fc46a347a | -9.40095 | -61.4483 | 2025-10-07 04:57:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 923f7710-cf3e-39bf-8df6-0f70fb14e10e | -10.61091 | -48.68061 | 2025-10-07 04:57:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 776f0743-066e-3b79-8082-a916c178fe5f | -10.32339 | -54.15633 | 2025-10-07 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4be45902-0d68-3f35-a688-fe60a2c17419 | -15.58987 | -47.27051 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c8466136-21b7-3281-a3b6-1ae5bc24024f | -8.34929 | -49.65914 | 2025-10-07 04:57:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0b9c6af7-d7d9-30e8-94e8-d039b92372c1 | -13.05748 | -48.71196 | 2025-10-07 04:57:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f12dbd1a-6e4b-38ad-b16d-08bd96abf5fc | -11.29562 | -48.26813 | 2025-10-07 04:57:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5fc5e732-fac2-3ca5-a1f0-7d563f78c4f0 | -15.11519 | -43.87228 | 2025-10-07 04:57:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 07b104c6-d96f-35b6-aa5c-f6d6a16f3115 | -12.41393 | -50.26732 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eba46a3c-b0e4-328f-acd2-0e76cddcde48 | -14.49986 | -46.93745 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a59bf309-4947-36cd-b670-5335a1b989fb | -10.41307 | -45.39571 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9675f441-9a37-3f50-88e7-3480af7fcbad | -13.65225 | -48.73454 | 2025-10-07 04:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d8b898e-1403-35fd-a538-5ede7f4061e8 | -14.77422 | -46.06615 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 01892bf8-c2a3-39ac-bcf3-59c851536958 | -13.22653 | -51.69134 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 35b260a0-469a-3ed6-83a6-02efe786c9a0 | -8.88176 | -46.04337 | 2025-10-07 04:57:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 79a040ca-0daa-397f-888a-795d241a3412 | -13.24349 | -51.67975 | 2025-10-07 04:57:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c974119c-2216-3eed-875c-203c8164a1e0 | -10.40504 | -50.30481 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 3cf16cc9-5780-3fc8-a43b-53f996641661 | -14.764 | -46.05729 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4c5a7d1a-5a9c-3f40-8cee-ce65eb0d61e8 | -13.76013 | -45.73206 | 2025-10-07 04:57:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae94a1c3-a9fc-3f6b-a946-4108f7caf820 | -13.96726 | -53.89147 | 2025-10-07 04:57:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b757ca4-28ae-3028-9349-99363a64ad37 | -13.26825 | -47.5785 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7afaa31c-4de2-38a6-84ed-f9e0e0fb2e87 | -9.63138 | -57.022 | 2025-10-07 04:57:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| da605282-e03d-3b25-adab-2ddf00cd0eaf | -11.78346 | -45.10319 | 2025-10-07 04:57:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79d16c49-d6b2-396e-8459-011dad7fd06c | -11.15106 | -54.8789 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 05ca1620-dcef-3387-9f73-b722e26b5dee | -13.26559 | -48.06305 | 2025-10-07 04:57:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5226ae6-2dd6-3110-9d21-ba156b4c02b6 | -15.44274 | -49.10226 | 2025-10-07 04:57:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 719b8689-3524-31f0-b12f-af7667918bae | -9.41694 | -61.88689 | 2025-10-07 04:57:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5bf6198c-3af2-377a-8bd2-96e3e7960724 | -10.39467 | -51.60064 | 2025-10-07 04:57:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65d63784-e67b-37e7-b06a-af31b63ae3f8 | -11.11915 | -47.21496 | 2025-10-07 04:57:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ba117cd2-0abd-36b7-9a87-90ed5bc0e23c | -14.90674 | -46.83369 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 06aefb87-c4b6-39a1-95d8-1a7bf51d69ab | -10.40111 | -50.30423 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 8f0443c4-3417-3c9c-819a-93109d0626c9 | -10.67775 | -54.69156 | 2025-10-07 04:57:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4e36391b-8f30-3092-b422-0f729fd92b75 | -14.90407 | -46.84968 | 2025-10-07 04:57:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 612261da-95df-3be4-9c02-192aa56e4dcf | -10.42791 | -50.31331 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| aad46b65-a554-32a4-b951-fd7c52904bf6 | -12.38324 | -51.10727 | 2025-10-07 04:57:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cedb02f4-735e-3e8d-9b92-185a461b1b9d | -14.28346 | -45.85164 | 2025-10-07 04:57:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0ea2d28-cb4f-3b61-97a7-963ac0fad407 | -14.7589 | -46.05276 | 2025-10-07 04:57:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 60b76a1f-d346-395d-9da8-dadb3123a426 | -13.24723 | -47.17659 | 2025-10-07 04:57:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 376de394-e992-3f33-9b72-9b678d37ea66 | -10.34172 | -54.19175 | 2025-10-07 04:57:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12204fb4-b7bb-3c97-bb31-a10986bf773f | -9.96814 | -43.78433 | 2025-10-07 04:57:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 7503b9a3-65c8-3be1-8f75-8081ee4d609b | -11.94596 | -51.46886 | 2025-10-07 04:57:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b5cfb32c-1c69-3761-a39a-1cd8fd35d32a | -12.94393 | -54.72358 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9c6ad44a-784a-3df5-a5e7-e13ca2e0f539 | -12.90787 | -54.73612 | 2025-10-07 04:57:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c487c67e-7e2c-31af-a515-69548a68255b | -10.39718 | -50.30366 | 2025-10-07 04:57:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.5 |
| 6fdc3efc-3e66-3628-a18b-198b886ad419 | -10.59628 | -54.3661 | 2025-10-07 04:57:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7326448b-4179-3006-8393-1547afccb0c5 | -8.55943 | -50.08495 | 2025-10-07 04:57:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 539a4caf-9d88-31a1-876b-0f68625cd83c | -12.24415 | -47.86157 | 2025-10-07 04:57:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7f6ae6fe-b447-3f7c-938b-30e20d30ada2 | -14.63932 | -52.53732 | 2025-10-07 04:57:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 353edeed-f857-3d4e-ae4b-c2cf5d8c6f3e | -15.60093 | -42.3734 | 2025-10-07 04:57:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README97.md)
