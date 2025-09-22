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
| 867936b4-3e70-3cd6-990b-2d4c12fb7cd1 | -15.9969 | -59.4651 | 2025-09-22 00:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| d7196066-3725-34e0-acd6-00bbea1ba2c8 | -22.9255 | -48.1819 | 2025-09-22 00:40:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 80174493-b999-33a5-bb43-297594f804cc | -11.6439 | -52.8397 | 2025-09-22 00:40:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| e48fc321-1c46-3f17-9757-09552ffc77a7 | -20.2735 | -55.5141 | 2025-09-22 00:40:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 0950d6a8-0aa9-38c6-a0ea-90b8941c97f2 | -10.3755 | -46.1015 | 2025-09-22 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| b6c6264a-a974-3cee-bacb-35ecd728c9e8 | -10.3382 | -46.0609 | 2025-09-22 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| cc4ddaf1-ffce-31b5-845b-4eafd0e73c3f | -10.3568 | -46.0812 | 2025-09-22 00:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 304.0 |
| ddc4a842-ea5c-3e66-8b4c-e8723b449a56 | -19.6475 | -57.7478 | 2025-09-22 00:40:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 77.8 |
| 9819c1c2-5798-3866-ab61-c8f5b3facb27 | -4.3196 | -48.1125 | 2025-09-22 00:40:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 19d000c5-454d-31c9-ac2e-a584c529c052 | -22.9044 | -48.1873 | 2025-09-22 00:50:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 107.6 |
| d683d9c2-2f77-344d-9696-87fd5afae153 | -22.8117 | -50.6021 | 2025-09-22 00:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.1 |
| e4df1b9e-d1bb-3a5d-a118-94a39beb2332 | -15.9966 | -59.4851 | 2025-09-22 00:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 71c17419-651d-353a-a511-662d7f94e658 | -14.333 | -47.7882 | 2025-09-22 00:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 8a761d64-fab7-3c65-92f5-054fba2adfad | -14.3525 | -47.785 | 2025-09-22 00:50:00 | GOES-19 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 6b49282d-a2f4-3532-88e9-59a4c5d563ee | -20.2735 | -55.5141 | 2025-09-22 00:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 103.9 |
| a11a4c9f-7720-3b51-be1c-adf7f63b389c | -22.9828 | -48.3559 | 2025-09-22 00:50:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.7 |
| c3fd67ca-925a-312b-b86e-db5bd882e377 | -11.6249 | -52.8416 | 2025-09-22 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 27303a90-8330-3f51-bf59-88e15dd89772 | -22.811 | -50.6251 | 2025-09-22 00:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.5 |
| b494b2d9-d4d1-3470-9d29-b473e4ba7ee0 | -11.322 | -54.3359 | 2025-09-22 00:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 1479e27f-1bfb-3712-ad05-2bf2a931d57a | -22.9255 | -48.1819 | 2025-09-22 00:50:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 48635ffa-ab50-3a78-869c-d31ff06761ce | -4.3197 | -48.0908 | 2025-09-22 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| b2b3889a-b434-3908-949f-20ac015e3eb1 | -11.6247 | -52.8624 | 2025-09-22 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 75e90a2d-8ab5-3433-bba0-c86a6cd134ec | -11.6439 | -52.8397 | 2025-09-22 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| bc905218-220f-3baa-bb82-fb9d871a00e1 | -11.6436 | -52.8605 | 2025-09-22 00:50:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 117.3 |
| 9aa75ffa-c264-3188-b142-490e17fddc7d | -19.6278 | -57.7296 | 2025-09-22 00:50:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.1 |
| cf960898-c2d7-3393-8dda-6b2808d0010b | -22.832 | -50.6203 | 2025-09-22 00:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.7 |
| 18455231-cefc-32b9-996f-f6381f74682d | -4.3012 | -48.0917 | 2025-09-22 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 7bcf4119-60e6-3b38-a2ce-59a1afe0ae3f | -20.274 | -55.4927 | 2025-09-22 00:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 211.1 |
| 678b2dcd-01df-346d-ba81-358a9d79d726 | -22.8326 | -50.5973 | 2025-09-22 00:50:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 90.4 |
| e11bb0a8-b471-3d4a-9516-8cdbd580fdc8 | -4.3198 | -48.0692 | 2025-09-22 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| bf5b5bb7-c097-39b6-86fa-e5390e19b109 | -20.2537 | -55.4959 | 2025-09-22 00:50:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 168.2 |
| f77269b8-3252-3cf6-8e64-9645568ca02e | -15.9969 | -59.4651 | 2025-09-22 00:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 73.9 |
| d891fa58-0aba-31df-8ba3-d74ba48e4270 | -23.0038 | -48.3505 | 2025-09-22 00:50:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 91.3 |
| 5290196f-6413-3339-a5d5-308a8bc98143 | -20.2533 | -55.5172 | 2025-09-22 00:50:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4a2843ba-8e84-366f-9a38-3ba412a040d1 | -21.8351 | -53.9546 | 2025-09-22 00:50:00 | GOES-19 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 22c830e4-adef-33db-9a19-134cae07d976 | -4.3196 | -48.1125 | 2025-09-22 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 5033dbfd-e007-3e43-8568-48b593d5e04a | -11.6249 | -52.8416 | 2025-09-22 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 080be307-811a-301a-97bd-eec614f151e8 | -22.9828 | -48.3559 | 2025-09-22 01:00:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.6 |
| 8e181b89-f76c-313f-a248-d8fcf01ee9a3 | -20.2533 | -55.5172 | 2025-09-22 01:00:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 3f7af146-6fac-3e59-a176-8a13f0e4055e | -10.3762 | -46.0562 | 2025-09-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 220.6 |
| 06b4c07f-153b-38da-a1bb-a83a1189d1bd | -11.215 | -49.6224 | 2025-09-22 01:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| af561ce0-4cde-39eb-b8f9-75345b076941 | -10.3759 | -46.0788 | 2025-09-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 317.4 |
| 0c3817ea-ccfc-3d70-a062-36bae2cfb2c7 | -22.2857 | -54.9191 | 2025-09-22 01:00:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 66.9 |
| d59c4150-2d8e-3e27-88f1-30d6db971063 | -10.3572 | -46.0585 | 2025-09-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 559.7 |
| a41282ee-d6e3-3770-b806-b2b257ea6f0b | -11.2343 | -49.5986 | 2025-09-22 01:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| c799aee5-f420-353c-a197-2dac12b9cbcf | -19.9133 | -42.3563 | 2025-09-22 01:00:00 | GOES-19 | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.9 |
| 5f9fb73d-f16d-37cb-ae4e-b93c8e752112 | -11.6436 | -52.8605 | 2025-09-22 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| ea456cec-a69b-347f-ab22-348122174851 | -4.3197 | -48.0908 | 2025-09-22 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 102.7 |
| 9da86eb5-4db9-3b1f-aff8-64c70a61d0d1 | -11.6439 | -52.8397 | 2025-09-22 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 88.3 |
| 40e84550-d075-345e-b77d-d143fac6ed25 | -7.4291 | -46.39 | 2025-09-22 01:00:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 83.7 |
| c15e15f3-75f1-337d-b500-9c338141ffbe | -22.8326 | -50.5973 | 2025-09-22 01:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.3 |
| 05f2e6a6-f232-32db-a737-c6f005b6d0a0 | -11.8626 | -64.9332 | 2025-09-22 01:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.0 |
| e8a19d8f-66e1-34ff-94af-8439c599bf2b | -20.2537 | -55.4959 | 2025-09-22 01:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 29b4a058-5e0d-381b-b669-be2d3da47e90 | -22.8117 | -50.6021 | 2025-09-22 01:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 101.7 |
| a8407889-d749-3c5b-8de6-b17a0566a7d3 | -22.811 | -50.6251 | 2025-09-22 01:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 92.7 |
| 707e35db-f2d6-3ee2-bde8-dd0730cdff07 | -11.3217 | -54.3564 | 2025-09-22 01:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 72327715-989b-3a6e-bbe4-c5bd61217843 | -15.9969 | -59.4651 | 2025-09-22 01:00:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 59f705f4-12aa-3217-8969-4a8b8ee7122d | -11.6247 | -52.8624 | 2025-09-22 01:00:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 1e991b78-d73f-316e-8ada-60d3c6507d93 | -11.2153 | -49.6008 | 2025-09-22 01:00:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c9415dea-39a7-3b0c-9cef-ab0ec2b3b3d7 | -4.3012 | -48.0917 | 2025-09-22 01:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 58fe187f-a0c9-3fca-87ae-bae138202dc4 | -22.9255 | -48.1819 | 2025-09-22 01:00:00 | GOES-19 | ANHEMBI | SÃO PAULO | Brasil | 3502309 | 35 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 5fdc1f76-f008-3324-9bc0-0a6cc4f30748 | -22.9285 | -47.4219 | 2025-09-22 01:00:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| 77750244-c3fa-326a-b896-67d104084304 | -10.3378 | -46.0835 | 2025-09-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 259.0 |
| d383c4c9-2197-369d-8cc6-62b07664b9d1 | -22.8529 | -50.6155 | 2025-09-22 01:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 151.6 |
| 42c769bf-1586-3ee0-af73-2a5ceb5c286c | -20.274 | -55.4927 | 2025-09-22 01:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 139.1 |
| d8067846-1f5c-3d65-8e50-006bd97da62b | -10.3568 | -46.0812 | 2025-09-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 668.9 |
| 4044e8cd-e703-33d8-ae16-736d3a8471a1 | -20.2735 | -55.5141 | 2025-09-22 01:00:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 81.7 |
| 2def6321-05ea-3b98-88cb-324fa15d304d | -22.832 | -50.6203 | 2025-09-22 01:00:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 143.6 |
| 60858346-5ed6-39dc-9b1c-78a0031c8cd7 | -10.3382 | -46.0609 | 2025-09-22 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 246.9 |
| 160a2899-c827-3034-9a53-802e10ea7f75 | -11.8814 | -64.9323 | 2025-09-22 01:00:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 29.9 |
| 54b8ee2a-d081-32cf-bca3-246803048085 | -19.6278 | -57.7296 | 2025-09-22 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 82.4 |
| 9260db9f-b9fb-3a14-87a7-6a1a6bd331da | -23.0038 | -48.3505 | 2025-09-22 01:10:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 196.7 |
| e50026a6-2cf4-30b3-ae10-e50bacce0344 | -20.2537 | -55.4959 | 2025-09-22 01:10:00 | GOES-19 | DOIS IRMÃOS DO BURITI | MATO GROSSO DO SUL | Brasil | 5003488 | 50 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 5ef08569-198a-3d96-96f7-cf898e525885 | -22.811 | -50.6251 | 2025-09-22 01:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| 8c688f0c-8cca-3a84-a459-c6272af26db9 | -22.8117 | -50.6021 | 2025-09-22 01:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 85.8 |
| 17fd6bf0-7888-38ef-9e4f-2a846e11966b | -22.9285 | -47.4219 | 2025-09-22 01:10:00 | GOES-19 | CAPIVARI | SÃO PAULO | Brasil | 3510401 | 35 | 33 | nan | nan | nan | Mata Atlântica | 73.1 |
| a156d42c-b275-338c-9753-aab744f97729 | -22.8326 | -50.5973 | 2025-09-22 01:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 9fe8c129-a615-3742-b1a2-ca03de3bb56a | -11.6249 | -52.8416 | 2025-09-22 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 953f4df6-5aa9-3b88-8b3d-2bad866a3568 | -11.6436 | -52.8605 | 2025-09-22 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 046cb883-3361-332f-9bea-e52b435cfd6a | -23.0046 | -48.3267 | 2025-09-22 01:10:00 | GOES-19 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 88.3 |
| 4d79b1b0-a590-3455-b8f3-d5774a308cff | -11.6247 | -52.8624 | 2025-09-22 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 447d7679-7b80-31fd-9151-26a3276cffee | -22.9828 | -48.3559 | 2025-09-22 01:10:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Mata Atlântica | 228.9 |
| 2dbe9ee8-d340-3025-bd42-02190bb758c1 | -21.8351 | -53.9546 | 2025-09-22 01:10:00 | GOES-19 | RIO BRILHANTE | MATO GROSSO DO SUL | Brasil | 5007208 | 50 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 545199d8-848d-3f84-b124-cd277b1fdc77 | -15.9969 | -59.4651 | 2025-09-22 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| d7776511-714a-3b6e-ba50-f0a904c73f9b | -10.3762 | -46.0562 | 2025-09-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 332.7 |
| b963e952-197f-3e72-8b35-3cf362086a54 | -22.982 | -48.3796 | 2025-09-22 01:10:00 | GOES-19 | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 101.4 |
| fb77659b-0f5c-3b1d-9f7e-32cabda72c29 | -11.6439 | -52.8397 | 2025-09-22 01:10:00 | GOES-19 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d0d094e2-47c6-3a9c-9df3-58fb1dd30fca | -15.9591 | -59.3887 | 2025-09-22 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 8270950c-8f02-3f3b-8ef4-b432a10550ce | -10.3382 | -46.0609 | 2025-09-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 181.7 |
| bd23b2de-ebe6-3322-9938-84ba5ca930f5 | -20.2533 | -55.5172 | 2025-09-22 01:10:00 | GOES-19 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 89.6 |
| 414eb5f7-156f-3ac3-9755-e558fbb5d19a | -10.3759 | -46.0788 | 2025-09-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 313.0 |
| 819f1a0f-c2d6-3fae-a502-e020bbb2b09e | -18.399 | -42.8644 | 2025-09-22 01:10:00 | GOES-19 | PAULISTAS | MINAS GERAIS | Brasil | 3148400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 72.0 |
| fe9e7858-dc28-3956-b7e5-146c6a5c82f3 | -10.3378 | -46.0835 | 2025-09-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 116.5 |
| 449d67c1-6648-3487-91ab-3f1f178873ca | -11.8626 | -64.9332 | 2025-09-22 01:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 0c7e7658-a137-30ec-bdb3-1c8eba64dd63 | -4.3197 | -48.0908 | 2025-09-22 01:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 011e1fb7-0834-3d3f-8d1b-43f286b7f439 | -15.9775 | -59.467 | 2025-09-22 01:10:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 40.0 |
| 332d1428-091d-389c-862a-4a2da3163156 | -22.832 | -50.6203 | 2025-09-22 01:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 132.6 |
| f84a6018-5fdc-343f-8c81-9e1a3a6aabed | -22.8529 | -50.6155 | 2025-09-22 01:10:00 | GOES-19 | TARUMÃ | SÃO PAULO | Brasil | 3553955 | 35 | 33 | nan | nan | nan | Mata Atlântica | 133.5 |
| b912a6ed-b443-3c40-99d7-597041ebbbbb | -10.3568 | -46.0812 | 2025-09-22 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 458.9 |
| 1ab91c78-6c05-3c33-b629-072a3e1bf4fb | -11.8814 | -64.9323 | 2025-09-22 01:10:00 | GOES-19 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 33.1 |


[Clique aqui para ver as próximas entradas](README6.md)
