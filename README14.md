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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0bb3642c-ccff-36a3-a33e-2bc8a9da83cd | -3.24725 | -50.67619 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3f6c5091-340f-3f95-b549-6b773e0459a2 | -3.1186 | -53.106 | 2024-11-24 00:49:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| e1fa56c4-10a2-3a16-9360-ae15afa878b2 | -4.11116 | -48.5202 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 85f2a6cd-ee9f-3918-9532-48abeb6e5890 | -2.54122 | -46.3754 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 11d30313-368b-3f2f-a763-1aa79f701273 | -1.26056 | -51.75932 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 095e3762-34ac-348f-8a48-847a87ca524c | -2.3245 | -46.33973 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a7219673-703a-34df-b376-ecf2b8d24bbb | -1.24085 | -51.74287 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c9075f9f-c08b-3fdb-9d32-b758bcb8511a | -3.95131 | -46.90827 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c3b2b834-9a8b-394f-ba83-b5024231786e | -0.88284 | -52.77366 | 2024-11-24 00:49:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 155.3 |
| 74c28bb0-3e58-3095-9314-3f07ccb41777 | -3.29719 | -50.36854 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 7e3644b4-1ab1-3d2d-8a8e-af006b39bf1d | -4.02874 | -46.67338 | 2024-11-24 00:49:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.8 |
| e92ea870-4c81-3bbc-97bd-e8574a9d06a9 | -2.63048 | -46.2244 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| fcd1737c-934a-318f-86d2-94a91edcf01b | -2.91214 | -54.28736 | 2024-11-24 00:49:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 7a88f901-edbd-3449-8f58-4c4d4892300f | -1.615 | -55.14044 | 2024-11-24 00:49:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 29.6 |
| ab55ad51-e156-324b-a18c-d691eb1cc632 | -2.70456 | -46.29281 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 81b98330-9c85-3eab-a6cd-724da4bd93d5 | -2.22032 | -48.4348 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 14ccce2d-f151-31e2-8c24-2eb8f82bb27c | -1.69877 | -48.46286 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b81cc881-8e75-3539-81af-a5078e412b74 | -2.58608 | -45.52777 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c5df62c7-5acf-3658-8bf8-ba20f295e909 | -3.35732 | -50.13574 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f684bd4c-25c9-3a25-a5f2-5c02cd470900 | -0.28153 | -51.61491 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| d8dfd100-78a5-3574-95c2-9a0bc29d695b | -4.59229 | -45.50018 | 2024-11-24 00:49:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 89c9b1b0-e922-300f-90e3-455959677f58 | -3.47411 | -51.99935 | 2024-11-24 00:49:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 9e857e3d-7b4b-3297-8093-e559579548de | -2.17932 | -48.93414 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f61dd67b-7ca7-3b3a-8828-94482ff31fe1 | -2.72368 | -45.71318 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8655c822-30d3-34cc-be95-c47d57ffe716 | -4.42741 | -47.68136 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 25.0 |
| e0a14109-a998-3e5e-9528-16dba5f7f24f | -1.28851 | -54.55361 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| ed5306de-818a-3913-a5ab-44aef773011b | -2.44088 | -49.09587 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 004ee2a9-e165-3707-93fc-ad03ca50930f | -4.09049 | -47.03876 | 2024-11-24 00:49:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 50ae4449-ff79-3f84-8e7c-62d602de09e1 | -2.2892 | -49.06305 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2458ebfb-5361-380c-99d2-2d9e751febcc | -1.46257 | -46.04778 | 2024-11-24 00:49:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 620ca9f3-0e8c-349c-8009-d675df86cf15 | -3.02891 | -45.13398 | 2024-11-24 00:49:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 20.7 |
| c4cceac3-c073-33b5-baae-b447bdb6b053 | -4.22201 | -48.65855 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 939c258c-a91d-3eb9-b1b8-4aaf1438e26c | -3.17314 | -46.54714 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6470a5ca-8f1e-3ec2-973b-867fddba04df | -2.59462 | -45.58732 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 271df4db-383a-31b6-a914-84874cfd813e | -2.4557 | -46.55294 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3300b316-b845-3867-bea4-eab43595291b | -0.92067 | -51.65446 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 851d4797-48bf-3317-878d-244a70a81300 | -2.15683 | -46.65703 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| f59a8a8c-3a09-3546-8f82-b6273847c0c9 | -3.00388 | -52.51713 | 2024-11-24 00:49:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 21e05013-b80b-39f0-bc31-7cbe982a455b | -2.57517 | -47.01395 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f7b4b635-698b-3422-9ad9-83f14f89475f | -2.21907 | -48.42587 | 2024-11-24 00:49:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6ba45d8a-ba9a-306a-b654-9c7baa767656 | -4.48688 | -48.10961 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 18421963-d83d-3f27-a1f6-77eb132d3703 | -2.69418 | -46.28483 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 927257e4-3674-3eda-92aa-738635babc63 | -3.26688 | -50.4397 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 86b9defc-032f-36cc-93d6-d440ea9afcab | -3.10344 | -45.79222 | 2024-11-24 00:49:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 06c7747b-00b8-3376-9d6b-c3fba8b9eeb6 | -3.98065 | -47.91094 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 253ed4d7-1e8d-3dad-8863-526c2e202174 | -1.6095 | -46.89149 | 2024-11-24 00:49:00 | TERRA_M-M | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 51880f46-b4fe-396d-a3d3-92d578f64eac | -1.86411 | -47.92551 | 2024-11-24 00:49:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 338f5ec1-703c-3093-8890-43814dd2ddd1 | -3.67066 | -45.76182 | 2024-11-24 00:49:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e8d3c718-6b3a-3cda-ad80-7bdb40ad4b20 | -1.83445 | -46.65559 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 08e27b32-a8df-3211-9f49-13aefeca3f7b | -4.31702 | -48.08158 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4ecf6738-e471-3a10-8665-65e27c47867d | -1.09611 | -47.50766 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bca3c3d8-b4b6-3a85-8d35-1c99fa7307e9 | -4.23868 | -48.71298 | 2024-11-24 00:49:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 55c7a6ad-2481-3dbd-8d0f-1bb64c5b8830 | -0.25428 | -51.64297 | 2024-11-24 00:49:00 | TERRA_M-M | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c3eb67be-438c-3430-8610-329fc4a804b2 | -3.27788 | -48.75409 | 2024-11-24 00:49:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bc0079c0-e90c-3aaa-b008-494b12cf2619 | -2.40588 | -49.10661 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c75f4466-3142-32e2-a6a8-7ee8d36d174e | -2.14586 | -50.9133 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| d873ba29-27a3-3e73-88d6-c44d6c1bc99a | -3.62541 | -45.06762 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| ba39ca7e-cf72-3e58-8792-1082cc13638a | -1.74879 | -46.70201 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| eb28cbe9-9e60-3992-bc67-9955bd6856a6 | -5.41852 | -47.39323 | 2024-11-24 00:49:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9e8f6eed-68fc-32e6-971f-ac20efab6a46 | -2.44884 | -49.21492 | 2024-11-24 00:49:00 | TERRA_M-M | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 16e68b3d-9c33-37ed-8e7b-569271b8eab5 | -4.03057 | -47.26965 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e43ce181-213a-3cea-8214-09c9dc85e5de | -4.36969 | -49.7519 | 2024-11-24 00:49:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3232c2af-de49-3683-a1be-89105d61ebfc | -2.3463 | -49.0771 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d6a22b27-d109-3cfd-9f9b-4f8ca3abe770 | -3.96019 | -46.90701 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1840230f-2bd4-3aca-babd-da48f73ae8fa | -3.86459 | -44.18108 | 2024-11-24 00:49:00 | TERRA_M-M | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 64d0ccbf-19c9-3f61-997d-a9d3cd9dce03 | -2.66813 | -46.16181 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b60c36d8-8a49-3bb9-8ad2-3e6001fad708 | -1.23795 | -51.74969 | 2024-11-24 00:49:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7e8b6f66-b55c-3dc9-98d6-6bda78c87cd8 | -3.86916 | -48.96704 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7000d91a-d49d-3381-a77d-8bb66f278b6a | -3.16225 | -50.57916 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| eeb73c4a-0b7f-3a60-96f3-32e4f9359715 | -2.10134 | -46.25986 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 6c892f3a-587d-32e0-81e7-a0f3539e9e79 | -1.81319 | -46.63691 | 2024-11-24 00:49:00 | TERRA_M-M | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 227.5 |
| 558cdfe9-0df4-36c1-9bae-581acf1674db | -1.62286 | -55.14486 | 2024-11-24 00:49:00 | TERRA_M-M | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 5349eb3a-2180-3195-89f1-7c4194a4193f | -4.41854 | -47.68262 | 2024-11-24 00:49:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 488ec9e6-52f8-3581-8132-3f13ff1d4aca | -3.61162 | -47.50313 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2416fe9a-15cd-3332-bdfe-1dbbf96ee1b1 | -2.64599 | -46.86095 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a2f0e891-e7b3-3d60-be6b-143b24a894df | -2.9352 | -46.68534 | 2024-11-24 00:49:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a44b9683-ce05-3c15-ba39-d910af605439 | -3.21965 | -49.80255 | 2024-11-24 00:49:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 2244ab8c-4239-3fc8-b597-77aa15ec44a9 | -4.59092 | -45.49038 | 2024-11-24 00:49:00 | TERRA_M-M | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c9165d74-d08e-39c8-9b46-d232ef0da96f | -2.69636 | -46.10369 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ba608390-fcef-38b7-9ed9-eec951235ac8 | -4.11778 | -49.43293 | 2024-11-24 00:49:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 1ed4433c-e739-3d9f-a23f-ac40a6048663 | -4.19531 | -45.3637 | 2024-11-24 00:49:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 8ba62e6f-67b4-3302-9e2a-ff840b4c0422 | -1.76919 | -52.71144 | 2024-11-24 00:49:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a2e3b6b4-52ad-3298-8ba2-37d196233975 | -3.8459 | -44.05402 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| c5e29ff1-1e51-3616-8908-7fcaf48cd23f | -2.17681 | -53.796 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 7b181e70-fdfe-3e21-9e5b-c9ac709d39ba | -2.25628 | -46.83973 | 2024-11-24 00:49:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| cdd136a1-ab63-3cfc-a944-77147ec97a57 | -3.15384 | -46.60526 | 2024-11-24 00:49:00 | TERRA_M-M | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| da8c5a8f-26f9-3905-9297-9e51b52224ec | -3.34636 | -50.50741 | 2024-11-24 00:49:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6af2e504-2fae-3b23-a844-00bfc119e820 | -1.7745 | -53.63542 | 2024-11-24 00:49:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0969d81c-7a50-38fd-83a7-eefc88bc0103 | -1.60967 | -54.41041 | 2024-11-24 00:49:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| e3f533cf-fded-3279-8b2a-02e758c160bc | -3.6461 | -50.22958 | 2024-11-24 00:49:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| eddd2f4c-c49c-3601-a0e3-ae2fcfa229ad | -3.5816 | -41.95984 | 2024-11-24 00:49:00 | TERRA_M-M | JOAQUIM PIRES | PIAUÍ | Brasil | 2205409 | 22 | 33 | nan | nan | nan | Caatinga | 18.1 |
| de3ed7ce-cf9e-3812-95fa-c2dac4b50f96 | -0.03081 | -49.6456 | 2024-11-24 00:49:00 | TERRA_M-M | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| f15c3bcc-57b0-3b9c-b74b-247f10b93bd5 | -1.51177 | -54.17956 | 2024-11-24 00:49:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| c3255d09-9482-3f7a-bb32-a92fb01381b5 | -4.41546 | -44.09925 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 9196ffc5-efef-3376-818c-fe9dba32369f | -4.52617 | -42.90717 | 2024-11-24 00:49:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| eb94cf7c-bd9b-360c-9301-56771f98e923 | -2.0715 | -46.50697 | 2024-11-24 00:49:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| ff4af275-346c-3cf7-a3f8-5c1e73b51d72 | -3.06368 | -49.20212 | 2024-11-24 00:49:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e05e5130-4bd6-380c-8edc-aed83f8efe1a | -3.84577 | -44.0484 | 2024-11-24 00:49:00 | TERRA_M-M | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 6fbcb912-ec8d-31f4-a07d-c6f0147ad0d6 | -3.9612 | -47.70573 | 2024-11-24 00:49:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 055a3df9-ca42-3efd-883d-b739859e2b4f | -2.03246 | -49.00432 | 2024-11-24 00:49:00 | TERRA_M-M | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |


[Clique aqui para ver as próximas entradas](README15.md)
