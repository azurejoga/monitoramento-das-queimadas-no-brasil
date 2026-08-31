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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0f6aaa6f-d932-31ad-abaf-920e6d11474b | -5.5943 | -42.3142 | 2026-08-31 14:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 78.9 |
| 1057bb79-edec-3476-a487-f1d820465719 | -4.9604 | -55.8424 | 2026-08-31 14:10:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 91895bee-e2d3-3344-ba56-86768186559d | -7.5845 | -61.3423 | 2026-08-31 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 3bf96067-8c70-35e6-a702-26ee3f3feb4e | -11.3806 | -45.1928 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 7580fe48-94db-389f-9de2-ed7edf24b404 | -13.9667 | -54.4157 | 2026-08-31 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 133.2 |
| abcc0e07-d8e1-336a-bcc5-050b66885dc7 | -11.2482 | -45.1194 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 191.9 |
| ad6ae3a4-39a5-3e2c-9d47-7bb1c5bd0d14 | -6.6221 | -58.5771 | 2026-08-31 14:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 1cbde330-9f86-3024-97b8-131605a9a931 | -11.2286 | -45.1452 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 074ddc3f-e5cc-3a76-b650-c0efd84bbbba | -11.2103 | -45.1017 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 6d1de87c-1e12-3a2c-8df6-0dd7d1a291c1 | -11.5479 | -45.4676 | 2026-08-31 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 99.3 |
| 4b8880d3-5e14-3a53-bc2f-69df4ede78c4 | -6.3892 | -45.489 | 2026-08-31 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 90.3 |
| b887a1e3-e019-3c5d-aae2-2140edb40bc1 | -3.6215 | -60.566 | 2026-08-31 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a691fe1e-ac06-31c0-80be-e63b3527e75b | -5.5941 | -42.338 | 2026-08-31 14:10:00 | GOES-19 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 10a2f3a6-f6d8-3eee-9f3a-7debf299de78 | -11.2295 | -51.2667 | 2026-08-31 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 68975ee0-f2ca-3c7d-82d5-2eab6b0538ba | -8.7442 | -46.4437 | 2026-08-31 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 6dd93e5e-7517-3653-ab7d-90b68cdf3ee2 | -7.9172 | -61.329 | 2026-08-31 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 6ce0f7ee-678e-3cc4-a952-af334def9a0a | -10.8046 | -50.5046 | 2026-08-31 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| e09007d9-1c2e-33c9-b559-b9926aa0a62c | -7.6251 | -55.2987 | 2026-08-31 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 6c75c231-af42-33ee-b0e6-75c2aa6965b4 | -10.8209 | -50.6945 | 2026-08-31 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 37ed5f5f-c917-3dfb-a4f4-1fd22a8fab31 | -10.7598 | -54.0179 | 2026-08-31 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 112e4b63-cacd-3f5b-8ee4-3b760301aa5c | -9.5961 | -47.6424 | 2026-08-31 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 7904e0ef-c1e2-3705-984f-6f46a9f6f0c0 | -13.967 | -54.395 | 2026-08-31 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 121.5 |
| 5ac1f5df-6fc3-3e7f-908b-99436b3b4bf1 | -11.3423 | -45.1982 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 4ade3229-6c3c-3a81-9cf2-59774222ab14 | -5.4876 | -57.1416 | 2026-08-31 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.9 |
| 5df1d311-c376-3138-85c1-811488ccb818 | -6.9368 | -55.6161 | 2026-08-31 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| f336f1b8-23bc-3614-aa2c-766a81649b9b | -8.1672 | -54.9246 | 2026-08-31 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 157.0 |
| 4d6f9498-992f-30a1-b317-4925746d51c2 | -11.7782 | -47.6697 | 2026-08-31 14:10:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| d8ed80e8-fd70-3e3e-a872-9470b7050718 | -12.9221 | -45.8582 | 2026-08-31 14:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 96.7 |
| c01f596f-a58f-391f-a52b-1bc3a3fc3d0e | -6.1295 | -57.6637 | 2026-08-31 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| 7f4f61fd-0b79-3045-ab87-ee5f473c9529 | -11.0936 | -51.5134 | 2026-08-31 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 82cf00a5-739f-33db-a310-f6375aad326f | -10.1341 | -45.7461 | 2026-08-31 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 104.5 |
| 6541944e-2399-31b6-9d59-5b4736c6a0fc | -11.1542 | -51.2324 | 2026-08-31 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| deb558a3-f158-3bf2-b626-750340fb5996 | -14.2796 | -52.8547 | 2026-08-31 14:10:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 74.4 |
| bc52a796-a688-3095-9d98-3a049666a79a | -10.7596 | -54.0384 | 2026-08-31 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| e0c00cb1-c965-32c9-a657-caf6047987f0 | -7.9907 | -46.5177 | 2026-08-31 14:10:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 147.8 |
| 910f36d2-e4f0-3099-a668-95d9023ed88c | -9.5967 | -47.5983 | 2026-08-31 14:10:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 135.1 |
| 9d6cb502-99d4-380f-b033-a91769951e6c | -10.7407 | -54.0401 | 2026-08-31 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 139.3 |
| bb638782-bc89-30ed-ad38-9540464030fc | -11.229 | -45.1221 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 110.0 |
| 72a56638-cd1c-35bc-8649-880d94584d76 | -7.5658 | -61.3811 | 2026-08-31 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 110.8 |
| f3ada407-1be4-3c23-8275-e969c919cf9f | -7.3118 | -60.5897 | 2026-08-31 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 174a1830-cecc-3a5f-8e26-a277ac119928 | -11.2485 | -45.0963 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 130.1 |
| 0ecb76f7-03c0-3e1e-8abd-5cccfcf00fb3 | -5.8967 | -59.9719 | 2026-08-31 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 942ff292-772b-33a5-8933-e882ece383d9 | -15.4601 | -52.806 | 2026-08-31 14:10:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 57e18403-d016-3195-8bee-ca76d27ddd03 | -12.9054 | -59.8857 | 2026-08-31 14:10:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| b39c2825-2770-3f3f-bcf1-69de423b0bad | -7.9239 | -44.2327 | 2026-08-31 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 142.5 |
| 1ed6bb78-8b5c-39aa-ba15-f982bc708a16 | -9.4342 | -45.6704 | 2026-08-31 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 814d01ed-7023-34de-9f10-d2bba64570cf | -14.5868 | -54.1153 | 2026-08-31 14:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 9d08e4d8-f1aa-34f6-a797-83ceb8b9126b | -3.6398 | -60.5656 | 2026-08-31 14:10:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| a527a02b-760b-3eb7-92bc-796c4d2ce71b | -8.1671 | -54.9447 | 2026-08-31 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 170177f4-6b3f-3953-a413-2397f3ae0640 | -8.7628 | -46.4642 | 2026-08-31 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 159.4 |
| 143a177b-7281-3afb-85d4-88a4fe262203 | -10.8212 | -50.6732 | 2026-08-31 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 77ea8fd8-d44e-37d6-b3fc-a65745448ff8 | -11.3236 | -45.1778 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 0e6d85a5-cd0b-32fc-9837-62e0897eb77c | -7.5659 | -61.362 | 2026-08-31 14:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.1 |
| e696a299-ea64-35c9-b56d-117222f64272 | -11.9378 | -45.0656 | 2026-08-31 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| f921870e-6301-3e68-b178-ff863164cb21 | -7.6253 | -55.2787 | 2026-08-31 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 582fb103-40cb-3031-8995-ae3f8dd9d290 | -6.9176 | -55.7166 | 2026-08-31 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fcc0c7f6-8883-3562-8a7c-c478757e2906 | -18.2904 | -52.6818 | 2026-08-31 14:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 134.4 |
| dde7a031-6fdf-3abe-89be-00a94b6e23c4 | -7.3119 | -60.5706 | 2026-08-31 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.6 |
| a5a0e489-11bc-32bb-93dc-55c94c3c5953 | -7.9425 | -44.2538 | 2026-08-31 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 106.7 |
| fb66d469-38a7-33b7-9b90-3d20d8ed28b9 | -18.2899 | -52.7035 | 2026-08-31 14:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 9e7eadf7-1d5b-3792-9268-cd2ace2742e5 | -18.2704 | -52.6851 | 2026-08-31 14:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 182.7 |
| 3a64a254-13d9-3451-92a3-edfff6986ce1 | -7.9236 | -44.2558 | 2026-08-31 14:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 102.6 |
| 1e0a9e2c-14de-3d2a-b25c-1674f57534bf | -8.8175 | -62.4898 | 2026-08-31 14:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| beed40f4-0795-3c80-89d8-8cd962d0458f | -7.2933 | -60.5905 | 2026-08-31 14:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| 0e6e16b5-8d7d-3e4e-a850-e1197860a03a | -10.1538 | -45.6982 | 2026-08-31 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 129.4 |
| e4d5c12d-b15c-39fc-b2bc-9687dae51e74 | -5.5831 | -60.2307 | 2026-08-31 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 150.5 |
| 722da5f9-5e3b-360f-9dbe-430ed746260e | -11.5475 | -45.4906 | 2026-08-31 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 42971c06-4bef-3bfc-9191-3d791d5564f1 | -10.8541 | -48.3587 | 2026-08-31 14:10:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 6915e1a1-3314-38f6-9d2f-61dacb5f748b | -6.9367 | -55.636 | 2026-08-31 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 134.0 |
| 0cb33744-e553-30c5-a074-ba969c5de759 | -7.9605 | -44.3212 | 2026-08-31 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.7 |
| c1be5e13-9f3a-30ed-8ba5-851c552d8082 | -3.6076 | -59.0769 | 2026-08-31 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 7c4b7fc8-d4e7-3e76-9d3c-6931559a584b | -7.9797 | -44.2962 | 2026-08-31 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.5 |
| 0f278d14-94d4-384e-aa03-4262a9c3b259 | -7.6149 | -44.8833 | 2026-08-31 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| f2d46e91-b0dc-3746-a63e-828580afff17 | -11.2294 | -45.099 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 4e522fa3-fcc3-366d-8737-a95d42e83915 | -10.7409 | -54.0196 | 2026-08-31 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 8b81a042-b81e-30df-b7f7-9e7861430072 | -11.2503 | -54.0146 | 2026-08-31 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| a77b5f5c-d5cb-3c18-aa97-5f2186acad74 | -9.0717 | -60.4918 | 2026-08-31 14:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.4 |
| c2ae936f-3dff-3ae8-847b-8d6a24bb567a | -18.2695 | -52.7284 | 2026-08-31 14:10:00 | GOES-19 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 56.2 |
| ab6fe904-06bc-3478-94bc-6b5f7edcfc42 | -8.7631 | -46.4418 | 2026-08-31 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 152.7 |
| 459e973d-fcb8-3565-b2fd-081d7b3da026 | -11.0747 | -51.5153 | 2026-08-31 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6370466f-a315-3430-9b52-61d5692eb27f | -11.0744 | -51.5365 | 2026-08-31 14:10:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 55a5ea69-758e-3e28-8989-a92f321d019b | -10.8624 | -45.3789 | 2026-08-31 14:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| 01446f60-a62c-369e-b989-ca08990cae7e | -7.1123 | -42.7727 | 2026-08-31 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 26ac84e0-974f-32f0-b071-6b9cb9796a78 | -8.7439 | -46.4661 | 2026-08-31 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.6 |
| 51678666-63b9-38f3-b4bb-926779052841 | -7.9794 | -44.3193 | 2026-08-31 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 413.5 |
| 79d85c08-9251-3114-b931-2e03e4db67c0 | -9.2092 | -51.5654 | 2026-08-31 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 181db2ad-2762-3379-8216-806f04f20953 | -11.2298 | -51.2456 | 2026-08-31 14:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 48a20af1-a303-30bb-bfd4-ee7f0a4865bd | -15.8844 | -56.4819 | 2026-08-31 14:10:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| baee7134-2811-3eef-9655-83a1599ed691 | -11.9186 | -45.0685 | 2026-08-31 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 112.4 |
| beb58a6f-9e4a-3368-a212-e536d1c13f59 | -19.14 | -57.35 | 2026-08-31 14:15:00 | MSG-03 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| f862b795-e257-31e9-a1f7-5e39bb27dd19 | -8.799 | -62.4905 | 2026-08-31 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 119.8 |
| 5686c92a-7c64-3970-b7cf-e168e1a3d813 | -7.6253 | -55.2787 | 2026-08-31 14:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 41d8018d-2393-326e-9535-409236bdc45c | -7.3119 | -60.5706 | 2026-08-31 14:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 173.1 |
| 88478d65-b95f-3e1b-9972-d972c319b523 | -9.2092 | -51.5654 | 2026-08-31 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 137.7 |
| d6767ced-5068-3f90-a3db-fe404fee1a42 | -9.2089 | -51.5863 | 2026-08-31 14:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 258d6202-cc64-3937-b0cb-6a25a09de021 | -11.1732 | -51.2304 | 2026-08-31 14:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 15c1617a-1ca8-353c-8c4c-8dc0a738b73a | -15.8844 | -56.4819 | 2026-08-31 14:20:00 | GOES-19 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| dcd1ae84-9d15-35fc-9380-86cc68d67bcd | -8.7989 | -62.5095 | 2026-08-31 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 104.1 |
| 14a26fd4-b7e9-3e6f-8622-1a795cccd15b | -7.9239 | -44.2327 | 2026-08-31 14:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 143.1 |
| c65ffbc5-a7a5-32b3-96b6-90cf7813acaf | -8.8175 | -62.4898 | 2026-08-31 14:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |


[Clique aqui para ver as próximas entradas](README92.md)
