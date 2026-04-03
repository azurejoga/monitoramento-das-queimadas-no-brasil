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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c9228d5-f5dd-389c-95b0-1a68978d8f15 | -20.915899 | -49.511501 | 2026-04-03 00:07:00 | METOP-B | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9928c81b-876a-3415-ac97-69a4199be0e0 | -19.391001 | -43.570801 | 2026-04-03 00:07:00 | METOP-B | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 88168f21-30b3-3ad4-88b8-09626631c15b | -21.71219 | -48.43013 | 2026-04-03 00:18:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 13493256-9531-349c-bfda-214ab7d0855a | -20.91569 | -49.5238 | 2026-04-03 00:18:00 | TERRA_M-M | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| b136aa1f-864f-349f-a255-b7d8787305f8 | -22.1829 | -56.97135 | 2026-04-03 00:18:00 | TERRA_M-M | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 27.4 |
| c87aa1a0-1d2a-3c48-9c65-89716f92b8ac | -20.91704 | -49.53451 | 2026-04-03 00:18:00 | TERRA_M-M | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.9 |
| 9c41845f-64b6-3946-a934-213c3365dd14 | -19.38421 | -43.58572 | 2026-04-03 00:18:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 909a36d8-0b3f-3ad2-9b76-ed421efccda9 | -19.39455 | -43.58405 | 2026-04-03 00:18:00 | TERRA_M-M | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 03e0f280-2cc6-329e-8fa3-51d8f1aa4c51 | -20.28548 | -50.4371 | 2026-04-03 00:18:00 | TERRA_M-M | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.5 |
| 5fc37f31-d5d9-3394-b145-181f25d89f79 | 1.30084 | -60.65317 | 2026-04-03 00:24:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 7e992342-5a0a-3e3d-a91c-4d6b07dffae6 | -19.389799 | -43.579399 | 2026-04-03 00:40:00 | METOP-C | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bcda84ea-dd38-352a-afab-cd9515260628 | -7.21509 | -34.90659 | 2026-04-03 03:30:00 | NOAA-21 | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| ca093136-f78d-36bf-b55c-ac542d096683 | -7.74586 | -35.42727 | 2026-04-03 03:30:00 | NOAA-21 | LIMOEIRO | PERNAMBUCO | Brasil | 2608909 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bffadadf-f16c-36d3-bc7a-9d16f3d77d14 | -19.38849 | -43.58552 | 2026-04-03 03:34:00 | NOAA-21 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a89b994b-be4c-30f6-85a8-fbfd5f844acd | -22.08137 | -43.17629 | 2026-04-03 03:34:00 | NOAA-21 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 495c25e7-ba52-31d8-a658-8bda00038001 | -19.598 | -40.06968 | 2026-04-03 03:34:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bd82a1fe-d79c-32f7-87a4-1ae9d52fcba1 | -30.40217 | -54.26269 | 2026-04-03 03:38:00 | NOAA-21 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 4.5 |
| a494a272-1be3-3f4b-b257-6538c4818b81 | -30.40539 | -54.26476 | 2026-04-03 03:38:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 4.1 |
| eb52c6b4-b945-312e-8cb4-7e5438fa09ac | -7.21375 | -34.90664 | 2026-04-03 04:02:00 | NPP-375D | CONDE | PARAÍBA | Brasil | 2504603 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 708772cf-e3f6-322e-a5aa-86a58702c675 | -12.05186 | -45.22132 | 2026-04-03 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ee0a66c-3c97-3a43-8e91-d41406d24258 | -12.05118 | -45.22513 | 2026-04-03 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 52a66ecf-306c-3449-8f8e-56d8ff7d32ba | -12.03806 | -45.22664 | 2026-04-03 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f989e2ec-6c99-3f26-a6b6-786d765cdd52 | -12.0422 | -45.22741 | 2026-04-03 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ec80f64f-6b62-34ae-bad4-e0b918d809b6 | -12.04289 | -45.22359 | 2026-04-03 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39b750be-8683-318a-ba22-cb57ad8976d2 | -15.76902 | -43.237 | 2026-04-03 04:04:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 83754897-3cda-3858-babc-fb2ed763d1e7 | -12.04703 | -45.22436 | 2026-04-03 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0e50368-0916-3850-ad6e-3fbb2eb4c9fb | -21.71134 | -48.42638 | 2026-04-03 04:06:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2732b4a8-a4d4-30d0-bc98-f61a09dbbe00 | -23.03494 | -52.68274 | 2026-04-03 04:06:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 269dd5cf-a953-30ac-8bc5-0c1511a6db30 | -19.38208 | -43.57885 | 2026-04-03 04:06:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 689d5a21-b4e6-3bc3-97a9-10c9f78aa685 | -23.02865 | -52.68522 | 2026-04-03 04:06:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| d22e4455-9693-3b7b-81ec-27e223966a93 | -21.70854 | -48.42453 | 2026-04-03 04:06:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fcc1d71c-3a01-354f-a618-fb734a4fcc27 | -20.28166 | -50.44161 | 2026-04-03 04:06:00 | NPP-375D | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| d0f31e86-76ec-3148-b83c-ec2fb85b6e56 | -23.02955 | -52.68129 | 2026-04-03 04:06:00 | NPP-375D | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| 503e2fef-b2da-319f-b7c8-a8000c12ad85 | -21.71279 | -48.42563 | 2026-04-03 04:06:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c396d044-34e5-3ce1-9a31-8e194f514ca2 | -29.746 | -51.1978 | 2026-04-03 04:08:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| 3e451202-32f5-3808-b24a-b4b15b6ffa9b | -22.18593 | -56.96962 | 2026-04-03 04:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5cc94499-ad1d-30be-b4ff-61832d4abe15 | -29.71863 | -50.68082 | 2026-04-03 04:08:00 | NPP-375D | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| af5137e5-7cbd-3787-8649-099bf398f1dc | -29.71353 | -50.68407 | 2026-04-03 04:08:00 | NPP-375D | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 66502cb0-da77-3fba-ab41-450e5c232375 | -22.18314 | -56.96658 | 2026-04-03 04:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e49bfc3d-0d6a-3db2-9b7d-9cfdbeee5182 | -22.18411 | -56.97681 | 2026-04-03 04:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7daf0222-37c8-3980-9378-41edaf45cca1 | -22.18133 | -56.97356 | 2026-04-03 04:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c73f86c6-f62f-3e51-bf96-6897f3c25732 | -22.17733 | -56.97419 | 2026-04-03 04:08:00 | NPP-375D | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a3bce4d-80d0-30e3-8cbe-b33ef2d7bcb4 | -30.40479 | -54.26315 | 2026-04-03 04:08:00 | NPP-375D | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 62977901-0734-3875-be44-b17e9951e194 | -31.04624 | -53.06815 | 2026-04-03 04:10:00 | NPP-375D | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| cb943cf0-6b1a-34e6-9fef-ea8c09bee822 | -12.05134 | -45.22033 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 315b9941-2528-3671-a1a0-0e86071d7426 | -9.45702 | -59.19482 | 2026-04-03 04:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9c0bcd9-62f2-32d1-9127-34b90be5a7ac | -9.45835 | -59.19675 | 2026-04-03 04:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8d7dfc56-b1d1-35cf-a605-d81480c50cb3 | -12.04078 | -45.22613 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5007bc1-0c1e-3b47-a6f6-e46b23dd0eb0 | -12.04746 | -45.22336 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44d55f3c-d371-33f0-91d5-c73a3e315c00 | -9.45565 | -59.20158 | 2026-04-03 04:23:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 90692a65-d556-3484-a3f1-9581c501d851 | -12.05079 | -45.22389 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 452bd87d-e51f-3a15-bb4a-8ad4a64c3365 | -12.04133 | -45.22258 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ddb34c14-2a24-325a-8a29-689ccc6aa329 | -12.04358 | -45.22638 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 45167285-62f6-37ce-b958-dddf5cfcf286 | -12.03745 | -45.2256 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f9a2d396-44e6-3813-992a-8392ae05f1c8 | -12.63606 | -52.14351 | 2026-04-03 04:23:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed3515c3-66d0-3160-8648-9bcb4bc5bc77 | -12.03412 | -45.22507 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f2fd926-9aa8-3934-961e-56d7e968c86a | -12.03357 | -45.22862 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 299494a7-15ac-3933-b0ff-4dbe1a1ad558 | -15.7684 | -43.2377 | 2026-04-03 04:23:00 | NOAA-20 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7c6733f9-7fda-340b-ae56-44645ad97cb7 | -12.04413 | -45.22282 | 2026-04-03 04:23:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa34197e-a683-3257-bb3b-ea13e3bce00e | -20.91546 | -49.52571 | 2026-04-03 04:25:00 | NOAA-20 | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 3a41a5ba-687c-33aa-9262-ade5620e6c78 | -20.759 | -49.33264 | 2026-04-03 04:25:00 | NOAA-20 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| dcdafbfc-ac0b-3fb9-b01a-50381a9b86a7 | -20.28364 | -50.44092 | 2026-04-03 04:25:00 | NOAA-20 | ESTRELA D'OESTE | SÃO PAULO | Brasil | 3515202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7a2bca71-566e-3c63-b07b-e445c65530bb | -21.71165 | -48.4278 | 2026-04-03 04:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| be64d3b0-47ff-38a4-89a3-71e10b5464a7 | -22.08093 | -43.17537 | 2026-04-03 04:25:00 | NOAA-20 | TRÊS RIOS | RIO DE JANEIRO | Brasil | 3306008 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6ffb611-01a8-3a10-9987-858ee488e0c9 | -21.70893 | -48.42349 | 2026-04-03 04:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f2b7ced2-2486-3545-a541-fb5d45758f10 | -21.70834 | -48.4272 | 2026-04-03 04:25:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e9c6725c-6bf3-3bfe-9325-d62d5c8834b5 | -21.66843 | -56.32281 | 2026-04-03 04:25:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41302de6-ec35-31b7-aa6e-f868c1f9ce7d | -21.20495 | -55.64404 | 2026-04-03 04:25:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65ac2cc4-1c69-33f0-842f-b13faaacc5fc | -23.776 | -55.3249 | 2026-04-03 04:27:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 80947658-7686-3db6-aa02-e0c1751dc834 | -30.40562 | -54.26047 | 2026-04-03 04:27:00 | NOAA-20 | SANTA MARGARIDA DO SUL | RIO GRANDE DO SUL | Brasil | 4316972 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| 8be2ccda-1b0a-3ca6-b555-ede81f2de3da | -23.02998 | -52.68227 | 2026-04-03 04:27:00 | NOAA-20 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 32b807bd-15d4-3237-b9b7-625c2403ca12 | -23.77684 | -55.32061 | 2026-04-03 04:27:00 | NOAA-20 | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 59d32d9b-ee5c-36ff-b0a1-7ba2b20e270e | -30.40473 | -54.26526 | 2026-04-03 04:27:00 | NOAA-20 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 2.9 |
| ba6ac815-e6a0-306e-807d-643202425ed7 | -26.66832 | -52.01869 | 2026-04-03 04:27:00 | NOAA-20 | PASSOS MAIA | SANTA CATARINA | Brasil | 4212270 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9397037d-0432-3c6e-81b6-bfcb03201ba1 | -30.05776 | -50.85555 | 2026-04-03 04:27:00 | NOAA-20 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| 78c57378-15d2-3b9c-bc23-d93425f3005e | -26.06045 | -48.62163 | 2026-04-03 04:27:00 | NOAA-20 | ITAPOÁ | SANTA CATARINA | Brasil | 4208450 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f6d677b2-05bc-357c-9ce6-655ead142a6b | -29.74666 | -51.19966 | 2026-04-03 04:27:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.5 |
| 62661dac-9baf-3afa-bb19-8504189c96be | -29.71824 | -50.68037 | 2026-04-03 04:27:00 | NOAA-20 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 173deafb-d511-31eb-9586-452fdfdff09f | -22.18321 | -56.96978 | 2026-04-03 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 88e4712d-9465-3132-989a-b72fa180f367 | -30.13028 | -51.96011 | 2026-04-03 04:27:00 | NOAA-20 | BUTIÁ | RIO GRANDE DO SUL | Brasil | 4302709 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 8150a7b9-7eba-3872-9fc1-6308d21bf0a5 | -22.17843 | -56.96841 | 2026-04-03 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8a9c1502-b1ba-3cd7-8270-80a924ceeb75 | -29.71429 | -50.68364 | 2026-04-03 04:27:00 | NOAA-20 | SANTO ANTÔNIO DA PATRULHA | RIO GRANDE DO SUL | Brasil | 4317608 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fdd35baa-c99c-33f6-8fcf-a7a386192ea7 | -22.1844 | -56.96416 | 2026-04-03 04:27:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 77945ade-96a8-36d2-b205-f9adca85fe58 | -31.04816 | -53.06704 | 2026-04-03 04:29:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 1.2 |
| 3860dd28-9a3e-3009-a324-f6a9574a518b | -31.04741 | -53.0713 | 2026-04-03 04:29:00 | NOAA-20 | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 3af86812-6191-3922-83b1-de02521702c9 | 2.82385 | -60.21107 | 2026-04-03 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37b66c56-e743-33a6-ae62-9665d869d636 | -3.0209 | -53.97018 | 2026-04-03 05:10:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 302ceba6-e6b9-37c5-8c90-df928ab3e1a3 | -9.46217 | -59.19424 | 2026-04-03 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.8 |
| ba42d960-2afa-3fce-a051-dfbaece45a68 | -9.11902 | -61.48932 | 2026-04-03 05:12:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| df129d95-ac1f-3fa6-8c21-df4a4d5bfe20 | -23.0298 | -52.67815 | 2026-04-03 05:16:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 31b335ae-4a19-383d-82f6-9f5a89fe62e0 | -22.18465 | -56.97189 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 026839d4-7068-3504-ad4b-15bbd12ad2d4 | -21.672 | -56.32031 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8757595-f95b-3491-8af2-839e783f7a7f | -22.18152 | -56.96654 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c498bea3-854c-38a2-832a-c772acff0f80 | -22.1809 | -56.9714 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce735a0c-cf3f-3e3d-81b8-04ccb2ef4e44 | -21.66427 | -56.31926 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| feabd854-5918-3b83-af76-d9d522aebd7a | -22.18528 | -56.96703 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| a29203b4-f202-3839-9f6a-a005a5c348ff | -23.02922 | -52.68393 | 2026-04-03 05:16:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 0f1e4a95-aa5b-3598-9e93-62a31122fc17 | -21.66748 | -56.32488 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 50c50447-23d4-3dfc-93f2-169ee21a9e6e | -21.66814 | -56.31977 | 2026-04-03 05:16:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9b2b6c13-4784-3e81-b59c-269fde04d765 | -23.03416 | -52.68458 | 2026-04-03 05:16:00 | NOAA-21 | PARANAVAÍ | PARANÁ | Brasil | 4118402 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |


[Clique aqui para ver as próximas entradas](README2.md)
