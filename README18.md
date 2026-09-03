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
| 705aea30-2b76-334c-a79c-db2887bc5223 | -9.6108 | -40.34913 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 26cf619e-409b-371a-8156-6a132928f10f | -7.24225 | -42.76986 | 2026-09-03 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 281e0164-fac5-34b7-822a-be125d356c3a | -7.23938 | -42.76542 | 2026-09-03 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a7023aaf-e853-3479-b9ea-69e602dc90c0 | -7.23651 | -42.76098 | 2026-09-03 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6e6b8133-a64b-3d79-8300-b4599dddf8a3 | -9.60456 | -40.34458 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.7 |
| d3451686-690d-38ac-98dd-d4b4ab8c966b | -4.50074 | -42.56181 | 2026-09-03 04:02:00 | NOAA-21 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3097036b-12f9-39f9-a5f0-4289ade0ac5e | -10.01675 | -42.37201 | 2026-09-03 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c748eb89-7c67-3bd3-8fa5-b528458cc7f3 | -9.60402 | -40.34808 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 0b30973e-7a82-3a75-95db-0746bae673a1 | -8.0757 | -50.98301 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8508b8d3-15e8-3aac-8f43-694d6f240d06 | -8.07794 | -50.97081 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 2360f773-5174-3da8-881e-b2175b0ccfc6 | -3.81841 | -50.11056 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b0f9145-52a5-38af-9d9a-5fee657fd6e8 | -10.89304 | -45.32326 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3708a683-f7d6-375d-b8fa-94075765d423 | -6.03158 | -44.43925 | 2026-09-03 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e547b70-8220-3cdf-9ac8-16baa3dbb2ba | -8.40588 | -45.71124 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eac78142-51e3-382b-b43d-2e93c78bb57d | -9.64667 | -44.82997 | 2026-09-03 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a362a50-4735-380b-8734-7a58026d884b | -3.03754 | -48.41674 | 2026-09-03 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 726fd937-a7ce-3dec-ad0e-f46320e3d744 | -7.40951 | -49.74143 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8c060a8-7896-3d42-a9c6-f5382cbc3508 | -3.93007 | -49.05386 | 2026-09-03 04:02:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfbf56ba-4a9b-38d1-9252-4152c1158df1 | -9.60683 | -48.56395 | 2026-09-03 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0cc0a2d3-cffd-3016-87b5-69606afccbff | -6.6541 | -46.13834 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3bd43e7-2c4b-3507-86e8-b2335346f8e8 | -10.77773 | -44.74512 | 2026-09-03 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e9a5a35a-6513-3e59-aefb-0b4995775a02 | -6.75931 | -44.56995 | 2026-09-03 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 07d1e768-4465-3e96-9730-7656608fcbbf | -10.90065 | -45.3246 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02ade8d9-c130-3805-9887-48d2cc28663e | -10.88406 | -45.30713 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d97672a9-3908-3f0b-9711-47429f79fe38 | -8.0772 | -50.97485 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| f4062c0b-b1f3-3a63-946a-62fbecd4b651 | -2.70909 | -49.50524 | 2026-09-03 04:02:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8cf796e5-cdbf-3f8e-86e0-85b09e76419d | -8.42993 | -46.89459 | 2026-09-03 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7dba5eeb-7b40-3d0d-83ff-15965c9ee057 | -8.07645 | -50.9789 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 92266871-c2be-39c7-9d14-dff6987fda68 | -9.61411 | -40.34966 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| e02ed001-2163-311a-ba57-6cfad1f5cf5b | -7.7337 | -49.59083 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a70a8019-0d57-33b6-bece-c72241be9ef3 | -8.08371 | -50.97189 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| b7c9fd6c-854c-384f-aed5-c1555a1a2e95 | -9.60511 | -40.34109 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 44.4 |
| e90ef792-fd0b-3b31-8c3a-bfe5764d3bc9 | -8.46532 | -44.69158 | 2026-09-03 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a89c1040-8f4b-3b5a-9250-7c20d887c20f | -3.2484 | -47.25451 | 2026-09-03 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| b925b323-d41a-3325-aa39-25d12ba6209f | -7.72937 | -49.59323 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe1febab-bff4-3058-9484-3a44a3365b7d | -6.94439 | -45.20131 | 2026-09-03 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a28e9191-762b-33c0-95e0-031071f41a17 | -7.26128 | -47.52611 | 2026-09-03 04:02:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2d85e34e-f798-38aa-a6db-9399d8f14d42 | -10.89085 | -45.31319 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a4e20f03-c720-37b6-8428-f1d2ed56cacd | -3.2435 | -47.25373 | 2026-09-03 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| b08902c9-85b5-3ce5-bdc4-1fda5800c6ec | -8.46151 | -44.69098 | 2026-09-03 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 16c80c0f-ca03-313a-be9c-49e7354b642e | -10.87698 | -45.32537 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a2e9c83-c690-334d-b8f3-99f8ae5dace6 | -6.48777 | -53.60983 | 2026-09-03 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c4aa7cc6-233f-3dc6-9259-6a04fd099573 | -10.56884 | -47.71288 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 52f7844d-c7ec-3266-9754-7ec19915abda | -6.75849 | -44.57482 | 2026-09-03 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 202d8eb0-12ae-31d8-9b2e-b7232b52b321 | -10.89166 | -45.3085 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 38628026-b93a-3d8e-afd8-eb48236a2b5d | -10.99014 | -45.09515 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01898132-c374-3d04-8e56-758092353003 | -6.94039 | -45.20057 | 2026-09-03 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78f444ef-90ca-3f19-a4fd-6604823ae3bc | -4.1153 | -51.03156 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 90701328-cae9-3068-9d7d-02304887a9ac | -10.77479 | -44.74004 | 2026-09-03 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97f93f84-9834-35e9-bbc3-3cb4afa48421 | -10.88487 | -45.30241 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79b8e7f9-54c1-3908-95d3-5f4e3689875a | -5.64336 | -43.89716 | 2026-09-03 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d52d3c0-581b-3fdf-91df-787a10ec5c2e | -6.94095 | -45.19717 | 2026-09-03 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d8721646-ce8a-3c05-8c91-f818e755db3b | -4.91326 | -43.46772 | 2026-09-03 04:02:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| da024a5e-540e-3923-b7c7-e9a26faa6644 | -10.89604 | -45.32862 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5ba91f6e-0349-356b-a133-07884df1e554 | -10.18026 | -36.24991 | 2026-09-03 04:02:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0482c7a2-1b84-3f8d-b525-fcc2976e9b4f | -10.56653 | -47.7262 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88faaffd-6b5d-3789-9f97-cc02d3650cc4 | -6.68127 | -43.41459 | 2026-09-03 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 371e4609-5101-3d0c-a39f-6afeaebaaeb0 | -7.72838 | -49.58993 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 51d6751f-83b6-370a-9cf3-ec9aaccbab63 | -9.60802 | -40.34512 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b5baae20-ab77-34ca-adfd-0158ce1c6ea4 | -6.75756 | -44.57214 | 2026-09-03 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fcc65a8b-00fe-39c0-8328-64f7bb945ef8 | -8.46427 | -44.69404 | 2026-09-03 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 4fcb3ce4-d374-300c-81ce-5e28f54eed0c | -11.00295 | -45.08786 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 496f63c4-640e-3434-8946-e502a556c0bc | -10.92871 | -45.3441 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1619f0bb-eaef-3949-b2fd-d595cd764dcd | -6.9357 | -35.17984 | 2026-09-03 04:02:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a909a92b-fcc9-374d-b523-3f74b692ba9e | -9.61258 | -48.55951 | 2026-09-03 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| cdada105-102a-36c7-91ab-e143cfee338d | -5.73544 | -43.27731 | 2026-09-03 04:02:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d2195c09-9aa7-3397-ba28-62f74bac022f | -9.27318 | -45.65009 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ebd20a5b-22b6-38fd-9423-b86636a90082 | -8.08018 | -50.9586 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7edf7c68-d7ad-3933-b675-6ac23933851e | -6.93168 | -35.17927 | 2026-09-03 04:02:00 | NOAA-21 | CUITÉ DE MAMANGUAPE | PARAÍBA | Brasil | 2505238 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 8c34c3da-f594-3dd8-aa1d-ae69db6ea29c | -5.80372 | -43.64734 | 2026-09-03 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6d9e215-98cf-39e9-be0b-cf58abdbf5c7 | -3.2395 | -47.24746 | 2026-09-03 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3ba4355b-5be7-3410-8b06-cc9d6a4495b7 | -10.99169 | -45.08593 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| 8b828a47-902c-354a-aefa-0871d073beff | -9.22107 | -45.76384 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 72b645ea-e213-3e3d-8990-bbb72cdb8309 | -6.65005 | -39.1147 | 2026-09-03 04:02:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8c5f7e24-c5b9-31e7-bd63-da1e35e6fb4d | -10.88026 | -45.30644 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7901bbe8-1d55-3a62-9c2c-58cbbc42c662 | -10.89004 | -45.31789 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 9ec5b6a8-32c3-3f93-9661-f647468ed6f5 | -7.07567 | -44.3544 | 2026-09-03 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7089c99-4d05-3ef8-81c1-ed1a5691025d | -10.87564 | -45.31046 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 20b0ac9d-3970-35d6-9b4e-cb1fe91ef032 | -8.49065 | -44.74626 | 2026-09-03 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c09e6f48-1960-35fc-b4f1-0841821e965d | -4.1466 | -51.07241 | 2026-09-03 04:02:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2f8ff46a-aa5f-3b22-8499-b0c010640108 | -7.61369 | -49.93169 | 2026-09-03 04:02:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d65a7848-a21a-3ec8-9143-977d3499721c | -10.9992 | -45.0872 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 23.5 |
| 3cd0050a-00a4-3465-baa7-546103f14f0b | -9.42502 | -45.60382 | 2026-09-03 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c042ed64-e685-3890-b22e-758d8d50ecdc | -10.87482 | -45.31519 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| ea271ea8-9273-36a6-8695-47e8c27e17c1 | -9.60125 | -40.34406 | 2026-09-03 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 33.7 |
| fbd34c9f-1395-329e-9c22-46aec5154022 | -9.61163 | -48.56483 | 2026-09-03 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 7779a816-1434-3914-a521-10d8e9ff1df5 | -3.24439 | -47.24825 | 2026-09-03 04:02:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| b1df124c-a11f-386f-9039-fa3c108da45b | -10.56571 | -47.71977 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b74712a-849d-31c1-bfcd-ca9e543d1ee6 | -7.72997 | -49.58986 | 2026-09-03 04:02:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82a4e98c-468d-38df-9a38-3c0e4b84b279 | -7.24163 | -42.77376 | 2026-09-03 04:02:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 9ef91802-c6e2-313f-8fa7-2ac12ce176fe | -10.8769 | -45.30749 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| b6c6d937-f389-36db-9ae0-a6429d317eb5 | -9.64653 | -44.83315 | 2026-09-03 04:02:00 | NOAA-21 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ab668c6-b50b-3ff3-b356-5c5c3198cfc5 | -10.87317 | -45.32474 | 2026-09-03 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 29a2b4df-f064-3b76-a56f-f0599b94f4c2 | -8.08573 | -50.9935 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28d27d9c-4ed1-3e6b-8374-c68f74a51f59 | -3.03809 | -48.41345 | 2026-09-03 04:02:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f560042c-cda4-3be3-af87-2e075189d2b9 | -6.64951 | -39.11823 | 2026-09-03 04:02:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 801a79e6-8edf-349b-8d91-d42c7d1996fc | -8.08446 | -50.96783 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| ca58c9c4-ce77-391b-b94a-680095bad77e | -11.39198 | -41.70284 | 2026-09-03 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ea68f3b6-bded-3260-87b2-f05987ede8b3 | -8.08072 | -50.98819 | 2026-09-03 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7524b282-f7e1-3fe5-8536-fb3e7983dab7 | -10.56206 | -47.72545 | 2026-09-03 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README19.md)
