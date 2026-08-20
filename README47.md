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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 02f77856-7059-367f-8a00-722ec774f8d1 | -11.21501 | -55.05661 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b3662dbf-2d18-31c6-8901-caadba56da98 | -8.66803 | -54.65727 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| a0f7c332-8b86-3cc9-841a-98b59578c533 | -10.92352 | -57.17804 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51b1bc1e-d8f8-327d-ba04-682ad61d546e | -7.4061 | -55.52956 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dbc169c4-7e17-337d-9835-259e9988e9e4 | -11.71384 | -54.57503 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef171601-4767-39c6-ba79-2e089951f4d5 | -8.66916 | -54.64988 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a44cc5fe-985d-3d84-ae1d-068f4969b57b | -12.79371 | -48.43536 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6bf859aa-8ea1-384c-8e3a-2df8e00e1869 | -9.22178 | -59.78158 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c296d223-ebbf-3e77-af0e-48b20a680423 | -6.84806 | -59.01451 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 39887cb4-9b75-3014-881f-c41bf43fc74b | -11.19447 | -54.81654 | 2026-08-20 05:06:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debc8e53-2ed1-3527-86b4-5407d8c72601 | -8.67143 | -54.65779 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.5 |
| 246e87fb-3dfa-3e0d-a9f2-985ad75dd86e | -12.25834 | -43.15797 | 2026-08-20 05:06:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 7fa830e2-e929-3df6-a68d-0262d16fe3fa | -13.61108 | -51.79374 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fdf5800e-e54c-3422-92e6-f5b4bb068b67 | -6.84448 | -59.01393 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6474ad8-470f-3d26-a5fe-61be53e39380 | -8.02328 | -54.0099 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3a68b353-5e87-372e-b5f2-27b5e67c8bb8 | -12.00344 | -53.43206 | 2026-08-20 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 02f73759-6fe7-33a9-b383-770d1c937325 | -11.21846 | -54.00614 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f18198f-ef5d-3638-9575-b8ca39fcc13a | -8.56182 | -54.66344 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56633f82-38c8-3a8f-97b0-ec5e1561877d | -8.57089 | -54.67238 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 703449a6-d4db-3ef9-8b59-cc462d005322 | -10.27909 | -48.24009 | 2026-08-20 05:06:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3383109c-964d-36b1-9c8e-7a211fc03111 | -9.40257 | -60.5587 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3414710-2527-3be0-a4f6-f030da705936 | -12.94562 | -56.63251 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 105fd849-01fe-3022-a9a5-5288d36abd4b | -8.5368 | -54.87287 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9e0a86d-37d2-37df-be1d-c300ae84ed47 | -9.27162 | -56.91149 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4ad1db22-cae9-348f-bd81-ae49ee3e5309 | -8.7157 | -49.62019 | 2026-08-20 05:06:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 4e0d90b0-c3d7-3e7b-b443-ac5d498d2d49 | -14.45318 | -45.61977 | 2026-08-20 05:06:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ce5b8635-754f-3f37-a81b-c064b3e3f0b7 | -11.21071 | -54.00918 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0be8bb87-4a95-312e-9e43-8cf50f35b307 | -8.54017 | -54.87342 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 994c18e5-9136-3956-8d26-c14885c903dc | -11.19405 | -54.02356 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 44c639a7-1977-369b-bdf0-26acf11db19f | -8.89841 | -60.55013 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| aa3be237-a368-3d56-8700-5955968cd992 | -7.79169 | -61.18779 | 2026-08-20 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4509c8f4-bd4d-339a-88b2-bddc362ff24e | -11.19226 | -54.01064 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b7ded27f-fb0f-3a62-bdf8-7011e23c4b46 | -12.95063 | -56.64425 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8edcb053-44e5-3dca-8803-810662adb70f | -6.79608 | -59.58464 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| dd4b9c41-92df-365c-a219-cc2ce7073226 | -11.58335 | -50.53843 | 2026-08-20 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3c0cdac9-30b8-3d2e-b6a2-d8c0dbeadf7f | -13.41018 | -54.3727 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bec16af6-f4a8-3620-8ed8-45e570cc2fb1 | -6.79239 | -59.58406 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e8e06254-e716-37b8-ae68-9b84e1c1ed5e | -12.81024 | -48.43701 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a655d02c-18c6-3bc5-8262-47b538878c7a | -11.41612 | -54.31272 | 2026-08-20 05:06:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f48eb41-2df4-34b0-a244-d382d6a28dd8 | -8.56932 | -54.77347 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0d5aa19-d0b0-3234-85bd-36941aecca4c | -8.57996 | -54.68128 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7651bd56-900f-361e-bdcf-9b22505db452 | -7.53939 | -55.59017 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d9447fc0-d419-3144-b42e-4fad3497b23e | -9.21092 | -59.77981 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7538808f-57ae-31ed-9d90-923ea967bd14 | -8.50415 | -54.8604 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 747f6bba-2117-3df3-be09-7585ac9dbf6b | -9.25397 | -56.91585 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f697af6f-34b6-3fa3-8484-6bd13786f76c | -11.18989 | -54.02713 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2eab5fbe-d955-3d60-836c-e3a9070274d8 | -12.94676 | -56.64729 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5af2a843-bc53-3e18-b1b2-392ed82a65aa | -11.87517 | -51.65394 | 2026-08-20 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 080974ed-a44b-3048-a9c2-670ed88a0f42 | -11.20357 | -54.0081 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 67cd4ddc-c4ef-3a2b-b0aa-4cc29162510e | -8.50649 | -54.89039 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4d32eb-f696-33ec-b887-41219a798030 | -9.55149 | -56.79569 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bf67a2f-5b7c-3496-8469-e755289e5043 | -12.83184 | -48.43353 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c6c07046-d181-3128-922e-f8fb9c8355ef | -9.22388 | -59.76894 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 84875be4-b43c-345e-8f8d-ecb97cd108bc | -8.57043 | -54.76619 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e59e1eda-1fd3-3ff9-a05c-7b66ca2912d8 | -8.66292 | -54.64513 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c6b6280-5b35-38c4-b4f3-e15c7ae70bb3 | -13.45147 | -51.4376 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9a8e7217-f9fd-335a-8372-318f09eecb9f | -11.2 | -54.00758 | 2026-08-20 05:06:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 041b1b09-5fd9-3671-8644-bbeedd24a954 | -10.4501 | -54.66434 | 2026-08-20 05:06:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e1c23727-e526-3759-972e-4f7ed35b247b | -9.15833 | -59.5529 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f1eaf17-4499-3d0f-aa41-315ecdfbe5cf | -9.3897 | -60.56599 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d62d18a7-2d08-310f-a0d2-66d2da443f89 | -8.58633 | -54.76125 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4c37b278-5844-3c7c-84a8-cebc433cea18 | -7.41609 | -59.99614 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c7a56aa-bfd3-3685-9deb-1ff55669cf28 | -8.53006 | -54.87178 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3e3d72dc-2b30-3ab2-acd0-c6ebae1906ef | -8.55864 | -54.79795 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c36b8708-d86f-384c-8b0f-8c7e2b11dc61 | -12.83152 | -48.43618 | 2026-08-20 05:06:00 | NOAA-21 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02c2b21c-06b6-3502-8936-7ae662912d5e | -8.57321 | -54.7254 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3b5e38-8140-3dba-8270-ab02ffeae7f8 | -8.56409 | -54.67133 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60146665-e8a2-3696-8ed9-42bdc207cac7 | -9.11375 | -61.60506 | 2026-08-20 05:06:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 55ffeb44-2e45-3c7f-8d17-6355f147d2b3 | -8.53061 | -54.86814 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 752409db-a8ac-3942-8407-452fc7c14b48 | -10.3351 | -57.56528 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4dc5544b-2215-3cd2-8dd4-1ef3fb4d410d | -9.10325 | -60.93354 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 2c7e0685-f168-3a49-8b1e-b3b34216d2fb | -6.76559 | -59.14708 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8270687c-f3e7-3b67-9910-d9df9ad4c893 | -8.52275 | -54.87435 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcb73b89-602d-387e-b9ca-61fbd5f1da93 | -9.3883 | -60.55153 | 2026-08-20 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b0dceb40-586f-3e0d-b258-06f789c00b85 | -11.69945 | -47.81777 | 2026-08-20 05:06:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4e66bdfc-2acd-33f5-b617-8b06239b89af | -10.63585 | -51.61202 | 2026-08-20 05:06:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01d848f6-d025-35c8-92d7-4cfd109081fb | -13.61528 | -51.7943 | 2026-08-20 05:06:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7597fb78-fadb-375f-86e4-78af15b3b6f7 | -8.54643 | -55.31879 | 2026-08-20 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 044c5fdc-5fa6-331b-931a-c24ef49e12a6 | -8.5573 | -54.67031 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 94682d85-d974-3045-8ee4-3dbe71004ac8 | -13.4064 | -54.38736 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7b044a91-70e0-3a99-8c22-ecad9fe134cd | -8.57656 | -54.68076 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| db769fa1-3f3e-3862-a7e8-e4fb5b5cbf9e | -9.07867 | -65.38829 | 2026-08-20 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0df8ed6-72c4-35ca-b150-86eb1986a83a | -9.55095 | -56.79917 | 2026-08-20 05:06:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a437ade3-a33d-3602-9052-833123910de8 | -13.41299 | -54.39265 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c11d879-51f3-3497-90a4-7ea420154d69 | -12.94617 | -56.62894 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1516b469-24a9-3fb7-8f38-daf275deccde | -11.46796 | -46.56864 | 2026-08-20 05:06:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| f06d1b7e-0d5a-3cef-875b-5091a0f447e8 | -10.38779 | -61.21084 | 2026-08-20 05:06:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f3442279-f110-3b53-8852-0aa9676b11b6 | -8.61725 | -54.71717 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f295b6fc-7bf1-3680-adca-86c949ffb5c6 | -10.33842 | -57.56582 | 2026-08-20 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1375b3c0-e5d6-36d1-bb13-bb6eee50df02 | -13.40476 | -54.3847 | 2026-08-20 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d39cb447-737d-3f7c-a9b6-b5f81d2cfc0e | -10.9041 | -50.25361 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1344dfe5-ff35-337f-b79c-566808f4e6d1 | -8.57343 | -54.77794 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73390cab-e02f-3df7-a5c9-627b9ed76dfd | -11.81203 | -56.60144 | 2026-08-20 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a439b59a-cb24-3247-afae-fc277a825b1d | -9.21454 | -59.7804 | 2026-08-20 05:06:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 990a5e45-568b-33b5-aeaf-b57aec8af342 | -8.03788 | -54.02352 | 2026-08-20 05:06:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50c4f347-53a6-36c9-8830-b42b7b4f933c | -11.20873 | -55.05179 | 2026-08-20 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 3aa21e0a-158a-30fb-b57e-8e07addc1f36 | -10.81004 | -50.28862 | 2026-08-20 05:06:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 26d230e9-bf9d-32c5-857e-a863719d4172 | -12.15373 | -57.22563 | 2026-08-20 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e192af63-fef5-34c8-9f8a-009b14aedde6 | -7.87276 | -63.76639 | 2026-08-20 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5641302-083e-3d82-8b7b-049c40667982 | -6.79167 | -59.58847 | 2026-08-20 05:06:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README48.md)
