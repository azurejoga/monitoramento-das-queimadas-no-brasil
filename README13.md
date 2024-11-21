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
| 9e15fd8d-5daa-30b7-bbb6-4ebafa149fbf | -2.61159 | -49.24973 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 493bd18e-5656-30db-9894-6211ede89904 | -3.77154 | -50.70075 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e5409610-fff9-349a-8cd6-10777df7bf11 | -4.61148 | -45.74113 | 2024-11-21 04:08:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b628d34-e743-3a14-a6d6-b0ee5c853984 | -2.76039 | -52.11851 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| d04573be-5825-381c-820b-66f312dc6f92 | -4.07143 | -50.9019 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 12e22ece-81fb-3e5b-8a04-558e44207523 | -3.78229 | -46.67035 | 2024-11-21 04:08:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1273b955-a9a8-3c7f-ad43-98a415dcfdae | -2.93501 | -49.43425 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7d38c99a-3caf-3b42-b9be-55c2fd330955 | -2.85163 | -46.68666 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a36c19f3-7884-3a1c-8936-91e0cd72de2c | -5.09411 | -43.24903 | 2024-11-21 04:08:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ace42a50-4339-309c-ab7b-1478bc27fee9 | -3.78419 | -39.09016 | 2024-11-21 04:08:00 | NOAA-21 | PENTECOSTE | CEARÁ | Brasil | 2310704 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 62f3da2a-ed10-3bfe-8780-fc10c0ffc66f | -2.94143 | -54.80107 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44bce287-e944-3d8a-afa3-7936a7060119 | -3.53676 | -51.60667 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ae47ce9-7254-3f89-9e82-316c4ad409b5 | -3.36022 | -49.50605 | 2024-11-21 04:08:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 25aedcf8-5fe3-3165-abe4-89afd81b2fa1 | -3.08907 | -49.47216 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c746b213-9022-34c5-b54e-8db63a3923f9 | -3.53961 | -50.52666 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d4f1df04-d41e-33ec-80c8-479e81d7cf51 | -3.27892 | -50.522 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26624ade-b098-30d4-94e9-31fd2f0ce31c | -3.00642 | -51.00203 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4782cf6b-4eb9-303a-8d90-3300f3aa55a9 | -4.63441 | -49.54735 | 2024-11-21 04:08:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 438b7bce-dbf7-3512-a1b4-279d41187c51 | -3.08472 | -45.97107 | 2024-11-21 04:08:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 43d71b09-d6b7-3071-a16b-24990038ed11 | -3.27676 | -53.84284 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| f4eef45a-8d30-3e67-967f-5e388cfa1194 | -3.48358 | -50.31649 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42ea6f44-4ee0-3cfd-8988-fdd298de81e2 | -3.56993 | -54.68661 | 2024-11-21 04:08:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c060ef49-4a3e-3d04-b138-d55755c7a6e0 | -4.49219 | -47.11016 | 2024-11-21 04:08:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9dd74862-3407-3520-8c88-2a3270160831 | -4.96532 | -49.84322 | 2024-11-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0b964232-c788-36cb-adad-24cd5b327327 | -2.99429 | -52.37722 | 2024-11-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a57c74b2-2962-3594-8824-060ddb08a4be | -3.60471 | -51.55852 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 46e50305-4b53-3047-b5b5-feb6b43044a2 | -3.29505 | -49.18922 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| da68fe9c-c810-3107-910f-5addba49f279 | -4.07081 | -50.90546 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c7cb67bc-e11c-3ca6-82d4-edf59535d452 | -2.53505 | -45.43714 | 2024-11-21 04:08:00 | NOAA-21 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 6cd4b145-b928-3399-8588-bd2ecd3274c0 | -1.72886 | -52.70647 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9731ee00-a999-3362-8490-756b8630af56 | -5.24817 | -45.88461 | 2024-11-21 04:08:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43ac4094-5684-3f6d-831f-c3a8a84b5ddd | -5.48011 | -44.861 | 2024-11-21 04:08:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab9a72b8-b3e2-32bd-895b-44b84dad818d | -3.2896 | -49.1912 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da509e95-43ab-3918-9417-95c1b99e58fc | -3.66213 | -51.57155 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c3c2a115-1d29-3ba3-818f-961b6370ac37 | -1.46581 | -52.67801 | 2024-11-21 04:08:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 12f106c1-58db-363e-a30d-b32990441c19 | -5.94918 | -44.46725 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7a87bafd-7676-3b25-a8fc-d157f7a19ca4 | -1.73395 | -52.38618 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d0e8b51a-982e-3342-90c9-e754531f343c | -4.07154 | -51.03328 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79622d9c-af0d-327d-87d6-8f33b5d41d76 | -3.26833 | -53.83429 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e43bc17b-1039-3b7e-94e2-546439463df9 | -3.30548 | -50.35855 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a0fb4fcd-96ff-38a1-92bf-12e4e500db84 | -2.84835 | -49.15144 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cd0b7f8b-b6a7-335c-b0a1-bfea327594b8 | -2.65613 | -46.14286 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2088114-b94f-3947-bde6-85b4c732b8b7 | -2.69232 | -46.25347 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1076c2e6-5a27-31b1-a6a0-1b6df2f82a59 | -3.38386 | -52.45978 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 3e2d238a-be5e-325e-8d25-881b7a3b9512 | -1.64803 | -52.6174 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0349562c-c3ed-3a33-8dd2-f90f30a7d75d | -3.79972 | -47.79654 | 2024-11-21 04:08:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61b901b2-97b3-320a-b7fb-abf9a573157b | -3.8089 | -52.36644 | 2024-11-21 04:08:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 9ec393fd-5f01-3c46-b32e-f311d6c1a89d | -1.13815 | -51.68317 | 2024-11-21 04:08:00 | NOAA-21 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 209dd295-5eb8-312b-bce9-3f30da4e40c1 | -3.27106 | -53.83594 | 2024-11-21 04:08:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| f7095831-b9b2-347c-af85-cec44d89418b | -3.64613 | -50.21642 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7699e494-9956-3334-a34b-571ee7dba259 | -2.69352 | -46.24611 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aec79ee1-a9c4-3b48-8d2e-d9e0d0f7111e | -3.19281 | -45.03645 | 2024-11-21 04:08:00 | NOAA-21 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7670112c-a62f-3063-aebc-6063de0924d8 | -2.78417 | -51.71792 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bef57d90-d8be-3ea5-b1e7-40a426a36937 | -2.59764 | -46.19347 | 2024-11-21 04:08:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 586bd841-5958-3b8a-8e9c-2cf2d20983de | -3.5483 | -51.43609 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f0ec90e4-7bfa-35d4-a31e-91a5ceeac356 | -4.96482 | -49.84616 | 2024-11-21 04:08:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 161feb48-034d-33c9-acf6-df08f6448824 | -4.88899 | -45.835 | 2024-11-21 04:08:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14202d15-018c-3fd7-87a6-922fa22ccdb6 | -2.6787 | -47.4749 | 2024-11-21 04:08:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19783d6a-9f3a-3398-8169-2f92f829c60b | -5.95274 | -44.24406 | 2024-11-21 04:08:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2d3c7456-6e3a-3a42-a617-e2bac76c4cd2 | -3.97316 | -43.45823 | 2024-11-21 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ec83798d-8d72-30fc-80d2-260fcb118712 | -1.73312 | -52.3912 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 8a2c3c99-eb2b-3377-a56f-65c675acd23f | -3.17093 | -49.15891 | 2024-11-21 04:08:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47bc4e0f-f02b-3e89-bef1-35fe0aaaafab | -3.18662 | -54.32051 | 2024-11-21 04:08:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e98c46c-2494-3d2b-aa2a-9ac2a43fba54 | -5.84379 | -47.49304 | 2024-11-21 04:08:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af53b80d-753d-3fc3-9f32-a2e769541017 | -1.62216 | -52.58843 | 2024-11-21 04:08:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60d99400-cabf-3ff5-8cea-200a72d70427 | -2.25012 | -46.874 | 2024-11-21 04:08:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3997ef1-bbfe-37e0-80c7-c30aee961d12 | -2.94495 | -48.33627 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7d7e0fa-cab4-3e4c-9bd4-3c463f085b37 | -6.12411 | -42.5177 | 2024-11-21 04:08:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| b6252529-8f02-353d-81c1-fee49116dacf | -2.55465 | -47.28896 | 2024-11-21 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35274f65-0ad3-36a9-97e5-5f815b8292b9 | -4.00232 | -43.2504 | 2024-11-21 04:08:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e980b875-b28d-3dd2-9864-38939448ea4f | -6.66663 | -34.97393 | 2024-11-21 04:08:00 | NOAA-21 | BAÍA DA TRAIÇÃO | PARAÍBA | Brasil | 2501401 | 25 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 0f0f7ba2-3550-30b5-abd4-d0058f629c32 | -3.22362 | -50.58541 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25241dd2-2e81-362b-98f0-c0391a209803 | -2.62352 | -51.79905 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98cb72c4-1443-3cdb-a658-6ba98b100c99 | -4.73803 | -46.66698 | 2024-11-21 04:08:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f0bb4aa6-9e90-3511-83e7-5429e9ddaa7d | -2.4001 | -48.60959 | 2024-11-21 04:08:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e7e6179b-f7d1-351e-9c20-20eabb3732dc | -3.0158 | -51.01531 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc9fb095-b2aa-3b65-850d-1306adb8df97 | -2.20858 | -53.72121 | 2024-11-21 04:08:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 39a40d21-ab8b-36c3-b6cb-2dac0de44b7f | -4.66006 | -46.40313 | 2024-11-21 04:08:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 03e7f3ae-2c35-384c-8f3e-6396e507f3cd | -1.60084 | -46.87128 | 2024-11-21 04:08:00 | NOAA-21 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a8942045-7bd8-3060-bddb-c5003fb63aa0 | -4.09664 | -44.85609 | 2024-11-21 04:08:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27f608d3-3879-30c3-bc3f-453dc46680ab | -3.59889 | -51.55762 | 2024-11-21 04:08:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34e71c54-516b-3922-816b-aee5b61f85ce | -2.62264 | -51.93004 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d09dcb97-d003-3e83-930b-238855c94ecc | -3.55438 | -50.2426 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e898ec33-190d-35d8-a710-6b3426cc35ea | -4.06525 | -50.90477 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4f7d845-ae84-3d7a-bb80-8131de5d6cc0 | -2.61068 | -46.80685 | 2024-11-21 04:08:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6c8f2f9d-338d-3200-bedd-46bdd6662634 | -2.96357 | -51.01487 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4e16b1d-c0d0-3284-8bc2-47682d83894d | -2.55908 | -47.28961 | 2024-11-21 04:08:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d3c5f68-3e8e-3c2f-a05c-d4df79bf65f1 | -3.10283 | -50.2002 | 2024-11-21 04:08:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 19f9e19d-7288-3315-b284-b7966b18cc30 | -4.10347 | -50.7424 | 2024-11-21 04:08:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02fa3298-205e-3d30-96e5-06ddd1614043 | -5.5449 | -46.99199 | 2024-11-21 04:08:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8055e0fb-1657-315c-8800-211c4c780ddc | -5.43757 | -42.83596 | 2024-11-21 04:08:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 11dddf13-4e98-39ce-9856-f9c76f9cea35 | -1.01725 | -48.07137 | 2024-11-21 04:08:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e8e4dc2f-15f7-322e-bd5e-b3de6daf5eac | -4.48743 | -45.36272 | 2024-11-21 04:08:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 331229e7-9ea2-3b91-8d63-d207b5d3eb4a | -2.83735 | -51.8209 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| a2423a18-6455-37ad-b701-b14631af916c | -2.88092 | -52.45104 | 2024-11-21 04:08:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f17719c5-9e67-34fb-a85b-3740a4331b3c | -3.33954 | -45.81451 | 2024-11-21 04:08:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cea654ce-49de-35c7-a351-cf876b818240 | -3.6926 | -49.96875 | 2024-11-21 04:08:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42e034fe-88f4-3e43-9ddb-9ce793f0eff0 | -2.94022 | -48.33555 | 2024-11-21 04:08:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d7018b8e-1536-3042-8279-8c268529d52e | -2.84039 | -51.82123 | 2024-11-21 04:08:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 65107b40-d5aa-332b-ab5c-e4002baf54d7 | -1.42852 | -46.01386 | 2024-11-21 04:08:00 | NOAA-21 | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README14.md)
