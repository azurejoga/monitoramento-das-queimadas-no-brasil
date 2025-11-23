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
| 2df56c9e-b607-3b48-a088-bc2b3b09a637 | -1.24893 | -52.63557 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 05d5aa4f-2221-374a-afbc-6ddb75288ca7 | -0.85702 | -52.70939 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c8a45695-681a-3b00-8944-47e74fc126c0 | -2.87153 | -45.45389 | 2025-11-23 04:53:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5e9969e5-ed9b-3690-8b50-6800e41e7b71 | -4.0419 | -50.48053 | 2025-11-23 04:53:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69b939e5-9e8e-37bc-9404-c787bddc6e36 | -1.31256 | -53.14173 | 2025-11-23 04:53:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9644d57a-468d-3fa2-8df6-ed50c51ca969 | -2.04825 | -52.04885 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5a33359e-c9ae-3173-9ca4-cd681bd18051 | -5.54709 | -41.03994 | 2025-11-23 04:53:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 00c2e9d6-6bf7-3710-824e-0242125acefd | -2.01712 | -52.35301 | 2025-11-23 04:53:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd627222-961e-3e9f-a20c-5785703a47e4 | -4.61136 | -45.6287 | 2025-11-23 04:53:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 49635a6a-52f6-3df3-9a6c-a63e7b8a7a65 | 0.94487 | -50.08989 | 2025-11-23 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e83c025b-d264-3f1a-b225-97feb2a9ad83 | -6.3179 | -43.82382 | 2025-11-23 04:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 123dfe84-2cd2-3ef0-abb6-a42ac82d78b8 | -9.55658 | -47.77097 | 2025-11-23 04:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| af47e758-13d3-319e-9e35-0512921a3f06 | -7.73929 | -47.25229 | 2025-11-23 04:55:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4881f3d-41c8-31ff-b83c-4acffcc97bf7 | -7.30641 | -48.39434 | 2025-11-23 04:55:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16106a44-c8e5-388f-a267-e45396ca0542 | -9.55183 | -47.7743 | 2025-11-23 04:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 527d478c-3a5a-3a6f-9cc0-5d652e531093 | -5.60249 | -45.37586 | 2025-11-23 04:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71f7387a-f195-3367-a13b-684066a28276 | -6.88063 | -47.24347 | 2025-11-23 04:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6fe0f70-2a3e-3b6c-a78d-65bfeb0c53fc | -5.67867 | -48.78728 | 2025-11-23 04:55:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be6253e9-2b3d-365f-88d8-7f76230f8dd0 | 0.79288 | -51.96774 | 2025-11-23 04:55:00 | NPP-375D | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bb9bc58e-7cf5-3e52-a738-377cbe0a37dd | 0.94431 | -50.08639 | 2025-11-23 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4e671687-7975-3170-adcb-d439706a7ca0 | -7.30252 | -48.39374 | 2025-11-23 04:55:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a9700b78-0dfd-335c-9ca4-dfe2d7cbbc4e | -6.31268 | -43.823 | 2025-11-23 04:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3bda43ef-8f24-3782-9374-54ffb06e1376 | 0.94292 | -50.09055 | 2025-11-23 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b60a1cfe-8a1d-3c83-a91a-d796ace4b906 | -5.14116 | -47.47115 | 2025-11-23 04:55:00 | NPP-375D | SÃO FRANCISCO DO BREJÃO | MARANHÃO | Brasil | 2110856 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9591901e-a5be-3fe8-9bb6-bf1ecfbcdca4 | -6.11352 | -45.83401 | 2025-11-23 04:55:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5107b20-1c51-36f6-8afa-3b2a9d3f7dad | -5.67429 | -48.79109 | 2025-11-23 04:55:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5b5b9a7-7c52-362f-bd55-355b3cfdd5ea | -5.98127 | -40.38494 | 2025-11-23 04:55:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 25b96dde-4ed4-3002-95c4-2b8656f96b58 | 1.05639 | -50.06531 | 2025-11-23 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d6623b93-a0d7-3f22-99e6-90fb088309fe | 0.86014 | -50.72804 | 2025-11-23 04:55:00 | NPP-375D | CUTIAS | AMAPÁ | Brasil | 1600212 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| da5cdc2f-9261-3624-b20d-37b8acd4149d | -7.29882 | -48.41827 | 2025-11-23 04:55:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| b396165c-052d-3d79-b826-8738fdd15b0f | -5.67801 | -48.79166 | 2025-11-23 04:55:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7325ed22-3a6b-3329-9776-5dde3c328a7e | 0.69197 | -51.45991 | 2025-11-23 04:55:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3df32684-0d50-3f04-961e-74e27fbfb764 | -5.97474 | -40.3842 | 2025-11-23 04:55:00 | NPP-375D | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 16.7 |
| 685c22d2-a9ae-372d-ade8-112e00bcbe62 | -5.67735 | -48.79605 | 2025-11-23 04:55:00 | NPP-375D | SÃO DOMINGOS DO ARAGUAIA | PARÁ | Brasil | 1507151 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0d15e90-b870-30da-bc6b-d7b8bb539517 | -9.55239 | -47.77044 | 2025-11-23 04:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81540d65-cd15-351a-bdf7-95069fda107d | -9.55602 | -47.77485 | 2025-11-23 04:55:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| daa1e04c-3dce-3507-b579-0ac8a65eea11 | -6.88118 | -47.23965 | 2025-11-23 04:55:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd9592c9-a3b2-3993-b224-21f0b987648c | 0.94237 | -50.08706 | 2025-11-23 04:55:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6bc91b6f-c2a1-392e-a5a2-b648233b5e5a | -6.37764 | -46.32769 | 2025-11-23 04:55:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bf9ef7eb-bec9-3cb0-bf20-50940d87e9e6 | -0.94519 | -47.166 | 2025-11-23 04:55:00 | NPP-375D | PRIMAVERA | PARÁ | Brasil | 1506104 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a086dbe-8dd2-3c70-aeb8-3d775d454a1b | -18.50041 | -55.52381 | 2025-11-23 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 1249e687-2500-3fd4-be4a-ba71f0d21087 | -18.1011 | -54.52192 | 2025-11-23 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 52bd6dec-792f-32ec-a9c9-a7f3df5b9364 | -19.23801 | -54.29451 | 2025-11-23 04:57:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 35eecdf4-f2b3-3c1d-9cf7-56d8e5246f21 | -18.16122 | -54.55466 | 2025-11-23 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 91217d27-f020-3032-b988-3db77e4cfde3 | -12.32447 | -57.33464 | 2025-11-23 04:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 1e2fc9a5-054b-3d53-873f-c5b3b9acaa46 | -18.09775 | -54.52135 | 2025-11-23 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.2 |
| bcabfd5e-c20e-3f6d-ae62-a3c5f2209ee1 | -11.49337 | -58.44234 | 2025-11-23 04:57:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2d01dbc2-b569-3cf0-927a-d1665e8aeaa8 | -18.10444 | -54.52248 | 2025-11-23 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80dbeff1-04a9-3329-9663-ead982d3213d | -18.105 | -54.51881 | 2025-11-23 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6a97f575-09ff-39f0-9672-f91c95b62948 | -18.50373 | -55.52439 | 2025-11-23 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| a914e0e9-a45a-382a-8788-434556f4b1d6 | -20.86575 | -56.04916 | 2025-11-23 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e50654d-c016-3799-ad10-abae84172194 | -20.88483 | -52.32482 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 42671269-7705-3c63-baa9-111e3bd29986 | -20.88359 | -52.33401 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 3fafd875-ddc8-30d1-8465-5d8485cc7e71 | -20.88791 | -52.32996 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70279ab7-ad12-3cb8-a573-ed14eca65586 | -20.88421 | -52.3294 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 02bb30f1-ee4c-32f8-8b84-bae0042613ac | -20.88052 | -52.32884 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1a8190f5-eaa2-35cb-aabb-36397daaec30 | -20.86633 | -56.04547 | 2025-11-23 04:59:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b396c70c-7ec0-3775-a9d6-be144c2df8f3 | -23.94069 | -55.28278 | 2025-11-23 04:59:00 | NPP-375D | PARANHOS | MATO GROSSO DO SUL | Brasil | 5006358 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bcb7797b-84a9-3f47-82a7-0e8d41ff1e5a | -20.88667 | -52.33916 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 30f18ba0-1d5f-3b3e-81b9-e9f1a9f979f6 | -20.88729 | -52.33456 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7bd87491-3188-3a0b-a605-90e1359c2c9f | -19.54997 | -54.94985 | 2025-11-23 04:59:00 | NPP-375D | RIO NEGRO | MATO GROSSO DO SUL | Brasil | 5007307 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e46dafa6-652f-3491-bdc1-1dc18197d0b8 | -20.20753 | -56.6145 | 2025-11-23 04:59:00 | NPP-375D | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| eba5efc7-5111-39a3-a82c-a52adf0a252b | -20.88175 | -52.31966 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bdad48c5-ad16-3ca4-a9bb-d0c73aff2778 | -20.88113 | -52.32425 | 2025-11-23 04:59:00 | NPP-375D | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f5dded2-3998-3ae3-a17c-31e2bd101865 | 0.94509 | -50.09062 | 2025-11-23 05:14:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1e79f23-814d-3bb4-89d8-2c72c99c7ac6 | 3.98926 | -59.62091 | 2025-11-23 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 765e9f06-ae70-3068-a7be-b615b39926e4 | 1.9651 | -60.5634 | 2025-11-23 05:14:00 | NOAA-20 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9a34b07-bb57-343a-9d62-5b4c30240073 | 3.5838 | -60.02126 | 2025-11-23 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d79caf6f-a967-3919-9f87-6cf295847ac4 | 3.98804 | -59.61306 | 2025-11-23 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 05116110-6fc8-3b9e-a92b-38595dc87cea | 3.88711 | -59.87608 | 2025-11-23 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f1f0520-869e-30a6-bcbe-d6395007ddea | 3.58017 | -60.02182 | 2025-11-23 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79206ca5-c643-3cd6-a534-ff9b1430c484 | 0.9443 | -50.08566 | 2025-11-23 05:14:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 347eebeb-a760-32ec-bbe4-1146fcd6d10b | 3.58082 | -60.02602 | 2025-11-23 05:14:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b9f48dbb-8545-3d3d-b97f-7e4e1b73e53c | -1.30766 | -53.14642 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| eb356583-1120-3a55-8549-aa6e157d6b3b | -4.71673 | -46.46864 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 1838fe22-84a9-31ef-9327-6a1477a4520b | -2.8787 | -45.28941 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5a36071d-864d-3650-8f6b-a5bb93e88576 | -2.88413 | -45.28933 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 06564941-8f92-30d5-b97a-88b60959a517 | -1.31555 | -53.14767 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb0aacc6-bfd2-37c5-abdb-a4ac7a447360 | -1.31081 | -53.15208 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddbddff3-a526-3ff3-97a6-8f71b7d6350b | -1.33431 | -55.3959 | 2025-11-23 05:16:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7733a6fb-8b7f-3c6e-927f-6a7b2b3eef57 | -1.31476 | -53.15268 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9980f4a2-1c77-3276-9d55-90602be18139 | -2.88643 | -45.28413 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 24974aef-bfee-35c1-aff8-e4649afd97a8 | -1.73911 | -52.01759 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f18573f-9c14-36f9-acfe-84b03c6dd573 | -1.66993 | -52.04878 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 54e7b7b5-300f-3171-ad64-11aea035f08a | -1.74524 | -52.03502 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2490cd9e-f967-38d7-9038-7f6ea20b60f4 | -1.74156 | -52.03035 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8906f3d8-e1d1-3776-8ac2-6078aaa21193 | -1.09596 | -54.10516 | 2025-11-23 05:16:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f581b56-86cb-3155-adec-119cbe8c045d | -3.38833 | -47.19395 | 2025-11-23 05:16:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 65b36231-48b3-3335-85d7-3892b3cda707 | -2.87961 | -45.28318 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| eef59bf5-0aa3-3cef-99fc-1413bb91d526 | -4.71108 | -46.45991 | 2025-11-23 05:16:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4f5d40fb-a009-334b-a660-0e027daca0cd | -2.9492 | -45.43876 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 70ec8145-c537-3abb-b910-9e02a5e6fa32 | -3.17397 | -52.95796 | 2025-11-23 05:16:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 880c6667-4848-326d-8bd6-02925a35e5d1 | -1.32344 | -53.14894 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 032149ac-8fb4-33dd-b593-f651134b7150 | -2.89415 | -45.27887 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c5191a16-7ce9-3707-b224-7fb7bb3c956a | -1.88677 | -50.97313 | 2025-11-23 05:16:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| da52cba0-4088-37bb-895c-d27cb93b53a6 | -1.74646 | -52.027 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 898a019a-9bcb-33ce-be12-bcb483078314 | -2.0469 | -52.0504 | 2025-11-23 05:16:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8a3ef1d-39b9-3203-b027-42253c4f8712 | -1.31634 | -53.14267 | 2025-11-23 05:16:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 537ea777-618d-33cc-ab7c-77d31bb689b5 | -7.30423 | -48.39554 | 2025-11-23 05:16:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d923fc93-5091-3101-8b85-5e36b35ff358 | -2.96028 | -45.43829 | 2025-11-23 05:16:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README11.md)
