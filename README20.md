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
| 3b0f6cba-ca8e-35a6-b711-5ffc9972abe5 | -7.34993 | -43.85921 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 6f2e2389-9188-3599-b077-876a436c5d9d | -8.3638 | -46.23997 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35971370-ebcd-3db6-bb32-fcb516d8a3f5 | -7.82441 | -44.12323 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c36822a2-52ef-39bd-9a9b-c403e3fb279a | -12.36477 | -47.17732 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7bb5bc52-f7d9-32bf-98b4-321f9ea7a57e | -11.58821 | -44.05822 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e91534c1-9f6d-3249-a166-801493f5f483 | -10.252 | -44.06291 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32681150-ab07-3be0-8d9b-d6a754f03ab8 | -13.76723 | -48.22422 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2e23d0c6-4bb5-3b9b-b485-f81163345f5c | -11.50567 | -44.05363 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eaf5df32-a778-3a2e-8db4-270e414df615 | -10.49999 | -43.45947 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e389108-a385-3007-8658-a9fc8cabeea5 | -12.15158 | -45.07478 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 04419973-51d7-38f8-9589-809db969ae7b | -11.49706 | -44.03946 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2aea04d-2451-3b5b-b289-4d02a5983a09 | -10.81109 | -43.92906 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4e743f36-3dbd-3f54-a0db-23d6dbc38a9f | -11.82873 | -45.13754 | 2025-10-18 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cbccb184-527b-3063-b6f4-1dd9bb870027 | -13.03083 | -47.27787 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1024e78-7a04-37b8-b653-6411015c0598 | -7.95753 | -44.11481 | 2025-10-18 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 8d225680-0e07-3722-a238-38b8ff12ba45 | -13.84274 | -42.38644 | 2025-10-18 04:02:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| f9b6626d-f631-32f9-a20d-84fab9364e03 | -13.63571 | -44.41992 | 2025-10-18 04:02:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b08b1587-316a-366c-ba97-3c6356cf4a66 | -9.3748 | -43.76074 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 591edbf5-6daa-3cb2-9fca-b85e5e9f016b | -10.46614 | -44.06255 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 64de6711-5710-35bd-8ec9-2c07c24e54a7 | -11.35526 | -44.27836 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 816d70f4-e8ef-3f3b-b45d-4812896baef7 | -7.58487 | -44.98474 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aaf9bea7-dd26-3441-8631-410e8f7c020f | -12.16785 | -45.09154 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68961b97-6f39-3406-894f-de604a892c33 | -10.24463 | -44.03999 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 34e428b6-5de0-3bcc-ae5c-ca75029817fc | -9.24659 | -44.34657 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7b697da5-39c3-3568-894b-baa5e5758e39 | -7.75596 | -42.51051 | 2025-10-18 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2b6a35d8-3255-3036-a182-360047903a2a | -10.69994 | -44.55668 | 2025-10-18 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c238d5e6-d7a6-3123-894f-ff396a121c19 | -12.15552 | -45.08619 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 3ce014ea-045e-31ba-a1e7-52655e04717d | -13.48819 | -47.96099 | 2025-10-18 04:02:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a28bc4eb-25fd-3626-85a8-1741605143ac | -13.18845 | -46.43557 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cab1a901-2113-3199-ad84-621cef26f801 | -7.58882 | -44.98546 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e2c0f35c-2512-3c07-a581-869a41648320 | -13.76462 | -48.23508 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| abd531b4-ae5f-3704-96a7-9b4c811536e6 | -10.25756 | -44.03711 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 38546884-1771-32c4-9a7c-f0938146d02d | -13.04649 | -48.1913 | 2025-10-18 04:02:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 854c4640-85be-303e-bfc2-f1bc8be7ddfe | -7.35234 | -43.85844 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 9cd7c31d-2d10-329d-a07c-801ae82e2b11 | -14.14934 | -44.24362 | 2025-10-18 04:02:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe55c0d5-1c09-3ef5-9557-c278a65fcc05 | -6.4282 | -47.30041 | 2025-10-18 04:02:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f2d02f90-2dd3-3682-aded-b2a76b538a19 | -6.90296 | -47.99425 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d033cf75-6157-3a4c-901d-2f8dccb4c87e | -12.63944 | -44.14075 | 2025-10-18 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 24bbea57-0929-3da5-a089-c7f37ee46d2f | -9.26128 | -43.74336 | 2025-10-18 04:02:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 932b4fb1-b1b6-3569-b707-6076a9df828b | -7.16531 | -42.37754 | 2025-10-18 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 33b8f744-2b5b-34f3-b749-188f4c8bde51 | -13.62826 | -43.96064 | 2025-10-18 04:02:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95eb706a-84ea-3913-8871-cf5fd4536db6 | -10.14374 | -44.58141 | 2025-10-18 04:02:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 773bd090-2210-3c81-9ee1-307171b01bb0 | -10.25753 | -44.08107 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 933d6189-a4c3-3c6f-9991-9d32c115fb4b | -9.03186 | -47.71944 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c3640455-a2c1-3a58-8820-bc0824a7c725 | -13.22319 | -43.97848 | 2025-10-18 04:02:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d7c2b7d-6801-395e-922f-ef6df978ddb4 | -9.66245 | -48.52907 | 2025-10-18 04:02:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 40c8efc4-cb02-3371-9c80-ca371418cf4d | -12.74706 | -48.62966 | 2025-10-18 04:02:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6f4c2e5c-6812-3ccf-86ea-a2c072e027b4 | -11.61391 | -44.07957 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1edb0f0e-22c6-3cd8-84c0-cefedd386b21 | -10.81823 | -43.93025 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 130d51c9-dc76-3df2-81f8-309067c80312 | -6.99433 | -45.19999 | 2025-10-18 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29b7b26e-55d2-317a-b1d6-08b085959483 | -10.51279 | -43.40397 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df1acb31-ad63-39ae-9801-4c2caeed4b7b | -13.46009 | -43.76561 | 2025-10-18 04:02:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 17aa47ed-3f64-3777-8ce1-1e5fb0e0f938 | -10.24686 | -44.04901 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e1ad80f5-131f-3dd5-a588-ea83863fcb4b | -11.49778 | -44.18885 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0aedf9a0-ff0b-348e-b659-dba89f2fa887 | -8.54551 | -50.0759 | 2025-10-18 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c245bcb4-8082-3cf9-94ea-e3d5b871c498 | -11.60106 | -44.06889 | 2025-10-18 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fe4f8a4b-21fa-3e6a-9cf5-158c4915b824 | -7.57903 | -44.97647 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3263446b-cf8d-3814-aaa4-4ddefdea562f | -9.12877 | -46.62048 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3a3d8446-6e0b-33d9-b581-f231cb636617 | -9.55477 | -47.77971 | 2025-10-18 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 629bf618-97b0-337a-8ee4-04e9d3de9ace | -10.62544 | -42.30122 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.1 |
| bca8aba9-a968-3317-a31e-37399186d8ab | -9.19853 | -46.87153 | 2025-10-18 04:02:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1eb4038a-4600-3419-a07a-6ca767e7eb7a | -6.89707 | -45.45475 | 2025-10-18 04:02:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db93ea72-1461-351d-8c86-615186047617 | -10.49949 | -47.53929 | 2025-10-18 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a8861255-909f-3071-8e5c-28954dc7c574 | -13.23731 | -47.10268 | 2025-10-18 04:02:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a15fb97-c92d-372f-9aa0-1b291205e259 | -10.2972 | -44.04403 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3e1011c-ed63-30e0-8bae-db11175be2a1 | -10.24908 | -44.05808 | 2025-10-18 04:02:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 668eefee-03f9-3865-a98a-477a3e936248 | -11.49587 | -42.39422 | 2025-10-18 04:02:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c143fa8c-c910-3fd5-9283-a534bc3fb5e8 | -8.86434 | -46.01138 | 2025-10-18 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08d69935-c9cf-3be2-8295-d885adac3c6f | -11.47632 | -44.0106 | 2025-10-18 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d64753e1-e03c-35da-88f5-67a63f851d42 | -10.48778 | -43.42473 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5d4d39b7-3356-388d-aba6-ffe84f9f4211 | -11.35887 | -44.27898 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9a58a74f-604e-352c-a836-5a33a1b01283 | -10.95644 | -45.45897 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ab119ce7-1184-345b-97a2-000decb2d78c | -7.97596 | -40.61401 | 2025-10-18 04:02:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| de0a57e0-23d0-376a-bd94-831720013a0a | -13.04429 | -46.96436 | 2025-10-18 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 98ed2986-8410-3684-b32a-1b3ddea99d5e | -8.69855 | -47.06403 | 2025-10-18 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1eba8e22-6db8-3a8d-8f33-777ff6337569 | -10.53506 | -49.55247 | 2025-10-18 04:02:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fe0d90ff-0f87-3fc0-ac37-8c354dba6417 | -8.23123 | -39.03657 | 2025-10-18 04:02:00 | NOAA-21 | SALGUEIRO | PERNAMBUCO | Brasil | 2612208 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 8954eb00-bffe-3f5a-9376-1da46cb23c5f | -13.76379 | -48.23952 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| a8af49c0-f2ca-3487-9282-669e73911627 | -10.49913 | -43.44299 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e80aa79e-da0e-3f3d-b2fb-fb1653afd982 | -14.09113 | -42.91704 | 2025-10-18 04:02:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1523008e-a324-368b-8157-cb8db76bdef4 | -13.66535 | -43.37271 | 2025-10-18 04:02:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1fb8bc22-29c1-34a4-8421-ad1498606e66 | -10.80385 | -44.01798 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ca9cf82-1610-3de7-99af-50a3607fccc9 | -10.80675 | -44.02275 | 2025-10-18 04:02:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3724f000-10a3-3745-afc1-ada15b138b47 | -8.15535 | -49.29404 | 2025-10-18 04:02:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c0523dd-83e4-3c0d-8077-c7c51dbac90c | -10.52394 | -43.40165 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df9ebcbb-d8a6-360f-aba9-0a9c6778d985 | -7.34862 | -43.85788 | 2025-10-18 04:02:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b146ab17-5455-3513-a384-5f69c8cb0d5f | -8.11441 | -45.43076 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bf6d423c-7bfc-33e7-bae4-0c88bdadc1c8 | -13.18783 | -46.43907 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77d174fb-9eed-3fec-a352-90deac28cf63 | -13.72173 | -48.37342 | 2025-10-18 04:02:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b03941b1-c854-359a-a25d-f63099af60f1 | -12.16658 | -45.05453 | 2025-10-18 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d3902e0-145e-3fe3-90ca-0d8c260a162a | -11.29079 | -45.0288 | 2025-10-18 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5f8b0c5e-6d2a-36e8-9703-9ff67af4f0af | -8.04693 | -41.11469 | 2025-10-18 04:02:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6115a0f4-8a81-3ea3-b830-6e5ea1c884a8 | -10.63552 | -42.30286 | 2025-10-18 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 8d0c8a3d-6749-3d08-9ce9-bc589b791774 | -7.06052 | -46.75501 | 2025-10-18 04:02:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 343cfdcd-30ce-3d4c-a47b-a659c28de8e7 | -13.34667 | -44.62263 | 2025-10-18 04:02:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f7e74c8-d5fc-38f8-b599-ee1ab0b1d1f3 | -7.60804 | -45.85095 | 2025-10-18 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d17bb63b-f4fc-330f-856c-30ad408f4f60 | -8.16175 | -43.30053 | 2025-10-18 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1187cbb5-58b2-3220-88c9-4f282221f7d6 | -8.10975 | -45.43373 | 2025-10-18 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 8dfeea40-3aed-34e9-b449-1eebde773bad | -13.18446 | -46.43497 | 2025-10-18 04:02:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93ff3cd9-8488-3f32-940d-ff740ef1a2d9 | -10.50131 | -43.45151 | 2025-10-18 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README21.md)
