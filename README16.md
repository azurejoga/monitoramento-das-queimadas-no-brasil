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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3527e87f-2c53-3cf6-81c7-95249e7ae32c | -2.36007 | -49.11846 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 11781220-d10d-3620-98af-4eb781c59abd | -2.35574 | -49.10997 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| cb0f9cc1-8626-3ab7-aea1-08c2ce5ad4bc | -7.55484 | -35.23061 | 2024-11-16 04:01:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |
| daf181df-3f9b-3b47-b778-99a2c5336e36 | -2.35623 | -49.11801 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| d51ff204-58fe-3dfd-abe4-aed02a44045a | -5.25371 | -43.19149 | 2024-11-16 04:01:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 063c1afb-f8ee-3c3b-9ec9-932a497efa5c | -3.91864 | -45.85592 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 74dfc74f-dc86-35e5-a9b3-d78b4133fc84 | -3.19982 | -45.55468 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 280d8a8f-6126-3cfa-ae13-88f878e32718 | -2.35963 | -47.14674 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 152246cc-c3a6-38ca-bbca-74c8f8ec2c42 | -4.36776 | -45.62745 | 2024-11-16 04:01:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 56f19a1f-4537-3ca6-be40-62a06a946629 | -3.74292 | -45.65812 | 2024-11-16 04:01:00 | NOAA-21 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 82.3 |
| 427f1ee6-a541-38c0-91c6-fcc15dbdb182 | -3.0713 | -48.01544 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1576e4e5-7b4b-3d13-bd40-93358516fc1d | -2.1023 | -46.59217 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0a50bee-b9f4-3812-b923-fc88e3b72038 | -5.87615 | -42.49514 | 2024-11-16 04:01:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 302966d2-c547-37f2-9cd2-7a79b11bfe53 | -4.53206 | -48.64472 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f209786-e08f-3c47-be98-e283d4e0062a | -3.12373 | -45.7454 | 2024-11-16 04:01:00 | NOAA-21 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daffab4c-9160-34c2-9748-df1793b6c2eb | -1.56025 | -48.71744 | 2024-11-16 04:01:00 | NOAA-21 | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e42ee736-1ef6-3e89-8948-6803587db3ec | -3.56609 | -47.37513 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e26cb92c-29c7-3b14-975e-0c56f75cc770 | -5.70161 | -45.67351 | 2024-11-16 04:01:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1b1a32cb-90d9-3c10-8a1d-00e2ce9a676f | -6.17273 | -41.16547 | 2024-11-16 04:01:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| af55961d-cb19-3743-b77b-8c143aa2b11c | -4.9056 | -44.0353 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 672af15f-4e37-3fc8-8cdf-b15609daf318 | -3.50139 | -42.00528 | 2024-11-16 04:01:00 | NOAA-21 | MURICI DOS PORTELAS | PIAUÍ | Brasil | 2206696 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6c2fb8ca-03e8-37f0-87ea-1ca3e16a45fa | -2.64132 | -45.97155 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ff24d0d4-bd63-317d-9645-60a896cec598 | -5.12223 | -45.15774 | 2024-11-16 04:01:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e559464-0cf1-37a2-9bff-431dc904ce44 | -7.42858 | -35.15396 | 2024-11-16 04:01:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b4a3d7c3-b1da-3cf3-9367-f0dcf9d6b43b | -5.66994 | -35.64689 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 52.7 |
| e3ca606a-2379-3776-9c49-b0eb2458855b | -2.74082 | -48.55944 | 2024-11-16 04:01:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f96f3017-6cac-36f1-9a57-7de0d91a382d | -3.98644 | -43.71518 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8ba97c4e-7787-31d4-98d2-49bc4aba96d8 | -2.20624 | -46.04591 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f84348df-fb35-357e-b1ec-4eb2dcee8ce7 | -4.37366 | -48.08734 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ab3e0ec7-9e80-308b-92b4-b511cb166427 | -2.65721 | -46.17003 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5a5f40a6-21cf-36d8-9d06-7c81e5b5e936 | -6.64325 | -47.34638 | 2024-11-16 04:01:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd6f375b-5a6e-3d65-b794-5bb93eb72367 | -3.88318 | -45.02768 | 2024-11-16 04:01:00 | NOAA-21 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1cecfbe6-8e81-33ac-9818-2346acd0d3a8 | -6.98853 | -38.48077 | 2024-11-16 04:01:00 | NOAA-21 | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2d3fa2f1-2a9a-3017-b8e1-fbd85d9e37d0 | -3.57293 | -50.24067 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25f25c69-d077-3da7-972a-113ce952a13d | -3.93902 | -44.09712 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c16800e-29d9-380f-ac89-367a905a7d8b | -4.13758 | -49.36392 | 2024-11-16 04:01:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5e513cf8-f4ed-39fa-85f6-37514bbd4675 | -3.50041 | -47.20785 | 2024-11-16 04:01:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bcf7644-721a-38b3-acb8-19f78d85960c | -4.28181 | -48.20741 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c07a67-c4e0-32f7-a700-6fa61f1a15b6 | -3.50802 | -46.05269 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 63e589ba-61cd-3536-b852-e7c14e99a59a | -5.30506 | -40.88742 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 608d9f9e-68d8-335a-957e-bcfeb6f51346 | -2.58731 | -47.47942 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ec388619-bf2a-3e67-82da-5211f4dcd177 | -6.49916 | -41.57858 | 2024-11-16 04:01:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0d930e9d-d82f-3956-9a09-5ea9010932c7 | -5.35025 | -45.56852 | 2024-11-16 04:01:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 59ddc4da-86ef-3808-a588-a38e9a369005 | -3.64605 | -43.02097 | 2024-11-16 04:01:00 | NOAA-21 | ANAPURUS | MARANHÃO | Brasil | 2100808 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2a72dc2d-58bd-38e8-8a2d-2e88ea7a6221 | -4.02507 | -49.1919 | 2024-11-16 04:01:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d37739bb-28e2-3355-bd0d-311dfd7eb903 | -6.59919 | -39.5478 | 2024-11-16 04:01:00 | NOAA-21 | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d81a32d3-3d71-3a05-b98d-8c45a5b7f0da | -4.90975 | -43.23184 | 2024-11-16 04:01:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 262aabe7-d004-3e82-a70a-c22b86121260 | -3.56344 | -50.23665 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b952008-f447-30fa-be18-0b5db0cb01cb | -2.82264 | -46.6602 | 2024-11-16 04:01:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f3a3ac05-024b-39cd-abc6-b545ab89aea5 | -3.98263 | -43.71459 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a23f444-757a-35f2-bae9-46eea1c6f572 | -3.19549 | -45.55397 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 04e6804f-5893-333e-a786-6a7d91b66189 | -4.61439 | -44.39757 | 2024-11-16 04:01:00 | NOAA-21 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae046f18-1ffd-3950-9e82-de6eb0fc9372 | -5.55481 | -45.24511 | 2024-11-16 04:01:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 318ba2ec-33f5-382e-ba47-cdd59997d106 | -4.30308 | -45.99084 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df645f37-ab04-3ff1-9eb7-d8d722fbfe10 | -6.82017 | -46.77761 | 2024-11-16 04:01:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 622378fa-547f-3707-9b8c-59726b020c8e | -7.55943 | -35.22763 | 2024-11-16 04:01:00 | NOAA-21 | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 67dec69c-89e2-3cf2-bd2e-739a647756ab | -6.30714 | -39.4807 | 2024-11-16 04:01:00 | NOAA-21 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e1cdf251-9253-3cf2-a3d6-92e102e160b1 | -7.62399 | -35.09451 | 2024-11-16 04:01:00 | NOAA-21 | CONDADO | PERNAMBUCO | Brasil | 2604601 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 5677a711-c38b-32d9-a889-0e8ccd3ca330 | -3.76691 | -43.24688 | 2024-11-16 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba6841c1-ca01-3377-9d2f-7f44a27bb310 | -2.62681 | -46.18412 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4e1ca741-91a1-3354-8cd0-51a27c781458 | -2.62961 | -47.91668 | 2024-11-16 04:01:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e99f6699-40ff-3aaf-b1a0-88cd3f79d424 | -4.01645 | -44.58652 | 2024-11-16 04:01:00 | NOAA-21 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c219679e-7041-3cc0-918e-f234fe263b48 | -6.02131 | -48.03055 | 2024-11-16 04:01:00 | NOAA-21 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 17.6 |
| f9250bde-181e-34a0-864b-584ad4955130 | -2.14205 | -46.55718 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 32cc1612-ebf8-377a-85c5-c40d9cf73104 | -3.06949 | -45.34629 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 62feb9e6-4982-3dca-a475-594c8b3a765f | -3.78802 | -43.90907 | 2024-11-16 04:01:00 | NOAA-21 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc867267-9492-3678-a21c-b18820efad7a | -3.75215 | -44.38287 | 2024-11-16 04:01:00 | NOAA-21 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 711d92ec-3a3c-3bbe-8abe-889a45ae5f3c | -4.0187 | -38.24897 | 2024-11-16 04:01:00 | NOAA-21 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 7.7 |
| a0822dd1-f9fd-308f-abb7-c23b384c96c7 | -0.78373 | -49.48141 | 2024-11-16 04:01:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8c6a63a-fa6e-393f-8d82-ac5fbc25a324 | -3.56274 | -50.24085 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7fc1a04-4b42-37c2-bf65-f6fbd92fb318 | -2.2408 | -47.21135 | 2024-11-16 04:01:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ed9295a-da30-3706-9475-2e724cfa6719 | -5.43563 | -42.88678 | 2024-11-16 04:01:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f157a45d-1250-3f27-8626-2c7d3e588729 | -2.93471 | -45.60406 | 2024-11-16 04:01:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab6a319e-d2af-3688-84be-6419b17963f1 | -4.91653 | -44.78496 | 2024-11-16 04:01:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b4f6090-a633-39c1-b220-32324051ec29 | -3.7662 | -43.2513 | 2024-11-16 04:01:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8eaa9fa6-930d-3729-b646-26ceddb73cae | -0.96895 | -46.93687 | 2024-11-16 04:01:00 | NOAA-21 | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9aff0346-5515-38c0-af56-32da110d5b0a | -3.94791 | -46.7083 | 2024-11-16 04:01:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfdb616a-fe78-395f-9e19-f4d1d122b7e2 | -4.01847 | -43.9998 | 2024-11-16 04:01:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 868d31b0-be74-3f63-876e-76feb6295d83 | -4.40555 | -43.81027 | 2024-11-16 04:01:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8709596-4578-3ee7-a82c-5e0de3cf31c8 | -5.48455 | -43.76436 | 2024-11-16 04:01:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 838621c5-c11a-3538-8266-3119887d6985 | -4.28691 | -48.20827 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58834a30-8536-3192-9078-569b8651698b | -4.13767 | -44.73955 | 2024-11-16 04:01:00 | NOAA-21 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2fedc82-7fc2-35d3-b233-9fd0bd44dedf | -5.22609 | -40.58841 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cf8a8501-692f-3a5d-9f53-b3cb5c707403 | -5.66925 | -35.65169 | 2024-11-16 04:01:00 | NOAA-21 | POÇO BRANCO | RIO GRANDE DO NORTE | Brasil | 2410108 | 24 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 963544ea-8005-3b11-b5b8-d82700b94269 | -5.33755 | -40.89593 | 2024-11-16 04:01:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 806e95e1-1da1-305b-8aa1-89ddfb3f08e1 | -3.9819 | -43.71922 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4745171f-7e4e-3143-a754-11fb3dd67e33 | 0.79052 | -50.7416 | 2024-11-16 04:01:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| bb182251-07f4-3879-99c9-e64bd5637458 | -3.98571 | -43.7198 | 2024-11-16 04:01:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dceee30c-a12e-3b43-9939-d423265ba017 | -2.67245 | -46.19152 | 2024-11-16 04:01:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9c72405-5631-3514-a49e-75e4aefb28a5 | -4.37824 | -48.56671 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c8ad2182-a42b-3974-83e3-73d2e6f42c38 | -4.29992 | -48.09953 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 24f34a5a-d67e-3396-8fb3-4dd0207ecff2 | -4.37736 | -48.5688 | 2024-11-16 04:01:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f60c7521-acfd-3f3d-afb0-846a6cde3d90 | -2.35384 | -49.12127 | 2024-11-16 04:01:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 55c4c3f0-63f2-3189-8e0d-ebd095b23b9d | -3.9755 | -45.80891 | 2024-11-16 04:01:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3aaca713-5cfc-374d-9d5e-bbe37e8a6b2c | -5.30003 | -43.07278 | 2024-11-16 04:01:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 05007950-ec69-3bf3-8dcb-c72cc27bf771 | -6.86932 | -39.05377 | 2024-11-16 04:01:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7be4e6e6-d8cd-3da4-8c30-0d77a49d538b | -2.02783 | -46.37182 | 2024-11-16 04:01:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c6f5c55-ff27-35e1-b137-da1caa26dd00 | -7.04797 | -41.05274 | 2024-11-16 04:01:00 | NOAA-21 | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8ad698ec-3056-3eac-8ac3-5af943508708 | -6.99341 | -39.65929 | 2024-11-16 04:01:00 | NOAA-21 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 66df0c27-c09c-371a-9acb-5be20eff74f6 | -3.567 | -50.23981 | 2024-11-16 04:01:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README17.md)
