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

## Dados Diários - Página 49

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1146117c-1614-32fc-956f-f9b887f7dd7e | -3.24043 | -50.31089 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 85645f1e-e15f-378a-80e0-aa60e40288a2 | -4.43918 | -44.62677 | 2024-11-10 04:14:00 | NOAA-21 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 36.8 |
| acf6bc1d-1793-3b01-80f2-dfb54bfaa7b1 | -3.24927 | -50.31783 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 714da1e8-7b71-3dbe-8683-9066888ebbf8 | -2.32872 | -46.07809 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f1054a4-7748-3e8f-9933-2bd3a0917855 | -3.04302 | -49.54973 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d9a87793-ac04-3f85-8264-ac5129833ae4 | -3.59501 | -50.24482 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9a8c760f-46ae-3269-9e6c-8563b6e0800d | -2.88907 | -45.36489 | 2024-11-10 04:14:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8d798f47-f1e6-3b52-934b-b5a516fabb34 | -3.48211 | -48.23765 | 2024-11-10 04:14:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca148261-2ed4-37ea-9fe9-f58c65282fcd | -2.42412 | -45.55177 | 2024-11-10 04:14:00 | NOAA-21 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 10f44c40-7d90-3aa0-b0e3-757226dfa06d | -3.78695 | -47.73358 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e944265-f49c-388b-b0d9-49619ed23a78 | -1.28053 | -53.71025 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| fdb46cd8-1778-3400-8e27-3ae00d102e9a | -1.51541 | -52.20242 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c2092e59-2f75-3fdd-b6e9-7fb880ffe37a | -2.29499 | -46.5075 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d9ebc627-a9be-3e72-8ab8-4ec7cfb7b088 | -4.90148 | -47.46865 | 2024-11-10 04:14:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8fc116bb-c6c4-3389-a55e-d16e467529ed | -3.57447 | -42.22498 | 2024-11-10 04:14:00 | NOAA-21 | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dc8639f4-526c-31a0-9de4-6180ee3ce8d4 | -3.59793 | -47.34477 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| ebd9a8be-2924-3273-ac4d-d58454c7f923 | -4.39914 | -41.90652 | 2024-11-10 04:14:00 | NOAA-21 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| a6707d38-24e1-309a-9bfe-b3abbc15e3b1 | -3.04011 | -50.26649 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 37317f20-baa1-3587-ad3c-b30c5b3e3559 | -3.09904 | -49.40602 | 2024-11-10 04:14:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 29587f19-e34d-385d-8f93-8951aa31028d | -1.28486 | -53.70842 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 249b0a72-ebf8-3212-9758-386c2c918cb1 | -4.08809 | -48.5124 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10708428-5fa7-34dd-82f9-bd5068f936af | -1.5548 | -47.69982 | 2024-11-10 04:14:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d839bc47-5ea8-3fb4-be10-a469e4a2cef0 | -0.04108 | -50.7757 | 2024-11-10 04:14:00 | NOAA-21 | AFUÁ | PARÁ | Brasil | 1500305 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 446da96d-a4b3-3e2e-8428-f7a8e1666f6f | -3.08838 | -51.22128 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae9562f7-240e-31ec-9e1c-5735abe5c58b | -5.36856 | -44.79053 | 2024-11-10 04:14:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 484d6436-84dd-3e79-8f93-40f0c402e9cf | -4.62422 | -45.65265 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ba49611-830b-3e54-a7c6-6fdba137d2d5 | -3.08064 | -50.57078 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 568ce070-11f9-34de-a03b-39339efb13e1 | -2.23466 | -53.7906 | 2024-11-10 04:14:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5502bff5-71d4-3d79-8453-0f7caeff873b | -2.2988 | -48.49994 | 2024-11-10 04:14:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 78984ebc-3884-359e-971e-ac3fc61e961e | -4.21844 | -45.94312 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b293e122-ecde-3c54-a6d9-a80fdb53485b | -4.50148 | -45.46804 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a7886502-b9af-31c7-a06c-8d1af13467db | -4.20349 | -48.54979 | 2024-11-10 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a055e500-a2f1-3bea-b202-3c8c6ee2c321 | -3.23926 | -50.27995 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78cdb68f-1938-36ba-9e15-a04540d064d3 | -3.59 | -50.27613 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a282be17-bf9d-3cb5-b0e9-7468f51a16cb | -3.12719 | -45.23644 | 2024-11-10 04:14:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53072bf1-2bf2-3394-8fa0-1032c1310644 | -3.13164 | -50.44202 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.7 |
| fe06469a-fa0c-30d1-b7a1-ca61c2bc495c | -4.84234 | -48.6258 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| be84364d-68b9-3456-b008-49dbd968c7aa | -3.6343 | -50.18358 | 2024-11-10 04:14:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cfa0bb9f-284d-3493-a44a-491b4d45ef3c | -3.69812 | -47.63869 | 2024-11-10 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51ef1d91-5a6b-3a46-bcad-ff566a34f5b4 | -3.22673 | -50.30321 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fdcda6cd-dad5-3f23-b2bf-48efa2cab929 | -1.16336 | -51.92089 | 2024-11-10 04:14:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8e24fd57-d028-35cb-aab6-f384edd7b931 | -1.70169 | -48.16676 | 2024-11-10 04:14:00 | NOAA-21 | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f6f7a5c3-cdaf-349f-92f0-a3bb4300a1ff | -3.88944 | -49.98039 | 2024-11-10 04:14:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 27587dde-ecf8-30fa-add0-c5dd7dd11d36 | -4.92439 | -48.52006 | 2024-11-10 04:14:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5d23ad10-b176-36b8-8503-775a98d53778 | -3.18233 | -50.57719 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57942973-db01-3cfc-9e56-861bfe82cbca | -3.8242 | -55.67461 | 2024-11-10 04:14:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7a0c0331-daff-396f-80e1-5b1f96ff7608 | -2.80406 | -52.54142 | 2024-11-10 04:14:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| b7fa1574-58aa-3e6b-b413-e383f7d8c163 | -2.37437 | -46.74258 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30acd95d-5164-3d68-a327-32f45bdb1e7b | -5.56747 | -47.77906 | 2024-11-10 04:14:00 | NOAA-21 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 4409ce00-75d3-3f37-9660-7a7c98c183c4 | -1.99371 | -46.35193 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 546b14e3-4003-399e-b876-8e9498fee952 | -2.98651 | -50.29853 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 895b8484-ca16-3b51-a90b-cd25254bb6da | -1.48582 | -51.74884 | 2024-11-10 04:14:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 29b23e0b-870e-3a85-87c2-efef0ae6d0a2 | -3.90536 | -46.44192 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07e28a42-8de6-38f3-bfd5-5435150df32a | -3.23812 | -46.53273 | 2024-11-10 04:14:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bca4742d-f3c2-3f2c-9900-402b55eb926e | -3.22469 | -50.45519 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78487f78-4f57-3e3e-82bd-b2eda9e7c693 | -2.96491 | -48.03074 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 63975270-e9f9-387d-8a36-7c2fa6358a30 | -4.85236 | -48.64358 | 2024-11-10 04:14:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f013627-675a-3697-8b2b-290acb4efed6 | -5.2356 | -46.71189 | 2024-11-10 04:14:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7abaf55-ade8-394f-8120-26a2a1c2c984 | -4.54364 | -45.54323 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0151de25-43fa-3eb2-8497-518217488484 | -3.18577 | -54.31873 | 2024-11-10 04:14:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 27a17188-18e9-3332-b728-9cb260a55c80 | -3.96081 | -48.17593 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f55ea866-8df3-3da7-acaf-5c8530a2dce5 | -3.96669 | -48.99217 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ba196963-e83e-3b3e-b898-b4e015de26da | -4.0074 | -46.5303 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 06beacbe-ad3b-3d27-8e83-69e472c3b3b4 | -5.52939 | -41.69697 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| eaa40236-07e8-3b28-b245-56787988d6c2 | -4.60967 | -45.98768 | 2024-11-10 04:14:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82e43cf9-c77c-32bd-bb8e-555a3fe4e189 | -3.23297 | -50.32625 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5c428e5-93d8-375e-a446-b76f081a9ca3 | -3.86245 | -52.38129 | 2024-11-10 04:14:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b6fbd858-a7c6-3898-b332-061d752698c9 | -3.51516 | -44.03343 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| 4059bd35-9be4-3b14-9e7b-f59bd86d1a34 | -3.19273 | -48.66444 | 2024-11-10 04:14:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a1b83de8-a965-3c95-be6a-097475802f0a | -3.87094 | -40.90757 | 2024-11-10 04:14:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e1e1540-9679-340e-97ac-574b9e4abd6d | -2.56405 | -50.68084 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a6e4326c-e3a8-34fd-a026-bb3267ccbdcf | -2.25898 | -47.06648 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f4e35846-c005-3fb1-96e8-d863b203b055 | -3.69498 | -45.81487 | 2024-11-10 04:14:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c76b3a6c-51ca-3de6-869e-2070e94eaa6a | -3.96094 | -48.99983 | 2024-11-10 04:14:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 892a0622-6f8f-3805-9dfb-a6f30bc5c184 | -4.23926 | -45.38076 | 2024-11-10 04:14:00 | NOAA-21 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6e93017e-3769-316a-9e07-e2b6a94202d9 | -4.38327 | -47.23735 | 2024-11-10 04:14:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| fd7ee49a-c8c5-3496-ac73-8a5d8d9fd6a2 | -2.42506 | -51.96128 | 2024-11-10 04:14:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 995723f3-45c6-3191-8826-7b5cf7ba084c | -3.23386 | -50.31186 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 80b53786-ae42-3455-a125-197a878a13ed | -2.54617 | -47.32409 | 2024-11-10 04:14:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e66964c-385a-3ac8-b302-f53a30c1cb83 | -4.58784 | -45.6757 | 2024-11-10 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9486093-d7dd-3977-87f2-fd2833e9c45f | -3.03456 | -48.04949 | 2024-11-10 04:14:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7d661da-c05e-3213-8f3c-f4331b16ca31 | -3.44768 | -51.33615 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 685c499c-f7f9-385c-92a3-321bdb08de0a | -1.73526 | -47.82073 | 2024-11-10 04:14:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5666c0f6-8c3f-3b78-8605-b68c1033b092 | -3.82555 | -46.52337 | 2024-11-10 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7b28756-a065-35df-8362-71addff109f3 | -5.53158 | -41.68267 | 2024-11-10 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| cbfc76f5-7e95-3e2d-a75a-1f6ff21229e9 | -2.93393 | -51.4773 | 2024-11-10 04:14:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 4c438c25-70e2-39f7-a142-8773b35beb29 | -2.25976 | -47.06144 | 2024-11-10 04:14:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| e1e40d2b-c7cf-3d37-a141-9b6b3c30f288 | -3.14413 | -50.4403 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 37bf5818-be13-3a4b-b926-2a13049a7578 | -3.04118 | -50.26899 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cca2857-8d71-3d48-99ea-ddb6e5d5c95a | -2.98163 | -50.29783 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b68786c-f344-3a7a-9f1a-1114879c4dfc | -4.31776 | -45.66499 | 2024-11-10 04:14:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2c9380d-1ed4-3313-a497-6fe77f95f1a1 | -3.51573 | -44.02985 | 2024-11-10 04:14:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b8a19631-b1cd-3874-8826-ba5e3f143668 | -2.0498 | -48.99079 | 2024-11-10 04:14:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc0e87cb-b846-32a4-b487-1f9cbc973cab | -2.04944 | -46.53696 | 2024-11-10 04:14:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 599580d6-859b-3025-b60f-66d6ba925b96 | -5.67436 | -47.99036 | 2024-11-10 04:14:00 | NOAA-21 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f4d6196e-294f-323b-8e3c-e10468c63efd | -3.96375 | -48.18399 | 2024-11-10 04:14:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| d84d8417-5a01-3c2a-acc5-d4dd5e7137f9 | -2.56453 | -50.67793 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f9415962-f285-3c6d-bfa6-115559a3bc61 | -0.40859 | -51.93653 | 2024-11-10 04:14:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab12d497-4172-3d08-ab5d-e2defb80f1ed | -2.38063 | -46.77834 | 2024-11-10 04:14:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0839d8e9-c84a-33ed-9f0e-ab796656e86b | -3.23244 | -50.29865 | 2024-11-10 04:14:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README50.md)
