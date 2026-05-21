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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 44ca335a-9f2d-34ad-aaba-0721535d2db5 | -11.30007 | -54.71492 | 2026-05-21 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e428b6fc-780d-393f-b9bc-0acaff6b84a4 | -11.18294 | -55.91551 | 2026-05-21 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dc98c32-00a0-35b2-a1d6-3ba795dcb205 | -11.18337 | -55.91211 | 2026-05-21 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b55e2ac-d12a-3bc8-8d45-1e48c5e9c136 | -11.55113 | -54.53648 | 2026-05-21 05:46:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cecf93ac-85b3-32dd-a9d5-d269e6301f9d | -9.95298 | -52.45644 | 2026-05-21 05:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 202fb606-ab03-38dc-8f37-532f4a93168b | -9.94647 | -52.45544 | 2026-05-21 05:46:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96b2d58f-b114-32d0-86b6-8436191bf2cf | -9.93181 | -59.922 | 2026-05-21 05:46:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5637f08d-13ef-3c00-9af6-0fe120a4e3e5 | -11.30057 | -54.7108 | 2026-05-21 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 897df8af-b151-315c-a518-68cc6c7e7d09 | -11.92068 | -54.10345 | 2026-05-21 05:46:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3c49056b-dcaf-3298-80d3-8fe6dda5d6d0 | -19.77201 | -54.07402 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e32391d7-9c99-32ff-8a9a-b2bacbf6b779 | -19.76535 | -54.0738 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2351e3a8-cc21-349f-abd1-2ae911016fb5 | -19.76903 | -54.06738 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 34432df1-1e45-3480-bf75-ddad41848d62 | -19.76851 | -54.07309 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9853c9e9-e944-3152-92d7-f18693ab37f8 | -19.76487 | -54.07941 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c4c9927-0c29-387a-84a2-a24c1ec1ab86 | -19.77249 | -54.06832 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dd8aa96-c406-3250-8c51-6b93fdb4f897 | -19.768 | -54.0787 | 2026-05-21 05:48:00 | NPP-375D | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 670c3ddb-b4e6-3f62-9069-f9b12116b64f | -5.94897 | -43.48562 | 2026-05-21 06:01:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 44a3bae2-0b3e-3fa1-b690-4ffe9f95d39e | -9.29752 | -45.4882 | 2026-05-21 06:03:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 25.0 |
| b0a55f93-2a20-3a81-80d2-ecb539d02f59 | -6.57262 | -51.07459 | 2026-05-21 06:03:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| cdf5c9f6-7d31-364b-ad42-2ad6c12ccd08 | -8.54803 | -45.98009 | 2026-05-21 06:03:00 | AQUA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 47.2 |
| a791bdbf-371b-385d-9234-9f1b35f0f5ce | -10.48829 | -49.36449 | 2026-05-21 06:03:00 | AQUA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 7281c137-e613-375b-82e2-6533d8b5a4bb | -6.57006 | -51.06956 | 2026-05-21 06:03:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 315ba215-603c-3a32-bedc-0d47113f299c | -6.56333 | -51.10936 | 2026-05-21 06:03:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 490f15d0-4253-3dba-8414-f05bfefe5fc0 | -9.30818 | -45.49004 | 2026-05-21 06:03:00 | AQUA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 14.6 |
| e2630c92-9022-3389-92bf-c7ffeec19dfd | -6.56567 | -51.11415 | 2026-05-21 06:03:00 | AQUA_M-M | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 2810e811-11e5-3969-8c4c-88a38def18bf | -7.41501 | -38.7971 | 2026-05-21 11:17:00 | TERRA_M-M | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 4c975340-735e-32ae-a554-43315201370e | -6.39285 | -38.91097 | 2026-05-21 11:17:00 | TERRA_M-M | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 10bdbc2e-5710-3154-8add-bc039c7cefda | -8.17252 | -35.41639 | 2026-05-21 11:17:00 | TERRA_M-M | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 95f81c4b-380e-3b09-8b03-1507578462e8 | -11.95892 | -43.38845 | 2026-05-21 11:19:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 216.8 |
| dbef72d8-9a02-3c64-b1fa-3711e0687798 | -14.4115 | -42.10322 | 2026-05-21 11:19:00 | TERRA_M-M | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6746e124-1a17-3326-843b-108902074103 | -15.313 | -41.83944 | 2026-05-21 11:19:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.6 |
| cd3def9f-066b-331d-be66-9745ce7bae22 | -15.64352 | -42.48993 | 2026-05-21 11:19:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 3f9bd016-7b53-3045-b667-01192091f2ad | -15.64539 | -42.47803 | 2026-05-21 11:19:00 | TERRA_M-M | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 935dd0e5-31a9-3100-89da-dfdda643235d | -15.31134 | -41.8503 | 2026-05-21 11:19:00 | TERRA_M-M | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 7a83f390-ea5c-3eff-b79f-84ad9fa74831 | -11.96142 | -43.37303 | 2026-05-21 11:19:00 | TERRA_M-M | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 4f0bc1d9-ed4b-3193-9597-d3e3b9d730a7 | -12.23726 | -44.24355 | 2026-05-21 11:19:00 | TERRA_M-M | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 74.9 |
| abebdf41-4e91-396c-960a-dca1a71763ba | -17.11608 | -44.51522 | 2026-05-21 11:19:00 | TERRA_M-M | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3d8c3613-61d9-3b9a-920a-cf12ac82a184 | -12.96513 | -40.08126 | 2026-05-21 11:19:00 | TERRA_M-M | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 5a379857-b47f-3e81-a250-95e9d4067b60 | -12.60156 | -44.52479 | 2026-05-21 11:19:00 | TERRA_M-M | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| b8e345f7-f9bf-3eed-aa4e-e537724791c1 | -17.59812 | -44.60217 | 2026-05-21 11:19:00 | TERRA_M-M | VÁRZEA DA PALMA | MINAS GERAIS | Brasil | 3170800 | 31 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 6e4a698b-d6e9-31ae-b466-e20ecb998d9a | -11.1428 | -48.1043 | 2026-05-21 11:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 64f4b8a0-6e96-315d-95c6-c9a1c954d091 | -11.1425 | -48.1263 | 2026-05-21 11:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1ca20b9f-7151-3b8b-9c6b-78f40e5b8d36 | -11.1428 | -48.1043 | 2026-05-21 11:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 94.5 |
| 71399b11-1512-36ff-a022-ecf86b5db7b1 | -11.1425 | -48.1263 | 2026-05-21 11:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| b0258339-a3f8-3174-aa5e-b1239d372d4d | -11.1428 | -48.1043 | 2026-05-21 11:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 133.9 |
| 5e2d96a0-2b18-3558-9ee7-b4a51ba263f1 | -12.6011 | -44.521 | 2026-05-21 11:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 106.1 |
| 79a4167d-04ec-3eed-aa4d-1469443a0eb9 | -12.6011 | -44.521 | 2026-05-21 11:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 125.9 |
| 3389b931-ce7a-343e-a19e-83012f1bd2ec | -11.1428 | -48.1043 | 2026-05-21 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| ca278aae-f2da-3f8d-b295-e6c50a2f7e38 | -11.1425 | -48.1263 | 2026-05-21 11:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 89.9 |
| 23a05487-3bb2-3ad6-ac5c-d515c284caa7 | -12.6011 | -44.521 | 2026-05-21 12:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 133.8 |
| ebf55f53-f75f-341b-b68c-5333bcfb93a7 | -11.1425 | -48.1263 | 2026-05-21 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 100.8 |
| 3879303b-e713-3e11-a693-bd57562766bd | -11.1428 | -48.1043 | 2026-05-21 12:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 120.5 |
| df345401-3fac-3dac-a5eb-d1b484185aa0 | -12.2408 | -44.2512 | 2026-05-21 12:00:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 97ec03e8-65e6-3ec1-92fe-2bdd07bfebbb | -11.1425 | -48.1263 | 2026-05-21 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 91.5 |
| 06afc5fe-45aa-38fb-a866-ca74070ce783 | -12.2408 | -44.2512 | 2026-05-21 12:10:00 | GOES-19 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 2c72aab3-2b92-3dd0-a985-bb9484c332b9 | -12.6011 | -44.521 | 2026-05-21 12:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 7477d13e-e2bf-36e9-8ddb-260705a3816f | -11.1428 | -48.1043 | 2026-05-21 12:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 6cee85d6-0965-3be1-be82-e6981c61687e | -12.6011 | -44.521 | 2026-05-21 12:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 191e2650-9776-3ebe-b497-c57803c42882 | -11.1428 | -48.1043 | 2026-05-21 12:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 115.1 |
| fd16b26e-c90d-32d9-9575-4fbd84f9ff98 | -11.2743 | -49.4642 | 2026-05-21 12:20:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| 49c68682-9813-30c2-986f-3af59fa81734 | -11.1425 | -48.1263 | 2026-05-21 12:20:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1508b6b6-4288-358f-a889-3e66b96224a3 | -11.1428 | -48.1043 | 2026-05-21 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 770039cd-adf7-3c55-8159-2f7212a95c2b | -12.6011 | -44.521 | 2026-05-21 12:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| f989e040-36ac-363b-a8a8-d54e6317aa9c | -11.2743 | -49.4642 | 2026-05-21 12:30:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 2cb5c6bc-9ba6-3eaa-8a94-77e9594d81f4 | -11.1425 | -48.1263 | 2026-05-21 12:30:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 7a03217b-afdd-36e5-aa84-ac2d8fd88062 | -10.6471 | -42.29 | 2026-05-21 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 123.8 |
| 1b1dc6ef-82cb-32ee-bab1-0bf23e649dbd | -11.1428 | -48.1043 | 2026-05-21 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 191.0 |
| aa13183e-3a62-39fc-97af-e59c335a82b3 | -12.6011 | -44.521 | 2026-05-21 12:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.2 |
| fe41a04d-9468-3333-84cc-81da756e03cb | -11.2746 | -49.4426 | 2026-05-21 12:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 84.5 |
| 5c289bdc-3ae4-3467-bde3-c378354f5802 | -9.95 | -52.4602 | 2026-05-21 12:40:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 963b7c10-bbcd-3aaf-b2ed-7463a302583b | -10.6663 | -42.2871 | 2026-05-21 12:40:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 122.0 |
| c3016469-1373-311e-adb0-80974c8cffe8 | -11.1425 | -48.1263 | 2026-05-21 12:40:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 139.4 |
| f0a7c752-0878-3efa-ab0e-86794311ddb7 | -11.2743 | -49.4642 | 2026-05-21 12:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 128.4 |
| 45a215bc-51b3-3800-b609-dff4f6624e6d | -11.2746 | -49.4426 | 2026-05-21 12:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| 3386d2d9-eec4-35c2-ab2b-8ab3b2f471b4 | -11.2743 | -49.4642 | 2026-05-21 12:50:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 121.2 |
| 0ea93481-26f0-3e72-b0fb-bd304043955c | -11.1425 | -48.1263 | 2026-05-21 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 116.9 |
| c99aaa57-51dd-36d8-b23e-85481c2c95f3 | -11.1428 | -48.1043 | 2026-05-21 12:50:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 178.4 |
| 42d3a8ee-c2b0-33c9-a04c-27e7561e1773 | -12.6011 | -44.521 | 2026-05-21 12:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 85.5 |
| ee3d2cac-5445-3592-8db4-85d69b4f9d1e | -10.6467 | -42.3141 | 2026-05-21 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 88.6 |
| 3d15856b-932c-30a5-a2e1-9cf83dc1c6cc | -10.6663 | -42.2871 | 2026-05-21 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 139.7 |
| c9059644-8eab-398a-9155-e43afbb04c05 | -10.6471 | -42.29 | 2026-05-21 12:50:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 159.5 |
| a1c41f63-7387-3591-b1ea-95163cb1962a | -9.94386 | -52.44798 | 2026-05-21 12:55:00 | TERRA_M-T | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 0da8a2e5-3456-3e49-bd34-f591c98e6e14 | -11.44656 | -52.90855 | 2026-05-21 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 1ea595c0-0c10-3226-a165-ac1812ce9cc3 | -11.45879 | -52.90456 | 2026-05-21 12:57:00 | TERRA_M-T | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| faef4c96-82ec-3530-b6c8-165f2d6f52fc | -12.6011 | -44.521 | 2026-05-21 13:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 6f54ef66-3d35-37c5-aa69-f3d887912d3c | -10.6471 | -42.29 | 2026-05-21 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 190.3 |
| e9cd503d-949f-36a0-8b37-645fce77e74a | -11.1425 | -48.1263 | 2026-05-21 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 123.4 |
| f58eedfd-26e2-32bb-b5aa-23d8dddd5291 | -11.1428 | -48.1043 | 2026-05-21 13:00:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 0cb468f1-ba27-388c-90ab-86c9bde107dd | -11.2743 | -49.4642 | 2026-05-21 13:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 104.3 |
| 3ff8abcd-28a9-3860-b083-9bd2c1a5197f | -9.95 | -52.4602 | 2026-05-21 13:00:00 | GOES-19 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| fe3b8a9d-e4df-3f21-b0ff-c201630772d5 | -11.2746 | -49.4426 | 2026-05-21 13:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| bf38f433-7c82-30c9-9d79-8b3585e31e3f | -10.6663 | -42.2871 | 2026-05-21 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 143.0 |
| d89af268-863c-3db0-bdab-e7c7e95c6c9d | -10.6467 | -42.3141 | 2026-05-21 13:00:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 97.8 |
| ac0adf99-18bb-38fc-b163-4788828416b3 | -10.6467 | -42.3141 | 2026-05-21 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 142.2 |
| 9125d4cb-7f90-382a-a8d5-0ec8b1b221c8 | -11.2746 | -49.4426 | 2026-05-21 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| dad48a72-bd4f-355d-9d2d-549bfe3ad593 | -11.1428 | -48.1043 | 2026-05-21 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 242.9 |
| 4cb6648e-80bb-3117-98ff-479cc3755237 | -12.6011 | -44.521 | 2026-05-21 13:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e3423f28-5784-368c-81de-d7c5708d19d4 | -10.6663 | -42.2871 | 2026-05-21 13:10:00 | GOES-19 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 142.7 |
| 2366a8d6-a1ae-3fec-84b5-a8a3d678e891 | -11.1425 | -48.1263 | 2026-05-21 13:10:00 | GOES-19 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 5cc1ccbb-3fa6-3d8f-b281-26e16526d6ab | -11.2743 | -49.4642 | 2026-05-21 13:10:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |


[Clique aqui para ver as próximas entradas](README11.md)
