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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 69e29db5-84f8-3089-9772-85ee13f39ea7 | -13.98987 | -44.54858 | 2025-09-01 04:34:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 710fbae2-a609-3be2-8817-2813357dff28 | -14.74132 | -46.74195 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3bbbc451-912a-3e9f-814e-20f693152768 | -15.69666 | -48.92911 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c317ae13-1e4a-39dc-829c-0347ab503f59 | -13.39938 | -47.05862 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23a7a9e9-8209-3e7d-aedd-a5388098eea8 | -15.32206 | -46.111 | 2025-09-01 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2605437f-005a-3af4-9610-18219b2e3a7b | -14.55906 | -52.99619 | 2025-09-01 04:34:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9e004da-52c8-383c-afc1-b9a2e60ef869 | -14.76695 | -46.76734 | 2025-09-01 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c14599ac-dcd4-383a-80b3-ef46c28620e6 | -12.57594 | -44.80435 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b486021-d9d6-3221-903f-250f4e9b7d97 | -8.62084 | -62.59392 | 2025-09-01 04:34:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f997d52-db06-36ba-8357-392dca4f12e1 | -12.84674 | -48.07748 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| fad36619-d364-3647-a3bd-d43fc911d8bb | -12.32571 | -45.72452 | 2025-09-01 04:34:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a66d39ff-57af-387a-8817-369739b174e9 | -11.78677 | -46.46239 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| da44ea7c-ac48-3109-a802-bcbdf3abad1b | -15.72682 | -49.00111 | 2025-09-01 04:34:00 | NOAA-20 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 20.3 |
| dc288781-3da1-37b1-9ca0-757783401016 | -12.97198 | -48.11469 | 2025-09-01 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3dd664c8-36e4-3a9b-916e-0fb466c6d457 | -14.99544 | -48.14841 | 2025-09-01 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 922df614-4d55-36a2-8617-12a711681ae3 | -11.80336 | -46.42396 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5a2b4b38-8727-353c-ad20-5362f3b783d9 | -13.47187 | -46.93614 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 81eff0b2-5cec-3170-b720-51ee81171dde | -8.74146 | -62.4118 | 2025-09-01 04:34:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba08cbd2-1c34-32f8-838e-3349c49ace3d | -12.62826 | -56.99006 | 2025-09-01 04:34:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8752613f-be4c-3fed-a0ad-e5759746c3a5 | -13.36959 | -46.9449 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 20453396-a6bd-3cee-a8ce-aa81d3fc16e1 | -18.21672 | -42.20268 | 2025-09-01 04:34:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 02d3ec39-50e7-3470-8733-f846b3e5e095 | -11.0448 | -46.97382 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5b70c4e6-5741-3f96-9c04-7cc21b28b63c | -13.31729 | -46.85607 | 2025-09-01 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d1082eb-83fe-3a36-b37a-7ebf35fc558a | -11.85289 | -46.79021 | 2025-09-01 04:34:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73ed0c7a-87d7-317e-bd30-f694e424375e | -12.57286 | -44.79139 | 2025-09-01 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ece8c083-5ddc-3aa7-95a6-e3a8bb609053 | -11.80749 | -46.4205 | 2025-09-01 04:34:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc486988-3605-3616-963e-292109c95db4 | -13.59663 | -48.14087 | 2025-09-01 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99780724-55bc-3f94-86bf-cdcf32e04382 | -13.36618 | -54.38197 | 2025-09-01 04:34:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 13f313ff-7473-34cd-888e-bdaeb568e2f7 | -22.2537 | -54.8888 | 2025-09-01 04:36:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 58e3bbc9-910a-33f0-a706-48e90aea4fda | -20.87831 | -51.48669 | 2025-09-01 04:36:00 | NOAA-20 | CASTILHO | SÃO PAULO | Brasil | 3511003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 63eccffd-41f6-3c24-af1c-b38529436cf5 | -18.65972 | -52.59345 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 1cdf9579-57c9-3e5f-b9eb-7c8765747dab | -24.20292 | -50.93684 | 2025-09-01 04:36:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d67fde21-f114-38d1-aa5c-3d6443ba2c97 | -24.14722 | -49.83592 | 2025-09-01 04:36:00 | NOAA-20 | ARAPOTI | PARANÁ | Brasil | 4101606 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6da33e9e-6a26-3b58-9d87-3b313f04d5b5 | -21.73397 | -50.74342 | 2025-09-01 04:36:00 | NOAA-20 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| bb3d605e-eef9-34db-ada9-dfa16526abb3 | -20.8962 | -55.14192 | 2025-09-01 04:36:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e18a64a0-7ab7-310d-b343-9ccbd46e0d9c | -19.48336 | -46.58982 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5fc2cca9-6964-32f4-adb6-dfab05583249 | -23.59137 | -54.76445 | 2025-09-01 04:36:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 1b6f5664-e8ee-388a-a50e-5a6b6c9c2dfe | -21.08564 | -48.23051 | 2025-09-01 04:36:00 | NOAA-20 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 46540acf-a7b2-3ced-833f-0894696fa66b | -19.35008 | -44.00188 | 2025-09-01 04:36:00 | NOAA-20 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3eaef9c8-ae81-388d-8165-2d0e0e562f32 | -21.08922 | -48.23108 | 2025-09-01 04:36:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 24ca3b15-0d11-36dd-99b7-14816a4e947b | -20.09876 | -47.33736 | 2025-09-01 04:36:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eb0dc239-0e60-32c0-8295-7f5817e4e5d2 | -19.48398 | -46.58511 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b2163bde-93e7-3200-82f3-274e29941b8e | -19.34811 | -43.9984 | 2025-09-01 04:36:00 | NOAA-20 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 575fa8fa-645e-3eee-b73f-c4fc081d9d87 | -21.35174 | -49.05483 | 2025-09-01 04:36:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 79b39471-b960-3b4f-85fb-0ce38ded58a6 | -18.65845 | -52.60113 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f403447f-380c-39c6-8c71-63517cab0c3c | -21.73064 | -50.74284 | 2025-09-01 04:36:00 | NOAA-20 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 326b88c1-d435-305e-b2f4-3b22f8d8e23d | -19.76126 | -43.95494 | 2025-09-01 04:36:00 | NOAA-20 | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0548cfc-0eba-3948-aa6d-f79189ac1f9b | -19.48779 | -46.58574 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4c1f00b3-f69b-36a6-b2ae-30d55d21a4e9 | -20.4106 | -46.42099 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cf45dd9c-be0c-31ad-b1e5-1b1d7d7150c4 | -19.09229 | -46.16402 | 2025-09-01 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3a721824-15e1-3c11-9e12-a99ceaf584ce | -21.97085 | -47.66005 | 2025-09-01 04:36:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 288420ed-747d-3ee0-97d5-206df8275a0d | -23.17573 | -47.11478 | 2025-09-01 04:36:00 | NOAA-20 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2d9f0923-2ae8-3495-9a11-3a685aea5276 | -23.80473 | -48.15198 | 2025-09-01 04:36:00 | NOAA-20 | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| da5d86ce-85fe-3369-bfa3-9602ecf6b141 | -19.12208 | -46.44661 | 2025-09-01 04:36:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f6c1b6c2-04b1-377b-8144-88358a9bdddd | -20.40677 | -46.41985 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0498489e-91b7-302e-aa43-ed53615a2ab1 | -20.40354 | -46.41404 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| dacda578-a1a5-39be-91aa-354d3c4df936 | -19.93603 | -47.06205 | 2025-09-01 04:36:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0d7d7145-43fb-377c-8d51-dd1d06b5c52a | -20.63562 | -55.31315 | 2025-09-01 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ef16ce70-5df0-397b-8fa7-aea1c8c6d40b | -20.41127 | -46.41589 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f182ebb8-7812-320e-bd85-cfcf270ce9d2 | -18.91058 | -47.20274 | 2025-09-01 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d07f4074-5f73-388e-9b54-d21ac8e13ec4 | -23.38668 | -47.05143 | 2025-09-01 04:36:00 | NOAA-20 | ARAÇARIGUAMA | SÃO PAULO | Brasil | 3502754 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d96081b1-15e1-39cf-a9ff-17afafea6fff | -19.50901 | -45.31512 | 2025-09-01 04:36:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1600be66-4cbb-30f0-acd8-9e0e2991cf23 | -21.08624 | -48.22615 | 2025-09-01 04:36:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 238ce306-19fb-3aea-9922-82bb51033007 | -21.08504 | -48.23487 | 2025-09-01 04:36:00 | NOAA-20 | PITANGUEIRAS | SÃO PAULO | Brasil | 3539509 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 42e4dd4f-753f-3c65-bf1a-f0edc831e7ac | -18.57176 | -48.34973 | 2025-09-01 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 445ee852-731f-37e6-afbe-f11ed7f4e2c8 | -23.36097 | -46.90987 | 2025-09-01 04:36:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 2ec3ea61-3062-3444-abff-66307b2ac65d | -21.35233 | -49.05076 | 2025-09-01 04:36:00 | NOAA-20 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| a44ea3a9-0a7e-3b77-a9bc-6cb76a48da42 | -21.73007 | -50.74659 | 2025-09-01 04:36:00 | NOAA-20 | RINÓPOLIS | SÃO PAULO | Brasil | 3543808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6d97ee63-1712-37c2-a527-c61daf25d59f | -21.08862 | -48.23542 | 2025-09-01 04:36:00 | NOAA-20 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a3d9f16f-d5ab-3c3b-aada-1ce861437d82 | -19.34757 | -44.00305 | 2025-09-01 04:36:00 | NOAA-20 | FUNILÂNDIA | MINAS GERAIS | Brasil | 3127206 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 393b06bf-49cd-377a-8145-5323306387d0 | -22.31099 | -49.05559 | 2025-09-01 04:36:00 | NOAA-20 | BAURU | SÃO PAULO | Brasil | 3506003 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf7ad9f0-c435-3a07-b2d9-fad02e058959 | -19.49162 | -46.58628 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bf3ec510-6bba-3c26-b346-8a58573adf02 | -23.84501 | -50.70671 | 2025-09-01 04:36:00 | NOAA-20 | SAPOPEMA | PARANÁ | Brasil | 4126207 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4c460bd2-5844-39c0-8289-9561a0eaa912 | -18.57119 | -48.35372 | 2025-09-01 04:36:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f1892318-36b7-359a-bad1-75da2451c4e9 | -23.11186 | -46.61624 | 2025-09-01 04:36:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 47159e4b-bf84-3130-8be7-16f510b6e797 | -18.9112 | -47.19823 | 2025-09-01 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 102e8a07-e286-3f69-b788-21a0f76cd73d | -22.45037 | -49.01313 | 2025-09-01 04:36:00 | NOAA-20 | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| fe328d88-4cee-3f3e-87da-1a7be00aeeee | -19.85917 | -45.01284 | 2025-09-01 04:36:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 73d83fd3-65ab-3f8f-a86c-1ef3647267b4 | -20.11095 | -47.31788 | 2025-09-01 04:36:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e212d336-e131-3b3a-a078-a1e78300f20f | -20.40883 | -46.40403 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 650e860a-c7b2-3b6d-bd81-3cf0604cd52b | -19.47954 | -46.58919 | 2025-09-01 04:36:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 70df824e-e02f-3847-9b01-e5957d3b6507 | -18.65504 | -52.6005 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 3ef80104-b645-317c-86fa-4bea3c50a64f | -19.6398 | -48.01122 | 2025-09-01 04:36:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b66886df-5fe5-35c5-87f4-a4f6fcc66734 | -20.89252 | -55.14117 | 2025-09-01 04:36:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f87acd97-ed85-3441-842b-a84975455ad5 | -22.36146 | -52.13232 | 2025-09-01 04:36:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 339ed749-42fd-3acf-bd12-b7e4506a1c50 | -19.85863 | -45.01706 | 2025-09-01 04:36:00 | NOAA-20 | NOVA SERRANA | MINAS GERAIS | Brasil | 3145208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bef6707f-bcf6-37fb-9eec-80cc7016da5a | -19.93273 | -47.06375 | 2025-09-01 04:36:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef725c61-713c-3648-83f4-b2f62e165840 | -20.6365 | -55.30832 | 2025-09-01 04:36:00 | NOAA-20 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4459649b-13f5-392e-8da1-9cf0743a9404 | -21.97147 | -47.65537 | 2025-09-01 04:36:00 | NOAA-20 | DESCALVADO | SÃO PAULO | Brasil | 3513702 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bbc25555-a435-3ae5-a83f-30a3576b3e6e | -18.66001 | -52.59203 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 8f347a1b-c146-3002-b786-4f7cabf4f2a9 | -18.66276 | -52.59649 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| a84421d1-aeba-3b26-a711-1b92cc558146 | -20.40292 | -46.4188 | 2025-09-01 04:36:00 | NOAA-20 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ddcaa2ae-54a9-3da3-aa12-9d04b5684d39 | -23.20888 | -49.75998 | 2025-09-01 04:36:00 | NOAA-20 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b72bfd06-caea-3878-95e2-bac2f47d8ee4 | -18.91425 | -47.2033 | 2025-09-01 04:36:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 220f2d24-99e8-3f51-ba5e-e62818b67e24 | -19.97273 | -50.21851 | 2025-09-01 04:36:00 | NOAA-20 | INDIAPORÃ | SÃO PAULO | Brasil | 3520707 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d4a2654d-884c-310e-a1b0-1726cfe11341 | -21.8752 | -46.74943 | 2025-09-01 04:36:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3efa5d7a-ef40-3e4a-8066-f9d3e9474fc7 | -21.87123 | -46.74933 | 2025-09-01 04:36:00 | NOAA-20 | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| ac7e0407-592f-31af-872e-0786c99efa3c | -20.89988 | -55.14272 | 2025-09-01 04:36:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a00c059-cc22-3d1d-bd7e-777c22c62f20 | -18.66341 | -52.59267 | 2025-09-01 04:36:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 13.9 |
| c8cd36d1-fd83-345b-9fc7-61a07ac7be5a | -23.35699 | -46.90952 | 2025-09-01 04:36:00 | NOAA-20 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |


[Clique aqui para ver as próximas entradas](README74.md)
