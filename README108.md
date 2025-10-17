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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| caaae28b-d66c-3871-9077-47aa8e4c8318 | -8.45662 | -46.24459 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cdfd9929-d280-3487-95d4-f2be4965c6d4 | -13.57332 | -48.49038 | 2025-10-17 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4de9da99-c8fc-334e-be2b-c1cbf98b12bd | -12.43399 | -51.30025 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1c41ec9-5c38-3772-8ed1-a1f54e967412 | -8.82184 | -47.31002 | 2025-10-17 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1353189b-3746-3609-a294-3966a0524ba1 | -6.60483 | -55.53907 | 2025-10-17 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 482df7b8-5116-3927-b99e-c093459bdc4f | -6.53604 | -55.05403 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1fa6304e-51ab-30d6-b097-c03836689da7 | -12.1542 | -49.68385 | 2025-10-17 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e5ef40bd-2fd0-35f9-98b9-9fa3ff846f65 | -10.95507 | -49.77591 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 5398d61b-1599-365a-bc3a-5a5c695b572c | -9.2151 | -61.54182 | 2025-10-17 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d6c3b2b-78fc-3987-8103-679eb5dfc3a8 | -13.43049 | -47.94083 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bd3631a-f08d-3930-bead-f8994b59c9c2 | -8.4861 | -49.04712 | 2025-10-17 05:10:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 66ffb381-6385-331e-a70b-18325d61ed27 | -8.44763 | -44.18135 | 2025-10-17 05:10:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4c241254-e16d-3358-ab80-608064f6a51f | -7.32747 | -44.15697 | 2025-10-17 05:10:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b258e937-cf7a-3fe9-aa14-45c782b85d58 | -10.12354 | -52.34431 | 2025-10-17 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ef4068dc-feda-3a13-b422-02521a2de180 | -13.43229 | -47.96345 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f4b8f6d2-83d9-3056-9eea-fb43fe674252 | -8.4577 | -46.24274 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 55a03d6c-f7e3-3e35-8511-bfb62564e7e9 | -9.62418 | -49.12671 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3dd653d-7618-3155-872d-8257da5e833b | -9.14783 | -46.64077 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c00efd48-cc2b-3901-849e-b95ef4c7f44a | -10.42913 | -45.01798 | 2025-10-17 05:10:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ce15456c-b67f-38ce-9c18-e80cf3bdd2e6 | -14.41737 | -47.88841 | 2025-10-17 05:10:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 869fa9a2-248c-3d1c-b5d7-9a4d89c660ce | -13.41428 | -48.57867 | 2025-10-17 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03728ac3-36fa-3133-aa1f-2e30ca760eca | -10.12 | -44.55223 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e6b985af-adbf-3884-95ef-e6466ac5b267 | -10.10733 | -56.77073 | 2025-10-17 05:10:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| efa73682-34ef-3dfa-81d5-008eda0e10d3 | -10.95547 | -49.77293 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 47b45e5f-9c96-38d1-9fbb-7bdd0315ccd3 | -7.95271 | -44.15046 | 2025-10-17 05:10:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b633fb1-81c4-3290-9b78-ee3947a15f54 | -8.82821 | -47.30653 | 2025-10-17 05:10:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95bba9d7-203b-308d-bbd2-57d6bd2b7949 | -8.33305 | -46.23593 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a27b89c9-97de-3b5b-b3b6-c2f163adfc82 | -10.55277 | -56.81001 | 2025-10-17 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ecfc9ae8-1f1c-39db-8662-bed2ef934ba2 | -8.6213 | -54.56454 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43860dbb-6ef9-3bc6-b061-7f7016f658e3 | -12.42868 | -51.30457 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efe4069d-ff6e-36c2-9f8b-132d0a4ffe2b | -9.71296 | -44.5496 | 2025-10-17 05:10:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4f3de304-acb0-3a7c-866c-5e570e4f1703 | -12.41471 | -51.30267 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| ed76c9d4-3a19-31f1-a797-eec6c97651c9 | -8.12122 | -45.54999 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 022c8479-3bde-39cc-a16f-5fc9cbd8a351 | -11.57906 | -48.56569 | 2025-10-17 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6f5a3777-4aa1-3b76-92ea-672ae2a928fa | -10.28481 | -44.05325 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f4046514-b70b-3dc6-8b09-90cba7f98245 | -13.42896 | -47.93977 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67894743-17d0-302b-a5b4-9817e649f711 | -12.60397 | -56.51064 | 2025-10-17 05:10:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4405da90-e1c9-353d-a500-0d41b7fc3b96 | -9.14203 | -46.64819 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 628a5df3-1cb6-3e52-be1b-598468047f0e | -9.14097 | -46.6567 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| fe5d4baa-407e-3f13-b0b2-7d32cb792f86 | -8.33915 | -46.23731 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4fa8660f-4b48-3a8a-8de7-c08eb3e68959 | -12.41535 | -51.29771 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 24.0 |
| e84d7eca-445d-317b-9432-576b4e98b5aa | -10.1188 | -52.34762 | 2025-10-17 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2a0a4877-e430-34be-b5f4-bdd1d7f08987 | -8.08094 | -55.17854 | 2025-10-17 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19683c18-613e-3269-93c1-29a08db8e8c3 | -9.88157 | -49.11924 | 2025-10-17 05:10:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 20a94239-2400-3046-a60a-9bb5cd5cab26 | -8.11188 | -55.09197 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 85eb2b3a-9e30-3ffc-a516-2a8c3665608e | -8.33382 | -46.2329 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9bec582b-4f43-3c03-ba9a-caa74a531714 | -7.22344 | -47.86963 | 2025-10-17 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dbf8865-9657-3f0c-9799-365a0515cd2a | -9.50717 | -47.26604 | 2025-10-17 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ef40bf70-58d1-3c35-bc1c-62e4f61dd1a2 | -7.32669 | -44.16318 | 2025-10-17 05:10:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| cc6b324b-ea93-3e2a-8540-28afef3d290f | -10.25644 | -44.04642 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 98e33cbd-7272-3a32-b6d7-b655d7f8c90d | -8.40691 | -46.29462 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ed299a9d-36fc-3f1c-8b6c-b1ab6a3f25b7 | -10.98172 | -47.89904 | 2025-10-17 05:10:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fddfb8e4-c0c2-3ff6-955a-f7996efcdd89 | -8.37547 | -46.24751 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d2b97d7b-9e9e-370d-b3ec-e5a6b2f7bb6c | -13.4191 | -48.58652 | 2025-10-17 05:10:00 | NOAA-20 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 107533ac-0b81-31ba-8f2c-a9befcba325b | -6.52914 | -55.05297 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b80ba8fd-e048-3c7d-b10f-a63718401d0c | -8.63057 | -54.62525 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c1787f4-2c84-3db2-9521-3d227ed90150 | -8.45102 | -46.23924 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b7b5428-2944-3a48-8e06-e02a72c95264 | -9.07368 | -45.90943 | 2025-10-17 05:10:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7c40c99e-2350-3a67-8166-ab4701fd1244 | -10.9504 | -49.77227 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6cde778-90f8-3618-8213-898cd6fc51d0 | -13.74001 | -48.21114 | 2025-10-17 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0c081de8-851b-3e93-a444-a081a27453c0 | -8.12056 | -45.55519 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cea7a925-cef5-3d9b-9bb4-15f1bc1076b0 | -9.1534 | -62.41768 | 2025-10-17 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00864cee-bbd2-370f-887c-5846564087b5 | -8.33365 | -46.23118 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21d82cb6-917f-34a2-ac5b-dd5ff13306ef | -10.27412 | -44.04456 | 2025-10-17 05:10:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f194ced5-051a-343f-a8ed-94b6f4b1fd43 | -12.45189 | -54.48514 | 2025-10-17 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c3f7f6c0-a95c-3b96-9c2d-ff9d5516a884 | -13.93785 | -48.69099 | 2025-10-17 05:10:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43d89df1-5405-3aad-81db-8d07797a08ba | -13.441 | -47.95308 | 2025-10-17 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72defd9e-f9ef-3fe4-9089-76d6bc531133 | -10.64953 | -45.24621 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2c6732c5-4b8e-39fa-acc3-59db0681e1c5 | -9.75856 | -62.27071 | 2025-10-17 05:10:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b04c10ed-e05a-37b2-99b1-e3d79dbe12eb | -8.37493 | -46.25167 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d151a36-2115-392b-8d39-1363ae43cdfd | -7.33224 | -63.20875 | 2025-10-17 05:10:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5b1e9694-63a8-3c15-84b1-96a4340d3ba9 | -10.95626 | -49.76698 | 2025-10-17 05:10:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| ddd63c09-36e0-3db2-81cf-69b649f39958 | -6.53259 | -55.0535 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2819fb49-e2c1-3f99-9ad7-1f43159aad05 | -10.10244 | -44.63257 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 504b8e36-0d94-3cb6-bf55-91c202df19cd | -9.1417 | -46.64036 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2e28b872-7b8f-36ac-848d-6024d919f8d3 | -10.18401 | -49.50956 | 2025-10-17 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df3a3df4-6ac7-346d-a208-1c17d320f18d | -8.08918 | -45.43624 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2e9872fc-36ff-3009-8e4f-fc0558eeb193 | -8.62995 | -54.62935 | 2025-10-17 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| aecd8e1b-0228-32c9-a596-cf00f3e77a96 | -7.17369 | -46.93987 | 2025-10-17 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71c2de0d-3336-3215-9fdb-ebd16b816622 | -8.38471 | -46.32092 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6622f2e0-0446-3fe6-b34e-c85e8646d1cd | -8.19795 | -46.9311 | 2025-10-17 05:10:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c03ccbc6-34ae-351a-8b33-fa366f412157 | -9.15286 | -62.42028 | 2025-10-17 05:10:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c981e8-a9d7-3f12-9d3c-0a61e7302e50 | -9.1415 | -46.65242 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 29f3f41c-123d-3284-a933-7df7385e2ef5 | -10.0513 | -58.43269 | 2025-10-17 05:10:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b03496df-684c-32bb-bf3a-4958c966fa73 | -8.25032 | -44.02085 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2d1d7861-ebdc-38e6-adf7-43adbf15d063 | -12.71305 | -48.63297 | 2025-10-17 05:10:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5c15aa31-1a09-3935-9363-7a9d75d1ee33 | -10.52541 | -49.55294 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 32e24868-563e-3feb-926a-2030cfc5f87f | -13.28843 | -49.5811 | 2025-10-17 05:10:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9912ef7a-0f86-3f4f-80d2-02ef1109f1ab | -8.82479 | -50.05923 | 2025-10-17 05:10:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8cac8325-e941-35a4-82cd-7e3ce3f1afdb | -12.42001 | -51.29834 | 2025-10-17 05:10:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.9 |
| e25f5fce-d21d-3cd6-84eb-8c760ba0e3cb | -7.21797 | -47.86889 | 2025-10-17 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 55bc9742-e40a-3f71-a41b-1c1390f0126b | -9.14876 | -46.74146 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| afdd4346-a163-3411-9949-47753e4f67b5 | -8.25754 | -44.0767 | 2025-10-17 05:10:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87445a50-0e6a-37eb-90fb-ebaf25dd82d2 | -9.61814 | -49.13233 | 2025-10-17 05:10:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1ef734b0-0b79-3c2d-9ae2-f8082516f8ea | -9.13214 | -46.62847 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b07e43e-220f-3a4e-b19a-33b7493b8a96 | -10.64601 | -45.25467 | 2025-10-17 05:10:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9c0c76f4-298c-3dcf-96dd-db97009c370d | -5.14742 | -60.37575 | 2025-10-17 05:10:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a8a4f1d-8f40-3104-99ba-84855834966b | -8.39432 | -46.24725 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| ff9bb01a-995a-35a3-a65d-e4a0bd4eece6 | -8.3399 | -46.23438 | 2025-10-17 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7a857d2-34e8-343a-9e99-1d6bf9f17a00 | -10.13677 | -44.57956 | 2025-10-17 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |


[Clique aqui para ver as próximas entradas](README109.md)
