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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eada0f5-f36a-3b5c-87d0-dccb4b3b9623 | -7.22823 | -45.31722 | 2025-10-18 04:49:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 70be441c-5272-3321-b914-a755206cfce4 | -5.07055 | -49.85009 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fd9486a-6d3f-3f03-9dc4-cf4f3d4fffc6 | -8.23287 | -44.0065 | 2025-10-18 04:49:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9b0badb3-1df1-317f-b945-29844c6d5933 | -3.85355 | -41.56855 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6d61bf8d-b379-324a-9296-f2e0c7bfa6bb | -2.71053 | -49.86262 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29c335f4-1d23-3863-b512-6df9b5d83682 | -3.0011 | -52.0073 | 2025-10-18 04:49:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d3b3919-072a-352c-9233-43e2738a8f7a | -7.43804 | -43.75504 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d9f6aa8c-520c-3e6a-9772-a84467dcf4d0 | -2.70374 | -49.86157 | 2025-10-18 04:49:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4a7279e-6c51-390a-9828-615acd36eadf | -8.38668 | -46.23206 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f0cddbde-4379-3dd1-bf44-003653ff4e94 | -5.06003 | -45.85918 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 00f0d0e5-d027-32df-a5ac-85b1bc992103 | -5.23726 | -49.85445 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9a4ccfae-96c9-35ba-a7e9-6d6dd1aa5581 | -8.94475 | -46.57676 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| fce1fe37-4a51-3060-890a-217a4741d959 | -2.12201 | -56.611 | 2025-10-18 04:49:00 | NOAA-20 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3ed79402-8f11-3247-a933-84004c782900 | -4.03892 | -51.15687 | 2025-10-18 04:49:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 670f0e93-1e30-328b-9a47-5ffe37b67e00 | -4.25411 | -48.37289 | 2025-10-18 04:49:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8c47033-f74e-3a55-97e1-01a6bd613373 | -8.53449 | -49.59919 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68aa8878-d83f-3744-b455-e61c5fb7c80e | -7.39914 | -44.75275 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 17831d15-78ad-3f61-8bc3-83e967d14950 | -9.77868 | -43.87174 | 2025-10-18 04:49:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 21aada91-f9d2-3de3-b01e-d07a2436287a | -4.98898 | -49.76804 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3ea920ec-a66e-3667-94df-88e0baf18c3c | -7.16062 | -46.21258 | 2025-10-18 04:49:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 43f2f699-b0fc-3ecf-aea2-956abeb74b1f | -3.99774 | -45.50655 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 180fabf2-4a8c-3007-9b22-e4da93d183ef | -3.16044 | -49.16537 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6b6754e-ae15-3223-8015-b7c8aa99b2fb | -5.24498 | -50.95983 | 2025-10-18 04:49:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b7d343cb-007c-313c-bc90-2b7dbec201e3 | -3.38093 | -52.48497 | 2025-10-18 04:49:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92e7748a-b28e-36c6-bb96-a995682542fe | -9.24565 | -43.76149 | 2025-10-18 04:49:00 | NOAA-20 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 05637e67-3c50-3331-8e2f-b7dba6b75c16 | -7.35442 | -43.85759 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03963701-e7d5-38b9-9d8e-8d7d1598c459 | -7.36244 | -44.23493 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 50d87af2-295d-3294-ab8b-0ce57e310026 | -6.32617 | -44.30713 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fb66099f-4c46-34fa-8b4a-3d85025c779c | -8.53939 | -50.08243 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0209e28d-f59a-3f78-a5fd-ba3caf652c60 | -7.60684 | -45.85136 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2740a044-f334-37bd-9041-5ea17bbbdd4b | -2.87512 | -50.7372 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c0bdf68-1362-3194-96a2-a0f29c4f6544 | -5.45631 | -45.41206 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22a7d282-dec4-32b2-9fc7-54969f9f85c5 | -4.45798 | -43.23642 | 2025-10-18 04:49:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| befbe849-44b6-314a-b9d7-5811ecbfc340 | -2.73851 | -49.39226 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 849083ac-4f4e-38a2-aa43-bb780c9877c8 | -8.33926 | -49.97204 | 2025-10-18 04:49:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74b07601-bf02-378b-a583-11545828a0c6 | -4.53254 | -50.42972 | 2025-10-18 04:49:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be2adcf6-48dc-32f3-8319-070da931cf0f | -5.84992 | -44.34085 | 2025-10-18 04:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 796b65f7-3326-3da6-8cd1-080b2e049a43 | -5.10023 | -56.15716 | 2025-10-18 04:49:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c2b68c58-5262-3407-927a-8465b332c38d | -4.99051 | -43.85579 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ea06230-bc4f-329a-9f57-159350183be4 | -3.42155 | -51.66834 | 2025-10-18 04:49:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68d71bd2-f526-310f-8288-43feaf3ffc54 | -5.12878 | -50.42351 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f18e33c6-d4cd-3e3b-a7be-85c30dd60a01 | -9.24517 | -43.76503 | 2025-10-18 04:49:00 | NOAA-20 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d71b19c0-9dcd-3924-ace9-b36a35ff12d4 | -6.14279 | -44.30047 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 287a9851-4251-36b6-a612-f1c9b4a68682 | -6.29174 | -44.72057 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 027e0448-3369-38b6-902e-968171857726 | -5.71333 | -46.51313 | 2025-10-18 04:49:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3c1c7bea-2289-309b-8b43-195747eb913a | -3.1419 | -50.2464 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| eb2f32cc-273e-3871-8bed-9873fdf75c22 | -7.75217 | -42.50949 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b864df5e-ae59-3d2f-9acc-fd055eb42a09 | -3.13008 | -50.21144 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 379b6df4-f29a-3c15-a5c4-c951781bde16 | -2.80496 | -48.66421 | 2025-10-18 04:49:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 54e0316a-dbbc-36f7-9571-a65a20739146 | -6.356 | -45.75609 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a1cb9c44-218f-30af-ab08-e920893e714c | -2.74197 | -49.39278 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3191c2b8-33ab-33e6-9d6e-2595a44e3e00 | -8.6971 | -47.0647 | 2025-10-18 04:49:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 955a4e83-ef0c-3da2-a965-8a1282946931 | -8.86029 | -49.89354 | 2025-10-18 04:49:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 456e1726-31c9-3aca-a080-6d7809eb68da | -3.1492 | -50.24387 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 80e88756-7efa-3bd9-9fed-c047b04ecf3a | -1.514 | -55.53933 | 2025-10-18 04:49:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7cb83f34-2cea-30da-a3ce-cf11c181a677 | -3.75608 | -49.03714 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5f6c41c7-a5d5-3a1e-aa1a-c2043ffe4e2d | -7.14424 | -46.41553 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 007971f5-a1c3-33fb-b6fc-a5c0290ccda8 | -7.76632 | -42.4912 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 41a58054-a8ae-389f-866a-0d61ea8bed70 | -3.86315 | -51.90686 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 20c6b070-715d-33e2-9a4c-ce136e054d1f | -8.36633 | -46.19891 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5b9967d0-50bb-3ba1-8ffa-7913b7757262 | -6.36875 | -45.76309 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4a86acb8-192d-34b3-ab06-05653299ced4 | -5.11692 | -49.2642 | 2025-10-18 04:49:00 | NOAA-20 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 924e2df7-f97a-31ba-a1b7-b82a5217ed05 | -8.44615 | -44.17531 | 2025-10-18 04:49:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7dd23b01-8444-36ee-9000-790d0c4b05a7 | -6.95923 | -47.12165 | 2025-10-18 04:49:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa5c3b47-2af3-352c-9cee-0080eed0faae | -3.13797 | -50.24945 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a0000e5-3414-30de-80ff-57b083cbc000 | -8.60845 | -40.19452 | 2025-10-18 04:49:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c56d9c34-66a8-38de-b19c-01c0583cc650 | -4.93978 | -49.76433 | 2025-10-18 04:49:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 213765b1-6632-3d3e-a8b2-80ee50b854ec | -5.33784 | -44.99837 | 2025-10-18 04:49:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a349087e-6220-3b38-a141-99a88b327410 | -6.36613 | -45.78086 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 266a10ea-0cbb-33c1-8fba-64c2be740d80 | -4.84547 | -46.72007 | 2025-10-18 04:49:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c31b62d2-1585-3e44-ba2b-3e63d52975a6 | -5.89261 | -44.70984 | 2025-10-18 04:49:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ca637c02-b527-314a-aab8-b1ce27b27039 | -6.88594 | -45.45885 | 2025-10-18 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d62ee3a-2593-3eef-affa-d8cf0f9e022f | -6.89058 | -45.45948 | 2025-10-18 04:49:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d3213ea8-9e19-3ddb-a11b-4a85ffa77eba | -4.94552 | -45.63255 | 2025-10-18 04:49:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd57ae33-7e94-3d7e-aab2-b75edbd5ed40 | -3.85296 | -41.57252 | 2025-10-18 04:49:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8ef4a91d-74cd-3fe6-b27e-a41717939138 | -2.86682 | -50.74664 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d0b48be2-403b-3715-8e53-08c837110068 | -5.88592 | -43.92353 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78bb11e9-1936-315d-a424-b04f993a4207 | -4.00831 | -49.02082 | 2025-10-18 04:49:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 206d254c-a166-3851-a16b-e737a5f5400b | -8.36255 | -46.24117 | 2025-10-18 04:49:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 69a36132-f42a-38fb-8467-be2c7f78857b | -2.87344 | -50.72622 | 2025-10-18 04:49:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ab9da718-8d75-359e-b5af-e43adf3ff995 | -5.8514 | -44.34243 | 2025-10-18 04:49:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f13d663-22eb-3893-b55a-fd83ed7d1091 | -8.10699 | -49.7592 | 2025-10-18 04:49:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d0ab11a1-1f98-35f0-84cb-d441953e7720 | -3.6467 | -45.26364 | 2025-10-18 04:49:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f66dc0f7-f918-3e0b-9a9c-819af450f3f7 | -6.84307 | -41.71714 | 2025-10-18 04:49:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 096e136d-63cb-36ee-8d57-72db35944e80 | -7.36205 | -44.23781 | 2025-10-18 04:49:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7f14624-df1a-3691-876d-456ceb731021 | -6.84131 | -42.4234 | 2025-10-18 04:49:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 58f18cde-e513-359f-910b-7d0248d977d0 | -5.8974 | -43.90404 | 2025-10-18 04:49:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e8f2f28a-4094-3106-9cf0-24d59d19056b | -7.34318 | -43.86211 | 2025-10-18 04:49:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| cfc65582-e54e-32be-aad3-b74b62cdd17c | -7.44585 | -42.68802 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8547265a-b89c-3e7d-bf5b-b13598f870c2 | -7.43988 | -44.74737 | 2025-10-18 04:49:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 491bb05a-ef9c-3a85-8513-89aa3c0c34b7 | -3.08444 | -49.49077 | 2025-10-18 04:49:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9cd8cca1-4ec0-330a-acb5-fea2a952dd80 | -7.48487 | -47.03223 | 2025-10-18 04:49:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd03b265-4fbe-3c68-83ad-e1a97a769599 | -6.00753 | -45.41718 | 2025-10-18 04:49:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4967fdf2-26ed-3a01-94e8-d2fe212fe64b | -6.76329 | -56.86595 | 2025-10-18 04:49:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21f5ea4f-a48e-3e44-8589-e1e336e9dcde | -6.23599 | -44.15178 | 2025-10-18 04:49:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffec611f-107c-363a-9d95-d9be986bdd70 | -4.97262 | -48.36531 | 2025-10-18 04:49:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbc30aa2-0c48-351d-a431-924dae3437fc | -8.27277 | -48.00587 | 2025-10-18 04:49:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 616f292a-0d33-3ab9-ac74-75d6b6836f4e | -4.9901 | -43.85863 | 2025-10-18 04:49:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b9f588b-444d-3665-a766-ded49a95a57f | -3.79033 | -51.76564 | 2025-10-18 04:49:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 648d7f78-1e31-3aa7-ad8d-086b3fd7922c | -6.17846 | -44.86166 | 2025-10-18 04:49:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README77.md)
