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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b831b27-6b65-3412-8940-bffad5e88cdf | -12.09326 | -43.34344 | 2025-08-20 04:10:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f4f2cb0-1b3d-3af2-b6d6-e321491e1d1b | -10.59837 | -48.60034 | 2025-08-20 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64b5d44a-1b6c-368f-b6c1-097adbd299a8 | -14.51577 | -46.63282 | 2025-08-20 04:10:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d2889de-6d00-36dd-a823-e6da90e3e9fd | -14.89501 | -48.07617 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0b638bb-28f6-35b7-8b09-2574e2da3725 | -12.90294 | -46.09583 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b89dfbf0-e4c1-36c4-bcc4-b653df43b728 | -14.50665 | -45.95776 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5284780b-d116-3290-9fec-15a85c9d71b0 | -13.61519 | -46.88609 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7cdf4c8-9e58-3078-8893-db4d75427883 | -12.5084 | -47.43399 | 2025-08-20 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3e75286-ea46-3aa2-ae2d-56ce7b48ac55 | -13.40449 | -46.35386 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5ca3586-3507-36b9-b866-49f020de0dde | -10.69527 | -48.218 | 2025-08-20 04:10:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| be5bc05e-38fc-3188-a504-8b749ad354ed | -17.55676 | -44.47932 | 2025-08-20 04:10:00 | NOAA-21 | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fef15e07-49c6-360f-99dc-b2982ec55583 | -17.3406 | -47.1613 | 2025-08-20 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3e58cadf-4940-3623-a776-14f7e523f534 | -13.14152 | -54.93195 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e9054c99-a8fa-3c6f-8bc3-7f0bed139647 | -13.18869 | -46.89746 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 82529ff4-a103-3c36-bca9-51a9ae952d80 | -16.31422 | -50.18428 | 2025-08-20 04:10:00 | NOAA-21 | ADELÂNDIA | GOIÁS | Brasil | 5200159 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e5108f64-6114-3160-89cf-9efd6f16b022 | -13.86709 | -45.55848 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83c4f882-62d8-378c-8ab8-da8449afb1ec | -13.58043 | -47.02228 | 2025-08-20 04:10:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 902a33bb-eb34-3a6b-87a3-c8c57394e68a | -14.68915 | -49.05166 | 2025-08-20 04:10:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eb1aa912-4d9b-3bfc-a892-cf3584ca07f0 | -12.95877 | -46.15086 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4383a5ca-bf06-3b5e-ae13-1b8608276556 | -12.9065 | -46.09639 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5025a0da-ac1c-31bf-9549-07abcccf3bfc | -12.97226 | -56.8695 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8a39da7f-fb9f-37eb-8734-da0ae7cd4ecb | -15.01813 | -54.82681 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b76b0798-ff04-3ec5-a82a-5460d09a29dc | -15.87704 | -50.67408 | 2025-08-20 04:10:00 | NOAA-21 | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f163ea8d-c9b3-3b4c-82ca-25858efe72bf | -13.40166 | -46.37074 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f3b3f304-4fdb-38fb-a77b-33cce1d02451 | -14.15361 | -45.28919 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77e2c96c-04d0-3b63-aca3-276695cd03bd | -12.97668 | -46.19674 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04292ac4-2e49-34ab-b2bd-ce9ec353e7a1 | -11.58812 | -50.54042 | 2025-08-20 04:10:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 03a75c93-1b3d-3fcd-83af-cfe792559048 | -12.23434 | -44.62837 | 2025-08-20 04:10:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ba777a6c-8659-3860-8406-5e071e0da9f7 | -13.03754 | -46.79022 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a820bcc-f669-3fb9-9095-637a04d99726 | -13.33051 | -54.40808 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| aa37d89e-d24c-3e06-a59c-5de51c071a24 | -12.77873 | -48.26945 | 2025-08-20 04:10:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e8a86bbb-734f-30d5-937e-33e9f270b116 | -12.97982 | -56.86829 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a986f0c7-1d21-311b-8dbc-3c21f638af99 | -13.4924 | -47.07732 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 36b3e586-772a-33a7-9199-fba4b5f2e20b | -14.62187 | -54.91318 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 052dd14e-798f-3334-acfb-f830d65d786f | -13.15635 | -54.92244 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4d23c9c4-842e-39b3-8c41-74b64adcfd2f | -12.95947 | -46.14673 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf6802a-7555-328c-876a-f158a20f6581 | -14.99933 | -54.80916 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| baa1425a-6c24-365e-8d5f-899bb134804b | -12.9934 | -45.20751 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5eb19ea3-bb20-3e30-bb08-6d5c032ad89e | -13.17488 | -46.86745 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 35b56b61-cc39-3fe0-ad53-f1905b7325b7 | -13.49103 | -47.06305 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e517c0b-6154-3afa-b029-97b557e6979f | -13.87334 | -45.56349 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6fa636e8-87f2-30d4-844f-2123c235eaeb | -14.50598 | -45.96172 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 907cadc2-af82-3390-844a-946636f8c0e1 | -13.32963 | -54.41248 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2a43190b-aeb8-3a39-a482-b6b753585ff9 | -11.04466 | -44.59676 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e75f88a1-d66d-3885-841d-e2910482f006 | -15.5447 | -42.28801 | 2025-08-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 45a1c07f-7178-34cf-96ed-8d3d56983ea0 | -11.31116 | -44.92253 | 2025-08-20 04:10:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b146e35-a903-3286-8445-03c0f62f008a | -12.95022 | -46.15811 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7993fc72-6f54-3003-8002-58dac80b1587 | -17.67546 | -50.48732 | 2025-08-20 04:10:00 | NOAA-21 | SANTA HELENA DE GOIÁS | GOIÁS | Brasil | 5219308 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4694f762-4969-3a34-927b-2f2412c6ef3a | -13.04121 | -46.79082 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9bd0cff0-e03b-3423-b85e-ab2cd02f8d00 | -13.13888 | -57.16096 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 3797f839-120d-3cc6-8506-b81d1c77884d | -15.5458 | -48.56821 | 2025-08-20 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e781962f-76a2-3997-bf83-1152ca2eca5e | -13.08421 | -46.82647 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c0cf1111-784f-36cb-8d7a-0f4434fe0af9 | -13.4881 | -47.05788 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 00a6b83e-80bb-31fa-bd23-033471fd22c3 | -15.9065 | -50.83779 | 2025-08-20 04:10:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4481fc59-57de-3596-b1e9-884cb238ba57 | -13.03049 | -46.79095 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 3c5a7e7b-9a70-3494-950d-19d308d5c292 | -12.59065 | -47.0732 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8e4d1e31-6187-3af0-95f6-e3005a7a5ecc | -15.05896 | -54.83694 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bbea4cc7-9937-35ae-8384-c21d996b8ffb | -12.86941 | -46.05642 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 733f7100-dbe0-321f-a336-41f81c90a018 | -13.56145 | -44.46269 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f27aed17-3dba-3102-9ef9-03f7a6bdab98 | -12.85187 | -44.58347 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f670024-b743-3d88-83b1-75b09cf261bd | -14.15763 | -45.28599 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b5f61ef-ea34-35d6-b13e-63358cd7de03 | -13.17784 | -46.87224 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 06c10cdd-9384-31bf-898e-efcdc7b2f4b1 | -13.48948 | -47.07212 | 2025-08-20 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4f33b02-d9b3-3027-a9d7-a27d36b4be0d | -13.00463 | -45.18211 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e80488-c0d9-3eba-a482-ae9a4c3c1251 | -14.9975 | -54.81806 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d8b575ac-4d32-342f-b414-5a5aae78592a | -14.89231 | -48.09122 | 2025-08-20 04:10:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fec8139f-ba2b-3a7f-a6dd-0c3883099f27 | -13.14726 | -54.93599 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 157b0192-074a-32ed-9452-ff05544028fb | -13.04044 | -46.79528 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12eb8eff-ce8e-39a2-bf33-bede409841d6 | -12.43083 | -48.69984 | 2025-08-20 04:10:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1771aeb5-26ab-324c-8764-faf363297e99 | -13.34323 | -54.40598 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c24d4de8-f25e-35d2-b9fd-004787cac1e7 | -13.87053 | -45.55906 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2dc368e2-1294-347d-b5ff-f046d6bc1e03 | -14.99442 | -54.82278 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 564104da-7763-3933-ad09-619b11de191e | -11.97226 | -46.77809 | 2025-08-20 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfc847fe-ef65-3104-abaf-c88f19e1f008 | -17.57852 | -45.38705 | 2025-08-20 04:10:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8712fdc0-1606-3739-b6d0-da226902653b | -15.54416 | -42.2917 | 2025-08-20 04:10:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 00b21650-e52b-329d-a865-6c212c4d9932 | -14.46086 | -48.38051 | 2025-08-20 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42df9235-bb41-32b9-80bf-5f1b7da9e104 | -14.9947 | -54.83166 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c552b5bd-0fa1-3975-9acb-364266e19a20 | -13.33371 | -54.42277 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 24d64584-c3d0-38fc-939f-a834670b9bff | -13.43315 | -57.09612 | 2025-08-20 04:10:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e4b2275d-19a8-3eb7-8dce-9fdac4370a3f | -17.1876 | -39.68272 | 2025-08-20 04:10:00 | NOAA-21 | VEREDA | BAHIA | Brasil | 2933257 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 47d1b047-1cbb-323f-a8a8-7bc4a4824ee4 | -12.59148 | -47.0684 | 2025-08-20 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 706e2493-137d-3f47-8353-7b75be35e7fd | -13.03082 | -46.80717 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 252c4a4c-7bda-3e3a-afda-30b4bdcb57ee | -14.99564 | -54.82711 | 2025-08-20 04:10:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6f28d6cf-0837-3f33-ae49-d71bc6cb46bc | -13.3278 | -54.42154 | 2025-08-20 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f33ed6ba-8ba6-3137-b32d-c484e19e0b62 | -15.40631 | -46.58972 | 2025-08-20 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a4cefac-25d4-3635-a0fb-1e8634844832 | -13.03887 | -46.80431 | 2025-08-20 04:10:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aa5bf67f-4502-3805-9e8c-9b33bdd72533 | -13.4109 | -46.35948 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f381993-e44f-3da7-9a2d-d5888f9d6256 | -13.56204 | -44.45906 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b457a12d-9b30-3177-be99-fff6d41ac358 | -11.97304 | -46.77358 | 2025-08-20 04:10:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 276bf1e9-9b82-32c6-9b6e-200c4a20cd4c | -14.1615 | -45.28693 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 24041d75-4d6a-31bc-a036-2467a640a3ed | -11.13223 | -46.98041 | 2025-08-20 04:10:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30f8d088-ca00-38ea-b348-84c06a047277 | -15.1956 | -48.74657 | 2025-08-20 04:10:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2741573b-4cef-32ec-9a3b-92f3cf9ad8b2 | -15.65059 | -52.68819 | 2025-08-20 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bee99d43-c9bf-3aff-a20f-7e8fbe78e497 | -14.88435 | -48.06937 | 2025-08-20 04:10:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9e238d5-ac20-34e0-9ac6-a584b6286e58 | -13.14663 | -54.93804 | 2025-08-20 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f0774e4e-3d82-37c0-b366-b9b38d7eb472 | -14.16225 | -45.27903 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 143dc791-c1f1-38c3-bd30-610bfc836b8c | -12.67664 | -45.8204 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c97eeba3-612c-33ce-8a64-d41fd26fa10a | -14.16427 | -45.29129 | 2025-08-20 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff70f395-bd54-3934-b48b-c590f4a84956 | -14.61681 | -54.90762 | 2025-08-20 04:10:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 15770b63-ea2f-3131-9647-090fb3005035 | -12.47811 | -44.79008 | 2025-08-20 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
