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
| 9ce4dcc6-7ab1-32b9-9299-a47acc69269c | -3.5586 | -43.476799 | 2025-11-20 00:15:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2cbd74be-38e8-3431-b3db-72e5854056c3 | -6.6919 | -38.058701 | 2025-11-20 00:15:00 | METOP-C | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 634b935f-c127-3e00-ae5b-f7f65ba8b41a | -3.0179 | -49.4193 | 2025-11-20 00:15:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 973d09c2-d9dc-3641-90cf-5ebdfb17b403 | -4.1499 | -43.6758 | 2025-11-20 00:15:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e82d288-6cee-365e-b9ad-357896452920 | -3.557 | -43.4697 | 2025-11-20 00:15:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9c6188ec-741e-3ae2-ab88-f8b4bb14e248 | -10.3465 | -48.9067 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b8f963df-6bd9-3448-bb39-34a48cc86a14 | -4.1417 | -43.685299 | 2025-11-20 00:15:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2f2f4903-7446-346b-83d9-fced38cdc1e8 | -2.2936 | -46.295799 | 2025-11-20 00:15:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64e765f9-9bbb-332b-b434-cfad782b1b2f | -2.9991 | -48.741402 | 2025-11-20 00:15:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3506f875-d2d3-3934-a9b8-6dee1748269d | -10.3492 | -48.869701 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e504c7f5-37e5-3fb0-b282-2a802b773ecf | -5.9271 | -43.520302 | 2025-11-20 00:15:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a6686439-80c7-30fa-a8e9-cc6387ef18df | -6.6939 | -38.0672 | 2025-11-20 00:15:00 | METOP-C | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 387eccf9-d762-3a29-be99-85234dc085a4 | -5.6453 | -37.429298 | 2025-11-20 00:15:00 | METOP-C | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 8077330b-af24-3581-b982-c8f8b2277b44 | -5.4972 | -39.1693 | 2025-11-20 00:15:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 526f7900-e7d6-3b15-b703-af5fdebfdf24 | -5.7476 | -45.1078 | 2025-11-20 00:15:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| eca233a0-d4d9-38c5-896a-56d142746b99 | -5.7457 | -45.099201 | 2025-11-20 00:15:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6e4fc8bd-98eb-3ae6-b9a6-eff62a1729ab | -3.254 | -42.5481 | 2025-11-20 00:15:00 | METOP-C | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f45fb826-a413-3974-aaf3-2afb102caaea | -4.1384 | -43.670799 | 2025-11-20 00:15:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fcb89840-bb38-3df9-b09e-10006181e513 | -3.002 | -48.754501 | 2025-11-20 00:15:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce2b7dd0-dcf1-3959-a337-418d8ea38115 | -5.3539 | -43.0341 | 2025-11-20 00:15:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1f7c5641-263c-3b65-909e-43660e7ffee2 | -9.2333 | -40.511101 | 2025-11-20 00:15:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6f8ed2e0-ba83-32bd-b86a-7548ddfcc256 | -2.5124 | -47.807499 | 2025-11-20 00:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9d4b421-2b3c-3c08-a550-30e0eff8a762 | -6.9862 | -39.004398 | 2025-11-20 00:15:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c7cb42d4-1e9c-33ff-8975-c694bc40e8f0 | -3.0081 | -49.421398 | 2025-11-20 00:15:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 707c2614-2863-383a-ad31-af757d4a46e1 | -15.784 | -43.365002 | 2025-11-20 00:15:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 47580bff-96bf-364c-a0a9-ebb9fe035bf2 | -2.9142 | -40.3969 | 2025-11-20 00:15:00 | METOP-C | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0e3d4c9a-1fee-3f89-8daf-5c6b982d51e4 | -5.4954 | -39.161598 | 2025-11-20 00:15:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 57e44728-a6db-35b0-9810-dcadae3f7e2f | -6.6821 | -38.061001 | 2025-11-20 00:15:00 | METOP-C | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 2f1f661b-72e7-3262-9462-a9afa65a827b | -1.0199 | -47.205502 | 2025-11-20 00:15:00 | METOP-C | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67e4bca1-af8b-3e26-b12e-c2ca2e2488e6 | -15.7821 | -43.355701 | 2025-11-20 00:15:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b65e1558-743d-376f-b6f5-8dcfffbed1f6 | -3.0312 | -45.828201 | 2025-11-20 00:15:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d624f42-9fa8-3abd-ad1a-e437ab4be120 | -5.7364 | -39.887199 | 2025-11-20 00:15:00 | METOP-C | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 48d3ee62-0a85-37bc-b434-2c5477791078 | -3.0586 | -45.813 | 2025-11-20 00:15:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 90952a57-751a-3f26-9015-a901e8c22d73 | -13.4868 | -46.718498 | 2025-11-20 00:15:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5a474fdb-b224-34ed-97af-c1b73c929c92 | -5.3555 | -43.041199 | 2025-11-20 00:15:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 946e2c61-904f-3473-8caa-629dbf09bca1 | -1.0177 | -47.195801 | 2025-11-20 00:15:00 | METOP-C | CAPANEMA | PARÁ | Brasil | 1502202 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 17e43a0b-8821-34dc-b2f8-643cf124f911 | -2.5001 | -47.7985 | 2025-11-20 00:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed03a379-4066-3990-a376-4f98b4911010 | -4.1401 | -43.678001 | 2025-11-20 00:15:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7d4de9e4-6ed8-389e-9f6a-48d5160a6e06 | -4.1482 | -43.668598 | 2025-11-20 00:15:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70575e73-0395-3b17-8602-a13f53db0cef | -10.3598 | -48.922298 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 756f6654-4e51-36f3-b6b1-0bf7c6d701f8 | -7.0049 | -39.040298 | 2025-11-20 00:15:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 34377236-71a5-3a03-b9dc-334bc1b14d1c | -7.0031 | -39.0327 | 2025-11-20 00:15:00 | METOP-C | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 577d20ac-4421-3f1a-a4ec-2b0aa6714e7c | -10.4773 | -49.354801 | 2025-11-20 00:15:00 | METOP-C | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e52e9b4b-8353-3127-9f5e-103feddf141a | -5.7111 | -39.2015 | 2025-11-20 00:15:00 | METOP-C | MILHÃ | CEARÁ | Brasil | 2308351 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 00f7e867-b74e-34dc-9cc1-20cbc2fcad5d | -5.6431 | -37.419899 | 2025-11-20 00:15:00 | METOP-C | UPANEMA | RIO GRANDE DO NORTE | Brasil | 2414605 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| e777e22c-53ba-3357-b4e8-113e461ee904 | -10.3527 | -48.887199 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 496618cb-22db-3749-9cc9-93086add2229 | -2.9159 | -40.404202 | 2025-11-20 00:15:00 | METOP-C | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d9f418dc-1b54-3dac-8784-c981e8c96f62 | -3.5554 | -43.4627 | 2025-11-20 00:15:00 | METOP-C | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f1a2857-0c67-3e1f-9b98-d1a1911aff49 | -15.7802 | -43.346298 | 2025-11-20 00:15:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| d67e69e9-065f-399c-8147-b01078ee2fef | -2.5026 | -47.8097 | 2025-11-20 00:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f135463f-e36b-390a-b4b5-f47dbcfcd271 | -9.7904 | -36.372002 | 2025-11-20 00:15:00 | METOP-C | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| bf5260a2-8d77-38a1-bb12-d2c3fee6f81c | -2.9726 | -49.262798 | 2025-11-20 00:15:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 264fbebb-e6e9-3b96-bb89-be00de93526b | -10.343 | -48.889198 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48f4635c-d18a-3da8-aefa-1484b46c0172 | -3.2555 | -42.554901 | 2025-11-20 00:15:00 | METOP-C | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf461ee9-73d7-3f37-ad5b-137104f7e0e8 | -6.5463 | -41.704201 | 2025-11-20 00:15:00 | METOP-C | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 418ca35e-3693-3a18-8a61-8fdaa818106e | -2.9747 | -44.579201 | 2025-11-20 00:15:00 | METOP-C | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b9212cea-6765-3da2-a169-dbe065199340 | -3.0799 | -49.514 | 2025-11-20 00:15:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 79e4b29b-ef46-3753-92ce-612075ee6dae | -6.0822 | -42.111198 | 2025-11-20 00:15:00 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9228323a-956c-317b-9317-549b6c912e07 | -6.6841 | -38.0695 | 2025-11-20 00:15:00 | METOP-C | APARECIDA | PARAÍBA | Brasil | 2500775 | 25 | 33 | nan | nan | nan | Caatinga | nan |
| 2771936d-f8ac-33a3-a752-92728586b286 | -8.8989 | -35.931999 | 2025-11-20 00:15:00 | METOP-C | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8edf2c9a-f8cd-32d6-ad9e-11c489e20c3c | -6.7318 | -38.843899 | 2025-11-20 00:15:00 | METOP-C | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1975fb3b-b5af-3c10-8689-93f0ba283a5b | -10.3562 | -48.904701 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 89d13063-81fc-390b-99e6-7ac36265de20 | -10.3625 | -48.8853 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f11ddc49-7074-3d56-b0ed-1ca84eac9699 | -15.7919 | -43.3536 | 2025-11-20 00:15:00 | METOP-C | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 55672cea-6243-3324-adca-85267ef09399 | -2.5099 | -47.796398 | 2025-11-20 00:15:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ead91b3b-c1a8-3b55-9787-f24ef132e80d | -2.8545 | -45.002602 | 2025-11-20 00:15:00 | METOP-C | SÃO VICENTE FERRER | MARANHÃO | Brasil | 2111706 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| cc89ea13-43ab-3bbc-9cb6-0d80a43fa1cb | -5.9052 | -39.237499 | 2025-11-20 00:15:00 | METOP-C | DEPUTADO IRAPUAN PINHEIRO | CEARÁ | Brasil | 2304269 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fa9ef52d-a260-3479-bc5d-26ff8d4120a8 | -6.0806 | -42.104301 | 2025-11-20 00:15:00 | METOP-C | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d4a686ec-524b-3aaf-8188-e13742618b3d | -8.8964 | -35.921501 | 2025-11-20 00:15:00 | METOP-C | IBATEGUARA | ALAGOAS | Brasil | 2703007 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 4d56aa7b-c037-3d8e-a702-f520931f9cba | -10.366 | -48.902802 | 2025-11-20 00:15:00 | METOP-C | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 59da9f8d-1891-36c9-9e59-6ca81eb53f9a | -3.7406 | -40.9832 | 2025-11-20 00:15:00 | METOP-C | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 326bb5e0-e1e5-37ff-b2ff-5d1edfd21e70 | -13.4841 | -46.704498 | 2025-11-20 00:15:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| aa7add7b-4dfd-3d5a-81ce-2df4aa2a7b52 | -3.0292 | -45.8195 | 2025-11-20 00:15:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5eb33bc-b420-3932-9bca-a1af7cdee5ec | -13.4743 | -46.706501 | 2025-11-20 00:15:00 | METOP-C | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8666647a-716b-3ee8-b72b-65067dcea45a | -9.2349 | -40.518002 | 2025-11-20 00:15:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 5c711a1e-5f4a-3833-a20b-33dbdc3b4331 | -2.9824 | -49.2607 | 2025-11-20 00:15:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eeb2194d-ccc1-35ab-af5d-b3762012a5e6 | -2.922 | -40.341202 | 2025-11-20 00:15:00 | METOP-C | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0c39d49e-cbbd-323c-8c4c-6f844672bcf7 | -8.6546 | -40.461201 | 2025-11-20 00:15:00 | METOP-C | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| f51b5360-019a-3a57-b83d-de98044ae3ae | -21.24167 | -49.17102 | 2025-11-20 01:09:00 | TERRA_M-M | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 32.5 |
| 39ebf3ef-a042-388a-96bf-f27e759f603b | -17.62053 | -54.18007 | 2025-11-20 01:09:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 3170bedf-dbb8-35d1-9b7c-0d6fb1c9b126 | -18.12483 | -54.526 | 2025-11-20 01:09:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 30.3 |
| c549ccc5-4b52-3230-a0f5-8c0a2c8d333f | -18.16028 | -54.54906 | 2025-11-20 01:09:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9c76001a-9c18-312c-8c70-37c2323a6f5b | -19.48018 | -53.94584 | 2025-11-20 01:09:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 63c671b7-223a-32a0-93ba-a417a3f1ddc4 | -20.8821 | -52.34583 | 2025-11-20 01:09:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a67d429a-76b2-3726-9d74-d40ca236e2f4 | -21.04643 | -48.55155 | 2025-11-20 01:09:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 50.2 |
| 11864fb3-2689-3389-ac40-7bf942aebfd7 | -17.53442 | -53.69736 | 2025-11-20 01:09:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 5485cb16-2c5b-318a-b487-0d454367c62d | -18.12307 | -54.51455 | 2025-11-20 01:09:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 16.6 |
| 615301c0-bd9c-3d31-ad91-d08847268e79 | -15.54312 | -50.66387 | 2025-11-20 01:09:00 | TERRA_M-M | MATRINCHÃ | GOIÁS | Brasil | 5212956 | 52 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 395cd81f-4da7-3238-a671-347316b543c2 | -20.2983 | -50.95568 | 2025-11-20 01:09:00 | TERRA_M-M | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| e1ca81d9-81f2-3fe4-abd6-94bd9507b6da | -21.03218 | -48.55483 | 2025-11-20 01:09:00 | TERRA_M-M | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 27.6 |
| 80461d89-6c68-3a85-8c45-c9387b30eba1 | -20.56217 | -49.56662 | 2025-11-20 01:09:00 | TERRA_M-M | TANABI | SÃO PAULO | Brasil | 3553401 | 35 | 33 | nan | nan | nan | Cerrado | 24.4 |
| f8a9240f-4d69-36a3-9091-6e88f9bfdd09 | -20.67773 | -50.11982 | 2025-11-20 01:09:00 | TERRA_M-M | FLOREAL | SÃO PAULO | Brasil | 3515905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 21.1 |
| 46f807f4-6ad2-38f2-bfd9-4362fb242582 | -18.16208 | -54.56053 | 2025-11-20 01:09:00 | TERRA_M-M | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 689b81a3-ec13-35a6-b48b-87f676ef2e50 | -20.73469 | -55.69856 | 2025-11-20 01:09:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 21.4 |
| 75b72680-3dc9-3e71-811e-b7c0fe007fe1 | -20.73614 | -55.70838 | 2025-11-20 01:09:00 | TERRA_M-M | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 9.6 |
| d4a3a176-a940-3a73-928e-0b72a8a0587e | -17.53649 | -53.71051 | 2025-11-20 01:09:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 26.7 |
| d0955068-4fa9-3d7c-9e7b-dfb68b4a9b51 | -17.62243 | -54.19233 | 2025-11-20 01:09:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f4e2663e-a028-3b2d-80e1-08d80c24f13c | -10.8274 | -56.965599 | 2025-11-20 01:09:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ff37b409-aabd-35ee-80a0-9a1be0baf532 | -21.0219 | -48.553299 | 2025-11-20 01:09:00 | METOP-B | BEBEDOURO | SÃO PAULO | Brasil | 3506102 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 462e5aab-abf7-392e-a5c3-92999d0ae881 | -20.292801 | -50.960899 | 2025-11-20 01:09:00 | METOP-B | SANTA FÉ DO SUL | SÃO PAULO | Brasil | 3546603 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README2.md)
