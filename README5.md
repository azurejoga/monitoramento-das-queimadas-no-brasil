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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 286d9f03-a24b-3a25-a43d-227af2865391 | 3.27566 | -60.62175 | 2026-09-29 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| acb6837a-d2ad-30e3-8615-7d0a0f11b7f9 | 3.2845 | -60.62298 | 2026-09-29 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 26.7 |
| e8afb7b5-38e6-3ac4-9402-b6bf26d7a588 | -7.8488 | -45.7912 | 2026-09-29 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 10e21373-70be-3834-99c5-db04f3cbe989 | -8.5738 | -66.994 | 2026-09-29 00:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 3a8f50f9-4d50-3be4-809c-6692322a3a12 | -9.1256 | -67.8507 | 2026-09-29 00:50:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 74.5 |
| bdd76842-f3fe-3fd0-8c9f-2a4b77b0483c | -7.8483 | -45.8363 | 2026-09-29 00:50:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 8ebd126d-a59f-3943-9782-fbba72204975 | -7.3825 | -72.4803 | 2026-09-29 00:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| 44ce72ed-df2d-3aff-acbd-9f5ae8398a0f | -6.2947 | -43.6427 | 2026-09-29 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 156.3 |
| aac1f42a-af6c-3db4-b64d-b4df1de6b026 | -10.3892 | -61.2695 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 44ae385f-ace6-3e68-98ae-26618ec5b9a1 | -7.3825 | -72.4621 | 2026-09-29 00:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 94080eb5-05ec-3a83-97b2-59aee63a8d32 | -10.4079 | -61.2685 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 597c3be6-2714-394f-97a6-666203b3bf85 | -10.4081 | -61.2492 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| f189aad1-6de0-3cc7-b869-3bd58f6f4098 | -10.3894 | -61.2502 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 114.0 |
| 727cdb61-4f42-306c-abe2-ea2f65559939 | -7.7025 | -48.8667 | 2026-09-29 00:50:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d4da86f7-0982-30a0-b7b0-bafa98a5e073 | -7.3641 | -72.4805 | 2026-09-29 00:50:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| f7575ba4-c9ad-379c-828e-965ecb91b7e6 | 1.6749 | -55.9225 | 2026-09-29 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 0471404f-f49e-35bf-b2b1-23acb94ca573 | -7.8297 | -45.8156 | 2026-09-29 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 174.1 |
| fb86fffd-b315-3c9e-ba3a-4fe0313d0bf5 | -5.6081 | -45.0038 | 2026-09-29 00:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 4a31a572-8ed4-3788-bc2f-a13815732b02 | -7.8486 | -45.8138 | 2026-09-29 00:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 306.5 |
| 7a0cad79-f11e-3de0-8854-518d1be0cb3a | -10.3707 | -61.2513 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| b6627d74-334f-3379-9448-06fac4f26200 | -18.5684 | -48.4191 | 2026-09-29 00:50:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 92.0 |
| c84fe5f8-9312-3b9a-a730-9af0b6e6389e | -15.4585 | -46.1367 | 2026-09-29 00:50:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 127.0 |
| 4ecff77f-139d-3626-a26d-1b3489ec5a25 | -3.7166 | -54.2297 | 2026-09-29 00:50:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 64c23085-1431-341a-ae37-e8f867996ae6 | 1.675 | -55.9028 | 2026-09-29 00:50:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 1c0d22ad-356e-3a8e-8018-4c18c05609b0 | -10.8424 | -60.7622 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 7a65fd49-e995-370c-8b4c-7d0b6f65a401 | -9.9266 | -60.7171 | 2026-09-29 00:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 92a542bb-4cf9-375f-ab94-2c5f3b4b9244 | -6.2949 | -43.6194 | 2026-09-29 00:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| 96f6017b-fc55-35d0-8e07-9798cbcc4228 | -7.8297 | -45.8156 | 2026-09-29 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 174.5 |
| 466c5530-06b5-35b1-bb66-8d517d748863 | -10.4081 | -61.2492 | 2026-09-29 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 21fb5238-4f91-3fc1-91df-94f7e1d9f40a | -11.9373 | -50.8912 | 2026-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 197.5 |
| c7546442-1cc9-3ba5-a9a4-11632da18119 | -7.3825 | -72.4621 | 2026-09-29 01:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| bfc4416f-c0d0-3a19-b3ab-65bac2474304 | -3.7166 | -54.2096 | 2026-09-29 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1d25397e-11b6-3621-920b-f50170d7a46f | -7.3825 | -72.4803 | 2026-09-29 01:00:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| b8409ee4-ab4b-3246-97bb-8eff0c1769f6 | -9.9568 | -59.2629 | 2026-09-29 01:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.1 |
| a80fc18e-86fa-30b8-8500-3dd7e832ad6c | -7.8488 | -45.7912 | 2026-09-29 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| beba7645-011d-32fb-bc62-615cd6450b8d | -18.5684 | -48.4191 | 2026-09-29 01:00:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 87.3 |
| c68fc6a3-a2ca-3c77-8d14-62083bb7e81d | -5.6081 | -45.0038 | 2026-09-29 01:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 69658c1c-af27-3425-abc8-2a8248238211 | -8.5738 | -67.0125 | 2026-09-29 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 5028d833-d3ec-38b4-a6d5-8d53e39c4a22 | -7.7025 | -48.8667 | 2026-09-29 01:00:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 4ff9f868-8d2e-3d06-857b-1124d9f14986 | -7.83 | -45.793 | 2026-09-29 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 3924be79-464a-3eb1-9a25-06eecd46f4c4 | -10.3707 | -61.2513 | 2026-09-29 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 550bcb4c-5369-321f-8d5a-b93fd78a7c6c | 1.6567 | -55.8833 | 2026-09-29 01:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 015bc5aa-f4ec-3e4c-9a31-e85aac3f88e7 | -10.3894 | -61.2502 | 2026-09-29 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| a90ff64b-552e-3f1e-a433-7c57678cbe9e | -8.5738 | -66.994 | 2026-09-29 01:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 0a76ba1c-9765-3122-b7c2-e77a6a196125 | -10.3892 | -61.2695 | 2026-09-29 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 3618b552-7f40-30a2-89d4-2b4e362097e7 | -11.937 | -50.9125 | 2026-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 79afa9a4-e6f7-32ff-bf52-25bfd107c49c | -6.2949 | -43.6194 | 2026-09-29 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 55b89fdf-8935-345c-b145-417d72f065ab | -11.9377 | -50.8698 | 2026-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| 116068bf-370a-30ba-ac14-d32bb21dd98c | -7.8486 | -45.8138 | 2026-09-29 01:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 320.1 |
| 8c935467-06cb-3827-a964-616d90aa18fe | -15.4585 | -46.1367 | 2026-09-29 01:00:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 124.4 |
| 409e04a5-4221-31fa-8ff0-1700a4e08936 | -9.9595 | -50.1431 | 2026-09-29 01:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 6e27a6ea-5689-38b5-a172-b30766ccf4aa | 1.675 | -55.9028 | 2026-09-29 01:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 6e64202b-04a0-3890-8270-ff4afcba6c96 | -11.9183 | -50.8933 | 2026-09-29 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.0 |
| 36f7dcc2-17b0-3ac2-8356-e61b2c217fb8 | -3.7166 | -54.2297 | 2026-09-29 01:00:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 53887403-9f0b-3233-8644-6cfd26d17a9a | -6.2947 | -43.6427 | 2026-09-29 01:00:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 171.1 |
| 85a0a8eb-a27d-3688-8468-d5f3f60f19ae | -7.8483 | -45.8363 | 2026-09-29 01:00:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| c2422d78-e8d5-3ab3-8fc9-c8ba4132e353 | -10.4079 | -61.2685 | 2026-09-29 01:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 449baa8f-6675-3add-8922-9eb6c64b1fbc | 1.6567 | -55.8833 | 2026-09-29 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e73ca5ee-a69f-3b8c-ae34-63bfed2fbdd2 | -6.2759 | -43.6442 | 2026-09-29 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 46ec6704-5246-3732-ab75-9e33a1960ef3 | -3.7166 | -54.2297 | 2026-09-29 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 95b836f7-1de5-3ec1-ade6-b1386bb2f093 | -9.9568 | -59.2629 | 2026-09-29 01:10:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| df7f4b2e-e3ec-3edc-b166-6e12bd62d728 | 1.6566 | -55.903 | 2026-09-29 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 98ea91c6-b928-391d-a233-694c8a3bb102 | 1.675 | -55.9028 | 2026-09-29 01:10:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 16ea42d2-8dd7-3488-8dc7-6804f65eba94 | -3.7166 | -54.2096 | 2026-09-29 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 8973c027-5724-39a2-91c4-2df9602b6dd6 | -7.6838 | -48.8682 | 2026-09-29 01:10:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 6e940eb3-4974-3cc5-bfdf-362485078123 | -5.6081 | -45.0038 | 2026-09-29 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1163f1a6-4754-34fa-b66a-0e6587030ccb | -11.1775 | -44.7832 | 2026-09-29 01:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| b04b9a34-90c7-3345-a605-5e7689d81644 | -10.3892 | -61.2695 | 2026-09-29 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 483ea53d-9b7e-3eb6-9959-5c656778a837 | -7.8488 | -45.7912 | 2026-09-29 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 15b6d2c0-7fe0-3a67-9144-3bcce798887b | -7.3825 | -72.4803 | 2026-09-29 01:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 20f41821-0148-343e-9f5e-0d80c112bbde | -10.3894 | -61.2502 | 2026-09-29 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 117.9 |
| fcbbcac1-7863-3080-98c3-77a3f813576f | -7.8297 | -45.8156 | 2026-09-29 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 197.7 |
| 357b05b5-3643-35b6-98a8-94ee0bc3a9de | -11.9373 | -50.8912 | 2026-09-29 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 495a55e4-862b-3c51-b854-4af284b3aaa9 | -3.6982 | -54.2303 | 2026-09-29 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d43e55a5-704e-31d4-a095-9aaf20e9ea96 | -10.4081 | -61.2492 | 2026-09-29 01:10:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 60f5f184-0bdf-3a37-92f5-b86f7f774fc4 | -6.2949 | -43.6194 | 2026-09-29 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 79ab6de3-e3e5-35a7-a782-09114e747a65 | -9.9595 | -50.1431 | 2026-09-29 01:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| b5e1a660-846a-3221-a4c8-0813cc17c68a | -11.937 | -50.9125 | 2026-09-29 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 103.0 |
| be48d13e-677d-38df-b982-e3a5d840757e | -7.3825 | -72.4621 | 2026-09-29 01:10:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 0c6d163b-6117-39a8-80f2-636f7729d9cc | -18.5684 | -48.4191 | 2026-09-29 01:10:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.2 |
| ac6354aa-0fe7-346e-9ceb-bc2d1f42a714 | -7.8486 | -45.8138 | 2026-09-29 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 276.0 |
| 19a64ed0-d9a7-3ec1-a5b8-3a6703f93dca | -15.4585 | -46.1367 | 2026-09-29 01:10:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 4257c4fa-fabd-3807-b460-843298a5e814 | -6.2947 | -43.6427 | 2026-09-29 01:10:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 146.9 |
| f4c8e219-21fd-3554-8ccc-06219061b0f6 | -7.83 | -45.793 | 2026-09-29 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 61.9 |
| ad6b0702-70bb-327a-832c-908e00f928b0 | -11.42 | -43.43 | 2026-09-29 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 397ab836-0c61-3f73-8224-4ad60922a0ac | -11.98 | -50.96 | 2026-09-29 01:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2324b6fc-1dc0-3ea6-aaa2-7d50e0d1efe7 | -11.45 | -43.49 | 2026-09-29 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 808ff58b-10b9-3cc4-9c21-8e78104d0c50 | -11.39 | -43.43 | 2026-09-29 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d777a658-a94f-387e-8736-45c19e2e34a4 | -7.84 | -45.84 | 2026-09-29 01:15:00 | MSG-03 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e4d655e1-10e3-3bc8-9a6a-0fc327b3d34a | -12.01 | -50.97 | 2026-09-29 01:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4ea1acb7-1a0d-3fdc-a784-45f22a7f856f | -11.45 | -43.44 | 2026-09-29 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 690357dd-1c69-3583-a68d-30f650c63058 | -11.42 | -43.48 | 2026-09-29 01:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3102bdd4-d52a-3fb5-a48f-b271c5f14aa0 | -11.98 | -51.02 | 2026-09-29 01:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2ca74f89-5c7d-361b-b1f4-2e603013eeb2 | -7.84 | -45.79 | 2026-09-29 01:15:00 | MSG-03 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bcc76e7f-a8d8-3e56-bca5-5feac0607dca | -5.6268 | -45.0025 | 2026-09-29 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 3a6beaf5-b4c2-3b10-8f44-f7fc5d644bd1 | 1.6566 | -55.903 | 2026-09-29 01:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 0fc07591-783a-33b3-8659-b2479ff5d38d | 1.6932 | -55.942 | 2026-09-29 01:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 1fa48736-c3af-3d53-a2aa-bead4794e9f2 | -7.8297 | -45.8156 | 2026-09-29 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 184.1 |
| 0095ac04-fde2-3ade-ab05-dfe65fe69f58 | 1.6567 | -55.8833 | 2026-09-29 01:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| f22618bd-5345-3b8a-afb7-b5f8cb4e79da | -8.5738 | -66.994 | 2026-09-29 01:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |


[Clique aqui para ver as próximas entradas](README6.md)
