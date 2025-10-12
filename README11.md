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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c998e7d-651f-320b-827b-86a64b6fbd34 | -11.49855 | -43.49968 | 2025-10-12 03:23:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 33df215e-a4f6-3e98-bcd9-b36ee3df83ed | -11.25304 | -41.89794 | 2025-10-12 03:23:00 | NOAA-20 | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 676ee568-5377-3253-9154-70fbafc03251 | -13.39037 | -41.33154 | 2025-10-12 03:23:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 78470d2b-4289-3f64-adae-a414f5668e06 | -11.71942 | -44.29168 | 2025-10-12 03:23:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b80af56c-d468-3365-89e6-05b067f1e270 | -13.38783 | -41.33186 | 2025-10-12 03:23:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 052dc440-0131-306f-b57c-3bd666971bd5 | -10.76507 | -44.1084 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9bd9fdf-7f58-33b7-a336-c87e528d0af0 | -10.14681 | -44.55647 | 2025-10-12 03:23:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b8b9840c-626e-3d91-8470-2a2c0cc99cd1 | -14.01423 | -43.48914 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| c574ea76-091f-3230-be9a-f043f99f20af | -14.02025 | -43.49047 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 74848a9f-3b72-32fa-ae0a-3440efdc8893 | -10.14528 | -44.56392 | 2025-10-12 03:23:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ffd1e6d-7bea-3e49-afd0-b4233b18ddd1 | -14.02124 | -43.4858 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 1024112d-cec6-356d-99d4-40a3136c3f5f | -16.37367 | -39.02988 | 2025-10-12 03:23:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| aab700f6-8c90-345d-8db3-23854d342766 | -16.37285 | -39.03415 | 2025-10-12 03:23:00 | NOAA-20 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f3c12e17-8417-3596-bb4b-dde80252cead | -13.38849 | -41.32856 | 2025-10-12 03:23:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f9249962-1f2c-3c3c-ab98-4c5317badda9 | -14.01986 | -43.48686 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 1be69226-2fcf-35fe-b606-4b1bc94090c5 | -14.01925 | -43.49516 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7e431418-54d2-33f2-845d-0ac8a199e68d | -11.36303 | -44.00104 | 2025-10-12 03:23:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1c25c21a-ccab-33de-a143-40f754d31573 | -14.02587 | -43.48824 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| bd271c57-1030-3711-92f6-eed640b67ade | -11.36396 | -41.88367 | 2025-10-12 03:23:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 5667d7be-b2f4-312d-8ed6-78f6f68115f1 | -14.02725 | -43.48716 | 2025-10-12 03:23:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 251580d7-d539-391d-ac4e-362dcde2ba66 | -11.36316 | -41.88776 | 2025-10-12 03:23:00 | NOAA-20 | IRECÊ | BAHIA | Brasil | 2914604 | 29 | 33 | nan | nan | nan | Caatinga | 22.2 |
| ad71b43b-9867-38b7-a82e-571f6b7b1e09 | -19.7691 | -42.42655 | 2025-10-12 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f38a78f9-f1d6-337e-a724-d0ec3b4b9828 | -19.78089 | -42.39533 | 2025-10-12 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 502cf303-f62c-3b29-a914-41dd06dd86bc | -19.09466 | -46.4173 | 2025-10-12 03:25:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e3375a8-f063-396a-9ee9-76fe7ae3f539 | -19.09599 | -46.41161 | 2025-10-12 03:25:00 | NOAA-20 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9b10d679-d0a1-3d58-bb49-17c73379d97e | -19.7802 | -42.39864 | 2025-10-12 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 74af6caf-1527-3105-96f8-dd3b68e00732 | -18.40099 | -46.39439 | 2025-10-12 03:25:00 | NOAA-20 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75daf659-0eec-3de7-92fc-012bf9835d1d | -17.54589 | -46.52686 | 2025-10-12 03:25:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 216104db-e161-32eb-8055-e9c1fe055b0d | -19.76407 | -42.42522 | 2025-10-12 03:25:00 | NOAA-20 | PINGO D'ÁGUA | MINAS GERAIS | Brasil | 3150539 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| d056b081-2303-38ae-b121-c8d97377015e | -17.4022 | -46.86544 | 2025-10-12 03:25:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2dab032b-1c03-3500-b3ce-d6002da35489 | -17.5392 | -46.52512 | 2025-10-12 03:25:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7aac915e-5bed-3240-b9f7-accadda95720 | -16.73553 | -43.98165 | 2025-10-12 03:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03980e73-56c1-329b-b125-74452f5887a6 | -17.5444 | -46.53329 | 2025-10-12 03:25:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 71df20a9-0f30-30aa-8993-cb4841c462ea | -18.55201 | -46.94958 | 2025-10-12 03:25:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 547b4fca-3789-3af0-9853-371d4cbe61e6 | -19.78157 | -42.39207 | 2025-10-12 03:25:00 | NOAA-20 | CÓRREGO NOVO | MINAS GERAIS | Brasil | 3120003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d0e25b89-7117-36fc-8bd0-8b5d8d3ef5b2 | -16.73634 | -43.97784 | 2025-10-12 03:25:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b22aa46-ef90-3f0e-8cce-de0c5b830b88 | -17.53773 | -46.53148 | 2025-10-12 03:25:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 08484690-a7ff-3fea-bf0b-8b25814c1fbb | -2.5423 | -47.811 | 2025-10-12 03:30:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 96.4 |
| 36d8e385-0414-3010-a277-b91867783214 | -4.271 | -46.9369 | 2025-10-12 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 44.0 |
| da21fff0-aa1b-3fe6-8c0c-64d7e350b05b | -19.5247 | -43.0642 | 2025-10-12 03:30:00 | GOES-19 | SANTA MARIA DE ITABIRA | MINAS GERAIS | Brasil | 3158003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 77.8 |
| f8139e31-3102-347e-9b0e-89a9b278ce15 | -3.5152 | -45.8634 | 2025-10-12 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 2f391275-ef50-3671-9f2b-461da1dc2b8a | -14.9572 | -46.7327 | 2025-10-12 03:30:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 3fe59f8e-01e4-394c-9e77-fbe0a7e11258 | -3.5153 | -45.8411 | 2025-10-12 03:30:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 0681965f-f882-3d14-b106-7fb2d29ef765 | -19.5459 | -43.0336 | 2025-10-12 03:30:00 | GOES-19 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 86.9 |
| ff752977-b4d4-37da-a69e-a588f4839355 | -19.5254 | -43.0391 | 2025-10-12 03:30:00 | GOES-19 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 116.6 |
| 6845702a-0a6e-3800-9e87-1d08a2182a13 | -12.2051 | -64.367 | 2025-10-12 03:30:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4a7036ea-cabe-3804-af7a-2664cb4f4f9d | -3.5153 | -45.8411 | 2025-10-12 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 09aaf428-1a1b-3cd0-94f7-ef8141225dac | -3.5152 | -45.8634 | 2025-10-12 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 74ca41e4-299f-3f63-8ef3-4138b15067ca | -14.9572 | -46.7327 | 2025-10-12 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 3af66be5-58f1-3ca0-be2b-faa34994ef02 | -2.5423 | -47.811 | 2025-10-12 03:40:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 83288ad0-963d-33a2-a3a5-d0822f57dff1 | -4.271 | -46.9369 | 2025-10-12 03:40:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 73748b2f-219d-3344-adce-bc3b74e9b002 | -12.2051 | -64.367 | 2025-10-12 03:40:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| 4ff34b99-9772-34d4-99ca-4e262cd625d6 | -3.5152 | -45.8634 | 2025-10-12 03:50:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f82da002-f5e9-3e33-be4a-481bf35e1134 | -2.5423 | -47.811 | 2025-10-12 03:50:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 215ec2cc-6e63-35cd-94a9-2a55425ef118 | -14.9572 | -46.7327 | 2025-10-12 03:50:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 100.5 |
| eb16a075-f5ba-36cc-8220-9f4a296dc442 | -14.9572 | -46.7327 | 2025-10-12 04:00:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 16e5c6e5-6fd8-32db-89da-1392cbbeecb9 | -15.6825 | -46.625 | 2025-10-12 04:00:00 | GOES-19 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 5d9f16c9-c156-3f2e-8343-64d1354ba15b | -3.5153 | -45.8411 | 2025-10-12 04:00:00 | GOES-19 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 309ada1f-ea72-3469-a39a-588a42ab2fd2 | -2.5423 | -47.811 | 2025-10-12 04:00:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| badf8be6-7dc6-3245-add5-f05c29c781d2 | -2.5423 | -47.811 | 2025-10-12 04:10:00 | GOES-19 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 9e4088e7-246f-3b74-839b-398deb9f871c | -14.3869 | -48.0036 | 2025-10-12 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 64.1 |
| f7de7da2-3e11-320f-819e-d504f098e5b5 | -14.4063 | -48.0005 | 2025-10-12 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 90.8 |
| 78b6a73f-f7be-3b48-9ce0-534d27ef2355 | -14.4068 | -47.9781 | 2025-10-12 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 20257b17-1d62-3a16-ae94-4213299cb707 | -14.9572 | -46.7327 | 2025-10-12 04:10:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 69.3 |
| 96a7e6e2-7e44-3773-bc93-081322d5b35c | -14.4059 | -48.023 | 2025-10-12 04:10:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 73.9 |
| c42417d0-42f1-3bb1-a172-cf306fa16483 | -3.51472 | -45.84581 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 4b5d0e2c-4cd3-30ea-9e4a-c7c250ecab97 | -3.61728 | -38.8022 | 2025-10-12 04:12:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2bd8d8c9-fb49-34f5-9cf3-7961fcd8f015 | -1.13758 | -47.80294 | 2025-10-12 04:12:00 | NOAA-21 | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| eca3bf8d-1d8b-3c5b-8278-57411bd95b69 | -4.42467 | -43.47018 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ecd70d43-edef-3e24-9677-25537780ef17 | -3.14247 | -44.42616 | 2025-10-12 04:12:00 | NOAA-21 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d9785915-0bf0-355b-8565-889dc4a4bce0 | -2.5347 | -47.80164 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 8587965f-4bc3-35eb-94b5-b428d43469d0 | -3.95389 | -44.2726 | 2025-10-12 04:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 775e5923-5cea-36af-a967-a30c9c6dc00a | -3.60884 | -42.75108 | 2025-10-12 04:12:00 | NOAA-21 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 446e2c98-54ab-3b15-bbd2-256fa37b9021 | -3.22109 | -50.22057 | 2025-10-12 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 87d0be9b-118c-3dfe-af48-6eb3d01c3138 | -3.5735 | -41.62482 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 13be7ce8-c18f-3820-8784-680b1d153cc9 | -3.09872 | -47.01795 | 2025-10-12 04:12:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 582eda58-2447-3330-acde-53516d61eeb6 | 0.26002 | -51.08313 | 2025-10-12 04:12:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99fe1654-ba40-30f6-892d-6e8d0bf2d18a | -2.92661 | -48.29983 | 2025-10-12 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7096c4e6-a245-3d95-a9a6-79099b46d7fd | -3.59394 | -41.62442 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d6631f85-309d-325f-8597-397893ff0885 | -4.41804 | -43.46914 | 2025-10-12 04:12:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 197dd267-aa5c-3ad4-bfdf-80da6fb5bba3 | -2.44625 | -49.37218 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 843a3b25-9912-3acf-828e-366f13f8439c | -3.53253 | -48.92509 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 895e8e56-ce96-30e0-8bca-6016150d9dba | -5.23215 | -35.59942 | 2025-10-12 04:12:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 692e7e09-e067-3ca5-80d1-217239bbebea | -3.87819 | -42.50862 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| a07ac07e-d8ad-3b4c-92bf-98b501a4ff76 | -3.50675 | -45.84891 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 9892cf83-c5ba-370f-a07d-12dd9d53f16a | -1.90408 | -51.01214 | 2025-10-12 04:12:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| acc52b67-a945-37a2-9e55-fa1cbc4225e6 | -3.82504 | -42.45455 | 2025-10-12 04:12:00 | NOAA-21 | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dc155c3f-2b9c-3f17-97ec-14a9e9767acc | -3.60559 | -41.63691 | 2025-10-12 04:12:00 | NOAA-21 | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5ffe8218-af47-3b7c-830f-164635cdc02d | -3.51336 | -45.85434 | 2025-10-12 04:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 05655eac-788c-31c0-882d-cc3b0432ead9 | -3.40348 | -46.90213 | 2025-10-12 04:12:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3bb23126-978a-31e8-b8ef-99f6b0f601f2 | -2.27105 | -47.8511 | 2025-10-12 04:12:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0ba99d0-da55-3317-b004-4aef0c8ff8d5 | -3.74807 | -44.39475 | 2025-10-12 04:12:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2df7907-6865-3619-9d26-3bda3ac62bfc | -3.53325 | -48.92072 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1da085ba-fb14-3ddf-92e0-2c5ef19a2a56 | -2.43875 | -49.36851 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68032598-8791-32dc-b64b-517509b36521 | -2.4434 | -49.36924 | 2025-10-12 04:12:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e8fbf7a-868d-370d-a9a5-59d156639904 | -3.87765 | -42.51205 | 2025-10-12 04:12:00 | NOAA-21 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 32aa6084-a19b-3f6a-bd8e-fb2456980405 | -2.53409 | -47.80543 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| cdeeed74-403a-3c93-8bcc-0f0b088dc492 | -2.71707 | -48.36083 | 2025-10-12 04:12:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2eaad683-e5cd-31b6-b887-423498621a56 | -0.90442 | -47.55087 | 2025-10-12 04:12:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e90d565e-56da-3036-83fb-42a2702f12db | -3.54138 | -48.92654 | 2025-10-12 04:12:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README12.md)
