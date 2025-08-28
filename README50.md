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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ddcd2be6-4852-3bfa-8bde-64b033d05c81 | -4.08542 | -48.04297 | 2025-08-28 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b3ba624d-1aa3-3487-afbb-25aa3c9b11b7 | -7.16012 | -45.156 | 2025-08-28 04:57:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2d7f5a7-8f3e-3ea5-a13e-641e8ca7c377 | -9.67616 | -48.29958 | 2025-08-28 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 5d80ac69-5f0d-3029-a66c-38c803dd3a6e | -8.28578 | -45.1891 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| e52408c6-eb89-3fa3-bbdd-ab4ddbed97c5 | -6.18156 | -44.06644 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86d7b406-7922-365c-bf6e-c5ea99d1b624 | -5.81476 | -44.76646 | 2025-08-28 04:57:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f5620fab-e1a4-3c0c-bc55-44efedbbe352 | -7.48869 | -45.04615 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bae5decd-0f6f-3873-9f60-ce764d29f685 | -6.86201 | -43.62713 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5cba552a-c7ca-360b-a62b-34663a20d706 | -6.86315 | -43.61843 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 32698fa5-f3e2-3d35-b05c-2db583ae7410 | -6.87793 | -43.59863 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0cabdf58-3d95-38c0-94ad-d894771631bc | -6.16554 | -44.05502 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 35a12fa0-9bbc-34b8-9d6e-eb88af82324a | -7.55855 | -63.84158 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d39cd72-4740-3819-b5f1-9360142155d8 | -9.45984 | -51.94546 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 19ec1219-7332-34d5-b063-1e7e66044330 | -2.74293 | -48.56367 | 2025-08-28 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e499ba6-f5aa-3c85-ba00-4094f383f649 | -2.92784 | -53.69319 | 2025-08-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47c3e10c-d5fa-3aa3-80bb-f5168922412f | -6.86259 | -43.62276 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 535c09d9-6df0-3142-8384-f17633f4f0c0 | -4.96007 | -55.81717 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fffb9336-a392-3ce6-a6c5-2ac75bc32dc8 | -6.65614 | -53.18665 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d2d51a2-866b-3bc9-96d7-8900977d8a6c | -4.48865 | -55.55618 | 2025-08-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 988d86f1-d70e-34be-80ec-3124d07ead5c | -4.55798 | -55.95895 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfcc40f9-30c0-3659-9016-7e616f144af3 | -4.80316 | -47.25922 | 2025-08-28 04:57:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 328f5636-b87e-3c5f-8d3d-13713c78be3d | -3.23587 | -43.44439 | 2025-08-28 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5e1269a-b833-3d90-ab6b-44d95eab6a29 | -8.27122 | -45.17211 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| b57343fd-5dbe-3bda-9dca-9edce6f0500f | -9.19462 | -44.43633 | 2025-08-28 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c96bb6a-f0b2-396c-9ce2-72955af32a0e | -5.3218 | -55.88163 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 03db9e1e-09a9-35fe-9a21-5eebdb97a9fd | -5.50309 | -60.98362 | 2025-08-28 04:57:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a157276-dcf2-328b-aecd-c98e7bebaca1 | -8.28514 | -45.1513 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ebbe0c82-0df2-307b-8c9d-1f3e8e279877 | -2.83216 | -54.56372 | 2025-08-28 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9f0bae95-6118-355c-8b7e-a5f7b4411134 | -5.19311 | -46.0686 | 2025-08-28 04:57:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1b822320-140f-314e-b0cb-00ff86490424 | -8.56047 | -51.31774 | 2025-08-28 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ffc3326-ebd2-3fa5-acaa-edda956079b7 | -9.0076 | -48.72504 | 2025-08-28 04:57:00 | NOAA-21 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8289eed5-e90c-3ac8-b4fb-31899eb6c155 | -6.57648 | -47.38366 | 2025-08-28 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abeff4a2-aef1-35f8-bf4c-5fabcdfe3f3d | -6.57254 | -47.37826 | 2025-08-28 04:57:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| f46302bd-aea4-3d9f-8f37-cf5b7c63d1b5 | -7.40053 | -64.34237 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 713a8f7e-4cb7-3916-aa1b-236aab811032 | -7.75987 | -51.08955 | 2025-08-28 04:57:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 49292d86-1298-3d3d-b734-2badae49243d | -6.86853 | -43.62376 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 585068ae-b421-3a87-82c7-18bf61f5c89d | -3.98684 | -47.88698 | 2025-08-28 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b12f10a-1cc3-3a43-9622-df1a794ef1b7 | -6.00382 | -57.85223 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8a87c66-bc40-3825-9e6d-71df6407914e | -6.18299 | -44.01266 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bd0ad3e9-b44a-3cde-bca8-04b0064e2f27 | -3.31808 | -52.76152 | 2025-08-28 04:57:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b277147-664b-3cfc-92bc-68a8414f5fb0 | -6.91464 | -62.9375 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e260d8ea-abb0-37ef-8401-871611384208 | -3.76135 | -54.82106 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 162a2502-72bb-3b2d-8048-636667c74491 | -6.91089 | -62.93579 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ef149764-f64e-3f56-ba37-df1b44ee857f | -3.98108 | -51.05661 | 2025-08-28 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ace57ab7-5943-389c-9f11-3c557859725a | -8.28674 | -45.18178 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 22d6d6f8-915c-3e41-916d-aa0ea70b71c2 | -6.28398 | -44.47565 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1de1c77a-20b9-3c16-9df9-0ecd329360e0 | -5.64831 | -45.2583 | 2025-08-28 04:57:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00b14095-6ed6-370a-88ed-744f407f9cc9 | -6.87619 | -43.61179 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 2f622f8a-57f1-379d-86f4-b61a31d5a1c7 | -6.43223 | -44.57921 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| dd69aa1a-88a1-3132-af56-31bba0a2f181 | -8.70696 | -50.38367 | 2025-08-28 04:57:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1e274db5-a1d0-3161-add4-7d4965377135 | -6.88157 | -43.6171 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 51197155-db9e-3a2f-bd56-1b7976e0d7de | -7.34834 | -57.63413 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbc31adb-34aa-31b5-8eaf-7deac7a47f39 | -8.83815 | -47.92096 | 2025-08-28 04:57:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| db2f8a94-f961-3186-b03b-2d979201ac63 | -7.26269 | -57.66269 | 2025-08-28 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfa3f615-e811-3bc2-8abb-cf0bff89ec34 | -6.17587 | -44.06524 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 581b5bca-7399-374b-b399-b31f84154bb0 | -6.92371 | -62.94517 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed71a5ef-735a-3496-8bbd-005b5f8dce17 | -8.28076 | -45.1847 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 65.7 |
| 58547937-6f47-3a14-8607-e4ff81e9eb99 | -4.88076 | -44.95794 | 2025-08-28 04:57:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edb69d6e-91d8-3822-a0bc-e2171dfc4967 | -6.94899 | -44.08869 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 960a6897-2d18-387a-bde8-d4fb24f1ada8 | -3.79013 | -45.04248 | 2025-08-28 04:57:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fce4799c-af78-3063-89a1-4981f9a9e66e | -7.37339 | -64.36768 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f6251329-0dbc-364c-9e98-72d87090a25c | -7.542 | -63.84209 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4127dd55-455e-3d6b-bed9-72c948814b36 | -7.28592 | -49.26071 | 2025-08-28 04:57:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3e45bdf4-0f6f-3e25-a5cc-fb182d23b9cf | -6.71147 | -43.15097 | 2025-08-28 04:57:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8cc52aad-6f57-3938-b319-2af2662d1953 | -3.24048 | -50.80703 | 2025-08-28 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aecec91e-be33-3fe0-af95-354d6bfd1974 | -7.1891 | -44.0662 | 2025-08-28 04:57:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 64aa4370-453d-3051-8eba-8a3bb4bfefba | -6.86429 | -43.6098 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cd814fb6-4dd0-31b7-a996-2884543b31ad | -3.23645 | -43.44033 | 2025-08-28 04:57:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 8956f3de-413c-316b-bc48-5e599aa2d119 | -4.96066 | -55.81351 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c94dab6-231d-3ae5-a963-8c38a055462e | -8.23874 | -45.07785 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 0c074d8b-dae1-3865-95b9-ba94daa3f969 | -6.88696 | -43.62229 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2becd7fc-b192-338f-aaec-07fe816e3c0d | -6.75564 | -54.99126 | 2025-08-28 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a18738b-56c4-37d3-8a68-703ce1610449 | -6.15358 | -44.18679 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05ca8e11-e44a-36b7-8061-cda319e460e4 | -6.17901 | -44.17075 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7cd0dc9c-27bc-378f-8bdd-6aa2695586d7 | -7.06725 | -44.36388 | 2025-08-28 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6286d80f-5969-31a3-b1f6-65b600f30d0e | -3.7658 | -54.8145 | 2025-08-28 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 268e97a9-0961-3e18-8984-9da25f056fc4 | -4.13003 | -54.89767 | 2025-08-28 04:57:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b0d0dc6-9eca-3d93-8b3a-5d6b053fef21 | -9.67954 | -47.06942 | 2025-08-28 04:57:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 53c8a3fe-580c-38a3-b8ab-1921768bf786 | -8.08281 | -44.97915 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7332ac65-391e-3907-8b80-401ebb114ee1 | -6.15412 | -44.1828 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b4b6a168-2c10-3c07-bb1d-54896a0a7274 | -8.20014 | -45.07175 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8bc4565-183d-38da-9b26-8c913be58ebd | -5.32237 | -55.87799 | 2025-08-28 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 05808059-3835-3ba6-b3ae-1c45acf806eb | -6.94853 | -60.07875 | 2025-08-28 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 062308e0-2539-39ce-8349-1e2392b812c1 | -3.75678 | -49.05307 | 2025-08-28 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e5371a6-63a8-33c5-87e0-c9db03b34dcb | -7.81099 | -55.22446 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 15748e9b-5a64-3477-9789-f2048bc730a7 | -6.8572 | -43.61747 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 001f3ce8-c8d3-3856-8b6d-971581bb0b8a | -6.86372 | -43.61412 | 2025-08-28 04:57:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fa1f240a-c0a1-3cdf-a9a1-599fec1dcb82 | -6.90506 | -62.93279 | 2025-08-28 04:57:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc732614-e51c-3f16-b86c-10a3103329b0 | -8.51619 | -55.26257 | 2025-08-28 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bafaedbd-210f-34c3-b726-e15ba1e9d59f | -8.28369 | -45.16238 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 94a5fc11-b6de-3398-a6e9-5354ed03ef6c | -7.06152 | -44.36326 | 2025-08-28 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f11dfaf9-7931-340b-8e5a-7a258c67fae7 | -9.45422 | -51.94632 | 2025-08-28 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| c4faac40-e6ab-348c-9d75-7efe8807ea3e | -7.56559 | -63.8636 | 2025-08-28 04:57:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b5a56dd5-f5ff-35e9-966e-b8086b732303 | -6.17843 | -44.17498 | 2025-08-28 04:57:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c5310e13-22f6-33ab-9dcd-4b275f1d17d6 | -6.2274 | -43.3643 | 2025-08-28 04:57:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 15eff6f0-0183-3869-b932-cbe0ab0b2473 | -8.29064 | -45.15208 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e1a346a9-af6f-3c4b-be20-54d8e09e0548 | -8.2777 | -45.16533 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 876622c9-d532-3c40-8b99-455aaccec440 | -8.28417 | -45.15866 | 2025-08-28 04:57:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| dac69198-05ba-37a2-b3ff-c7f3df482f01 | -3.48326 | -51.18893 | 2025-08-28 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc0068f1-2e90-3de5-aa81-0f45c8a6fcac | -6.43776 | -44.58033 | 2025-08-28 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |


[Clique aqui para ver as próximas entradas](README51.md)
