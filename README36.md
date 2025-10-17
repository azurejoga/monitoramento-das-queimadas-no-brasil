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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| acffa997-9604-3b0d-b0df-25b7a12a5822 | -3.85027 | -41.56939 | 2025-10-17 04:17:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 13277020-7666-3946-8038-6ef382f03414 | 0.32198 | -51.36321 | 2025-10-17 04:17:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 21572d7e-2541-3597-8b32-f9848eb6bc01 | 1.06027 | -51.22369 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3b586685-47ae-361f-a77e-6b78ee625404 | 1.71566 | -55.80391 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a73aeb3b-38be-3818-9fc3-d50328a792ab | 1.02786 | -51.11135 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8655d56d-deca-376f-b2a1-21409cd409db | -3.24367 | -45.97611 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a6a025e6-5dfe-3139-bde9-19f42154b72f | 1.03559 | -51.16244 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73e52d19-c035-33bf-97ef-2dd1d01063bc | 1.84497 | -55.68356 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e32a20da-4ba0-3c84-90af-22f1066d6309 | -3.23682 | -45.97503 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 670a2d40-cc46-33d5-8b02-2a9b818a69a6 | 1.04304 | -51.21164 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76101cd6-6831-304b-8072-2f7503519ebe | -3.62695 | -42.76974 | 2025-10-17 04:17:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22d480ee-b795-3910-92cc-9aed4c685454 | -2.74464 | -49.39186 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 436341ff-1d88-3d68-a477-36b57cf5a503 | -3.23565 | -45.98251 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 36fb97d4-2ed7-37ab-adf7-e6949f4de539 | 1.78087 | -55.90144 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f4dcf3ff-4343-3cbf-8f80-920f9d036f5e | 1.85245 | -55.67166 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 61820497-cb7b-3790-a129-07f7268ad5b6 | 0.87559 | -51.12587 | 2025-10-17 04:17:00 | NOAA-21 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9e99451d-8937-3ce1-897b-34f69a14af33 | 1.82898 | -55.69994 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| fbba57f8-a7b6-3e81-9b49-3e8893956b5c | 1.0426 | -51.20876 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e61660d-fe0d-33c9-bad5-7d4b8660ffa0 | -3.98288 | -42.49117 | 2025-10-17 04:17:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 334f29c1-a75a-3cba-a36e-a7b95900d8d7 | 1.73588 | -55.78742 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 9c5f04a1-95bc-3d22-9eac-429ffcc9161b | 1.83329 | -55.69754 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c2164fca-da14-3ff2-a992-490cbca1d0a9 | -3.43652 | -39.64948 | 2025-10-17 04:17:00 | NOAA-21 | ITAPIPOCA | CEARÁ | Brasil | 2306405 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2e8fb376-f8dd-3878-a971-ed8f74037ce4 | -3.10675 | -47.51153 | 2025-10-17 04:17:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7d52508-7459-38e9-b580-fa1abd9abfdc | 1.78676 | -55.89397 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8be843a4-52d5-32dd-a5c7-7bcf584d9126 | -2.71364 | -49.41483 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| dd548574-c2a9-3ded-b761-b7c8562d0853 | -2.74881 | -49.39251 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe27b447-4a59-363e-b1fa-03f5ac643521 | -3.23966 | -45.97931 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6a5996fa-c009-3e00-bef6-2d484415c341 | 1.78378 | -55.92076 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cbf4cd55-a21e-34b7-9efa-7f0360695e7f | 1.82158 | -55.71147 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| df1acb20-0f56-3384-b582-9eb2e751c1a0 | 1.73509 | -55.79447 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| bb1d58a0-d58e-3f75-8bba-3ec10a2b2234 | -3.43237 | -42.46589 | 2025-10-17 04:17:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2cf222fe-7d34-3427-9e75-875509727633 | 1.82987 | -55.70597 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4859e41a-04cc-34da-a8eb-75e425b8b06d | 1.02704 | -51.10591 | 2025-10-17 04:17:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0836d52-2997-3bdd-88e9-aa966957ff3e | 1.83913 | -55.69057 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 95e55d8f-c717-31ae-8d33-1c50bccd2ded | -3.23115 | -45.96655 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0f17232-2e53-3756-8b63-2c7f337dd414 | 1.72505 | -55.80825 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4f4e9a68-8a0f-36cc-9a31-c36c3df562a3 | -3.53553 | -44.31686 | 2025-10-17 04:17:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 00a39dbd-de7a-3de7-acc7-6d212bddc6b2 | -2.60698 | -45.02481 | 2025-10-17 04:17:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 53cfa4e6-5b34-3d44-843a-21437fb08adb | -2.74943 | -49.38869 | 2025-10-17 04:17:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 8e060370-b438-3519-9462-945ed11a69dc | -2.92603 | -48.30236 | 2025-10-17 04:17:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2ec7feb6-5fd4-3d69-af2e-70c4b864bf39 | -3.2425 | -45.98358 | 2025-10-17 04:17:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40446d57-b161-3ff5-aecd-1a07ba9084a3 | 1.73318 | -55.78219 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 48004ca7-d371-33e6-a2b8-72b40dc30d12 | -2.60308 | -45.02783 | 2025-10-17 04:17:00 | NOAA-21 | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e066ad51-168c-3da2-85ca-48ee83a9a569 | 1.77108 | -55.7442 | 2025-10-17 04:17:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6d254c8d-d679-3a88-9075-d997087f3a8c | -2.4449 | -52.24958 | 2025-10-17 04:17:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7dff3ae4-3f5b-3fe8-8aee-3ddd8bc79eb6 | 1.80033 | -55.9374 | 2025-10-17 04:17:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 69819917-8419-3868-818e-83f6a618bbf9 | -4.17145 | -38.48112 | 2025-10-17 04:17:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f31dc706-7b28-3bb3-8cb7-17b64731e7bb | -1.95824 | -48.11258 | 2025-10-17 04:17:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80687fc3-ff85-3dbe-a79a-d637a74013e2 | -7.46601 | -42.65987 | 2025-10-17 04:19:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 645bb538-665a-3a52-a937-0c6fff14541c | -6.60356 | -44.80295 | 2025-10-17 04:19:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d1764f38-d294-396f-ac12-02c993225e37 | -4.52474 | -46.40358 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c860679-fbdf-32bf-872d-5db90240a0b0 | -5.85648 | -43.87889 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 664895f9-28be-3079-89c8-ff1f91c02d2e | -5.2132 | -46.18717 | 2025-10-17 04:19:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14687005-c06a-372e-9b96-781178585072 | -5.21751 | -45.242 | 2025-10-17 04:19:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 488c26c1-853d-3ce4-8e0b-df5716ec2a05 | -10.64558 | -45.21996 | 2025-10-17 04:19:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6eb87dfb-0b2a-33bb-9a2d-93c82f22d0b3 | -7.42897 | -44.75015 | 2025-10-17 04:19:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c3da75e2-47bd-3b76-a75c-5061577ae1ba | -7.35969 | -41.9056 | 2025-10-17 04:19:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| f10d146d-af56-330f-b6a7-806684eefc6f | -6.58959 | -44.37365 | 2025-10-17 04:19:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d7919500-67d3-31d1-92b7-81171a15602e | -4.8355 | -45.65823 | 2025-10-17 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa1e0928-8b6e-39c1-9af8-e7e2b1c6e48d | -10.51187 | -43.36222 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ee1e077-11f6-33cb-af0b-83f02653643d | -10.44643 | -44.57202 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb7b3544-d23a-3566-bd5a-95c4b845ee4a | -11.14514 | -45.0698 | 2025-10-17 04:19:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1cb748aa-8da3-349b-8e19-3b0a825625f9 | -8.38814 | -46.24245 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ab8f7838-2d5e-3d1b-9e3e-95655baa2fb4 | -4.57933 | -46.30451 | 2025-10-17 04:19:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acb6650f-0823-3599-bb45-0d1000fe5c57 | -6.36827 | -41.48624 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 919ef7f4-3d29-3ecb-ba4a-e377e73a8dac | -11.44686 | -43.48237 | 2025-10-17 04:19:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb0b7336-9a6a-3db3-a94a-aee0c308a09c | -10.13804 | -44.54198 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5f7f5004-8b3f-3688-890e-a2bab5d750d9 | -8.33873 | -46.2343 | 2025-10-17 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b8ca2410-f052-3a62-8f7e-3dd14734b8ce | -4.12211 | -50.71461 | 2025-10-17 04:19:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dfb8e42b-3758-3d7b-9e7e-b3a4f152a92b | -7.30684 | -43.95934 | 2025-10-17 04:19:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 90a65a66-06bd-351c-bd7a-830f2ddd55e3 | -11.48645 | -44.19696 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47910408-c198-34f6-a288-9619d954483a | -4.31325 | -48.08374 | 2025-10-17 04:19:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4520e332-24f4-3be3-885d-7898d4a503cf | -5.84655 | -43.87734 | 2025-10-17 04:19:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99618c05-4a7d-3cf0-8ae2-cb82adfea24b | -6.4919 | -39.59599 | 2025-10-17 04:19:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8517dc3c-c56b-3082-a45c-7f3a8994e905 | -10.43118 | -45.02419 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 632b3330-20bd-3067-b1ca-878cdde9f8dc | -11.48419 | -44.18908 | 2025-10-17 04:19:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2691e4e5-0f14-3304-ac44-dede962c4bcc | -5.93466 | -43.33145 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6842527-0a8a-373e-ab69-8ec932d39b8d | -4.83494 | -45.66178 | 2025-10-17 04:19:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df0e2242-5c09-38fb-a751-479c4a91478b | -5.40353 | -45.63528 | 2025-10-17 04:19:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e6884fc-3bc9-3593-84e3-744e3f241fc7 | -8.22047 | -43.98953 | 2025-10-17 04:19:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4b2cb931-f3c1-30f5-ba86-4f1ff904c2d6 | -4.29587 | -41.73343 | 2025-10-17 04:19:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9c81ac37-493f-3422-b980-34dad9941dac | -10.23052 | -49.86857 | 2025-10-17 04:19:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e966471e-d288-36f2-a56d-8f23bf6f7936 | -10.43558 | -45.0177 | 2025-10-17 04:19:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 968b3e0c-4007-31e0-b1f6-454d3510bc21 | -9.06353 | -48.84764 | 2025-10-17 04:19:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1afdce18-babd-3e70-bab3-b2f46ed6fc22 | -9.40922 | -48.64485 | 2025-10-17 04:19:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7d0b2fd6-c516-3a6c-b32e-7345ccea8af6 | -6.13683 | -41.75381 | 2025-10-17 04:19:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 395532f4-f569-3cca-83a1-d50d3321c0e4 | -9.26158 | -45.26232 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00b3d416-0bd1-38ce-b8a9-c089de63dea5 | -9.26271 | -44.35409 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a658cc2a-24b1-323d-bd89-42b69daadfe3 | -6.37435 | -41.46998 | 2025-10-17 04:19:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 27ae63cd-798f-3781-b4e3-e76b615997c0 | -5.47466 | -42.94273 | 2025-10-17 04:19:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 40316436-ddab-3d35-a2b6-2f2ec678d5e0 | -6.52034 | -46.51397 | 2025-10-17 04:19:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 85008164-3427-3fff-b0d4-c1b1c2dced8e | -9.08993 | -48.0293 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 713cffcb-c08d-3d95-959f-05e00041b285 | -6.93527 | -45.14212 | 2025-10-17 04:19:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 00a765c8-8e64-36ad-a345-8c9db3502079 | -8.11 | -41.144 | 2025-10-17 04:19:00 | NOAA-21 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a3491a15-80a6-31b0-8570-c58afe7f11d1 | -4.96276 | -44.95954 | 2025-10-17 04:19:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a38e564-5b9e-350d-8158-ed85fe30b11e | -10.13875 | -44.58183 | 2025-10-17 04:19:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9a9de42c-e7c6-3419-87f5-a678057e2c52 | -8.36832 | -44.77183 | 2025-10-17 04:19:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78633169-6f66-36f1-a982-ccd0f76297e5 | -9.8821 | -49.1191 | 2025-10-17 04:19:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d95913fc-0c57-3222-913e-713392ac7c35 | -5.77769 | -42.45987 | 2025-10-17 04:19:00 | NOAA-21 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 6a10fc06-f4a0-3332-8c9d-91c77cfc7a05 | -4.56111 | -46.61953 | 2025-10-17 04:19:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README37.md)
