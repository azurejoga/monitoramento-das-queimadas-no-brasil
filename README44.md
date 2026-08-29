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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1b7e084f-cb20-3041-b559-57e9fe98c1ec | -10.89053 | -50.49813 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4826c517-9fa3-3bca-820e-cf655217df76 | -9.01824 | -57.54397 | 2026-08-29 04:53:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b24f003-179f-3bd1-a1c0-b746e8c9f215 | -10.75115 | -54.03545 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 645e6b5c-0615-3454-bc2c-d7bb5669fae8 | -8.59579 | -54.79705 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9e6c6763-f7a6-370e-ba9a-8438e12ed2b2 | -11.38196 | -45.13765 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2d4d029e-e7d9-3d4e-b6fc-d4a12af6bf24 | -10.53905 | -50.77945 | 2026-08-29 04:53:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9202d028-1720-3298-bded-3cb8d8422fed | -9.31234 | -47.62268 | 2026-08-29 04:53:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 41ba0da4-092e-3dcc-a088-3ccecbb82775 | -10.4865 | -64.50195 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 10cfc1f5-251d-38e1-9407-b11202b3d5c8 | -11.0378 | -57.21862 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 266b3266-5bce-3b52-8246-41d2260a6dc4 | -6.16851 | -57.78072 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 539f0ee6-98fe-320d-a6f5-bcda28225379 | -6.2017 | -55.41331 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e3c463e-a0a4-3b8e-8812-9de8d5272f01 | -10.50759 | -59.61972 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd0d619d-aa45-3ade-bfaf-583b0e369cee | -12.2458 | -50.53642 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 401dd3cc-e227-38db-ad8a-35453158331e | -9.20663 | -51.55045 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1a482cb-94c2-3d9b-92f4-72a5fac8739d | -7.36261 | -55.17826 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2109ad7c-eb51-3ddb-9599-4bd562de2b7d | -11.02462 | -57.23623 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f0ca2519-b00b-35d2-8068-50114ecfdf8c | -7.27281 | -49.84404 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5b835421-e9f1-3b65-973d-3f2486a0e33f | -8.59873 | -54.80159 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31d83d0e-136d-3fb8-9124-85015b2943d8 | -11.71571 | -54.52654 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b34df92-41a2-3a45-b673-fd06918b18f7 | -6.5354 | -55.24746 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 16f515e4-5e53-378e-a365-b0046a7bcc23 | -8.60275 | -54.7771 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf0cb68e-7e8f-3639-b718-d189f6702158 | -6.75194 | -58.7254 | 2026-08-29 04:53:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3cfadd42-8ad1-3f41-adfe-31f8d8ab139e | -11.711 | -54.53357 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| efa2e4f9-5d29-3f2b-b0f4-cd1a929dbb8d | -6.57429 | -56.54414 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 99f87108-f86d-3d5f-8c80-d315e0f37e5f | -11.06685 | -47.13202 | 2026-08-29 04:53:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8bbda987-d907-3907-95d3-ce88687a0a34 | -11.03729 | -57.24463 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a96a59f-2f4b-3107-8906-b876d41582f8 | -11.02497 | -49.68263 | 2026-08-29 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b178de82-c8be-35dc-8976-c4937c157845 | -8.5342 | -55.26318 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57efb55e-9d36-3ccb-8922-765b1ee38393 | -7.50713 | -55.28371 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e269a5c5-f220-346f-adef-c9644fe32dbf | -8.5886 | -54.79599 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8209cce7-c5b8-3e9d-abc9-dcce33324938 | -6.15358 | -57.78712 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4bfdcc94-0fd3-3d2f-9d9d-02487cded628 | -11.02716 | -57.22134 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3155baac-c3bc-3c68-a98d-8c97a6fb7bc1 | -14.07446 | -44.06007 | 2026-08-29 04:53:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f2bcc4aa-9ba7-3814-a837-616eeb524012 | -10.74993 | -54.0429 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88adc3b5-4a6e-3707-9ed3-75a5976ea4ba | -6.5109 | -53.60335 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6385dca-320e-36d7-9177-7e2618e53d8c | -8.58919 | -54.70309 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f595c2ac-9104-3749-a9c1-570790999e46 | -6.15151 | -57.78548 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a3a79232-33ed-3cfd-8d7c-a20e5255cef1 | -8.59287 | -54.79241 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 788482e0-d31d-3951-8990-211aeb6ea3bc | -11.02658 | -57.23554 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e5a0d1d6-b567-302d-bb4a-93d2108323cf | -11.14583 | -50.59354 | 2026-08-29 04:53:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee0408ba-7ea6-326c-b926-7b0cbfa9995e | -6.76419 | -55.66479 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4866fd26-c04c-36b7-a9ab-ee0f3d2f74bf | -9.4287 | -51.69274 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 92d38679-639e-3619-8150-0ba34ff3d9f7 | -6.76799 | -63.04626 | 2026-08-29 04:53:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| be254d9a-e708-3359-9f41-f394ab2413e6 | -8.94678 | -63.28665 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 5.5 |
| bed70cc3-b6ac-3442-a238-bd9067322926 | -9.2657 | -45.6429 | 2026-08-29 04:53:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| ec952a5f-6248-381d-8ae5-762d7ae03da9 | -6.48957 | -49.90508 | 2026-08-29 04:53:00 | NOAA-20 | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b605b04f-3d41-31b9-98f4-083f73a57563 | -12.76558 | -44.26488 | 2026-08-29 04:53:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccae375e-0f49-3ac9-bb1f-25d501913ec0 | -8.59646 | -54.79297 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a141844e-ea6e-39ab-8e3e-d076a4a51021 | -7.83354 | -51.36337 | 2026-08-29 04:53:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ebeb87d-e03b-380b-bda0-8edb74beb3b4 | -7.50044 | -55.27785 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9ddb027f-4486-34ed-8d86-4c8cb9849eaa | -9.92628 | -60.44186 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b883152-09f3-3d05-be38-4b6a5354d58b | -11.48268 | -45.06326 | 2026-08-29 04:53:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cc5e34d3-a656-3496-83a8-d5eb64c97518 | -6.76256 | -55.67448 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 93fcfb14-991c-360e-835e-da3a97c1a02d | -9.27758 | -57.07212 | 2026-08-29 04:53:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee978d91-5757-3cd1-94e9-5b25534375a1 | -17.57485 | -51.63815 | 2026-08-29 04:53:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccd346a1-ab67-38c6-8869-48d7cbb0b6ab | -6.43599 | -55.77429 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66d04fdb-7331-3f69-8efa-5fc2e6e39a60 | -8.04678 | -54.0117 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8155bd69-7477-35cf-8e96-37d925353626 | -11.24602 | -53.99501 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a0de99e6-6d0f-3600-8db9-180bba623921 | -6.94962 | -45.22747 | 2026-08-29 04:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c933044d-6794-3886-941e-a326434fe091 | -12.24924 | -50.53695 | 2026-08-29 04:53:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46d5608c-bcfb-3a74-bb4e-0e394f4701d7 | -7.50711 | -55.30694 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9bb078da-1e3d-3bfb-bc5e-023f0b45ac28 | -9.46569 | -51.58815 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 060471e6-4114-3538-bb8e-7442d37d2307 | -6.72002 | -56.34307 | 2026-08-29 04:53:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| def1faac-556e-3a2d-b20f-a32eb85ff470 | -7.0473 | -55.68507 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 967429c4-c1e2-3a06-bae1-f46ed5aee372 | -8.50126 | -55.32515 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a893945a-f680-330f-88d6-7d4271a8e13e | -19.28875 | -49.51862 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b8c294f7-5d51-36c3-8497-0582b1d7ede0 | -7.28976 | -49.95801 | 2026-08-29 04:53:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88039c6b-aab5-3dcc-b01b-ed2bb7bc4bfc | -8.9825 | -52.38617 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4152d15a-8917-35a4-ad40-0113931fc732 | -5.77795 | -57.58485 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64b8cf90-3bea-3c05-bfc5-b89af01a68a1 | -7.2571 | -45.86062 | 2026-08-29 04:53:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 167d6beb-7a86-3890-8fff-946ce9383a4b | -9.20554 | -51.5574 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f3020dcb-c6ed-388d-8d96-197febc6963f | -17.27931 | -46.03 | 2026-08-29 04:53:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 81ba7f68-a773-3a45-af1f-079cd4a52187 | -5.89356 | -57.75792 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| d785d4cf-0641-32d0-89f9-774bdb46cf49 | -7.59132 | -61.3471 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b902a3e-af3c-3018-ae5e-6bfc8955848c | -8.94812 | -63.27808 | 2026-08-29 04:53:00 | NOAA-20 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 549f5603-f606-342c-8a41-7d997b0f24e9 | -9.92682 | -60.43892 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 32e2b9d2-db48-316a-a2ca-ea461b3ba55d | -6.93785 | -58.95336 | 2026-08-29 04:53:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff90eb71-6e44-3af3-94a3-34faaa95d5b9 | -13.35073 | -43.65286 | 2026-08-29 04:53:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2441d5e-a569-34eb-9b28-ff223e54e935 | -7.49742 | -55.29597 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7fcce9c0-9eec-3691-8383-6b5dc15f5b2e | -6.40711 | -51.6829 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30860295-4c8b-38c0-bb4e-4e85b269d942 | -11.02411 | -57.24941 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 973ce606-4b03-389d-9cb2-6b499e8ca651 | -9.96712 | -53.93845 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc28041c-edee-35f6-b49d-9ae686d8ee03 | -6.77499 | -55.67133 | 2026-08-29 04:53:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6dd8bc2-2155-3910-991a-1a9a2a979822 | -9.91792 | -60.43102 | 2026-08-29 04:53:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 279f4d98-8d04-3746-8b44-401c05d4fc3b | -11.62939 | -54.5832 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 10b4612f-cd12-30d3-b9f4-245cb5ac9aa8 | -6.12108 | -57.69365 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fb4d62dc-929e-324d-973f-2114b9751264 | -7.55228 | -61.3093 | 2026-08-29 04:53:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0825b641-bdf2-3355-8b1a-4e1a0a98c42a | -10.4673 | -64.4978 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 7734eda0-c5a6-3cf3-819b-9fc88a058739 | -10.7609 | -53.97597 | 2026-08-29 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 877e33eb-b0ce-323a-97c8-3315b33eec5e | -11.2587 | -54.02374 | 2026-08-29 04:53:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4342f5f-e8a6-3dab-87f9-dcd0da841182 | -9.97116 | -53.93529 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 30b8c406-4ea3-301a-b2cd-20dfa1ef9c27 | -8.62335 | -54.69617 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 826d3f7a-ce76-3980-a544-aeb525671eaa | -9.39834 | -51.64858 | 2026-08-29 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| aeb4d176-09db-3912-aff8-df8db00958b7 | -8.59276 | -54.7037 | 2026-08-29 04:53:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ba42a927-cd60-32ef-ac64-9f13eff64052 | -9.97177 | -53.93157 | 2026-08-29 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d37e31ae-cfe0-3855-b41f-774ca8aaf201 | -19.27315 | -49.51427 | 2026-08-29 04:53:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6039fd67-8ef1-3169-83a0-27e8e15375ae | -12.78191 | -46.45341 | 2026-08-29 04:53:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 71c21d45-e917-3840-bd32-fea4a57b1e36 | -5.8838 | -57.76102 | 2026-08-29 04:53:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 9584d420-6294-39e5-bef1-0ec88a8ca918 | -10.4737 | -64.49919 | 2026-08-29 04:53:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c3b6b1e5-5c14-30f5-a12b-0ca66f4c5ecb | -11.03601 | -57.21751 | 2026-08-29 04:53:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |


[Clique aqui para ver as próximas entradas](README45.md)
