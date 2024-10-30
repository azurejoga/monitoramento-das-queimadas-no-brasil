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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3a626c4-e8dc-3bc6-abd2-a952a88b3445 | -2.92318 | -48.95672 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 485f6892-fbad-38ac-81c4-ea73f322b808 | -2.87773 | -48.90628 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7969cc14-4c8e-3bb2-85cd-96b9b6f1027b | -2.70324 | -48.63831 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6c9e91d-0ad1-34b0-a1f5-9b18aabc7898 | -2.69308 | -48.63674 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8eb37a17-2043-3dbf-b9a1-a44c3c79563a | -2.69196 | -48.64392 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f44ece17-c729-3c4e-ad18-1fc41e0f360e | -2.66079 | -48.53192 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae38f6b-9ef5-312a-80af-19e7280aa31c | -2.61601 | -48.32725 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 409db54e-7fb4-35d1-981d-bc09f8b34cc1 | -2.60977 | -48.25474 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8974d791-7382-3421-850d-bdbda0361540 | -2.58076 | -48.3967 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22fa07bf-e92c-34cc-96c1-37893505d98b | -2.5366 | -47.51549 | 2024-10-30 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9bcb0dfb-8929-3be2-a160-5e6f4221d843 | -2.50954 | -48.1338 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8eaa82b-bfa9-3e70-807b-58004d3420e0 | -3.11314 | -48.65247 | 2024-10-30 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 249791ba-9c9d-3e2c-bc3b-2964c0096c04 | -2.26939 | -48.06773 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3cee6a19-decb-3f6b-88f7-111be84d9693 | -2.20273 | -48.35822 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 32f68ea5-bb00-3e01-b581-93f866fdf170 | -2.16305 | -48.38926 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3da0871e-58ea-3ec6-9fa2-d295463a6d24 | -2.12963 | -48.38038 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1117db90-867f-3e17-97fb-b31757ec359e | -2.44884 | -48.48081 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 33a4ef7b-b18d-3050-9088-079b80064712 | -2.44562 | -48.61326 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76c78438-100c-3f5d-a408-d2ae96dc404b | -2.44547 | -48.50253 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1bb373c-7e30-30dc-ad12-43b4fced2860 | -2.44261 | -48.47614 | 2024-10-30 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| daf02722-4b76-365d-89a6-14e6fd33ffe4 | -2.39139 | -48.57955 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| bc48ac8d-dc1b-3809-b25e-c547a87d4a76 | -2.39082 | -48.58315 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8692cd7e-853b-3bc3-94a4-df6a79128982 | -2.33512 | -48.67366 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a6a5b994-2067-36af-8bf2-96f9f4415c66 | -2.31692 | -48.56805 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f7dfd56b-4674-3f0f-bcd3-f99c0d8513cc | -2.31637 | -48.57164 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 99a89fa5-352a-3de7-a145-31cf9bdd9e42 | -2.30752 | -48.51161 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2d93eb94-3d3c-32ce-bc58-b3a949134ae8 | -2.30352 | -48.58099 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9d52fb78-2fe7-38e8-95df-6208edb1bf05 | -2.30014 | -48.58047 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 12a7657f-244e-35b8-be40-ef3841a8a542 | -2.28888 | -48.49765 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1bad02b6-19bb-3305-9c0f-3dcd057f37cb | -2.28831 | -48.50126 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69e8767f-ef1a-38cd-b525-44e70370807e | -2.1936 | -48.8196 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e22515eb-8534-3e62-afe0-99ab86f0d52c | -2.19023 | -48.81908 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 00ccc253-aa9e-3cb7-abee-a466f89d15f8 | -2.18968 | -48.82262 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3a14893-870e-3e7b-94e8-027bd6527cd8 | -2.18632 | -48.8221 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce81c35f-1be8-3a9d-aea3-24b5a8f75121 | -2.149 | -48.5239 | 2024-10-30 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 413b7c6e-0c4c-3e08-951c-bd9f620cc385 | -2.14135 | -48.79318 | 2024-10-30 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bcdae0a-e07e-3c3d-966b-7ce7f0a65ab1 | -4.51667 | -48.76326 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88f17eb5-bce7-3aab-986d-ba8ab7f631a0 | -4.48703 | -48.11691 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21518669-42be-3d0f-a1a7-fd3756bb5459 | -4.48644 | -48.12076 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8deb6e14-ee0c-3d08-922e-da7b2dfc7314 | -4.44622 | -48.17343 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8d29baca-40c8-3051-a99f-77181f52047e | -4.44273 | -48.17289 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be3530a-5c4a-3378-b088-096bd1952ac2 | -4.36965 | -48.62793 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02b22b1c-db2c-366d-8bb4-85af68d9014e | -4.36622 | -48.62741 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d4cd1cac-73a2-3f9f-a23e-ba9c416231ef | -4.36323 | -48.22041 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| efadb647-287a-3cea-b1fc-286ca7d78be1 | -4.35578 | -48.1529 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8c1d32e6-421b-31b6-9187-0df59e8fd3ba | -4.34866 | -48.61029 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8f198ce0-2868-36c5-b869-9ed129c229c1 | -4.34808 | -48.614 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4b5d23e-3614-3815-aaaa-5d94639ca6e0 | -4.34581 | -48.60605 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7cd3e02b-5050-3e91-a473-683a080b28be | -4.34523 | -48.60977 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ef2943f9-3aee-39ae-af9a-7450304f56f8 | -4.34239 | -48.60552 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2483849b-b95e-3f1f-ad55-c56a6d2ace76 | -4.34181 | -48.60924 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bafa4252-c140-3a70-8e66-c33a28497785 | -4.23077 | -48.55859 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a52b9b7-454d-34ed-8c3c-6cad1bd89a99 | -4.22785 | -48.04453 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ac907e82-a0d2-3594-81fe-d4c4e4dcfe18 | -4.22724 | -48.04843 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7fb9219d-409a-3697-a03b-834ca56e97f6 | -4.94939 | -48.37239 | 2024-10-30 04:44:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 15821b13-8be8-38d0-88f8-49c23d09289c | -4.91203 | -48.64064 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00a4d9d8-edad-3e09-adb0-4ed88a1257fe | -4.91146 | -48.64436 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7a1ebd1-05f2-33d1-a9d1-91bc6fa3cdcd | -4.91089 | -48.64807 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d61cad42-467a-33d9-8b83-07bf4ebd5893 | -4.90859 | -48.64011 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20500d4c-54a5-34b0-a353-7e43f5b1489c | -4.90802 | -48.64383 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bdd4a374-cb9f-37f7-bf88-9c2a8177a0c8 | -4.90745 | -48.64754 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a138c81e-18a9-3f09-a9bd-02f9cec82bdf | -4.88754 | -48.59927 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21bcaacc-3b3c-3f11-99ad-faff343bd6e6 | -4.8841 | -48.59874 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aa4c151b-429e-3e8b-b474-1e83acc28f4d | -4.87151 | -48.56621 | 2024-10-30 04:44:00 | NPP-375D | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2d87ced-1761-3b16-b657-e11cccca05e0 | -4.85528 | -48.73881 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d289fab3-a993-3fd1-9ab9-f7c7ebce31ce | -4.85185 | -48.73829 | 2024-10-30 04:44:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c7e13bf-a91e-3e22-8d9e-15eb77b709bc | -4.79347 | -48.57806 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bcb5fce7-3f83-3dfe-ae15-99dca2f63c23 | -4.76149 | -48.04204 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4b2f250-7a38-32a3-8a52-a383e9bb0df7 | -4.69388 | -48.83534 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 631af251-7788-3fc8-8d5b-b2ad31e2aa76 | -4.59493 | -48.07301 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 534f56e9-c805-3a26-89cf-f25eea41e4df | -4.59141 | -48.07251 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a60e43c2-e68c-3628-a516-ea3317f67a08 | -4.57162 | -48.01384 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f6f8cfae-abab-3596-ae98-633f3d53c77e | -4.13212 | -48.1322 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| a1f96926-3326-3b18-882b-45b6a1c13fb8 | -4.13153 | -48.13606 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ad7aa193-d66c-3673-83ba-5d65f63fa07a | -4.12863 | -48.13167 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67555299-30d7-3528-b863-77c5c64b9b97 | -4.12805 | -48.13552 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a15b54de-31d5-3b07-acf9-c1996b2aa7bf | -4.11352 | -47.96759 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4b5d1b5c-39c7-3385-b24d-0be9b910c20d | -3.9555 | -48.12935 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 8eb67762-fed4-3a14-8553-48493c42f901 | -3.9549 | -48.1332 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b1a72fa9-e178-3f35-9068-33f44ea92d42 | -3.95261 | -48.12498 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 372948ca-f2f0-3b54-ac35-6f27fe4cb1bb | -3.95202 | -48.1288 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 73a91fba-03e6-3060-a5e6-41114ff0eb1e | -3.95142 | -48.13266 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9fd0107b-c654-3b6d-846e-85c48ddc6215 | -3.95083 | -48.13653 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 367dcf94-761f-3ac1-b64b-fb34bbe28594 | -3.94913 | -48.12444 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ade0894-9087-39da-acf9-de15fc300715 | -3.94854 | -48.12826 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d7193937-b1d8-32d8-af73-c03e430c3945 | -3.94795 | -48.13213 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7681af46-a865-3b20-8ecd-7a56e05694d2 | -3.94507 | -48.12772 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 840df47e-42ed-3fc8-9150-00aed95acb2b | -3.91187 | -47.9427 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9faf3a60-cf29-3532-ab5d-6a9d50e060fa | -3.76023 | -47.7368 | 2024-10-30 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b2ebca61-0a83-38d5-a5b3-ed494fea39fc | -4.14785 | -48.39799 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad8a3de2-5d79-3cd5-8ad0-c9f74e0091b3 | -4.14575 | -48.29759 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 756cc512-f6db-32f5-91f5-86404d0518aa | -4.1444 | -48.39747 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| e101eeea-1122-3510-8a56-01cd83f33952 | -4.13774 | -48.25769 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd5107b5-9ab9-3a6e-88dd-7a49ff5b2ec4 | -4.13427 | -48.25716 | 2024-10-30 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2d47cff3-2cb7-3ad6-8d66-6eafb6aa407d | -4.10585 | -48.50973 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d297faf1-e6f2-3190-a414-bdfaa1426ffd | -4.10528 | -48.51342 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f14e04d9-3172-32bd-a16a-809c9649e535 | -4.10241 | -48.50921 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 29e18852-03c3-3d96-83d2-337939cb1b4f | -4.10184 | -48.51291 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f304b38-102c-314e-a781-b996bca07c57 | -4.09898 | -48.50869 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 092f13c7-1117-3f45-9384-74c7320792dd | -4.09841 | -48.51239 | 2024-10-30 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README56.md)
