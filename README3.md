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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae786c95-107b-3fe5-92a3-9a9528635f25 | -14.2123 | -45.46217 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3745f5d-3915-37dc-a882-c27571b19661 | -14.21095 | -45.46959 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ba4e88df-c383-3746-a4cb-a0c5fd68a25d | -14.22583 | -45.45703 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6d802064-aef6-379c-bb0e-e0c6415d84b9 | -11.19161 | -44.50821 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 89809949-ebc4-3ad5-8fe0-10f60011f43b | -11.00206 | -44.34346 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ed0c8561-9494-37f5-aabb-9fd29f95fe3b | -10.99381 | -44.44057 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c79b29a5-8fc5-399e-9923-1659c70884a8 | -10.99321 | -44.44414 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19767aed-63eb-3952-b83d-e3e7d22a9ff9 | -12.17953 | -44.34073 | 2025-05-06 03:55:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5b0fb0c1-c89d-3295-9e0d-230963e2967a | -14.24007 | -45.47119 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 52a4c9de-631a-380c-9889-d3dc5b2cffb2 | -10.9926 | -44.4477 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22c82914-fd3b-391f-a31b-0c27c70f8366 | -14.22988 | -45.4578 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8dc3eda7-a1e2-394b-af29-9882a6480bbe | -10.98178 | -44.43837 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b665dffa-3b6d-35b8-965c-efe15b13c922 | -14.23328 | -45.46226 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 01992f93-1f92-35ba-83ff-c799307df7e5 | -15.08138 | -48.94416 | 2025-05-06 03:55:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| efaea9d0-f7bd-3383-afeb-5143dda0d2c7 | -14.22922 | -45.46148 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56658c39-7daf-386d-b349-77c721a5cf92 | -15.08083 | -48.94695 | 2025-05-06 03:55:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5dc0019d-49e8-3267-a8c0-ebfd48cd43c5 | -10.99372 | -44.44804 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e436cf88-8c58-3d51-b1c9-57e9fd1713a5 | -14.22788 | -45.46888 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82e86d09-d10d-39b0-bf82-88bc3926708b | -10.60379 | -44.76485 | 2025-05-06 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ba7012dc-1507-3f86-8062-0f3ea376669f | -11.00266 | -44.33994 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc0337d0-a727-33d4-8962-a5531cd808ff | -12.8341 | -44.89111 | 2025-05-06 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bbe893c-5885-39dc-a03e-4fc73958f6d4 | -12.4909 | -45.50362 | 2025-05-06 03:55:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7cf1f84-f4d1-3a19-a41a-dfcb65068541 | -14.23055 | -45.45412 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ff6d50f1-08d9-3a76-b17c-123ecf474d54 | -14.20621 | -45.47257 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f4ac9fbc-dc6f-3ea3-96b4-e09213c20603 | -14.21703 | -45.45921 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 75f2f7eb-57af-3e42-aed3-62c130d5cb3b | -14.21975 | -45.46738 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fcea33b4-c796-379a-af05-973d6c22be33 | -10.6978 | -37.04946 | 2025-05-06 03:55:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1d4c1e48-8e36-3d50-9c88-0c9a120c5953 | -10.60576 | -44.76859 | 2025-05-06 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6da26c67-08d7-314e-8d59-1d547a9a5a5c | -15.51387 | -41.66959 | 2025-05-06 03:55:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 374d25eb-cb4b-36a5-821b-2c4055d52035 | -14.22449 | -45.46442 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6ef81b2e-7875-3156-a38c-6b0a74800c61 | -14.2096 | -45.47704 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 030ee792-dfc3-350a-8130-0acdc06da422 | -10.98299 | -44.43124 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 177e707c-3c4a-37a3-9cbe-97ce538b667e | -14.2211 | -45.45996 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7678434a-7fcb-3f4c-8459-560a6c83e2f5 | -10.97777 | -44.43764 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c2e4c97-d39d-393a-82c0-cd5db9b6e847 | -10.9898 | -44.43984 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 35a13075-6f26-3a9b-a65f-9c9fea556371 | -11.19563 | -44.50894 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 10008298-83ca-3323-a292-3f227c1e864a | -14.23394 | -45.45858 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 059a85fe-5f57-3fa5-a421-8dcc5ef12c55 | -14.24073 | -45.46751 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36568e97-ef7f-3cf0-ae22-13e3bc4085a9 | -14.21502 | -45.47034 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b38746f-a93b-3f9d-bb37-c07189f41cdf | -8.20318 | -48.9846 | 2025-05-06 03:55:00 | NOAA-21 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 30d12adc-4e24-34f8-b4fb-9352a6fbe72c | -14.22177 | -45.45626 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a040255-2f10-3a9f-bc2d-87eb05e5f84f | -10.99435 | -44.44449 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53e2fdfb-5309-378c-aaf7-a6897d9956f3 | -10.97716 | -44.4412 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c386ca9f-a023-31f3-bf59-43f1f3cf6642 | -14.21162 | -45.46588 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63501d94-32da-35e4-ad17-f42f4b55fc39 | -13.66702 | -43.79176 | 2025-05-06 03:55:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1954cd26-1f92-3702-a127-8669592ab399 | -14.23601 | -45.47041 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 54f02beb-9245-3b80-b5cc-41781c1c3600 | -11.96946 | -44.15578 | 2025-05-06 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bee89b9e-5bab-37e1-8653-62f71ceac35b | -14.21367 | -45.47778 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| faa580f9-9007-3c16-8af8-f0b592dd46de | -13.06447 | -47.58475 | 2025-05-06 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| cf6f6ebd-03d4-3b24-8a10-050fea3be380 | -14.21636 | -45.46292 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| db37aa6d-993d-3696-a63e-5e4fb4ba17dd | -14.21569 | -45.46663 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d7b2b23d-499b-3372-8c56-c01d951c6d9e | -14.22516 | -45.46072 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d3f67fb4-f735-3fb3-8a3e-bbc102c12ccb | -10.99498 | -44.44093 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4af80288-e7a9-3c7e-a721-dfcf3ac3cbc6 | -14.23261 | -45.46594 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 88bdc7e2-9b58-39a4-92ad-ec06a9909b34 | -14.22855 | -45.46518 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3339dc7d-9061-3377-916f-9ef83da54c67 | -14.21297 | -45.45846 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6f3058ac-eeaf-39e2-b4ef-a0ce230cf9f7 | -14.22043 | -45.46366 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5094e539-0661-3433-a46c-629a262ea2a9 | -14.23667 | -45.46672 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3b747ec3-14a1-332f-9ff1-8a45e03b4160 | -12.9469 | -47.97842 | 2025-05-06 03:55:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c940d7a6-0d33-36f0-95c4-e7fb18fdf514 | -10.99041 | -44.43627 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2644c107-9d0e-390e-8fc3-7a25d5259ea2 | -10.98239 | -44.4348 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cb9019b6-383b-39ee-a3d2-4e25789b4bc6 | -10.97898 | -44.43052 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f9db38e5-89f4-305d-9b7b-175e16db4168 | -10.97837 | -44.43408 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 08554eaf-192e-391a-a293-cd8c25ea6786 | -10.98117 | -44.44193 | 2025-05-06 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 448aaf94-cd9f-30ca-b6ae-7b9fd9a66619 | -14.21434 | -45.47406 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 882ab927-47cb-3db2-8dbe-df4069bd1c8e | -10.60643 | -44.76481 | 2025-05-06 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39038772-b369-3e6e-9619-d76383a2bc19 | -10.60727 | -44.76936 | 2025-05-06 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 657de8ad-1718-39f1-b623-d514e70d237a | -15.59897 | -41.79431 | 2025-05-06 03:55:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 93e61b19-ffc4-3ee7-b7f2-0b2294739d13 | -14.21027 | -45.47331 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4e6175b1-b8ea-3b1f-88ae-f28614615329 | -15.51722 | -41.67014 | 2025-05-06 03:55:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 60171b2e-23b8-3ee3-ac61-d471c400e80d | -14.23534 | -45.47411 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5e2d4b19-05a5-3273-be61-b5b2b35b9f5d | -14.23733 | -45.46304 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e4598492-8373-3959-8bcd-6335d9b55be7 | -12.17866 | -44.34577 | 2025-05-06 03:55:00 | NOAA-21 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91c251f6-dd33-35ef-8bed-0e4c8262d440 | -10.60792 | -44.76556 | 2025-05-06 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f99cce74-9a9e-3375-8815-87cf2ddded9e | -14.21841 | -45.4748 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd6944e0-74d4-3a77-ae76-b80f11a460ea | -14.23128 | -45.47335 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b642d846-cc4a-386d-ac41-01341c2def55 | -14.23195 | -45.46964 | 2025-05-06 03:55:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 66b164f7-5a6e-3a55-ba83-200f6ea59551 | -17.77735 | -42.80513 | 2025-05-06 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67e3ebfc-93df-346e-b2a4-9a69c3bd0d7b | -18.60381 | -46.99574 | 2025-05-06 03:57:00 | NOAA-21 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 075d7fa1-6198-38c6-bd38-6fd00336a169 | -21.17991 | -43.97898 | 2025-05-06 03:57:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4591d902-2e2a-33ab-b81a-07c3967b063c | -17.59559 | -43.19861 | 2025-05-06 03:57:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 36da513d-6983-3dc3-82bf-1b8ca094f3fb | -21.36471 | -48.62493 | 2025-05-06 03:57:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| edc069cc-ef2d-342c-8d9b-afe3ce04c407 | -16.35757 | -49.33319 | 2025-05-06 03:57:00 | NOAA-21 | NOVA VENEZA | GOIÁS | Brasil | 5215009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cb8102b-568f-3825-bb16-fa96522f1c00 | -15.83098 | -46.57795 | 2025-05-06 03:57:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 65353c21-ae00-328b-beab-c7c560a4acba | -22.90929 | -49.69009 | 2025-05-06 03:57:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| a76abb50-3747-33fe-aff3-1158e965d540 | -18.50065 | -47.59831 | 2025-05-06 03:57:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 55bf4e97-e3b1-360c-93b9-f638d4c1f6ef | -23.33988 | -46.77292 | 2025-05-06 03:57:00 | NOAA-21 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b7e16e98-5137-315a-b8ad-3f77fa4c9cd7 | -16.93379 | -44.8073 | 2025-05-06 03:57:00 | NOAA-21 | IBIAÍ | MINAS GERAIS | Brasil | 3129608 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf9f8155-4c78-3072-a164-1b8760ba3e22 | -20.06324 | -49.37285 | 2025-05-06 03:57:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| ca86a5da-b47a-3f2b-b915-018f9009e7e8 | -22.03996 | -47.93678 | 2025-05-06 03:57:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0ea3436a-ad16-3230-8d17-a236f6bdaab7 | -20.05963 | -49.36646 | 2025-05-06 03:57:00 | NOAA-21 | PAULO DE FARIA | SÃO PAULO | Brasil | 3536604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| a01c3b2b-ca63-39d0-a5af-62c82260f4bd | -21.82453 | -53.61256 | 2025-05-06 03:57:00 | NOAA-21 | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9c171898-7245-3884-b5f5-82ad81e2b37b | -17.67886 | -42.74093 | 2025-05-06 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18179926-2c9a-343b-bbc3-b52a04d81c3b | -20.16065 | -41.66686 | 2025-05-06 03:57:00 | NOAA-21 | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 78fb7435-b6f7-3183-b6ed-2cea284b7ba0 | -22.04077 | -47.93272 | 2025-05-06 03:57:00 | NOAA-21 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a0c3820f-5dee-3b67-a862-a69d3040c02f | -19.56888 | -49.68262 | 2025-05-06 03:57:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| c1186c59-cb7d-3a79-9dc7-68ffefd3e4cd | -21.36379 | -48.6295 | 2025-05-06 03:57:00 | NOAA-21 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 9e86f7db-18e2-3b0d-a583-d886cba91312 | -22.90336 | -43.75731 | 2025-05-06 03:57:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 7997c792-9bbb-342c-8726-0af4d702b76c | -20.76589 | -46.76923 | 2025-05-06 03:57:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 85368046-2668-3474-90c6-cafb26f67c09 | -17.78011 | -42.80959 | 2025-05-06 03:57:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README4.md)
