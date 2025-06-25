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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05c745dc-36d0-3dbf-bf67-55287a152596 | -8.23964 | -44.94149 | 2025-06-25 04:06:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2919288f-0f43-3120-bef4-061583eb3150 | -7.00551 | -44.54945 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 27818493-91fe-363d-b907-3e6da3fe9f72 | -6.22154 | -43.36472 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e66ff925-c743-370c-8be0-a8a7c6967e55 | -6.22555 | -43.36158 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34f081db-a696-38b1-8365-47472b6140d7 | -8.53168 | -46.32906 | 2025-06-25 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 51a23ca5-b33a-3aa6-a051-8cffc1f5bbeb | -7.36015 | -43.48124 | 2025-06-25 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8438d1af-856b-3601-ad62-f6c8d516dafc | -6.1762 | -48.05814 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 1f6ca7d2-3347-3942-9b9e-6aa22964d337 | -2.63898 | -47.30776 | 2025-06-25 04:06:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4be03cba-1e27-3d94-94b6-0e8fd4e3a5a2 | -6.81625 | -42.86853 | 2025-06-25 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| b713864d-5e6a-3456-b115-d96debc908ab | -5.97399 | -43.80943 | 2025-06-25 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2e54d42c-faa8-384e-b0bc-fedb469239f7 | -6.17549 | -48.06237 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 0c220c99-1a54-349f-a579-1250c9e4da00 | -7.36355 | -43.48178 | 2025-06-25 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20709827-fa9d-3334-8ecc-0f95393fcc6d | -7.02357 | -44.57261 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 631ca5ff-d208-3b96-8e50-2dc4031dfbf8 | -8.15142 | -46.82578 | 2025-06-25 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64670408-68e7-3887-83d3-5dc0a0318c10 | -6.18065 | -48.05894 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| acf8adaa-ca1d-3379-8427-70d3fc372f0d | -8.52785 | -46.32836 | 2025-06-25 04:06:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6b3c0f63-c415-3f1c-a5a4-31933a479b0d | -7.02843 | -44.56527 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b94c4614-efd1-3e13-a420-4acb19fe9bde | -6.29598 | -44.23533 | 2025-06-25 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| eb094664-44db-3275-aca9-bbe1783392c5 | -4.39251 | -47.28241 | 2025-06-25 04:06:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 71a087a1-c727-348b-abc5-488648318544 | -8.15396 | -46.82361 | 2025-06-25 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9086cd8f-7602-376f-9ba7-d40fb8ae37f5 | -6.17994 | -48.06314 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 2fbdfaa9-6616-3a4e-9d69-81fbbe01f890 | -7.03189 | -44.10115 | 2025-06-25 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d96697ba-9eeb-309e-9dae-f8d03992a387 | -6.18135 | -48.05478 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 73e9e784-592a-3fea-88ce-5a565a2c62b5 | -8.06836 | -43.11263 | 2025-06-25 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 0e4c0f7e-11bc-3f09-b1cb-d1ed5ded606f | -6.18365 | -48.06837 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| e0649738-3584-31b2-8130-8fa30163cd25 | -5.77976 | -43.6223 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 61203671-da4b-3dbf-8948-46257ea8b6b5 | -4.53781 | -48.00636 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| acdc25f8-25bb-3728-b40e-5da004879b87 | -6.22094 | -43.36841 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f20ae0f8-e402-32ee-a333-421d4468d65a | -5.73391 | -43.495 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 633a757e-1b6e-32ec-bb25-624c88787632 | -4.54163 | -48.0116 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fd35254f-b63c-38c3-b3ea-1d5a55f1aded | -5.76383 | -43.39602 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a85abf12-ff18-30de-870a-d703d7d20072 | -6.92203 | -46.40802 | 2025-06-25 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e1b98afd-5404-38a3-8b64-f3b6aaad3956 | -4.54697 | -48.00767 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| efb5277a-b3bd-39dd-8db3-86642a6d616b | -7.02423 | -44.5686 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b3f3fc6f-6106-3d38-a11a-1d7805c6d4a5 | -6.92597 | -46.40876 | 2025-06-25 04:06:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9206ba23-dfd5-3ab3-acc9-64aadcbac0ba | -6.22116 | -43.36475 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2987843d-090d-3541-b09f-9659c9e45991 | -7.43651 | -45.54134 | 2025-06-25 04:06:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7bd5071-4685-38de-a134-1ea3b437b472 | -5.97578 | -43.75461 | 2025-06-25 04:06:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a95ba676-8a77-3062-8e34-1ee7fcdede3d | -6.95614 | -42.92384 | 2025-06-25 04:06:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 76fb8345-10e0-3821-a13e-e17920ffc9f8 | -7.012 | -44.55433 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 12d19bbc-b441-3369-a85a-82e1ee8e0368 | -7.33777 | -43.19051 | 2025-06-25 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| af215f6c-bcb1-3de1-820b-451f5a73e0c0 | -8.05889 | -43.10744 | 2025-06-25 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 520ef4cb-bf58-3253-9c9a-2d7fd8eae347 | -4.01074 | -43.23919 | 2025-06-25 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 528b7d95-45e7-3258-ae0c-a720280df23b | -9.55323 | -40.34625 | 2025-06-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 8125ba71-2ccb-309f-95d0-1428b7b76d11 | -6.60395 | -44.25823 | 2025-06-25 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 495dcf50-272d-385c-97ec-984fe9d20e36 | -6.22836 | -43.36581 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dbbe789-0b43-307d-a649-706dfa9b67fd | -6.91151 | -43.97503 | 2025-06-25 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7854baa3-55f4-3f70-98bf-16921fdb6b03 | -6.95923 | -42.80377 | 2025-06-25 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 41cce7f8-02ca-38a1-8562-b0cbcf93b4b2 | -7.70816 | -47.38002 | 2025-06-25 04:06:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb08d45e-128a-39b2-b5f3-863920fc12cd | -4.18455 | -48.15069 | 2025-06-25 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| adf90748-f6b6-33e2-ae87-74786e29cb1a | -5.82783 | -46.36529 | 2025-06-25 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 89215f0f-49ab-3fe2-aea3-cc33f980b9f4 | -6.1792 | -48.06757 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 8af79c14-84e0-349e-951f-8f709cf8f57a | -6.95589 | -42.80324 | 2025-06-25 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f6f6b7de-ea55-340a-af31-7d113724ab05 | -4.54239 | -48.007 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b96b7a50-3424-37c4-a4e7-3d2cb23423c1 | -5.75295 | -43.39812 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5dd9a0d-7daf-317f-8642-a257b4747ec6 | -7.00599 | -44.55135 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa6b5416-8a85-3ef5-810d-e7a964b8b265 | -6.17768 | -48.07667 | 2025-06-25 04:06:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 20c1c0f6-4474-3219-99d5-e383cd2531d1 | -3.89639 | -42.55113 | 2025-06-25 04:06:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b44487ef-05e7-30ec-abfb-198d5df4acf2 | -6.95867 | -42.80732 | 2025-06-25 04:06:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e8aa4f4e-b2cd-3fbc-b21e-4ff0db3cbdf8 | -8.05946 | -43.10387 | 2025-06-25 04:06:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1a667aef-0d49-3a25-bb8b-344cb87fc134 | -7.33647 | -43.21982 | 2025-06-25 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6b815194-3455-3146-80c9-ab3ff35835ad | -3.78326 | -41.03864 | 2025-06-25 04:06:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f43ed20f-5cf1-3a92-9aa3-7f6a34924604 | -8.04551 | -46.89403 | 2025-06-25 04:06:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7e9f99db-774c-353e-a5a9-3934ca970128 | -7.33552 | -43.19371 | 2025-06-25 04:06:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6f6a4f46-ba58-3938-bd52-27cc9e58b306 | -7.00484 | -44.55346 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 26ccb1ab-59b1-398c-8529-37bc94ccbbe9 | -3.61822 | -47.54062 | 2025-06-25 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5b4b2f2-c520-3633-9a92-c80ee5e35db2 | -3.9963 | -43.24077 | 2025-06-25 04:06:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 8fe36c5f-0a44-36cc-9e5b-d52d9968324f | -7.35277 | -43.48383 | 2025-06-25 04:06:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f68d242b-c5e8-3cb9-8ce5-6641c83a4b9f | -5.45043 | -43.57507 | 2025-06-25 04:06:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94403ffa-feba-3c4e-a3e1-15a8ce19517a | -4.37226 | -48.06784 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f4df4ee6-35b2-3683-83d3-027958c9f732 | -5.35914 | -45.12212 | 2025-06-25 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48560202-d147-3462-b80f-66c81eb5205b | -5.35987 | -45.11765 | 2025-06-25 04:06:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fdb80bea-5ef7-396d-99c3-bd827ace0255 | -6.90804 | -43.97446 | 2025-06-25 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 93e0f2eb-63c2-3b21-864d-c30bb2e1be49 | -4.53705 | -48.01094 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 19490004-e0fb-382a-bf32-52d1ad4fce81 | -3.61896 | -47.53617 | 2025-06-25 04:06:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 401fbdf0-e073-3335-b8bc-a2b066744de3 | -9.54981 | -40.34573 | 2025-06-25 04:06:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 3169af9a-511d-36ce-8f8c-6a0d19207d4d | -7.94727 | -44.86207 | 2025-06-25 04:06:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92e3cc73-6730-304e-b499-52e5e570d499 | -6.6033 | -44.26226 | 2025-06-25 04:06:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac30e583-1e02-3b3d-852e-8ee9dd17a20b | -7.02068 | -44.56802 | 2025-06-25 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aa9f75dd-3aef-36cd-8c72-cb8dc78f4822 | -4.53245 | -48.01038 | 2025-06-25 04:06:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8a890288-3ba3-3876-b344-8242390598cf | -6.90929 | -43.96682 | 2025-06-25 04:06:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f72d749-c365-3d5c-8f31-15ad63de0f78 | -6.22214 | -43.36103 | 2025-06-25 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3810c601-186c-33c6-9c82-672c5b3e8276 | -5.56512 | -46.29332 | 2025-06-25 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f617712d-688e-3c46-8766-2f2d5461d7fa | -11.1817 | -48.61844 | 2025-06-25 04:08:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| ed3b4ae4-b37f-3c92-a090-f83735284586 | -8.71219 | -47.85847 | 2025-06-25 04:08:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5ca2c87b-2a78-3e56-bfbf-6844680b5467 | -9.92067 | -52.4315 | 2025-06-25 04:08:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3f6855a2-2b49-3fa2-a7d2-7b449dce67c4 | -9.26118 | -47.64792 | 2025-06-25 04:08:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 471105a3-45c0-3df2-9fd7-cf542ffbb2ab | -14.25506 | -50.41045 | 2025-06-25 04:08:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cef7fae8-0981-34f5-bd5f-a58c08d9aad4 | -10.44562 | -47.95346 | 2025-06-25 04:08:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 82a88a47-55ad-3d64-bfd3-b07c25903ab7 | -11.08813 | -46.64009 | 2025-06-25 04:08:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 66dff662-17fa-3f01-893c-caa211ed0fdf | -10.51921 | -47.57833 | 2025-06-25 04:08:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f145f772-1cc6-3ee7-a1c5-761c984f57fe | -14.25414 | -50.41527 | 2025-06-25 04:08:00 | NOAA-20 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f23e422d-f6ae-38bd-9089-9afa49122b40 | -9.87274 | -49.56185 | 2025-06-25 04:08:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1f5a8d1-ba4e-3ad6-a455-ea8a68a253d2 | -12.80422 | -48.73398 | 2025-06-25 04:08:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7f841c9f-d2c5-3a4e-a65f-26caed1690f7 | -11.77619 | -47.39956 | 2025-06-25 04:08:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ec70cd6c-e7fd-360e-92d3-6cabf71b11e2 | -11.93816 | -48.4229 | 2025-06-25 04:08:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7f5cc5ad-1d78-3551-8cbb-772681cde22a | -14.71747 | -48.40675 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9bd44ea4-065c-39f4-817e-3afd19e4a087 | -9.81489 | -48.38873 | 2025-06-25 04:08:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 334b6eb1-b7b0-39f1-abba-46862c8e269b | -14.40193 | -47.87588 | 2025-06-25 04:08:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e7ac72d0-9dbf-32bb-b6fe-0185683906d7 | -8.97835 | -49.87486 | 2025-06-25 04:08:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README10.md)
