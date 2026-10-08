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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a6210e9b-03c7-3498-a676-a8fb365bf8a0 | -3.3028 | -54.696301 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17380fca-86bc-3989-b9a5-68038388d03f | -3.5245 | -54.630402 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d89238f-3d3d-3b44-9f9f-efd12678ad79 | 3.7405 | -51.6259 | 2026-10-08 00:48:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3393737e-3b72-3cd1-8620-c53e277d2c1e | -3.8484 | -51.936798 | 2026-10-08 00:48:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 509e437d-eb24-3667-a07b-14d83134da70 | -4.3042 | -54.803101 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6044a0ac-a274-3787-8d45-4b4e2c64292b | -3.5037 | -59.330002 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c926e0be-279b-364b-b7de-9b48c37791d0 | -2.9195 | -54.142101 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3886a91-6f70-3f99-b3c0-515248355860 | -10.4469 | -47.287399 | 2026-10-08 00:48:00 | METOP-C | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 41f466df-6c54-3f28-8f10-8f695b2ca64b | -2.466 | -56.085499 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21e9ed12-e74b-38ad-af0b-0b06442736ee | -6.1583 | -52.666599 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9550edc-1f30-32b0-b514-9133e169fb47 | -3.4298 | -50.432201 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1ab2d8a-440f-39d8-8fd5-f48b7115ccc4 | -6.136 | -53.069401 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e5774b47-7946-34c4-b1be-8455647e9fc9 | -2.4851 | -56.169701 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 64c89faa-77ec-334e-b08b-d641fc33e7d2 | 1.7544 | -55.597301 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ea2e8c25-2353-3a3b-aaa9-0bdbe2b868e3 | -3.2609 | -54.058601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60977190-852e-38a2-a5be-1d17dddf9674 | -3.4758 | -59.571098 | 2026-10-08 00:48:00 | METOP-C | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5a7a9899-72f4-3adf-b19e-64e81d5e7585 | 1.7042 | -55.6357 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7671806d-6641-30fc-b1ec-bfe75dd973a8 | -1.4506 | -54.4762 | 2026-10-08 00:48:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 349665bb-6ee0-3664-9824-029bc7b78d9b | -2.9362 | -54.1703 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc941e18-dedf-38ce-a78a-3a3e28b71afa | -2.5634 | -56.152401 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c78b1b7-7568-31bf-8ff4-635712acaa57 | -5.7461 | -45.165401 | 2026-10-08 00:48:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ff36215c-131e-304f-9a7d-df4d5a7ce391 | -3.0337 | -53.919701 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9efa5a74-8934-3c71-92a3-5c5a4bf763da | -2.8624 | -49.541599 | 2026-10-08 00:48:00 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c9da047-7a6e-3622-9a5c-a252882bd958 | 1.75 | -55.571602 | 2026-10-08 00:48:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 03e56bfe-d470-3d34-838c-4930b4d694b1 | -6.028 | -51.7299 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbe4ef42-ab18-3598-8b02-1f888adac7fb | -6.5807 | -53.033199 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56acb879-bdcb-3c0a-8de4-c71cf5503d32 | -1.4665 | -54.770699 | 2026-10-08 00:48:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad942ed4-4f96-3b04-b1f6-5b861baa9392 | -3.1226 | -53.767799 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a28122c5-2b10-3446-b50b-c1d7c063e3a2 | -2.4927 | -56.1581 | 2026-10-08 00:48:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0098f369-f80c-31b5-8203-ea2efc727174 | -3.0025 | -54.099899 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b444918b-ff39-32a6-ae78-5831611d80db | -6.2417 | -52.853298 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a61c1b5a-7f60-3e97-8642-47f06319bcbe | -3.0042 | -54.107498 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f4ba635-c86a-357e-b65f-27982946ae1a | -3.2481 | -46.958698 | 2026-10-08 00:48:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b787eae-5bd2-3b4f-ad13-2aa10466de83 | -3.2575 | -54.0434 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4f06cfa-aede-3cc3-86e2-56c4aa95249f | -6.5889 | -53.023602 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8b68796a-84bc-3353-86e6-b0ef396e4032 | -11.228 | -44.870201 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21e58704-3c42-3d30-b608-9d339fd2f5e8 | -3.3083 | -54.0401 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eecf70ef-5750-3ec8-9c77-6ca742ecedf2 | -2.9143 | -54.119499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b17878f8-0dda-3d18-a5cc-8de62adc74a6 | -3.2852 | -54.0294 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d0d845d-d629-3711-a5cf-9eab4ce0fe1d | -3.0187 | -54.080502 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4213c80-13f2-3195-839d-aaa529d8786c | -3.1793 | -58.655701 | 2026-10-08 00:48:00 | METOP-C | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa1f3c28-4a8f-3597-bf99-17439fe56b1a | -4.9451 | -49.226002 | 2026-10-08 00:48:00 | METOP-C | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb71685-7419-3517-b6ab-357288048145 | -3.0498 | -54.217098 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45b91bc7-6241-3b26-b426-59f615f6981e | -3.4865 | -50.097599 | 2026-10-08 00:48:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93692a2f-4f8f-30c5-a766-8b22b6bb59e1 | -3.5453 | -59.4711 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c634c7c2-8952-39ed-9f14-9af8688662fc | -6.2531 | -52.858501 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49afce6f-68a4-3085-b297-960c074f0e5d | -6.2187 | -52.797298 | 2026-10-08 00:48:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d25513-f7a8-3f90-91ac-3f4cf528e700 | -2.9541 | -54.158401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dd52a28-2fd3-3ec3-a91a-45caa139ae1d | -2.8757 | -54.1758 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 521ec8b5-2342-3c58-b7f0-62be8bd03ddb | -6.9014 | -45.893902 | 2026-10-08 00:48:00 | METOP-C | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5ddd6c93-5ee2-3e50-8238-1633e67a3650 | -9.5931 | -47.783501 | 2026-10-08 00:48:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 57ae48f2-b1db-3bf2-be08-752c506e8217 | -3.0371 | -53.934601 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b188b712-4834-393d-94d9-98aec3e6d2b1 | -5.7102 | -53.509201 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa99b9f5-9bbe-33d4-875f-9db46c30d771 | -6.1017 | -55.724701 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b3bcd85-c1c6-32bd-af88-73b62b749414 | -3.0055 | -54.0676 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5e93229-faf3-3aa6-bef1-72537b6a5aea | -3.2592 | -54.050999 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc42f49-39e3-3952-9a0b-3d169c3ed768 | -3.0753 | -54.283901 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1570ecce-205e-3e6a-84e0-c1fcc8bf8c65 | -3.677 | -53.714699 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41d78505-1e74-3e7b-bdd1-0640850606a4 | -3.5766 | -54.3605 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45d97640-b624-30f0-819c-164ccdfb3753 | -5.9833 | -55.375198 | 2026-10-08 00:48:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9c6949a4-fbcf-3df5-9b27-b96211275e80 | -5.8803 | -50.098598 | 2026-10-08 00:48:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92f77a89-238e-36c7-8741-d049094d3e8f | -2.9922 | -54.054699 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7965de-6b9a-34d1-a1e6-c2bc1961d82e | -5.7637 | -42.091202 | 2026-10-08 00:48:00 | METOP-C | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8297452e-bc80-3e37-8332-1b93b2eab3d2 | -2.9408 | -54.145401 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ca41cde-b460-3de8-8f5b-dc70567ad960 | -6.1424 | -47.949699 | 2026-10-08 00:48:00 | METOP-C | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88fa740b-d44d-30dc-9ea8-a31429f6b04d | -3.1064 | -54.148602 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35188781-ddc5-3b7f-af03-c237cc238e83 | -13.5028 | -44.361 | 2026-10-08 00:48:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e7644277-c8a3-3361-a836-409e59b3267f | -1.8284 | -55.047798 | 2026-10-08 00:48:00 | METOP-C | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b02b2e9-da41-30d3-b058-37a3d09eb44c | -3.1576 | -54.736801 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a35bc129-8319-3243-941b-15b5a92a08a3 | -3.1069 | -54.196499 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a1056e-0bd3-3e34-a9ae-8ac8714aaefd | -13.508 | -44.382099 | 2026-10-08 00:48:00 | METOP-C | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fb75c103-2b9b-3b98-b614-3275208ab493 | -9.9196 | -44.803799 | 2026-10-08 00:48:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f03bb3f7-45b2-3adc-b3cc-fd82a653bd50 | -15.4204 | -43.701099 | 2026-10-08 00:48:00 | METOP-C | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | nan |
| 83466851-30f9-3177-be39-5bd8a2a93844 | -3.1565 | -54.097599 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c0e671c-c723-387c-bf14-85a7396028e6 | -7.2195 | -55.167198 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7affdb41-65b7-3165-a269-86a8c2203e46 | -6.6269 | -43.750599 | 2026-10-08 00:48:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b3b7d445-d1dd-31bd-8682-91fc9705ef62 | -5.7392 | -53.4552 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9de38fca-922c-3718-98d9-dbfda300c701 | -2.9356 | -53.941502 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5bc50e67-3b29-3e89-a1a9-56853731a7b8 | 2.4407 | -50.8186 | 2026-10-08 00:48:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| a8ab84a7-850b-3fd3-a0f4-3f9e9c23fe2d | -3.1749 | -50.445202 | 2026-10-08 00:48:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3b972f2-c4e1-30b6-b6fd-2b6767e81244 | -6.7242 | -55.106602 | 2026-10-08 00:48:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54a367cd-2eaf-3278-b55e-661eafebdd75 | -2.9991 | -54.084801 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8a9ee7c-1cd5-37b9-9dd0-2512e8414053 | -11.0649 | -49.540798 | 2026-10-08 00:48:00 | METOP-C | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6e22c9e0-96c7-398e-81d1-fbf3471e75e6 | -3.5423 | -51.5466 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aeb59e7f-187a-3515-a8f2-44d9e1a7a5eb | -1.4457 | -53.240101 | 2026-10-08 00:48:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 63fd252f-ecd9-343b-b2f9-e564e9aadc74 | -3.2685 | -54.0014 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1a3164f-360a-3216-9ded-50f8294af854 | -3.1695 | -54.608002 | 2026-10-08 00:48:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b4d96cc-2843-3be7-87f2-401442bc437a | -2.9379 | -54.177898 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08772614-44dc-3f98-8a7f-54545e829ef7 | -11.7825 | -46.775902 | 2026-10-08 00:48:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 98d81f23-1fb7-38b5-8e13-2e16d7f5d309 | -11.109 | -44.013401 | 2026-10-08 00:48:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1aedbffe-40f3-3d86-8e22-5e84f00f5590 | -2.9281 | -54.180099 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3ff6a71-6b8a-36e6-a319-dcfca50b0d71 | -3.5569 | -54.682598 | 2026-10-08 00:48:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34432833-452a-3fc9-afeb-458dafd05547 | -3.0442 | -51.2201 | 2026-10-08 00:48:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ef256b5-3782-39e6-b4e9-f227a888cf86 | -9.8727 | -50.507198 | 2026-10-08 00:48:00 | METOP-C | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 083577cc-6ca1-3790-aa02-dc5acf76ff22 | -5.6799 | -46.348598 | 2026-10-08 00:48:00 | METOP-C | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4513515a-6b9d-323a-9bcf-9183e5a6a231 | -7.4122 | -55.578899 | 2026-10-08 00:48:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4efb3d87-59a4-3e36-ba4b-b1288d567dfb | -4.0677 | -59.850101 | 2026-10-08 00:48:00 | METOP-C | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a03707c-0c96-3462-b36c-93976807533b | -2.9448 | -54.208302 | 2026-10-08 00:48:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cf52a510-85c4-3f21-9f9e-74484838a01c | -3.2626 | -54.066101 | 2026-10-08 00:48:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8adba67f-5d68-379b-bdea-c409e0ec47c4 | -3.7267 | -57.123501 | 2026-10-08 00:48:00 | METOP-C | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README36.md)
