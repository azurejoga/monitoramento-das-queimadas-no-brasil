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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 32a9a31b-cbc2-3cb3-ba88-99daa59e02fa | -7.61708 | -43.57862 | 2025-10-30 05:55:00 | AQUA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c0d75396-f941-3d03-915f-69c9a8d2f399 | -7.29821 | -44.97185 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b110964d-a3af-340b-948f-717c5c24296f | -12.30658 | -50.25091 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0a74af06-ddac-3c5e-970e-a98491a44d1d | -4.26091 | -43.71466 | 2025-10-30 05:55:00 | AQUA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 79.7 |
| ef35bcbd-4f87-3104-9285-51322dc27e66 | -10.74075 | -44.74504 | 2025-10-30 05:55:00 | AQUA_M-M | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0a1a80ea-96ff-3299-9b42-c86385ca0439 | -8.32577 | -47.92717 | 2025-10-30 05:55:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| d9b9609b-9532-3202-a341-e7fb6b15fbbb | -12.51835 | -50.54844 | 2025-10-30 05:55:00 | AQUA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 6717e1b9-ef86-30c5-8ad5-a613d1a0cb22 | -8.15468 | -44.80358 | 2025-10-30 05:55:00 | AQUA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f52436dc-6922-349d-b392-d9eaf9cb35d8 | -7.95534 | -46.73266 | 2025-10-30 05:55:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 3acd0110-a0e5-3576-a8b7-857856067450 | -12.91199 | -45.046 | 2025-10-30 05:55:00 | AQUA_M-M | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| eb1a0124-0bbc-31ed-a8e6-c9acdb59d47a | -8.72113 | -46.5007 | 2025-10-30 05:55:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.1 |
| c661b9c1-c76f-3613-a8d9-66e21e18783b | -7.95389 | -46.74212 | 2025-10-30 05:55:00 | AQUA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4e7c6c60-ed8c-324d-8bd8-48147d084076 | -6.05532 | -44.15238 | 2025-10-30 05:55:00 | AQUA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| eab76df1-cdeb-3b62-9a83-f38c2e1682f9 | -4.84671 | -45.4188 | 2025-10-30 05:55:00 | AQUA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d552b0fb-6881-34d1-b115-f7edac32c9c7 | -14.31847 | -46.52657 | 2025-10-30 05:57:00 | AQUA_M-M | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 196d42e9-2ea8-32da-8435-9404a4bc0202 | -13.36695 | -54.31112 | 2025-10-30 05:57:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 25.3 |
| a8bd2dfd-72cb-3b0c-93fe-64923668ac7a | -14.26635 | -47.30199 | 2025-10-30 05:57:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 052cd130-e328-351e-a32b-c674a8695e3b | -13.3764 | -54.33924 | 2025-10-30 05:57:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 0f2dae75-e639-3c91-8a6e-de3b586fe422 | -13.37923 | -54.30574 | 2025-10-30 05:57:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 07f653bf-b134-3c94-8b43-1c65a52f3da0 | -13.57043 | -49.58228 | 2025-10-30 05:57:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 676294cf-718c-353d-8a3f-54363acb6254 | -13.56242 | -49.56947 | 2025-10-30 05:57:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 123f39ac-73ce-3f73-83c1-91025242e02d | -14.24434 | -47.31112 | 2025-10-30 05:57:00 | AQUA_M-M | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 18.6 |
| e6aff430-ee48-3db2-a35c-dcc8f368f98c | -14.28436 | -42.3367 | 2025-10-30 05:57:00 | AQUA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 55.6 |
| 489b34a2-2f05-36bc-b03f-6014f3ad2230 | -13.57224 | -49.5712 | 2025-10-30 05:57:00 | AQUA_M-M | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| acb04cbd-206a-3234-9323-3a4ec5b738f3 | -13.38113 | -54.31364 | 2025-10-30 05:57:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 543803e8-2648-373f-a64b-5e6099744453 | -14.28617 | -42.32303 | 2025-10-30 05:57:00 | AQUA_M-M | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 48.8 |
| 5bdf8c75-d7e1-3284-ba40-2100ac9cbd6a | -14.48603 | -51.49547 | 2025-10-30 05:57:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1954005c-b7d4-3c62-9ceb-dc1a79ddce90 | -14.4835 | -51.51041 | 2025-10-30 05:57:00 | AQUA_M-M | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 70d2e3d4-f1cd-354e-9f81-ba1d9fd23f27 | -3.7867 | -43.9011 | 2025-10-30 06:00:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f5cb4942-b7c4-315e-acd3-e2ac46df516f | 0.8364 | -59.31799 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06cfd2d3-5f0c-3c5a-aa4d-ce7f8be0ab9f | 3.14169 | -60.69643 | 2025-10-30 06:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 117cc708-f62a-3456-b22f-8f165acfe829 | 4.16289 | -59.85858 | 2025-10-30 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc06d8aa-3507-3ba5-bc67-478f7d8df72d | 3.1422 | -60.69948 | 2025-10-30 06:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46b0d455-9d26-32b8-814f-2e41334bd949 | 3.62723 | -61.04788 | 2025-10-30 06:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d36080c9-5d24-3d8a-969b-d4f04a9ec649 | 0.84199 | -59.3252 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 24a22b69-a234-3f2a-976c-dedc359754de | 3.62222 | -61.04869 | 2025-10-30 06:03:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e9921a32-5318-39c4-9930-fcd0d62e62e1 | 4.48866 | -60.72807 | 2025-10-30 06:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ba9d16-1736-3f46-9cd5-4d40cca5de72 | 0.44366 | -60.48072 | 2025-10-30 06:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e76231b-a3a2-3bf6-9ed5-5e3309101302 | 4.4881 | -60.72472 | 2025-10-30 06:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4d13c2f9-a3e1-3d5d-a725-24f5dbf96555 | 0.84361 | -59.32547 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 575106fa-1e4b-3a28-a825-73e3001e1ba7 | 0.83612 | -59.32612 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 817fac22-e86c-3b91-b2d5-3454d2cc2433 | 0.83051 | -59.31883 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f5208081-8941-3c34-b8c8-3c7befeaaaf3 | 4.15746 | -59.85925 | 2025-10-30 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ad07623a-bda4-3357-a0d9-13f0babeb596 | 0.83542 | -59.32192 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 10b801c2-d712-3c6e-9227-7c3481e349f7 | 0.83472 | -59.31767 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e4aa028b-b4d7-3462-88e4-68f4b67bad25 | 0.44914 | -60.47984 | 2025-10-30 06:03:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb95459a-9d60-3a18-9d54-f17162d155c1 | 0.83707 | -59.32224 | 2025-10-30 06:03:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0489fc7e-3f1d-3a46-95eb-66ee86365d65 | 3.14689 | -60.69575 | 2025-10-30 06:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 141263e2-d0fe-3874-987f-08fd9515ea3c | -17.1444 | -41.938 | 2025-10-30 10:40:00 | GOES-19 | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 149.3 |
| 9bd90614-b471-3d75-89aa-1efb759e7fda | -12.93278 | -42.04568 | 2025-10-30 11:19:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 39.4 |
| c3bfcce7-3734-35a6-92f4-01a3c39c6fc4 | -6.46875 | -36.24 | 2025-10-30 11:19:00 | TERRA_M-M | PICUÍ | PARAÍBA | Brasil | 2511400 | 25 | 33 | nan | nan | nan | Caatinga | 15.8 |
| 061a5bce-86f8-3a4a-8254-069d0b5d6582 | -6.96563 | -38.13489 | 2025-10-30 11:19:00 | TERRA_M-M | SÃO JOSÉ DA LAGOA TAPADA | PARAÍBA | Brasil | 2514206 | 25 | 33 | nan | nan | nan | Caatinga | 15.7 |
| ea4b3672-d84f-3de7-aeb4-7a4705303dbe | -7.61527 | -43.57701 | 2025-10-30 11:19:00 | TERRA_M-M | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 56f593df-3d98-35b2-bd1c-dfa649b2b5f4 | -6.92345 | -35.3388 | 2025-10-30 11:19:00 | TERRA_M-M | ARAÇAGI | PARAÍBA | Brasil | 2500809 | 25 | 33 | nan | nan | nan | Mata Atlântica | 17.4 |
| e4910bd2-3b24-3fc1-8b5e-24ff3effcb32 | -6.91533 | -42.25876 | 2025-10-30 11:19:00 | TERRA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 39.0 |
| 775ede05-e3b6-3c44-9a5a-13283d2d88aa | -7.50168 | -37.27238 | 2025-10-30 11:19:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 45.6 |
| 4bd7599b-faf5-35c0-a541-8e5b9f6c8661 | -8.628 | -39.67284 | 2025-10-30 11:19:00 | TERRA_M-M | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 51f0fe1c-3825-3688-9f0d-f7a8befea8fc | -12.01568 | -42.47973 | 2025-10-30 11:19:00 | TERRA_M-M | BROTAS DE MACAÚBAS | BAHIA | Brasil | 2904506 | 29 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 3a996095-5ecc-37df-82e8-aa0a4bf91f3a | -7.93698 | -39.55833 | 2025-10-30 11:19:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 5ae99926-8981-3bba-aef2-55b0781f2917 | -12.92778 | -42.02493 | 2025-10-30 11:19:00 | TERRA_M-M | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 58.8 |
| e7a0498c-636a-3719-aa9c-83b781345804 | -7.93383 | -39.57784 | 2025-10-30 11:19:00 | TERRA_M-M | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 33.3 |
| 06e2e912-8d20-3142-bdc9-5193c2c5ea86 | -12.84078 | -43.45061 | 2025-10-30 11:19:00 | TERRA_M-M | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| f4de3d5b-e18d-3679-a63a-faeb1029b9d8 | -7.9339 | -39.57085 | 2025-10-30 11:19:00 | TERRA_M-M | SERRITA | PERNAMBUCO | Brasil | 2614006 | 26 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 0d1f9a88-361a-3802-84b7-b02f8794dc0d | -16.65536 | -41.76781 | 2025-10-30 11:21:00 | TERRA_M-M | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.4 |
| 2bb72278-dd44-3d2f-8ee8-42375654b311 | -17.15344 | -41.93771 | 2025-10-30 11:21:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 35.3 |
| 20a5b377-e3c8-3448-bff4-841a43085ef5 | -13.63195 | -41.56562 | 2025-10-30 11:21:00 | TERRA_M-M | JUSSIAPE | BAHIA | Brasil | 2918605 | 29 | 33 | nan | nan | nan | Caatinga | 90.4 |
| 3ebae054-61f4-3c99-8f02-5fa1af88d9a6 | -13.5876 | -47.3438 | 2025-10-30 12:10:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 119.5 |
| 0b8eb73b-8475-3fd6-9067-f15f009ca88f | -13.2271 | -47.0387 | 2025-10-30 12:10:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 2c285d01-8627-3afe-971e-8b87dc438362 | -13.5876 | -47.3438 | 2025-10-30 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 7889f8ea-e580-3cf2-9407-f5f3de338f36 | -13.5686 | -47.3242 | 2025-10-30 12:20:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 26a7e828-47e9-3a57-b846-7bb7428d5435 | -13.5686 | -47.3242 | 2025-10-30 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 130.6 |
| 06e9e4bb-c3d2-359b-a46f-ef979f4b6e5e | -13.5876 | -47.3438 | 2025-10-30 12:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 122.0 |
| e51b0759-6535-3b89-906a-cc75d400e2af | -13.5876 | -47.3438 | 2025-10-30 12:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 94.3 |
| 9608d5f2-c8be-36b8-a603-37a54e098d41 | -13.2271 | -47.0387 | 2025-10-30 12:40:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 9632a4e8-314a-3cbb-af89-f2e1633af704 | -3.7867 | -43.9011 | 2025-10-30 12:40:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 109.8 |
| 39eefdee-c0f4-3d97-98f8-ad299f09d0d4 | -13.5876 | -47.3438 | 2025-10-30 12:50:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 2e3ad4fe-d284-3c0b-ac46-dd59a7c018c8 | -3.7867 | -43.9011 | 2025-10-30 12:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 122.2 |
| a270abd2-d61e-3a95-8946-201e5f583601 | -4.2731 | -43.7139 | 2025-10-30 12:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 172.1 |
| 6d387c9e-bf3d-31fc-ba1c-07718e1b8de2 | -3.8054 | -43.9002 | 2025-10-30 12:50:00 | GOES-19 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 52d095e0-473d-331c-a74f-cac5ebde8ec9 | -4.2544 | -43.7149 | 2025-10-30 12:50:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 100.6 |
| fe440d9b-a726-3ce9-9965-0c5f8dd745fb | 2.07845 | -50.85692 | 2025-10-30 12:53:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 22.5 |
| c5d8763b-11cf-3a4c-9370-a31d717dd6d3 | 3.69067 | -59.86393 | 2025-10-30 12:53:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 13.5 |
| 9a25169c-6465-3e16-8ae4-359948ffa453 | 3.69264 | -59.87776 | 2025-10-30 12:53:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 14.3 |
| fdf8e973-f6f6-30b9-ad8f-fc4b7edf7f04 | 3.69509 | -59.87144 | 2025-10-30 12:53:00 | TERRA_M-T | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 29.3 |
| 855cab2a-5e3f-3b68-b2c3-2ecc983673c0 | 2.08065 | -50.87204 | 2025-10-30 12:53:00 | TERRA_M-T | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3dfcb667-ad6f-3705-bef0-1bee65391c26 | 1.62314 | -55.66891 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fa67178a-c2ce-3be7-92ab-97bc4d84a41c | -1.46407 | -49.45058 | 2025-10-30 12:55:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 34.0 |
| 85c4e2fe-7360-317a-8a78-9bdd347cb847 | -1.51164 | -54.53518 | 2025-10-30 12:55:00 | TERRA_M-T | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 4ec91493-418e-3121-b839-662c60d9796a | -1.45634 | -49.44387 | 2025-10-30 12:55:00 | TERRA_M-T | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 6023772e-a022-3419-9bce-039c9caae1e4 | 1.46399 | -55.72133 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 1bf9554a-79bb-3cc8-85c7-b07406e4ade2 | 1.77925 | -55.6765 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 5d618657-3886-3739-b2ee-2a423452aadc | 1.78679 | -55.66655 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 451ae8b1-37df-3842-b9b6-8eff56f8533f | 1.10329 | -50.72244 | 2025-10-30 12:55:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 81695ed5-6c52-3c5f-b292-11357e3b9b3d | -1.35125 | -55.91927 | 2025-10-30 12:55:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 17d29e03-9b59-3b2e-bb0b-6467477be36e | 1.61505 | -55.69389 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| f0a7460d-8e8d-312c-a823-491b577f90ac | 2.1553 | -55.78636 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 425b34a6-0a67-3157-ae58-58b9e55594e6 | 1.67338 | -55.64412 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 91866a1e-59ca-34b2-bac6-0bc7455837c1 | 1.60501 | -55.68638 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 7042ce58-bfb4-3094-8b39-f800d6d73a88 | 2.1691 | -55.75774 | 2025-10-30 12:55:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a4c5c715-bcf8-3020-bc40-1717e9400571 | -5.6162 | -47.12635 | 2025-10-30 12:57:00 | TERRA_M-T | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |


[Clique aqui para ver as próximas entradas](README68.md)
