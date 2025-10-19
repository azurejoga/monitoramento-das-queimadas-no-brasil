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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ff8e45c-3379-356f-b1ac-70fcafef7970 | -9.09854 | -48.9149 | 2025-10-19 04:12:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c6d94cf0-adc7-31bd-a32f-2e9af2118486 | -14.10921 | -42.24545 | 2025-10-19 04:12:00 | NPP-375D | LAGOA REAL | BAHIA | Brasil | 2918753 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 09a25167-5f86-37e2-a367-01be0278c24a | -8.95734 | -44.92683 | 2025-10-19 04:12:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 264ccfbd-2c2d-3ea6-aeb6-1b64ee6742cb | -9.94189 | -47.65778 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a51130d4-309b-33ff-b243-5881ddd208f5 | -10.11849 | -45.514 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7ea39844-eaa5-3ae5-a470-5888511b4973 | -9.6202 | -49.02504 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6d4e1aa-4c81-3649-bde0-b5de5fc39b44 | -9.60132 | -49.01895 | 2025-10-19 04:12:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e2744c3-abf6-3209-bd8c-2ec80526b2ff | -11.87691 | -45.45979 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 25110bd0-8536-3d6a-9336-3401185ca57e | -12.14519 | -45.06136 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ad779a53-eeac-3b0c-b6d7-655fcd11a00d | -8.35637 | -46.20683 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 737f5a1c-32d3-3bce-b61c-8decb500a19c | -8.31214 | -49.49162 | 2025-10-19 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6ee81e8-6fcb-3f2a-ba2b-14e79898a22b | -12.14582 | -45.05751 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e6465ea1-d2f1-356c-ac3a-66080cd41797 | -10.99943 | -47.91957 | 2025-10-19 04:12:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 69561320-7077-3a90-8cbf-e9b7dbf69743 | -7.44929 | -47.13202 | 2025-10-19 04:12:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ba55850-6e41-3282-8f5c-90317171cfd5 | -10.97803 | -42.29207 | 2025-10-19 04:12:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c43c5978-b0ca-394f-ba30-b471a61617be | -13.11839 | -42.16223 | 2025-10-19 04:12:00 | NPP-375D | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 0e909540-47ea-3987-8712-5b977a27b8aa | -11.89154 | -45.43764 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ecbe5dfe-21d2-3a25-84e0-491ffd500d69 | -10.5238 | -43.36354 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d615244-dfec-3efa-9917-3e980230349e | -11.4763 | -42.22289 | 2025-10-19 04:12:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| ece34102-af19-3f65-a033-4facefa1c455 | -9.22661 | -46.06477 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd9be908-0964-3448-8e36-1cbe47334220 | -10.92025 | -43.82631 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cd45fa22-062e-37ae-a769-30ceb20940a8 | -12.18233 | -40.62389 | 2025-10-19 04:12:00 | NPP-375D | RUY BARBOSA | BAHIA | Brasil | 2927200 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 40db1d0f-902f-338c-92b0-e52720c6632e | -10.8435 | -43.9364 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee48f51a-1b15-344d-8edc-5260747998b8 | -8.15706 | -44.02034 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d98f7b83-91ec-3ea7-beac-cb7f5a847841 | -13.91146 | -43.18428 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c3b80a2e-05eb-37e8-bda1-4ba3d1bbfd97 | -10.22223 | -44.06031 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6d93a3cd-8fbc-3288-b0ec-4c408fc93e32 | -8.61879 | -40.19392 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 17634202-eafa-3584-99e1-d5dd12d1e9b3 | -10.68117 | -44.54614 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dedbd414-e041-3a70-bc1f-3f45ff280493 | -13.99047 | -44.09355 | 2025-10-19 04:12:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e892764e-2ec4-3748-8dfa-d3a568b66a21 | -12.1474 | -45.06954 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9fb4c5ef-1e9f-313b-b66f-699ba5005772 | -12.24101 | -49.39359 | 2025-10-19 04:12:00 | NPP-375D | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3d15e0ae-836e-3c6a-97c8-5fbcfcfdc8e0 | -10.86833 | -43.93305 | 2025-10-19 04:12:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83cfb434-f478-3b87-8348-8b0d179ce80f | -13.6212 | -44.10674 | 2025-10-19 04:12:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| de6cea97-0855-351b-92ea-3ec8faec0452 | -11.60521 | -48.53942 | 2025-10-19 04:12:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4744f37d-308f-3061-bcb2-241f2acba284 | -9.90213 | -45.95641 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5f26b57-dd6e-3b35-b4f4-cdff4414d4d0 | -8.43515 | -44.15339 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0fabce8-bd50-3b89-a4bb-944b591c4fca | -9.70532 | -42.62353 | 2025-10-19 04:12:00 | NPP-375D | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fc958713-cec0-3dde-833b-b31f3de12594 | -11.63172 | -44.07345 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5e2459bd-a3e0-3b2b-8c06-bfa83e982d87 | -8.20261 | -43.95761 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdad5c05-c6dc-395a-88e0-4ad46b0862e9 | -10.23434 | -44.89318 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1a4d3085-b967-3ae0-a084-6a003cdec411 | -10.1505 | -44.52233 | 2025-10-19 04:12:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 92dc0621-5cfe-3b46-a972-92659d4a93f1 | -9.90285 | -45.95213 | 2025-10-19 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ee0f4750-3569-3ea5-9b1d-462945eadd9e | -11.44908 | -42.22216 | 2025-10-19 04:12:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 6ce4786d-e079-3bd3-88fd-4e528bccc7cf | -9.9365 | -47.66456 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 19f3b9c5-d3b1-305f-9c3f-f3aa3b6e5948 | -10.16257 | -42.212 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 34d67b99-9287-3cb6-b6bd-f972d2febb11 | -7.95177 | -43.86391 | 2025-10-19 04:12:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d9d6718c-565f-3cb2-a5ff-01dc8a42d9ed | -13.89667 | -45.52252 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7030ac30-56b5-384f-b159-3ed9fc6379be | -13.60497 | -43.11204 | 2025-10-19 04:12:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| a16a4c00-696b-38e1-b5c8-c7d0e6ec77d2 | -12.41104 | -40.92593 | 2025-10-19 04:12:00 | NPP-375D | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ca32cf6e-17b9-340b-8558-109d80d0ca1c | -12.14677 | -45.07341 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 67e4b3b5-6b2c-3192-a216-fd7cb072dce9 | -9.11687 | -46.64349 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a84801de-53f8-3c05-9c43-a8e5d72c38f0 | -11.65417 | -44.0847 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 54b71021-415a-3f5d-975e-9882cd509f06 | -8.60849 | -40.19234 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 38.3 |
| 97cdb842-cdd0-3400-843f-44374ef8adbf | -10.4233 | -45.01754 | 2025-10-19 04:12:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 86eae339-0231-38ae-8dfa-1c3a2ca63826 | -11.15846 | -43.47846 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a21c4138-5898-3ab5-b469-3cc0dd14f291 | -10.53351 | -44.14561 | 2025-10-19 04:12:00 | NPP-375D | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c7f819d-c3da-34c3-a13b-c945248128fb | -7.95627 | -48.12576 | 2025-10-19 04:12:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fecb88c1-1020-37bd-8fe8-49439a9f3432 | -10.7211 | -44.55219 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cd39fc55-4097-336a-bed8-9d3283d8f625 | -12.47077 | -45.43118 | 2025-10-19 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d443aaee-9f01-3650-a693-d152db30ae63 | -8.61535 | -40.19339 | 2025-10-19 04:12:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 2830db54-85d9-3ec0-b519-515e1db7f0cc | -10.88819 | -46.0694 | 2025-10-19 04:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 773391d3-d7e4-3f94-a404-a2448d074c61 | -10.92141 | -43.8191 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 03ac1d48-5e48-31d5-b1b1-56b16563e610 | -10.87852 | -47.45895 | 2025-10-19 04:12:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f26d7117-558b-3014-9d33-4d9a09c2ab02 | -9.04862 | -49.51449 | 2025-10-19 04:12:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 444fa6e3-5686-32b2-b9a7-8d8e0121cc44 | -10.67992 | -44.55374 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 410d417e-f545-3cb7-956e-7e115fefcc72 | -11.35021 | -47.27398 | 2025-10-19 04:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f7252a7-4e4f-3995-8f6c-e5a3fd9b2fdd | -11.62159 | -44.07176 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fa35291c-067e-33af-a217-798e69847800 | -8.2789 | -43.35386 | 2025-10-19 04:12:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7c3c067a-37d2-362d-ab01-3d4b87e8c165 | -10.92083 | -43.82271 | 2025-10-19 04:12:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cfa021ec-a86c-312e-a310-ab431e1c375c | -13.95918 | -41.72386 | 2025-10-19 04:12:00 | NPP-375D | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0028f500-3050-3232-84bc-7c2be7032645 | -10.15869 | -42.21497 | 2025-10-19 04:12:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| bfdad8f5-2b5b-3ca6-b7f1-5167c746bcf0 | -12.14468 | -45.07202 | 2025-10-19 04:12:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fbbee913-1b56-3f8b-8c36-531a51e6582a | -13.8982 | -45.53482 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59f6ea0c-164a-32dc-9059-f97663fa5743 | -13.89408 | -45.53814 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 95ec0f5e-88e5-3ab4-9db4-5304c22115d5 | -8.49289 | -44.14788 | 2025-10-19 04:12:00 | NPP-375D | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a6bf048-5cdc-30d6-bdb8-e80e36140527 | -13.86417 | -45.46073 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2d642fc-9386-304a-8bb7-1da0b36c0854 | -12.93216 | -42.86036 | 2025-10-19 04:12:00 | NPP-375D | BOQUIRA | BAHIA | Brasil | 2904100 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3431a338-d0a0-36a0-aa8a-3d20ea3298b3 | -13.89884 | -45.53091 | 2025-10-19 04:12:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5e6029eb-ec11-3b66-99b9-148adcc357cc | -8.89983 | -49.00399 | 2025-10-19 04:12:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc9aa158-8237-3b01-ad6a-f7936347d1d4 | -8.34636 | -46.21952 | 2025-10-19 04:12:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a2955259-0b76-323d-a5f6-87ff14e55be4 | -8.43178 | -49.59088 | 2025-10-19 04:12:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2776ab2e-bb49-36ff-bfbf-12f5d39fd59f | -11.63611 | -44.08916 | 2025-10-19 04:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8690dbd9-a0e8-3eb0-8dc7-0a264bd60234 | -13.01313 | -46.95185 | 2025-10-19 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f0d294ac-f167-3a09-890a-2ebb2483f75b | -11.99577 | -46.77324 | 2025-10-19 04:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 87de8212-4aad-3132-bceb-3b18b18ee433 | -8.44567 | -40.57537 | 2025-10-19 04:12:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 607cf1fb-0883-347f-8ca2-16242e6558fc | -10.71674 | -44.53588 | 2025-10-19 04:12:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 506cd6c8-9525-3c39-a154-b13ea4b411bc | -11.38792 | -40.68832 | 2025-10-19 04:12:00 | NPP-375D | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 1b4f97a1-a44d-36c2-91d6-8aea35b518e9 | -9.10666 | -43.20719 | 2025-10-19 04:12:00 | NPP-375D | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e5d8dc8c-224f-33fe-a1a0-495e07cca26f | -10.60997 | -49.52519 | 2025-10-19 04:12:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dcab5a4d-481d-366f-bd0f-d147d2422ce7 | -9.89561 | -47.65699 | 2025-10-19 04:12:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 083ad50b-4854-3dab-adc8-6296a557060e | -13.92367 | -43.83241 | 2025-10-19 04:12:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58adcb1d-ce85-3041-b7e0-556456a3ecec | -9.66856 | -44.55885 | 2025-10-19 04:12:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3fb40b4-85f8-320c-88e4-e87f586cebfd | -13.08452 | -41.08408 | 2025-10-19 04:12:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32383855-e4c1-3443-a226-d243ccd341e4 | -8.2095 | -43.95874 | 2025-10-19 04:12:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1d5f36e4-8757-30a3-a804-28a29cc3c593 | -10.29827 | -44.02399 | 2025-10-19 04:12:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b57500b-bc09-3cda-bd19-975c012f287e | -8.16046 | -47.98507 | 2025-10-19 04:12:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a0b2ff01-cb09-3a46-a269-b4a3cc5abfbe | -11.36755 | -44.91716 | 2025-10-19 04:12:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a5a0f6ba-cc35-3ec1-9c9f-76a45ce89c08 | -9.25695 | -44.34008 | 2025-10-19 04:12:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2914ad39-0598-3921-a170-bc85353fa002 | -13.92672 | -42.95676 | 2025-10-19 04:12:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4c1d0347-27e0-329a-b4b1-0624d77ca71f | -15.68774 | -45.34558 | 2025-10-19 04:14:00 | NPP-375D | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README34.md)
