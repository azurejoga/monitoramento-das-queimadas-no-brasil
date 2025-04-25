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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9449de62-b531-368a-b67e-883c9e8cd0b8 | -6.2411 | -43.3677 | 2025-04-25 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 329b8203-9440-37df-9098-6364214a2a62 | -11.3963 | -52.9477 | 2025-04-25 00:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 50.3 |
| e08bef68-07c9-3b62-a98d-bdfebcf58d4b | -6.2224 | -43.3693 | 2025-04-25 00:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 69.6 |
| d28fee3c-23d2-3ce9-9c56-d1e6faafbf69 | -6.2411 | -43.3677 | 2025-04-25 00:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 8356df95-497d-3741-a09d-555bcdd41059 | -11.3963 | -52.9477 | 2025-04-25 00:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| e9df6d6e-47ce-3b3f-94e4-ecd7fa32258f | -11.3963 | -52.9477 | 2025-04-25 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 5c7417af-0147-36e3-848a-0b6f5f6a183f | -11.4152 | -52.9458 | 2025-04-25 00:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 077c04ee-3484-33ff-9616-1aa7a9f6ff6f | -11.3963 | -52.9477 | 2025-04-25 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 04782012-565e-3a42-8571-aa2c0020e46d | -11.4152 | -52.9458 | 2025-04-25 00:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 9687eb2c-fc81-3525-afea-82be5f83a40f | -8.7265 | -44.016201 | 2025-04-25 00:37:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e02af5b0-fe2f-31d3-b695-fe6e0dbaa460 | -9.623 | -37.025002 | 2025-04-25 00:37:00 | METOP-C | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| f8b40e9d-44e9-34d6-860e-8c83bc403cb3 | -9.6287 | -37.046902 | 2025-04-25 00:37:00 | METOP-C | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| 6d4469c8-6811-3722-8c08-214c48fc1aa3 | -9.1989 | -50.726799 | 2025-04-25 00:37:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e77190ee-85d4-3649-97da-aa812606ad88 | -8.7284 | -44.024399 | 2025-04-25 00:37:00 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c8bc73db-a54d-3bdd-8fee-a5feec0cb27f | -8.1098 | -43.118301 | 2025-04-25 00:37:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5583b0a3-80db-3896-b941-55478ad801da | -9.197 | -50.717899 | 2025-04-25 00:37:00 | METOP-C | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4748ae2-495e-3b87-a488-7ba7bad0be8e | -8.861 | -49.8867 | 2025-04-25 00:37:00 | METOP-C | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f23498c-2cd5-3394-bdd5-a671adedc4ce | -19.8127 | -43.031898 | 2025-04-25 00:37:00 | METOP-C | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 9f6780aa-03c7-338b-9550-83c6a9ec195a | -11.4152 | -52.9458 | 2025-04-25 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| acb52f8a-0fec-38da-9c43-48e3e465f99b | -11.3963 | -52.9477 | 2025-04-25 00:40:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 62.5 |
| c5e3f874-1e20-3db5-b41c-3d311c0f8ca8 | -11.3963 | -52.9477 | 2025-04-25 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f0bfd84d-b988-3cff-838a-2ac4c80efab9 | -11.4152 | -52.9458 | 2025-04-25 00:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 39e5e474-e604-3a5f-8a2f-56fc5a0e34d8 | -11.4152 | -52.9458 | 2025-04-25 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| a50f986f-7ed8-358a-af5f-296c983c7777 | -11.3963 | -52.9477 | 2025-04-25 01:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 1469eed3-5072-32dc-8fb7-9553c5db9ef9 | -11.3963 | -52.9477 | 2025-04-25 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 5a57f9a3-6e3c-34fd-a361-814e85dcc381 | -11.4152 | -52.9458 | 2025-04-25 01:10:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 786725fb-53b0-3c86-85e0-eb920a1de692 | -11.3963 | -52.9477 | 2025-04-25 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.3 |
| a89ec6e4-3719-30bd-9ba6-9ebb5bd9b4a5 | -11.4152 | -52.9458 | 2025-04-25 01:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 7d3878f9-fb51-3398-b001-896590cf5f58 | -11.39909 | -52.94326 | 2025-04-25 01:28:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 29139124-ebdd-3b21-9138-306d36e91caf | -11.3963 | -52.9477 | 2025-04-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 1111129b-bc03-3c0c-bd7e-587d94fc1d5b | -11.4152 | -52.9458 | 2025-04-25 01:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 9218929e-0655-3d71-949b-220c155de2c9 | -9.71583 | -36.69709 | 2025-04-25 03:10:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| d086df0c-049a-3411-a6c0-abcfc393eef7 | -9.72153 | -36.69511 | 2025-04-25 03:10:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72eaf1bf-8031-355d-b7a0-b9e5fa895e3c | -9.71641 | -36.69398 | 2025-04-25 03:10:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c0e8acb0-c6a3-3899-9237-740c082cf407 | -9.86539 | -37.11293 | 2025-04-25 03:10:00 | NOAA-20 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 81a7cbab-9740-3bcf-b73d-4aceb8fc3250 | -9.72096 | -36.69818 | 2025-04-25 03:10:00 | NOAA-20 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e3b68b2c-4a2c-3eac-83e7-cba5e04c53a1 | -6.2224 | -43.3693 | 2025-04-25 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 1ce4bae3-817f-3d3b-b2ae-0547f3f768ec | -6.2411 | -43.3677 | 2025-04-25 03:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 5149f311-2aa4-368b-90b5-a4f1dc8be51f | -6.23858 | -43.36829 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 7577c762-b8ef-3a5d-bd4e-15c0909c24da | -6.22741 | -43.37259 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4cde0e21-99aa-3e4a-9036-0121a71c56b0 | -6.24216 | -43.37504 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72a0040e-578b-3da0-9605-6635a549b6d2 | -6.24146 | -43.37941 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cbfe079f-d0a7-3cdb-bcee-833d1d2037a8 | -6.23778 | -43.37877 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 11690f10-6949-3eaf-a79e-3fae2e029fe4 | -6.23714 | -43.37696 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f13dd236-a39b-3036-8f3e-4a48b531bb47 | -8.08227 | -43.11322 | 2025-04-25 04:00:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5e89eb34-9312-3e76-9d85-3762a82541cc | -6.24154 | -43.37324 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 37515f41-7cf2-3b6d-a953-3a553f0df141 | -6.2318 | -43.36882 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b8e7d3af-c559-36e8-aa73-9901a074068f | -8.11009 | -43.12191 | 2025-04-25 04:00:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 597f0cbe-9355-3ecd-bd8a-3cb922640bf8 | -6.23917 | -43.37006 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e4c746c1-5cfe-36cc-8329-2e60c73562e0 | -8.10652 | -43.12135 | 2025-04-25 04:00:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| babe4ccf-b564-303c-86d5-4fa79b404f73 | -6.23786 | -43.37262 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6c2edca1-c57e-3638-9ff2-aae585898cd5 | -6.24286 | -43.37069 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5a70a61-74da-3750-a886-e743fde1820f | -6.23409 | -43.37818 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0083cd56-e69d-30a3-8ecd-bf9c50f91a3b | -6.2364 | -43.38136 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1400e635-5e70-3c80-9609-ac66d76961e5 | -6.2349 | -43.36766 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5f5fc28e-2a0a-39df-b4b3-a813d467b7cd | -6.23418 | -43.37201 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 39cee945-8616-3539-a499-158607ee89ae | -6.24226 | -43.3689 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c76f42dd-b757-3575-8481-86c743a22327 | -6.2304 | -43.37759 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d878b883-01b9-3813-a613-0cb17fddd67a | -6.2311 | -43.3732 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a3387cf6-5604-33d2-94ea-bb6fd7e5c20c | -6.23549 | -43.36944 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7b3170d8-c12a-346c-aa65-c5829622881f | -6.23345 | -43.37638 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6670678f-77c9-3192-bdad-08b91b39b663 | -6.23479 | -43.37381 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 637c3f36-4fa6-3a6c-be3f-102afd924aea | -7.43907 | -45.42405 | 2025-04-25 04:00:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 900e1278-83e3-354d-b8be-18e422577eea | -6.23848 | -43.37442 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31901932-24df-3ceb-88fd-dd50ead9b969 | -6.22812 | -43.3682 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7504a4cd-cbf7-3e85-98f3-c8111d427978 | -6.24082 | -43.37759 | 2025-04-25 04:00:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0093e5e-6ba1-354e-929d-758a1207ef96 | -9.62201 | -37.03703 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b12d417d-c5ff-3113-8d1d-0623e13557fe | -12.86353 | -38.36815 | 2025-04-25 04:02:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 25081c56-dbdf-3038-ae55-bca10124d2f9 | -10.69557 | -37.048 | 2025-04-25 04:02:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f71c4469-a724-3e19-8bca-90e629e050e7 | -15.69808 | -42.2547 | 2025-04-25 04:02:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e638cb0-5163-392a-82fd-b377d9b8e5d3 | -10.69681 | -37.05073 | 2025-04-25 04:02:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e940fc91-fc77-3e28-85a9-c529d1c9d24d | -12.33359 | -45.63763 | 2025-04-25 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 797f4b88-3a82-3ebc-894d-8216db47995e | -16.18344 | -43.19666 | 2025-04-25 04:02:00 | NOAA-21 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b03e3bf5-52cf-332f-9391-765cea0d89c1 | -9.62212 | -37.03476 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 6a4e10fd-153a-3bb6-b1cb-348b41bad90b | -15.26194 | -47.46355 | 2025-04-25 04:02:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a72d7d58-9245-3108-80a1-ef954b03668e | -9.61834 | -37.0365 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 911d087c-fabf-309f-8cab-29dfcf7a0643 | -8.72514 | -44.02174 | 2025-04-25 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d2a5e156-d28e-3121-86fa-b124f430b61a | -9.61164 | -37.0311 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 5.7 |
| 446b548f-aa27-3847-96ac-16a820b95d65 | -9.61899 | -37.03214 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 50074aa2-4e30-3a3e-8c44-49c655441746 | -9.62136 | -37.04139 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff603c83-0d23-3e40-b32c-1cb76634c3c9 | -8.86714 | -49.89025 | 2025-04-25 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f6212c29-ad9e-3c7c-b6cb-2c939f69bff3 | -14.46281 | -45.27844 | 2025-04-25 04:02:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0487abb-02e9-37db-8299-6773c7c7d4f0 | -9.61769 | -37.04086 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 900aae50-0ebc-3095-9f21-e525a2432641 | -12.82318 | -38.42088 | 2025-04-25 04:02:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 51647766-9777-3428-9467-cdce72a08af7 | -11.80321 | -43.79746 | 2025-04-25 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1b58867-b04e-3eb4-98ff-6817c4ca66df | -8.72588 | -44.01725 | 2025-04-25 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e2dc9477-7895-3c5b-b522-3c36cfbd0e60 | -11.79968 | -43.79686 | 2025-04-25 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 468c1c52-8f66-3542-933e-aa273bc50602 | -9.62266 | -37.03268 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ba537ad9-2014-374d-b58c-455d37ab54e5 | -9.6215 | -37.03912 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 8.1 |
| a5c03891-9937-3378-ad23-a86b25f009fe | -9.86519 | -37.11192 | 2025-04-25 04:02:00 | NOAA-21 | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 809b63b0-2534-331d-b402-7b5add85d6c6 | -9.61845 | -37.03423 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cbe6a6c4-b36e-3289-8d32-a86df981a4a2 | -9.72005 | -36.69549 | 2025-04-25 04:02:00 | NOAA-21 | ARAPIRACA | ALAGOAS | Brasil | 2700300 | 27 | 33 | nan | nan | nan | Caatinga | 12.7 |
| 53cf8013-97b5-301d-81a9-6b328cea88cd | -11.84461 | -43.8117 | 2025-04-25 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f6be603-661d-315f-8547-d374d558100c | -9.61783 | -37.03859 | 2025-04-25 04:02:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 3.4 |
| c92f49f4-bc0b-39d1-8e9b-eb3dec20e001 | -8.79067 | -49.80788 | 2025-04-25 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 330b5c33-c598-3ae9-9619-216dcad2bab9 | -17.53312 | -40.05216 | 2025-04-25 04:04:00 | NOAA-21 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c280c012-560b-360c-b845-2ccd59ef3e61 | -19.8096 | -43.03658 | 2025-04-25 04:04:00 | NOAA-21 | NOVA ERA | MINAS GERAIS | Brasil | 3144706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc352a44-9a96-3615-8ff5-44f45de029a1 | -18.04156 | -39.92641 | 2025-04-25 04:04:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 306a527e-7128-3312-948c-0326e39feb2a | -16.70395 | -42.34666 | 2025-04-25 04:04:00 | NOAA-21 | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 622ad7c0-0123-3e37-b206-d5f079da2940 | -16.68128 | -43.88572 | 2025-04-25 04:04:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README2.md)
