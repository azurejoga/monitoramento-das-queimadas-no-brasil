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

## Dados Diários - Página 97

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 40cf4181-f7f0-3602-abc1-8f2ae8ecd111 | -6.4355 | -44.5764 | 2025-08-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 953a7db1-92c5-3d12-9ea1-ca4f2cdb713a | -7.6411 | -42.6955 | 2025-08-28 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 98.2 |
| f2df5fc6-5ada-3763-9ed6-6b0ebf66b705 | -14.3309 | -53.2477 | 2025-08-28 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 78c490ea-8869-35d8-9eaa-7df30bee8018 | -10.8421 | -60.8009 | 2025-08-28 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 100.8 |
| 01bf42b6-8e6b-33f4-9e72-1b2b6edd8244 | -7.0569 | -44.3623 | 2025-08-28 13:50:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 110.2 |
| fc7aedce-b823-3eb5-b938-4d239cf7185d | -12.8613 | -48.1213 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 8304330f-2574-352d-b61c-824a4dc85886 | -7.6408 | -42.7192 | 2025-08-28 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 91.1 |
| 8fd75823-1f06-376c-8634-09b83f4123ad | -5.8889 | -42.9283 | 2025-08-28 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 67.5 |
| 94063f90-69c9-3c99-a095-e89f189ad5d0 | -11.6539 | -44.8765 | 2025-08-28 13:50:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 944a3491-2f85-3b41-902a-e9d162273e22 | -9.4058 | -60.5904 | 2025-08-28 13:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 126.3 |
| 443e7b6a-9dee-3911-bd61-37afce0269de | -9.134 | -65.7694 | 2025-08-28 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 257.8 |
| fa245aad-c156-3169-91ea-ac8e42729248 | -9.6794 | -47.0798 | 2025-08-28 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 903cbbc3-a9e9-362d-9f45-083afb2ebd13 | -15.191 | -53.79 | 2025-08-28 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 94a4aeff-46ea-3c1e-9f42-cd670b76b51b | -7.192 | -44.0501 | 2025-08-28 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 76.7 |
| e3a9acfd-0a97-312c-a89d-7bd34a809c98 | -9.1363 | -65.2835 | 2025-08-28 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 34baf18b-254c-3550-b860-506333a5f670 | -10.4738 | -57.9366 | 2025-08-28 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 67e6ff36-211b-3641-9e9e-f3decefd6f33 | -6.8772 | -43.6152 | 2025-08-28 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 196.9 |
| 385d1f4e-76c0-3e88-9cda-f52d00d7d152 | -11.1523 | -54.3104 | 2025-08-28 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 387e8b80-bff4-38e5-8d8c-c300b9ad9f23 | -6.8583 | -43.6169 | 2025-08-28 13:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 7ad6ee20-b11b-31fd-b7db-3560e7f57e00 | -6.2755 | -43.6907 | 2025-08-28 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 73.6 |
| bf2a7ceb-2911-370b-9d97-99b230b1a452 | -13.4208 | -46.9864 | 2025-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 74908866-c6c9-3a5f-a13f-d57a777c893d | -13.0863 | -46.3352 | 2025-08-28 13:50:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 05b0a06f-cc54-36bd-b2a9-df4b457be1cd | -15.2101 | -53.8086 | 2025-08-28 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 69.5 |
| 1487cb47-ac90-3b8c-bde3-310a0da6a00d | -8.7322 | -47.4003 | 2025-08-28 13:50:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0ec7de8a-04bf-39cf-8ff9-089d15582793 | -7.6225 | -42.6738 | 2025-08-28 13:50:00 | GOES-19 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| 538fd77b-523f-3090-9499-e0e1b28e4c9e | -13.4212 | -46.9637 | 2025-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 429fc47b-3de3-362f-9ba5-66c3a6a1868a | -10.8419 | -60.8202 | 2025-08-28 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 221.3 |
| 16ea0938-a17b-3b5d-a9b2-53c2de2db39d | -13.5386 | -46.8775 | 2025-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 4704e5ee-b99a-33e9-8a01-8c10ce9378f4 | -12.9963 | -56.9 | 2025-08-28 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| e55a473d-b911-3bab-ab73-2b45a6a27540 | -9.676 | -64.9838 | 2025-08-28 13:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 63.5 |
| c327c9df-f1e1-33e3-94bb-7c584606e1c4 | -12.6875 | -48.1899 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 282467a1-7a75-3b56-afcb-d7e6854b2498 | -12.8617 | -48.099 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 53c2975e-5443-3bb3-a23e-6489b8a58aa5 | -13.5193 | -46.8805 | 2025-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 06efd0f9-4ec4-3a17-a0f2-21f5403db122 | -14.3696 | -52.0813 | 2025-08-28 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 24c13392-d267-3633-a83c-4cdb8ed12a9b | -6.1595 | -44.0472 | 2025-08-28 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 192.6 |
| bbf78707-7176-3671-84db-e316aeba9a6c | -11.3526 | -43.5187 | 2025-08-28 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.6 |
| 49253151-1e5c-3e2d-b8c5-92125f2946dc | -10.308 | -46.8068 | 2025-08-28 13:50:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.5 |
| c0896133-b758-3b22-826a-e3bcb2256767 | -10.8233 | -60.8019 | 2025-08-28 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 87.2 |
| ab1554c3-522a-3d16-8d11-74cf17b72582 | -15.1906 | -53.811 | 2025-08-28 13:50:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 94.8 |
| 727ab57c-abf1-3128-afe4-e94f1a87c61b | -7.3196 | -46.109 | 2025-08-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.7 |
| 5052c57e-59b3-391c-b0d5-20e6c9670264 | -9.5423 | -62.4014 | 2025-08-28 13:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 93551995-2f16-3be1-ad40-67ff17eff5eb | -6.1372 | -44.417 | 2025-08-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 72.8 |
| 6825dec5-b4e1-3ab2-acb0-6e10f946202c | -9.2632 | -65.8959 | 2025-08-28 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 73.6 |
| 28365f80-4f8c-34e0-89e5-e30d51785138 | -9.1339 | -65.788 | 2025-08-28 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1026.3 |
| e2eaa04d-efdf-3534-970d-110050c5428a | -14.5638 | -52.013 | 2025-08-28 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.5 |
| 08f9e08a-acb7-3b63-bc61-fc237bf03ae5 | -10.972 | -46.8593 | 2025-08-28 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 23d84f43-45c7-33fa-b5c3-a0f73a347c4a | -12.9961 | -56.9201 | 2025-08-28 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 725bab80-359a-38f1-ae5a-415a204c6c15 | -13.0151 | -56.9184 | 2025-08-28 13:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 101.2 |
| ca82c55c-46c0-300f-b113-cc5c393a3a3a | -8.8842 | -60.7507 | 2025-08-28 13:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 8acb89f1-d116-3157-8c07-7495f09fa8f5 | -10.8049 | -60.7644 | 2025-08-28 13:50:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 1bc09a02-356d-334d-89d5-c35868e293b6 | -12.3993 | -45.0183 | 2025-08-28 13:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 0d5ad62e-aed1-3c71-a01e-a4d4f082a4f9 | -9.4363 | -48.3174 | 2025-08-28 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 224.1 |
| 66c20c66-b4b8-3fe0-8299-6278bec318d0 | -7.3193 | -46.1314 | 2025-08-28 13:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 7e99171a-74a0-3727-8dae-03bbf63f67b0 | -8.2705 | -45.1605 | 2025-08-28 13:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 99.9 |
| c54cf815-f51c-371f-969c-139a00cb6e48 | -16.3606 | -43.7858 | 2025-08-28 13:50:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 279.5 |
| 638b9523-18fe-3ef2-a183-b61c1e124131 | -11.3517 | -43.566 | 2025-08-28 13:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 237.5 |
| 9de937a8-a649-33ce-a796-e19b8103506a | -9.1155 | -65.7699 | 2025-08-28 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 607.9 |
| fbd79d3a-5b6c-3df2-aa12-9ef7f0dc8751 | -13.5576 | -46.8972 | 2025-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 70.6 |
| a0792d5d-4e2b-3671-87fe-72c09c45df00 | -13.4204 | -47.009 | 2025-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 564eae5d-7d41-3945-8019-ffec5e1ef3b7 | -9.4366 | -48.2955 | 2025-08-28 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 121fe039-6023-3a43-9454-36978bbc18de | -9.5424 | -62.3823 | 2025-08-28 13:50:00 | GOES-19 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 60f20bc5-aadc-30b1-8b74-58e26bf73ba9 | -11.1017 | -44.7476 | 2025-08-28 13:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 9b164600-a9cb-3fd6-bdc2-2a0930211cd1 | -11.5921 | -46.2363 | 2025-08-28 13:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| 146417a4-497b-3c63-93f1-ee7f48ac3802 | -6.2757 | -43.6675 | 2025-08-28 13:50:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b91e55e5-8492-3d3b-9a4b-45420c996a7e | -10.6438 | -47.1904 | 2025-08-28 13:50:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| d124a015-1191-35a3-a147-e8e684bf8394 | -9.4552 | -48.3155 | 2025-08-28 13:50:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| db3b2792-8948-329e-9291-80ba73937ecc | -9.6797 | -47.0576 | 2025-08-28 13:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 59.3 |
| a27d7410-7835-370e-a382-c42f6767facd | -14.3506 | -53.2243 | 2025-08-28 13:50:00 | GOES-19 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 77.8 |
| de9d49d4-2c1f-35fb-8020-dd345c18b90d | -10.4736 | -57.9563 | 2025-08-28 13:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 65e430ba-53bb-32de-909f-7221ea5f3817 | -6.1593 | -44.0703 | 2025-08-28 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 217.8 |
| f8ceadda-0263-3c89-94eb-2bae46f46b63 | -9.2446 | -65.8965 | 2025-08-28 13:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 91cbac3f-ee75-35d1-91bf-ff77942c44b3 | -12.8028 | -48.1739 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 24c304cf-29de-3789-9585-6881edeb731b | -5.8701 | -42.9298 | 2025-08-28 13:50:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 92.0 |
| 0d7cb5ab-3988-33b5-bbaa-988e130169e1 | -6.4543 | -44.5749 | 2025-08-28 13:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 136.1 |
| 8f9d5667-a0e1-37dc-b4e9-316a888500a6 | -12.8224 | -48.1489 | 2025-08-28 13:50:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 162.7 |
| 72c41edc-22f8-3b1d-ba91-93689e8a0793 | -11.2378 | -55.0569 | 2025-08-28 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| ba0db588-b0fb-34ea-835d-b235eb2c9465 | -6.178 | -44.0688 | 2025-08-28 13:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5e18c0d9-5d66-388e-be08-5a6b826965ff | -11.2189 | -55.0585 | 2025-08-28 13:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 88.8 |
| aadd9ea9-aafd-3fac-a708-83a74eb7a932 | -8.7325 | -47.3783 | 2025-08-28 14:00:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 1833a4ae-3c02-3863-92b0-f92fad47f09b | -13.0151 | -56.9184 | 2025-08-28 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 257.1 |
| 7f80cccd-6255-3abc-aef5-93e2f96a8e70 | -13.4208 | -46.9864 | 2025-08-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 69f89f0d-0242-3be3-8307-1c12b3f04ff1 | -11.3517 | -43.566 | 2025-08-28 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| 233ca996-a084-320f-834e-9e8885366f3f | -9.4363 | -48.3174 | 2025-08-28 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 186.6 |
| 5095a5cc-19c2-3e88-9829-09a2efea5de8 | -8.8842 | -60.7507 | 2025-08-28 14:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 543b83c6-9439-3e94-b3fb-04cca8ab50c0 | -13.0863 | -46.3352 | 2025-08-28 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 103.9 |
| fb5e49d0-2337-3eb9-8e56-67ffb0295776 | -6.131 | -45.079 | 2025-08-28 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 88.3 |
| d1f6a703-96bc-3fd2-bb3c-83e6a92b4c0b | -16.3606 | -43.7858 | 2025-08-28 14:00:00 | GOES-19 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 118.6 |
| f47c46e8-4806-39c6-89fe-352369d96760 | -9.2446 | -65.8965 | 2025-08-28 14:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7f7d8791-2fc3-3930-aed8-da7ffbbf604c | -10.8233 | -60.8019 | 2025-08-28 14:00:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 75.0 |
| e7ba8bd8-2d86-31e6-a9fe-75df2c1c4bd0 | -9.4366 | -48.2955 | 2025-08-28 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 7a124f6b-9d68-311b-8e3d-4d9bf030e392 | -13.4204 | -47.009 | 2025-08-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 139.6 |
| 8d4e06e2-741c-3be8-a8f9-73e6db95fb93 | -18.4668 | -46.9213 | 2025-08-28 14:00:00 | GOES-19 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 80.4 |
| e3b6ac52-44e7-3541-89e1-6f4b697c378b | -7.1917 | -44.0732 | 2025-08-28 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 106.5 |
| b9474391-f1c8-34af-b872-f9e149c95c6e | -12.8613 | -48.1213 | 2025-08-28 14:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| b4382f39-7dab-3580-aa61-a14c7a1afa98 | -10.308 | -46.8068 | 2025-08-28 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| ae0b8ef9-d218-38f8-850b-d176adb603b0 | -15.2101 | -53.8086 | 2025-08-28 14:00:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 129.5 |
| 63e6df96-1d60-3b15-bb70-8f547c7f2b1e | -11.5921 | -46.2363 | 2025-08-28 14:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 9952a366-c529-3486-bc4f-d0e2ac4ad6be | -7.3357 | -59.6484 | 2025-08-28 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| db552852-01ef-356e-bfcb-0ca3ffdbc095 | -7.5485 | -47.4867 | 2025-08-28 14:00:00 | GOES-19 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| dd6c829c-f062-3d76-919c-7680a47801a4 | -13.0154 | -56.8982 | 2025-08-28 14:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 104.8 |


[Clique aqui para ver as próximas entradas](README98.md)
