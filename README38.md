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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 142844f1-b4a9-37fb-9bd3-bd5065a0521c | -3.51053 | -49.99078 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1ec5ecb-a942-376e-9e9d-75526f38291e | -3.46981 | -50.35781 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1e1a5af7-5fbc-3ba8-a1ba-3e6c4fc0ae86 | -3.46814 | -50.34644 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dee593f-b416-3362-afa7-c44b0869a8f6 | -3.43991 | -49.55593 | 2024-10-21 04:36:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7d0293c1-b271-3d01-87c3-6218393d61a0 | -3.43129 | -49.9784 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| edac306f-c1cd-310a-95a3-dd819bfd0e50 | -3.39852 | -49.53835 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2dcbda4-58e3-3d31-9109-23c8dc826ad4 | -3.39454 | -49.73469 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e306683-af16-3261-8b4d-77570b522d4c | -3.35934 | -50.30371 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c24a24d3-ac7b-383f-b36e-a96decf4ed03 | -3.35632 | -50.1049 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d670d62-386d-363c-852c-5b428ccd4265 | -3.2967 | -49.5581 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d69d0e5-dfa6-3a45-98b7-497316ce68b1 | -3.2809 | -50.17703 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 30647c39-b5b6-32a0-943c-70e80281f158 | -3.27945 | -49.08764 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75618b52-f6bb-37c8-a1d3-1e27d123c860 | -3.27891 | -49.09108 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| de0a57ec-f796-3d1c-bf99-017f839810c2 | -3.27615 | -49.08712 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb601c75-4eae-3a5b-8620-9a51f7b51a12 | -3.27085 | -50.13145 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc95ae22-383d-345d-ba55-29120f468b28 | -3.27062 | -49.07922 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 62959af2-3c92-3b63-90bb-edad733d0350 | -3.26903 | -50.2304 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e25600e-4ba5-3f47-88b1-fc78b139bc39 | -3.26677 | -49.08214 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 79d9fcaa-83b2-3da9-b52d-95c83114cbf8 | -3.26617 | -49.75013 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa4e4758-c6b3-339d-a0e6-8bac4a1ecdfd | -3.2542 | -50.01934 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e7ea414-d423-3caa-bbc8-81f40ac357b8 | -3.24985 | -49.49017 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b147bfe3-a4ca-38d0-87c0-7f78d0dbb3ce | -3.20678 | -50.36107 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99ee4746-f8c6-323e-bd0b-a4de19ee929b | -3.20621 | -50.36469 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3580d057-b43a-3120-b68c-b42b4f5f75ba | -2.46785 | -49.75189 | 2024-10-21 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5edd7162-aa82-36fb-8cf6-0909728ba689 | -2.45602 | -50.42867 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9747c1d8-d5b6-3018-82c4-0c62897efc17 | -2.42973 | -50.33047 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb142410-aa00-33d7-93ab-fd26d494c257 | -2.42914 | -50.33414 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b93a9db4-fab2-3c70-ac0a-950fa1947cb9 | -2.42652 | -50.28511 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8b9af5f7-e5df-3c71-80de-cfb2b0599ee2 | -2.42312 | -50.28458 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 0f421ce9-8613-37f3-bae1-b4296532e0d5 | -2.41973 | -50.28404 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 43af4700-d33e-3b3c-a564-d8d2cfd28265 | -2.41061 | -50.40644 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 47fa793d-8e5d-3fe1-8871-f16a8a51d0c1 | -2.41003 | -50.41011 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e0c90eeb-19f5-373d-94b9-0606aa48a2d9 | -2.4072 | -50.4059 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd0f6198-bbc7-395c-8826-adebb7ba4d7c | -2.40662 | -50.40958 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5df8cf91-e472-36b0-8692-575050abe57a | -2.36016 | -49.81134 | 2024-10-21 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| deb5c74a-73ec-3e4d-8d88-eab699cdac8d | -2.21964 | -50.30597 | 2024-10-21 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fd3a60a3-8038-3e3f-ac9c-9badde078c19 | -2.49631 | -49.29041 | 2024-10-21 04:36:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5ee3c61d-4707-336a-b206-f1d7649bd6e4 | -2.48765 | -49.10826 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43fa1a17-f013-343a-b071-eed940e7b741 | -2.48434 | -49.10775 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b52115e7-0f51-3670-bfb5-edd5b0713fcb | -2.48325 | -49.11465 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 70913c4c-122d-3486-a822-00c736286e02 | -2.48271 | -49.1181 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3aa559d5-867d-33db-9067-8cdda1c0fff5 | -2.48102 | -49.10723 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5df54b68-34b5-3c6f-af59-9ec60a0b06a7 | -2.48048 | -49.11068 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 205ccd01-75cb-3351-bb5a-1c65b4c96da2 | -2.47994 | -49.11413 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b96a11f8-5089-3d7d-8c0e-252453950cd6 | -2.4794 | -49.11758 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 77d57efc-b5b6-3f70-a8c5-aa281d64fb00 | -2.47826 | -49.10326 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dab28fff-aa1d-384b-8492-927aade63b23 | -2.47771 | -49.10671 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 555917d5-91ed-30da-9cd4-95e29e142569 | -2.47717 | -49.11016 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 19485dba-f0bb-39d1-8d69-ce0aa14d0628 | -2.47663 | -49.11362 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ac4e5b4-33d7-31e2-b6c4-47372fbf5f0f | -2.47609 | -49.11707 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50698941-cff0-36e2-bda4-e587972f2c4d | -2.47495 | -49.10275 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 526c530a-8cc4-37ab-9d42-67f8d1b08f7a | -2.4744 | -49.10619 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47f8b70d-5607-3a36-b484-b8a14f5a882d | -2.47278 | -49.11655 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b6d12a09-79c0-309e-968c-864d2bd1ae14 | -2.47272 | -49.09533 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 01134119-a767-3f9c-8691-cb984d5e018a | -2.47218 | -49.09878 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27c4d034-ca33-377f-872e-0bfbb9258ccb | -2.46941 | -49.09481 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3320d60-c40c-38fe-852e-a8afc5f0e764 | -2.46887 | -49.09826 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 799607b8-fe0b-3101-97e2-4f15f771e305 | -2.41481 | -49.39872 | 2024-10-21 04:36:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea6a68e3-7db2-30b5-8668-5dd2f924e02d | -3.50154 | -50.53719 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e7e87d61-d22a-3223-b0f0-7edb6b08947d | -3.55255 | -50.30386 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 147bbaef-9200-356c-9463-6ee9c194113d | -3.55141 | -50.31104 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ba3a4155-21a2-39ee-b543-9c897f33a58f | -3.54804 | -50.3105 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 20c878a4-e67e-30c9-a284-199fbb86ed25 | -3.54747 | -50.31409 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da8750bf-b030-36d1-bd4d-3674197c5fec | -3.54523 | -50.30639 | 2024-10-21 04:36:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 608007a0-4e9c-38e8-b239-f4a94856463b | -2.7101 | -49.03339 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d8c946bb-fdb1-314e-a914-cfdc6977dedd | -2.70679 | -49.03287 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b90e124c-778b-3f5d-9978-d51b85daf887 | -2.70348 | -49.03236 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f5cfa900-4a7d-361e-b2f3-1b43d933b5c6 | -2.70018 | -49.03184 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcedb97d-49e5-3193-86d8-2521840a6418 | -2.69253 | -49.05888 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db5a9260-427d-3127-979a-2364378a667a | -2.68977 | -49.05492 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 67c7840f-6b5f-3881-a6bf-07736614e7e9 | -2.97217 | -49.09597 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b6ed5c51-af1c-32c2-a7e6-11e6c4f49b4d | -2.97162 | -49.09941 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82f73542-2734-39fd-93e0-a9cae81071b2 | -2.96634 | -49.47791 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fcce307-10cf-3706-b654-e71d315bf48b | -2.94655 | -49.5605 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7462310d-9090-3a76-ab03-4222adbe9957 | -2.946 | -49.56399 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49cab6c3-3e99-31c2-ab86-04b2c446592b | -2.94322 | -49.55998 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 823651a9-7bf5-3cd1-87ea-c0573dc1aa47 | -2.94267 | -49.56347 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6617f112-b445-339e-94aa-bd078807a9f4 | -2.93348 | -49.34117 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb6fe8d8-a957-3f5a-bf82-53823d75c049 | -2.93293 | -49.34464 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5f71a91-81f0-34bd-932f-2344f19f7d57 | -2.88662 | -49.48684 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8aae49fd-11b4-3443-801c-7382c56560b4 | -2.87443 | -49.45641 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 519b58f6-d0a1-351e-8d38-c6cff3aa9464 | -2.87387 | -49.45988 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f525bf24-0206-3067-a2c3-348f433ded49 | -2.84706 | -50.46281 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9381f0b-c55a-3186-938c-510d370d4955 | -2.84515 | -49.34157 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 214effed-8bc5-3b62-af6b-dcfb06b64265 | -2.84493 | -49.5375 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da6484d8-cf68-36c1-bd97-bd1b01bab4e2 | -2.84483 | -50.45493 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| aa40c123-f8cc-3104-8fcc-4f417ab20289 | -2.84424 | -50.4586 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfd0dbb5-141e-3e24-8719-aa3ab88076e4 | -2.84366 | -50.46227 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e03228a-58da-3956-8f2a-b74b776075ae | -2.84215 | -49.53349 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 441b7fb5-e92c-3f03-ba5c-9c4e8a7f4625 | -2.84183 | -49.34105 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a0b512f-8c84-37c1-a8d0-ecf67be29b26 | -2.84084 | -50.45806 | 2024-10-21 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5feb8240-ae62-3e08-b53d-b6a2526bd6cc | -2.81802 | -49.77403 | 2024-10-21 04:36:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2eabf8e2-16e0-32ec-abb9-ce982e269e8e | -2.79185 | -49.24771 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aec1ca80-2102-38ee-af4f-f021f30e3c28 | -2.7913 | -49.25117 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef0d58f-20db-339f-b396-4e1a2ea7a58e | -2.78908 | -49.24374 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbb7a64b-cd7d-32ce-80bb-8ca449e7403c | -2.78701 | -49.30016 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2060466d-d2b7-3bed-b915-6363c3181262 | -2.78592 | -49.30709 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 17bad53c-e301-3e70-8aa1-5900c3b15a5e | -2.78424 | -49.29618 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15c4a993-5df9-3ffe-9bc5-b6407e6549b6 | -2.78369 | -49.29964 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4b198714-ab03-344b-8725-962a19f8834a | -2.78315 | -49.3031 | 2024-10-21 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README39.md)
