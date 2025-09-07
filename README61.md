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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6942ae41-b3a5-38ad-981a-380dd63a7fd5 | -13.01226 | -54.84411 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 040cf96d-0f77-3d72-aa6c-f1df53c0816b | -16.28882 | -58.12188 | 2025-09-07 04:21:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| bb6ddac5-c6b7-3101-a00f-eb785bfb18c8 | -19.34305 | -42.17643 | 2025-09-07 04:21:00 | NOAA-20 | SÃO JOÃO DO ORIENTE | MINAS GERAIS | Brasil | 3162609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 7466beb7-92d5-32b5-8522-4ae86dceb68a | -16.89789 | -45.74401 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2da85145-978a-3f90-a373-2a9a510993c6 | -13.77306 | -52.77318 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 99e7be98-fa21-3482-993b-c15977356b26 | -14.85078 | -46.69548 | 2025-09-07 04:21:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8c921376-9d69-368f-a650-3013b19ee813 | -16.96908 | -45.83144 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a2f95616-1e90-30a9-92c7-e1fc59b0d665 | -12.9537 | -54.77418 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 4a944533-84af-38fe-a3fb-6079b90645be | -16.92145 | -45.79345 | 2025-09-07 04:21:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5491f337-00e8-30ef-aa34-0840537aa8bb | -20.56063 | -43.71457 | 2025-09-07 04:21:00 | NOAA-20 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e81de5fc-3381-303a-b1f4-1bd2b99a475d | -17.68365 | -43.55351 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b737abc-4b49-370f-ae02-487410d9e2ba | -13.8336 | -46.27683 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3ef9e38c-67ee-3408-8654-0282939fbac8 | -13.85184 | -46.24713 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e4ae1d07-e229-38db-9580-bee81801b02e | -13.36477 | -46.83562 | 2025-09-07 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ab30bbd-5f10-3ffe-8d3b-9712eab8c7b8 | -14.44147 | -48.45938 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1572d1d9-627a-3d90-a12b-6411aa23b937 | -14.49237 | -48.76916 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e038381e-835c-366f-98ae-fd69b144dd00 | -12.95145 | -54.78606 | 2025-09-07 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d1055b8-9a8d-346f-987b-9ccc3cb02496 | -14.68334 | -47.15002 | 2025-09-07 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3e84fecb-f13d-3c17-a305-fdb6f9bfb94c | -16.53306 | -45.09836 | 2025-09-07 04:21:00 | NOAA-20 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d52e1ca-b829-35ad-8d95-d3f4d9b1d579 | -12.8181 | -52.94188 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b7f14f5-8a03-3ed4-be4f-5d6bc084cacc | -13.06051 | -48.06608 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a8942778-ea2d-3b7d-aac4-ec798494e19a | -19.8806 | -45.02968 | 2025-09-07 04:21:00 | NOAA-20 | PERDIGÃO | MINAS GERAIS | Brasil | 3149705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce8e34db-7220-31a9-af4f-a1bf0b3c6d65 | -17.38396 | -49.23427 | 2025-09-07 04:21:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| babc90b8-d200-396e-90fe-85adbd4cade8 | -17.691 | -43.54255 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a6810ecb-e6f6-375e-8812-688698e600f4 | -17.37582 | -49.24072 | 2025-09-07 04:21:00 | NOAA-20 | PROFESSOR JAMIL | GOIÁS | Brasil | 5218391 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a1c86eac-029b-35c4-9a69-bea94c2d96b6 | -17.6739 | -43.51502 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6672af38-1470-3050-bf32-f06c400b696d | -13.84133 | -46.27082 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 49e31d0d-1332-3a89-9a14-27954ab13933 | -12.81892 | -52.93742 | 2025-09-07 04:21:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c7a7a1f9-39d5-37f2-b1d2-6fd5ccca50a8 | -12.62814 | -56.98307 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8bbb9dba-c73d-3a2d-bd6f-6ef94b91d902 | -19.55757 | -49.73672 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 05b99046-b18d-3621-bb01-5412d52d1a36 | -19.88538 | -41.4302 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| ccc6929d-eca4-36af-9828-b1f74c506c1b | -13.71602 | -46.88987 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 97b2931b-da2e-301b-aa8a-ce3a6937610f | -13.66446 | -46.95792 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 38b32224-acaa-38b3-b805-3c5aff16187c | -13.78717 | -52.77473 | 2025-09-07 04:21:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| b88bfe4c-e8a5-3057-89f0-923e3503596d | -13.03891 | -48.06955 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f92f4338-8d09-3320-a8ec-12fad874380c | -14.58467 | -52.13853 | 2025-09-07 04:21:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6394a8ef-98c2-38f3-ba28-e84c1d76a39a | -15.23471 | -52.36541 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62a7be4e-346a-3826-a8c1-f06c3f1717ba | -15.29685 | -46.98891 | 2025-09-07 04:21:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15deacad-47f6-32ff-92eb-ce83c30b5c28 | -18.01955 | -44.90274 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81558e3c-e17c-37fa-93a3-82ac0e32dcfa | -20.45428 | -45.51137 | 2025-09-07 04:21:00 | NOAA-20 | CÓRREGO FUNDO | MINAS GERAIS | Brasil | 3119955 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4e7ab9cb-f771-32da-919d-aeb96f059e4a | -19.41317 | -44.31677 | 2025-09-07 04:21:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 42781e90-e4f4-37c3-b9ee-97b957b0a91a | -20.04308 | -41.22492 | 2025-09-07 04:21:00 | NOAA-20 | AFONSO CLÁUDIO | ESPÍRITO SANTO | Brasil | 3200102 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 47cd307c-33bd-3137-9d06-7b662162a87d | -14.56774 | -43.72758 | 2025-09-07 04:21:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb3b0d3a-9db8-36dd-be29-f26a048022f0 | -16.68766 | -46.80138 | 2025-09-07 04:21:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 21.3 |
| a9aa5fe5-4721-30b0-ae37-36b38e17f589 | -16.29544 | -45.68649 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4cbb421-b25c-3cac-87f3-7eb9381fce78 | -17.67506 | -43.53379 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2d24e71f-213d-3dda-93c2-127da7b6ac19 | -15.84544 | -52.27464 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| add660ee-6280-3524-8614-7662db073f96 | -15.2168 | -52.34659 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 225767e9-b016-3a85-9228-07b9dbe54e4b | -13.89365 | -47.95217 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95dee1e8-7ce4-3279-b8f4-13c98fd15dcc | -13.55401 | -48.11766 | 2025-09-07 04:21:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d15adf93-13a8-34d7-ba25-76c58094c357 | -14.44889 | -48.45697 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0e4ec266-4a05-391c-aec7-0ec7cb6b1175 | -14.49232 | -53.24445 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69a7bb0f-084a-317e-959a-b41e833203ac | -19.61682 | -46.43513 | 2025-09-07 04:21:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 946a4dfe-9612-3904-baac-fbf3498a5375 | -15.17867 | -47.97205 | 2025-09-07 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 776f9bd4-015b-33cc-8b46-b08766cc15c3 | -17.87816 | -44.33499 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6baabd9c-d416-3ea5-a960-e37d51ab4900 | -19.11162 | -49.46493 | 2025-09-07 04:21:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cc11b63-f574-329b-9ad7-e1699ea8271c | -14.77863 | -48.11646 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dfe3a8b-3a4b-3be1-9cda-25917bc8a000 | -13.04138 | -48.05447 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e363a435-6e99-376a-80db-1942dc00b137 | -18.55336 | -44.04383 | 2025-09-07 04:21:00 | NOAA-20 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1f2a6462-fb63-32a8-a262-5ed6127ab67d | -20.35648 | -43.88614 | 2025-09-07 04:21:00 | NOAA-20 | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| a395290a-8d37-3780-9405-8aff6aad1989 | -13.04784 | -48.07925 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c4b05ea-0dd2-345b-a502-3acf32b580d7 | -13.03488 | -48.07272 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faa752a6-0813-3663-9c81-afd37a3b9123 | -16.30161 | -45.69128 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79cb3059-fe31-398d-8770-3f8194324279 | -15.94501 | -41.88609 | 2025-09-07 04:21:00 | NOAA-20 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6302ae8d-9474-348e-8b8e-c6acaa0f3c61 | -18.7327 | -49.62963 | 2025-09-07 04:21:00 | NOAA-20 | CAPINÓPOLIS | MINAS GERAIS | Brasil | 3112604 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5ad3225b-a37f-3b1c-810b-79f812fb1386 | -16.33749 | -52.95051 | 2025-09-07 04:21:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0a38f48-da07-3c60-9c08-467d0a54bc90 | -14.59488 | -48.10078 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bfe15874-f594-384b-b711-78c311421371 | -17.67136 | -43.53313 | 2025-09-07 04:21:00 | NOAA-20 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f69f6290-8cf2-3c03-a36a-8ea481b80410 | -19.89206 | -41.43722 | 2025-09-07 04:21:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 2040aafb-d44c-3aba-a7cf-693dda297654 | -15.70606 | -47.50943 | 2025-09-07 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 45822e75-fd31-3552-94d9-0268ed7b325a | -15.38652 | -52.91693 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6094971f-de5d-3611-9f47-5f7bf26772b2 | -14.8218 | -48.19947 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bee6032d-6e7a-3f50-9c40-7d91a691a7e8 | -13.82423 | -46.27167 | 2025-09-07 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 55918524-2e4c-30df-95f3-0441376bdeda | -16.29207 | -45.68594 | 2025-09-07 04:21:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cac62c78-c254-3031-a37c-0205a3b222ad | -13.04198 | -48.05085 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c432501b-7619-3faf-b2ec-7961829b8375 | -13.65429 | -47.91564 | 2025-09-07 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| da0c83c6-944f-3723-9655-499ea6b5747d | -14.40238 | -53.26692 | 2025-09-07 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b55b4296-7c5f-3bfc-bd05-eaab8041e7f9 | -15.17531 | -47.9715 | 2025-09-07 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da0a6f52-91d5-3ce3-8623-79f1d72908f2 | -13.91039 | -48.0195 | 2025-09-07 04:21:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 96924e40-aba5-3224-be46-1c2c7dba4100 | -15.36311 | -43.66853 | 2025-09-07 04:21:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 10.3 |
| ba9c48da-037e-36c0-9789-ba4ee943304f | -19.36659 | -43.65542 | 2025-09-07 04:21:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e46fbade-c7bc-31ea-ace0-61b40ab5fa95 | -14.82552 | -48.17698 | 2025-09-07 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e07d9f8-9f07-35d5-adc4-9f61d1bd4072 | -13.66721 | -46.9621 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74075e57-cc18-3eae-9700-61e4dc8d1381 | -17.68371 | -44.506 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 766907d1-cdd3-3abb-9a8d-98a2829ff467 | -12.63937 | -56.98151 | 2025-09-07 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee6aa447-ac75-3bf7-8edf-efd1c8caa628 | -13.85129 | -46.25067 | 2025-09-07 04:21:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e82c0c2-0fbb-3a65-b5c5-c60eae1ce462 | -13.82479 | -46.26814 | 2025-09-07 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27255965-ec93-3db4-acfe-12387c99c3ee | -19.59817 | -43.68254 | 2025-09-07 04:21:00 | NOAA-20 | TAQUARAÇU DE MINAS | MINAS GERAIS | Brasil | 3168309 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fbeeb8a-716e-34f6-8f09-e8f4983433fb | -13.03083 | -48.07602 | 2025-09-07 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 07d303a0-8c92-3323-a8b0-84332bf58d86 | -17.36444 | -42.63866 | 2025-09-07 04:21:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 5aa31aa7-28bd-3647-b8b1-5e45d0754f12 | -12.47518 | -53.85466 | 2025-09-07 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f2e2d7af-d75a-36f7-9422-e2446632ad7c | -18.03422 | -47.08949 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c3cf0573-5f76-3c85-b3a0-3901eecb539b | -13.71126 | -46.8781 | 2025-09-07 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9baf7185-b268-36c5-962c-d27ab589939b | -17.74917 | -49.31931 | 2025-09-07 04:21:00 | NOAA-20 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 001270dc-166b-320b-b3a1-837837447781 | -17.38053 | -49.23367 | 2025-09-07 04:21:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58ce880b-3257-3617-9698-88bc29104218 | -16.36935 | -48.96155 | 2025-09-07 04:21:00 | NOAA-20 | ANÁPOLIS | GOIÁS | Brasil | 5201108 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0bd5ffa3-1e58-34f0-b194-2a9431de59ec | -15.73206 | -47.02843 | 2025-09-07 04:21:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 5f7f3b9c-051e-32a9-9351-6ea496db1f9d | -17.71491 | -44.4903 | 2025-09-07 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e7da151-c0c9-34d7-9494-858d297e6f17 | -18.03091 | -47.08891 | 2025-09-07 04:21:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8056c54d-f07e-36f7-96f2-217e083a8b9e | -15.23126 | -52.3609 | 2025-09-07 04:21:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README62.md)
