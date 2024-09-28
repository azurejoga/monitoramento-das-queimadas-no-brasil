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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3bfdd15-6e0d-3537-b139-53c6be8440c9 | -8.8069 | -58.219299 | 2024-09-28 01:09:12 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8c933530-a864-3cc7-9612-c8b6aef6512c | -8.7859 | -58.1688 | 2024-09-28 01:09:12 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ffaeac3-26f3-3a0d-b07d-01dad94da688 | -8.7882 | -58.179298 | 2024-09-28 01:09:12 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a9a4b3b-f887-3f84-acec-c6c3ae43c2c4 | -8.7904 | -58.1898 | 2024-09-28 01:09:12 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25d9b9e2-527b-36ce-916c-33b6268831ae | -5.7757 | -45.5466 | 2024-09-28 01:09:14 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ad543e9-ee17-3bca-bf03-e131005b20f8 | -5.5475 | -44.6665 | 2024-09-28 01:09:14 | METOP-C | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 60164ec6-7f0d-3892-8020-3ca099f105e0 | -5.7661 | -45.549 | 2024-09-28 01:09:14 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d9d2076-c99d-3d0c-9986-d30c38df0d16 | -8.3161 | -56.481201 | 2024-09-28 01:09:14 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee94a6d0-1f84-3d5c-8c58-3e820f1e9dd0 | -7.9816 | -55.068501 | 2024-09-28 01:09:14 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bf48053-8bf8-32ae-a6a5-8ef8b11797e5 | -8.673 | -58.214802 | 2024-09-28 01:09:14 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d4a3f084-9d21-304d-a1d6-6a9a7ad2294c | -8.6753 | -58.2253 | 2024-09-28 01:09:14 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2532c9d-7d9f-393c-a331-94b3d99cb5bd | -5.7079 | -46.442001 | 2024-09-28 01:09:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab97023a-8eb3-3632-8474-974c13c749cc | -5.7117 | -46.4571 | 2024-09-28 01:09:18 | METOP-C | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a31dd258-e8e8-37dc-9c79-b0722c90a49f | -5.5656 | -46.280499 | 2024-09-28 01:09:20 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2727cdab-a396-3d4c-8cb6-d7cca3a13565 | -5.2054 | -44.940899 | 2024-09-28 01:09:21 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3b3420e0-4300-306f-9134-8bc66f6b17d2 | -5.1908 | -44.923599 | 2024-09-28 01:09:21 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 95d67d89-db00-3533-92f0-e698b8bc12d3 | -5.1957 | -44.943298 | 2024-09-28 01:09:21 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5578be8b-30c6-34c0-87b3-2f5d69758200 | -8.1021 | -58.035198 | 2024-09-28 01:09:23 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 37e18d51-f103-3fa1-8cce-660ad50d6c95 | -8.1043 | -58.0453 | 2024-09-28 01:09:23 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d9781064-b7c3-3388-bf84-95a062dff0e9 | -8.0901 | -58.027199 | 2024-09-28 01:09:23 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b9474d47-5df4-3880-9f1a-bed3b1cb2905 | -8.0923 | -58.0373 | 2024-09-28 01:09:23 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce256442-aa9b-3275-abe1-e986dad997e2 | -8.0945 | -58.047401 | 2024-09-28 01:09:23 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3b98e01d-d6f8-31a6-b4d9-3a18cd20fd75 | -6.0055 | -49.3395 | 2024-09-28 01:09:25 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52f69e09-c233-319f-a2f7-cda1d254f0cb | -5.9484 | -49.186501 | 2024-09-28 01:09:25 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76f52f00-c46c-3fa4-87e4-436537e03263 | -5.9508 | -49.196499 | 2024-09-28 01:09:25 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fdf77b0-2d63-3a6d-bbec-c77eb8613160 | -5.9387 | -49.188801 | 2024-09-28 01:09:25 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc470e9-e75e-3da1-a00b-97d526fe95b1 | -5.9411 | -49.198799 | 2024-09-28 01:09:25 | METOP-C | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1d2d7a9-3c26-3e92-b246-72d71fdfbf92 | -5.0939 | -45.822498 | 2024-09-28 01:09:26 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 373ea12e-8910-395a-a6b8-7893eec5f366 | -5.0981 | -45.8396 | 2024-09-28 01:09:26 | METOP-C | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5c1ee100-85ca-33ac-abb6-dee83d208c45 | -5.3251 | -47.704601 | 2024-09-28 01:09:30 | METOP-C | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b2bc56b9-d15f-347f-ba54-f55e7acb5e84 | -5.2234 | -48.180599 | 2024-09-28 01:09:33 | METOP-C | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ff30d090-e445-3081-801a-f1bfe587afc8 | -5.2138 | -48.355202 | 2024-09-28 01:09:34 | METOP-C | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 4fd69f94-d2ec-3e15-983a-7ee8534e29ff | -4.9132 | -48.6059 | 2024-09-28 01:09:40 | METOP-C | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5f548a78-6223-3185-aaaf-78ec9edc50b9 | -7.4549 | -60.3899 | 2024-09-28 01:09:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 54a7c78b-ef32-3300-add3-705208f3c3f7 | -7.4579 | -60.4039 | 2024-09-28 01:09:42 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2d79e5ac-3808-330b-9fd9-f088cfcb00d5 | -4.5829 | -47.999599 | 2024-09-28 01:09:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b4b39051-61fe-324c-8bd1-11d64190d878 | -4.5859 | -48.012001 | 2024-09-28 01:09:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16e69567-7b41-33e5-b310-47391bffbb3a | -4.5889 | -48.024399 | 2024-09-28 01:09:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e76f0c5e-7a97-376f-942a-5d1fc9e29acf | -4.5732 | -48.0019 | 2024-09-28 01:09:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88073dca-e37e-3287-a848-c17c29bab4c1 | -4.5761 | -48.014301 | 2024-09-28 01:09:43 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 10aa4f2b-5f74-3519-b013-122a957e3371 | -3.9198 | -46.439499 | 2024-09-28 01:09:47 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1961932f-4c50-3b07-98d9-fe595d510988 | -3.9237 | -46.4557 | 2024-09-28 01:09:47 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 33409c86-2eb6-32c3-ace6-ab43d620de97 | -3.9101 | -46.441799 | 2024-09-28 01:09:48 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 04d48a7e-fc4f-35a5-90a0-6c4887e795b7 | -3.914 | -46.458 | 2024-09-28 01:09:48 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1900779a-1e8d-34b3-9bbf-259e9a0d52e6 | -3.9179 | -46.474201 | 2024-09-28 01:09:48 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d0910fb7-0840-3905-acd0-7463c9991d76 | -4.4074 | -50.692699 | 2024-09-28 01:09:56 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| def4b42b-3cd2-3b7b-92e3-89904873143a | -4.3177 | -50.749401 | 2024-09-28 01:09:58 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4c38650-490b-3ed2-ae43-6c6d4d03bc4c | -2.6014 | -45.987099 | 2024-09-28 01:10:07 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1d48cc1b-69ad-332a-b30b-d4c846f17f96 | -2.5873 | -45.970901 | 2024-09-28 01:10:07 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 494de058-0497-3e80-b50d-f9e7b38b6396 | -2.5917 | -45.9893 | 2024-09-28 01:10:07 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c8810e9d-484f-3930-9807-2920163d2699 | -2.5961 | -46.007599 | 2024-09-28 01:10:07 | METOP-C | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ef470d7b-5bcb-3a36-a5a8-6e49a1c2abe4 | -2.7161 | -46.723801 | 2024-09-28 01:10:08 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e3faf52-0662-3525-869d-4e0dc47ffd45 | -3.5697 | -50.372898 | 2024-09-28 01:10:08 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c29c066-8288-3f13-9f2e-a4008904cdb1 | -3.5599 | -50.375198 | 2024-09-28 01:10:08 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd420155-3d98-322a-984e-57c6ae16bbb5 | -3.5805 | -50.550999 | 2024-09-28 01:10:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28cd964d-ade4-336f-8920-fb62a07205bc | -3.5707 | -50.553299 | 2024-09-28 01:10:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 526a3cdb-bd72-3052-a8e1-b0414d85200f | -3.5728 | -50.562302 | 2024-09-28 01:10:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de1319e8-b663-3304-ad03-7c510d8261da | -3.5749 | -50.571201 | 2024-09-28 01:10:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 002e60bc-c89c-3cad-829b-c4e37e2d20f5 | -3.5652 | -50.573399 | 2024-09-28 01:10:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1960884-fbd4-3ab5-8932-c2eb5955235a | -3.5673 | -50.582298 | 2024-09-28 01:10:09 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a19bc58b-9e60-3337-9c23-0646060d3d48 | -3.8473 | -52.3591 | 2024-09-28 01:10:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06611266-6405-3d17-b6da-48c22bd1413d | -3.8491 | -52.366501 | 2024-09-28 01:10:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67cc5189-e683-382d-83e4-2434d3279588 | -3.8508 | -52.373901 | 2024-09-28 01:10:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc41999e-a6bd-336a-9998-bd2d99ce2983 | -3.8375 | -52.361401 | 2024-09-28 01:10:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85999994-59e5-3b5a-a334-9eefe63a85b7 | -3.8393 | -52.368801 | 2024-09-28 01:10:11 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e59e2b5-7613-3b7d-b772-b0a3fb24fae1 | -3.3266 | -50.302799 | 2024-09-28 01:10:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a43357e1-86a2-3ecd-9c3a-6171149bc372 | -3.3287 | -50.312 | 2024-09-28 01:10:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fbd00dc0-a266-34e0-b772-3116c2a0e948 | -3.3168 | -50.305 | 2024-09-28 01:10:12 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e4ef545-3c49-3112-9c90-d47dd5630a69 | -2.5385 | -47.226799 | 2024-09-28 01:10:13 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c9409c-8c20-31de-9df2-bf8d260a6ed7 | -3.0593 | -49.559601 | 2024-09-28 01:10:13 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e06b685-610e-3e09-947e-5ec87b1edecc | -3.2975 | -50.6628 | 2024-09-28 01:10:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d30aa02-571c-3307-9efc-108c1944d8c9 | -3.2036 | -50.437698 | 2024-09-28 01:10:14 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06cf6baf-ad20-316a-9fcc-0fa39fbe395a | -3.1917 | -50.430801 | 2024-09-28 01:10:15 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fe214ee3-e276-3018-afc6-ae11ffa7bc57 | -3.1939 | -50.439899 | 2024-09-28 01:10:15 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcbee3ec-5931-37cd-8d41-d7e82ec29141 | -3.196 | -50.4491 | 2024-09-28 01:10:15 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5585461e-e58e-3a52-a691-c941231c92fa | -3.5759 | -52.1227 | 2024-09-28 01:10:15 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7101345-f943-32d0-b2f3-89bf9fd84b10 | -3.5777 | -52.130299 | 2024-09-28 01:10:15 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b28cb67-0981-3fd5-b9d0-3df0fad82802 | -3.1353 | -50.277901 | 2024-09-28 01:10:15 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dce3258-7529-349c-b939-dafde54251a3 | -3.5661 | -52.125 | 2024-09-28 01:10:15 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1d04204a-1637-3966-a4bb-23df7ed99676 | -3.5679 | -52.1325 | 2024-09-28 01:10:15 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723c56a4-139c-35d1-bcd6-f220d553e5e2 | -3.1101 | -50.478298 | 2024-09-28 01:10:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4e3dfce-7a48-3705-9838-24daaa46aec1 | -3.0884 | -50.473701 | 2024-09-28 01:10:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aef7c0b9-575e-3e81-bc53-2eaa0e5cc51e | -3.0905 | -50.4828 | 2024-09-28 01:10:16 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b53ede5-470d-3919-a021-ef0537a864b4 | -3.0765 | -50.466801 | 2024-09-28 01:10:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b7370ab-b99f-3ffd-8116-7a44f67107a2 | -3.0786 | -50.476002 | 2024-09-28 01:10:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48e05d01-3d8e-3566-95ef-cee82b748ff0 | -3.0808 | -50.4851 | 2024-09-28 01:10:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0546300a-ae70-3c18-a463-692e71ffad6c | -3.0668 | -50.469002 | 2024-09-28 01:10:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| efe96974-e1da-3e9b-98d5-a7c3a131a24c | -3.0689 | -50.478199 | 2024-09-28 01:10:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0dfb127b-6499-33f4-a101-96b83e2ed68c | -3.071 | -50.487301 | 2024-09-28 01:10:17 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7a8212c4-4561-3927-89f2-6290f32a37f9 | -2.3588 | -47.5938 | 2024-09-28 01:10:17 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a414c2-031b-3bad-90ac-c5f42bf87bec | -2.3621 | -47.608002 | 2024-09-28 01:10:17 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdef309d-45dc-3ab5-b024-345a13b1b883 | -2.9017 | -50.468201 | 2024-09-28 01:10:19 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2513064b-0c4c-30c5-b46f-49de9d70be60 | -2.8919 | -50.470402 | 2024-09-28 01:10:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 633ae924-9426-3f20-a059-b3423d14cb49 | -2.8941 | -50.479599 | 2024-09-28 01:10:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eca28b43-74fb-3a70-822f-cf137b835b73 | -3.0164 | -51.047501 | 2024-09-28 01:10:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 114e1e27-20b0-3280-9218-668e6bf55898 | -3.0184 | -51.056 | 2024-09-28 01:10:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89d9a4b3-d919-3946-91a2-912d288afbec | -3.0066 | -51.049702 | 2024-09-28 01:10:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b6a4850-7c53-3686-99c5-36f0d340df95 | -3.0086 | -51.058201 | 2024-09-28 01:10:20 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45cdf6f2-5092-3d63-ac69-1affa9576f48 | -2.9591 | -51.642399 | 2024-09-28 01:10:23 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f67a407c-4abc-3123-a53c-ecaeeb656197 | -2.961 | -51.650398 | 2024-09-28 01:10:23 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README23.md)
