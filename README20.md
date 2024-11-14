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
| 62b91449-1959-3593-9ac5-f006b9077c74 | -5.34864 | -46.02858 | 2024-11-14 03:46:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 905fe65b-2867-3484-adf9-4b4397aae081 | -2.66414 | -46.99306 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| e264056a-a6c1-3eb7-82b3-c8f9ba8673e6 | -3.86695 | -41.03568 | 2024-11-14 03:46:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae6e53d8-2724-322f-985d-5db8c0a75346 | -3.953 | -46.41507 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6e2e41f4-1eab-395c-82ff-508bd1938dbb | -2.42123 | -46.27143 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 187becc9-1b28-3b84-b65e-968143bf4c0d | -4.51943 | -46.48265 | 2024-11-14 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6451b3b-4060-30d3-b740-c25ce12ad22b | -2.9883 | -40.70868 | 2024-11-14 03:46:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1ef58ea3-8bcd-3f5a-8993-cd29d7b45b40 | -2.26486 | -45.34838 | 2024-11-14 03:46:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cda92319-89bc-3a04-a39c-5480b29addc1 | -11.69693 | -40.08855 | 2024-11-14 03:46:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 91fbc8d0-9995-3cfd-9742-4c6036979c7a | -2.64019 | -46.16916 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22c8c1e3-c705-3eeb-9fc5-3891f8f982c8 | -4.1551 | -46.25053 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d7b407f4-a5de-3a94-8dfa-1bdaef65b3a3 | -2.88101 | -46.86662 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83c4cbd6-9274-3312-8509-7284801a494b | -7.79034 | -37.59627 | 2024-11-14 03:46:00 | NOAA-20 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f988b3fd-1237-3f00-8743-9fdc7346672a | -3.0491 | -45.53118 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa3a612d-72b2-35ff-9124-01ef83365703 | -6.13296 | -43.96429 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd55af5c-b10e-367c-9c0c-d0e0b415d71c | -2.6396 | -46.17908 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682c79fe-a06e-36f6-88ab-3d279ee41257 | -3.77603 | -41.59515 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e318d21a-43f4-31f2-b90f-23118ad9ab93 | -6.13432 | -42.21129 | 2024-11-14 03:46:00 | NOAA-20 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b19cf4f0-c0ac-3429-ba38-4062e24a2bf2 | -2.42054 | -46.2757 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e8da0da6-e030-3a30-a210-cd49de3ff370 | -4.37141 | -48.08423 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 51da0777-c67f-3d87-b4b8-51da5675ead9 | -1.85273 | -46.29128 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea2e1e0e-8317-3d71-8495-7f8e1c5e06b5 | -4.15171 | -43.73993 | 2024-11-14 03:46:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93af671b-563a-3e8c-8ea0-55010959c44f | -4.94217 | -44.96173 | 2024-11-14 03:46:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bfdbe5fc-2635-3b19-b953-0246d11d0fc5 | -4.45217 | -44.93256 | 2024-11-14 03:46:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7e72dc1-a8e3-3be9-a6c7-5132d733217e | -3.10829 | -45.88317 | 2024-11-14 03:46:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6deab197-a034-35c1-8f84-d5877ff645bc | -6.26611 | -44.54836 | 2024-11-14 03:46:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f675ad97-6e96-3bb7-91db-81877ae0e724 | -8.64954 | -36.9289 | 2024-11-14 03:46:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc14acab-8845-3ab1-a0ef-f3097d0a6b0e | -4.58411 | -46.63153 | 2024-11-14 03:46:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 02ba2c76-0c99-37c4-94f7-43f7170cbd42 | -2.65108 | -46.18114 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9c0fd41-546a-342a-a719-61d417e07f8b | -4.04727 | -47.23104 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ebe5119-8ec0-312c-8265-c98c2188d23e | -4.16511 | -46.25985 | 2024-11-14 03:46:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 996370ee-a25a-339d-887c-722f3422405b | -4.52073 | -46.48727 | 2024-11-14 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93826a47-5369-3451-a154-b8a4fe5aedeb | -3.30035 | -43.51404 | 2024-11-14 03:46:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be071651-424a-3b8f-a015-9abbdcf03c62 | -4.28851 | -42.54515 | 2024-11-14 03:46:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c8f9bd0f-71f8-32a1-985b-c290681b5b22 | -6.26894 | -43.88285 | 2024-11-14 03:46:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb7dfe00-f6e6-3942-acfe-d44f847d4363 | -5.32265 | -35.61617 | 2024-11-14 03:46:00 | NOAA-20 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| cdd03c55-6582-3664-8a88-ced5f45eb8d3 | -4.55567 | -48.01337 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 0704926a-09bf-33d8-bea5-30a74ff6c8be | -3.76334 | -47.49392 | 2024-11-14 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e53c7a2-5b8c-332e-aee3-90b269f73c8d | -6.96292 | -39.8312 | 2024-11-14 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 6.5 |
| cfd52326-bd64-33cc-9366-24e9c9f9e0b9 | -4.18843 | -42.3326 | 2024-11-14 03:46:00 | NOAA-20 | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d0811290-b9c0-3361-8707-6b4b3724c266 | -1.85175 | -46.28912 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 09a95ebb-d558-360f-8b2a-c0b915e3b8ca | -2.66339 | -46.99754 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3613c70b-4d7f-3f95-8ef9-d6459b908d9c | -2.40637 | -45.34722 | 2024-11-14 03:46:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 945b031b-c61f-38b8-a39a-d8da0064d311 | -2.42127 | -46.27103 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b9efdf9c-a823-34c5-9c3b-16b76241e21e | -2.64399 | -46.18213 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94a9179f-98ec-3455-bef7-4efe5a2a3c6f | -5.93983 | -43.78742 | 2024-11-14 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b876fc73-78ab-33a2-b002-5a2c180f270d | -2.27034 | -45.34926 | 2024-11-14 03:46:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 71a6ccd2-9115-3b87-9430-0276bff70df7 | -3.04968 | -45.52761 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 02baff07-522f-3e3b-866d-da66402ac2c1 | -5.94876 | -42.43646 | 2024-11-14 03:46:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| c92ac4fb-9b00-3366-890f-7acd01e8b10b | -4.13459 | -38.7016 | 2024-11-14 03:46:00 | NOAA-20 | GUAIÚBA | CEARÁ | Brasil | 2304954 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c13f4049-3d3f-3eeb-99d7-150a50831426 | -4.92167 | -45.71312 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fedaf7c2-a493-3345-82cb-c76c5ee5667d | -4.45732 | -44.93342 | 2024-11-14 03:46:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47a8198a-7f9a-3016-aa50-e2eccdc944de | -3.77065 | -41.60208 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 64e3a976-1f42-399c-99e3-48411864ef20 | -2.63318 | -46.18207 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3204c62b-c9d4-3e72-9c0f-374de2dc0aa9 | -4.23071 | -46.88015 | 2024-11-14 03:46:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a7284e2-d229-3082-9dbe-2a8b6c7ac209 | -2.98709 | -40.70952 | 2024-11-14 03:46:00 | NOAA-20 | CAMOCIM | CEARÁ | Brasil | 2302602 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 889d2e96-d4d3-3e24-9cd9-8f0be6b96a5f | -2.07418 | -46.56699 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 26cb06fe-2db1-3773-be0c-16a1dbfb7a4b | -3.05399 | -45.53567 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 91d5a42d-bceb-3864-9ef4-a92d56cd9acb | -2.64162 | -46.16719 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48b12c9a-cc50-39e8-a95b-7548c3fd8a69 | -4.45573 | -44.931 | 2024-11-14 03:46:00 | NOAA-20 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e76e280c-b76e-3d0e-abe7-09357106a530 | -6.06083 | -44.0479 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 05b556db-12ab-373d-b70f-ed50774cb94b | -6.05698 | -44.04211 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 20c8c84a-666e-3935-a145-a46d93c1fb44 | -2.1913 | -46.36279 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 918df778-eef4-3376-a254-44c7de141355 | -2.64464 | -46.17815 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a067b34e-fb6f-3b23-b28d-64d8dace4218 | -5.15082 | -46.09349 | 2024-11-14 03:46:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6eefd044-4c92-33e4-b9d3-425ecca47567 | -5.19013 | -44.35989 | 2024-11-14 03:46:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 79a1fd87-77d3-31e7-808b-300fdd086610 | -5.93707 | -43.78491 | 2024-11-14 03:46:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 6bd9b0c6-2fd2-3680-90be-fa8aa187ffe7 | -4.14293 | -43.85066 | 2024-11-14 03:46:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e60448f0-4f86-344e-b55c-66cdc5a1f8f2 | -3.1471 | -45.48586 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e668e35b-f81d-31fa-935d-e092ac7ed361 | -2.887 | -46.86759 | 2024-11-14 03:46:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3d73438f-4363-342c-a73c-ab941fbbd47a | -4.55478 | -48.01851 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| af16a456-43d8-30ea-bcfa-82bd7f01d883 | -4.94166 | -44.96473 | 2024-11-14 03:46:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c4282186-935b-38c5-9dc3-a86c6e196f11 | -4.30058 | -48.10133 | 2024-11-14 03:46:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e241ba67-098e-326c-b785-d76e1e12b04a | -3.77417 | -41.60654 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| aaf071c3-f0b8-3da1-bb56-5d922b07ed70 | -4.05507 | -47.2322 | 2024-11-14 03:46:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a1ffe82b-1d57-353c-ae87-f102e9dc7093 | -2.647 | -45.80743 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ab227fde-c8fb-35e0-9d41-a4a68bacece7 | -2.11625 | -46.53385 | 2024-11-14 03:46:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8534900-a58d-3271-8e0f-0367a266900c | -4.02365 | -44.68382 | 2024-11-14 03:46:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 98fbb4fe-ca9f-333f-8830-9e62d7948263 | -4.02415 | -44.68082 | 2024-11-14 03:46:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0796332d-f34f-381d-bf36-4ca97580ad11 | -3.77955 | -41.5996 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2f27709d-fe08-30a9-979d-bb6eeb1f8f0b | -4.00409 | -45.57369 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c0cc9277-c455-3536-8fe2-f6672b323a78 | -3.13673 | -45.28127 | 2024-11-14 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2e4042c-76d8-34b7-b874-735247fb953b | -8.03326 | -37.4353 | 2024-11-14 03:46:00 | NOAA-20 | SERTÂNIA | PERNAMBUCO | Brasil | 2614105 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 480c0e29-9544-364b-b54c-b1a2ef3689c9 | -2.64466 | -46.18409 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a780634f-9b72-37c8-8bc0-0036e4a28542 | -3.77541 | -41.59893 | 2024-11-14 03:46:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 022968c8-4623-3ebd-bc80-10bc4cc9b7b3 | -2.90285 | -45.59454 | 2024-11-14 03:46:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90edd8f8-3071-3f15-969b-9c7a6cd60811 | -2.36191 | -46.99353 | 2024-11-14 03:46:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ea01dd7a-85fc-34d3-a7e8-99a2564f87b8 | -3.76951 | -47.49478 | 2024-11-14 03:46:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c0d489c7-676e-3e97-8f56-0351f10c2d4e | -4.51585 | -46.48169 | 2024-11-14 03:46:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13f4ab98-7964-3b05-aadb-eecdb28eeff8 | -6.95936 | -39.83064 | 2024-11-14 03:46:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3963284d-2c6d-3619-b550-52f1466f2534 | -2.64973 | -46.18316 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1203a308-c170-34b0-845c-7fcfce1d13cc | -6.03809 | -44.03921 | 2024-11-14 03:46:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4b8086d0-f463-32e8-93e4-94bc7e02a338 | -3.86358 | -43.93982 | 2024-11-14 03:46:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0c853ec9-0997-305f-9211-ab07ce51a192 | -4.15148 | -45.77669 | 2024-11-14 03:46:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 75ade550-5997-3ef7-a1c6-c06da0088196 | -11.86905 | -38.35865 | 2024-11-14 03:46:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ad1da8ab-805a-3e06-94e8-b5bea58ef64d | -2.27093 | -45.34571 | 2024-11-14 03:46:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 43.5 |
| f3defee7-9aa3-35af-a38a-acef51306bab | -5.12767 | -36.38406 | 2024-11-14 03:46:00 | NOAA-20 | GUAMARÉ | RIO GRANDE DO NORTE | Brasil | 2404507 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 11a2abf3-e4dd-3b95-ad57-ff2ac8885bb1 | -3.14746 | -45.28317 | 2024-11-14 03:46:00 | NOAA-20 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6cfa154-4308-3ff0-a902-3fd4e68dc6dc | -2.63186 | -46.18404 | 2024-11-14 03:46:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 276a1b64-31ae-3deb-897f-fcd330fe3af5 | -1.62664 | -46.10585 | 2024-11-14 03:46:00 | NOAA-20 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
