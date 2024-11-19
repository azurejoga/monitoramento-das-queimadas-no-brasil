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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 67ddcc98-0939-3d2f-b230-3906c645f861 | -8.26345 | -44.0415 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3dedfe1d-7f04-3dbe-8e82-cee81bc06e7c | -8.00034 | -44.39001 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 02e827df-fc2c-378e-a891-3e3dd1ddacc1 | -8.27933 | -44.02209 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b8d4f5e-4f43-3902-9fb5-06f1aefe977e | -8.59432 | -39.53876 | 2024-11-19 03:55:00 | NOAA-20 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 903166f1-e439-3721-ace2-c1171069ec13 | -7.97569 | -48.18143 | 2024-11-19 03:55:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6334e795-9f71-3c1b-a180-39cfd3694d95 | -9.52791 | -35.70655 | 2024-11-19 03:55:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 3091c399-ef1a-3e16-8b1e-f79f508854e0 | -7.48356 | -47.15668 | 2024-11-19 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 69b4db81-0de2-3d59-9a63-55b75486dd96 | -17.21514 | -43.70211 | 2024-11-19 03:55:00 | NOAA-20 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db433ce0-d54a-3b01-a885-762e31ff40cf | -9.25245 | -45.00836 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b247353-9df6-342d-9dbb-c175df40d620 | -7.89924 | -44.21988 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 321e079c-1824-362f-8070-f9aa9c24c4b2 | -9.08339 | -40.54128 | 2024-11-19 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4cb382a8-b2b3-3075-982f-6554dfc9574f | -8.26469 | -44.03418 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8e0fb4d4-5a5b-34cb-8501-6a36d1c56803 | -13.98811 | -43.66626 | 2024-11-19 03:55:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5141be74-73b7-3ac7-aa19-01e941f00c2c | -8.68021 | -47.98564 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| f622754e-67bc-3e7f-84be-4c910fb9894f | -9.0828 | -40.54495 | 2024-11-19 03:55:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 88361037-8af0-3201-8db7-9dc782711604 | -7.56687 | -46.45802 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6245353e-38f6-35d8-9063-738e9286942c | -7.88613 | -44.22148 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 415b7598-5172-3336-bb00-011443222096 | -14.47873 | -43.363 | 2024-11-19 03:55:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| d0b8fefc-8819-39b1-bb36-d684bd97a808 | -7.47198 | -47.37239 | 2024-11-19 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 56b77a89-27a9-326f-927f-aeb57b90ecb2 | -7.99968 | -44.39392 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9d9be390-1c68-30b9-8b9f-3a49ce1f3186 | -8.2653 | -44.03053 | 2024-11-19 03:55:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c032f4d5-0677-3109-9303-820c80550405 | -9.24961 | -44.99942 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 9cd50555-25e5-388a-b8b7-1da0b189a21e | -7.89586 | -45.96329 | 2024-11-19 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5ebfc6b7-bad4-3e9e-be22-1c8045d5f343 | -8.00388 | -44.39464 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 992ff4a1-485b-3842-a73e-b2257afdbc02 | -7.9196 | -43.78045 | 2024-11-19 03:55:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4837feb5-c59b-329c-8ae3-be54626567de | -7.56876 | -44.55124 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dcd74c7-e327-348f-964f-c06c0ff583f5 | -10.14424 | -38.51724 | 2024-11-19 03:55:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 131a65da-ebdf-35db-b4c7-4b198f7e24b7 | -9.53217 | -35.70286 | 2024-11-19 03:55:00 | NOAA-20 | MACEIÓ | ALAGOAS | Brasil | 2704302 | 27 | 33 | nan | nan | nan | Mata Atlântica | 13.2 |
| ecca4f73-435b-3328-b9ff-da9af02ab369 | -20.10718 | -47.46932 | 2024-11-19 03:55:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a24756e5-ba6b-3694-b46c-7b3a871d3d84 | -6.97996 | -47.82417 | 2024-11-19 03:55:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cbee52d0-21e0-3221-a647-2a3458e1f07b | -16.08801 | -39.40873 | 2024-11-19 03:55:00 | NOAA-20 | EUNÁPOLIS | BAHIA | Brasil | 2910727 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 99e6f655-8865-315a-9318-3d525ed2c6e4 | -7.43723 | -44.68247 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e563a29-12f8-3765-ac96-95fd23d97736 | -9.15817 | -44.30331 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5ddfa879-3813-3470-9b44-9743d0855a5a | -6.64344 | -47.9193 | 2024-11-19 03:55:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cff3f78d-81bf-37dd-8a66-c6f3c08abf79 | -7.49701 | -47.359 | 2024-11-19 03:55:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| eca8b500-c76c-35e1-b9b5-e9fa50597473 | -9.29497 | -43.27759 | 2024-11-19 03:55:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b6dfe58a-2af7-393b-9595-2d13bb3afa34 | -16.67984 | -43.88419 | 2024-11-19 03:55:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7d291185-2577-3159-bb04-7283de44c0b4 | -9.25674 | -45.00912 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| baaaf412-ad7e-351a-afa4-ae158efce87b | -8.67371 | -47.99143 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c55441f8-2e79-3f4d-b557-3b14cb0b3623 | -15.78202 | -38.95913 | 2024-11-19 03:55:00 | NOAA-20 | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| cae7429d-94f1-308f-8f20-03a7d1f40ab6 | -9.26173 | -45.00581 | 2024-11-19 03:55:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 600df60b-a1d5-30d2-bc5b-83ad9fb7d4d5 | -7.56622 | -44.54836 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9c5056ba-ee70-3814-b282-9f7c2d0ddd84 | -8.67491 | -47.98475 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 49838281-a83e-34d5-9fed-ff9ab8f685e4 | -20.7641 | -46.76935 | 2024-11-19 03:55:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ee8008e6-361d-3ce4-bdf1-d8052d068cad | -8.66842 | -47.99048 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 551b2fdb-33b4-3c66-ba9d-d0961ba8e7f5 | -7.99944 | -44.3698 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 972c38da-70e2-391e-8cec-a1e0298c4012 | -7.56442 | -46.45619 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 529101c5-5998-334f-a543-02faaf0f4670 | -15.08015 | -43.4068 | 2024-11-19 03:55:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 74c70327-aaad-3964-87ee-c8b6da14fcec | -7.89859 | -44.2237 | 2024-11-19 03:55:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3afd2b8-e254-3b07-bfec-8a587d278825 | -7.42589 | -47.86892 | 2024-11-19 03:55:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3dd971d-9b68-3f2f-b9fa-ccb1997ca571 | -8.67431 | -47.9881 | 2024-11-19 03:55:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8141b959-4b1d-3ba6-9780-947eeeb10d65 | -8.50226 | -43.91336 | 2024-11-19 03:55:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7af5777d-17f7-35e5-93f2-90e14a87683f | -8.001 | -44.38611 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1190bd94-f691-382f-9641-d543bf9f8d50 | -8.00454 | -44.39073 | 2024-11-19 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34edf6ea-0ca3-3224-b664-cf1ff9733eb6 | -7.5659 | -46.4634 | 2024-11-19 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 554094bb-a29a-3f14-a62a-16fb47df0af4 | -9.297 | -43.27529 | 2024-11-19 03:55:00 | NOAA-20 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a3b71b0b-6cc1-351c-98fd-ad42a354081f | -22.30625 | -49.76872 | 2024-11-19 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 6bd3a756-c02d-3bec-abbd-f023031266fb | -22.91873 | -45.41343 | 2024-11-19 03:57:00 | NOAA-20 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1a5a0cf3-c9d3-3017-855d-2fa67e3c0696 | -23.42788 | -46.41192 | 2024-11-19 03:57:00 | NOAA-20 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2bdccd43-bc9c-3225-a2e0-48a0b8643a78 | -22.30734 | -49.76344 | 2024-11-19 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| e7003d1c-30bd-3e99-a102-1d877643eb0d | -23.33772 | -46.7756 | 2024-11-19 03:57:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3bf64178-03f2-37b1-baa8-358f162db39f | -23.983 | -48.91874 | 2024-11-19 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1bd5c287-7b6e-38eb-98d4-75e7ec649bad | -22.54024 | -48.81505 | 2024-11-19 03:57:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 78821205-0c92-35ce-bafd-895485ac63b1 | -23.75468 | -49.00977 | 2024-11-19 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2565c110-c887-33da-acb8-692f371b2e7c | -23.06541 | -50.25377 | 2024-11-19 03:57:00 | NOAA-20 | ANDIRÁ | PARANÁ | Brasil | 4101101 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| f0e5076c-00e8-32be-bfa8-9bbf196230f4 | -22.78864 | -41.99014 | 2024-11-19 03:57:00 | NOAA-20 | ARMAÇÃO DOS BÚZIOS | RIO DE JANEIRO | Brasil | 3300233 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35ec9c09-04b3-365c-8266-b6c250727861 | -23.7045 | -46.47899 | 2024-11-19 03:57:00 | NOAA-20 | MAUÁ | SÃO PAULO | Brasil | 3529401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| cba1f8b5-c6ac-3587-bcf6-31d31a255fcf | -21.19778 | -48.56338 | 2024-11-19 03:57:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 991fb389-b687-372b-936a-c8995d207ec0 | -22.30168 | -49.76751 | 2024-11-19 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 7512b865-e74f-3948-8079-f85944cd0d04 | -23.96787 | -54.15016 | 2024-11-19 03:57:00 | NOAA-20 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| a5f3493d-7a0f-3194-b5c0-9dadf87abc00 | -23.75983 | -49.0064 | 2024-11-19 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 13aa4a6c-3d05-3644-bc35-3fab60fcfc9a | -23.40513 | -46.55803 | 2024-11-19 03:57:00 | NOAA-20 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6a196643-fbc6-3651-8d09-fcec43a3aa31 | -22.30275 | -49.76229 | 2024-11-19 03:57:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 03be4648-16d8-345d-9d12-a9caf6e977c3 | -26.98634 | -51.17008 | 2024-11-19 03:57:00 | NOAA-20 | VIDEIRA | SANTA CATARINA | Brasil | 4219309 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da4cc14b-2e57-346c-a068-f546cd7e1cc0 | -4.1059 | -43.5843 | 2024-11-19 04:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 92fa4537-71a4-3d8b-bce5-c502d9140a41 | -4.5614 | -48.0141 | 2024-11-19 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 157.8 |
| 23ab3b85-753f-38c6-876b-7d7cfe32cc59 | -3.5125 | -50.2343 | 2024-11-19 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 758c30ed-4a5d-3e20-871e-efffccd7f751 | -23.9711 | -54.1148 | 2024-11-19 04:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 92.9 |
| 6c8648dd-782d-3bb1-ab77-32cea24658c6 | -23.95 | -54.1191 | 2024-11-19 04:00:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 81.2 |
| 05fbc502-9172-35e2-bc15-7a5021b76c3c | -4.5429 | -48.0151 | 2024-11-19 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 16e365ae-cbe3-3da3-9045-4f04772afd9e | -4.5616 | -47.9925 | 2024-11-19 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| d0798406-be3d-35b9-bfde-4aacf0767e67 | -4.1246 | -43.5833 | 2024-11-19 04:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 90c7e86b-7953-3df6-94ca-559a7e9542aa | -4.5613 | -48.0358 | 2024-11-19 04:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.6 |
| d988f0c6-53f3-39c3-ade2-5bcc02e00ba2 | -1.5869 | -53.7933 | 2024-11-19 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 351c2b8b-2f27-3ee8-83e5-46e25243dc3c | -5.9788 | -45.3621 | 2024-11-19 04:00:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 3be1ebbe-69a5-3f05-bbfd-80517145da75 | -1.5869 | -53.8134 | 2024-11-19 04:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 55.8 |
| d74f5f14-5a30-39d4-8ddd-879d9cce5e2e | -23.9706 | -54.1372 | 2024-11-19 04:00:00 | GOES-16 | MUNDO NOVO | MATO GROSSO DO SUL | Brasil | 5005681 | 50 | 33 | nan | nan | nan | Mata Atlântica | 99.1 |
| 32b59840-2f3e-3183-bb80-7446a0da5e76 | -1.424 | -52.4368 | 2024-11-19 04:00:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 59.8 |
| d13d3076-3df0-30f8-a4ba-d12baa73e476 | -3.5126 | -50.2133 | 2024-11-19 04:00:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| f3384acd-5926-3848-b62c-2caf79c9b9e8 | -1.5869 | -53.7933 | 2024-11-19 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5144c738-aefb-3432-b0fd-4f6d59271a72 | -1.424 | -52.4368 | 2024-11-19 04:10:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b5869f0b-f843-3050-bb18-307792fe6351 | -4.5429 | -48.0151 | 2024-11-19 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 0d1f4ee6-db3a-374c-83df-ad141458b2a1 | -1.5869 | -53.8134 | 2024-11-19 04:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4fa649f0-22f8-317d-8c64-6410e287ca2e | -4.58 | -48.0132 | 2024-11-19 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| e15b747d-d9d6-398c-9049-6f1189d47adc | -3.5125 | -50.2343 | 2024-11-19 04:10:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 26dfa2a3-4d28-3c83-b4bc-a86624282498 | -4.5616 | -47.9925 | 2024-11-19 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 37b30567-a4dd-33e5-a9ae-703c9d698733 | -5.9788 | -45.3621 | 2024-11-19 04:10:00 | GOES-16 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 3e3d886e-fa2d-3014-a25b-874257852b73 | -4.1059 | -43.5843 | 2024-11-19 04:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 0b40a388-3184-33ed-94b8-bcb2b3689579 | -4.5614 | -48.0141 | 2024-11-19 04:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 36c7aaff-f5e0-3a67-b56a-07b1c5d5abe3 | -4.1246 | -43.5833 | 2024-11-19 04:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 56.7 |


[Clique aqui para ver as próximas entradas](README22.md)
