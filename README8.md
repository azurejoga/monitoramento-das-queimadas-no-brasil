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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fdc7b2ef-21fb-3e81-8b58-6d7f3b8d0f38 | -4.86409 | -43.22279 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d93bf357-8afb-3b76-a0ca-0ae8dd3c41d7 | -7.15331 | -42.28989 | 2025-07-14 04:27:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b2840f22-18cf-3894-a799-80728e5a2a36 | -4.58122 | -47.26287 | 2025-07-14 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44e7b7b3-9e58-3eac-88a6-bb164619ada5 | -6.25447 | -43.35803 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33f7e96c-2817-3112-a378-2cdadfb23b19 | -9.40047 | -48.69096 | 2025-07-14 04:27:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d07ecc9-71ef-3041-9f65-675b61e971c5 | -4.11925 | -47.35403 | 2025-07-14 04:27:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc0639b4-26ce-367c-b445-3314b486db53 | -9.38714 | -47.96994 | 2025-07-14 04:27:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| de02c705-504c-358f-bfed-6da0b7a12b0c | -7.31378 | -50.06265 | 2025-07-14 04:27:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a26ab4bc-1b27-3ba8-bb7e-7d82bf144f59 | -8.86857 | -46.86702 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a592d5f5-8424-348f-b0f1-74788723e62f | -6.46006 | -45.36054 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 898539e7-0062-3ec4-9e11-e563569ec876 | -9.50862 | -47.56856 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61dba9b9-1807-3dde-8281-5dbca59bac29 | -8.236 | -44.9175 | 2025-07-14 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d72f600e-2339-3474-9413-9f061b496f25 | -8.51725 | -43.30246 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.6 |
| 88f3dddd-8d44-3d3e-87c0-8739ac8bcf24 | -2.91135 | -48.23909 | 2025-07-14 04:27:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 9699873e-606f-3f96-85da-8dc97cc0bcf2 | -8.86802 | -46.8705 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b84ed14e-1278-3cd9-b76b-f1ec12e81de2 | -10.27709 | -47.61002 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0690f614-883b-3bb6-9591-93cbae81602e | -6.27214 | -43.41028 | 2025-07-14 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0fee67de-f239-3e30-a232-b38dea89aca4 | -10.28374 | -47.61109 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4f49c03-6f5e-353e-ae44-b0acb31b191d | -8.51086 | -43.30357 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| c9937cf5-436f-3a3b-9266-57ba2d03c6d3 | -6.70607 | -43.89651 | 2025-07-14 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b823986-f10a-38c2-acc1-31e1c82bd99e | -6.28809 | -43.42525 | 2025-07-14 04:27:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d939518c-59ae-38f9-b5d8-928efcd8ddd7 | -3.5848 | -47.52638 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 73a2498e-5ac9-309f-975f-4b620a64f4d9 | -4.58402 | -47.267 | 2025-07-14 04:27:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 426ffae9-6c85-3497-b4a5-37d7fdc4bc58 | -10.27653 | -47.61353 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05d55715-4822-3ff3-9a0e-457a2526ec81 | -5.16012 | -37.68419 | 2025-07-14 04:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ce9626a3-7522-34f6-8164-0fb2762171a7 | -7.87668 | -46.1379 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3b661ab4-c8a5-340f-af01-6a8d97200646 | -8.23258 | -44.91697 | 2025-07-14 04:27:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f0093723-3511-3325-967c-869d82b3cf66 | -7.18404 | -47.15928 | 2025-07-14 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8a8b5c68-db04-3451-a622-6ea258fe768d | -7.02372 | -44.36203 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1ae97b8-a697-3249-9108-a757c58fe4ac | -7.18794 | -47.15628 | 2025-07-14 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 71e8824a-3ba2-3e9a-9b4e-c5f8ebb0b455 | -7.35556 | -44.62926 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 88cf21d1-4a3e-3eca-91d9-c67389887567 | -7.19492 | -42.96591 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dd78d443-1d6c-3e08-9c78-e3cb840dc965 | -8.51387 | -43.30846 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 7d069f08-dccc-3c3e-88bd-e951584c79ff | -7.27103 | -43.49701 | 2025-07-14 04:27:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c6853297-8e3a-3a32-a24d-675d5e859649 | -7.62992 | -56.76174 | 2025-07-14 04:27:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cc6a842-40cf-348d-9e08-5bbf3a18d277 | -6.65686 | -43.12848 | 2025-07-14 04:27:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e147382b-bc2b-3d34-948e-14264100aab7 | -9.95037 | -48.16702 | 2025-07-14 04:27:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e7788bb6-93a1-3ace-98fc-b74139ba4c3e | -6.1654 | -45.87984 | 2025-07-14 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c9a75e63-fb16-328e-b2e8-25dd6fcbbb4f | -6.14409 | -44.08911 | 2025-07-14 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b7088f3-b9c3-3b55-9f8a-6e37240e207c | -8.50718 | -43.30302 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| 905ee882-bb5c-39cd-bab5-bd9eb02bf8a0 | -4.51021 | -38.55062 | 2025-07-14 04:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| e0139d2c-2ff5-3766-82a1-3cc8f81900ad | -4.86343 | -43.22141 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| de3673c7-f0b1-3c76-819b-3c820e131211 | -6.99094 | -44.48362 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa2aa8ce-b5a8-3102-968d-e0c2e88f86e8 | -6.2745 | -47.51157 | 2025-07-14 04:27:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fa28dbb-7b14-321b-ac54-bcbb381c0ed5 | -6.64666 | -45.02162 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cba3e042-39a7-3f53-96d7-23a5d713a4ea | -7.29145 | -43.04024 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3502d09d-1532-351f-87e7-93ea87637360 | -7.26498 | -45.31073 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92d67c62-5dd2-348a-9649-89c308b10d5e | -7.54143 | -43.94628 | 2025-07-14 04:27:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 130c0293-b946-3933-9f41-0ff84b576497 | -7.24358 | -46.97869 | 2025-07-14 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 57fa627f-45b5-3dad-b6b7-6f2ca87eca39 | -8.03694 | -50.0909 | 2025-07-14 04:27:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c936357-f04e-359d-bf45-9cab2b28cf44 | -7.16711 | -43.00135 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bfc4ed9a-9262-3274-a497-744305e5155f | -6.11951 | -44.22736 | 2025-07-14 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c665b821-da29-37d0-871e-d508d2863352 | -5.279 | -44.88047 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 633e9aa9-49d8-3951-a071-71f0a9f81c72 | -3.58315 | -47.51471 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c2f01c04-83a8-31b3-8847-def249ff6e28 | -6.43606 | -45.33873 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| b6a6ca8a-4e58-39c6-93e4-5538a75a9ace | -4.27636 | -46.93346 | 2025-07-14 04:27:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2228bb4-88b2-3411-9e58-492275cbf34d | -6.68778 | -43.68588 | 2025-07-14 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 053aa880-73ee-394e-8551-a6d933afccf5 | -7.00928 | -44.41008 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f3329f7c-f40f-3161-95f2-bb6983e36a4d | -7.29081 | -43.0446 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 45538bd3-a494-3c55-a721-7a74d0f32f1f | -6.70957 | -43.89702 | 2025-07-14 04:27:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cc553efd-a085-36d4-929e-00358be0849b | -7.04321 | -44.37296 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04e020b0-30e5-3f71-aa33-6c8b986e01e8 | -7.2591 | -46.98835 | 2025-07-14 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0f509d54-2889-3258-bdda-08a8cf243798 | -3.5854 | -47.52267 | 2025-07-14 04:27:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f0b8ccfd-9839-3948-ba69-21e0867c8e3f | -6.73417 | -45.26548 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c8103b9b-f368-3b81-8104-fe30999891aa | -6.23901 | -43.34851 | 2025-07-14 04:27:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b36654c-72b0-3d7e-9a27-bba75f7518f3 | -8.59865 | -47.31026 | 2025-07-14 04:27:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 02f94d41-07b0-3214-ba14-43f70eeb8cb7 | -5.58703 | -45.74562 | 2025-07-14 04:27:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d5c1eb41-ee78-3cd6-8c3b-d02960a1387b | -6.41163 | -42.42964 | 2025-07-14 04:27:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ebc334a9-bb2d-371b-afaa-e3dfc9cc54e6 | -8.90734 | -47.34938 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 78efe064-d0d3-3198-89a3-6d3940e4760e | -8.12833 | -47.58494 | 2025-07-14 04:27:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef0f591b-2413-3aa1-bf63-84b57e81754b | -7.18738 | -47.1598 | 2025-07-14 04:27:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6123b18b-5b6c-3ba6-a8cd-1a3c79024dc7 | -7.01621 | -44.38795 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c2c14248-c089-320c-8d31-6f1801664760 | -7.13909 | -44.28996 | 2025-07-14 04:27:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| be8f81ed-ba09-3c8f-99c7-f9993947bba6 | -6.46898 | -45.36914 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0470c74f-a596-31ee-a90c-6ea4a8a1d60d | -5.86827 | -45.15649 | 2025-07-14 04:27:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4a16fdc1-88f1-3857-bd8e-432cac59725d | -4.5334 | -48.02282 | 2025-07-14 04:27:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ec474674-322c-3bca-b4cb-696c6c296b84 | -5.42804 | -42.88182 | 2025-07-14 04:27:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 90789d95-8b0c-3bb2-819a-cbde9bc92059 | -6.46285 | -45.36457 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fa67309-d366-369b-8ca1-b43838e94444 | -8.51886 | -43.30034 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 25.6 |
| 1338e7fe-04df-3518-9625-edfc4205c552 | -6.43551 | -45.34227 | 2025-07-14 04:27:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e91f13fe-20e0-3f57-8e0f-2949abbdde18 | -7.22725 | -44.00031 | 2025-07-14 04:27:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f278d0fa-d264-3255-9d5e-43527d09ffd2 | -9.4953 | -47.56641 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| afed2f91-c1f0-367a-b677-d7764ae7227f | -4.51093 | -38.54562 | 2025-07-14 04:27:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| db14415f-15ac-3336-9868-03d7830c9a5b | -8.91067 | -47.34991 | 2025-07-14 04:27:00 | NPP-375D | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5feaf0c9-483d-31a9-b38a-f5e11c837b43 | -5.15464 | -37.68637 | 2025-07-14 04:27:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 311231ed-ad1c-3fa0-b1ec-8a622a3c99ab | -9.49197 | -47.56588 | 2025-07-14 04:27:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ec33c0b4-58c2-3658-bc26-9a072c066843 | -8.24856 | -41.93241 | 2025-07-14 04:27:00 | NPP-375D | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| a0be3017-a37f-3720-b6c9-0248f5201c20 | -6.12295 | -44.22788 | 2025-07-14 04:27:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ff15ffaa-57b3-38f2-b464-dba0d1ce23a0 | -6.68717 | -43.68983 | 2025-07-14 04:27:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 143ac7ce-4862-30ba-a39f-87e0b080fbf7 | -7.53899 | -45.25021 | 2025-07-14 04:27:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0e45c705-4302-30df-a3f9-331218fd8d1a | -7.58535 | -44.72413 | 2025-07-14 04:27:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bb9eebd9-5900-3db7-b00d-88c9599039c9 | -9.16331 | -43.34626 | 2025-07-14 04:27:00 | NPP-375D | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 3dc0b899-19fd-3b18-89f9-1c166ba9ee05 | -7.60008 | -46.26606 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5d470fc6-957b-364c-bc8c-5c90281fd2ef | -7.01964 | -44.38856 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 14a0d099-8d20-3664-92b2-c38856a11655 | -8.87744 | -46.89703 | 2025-07-14 04:27:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5fdb900c-2a57-3b80-9d1a-acdbb07b2816 | -5.10849 | -43.15051 | 2025-07-14 04:27:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d6a0923a-ba20-360c-a27a-434d42805e7a | -6.83044 | -42.86948 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 817aa375-616c-3879-b1f2-22f8d5a8ff40 | -7.03976 | -44.37246 | 2025-07-14 04:27:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 02c29606-3b8e-310a-835c-d08734d72bae | -7.16788 | -42.97061 | 2025-07-14 04:27:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 63fcecd7-9924-33a8-821c-ea0166ba1996 | -8.51662 | -43.3068 | 2025-07-14 04:27:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |


[Clique aqui para ver as próximas entradas](README9.md)
