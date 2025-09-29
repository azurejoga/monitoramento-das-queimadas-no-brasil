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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 160bca83-7cf3-3029-8298-d5437cc9141e | -13.00157 | -49.42992 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cd2c055-ef2f-36e2-a664-4c9d22a416c8 | -14.56341 | -48.25356 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4dc41c62-a886-35b9-b66d-c5832a38e611 | -9.27998 | -45.69915 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e4c6e9e-f1f5-3bb6-8bb9-2b83f0fff1d9 | -12.94737 | -47.17818 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9c20edf8-e715-37de-986e-67913ceec2c0 | -11.71145 | -44.46788 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e17ac851-f045-33b1-b172-9d088ca267ff | -13.7966 | -47.89903 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 0f39a9dc-eee3-34ad-8321-e8e152102fa5 | -11.70959 | -44.43684 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 791790e9-7a6c-3e17-9ab6-4c7fd7053a14 | -12.6681 | -46.90457 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9df6b8cf-b6b1-3b45-9347-13da52a8cfb4 | -15.04733 | -46.96869 | 2025-09-29 04:08:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3c88486e-3792-3e17-90ee-42456fd5bf33 | -13.84099 | -47.48837 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2bc0840-9e69-366a-8a04-f69c1eca3e54 | -9.93805 | -48.80202 | 2025-09-29 04:08:00 | NOAA-20 | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eb80905e-355c-3aa3-b220-4662c0c3935c | -12.93993 | -46.77551 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a48f64-83bc-3ce7-be7b-adcd877a5921 | -10.81252 | -46.6695 | 2025-09-29 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 196c2ba8-31bb-3066-9695-87ccc924cf16 | -11.82883 | -51.79513 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6f0db86c-7f84-354d-9580-40f37ed36000 | -8.88441 | -47.62862 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6b26ea91-9ed9-3fe3-9f13-180ba3e0e466 | -15.25958 | -48.75566 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4c78e635-3abb-3356-b19e-8c3c193d51fb | -11.45349 | -45.0105 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a65a57b-7ffd-3b6e-bde2-005a870a36ba | -13.596 | -48.05882 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| de0ddf08-72dc-3c2f-9f8d-3f633eff3f5b | -13.7823 | -47.86541 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 121d88da-7c98-367b-9809-912dfec6c5d8 | -13.57013 | -47.30611 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5dc42902-e8d4-37d2-9758-ee135548d4a3 | -13.00088 | -49.43371 | 2025-09-29 04:08:00 | NOAA-20 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 088c3c86-1653-3e89-91d8-fe3be22f793c | -13.16359 | -47.44558 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a751db9-dcea-33f3-af2a-a6cf568fbe6d | -15.25825 | -48.76296 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f9bdeb30-5610-3805-8310-8f8b93acf695 | -12.76189 | -46.85733 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a3357524-a516-3fb7-a04c-3e26ca189d3a | -9.87968 | -45.94475 | 2025-09-29 04:08:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df4c22d2-8f3f-3a20-aea0-bf8c72823085 | -13.79439 | -47.88858 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6acbf7d1-2d89-3cb9-8147-1d810d2291e3 | -11.7046 | -44.33714 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e192a0d3-3f2d-35a3-92c4-8057ead8487b | -11.71021 | -44.43311 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dbc0689b-102f-32ca-b018-e46542eefc2d | -11.92432 | -48.03305 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f37c40e3-7a51-36f8-acee-df2d82b333b0 | -11.94106 | -48.00952 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32363eb3-b618-361b-bb4c-0ebb0fa33bf3 | -13.18548 | -47.43432 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85395f9d-fa70-3f1d-9bac-aa22ec07949b | -15.86158 | -46.23777 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7d13a57-b039-3f3d-8f25-641c43103d47 | -11.45324 | -44.99039 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f1028e10-e063-300d-81ce-d72e9dd3c0b3 | -14.54088 | -48.44662 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6b09e2f2-214a-349f-bbcf-a72aa2fa7e92 | -11.66879 | -45.33032 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 58ed0b14-ca60-3887-a197-79e01806ef0b | -11.66715 | -44.28893 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d105dddd-6063-3cfd-a922-e4ca9f64d3cb | -13.16169 | -42.35255 | 2025-09-29 04:08:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b488d669-38ba-38f6-be6a-aaeeaa721c24 | -11.81962 | -51.78659 | 2025-09-29 04:08:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| d798cd52-391e-310e-aea9-ea712573453d | -11.95508 | -48.04978 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f237df6-478a-3251-8259-16973ce48c5d | -13.30427 | -47.31158 | 2025-09-29 04:08:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6acc9694-9c86-35db-8723-c12044b28b6d | -16.73471 | -42.54513 | 2025-09-29 04:08:00 | NOAA-20 | BERILO | MINAS GERAIS | Brasil | 3106507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74232fe9-1ca6-3fd8-ad2b-4162f91eb7e2 | -8.73356 | -44.88396 | 2025-09-29 04:08:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a541c60c-4483-347d-b579-9c9b747b35da | -15.5826 | -42.40767 | 2025-09-29 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c16fc3b0-69bc-3dda-8199-43aabfe540da | -13.16446 | -47.44067 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3e4bd02-44bd-3095-a860-1aaa76d38364 | -12.58496 | -41.2933 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d074b122-09de-3838-8ef9-acb28a9143f8 | -15.18981 | -48.47083 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65df1a2d-7570-3d7b-a715-2dca2231580e | -9.46013 | -45.49468 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6d8e3f2-9ae1-38ce-9e6f-123a70433078 | -15.55293 | -42.66763 | 2025-09-29 04:08:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 327cf773-4ccb-3130-870e-8ddb5e50c0c0 | -11.92312 | -44.75899 | 2025-09-29 04:08:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e1b7380-3f4c-34ff-9c88-b0c1a1bf9338 | -9.30215 | -45.72567 | 2025-09-29 04:08:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 085a18fd-62a9-340b-af94-dad4dc0ff29d | -12.00062 | -46.60874 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a81660e2-ddfa-3a16-8582-3e903b1d1a64 | -12.89281 | -45.21492 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 661c6b6e-ad1d-3eae-8fca-1edf0208060a | -13.1876 | -47.44489 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 292b0cb0-9b49-312c-aa97-0980975af9e5 | -14.93788 | -46.5845 | 2025-09-29 04:08:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4792da65-f904-3ce1-959a-64c7aa5b8c5e | -13.59255 | -48.0668 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ff876f04-0c15-31fc-b227-1cfecd49e5f9 | -15.06358 | -45.06015 | 2025-09-29 04:08:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 31623897-e482-38b4-88b5-2ff9d7ef0368 | -13.8034 | -47.90649 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1f9a89ee-f051-38a5-91b1-0c260f778bb7 | -8.71299 | -47.98278 | 2025-09-29 04:08:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c79dbdd1-99c8-3504-8c70-2f954b29fb6a | -15.47279 | -47.93234 | 2025-09-29 04:08:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f6694bfb-b5ff-3ffe-8425-21032402fa49 | -12.00099 | -46.60163 | 2025-09-29 04:08:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5ca69c3-c4c4-31b3-9850-b1f88a812884 | -11.72104 | -44.43111 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3d1325ee-f41b-3a97-93f1-0c2bf28c4524 | -11.5046 | -44.8521 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4e6e9bde-ff60-340e-bf98-baea478c54ec | -11.71238 | -44.44115 | 2025-09-29 04:08:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eb299ae7-7bb6-3108-8016-09beab8559c9 | -11.37112 | -44.98114 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 729e8cc8-a25d-3f6f-84c9-7d72bc030fb5 | -15.25418 | -48.76235 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 87b5552c-a758-3849-8059-3529be1fa8f0 | -11.26186 | -48.93621 | 2025-09-29 04:08:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 84a18bb4-132f-3a2e-85a0-9fa759db16bf | -11.93442 | -48.02347 | 2025-09-29 04:08:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bdcd0471-129a-3273-80c9-18be6d4a63be | -11.36827 | -44.97674 | 2025-09-29 04:08:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eac4b4aa-ae58-3376-acf7-05d943372437 | -12.01343 | -47.79046 | 2025-09-29 04:08:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a00552aa-c0b1-390c-813b-b897b68cc429 | -11.58081 | -45.48656 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cefb381-b2c2-3201-996a-8af84eac259b | -12.76033 | -46.86635 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| eda86379-53df-3cca-aad6-a27b99b522e1 | -15.25866 | -46.26414 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 916d9fc6-40f1-3453-a34f-56fa2c7fc015 | -14.5342 | -48.43768 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 329d8b67-5395-36e7-9bef-7873c474a26c | -12.94917 | -47.21334 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| acb03d53-4237-3e09-8cf2-4c0f59bbb519 | -15.26017 | -48.77548 | 2025-09-29 04:08:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 46b19fa6-b546-3c56-a293-7aac7dde9bb6 | -12.8915 | -45.22269 | 2025-09-29 04:08:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 95dcb233-c361-39d5-83b0-372a30ca076f | -10.38351 | -47.80458 | 2025-09-29 04:08:00 | NOAA-20 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 74fe1d9c-7997-3afa-bcb3-dc06154bdd44 | -8.86213 | -45.02999 | 2025-09-29 04:08:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 1f104260-58a4-3514-80fa-6c06acfad788 | -15.29356 | -46.42438 | 2025-09-29 04:08:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 718f9803-bc91-34f4-98f9-454a434f5b50 | -11.99766 | -47.10053 | 2025-09-29 04:08:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eca1db2b-06e3-38ad-bffc-2dc4702ab0da | -15.91183 | -46.20108 | 2025-09-29 04:08:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f1292d4-e770-3f24-85eb-b99b6bc5f544 | -12.92027 | -47.15332 | 2025-09-29 04:08:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c13abeeb-2f46-367c-8875-d11034c9d939 | -13.22482 | -50.95368 | 2025-09-29 04:08:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 290f3387-7727-3ee9-9fa9-1f4812673e04 | -9.66202 | -45.74337 | 2025-09-29 04:08:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02644196-ff9f-3cb3-ac2b-45ca0d333552 | -15.41535 | -48.22693 | 2025-09-29 04:08:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e11354a4-ff6f-3d60-8bce-5f87ecc64fa1 | -14.57987 | -48.23036 | 2025-09-29 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 42064c22-b039-3ec8-a733-90edbf8ecadf | -11.45889 | -44.99948 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f155228f-d442-3dda-8c8b-e84026196c96 | -12.58946 | -41.28645 | 2025-09-29 04:08:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| fda7e373-c6b3-3404-afb5-3c63bc09d6c5 | -11.37342 | -45.05431 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8fdacea-97bb-366e-9821-d2fef8ace336 | -9.0555 | -46.72114 | 2025-09-29 04:08:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4360af1a-d94e-3d1c-9ab0-836ee0d421ef | -11.35905 | -45.07619 | 2025-09-29 04:08:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 4bd88f50-756b-3e1f-b9c7-29e7c799f97b | -15.29009 | -49.51356 | 2025-09-29 04:08:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 084b30b1-e97e-3df9-b71e-839fa4a95c13 | -11.43433 | -45.03955 | 2025-09-29 04:08:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b688fbaf-3aab-315b-9b3e-6ace5c921676 | -9.34951 | -47.62577 | 2025-09-29 04:08:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bdcb02a-1494-3dd3-9d68-c8f91e0ab7f3 | -8.82279 | -49.23871 | 2025-09-29 04:08:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7d25616-6f78-3220-9412-ffaea04f447c | -15.27444 | -49.50742 | 2025-09-29 04:08:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c41d2d1a-3407-3eb4-86c9-f5431af95c3d | -11.4844 | -43.212 | 2025-09-29 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b2af1a0c-a200-34e8-b5ea-cfe0b9ae8352 | -9.78729 | -46.93635 | 2025-09-29 04:08:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 403c7802-f552-3018-b1ad-6c651710cd00 | -13.83794 | -47.94112 | 2025-09-29 04:08:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b24511e9-b7da-311b-b15e-a239f58cedd2 | -11.48773 | -43.21254 | 2025-09-29 04:08:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |


[Clique aqui para ver as próximas entradas](README43.md)
