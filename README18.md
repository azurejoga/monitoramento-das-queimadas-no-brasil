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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ce0e509f-a80e-3354-be8f-ce7b6491298e | -7.1471 | -44.17055 | 2025-08-25 03:21:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cd96943-8c7e-3c0b-a9a5-9679d47a795e | -5.86189 | -43.89456 | 2025-08-25 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 65422209-02d9-342d-8c32-cca309c7c411 | -7.14834 | -44.16397 | 2025-08-25 03:21:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1ff3609-ef03-3d34-9315-e266d3d702dc | -7.73437 | -35.13695 | 2025-08-25 03:21:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cdfb7e8e-8c8e-3682-810e-a099fc65a3a5 | -6.24496 | -43.74843 | 2025-08-25 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c9f283f-af40-331f-82fd-ca841db2de16 | -7.65693 | -42.67778 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 15470cc9-1d44-3b33-90c4-e4adafa1b33e | -7.0913 | -44.63792 | 2025-08-25 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f7ada24a-53e4-3410-a4a5-4bd94db3194b | -7.65788 | -42.67285 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 816721c9-ea40-3f92-97ff-5e0b2a7dd111 | -4.17154 | -40.71812 | 2025-08-25 03:21:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ca96f03-7209-3c4a-9bb5-3bc8c816ad60 | -6.24371 | -43.75512 | 2025-08-25 03:21:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 705f196c-bdbd-339f-a29d-50e050a0ac18 | -3.45685 | -43.34986 | 2025-08-25 03:21:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| bfc9d799-85cf-38d2-b4a4-6857683ca4f3 | -6.91576 | -43.77863 | 2025-08-25 03:21:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 919e103c-aa2d-36bb-b652-ea318877e942 | -4.17356 | -40.71922 | 2025-08-25 03:21:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ea33194a-7312-3d74-8938-1cefd66f3f20 | -5.48721 | -37.26222 | 2025-08-25 03:21:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.9 |
| fdec048e-f7db-3afb-88f4-026337b28080 | -8.40937 | -39.83344 | 2025-08-25 03:21:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3a8ce03e-e6d7-3d9e-8e8d-1c73b3c7c126 | -7.08851 | -44.63589 | 2025-08-25 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 54977e07-42d0-3b72-843d-da261920bd51 | -6.43635 | -44.56504 | 2025-08-25 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5f8f9533-5276-3f73-9471-46ad6f4fc303 | -4.17076 | -40.72255 | 2025-08-25 03:21:00 | NOAA-20 | GUARACIABA DO NORTE | CEARÁ | Brasil | 2305001 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62302d8b-0f3c-3505-adf5-e5b56b2e62a8 | -5.86061 | -43.90139 | 2025-08-25 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f4223dc0-6124-35af-9724-d0e28a2ec088 | -7.66057 | -42.67801 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0ed3db7c-9f94-37e4-9aa6-e54654f63694 | -3.458 | -43.3432 | 2025-08-25 03:21:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7623c49b-480e-36f8-92e6-16bbd056c7fa | -6.67935 | -44.42971 | 2025-08-25 03:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4ca6a90-8476-3aea-af0d-c379393d4fbc | -6.52784 | -44.43521 | 2025-08-25 03:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 93b31198-78c2-35b3-93b1-f0f03d8dbc3a | -6.67703 | -44.4235 | 2025-08-25 03:21:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f7d622e2-8ad9-3ed0-8e10-f28df10ad281 | -5.49181 | -37.263 | 2025-08-25 03:21:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79ca4e67-614d-36b9-ae00-199b17231145 | -7.7566 | -34.91829 | 2025-08-25 03:21:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d04b9c0d-8313-3cfc-a6fa-4962adfb6a26 | -8.41037 | -39.83174 | 2025-08-25 03:21:00 | NOAA-20 | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d8f5ca8e-5a1e-3d2a-8e44-6729392e6c7a | -6.03512 | -43.99187 | 2025-08-25 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 598fbcdb-27c1-3603-9e3d-6955d6af1bf1 | -7.74975 | -34.91238 | 2025-08-25 03:21:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 841d8868-f47d-3872-85a0-6348e3454c26 | -7.65429 | -42.67667 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8f35774d-ab38-3170-814b-e3af898f7c3c | -7.65883 | -42.6679 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| a88848a1-ba41-36d7-8774-4d9f3ffaa543 | -7.66417 | -42.67416 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1343f92c-7b38-3fe6-940a-aa48bcc55d0f | -7.6615 | -42.67302 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 447505c6-c8ba-3984-8eb1-2bd47cf04d79 | -6.03603 | -43.99809 | 2025-08-25 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b9eb0f9a-5a6a-342a-ac06-c57d28ecc877 | -7.09269 | -44.63078 | 2025-08-25 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c91acaa5-9c22-36eb-9242-96b50e43c232 | -7.74861 | -34.91492 | 2025-08-25 03:21:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7f5d689e-4be5-3dc7-9899-39bc1f6aa2f9 | -5.86775 | -43.90173 | 2025-08-25 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6009f288-42d0-3999-97f2-b1b6b06b5851 | -6.43548 | -44.5559 | 2025-08-25 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 618f382e-1ac3-31e1-a617-b05407eb8f3b | -7.75621 | -34.91619 | 2025-08-25 03:21:00 | NOAA-20 | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 842e9ff6-c10d-308e-90ce-df4903ccd40c | -7.73823 | -35.13758 | 2025-08-25 03:21:00 | NOAA-20 | TRACUNHAÉM | PERNAMBUCO | Brasil | 2615508 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| bf1706be-7813-3f01-bf3d-069876eb67b5 | -5.8629 | -43.89845 | 2025-08-25 03:21:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 14835faa-973f-3351-b1d0-f38441f90aff | -6.03405 | -43.99752 | 2025-08-25 03:21:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f47d52de-ee95-39d8-98d0-8fca0c21a02e | -7.66241 | -42.66806 | 2025-08-25 03:21:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e21daf80-959b-3ad1-8e38-c0d00205db1d | -5.49101 | -37.26777 | 2025-08-25 03:21:00 | NOAA-20 | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7cfafac9-7dd5-3e95-972d-f452a547112b | -6.4378 | -44.55759 | 2025-08-25 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7438946c-9c44-3319-b828-74bc57622607 | -6.43406 | -44.56344 | 2025-08-25 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74bc42d1-a02b-3818-accb-1621dd6a53e7 | -6.43273 | -44.57056 | 2025-08-25 03:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b9268171-2c8e-3073-be68-11ac8ef79e11 | -7.08988 | -44.62861 | 2025-08-25 03:21:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edc83f93-88db-3c38-bfdf-a267b8b567e2 | -11.14026 | -44.7934 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 138dc993-5c6d-33ac-9a09-618557e3f44a | -11.09417 | -44.76817 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 87c6ba1b-bf81-3b0a-bcb9-5b6263a09efe | -9.5187 | -40.33205 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 8dee4366-bff9-3cb6-9387-604cf4acfed2 | -10.60097 | -44.33116 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 76ad2d04-e217-3883-bdf3-fd67e84415b2 | -11.14571 | -44.80102 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 127fe845-7e96-35da-855b-034cde1b7f1f | -10.59645 | -44.33902 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 5ef943df-5fd9-3b25-a967-4346836490ce | -12.99053 | -45.2276 | 2025-08-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8775be77-ad02-3ef2-8c04-d02add08c75f | -12.93492 | -46.32318 | 2025-08-25 03:23:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 94b5fdee-433d-3ae4-bcce-cbab5b8c4bf0 | -9.52811 | -40.33392 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0c0aae03-a420-31c7-92ed-4c01a915d885 | -10.59436 | -44.32973 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 05d8462d-c6ae-3cf5-bb26-77090db24300 | -11.10523 | -44.79279 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ac6db54-dcc1-3c41-b92f-0396f4b10f4d | -10.59768 | -44.33298 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 032d7db9-fd30-3113-944e-75d8b9d8fe89 | -12.93253 | -46.31421 | 2025-08-25 03:23:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a22f7e40-400c-33a6-ab17-60704cc85470 | -10.5989 | -44.32701 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d7be0eda-bc70-325b-9897-3885800b1e6e | -11.09288 | -44.77451 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6a25f01-d124-3a6d-9117-37937f6edec3 | -11.10651 | -44.78671 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cd9201a-ecef-3490-bceb-333771ad69bd | -12.93716 | -46.3127 | 2025-08-25 03:23:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5345ffd3-4766-3120-8cba-d8fc8e4015b7 | -9.52222 | -40.33622 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 79d45808-b9a7-3a13-be60-d86f0d8f7fc1 | -9.52749 | -40.33722 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0951b307-f6b0-30c2-8bd1-4c12ce693185 | -9.52337 | -40.33638 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16312274-bc6a-3d9c-9eca-38ad48a95536 | -9.52397 | -40.33307 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| e844b722-257a-3094-a8da-8c01ca7da0dc | -9.52284 | -40.33292 | 2025-08-25 03:23:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 702dc87f-84f8-3566-baf9-3fca68148092 | -12.75129 | -44.41951 | 2025-08-25 03:23:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1c04c45d-9fc8-3649-97ad-34cc28a96892 | -12.98772 | -45.22812 | 2025-08-25 03:23:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c98788a2-a314-31cb-853d-89ebde1dd694 | -11.09159 | -44.78085 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 430ae46b-2bba-30d0-b431-524ae0351e84 | -10.59979 | -44.33717 | 2025-08-25 03:23:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 4d7e60c9-c48a-3164-abf3-b17e74871e3c | -20.01409 | -42.84768 | 2025-08-25 03:25:00 | NOAA-20 | SÃO DOMINGOS DO PRATA | MINAS GERAIS | Brasil | 3161007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ebbe5353-82df-349e-b961-cd3da1def412 | -20.98068 | -45.4882 | 2025-08-25 03:25:00 | NOAA-20 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 75d4cefe-e95f-35d6-9336-2b2dae554c90 | -20.04454 | -44.48132 | 2025-08-25 03:25:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ac41e85e-1635-32b2-9820-693f36be6833 | -20.51151 | -45.99398 | 2025-08-25 03:25:00 | NOAA-20 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a1c42641-0c75-37b4-a606-5ca3ff3afb0e | -17.84185 | -44.41839 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 15d5ca76-117a-33f5-8448-a981c8d6bbd3 | -20.61392 | -45.02425 | 2025-08-25 03:25:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| c3542872-0abe-38f7-9232-740900a05639 | -19.1728 | -44.51661 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ede3a6f-1d1a-3287-a62f-fd55e4b8a87c | -20.36221 | -46.76959 | 2025-08-25 03:25:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a4d3780-a477-3c0c-b872-dd8638628e4f | -20.43535 | -41.68845 | 2025-08-25 03:25:00 | NOAA-20 | IBITIRAMA | ESPÍRITO SANTO | Brasil | 3202553 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22c13839-c3ad-339b-a11f-35fc28a55334 | -21.59206 | -43.90623 | 2025-08-25 03:25:00 | NOAA-20 | SANTA RITA DE IBITIPOCA | MINAS GERAIS | Brasil | 3159407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 94f2d005-9ba0-3731-84e2-d321600f0979 | -20.61295 | -45.0285 | 2025-08-25 03:25:00 | NOAA-20 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 31757310-9b3e-3187-b9ec-3fd648f73c81 | -20.29537 | -47.18835 | 2025-08-25 03:25:00 | NOAA-20 | CLARAVAL | MINAS GERAIS | Brasil | 3116407 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1258dc48-34e9-340b-b100-a445bbd533b5 | -17.83601 | -44.41703 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1483d3f4-1f19-3ed9-a161-aba4b75031d0 | -19.81163 | -42.2058 | 2025-08-25 03:25:00 | NOAA-20 | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 400404bb-037a-35f9-a714-2475a7bbea6f | -19.92214 | -44.04338 | 2025-08-25 03:25:00 | NOAA-20 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d7178422-6ede-3c39-8f44-3e8856ffe088 | -17.80174 | -44.48893 | 2025-08-25 03:25:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4def047d-8de4-37ab-a6a7-d1f568b97726 | -20.45781 | -47.41381 | 2025-08-25 03:25:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e7a3933-2217-3db6-8868-e83882237393 | -14.65211 | -44.07504 | 2025-08-25 03:25:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 27e282f7-4d89-39bd-98d7-f2cfdab54eae | -21.2793 | -43.7877 | 2025-08-25 03:25:00 | NOAA-20 | BARBACENA | MINAS GERAIS | Brasil | 3105608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| c476bf22-7f8e-385a-9ffa-5a4e8dc9ebc9 | -20.90582 | -44.08047 | 2025-08-25 03:25:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 42d493b1-7a48-3716-9fc6-05afad8aabae | -18.3863 | -46.83685 | 2025-08-25 03:25:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1425a95-678a-36e4-8045-d5a19aaf17c5 | -20.90693 | -44.08 | 2025-08-25 03:25:00 | NOAA-20 | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5c9e8176-2e8c-304a-a700-c47115887d00 | -19.17795 | -44.52195 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| dfc5f8a2-6e2d-3be4-8c24-8da3677f1fac | -20.45388 | -47.41343 | 2025-08-25 03:25:00 | NOAA-20 | CRISTAIS PAULISTA | SÃO PAULO | Brasil | 3513207 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98d7dadb-044b-3fb2-b608-25138b51f193 | -19.17895 | -44.5175 | 2025-08-25 03:25:00 | NOAA-20 | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bc5a5ace-e240-364a-b1a4-216457b1812e | -19.9157 | -44.63191 | 2025-08-25 03:25:00 | NOAA-20 | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |


[Clique aqui para ver as próximas entradas](README19.md)
