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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7de41f00-6437-3152-a5aa-6721f59a4d83 | -6.246 | -59.9982 | 2025-08-26 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7570dcbe-a679-3a9c-83dd-c842854ddc27 | -6.8043 | -58.9761 | 2025-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.9 |
| b8d9723f-0ef0-38e4-a046-37c41a6e807e | -11.1587 | -44.7627 | 2025-08-26 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 166.7 |
| 235f05c4-e70f-32ab-b9df-acc3a0341f60 | -6.2275 | -60.018 | 2025-08-26 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 52d483d2-6f39-357f-8c1d-7aeaa0082c3e | -9.1717 | -59.5405 | 2025-08-26 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| a411e32d-9c9c-381d-b636-aab95ab2de0d | -8.8364 | -62.4321 | 2025-08-26 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 9ca5c0c8-3782-3866-ae24-1fa3addd4ae5 | -10.5361 | -46.7792 | 2025-08-26 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 49ea4e8f-8535-3112-9358-8bc286685c3f | -11.1591 | -44.7395 | 2025-08-26 04:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 90.9 |
| ea17e87d-971b-3995-82e8-4374585b67b5 | -10.5358 | -46.8016 | 2025-08-26 04:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 183297d0-1042-3cc5-833f-0a583c0b584b | -8.855 | -62.4313 | 2025-08-26 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 122.2 |
| e8939814-4d5a-3ae0-a511-bb77c728d6e3 | -6.8228 | -58.9753 | 2025-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| b5b18525-1f20-3fc2-afcc-749839951201 | -9.1718 | -59.5211 | 2025-08-26 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| ba17d91b-f0bd-376e-9665-53f3ba377a81 | -9.006 | -65.4 | 2025-08-26 04:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 33.3 |
| ced9bc28-05b9-331e-9fc9-7530cbaa61cd | -9.1904 | -59.5201 | 2025-08-26 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| d576db14-bd11-38bf-80ee-2fd84da222a2 | -6.8229 | -58.956 | 2025-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 669aeed8-2ee3-31cb-b381-86b6830244d6 | -6.2459 | -60.0174 | 2025-08-26 04:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 212a4b4e-de50-3ba9-b3af-ef6fe3b59796 | -7.3854 | -64.3475 | 2025-08-26 04:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 81.1 |
| c2983abf-6aeb-35f1-8606-0e9d8e815048 | -8.8363 | -62.451 | 2025-08-26 04:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 85.9 |
| cfaf893c-cd5a-3d0d-a1e6-97e0a4f0d383 | -9.1722 | -59.4629 | 2025-08-26 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.2 |
| cfe383b9-64d7-3718-a3f7-4ddee30e47a8 | -6.7635 | -59.6718 | 2025-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 34.4 |
| 999685f8-84d8-3403-bc1a-0abf0f2983d8 | -6.8413 | -58.9552 | 2025-08-26 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| f155f782-5cb2-3c8b-a40e-7179f77c15ad | -0.29797 | -50.41788 | 2025-08-26 04:42:00 | NOAA-20 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a04d7cf4-79a9-3316-8da0-01669a3fc6f5 | -7.53312 | -50.54547 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9923f5d4-d331-34cc-b27a-ea175f3247b8 | -7.75094 | -50.28214 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ffdc5da8-d79c-333b-a059-1cb720666cd1 | -4.93336 | -47.55225 | 2025-08-26 04:44:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c172cb66-2709-3052-bf92-5c57c9a22adc | -6.19467 | -44.15492 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07c57f31-49b9-3d1e-8d2d-050747fa895c | -7.20795 | -45.31007 | 2025-08-26 04:44:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 822adab6-bd49-32f6-b673-ea8dad0a77a0 | -2.4874 | -47.75259 | 2025-08-26 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 940ac09c-3bb7-39f7-8fa0-43ff168e2ab1 | -8.47332 | -43.67183 | 2025-08-26 04:44:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 63cb0677-1791-328a-a7df-7e5c98f7c111 | -6.29563 | -43.77752 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c8aa854a-f087-3599-927c-272b1a880d61 | -6.05534 | -44.44595 | 2025-08-26 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 082e30c3-5e7b-3e86-937c-7c7249b42435 | -5.52838 | -60.21133 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2b8bf8fb-75c9-33a3-b873-32dec4ba4a79 | -7.74369 | -50.28469 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1a45a26e-d203-3ab7-ae50-4cdcb2ebe49a | -3.25157 | -46.90977 | 2025-08-26 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c6af334-a898-3649-bbf8-7057184f8a48 | -5.57023 | -42.62538 | 2025-08-26 04:44:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 8ebc1dd2-e9db-3284-98a3-7472edae1f71 | -6.24834 | -60.00967 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5bf38c7f-34b7-3aac-8ffa-b986bb8d95f7 | -7.74423 | -50.28118 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7783b441-0548-3e36-aadb-8fcff0a485f6 | -5.41099 | -49.19971 | 2025-08-26 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f71a36fc-09f7-3747-bd45-ed5d93c3938c | -6.18563 | -44.15292 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e0d6f18-28d1-3b48-8016-162b4bdfe637 | -1.94902 | -52.08235 | 2025-08-26 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26c89dc3-d0cc-3778-af9f-22ecb7946369 | -5.432 | -60.1772 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46d64c25-e564-399f-bddd-1bd4db311a1b | -3.98347 | -47.88267 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 24639403-abdd-3331-886e-8f3a9f22091b | -8.12517 | -47.12085 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18d46fd2-528d-313d-bb95-761b5c66df9e | -6.30955 | -47.41924 | 2025-08-26 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01a2d01e-7574-34f3-88a7-8fa874983f96 | -6.87055 | -45.65042 | 2025-08-26 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5bf50f50-2b57-37a1-b035-061cb1f27887 | -6.23732 | -60.01088 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 48678c24-7108-3e58-8f55-42e851684674 | -8.27035 | -47.22946 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fd3aee96-d349-3988-a0fb-3b67e22e9032 | -3.98063 | -51.06396 | 2025-08-26 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe17c9f6-1fa0-3976-9220-fa40d1591199 | -7.15599 | -44.17584 | 2025-08-26 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8cfa9dc0-3755-3dd7-8732-31f78314c23b | -6.25882 | -60.01159 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9072835e-1ccf-3ca8-bd36-7453c04e14c0 | -6.94513 | -44.17231 | 2025-08-26 04:44:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3b7838f-37d2-3d6a-a9a0-e38540676724 | -4.95826 | -55.81843 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 75c41acb-fd66-3935-ac65-0c62e170c457 | -6.8977 | -44.43754 | 2025-08-26 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 03418044-19b7-31a5-832a-91667a966e66 | -3.2479 | -46.90923 | 2025-08-26 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce7cf501-01e8-3d5b-aefa-83cf23af3e01 | -5.76298 | -53.77167 | 2025-08-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 97b7d786-0f52-3e45-a0ab-8aacaa8b13a4 | -8.12548 | -47.29296 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e0f81381-a7c4-3022-a1e3-ae95f60edbdf | -7.46952 | -45.00996 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2841ae2-1187-3724-bd2e-e702104adf3d | -6.64985 | -53.18679 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 040d91b1-00a2-3e2f-8b91-20ff67fdfc4b | -7.74704 | -50.28518 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5dc49ce-2f0e-3744-ae31-c96238a12ed2 | -6.19015 | -44.1539 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5985d11a-f574-3fcb-b9c1-debcd2868ee5 | -5.30308 | -60.20388 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96c82a6a-00cf-364c-a519-6eaf2f4d24ae | -6.25301 | -60.01395 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1bfaae5-aae4-347b-b815-8a3067a2b927 | -5.74433 | -45.37823 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4b07736-47d0-3eaa-abf6-c21f34d950e9 | -6.57695 | -59.88715 | 2025-08-26 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2258627-6ef8-30b3-9d0d-e47b3c9c9f12 | -7.46985 | -45.00874 | 2025-08-26 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5999749f-7120-3e9c-ad42-d5f786ad5e77 | -5.44746 | -60.15182 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 780eb1a4-ae99-3ef8-9e32-ba20dc329d38 | -5.30247 | -60.20737 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e3b9c063-6787-3cd6-a6b9-d3fc7376f819 | -6.08638 | -45.90383 | 2025-08-26 04:44:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 990ecb9a-4cfa-316c-92e0-2750f4b47588 | -5.59378 | -46.33803 | 2025-08-26 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cefca061-bda5-3373-b24f-bd6fac4396d0 | -7.57564 | -47.48822 | 2025-08-26 04:44:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fdde2b9-be5e-3f1b-b6f6-c438cb59abf8 | -7.52701 | -50.54092 | 2025-08-26 04:44:00 | NOAA-20 | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fb2db80e-dd78-3dbe-a4e2-ec07e1cc4d31 | -7.18735 | -47.57158 | 2025-08-26 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef0d9f74-8446-3d8f-822a-6f5b005ef1af | -6.28633 | -43.84244 | 2025-08-26 04:44:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79353efd-79c4-3fd1-a3e8-07c885c5b956 | -8.39381 | -47.39071 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d85ec26b-d46f-3289-babb-1423f2d14bf2 | -4.95767 | -55.82199 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ff347ad6-89e2-3579-9531-ee8764ad4b8d | -4.95944 | -55.81133 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 1fd655ac-8fe6-3679-a74c-6f87d32fdc64 | -7.74818 | -50.29988 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ec316ed0-e9d4-35f6-aeb9-c54b905d10fd | -4.12912 | -54.8998 | 2025-08-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cb76f4-484e-3f0c-80b4-3f8fb02862f0 | -7.74093 | -50.3024 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8ff2baf-842f-3bdc-aff8-fe81ba5cc6e8 | -4.93694 | -55.82202 | 2025-08-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 595315b1-2194-33e0-8794-4ec514cf9803 | -6.06678 | -44.00407 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82b4fa56-cd1c-3fda-b865-5505762e92d9 | -5.53494 | -60.20552 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 02dae8dc-5756-32ad-b7d5-04422d18c455 | -8.29202 | -46.33136 | 2025-08-26 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cd2844b9-996b-326c-bc6c-d74f46c56ccd | -7.73813 | -50.29839 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 348b691e-98f0-3362-9862-b9c31287478e | -9.16484 | -40.60525 | 2025-08-26 04:44:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 75ffb90f-706e-3065-8a57-1262255eca18 | -6.31393 | -47.41533 | 2025-08-26 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5789e2c0-d973-3c70-8ed0-bb48707679dc | -6.38787 | -45.31789 | 2025-08-26 04:44:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 805a4dc6-56db-3bb5-ae68-725dcebdda72 | -7.74148 | -50.29889 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18038222-d061-3fd3-ae25-1dba47844eed | -7.73868 | -50.29486 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 25a5f952-4ff4-3277-84d3-0d9ff2cc7f27 | -6.23207 | -60.01 | 2025-08-26 04:44:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4dc6573c-4ba3-30d9-9a47-8ee769b6706c | -8.07464 | -45.01598 | 2025-08-26 04:44:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 896173e3-aed4-3bcf-93f1-d41df44d40a4 | -6.03141 | -43.98783 | 2025-08-26 04:44:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f1cd1de-b25f-303b-8523-b29f401e8c85 | -6.34119 | -43.66203 | 2025-08-26 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d2e97901-7a69-3ca0-b958-896f0d18c389 | -8.31194 | -47.24047 | 2025-08-26 04:44:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1cc44b0b-e3f2-3dab-8c84-dbd94202255f | -4.70428 | -56.06623 | 2025-08-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 082efac5-5b04-3dfb-b48a-856abe710977 | -5.47486 | -42.61502 | 2025-08-26 04:44:00 | NOAA-20 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d5da6907-5b14-3f1d-9ebf-3c1fb83d7509 | -6.39665 | -43.51569 | 2025-08-26 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bad29636-02c6-309c-9fbe-9bf0d9ac7092 | -3.92297 | -47.69121 | 2025-08-26 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f60b41ad-b7a3-3181-8c87-2bee6fc58978 | -7.74482 | -50.2994 | 2025-08-26 04:44:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cc7d38f-32e5-37f1-94c3-d184a80f12ce | -6.7655 | -42.98879 | 2025-08-26 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |


[Clique aqui para ver as próximas entradas](README54.md)
