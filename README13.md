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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05ee181e-03d6-3a91-9f81-cf9644fc1d12 | -10.36779 | -57.50496 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3bc0c673-1648-366e-9983-7c86c7a6c234 | -12.21057 | -49.6197 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5cbc0594-a681-3295-adf0-74287ebf29f6 | -11.76435 | -54.36498 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a769e9f5-a675-35ae-96c3-1358baea8bd4 | -10.86347 | -53.77952 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12648a5a-3005-3306-9873-ae58785475fd | -11.90886 | -54.8265 | 2025-06-10 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b8fa11b-5e15-3b2c-af88-4cbfe61de1f3 | -11.76908 | -54.38225 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6041e201-9727-3ae9-95e3-4a9ccf9729ff | -12.29305 | -50.10902 | 2025-06-10 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4b9d5b85-1784-3bc0-8367-77c07e1f816d | -10.94696 | -55.32148 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c555b47-fc90-3089-b973-f74b00c09f29 | -14.19359 | -45.48737 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 4e5b7dbc-ea79-3a5c-8ee8-ed3e3c3ccf8c | -12.24958 | -51.43064 | 2025-06-10 05:08:00 | NPP-375D | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a26eec55-b4cf-3217-81a4-1149691ba7da | -13.09737 | -52.28878 | 2025-06-10 05:08:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 688bcca6-60a5-38aa-ac33-2620233369c0 | -12.42688 | -47.80299 | 2025-06-10 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e18c580b-098f-385e-b832-9c82e56e5864 | -11.06535 | -55.04585 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1bb1abdb-a8b5-35fa-9b95-688492617f57 | -10.94356 | -55.32094 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2524dd28-3843-30b2-9591-6487dd872e3e | -10.30904 | -59.09015 | 2025-06-10 05:08:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3650f642-2d8c-3c97-aa91-69d6fe7d9698 | -12.42643 | -47.80654 | 2025-06-10 05:08:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8efe212a-5de2-32be-8335-5a35f879cea8 | -13.06314 | -49.25235 | 2025-06-10 05:08:00 | NPP-375D | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 61b0698d-812e-34dc-87fd-01a360e65339 | -12.88057 | -61.64764 | 2025-06-10 05:08:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c0a8255-7c7e-3197-ae96-6481358a6ae2 | -10.32492 | -57.49432 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 48430592-adfb-3e51-8947-5d4b0ec15913 | -10.9464 | -55.32516 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eb95eef3-6b3c-364a-829b-f8ff47122379 | -14.20702 | -45.48341 | 2025-06-10 05:08:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed9dbf51-6ecc-39ee-9881-1d6e36b092b2 | -14.03923 | -55.13301 | 2025-06-10 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a88299f0-4d65-3d38-89c3-10a355bbe4eb | -12.13019 | -54.66687 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d97f78fd-28b6-3270-8e59-ef2b0fc178f0 | -12.13079 | -54.66289 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7b20988e-4e88-39c9-beba-62cfad4151ab | -10.36893 | -57.49787 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8dc0416c-0e0a-3260-8237-0326b5396192 | -11.83706 | -60.92847 | 2025-06-10 05:08:00 | NPP-375D | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 92678412-504f-3984-8773-561bef8b352b | -10.30393 | -57.1397 | 2025-06-10 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 68dedad2-645c-3a58-8662-b120481a18f0 | -12.28905 | -50.10353 | 2025-06-10 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 5d80b9a8-7d90-3e62-8b81-68177e9a569f | -12.13139 | -54.65891 | 2025-06-10 05:08:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 93de7cb1-f388-387c-aea3-eba95338a060 | -10.37171 | -57.50196 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1af97be-b6a6-3cd1-bf8c-616812d85999 | -11.14014 | -53.94844 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dae9cd72-317a-3a0e-8868-b5e2eb6edbc8 | -12.20579 | -49.61909 | 2025-06-10 05:08:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d70e95f4-1679-3628-8c0f-828f19cac250 | -10.87641 | -54.31726 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8caed719-c820-3151-b538-832782847b2f | -13.72144 | -58.67638 | 2025-06-10 05:08:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38fc1f19-ae7f-365b-b447-79feb64237b4 | -13.7932 | -54.31292 | 2025-06-10 05:08:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fc92d180-6240-37e0-887f-569c569b9e7a | -11.78989 | -54.77436 | 2025-06-10 05:08:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ed0a9b1-30af-3ac3-9d94-84dc272b8908 | -10.30116 | -57.13565 | 2025-06-10 05:08:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f112986-e410-3c06-9ea9-0788804e2c56 | -10.87701 | -54.31328 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6327c38c-c097-3a4f-ab91-a825e1508c9c | -10.9498 | -55.3257 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d1a85be-0f12-3637-9f25-317702e0f674 | -10.2573 | -58.45006 | 2025-06-10 05:08:00 | NPP-375D | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8d72214f-5357-3bd5-bdd5-05ef65c23856 | -11.36619 | -56.5606 | 2025-06-10 05:08:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7fe3bd0b-7082-3fa7-a8c7-dbc3b09217db | -10.37114 | -57.50551 | 2025-06-10 05:08:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9382cdf-0dd7-394a-9c71-b683b99ec77f | -10.94867 | -55.33306 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1bbcde-1936-3e7e-b87c-b62a8f2b2a51 | -14.03337 | -55.12393 | 2025-06-10 05:08:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 515df9e4-59b6-309a-87ec-40021f55e005 | -12.28842 | -50.10838 | 2025-06-10 05:08:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0b762a3e-3e17-3add-be7f-3067faa6a20f | -10.8418 | -53.77631 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 93549b40-d063-30db-b7b1-4246c165e4a0 | -11.7673 | -54.36958 | 2025-06-10 05:08:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2fff66cf-0a50-349f-8bf2-dbdeda504f9e | -11.58902 | -51.33442 | 2025-06-10 05:08:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46f98801-0716-302a-9aa8-abd41fb6bb0d | -10.88054 | -54.31382 | 2025-06-10 05:08:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb42c3ce-3652-3b73-837f-e637bdc936b3 | -10.94583 | -55.32885 | 2025-06-10 05:08:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 94828ce5-f862-39ad-9c21-51390bf08ca0 | -11.90793 | -54.82745 | 2025-06-10 05:08:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0cc54085-59b2-3881-aefd-008b0e857e83 | -5.2106 | -43.33 | 2025-06-10 05:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 3d6d7061-3f63-34ab-99fd-1ea18aecefa9 | -5.2108 | -43.3067 | 2025-06-10 05:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 49a19223-bef1-35da-b1cb-0675ccf02b30 | -20.82376 | -54.95488 | 2025-06-10 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 478cb8c2-c1fb-3c49-9261-fddeb770e77a | -21.5904 | -57.58656 | 2025-06-10 05:10:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ad1f80dd-b338-3625-b739-f2669ae433d5 | -19.38577 | -55.11514 | 2025-06-10 05:10:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2010b19e-cb25-367c-8f4d-72a5d826f5cc | -19.38511 | -55.11983 | 2025-06-10 05:10:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b935ed3-0a38-3c83-bfcf-e10627c14cdc | -21.029 | -55.64782 | 2025-06-10 05:10:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 44b8c978-0d80-3c40-aab0-9118cd8bf861 | -20.8231 | -54.95975 | 2025-06-10 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0eb69f98-2f52-3f79-aafc-a6f70815c3ac | -20.82202 | -54.95648 | 2025-06-10 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bbb776bc-35aa-3a47-8690-01a668bb20be | -20.82583 | -54.95708 | 2025-06-10 05:10:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a70e889f-f7f1-3572-83f9-c4f49f18281f | -5.2108 | -43.3067 | 2025-06-10 05:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 1f30a5b1-38e2-3204-9ef2-1dc8e91fd32a | -5.2106 | -43.33 | 2025-06-10 05:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4e0c06da-3a54-3066-92d0-6f523328da2f | -4.30859 | -48.08166 | 2025-06-10 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 74014780-de6b-3812-b5f2-1b8a018c9291 | -4.30395 | -48.07944 | 2025-06-10 05:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ddc5cbce-9133-35f1-8210-09d3506c595a | -9.55972 | -64.62479 | 2025-06-10 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 088f5e5e-3801-3b0e-845e-d86cfc77e13c | -9.9257 | -59.92075 | 2025-06-10 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3dfd79e8-451f-32f7-813b-f3145dcaa9d0 | -9.08462 | -63.6974 | 2025-06-10 05:27:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57e66a7c-0822-398c-8427-ca9ca7d74686 | -9.92748 | -59.93361 | 2025-06-10 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 739dbdda-56b5-3556-8dd0-c7bf655f4f4e | -9.43037 | -62.11084 | 2025-06-10 05:27:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 319026f7-7e33-3527-9fa9-9abe81559eb1 | -9.20756 | -48.86435 | 2025-06-10 05:27:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4cfde9bf-6639-3662-93fc-05832491659c | -10.9491 | -55.32402 | 2025-06-10 05:27:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6547a49-ca0c-3304-b787-e2b7360f14de | -10.84665 | -53.7694 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3639c60e-71e3-3765-be3a-8851a8c1fd76 | -10.84083 | -53.77205 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 71074208-6064-3d72-9e33-3facb1138abb | -11.13308 | -53.94596 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ae2d1a8f-deea-3ad4-a646-c0b2f7a7e8a9 | -7.59282 | -63.77667 | 2025-06-10 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 953338bf-20e3-397f-81a5-a8123a61575c | -8.99798 | -49.19997 | 2025-06-10 05:27:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8cbf5e75-7bc5-339e-9516-db051845592f | -10.8404 | -53.77537 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3b13c001-2fcc-32f7-91f5-155cc0f0b6f5 | -10.88258 | -54.31557 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2183eb3a-8cbc-3ea2-867d-93758ddb3c20 | -10.30735 | -57.14012 | 2025-06-10 05:27:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48f9479f-9082-3d10-b41f-485bcbe6f6c5 | -11.13842 | -53.9467 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4f8f0981-f880-3745-89a0-0a6592b4aa1d | -10.88299 | -54.31239 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2fa7b539-9c52-3d20-8b86-69c54d0edfb5 | -10.83544 | -53.77134 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47f88951-b783-3302-a252-6d1127156b6d | -10.87737 | -54.31495 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0267daba-d925-35d4-8019-4abebf1a2b17 | -9.7087 | -57.87637 | 2025-06-10 05:27:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67791366-c8f8-3b3e-be0d-365f68901bbc | -10.36762 | -57.50521 | 2025-06-10 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06858e30-96c6-3c7a-8223-02c516f67108 | -9.55631 | -64.62423 | 2025-06-10 05:27:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e27b30d4-586e-3ef8-948d-108bc53a1def | -10.37177 | -57.50581 | 2025-06-10 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db384a08-da1e-3866-a606-9242928a8a73 | -10.36816 | -57.50142 | 2025-06-10 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5217149b-e4d1-320b-974e-5f5420b86dea | -9.92314 | -59.92199 | 2025-06-10 05:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 66a51f19-54f3-3486-906a-e0a2cc9f3535 | -10.86153 | -53.78141 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f34ed1f0-1fd7-3515-852f-75dd840fcbfd | -10.23872 | -52.21894 | 2025-06-10 05:27:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2f50e3a-cb9e-3062-b63d-b382b71b5040 | -7.89307 | -61.4734 | 2025-06-10 05:27:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d56666bd-1b75-3d3e-ad58-db65bddaa9b4 | -9.00204 | -49.57524 | 2025-06-10 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e437e642-74ef-3895-b6f3-bf13d6896a49 | -9.0089 | -49.5761 | 2025-06-10 05:27:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6533e499-9815-3656-9cc1-bfa8a24c0e63 | -10.24065 | -52.22111 | 2025-06-10 05:27:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cd1e6a66-33e0-3e63-bfad-a42eb2d44d8a | -10.37231 | -57.50203 | 2025-06-10 05:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ea0897f1-139e-3a2a-bfb7-2de04b57601a | -7.58779 | -63.77575 | 2025-06-10 05:27:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 64babc96-f7bb-3e6b-95ec-b1c84c791195 | -9.93857 | -57.48754 | 2025-06-10 05:27:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c817c63c-7aa2-3c87-8739-4969de9a5815 | -10.84126 | -53.76869 | 2025-06-10 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |


[Clique aqui para ver as próximas entradas](README14.md)
