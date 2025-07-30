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
| ad63590a-2b4d-3f59-8857-95dfe4af6f9a | -8.60108 | -45.52903 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78b44157-fc49-397b-92e3-89a297553a34 | -10.93169 | -44.19704 | 2025-07-30 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dbeaaca-d7f8-351a-9060-1c1f7f3d671c | -7.13271 | -44.67732 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d0debc00-020b-35b8-ae14-66acc316ed41 | -9.26124 | -50.23281 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dbfefebb-36d2-3326-aaa7-1168435b52ff | -7.35643 | -46.09367 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7536287a-acd4-347d-8381-33e29187f949 | -9.75048 | -37.00607 | 2025-07-30 04:02:00 | NOAA-21 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 4.5 |
| e2aa6034-cd7f-3252-a39a-1443f054d20d | -10.52895 | -42.55273 | 2025-07-30 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 0d9a8855-ead0-36b8-8ec5-c1b114caf612 | -7.87633 | -40.33462 | 2025-07-30 04:02:00 | NOAA-21 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2700b005-7db1-3382-917c-3790fe349c15 | -6.89014 | -44.73198 | 2025-07-30 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2c2afa41-b147-3465-87e3-f00435f20c0f | -9.8331 | -41.49793 | 2025-07-30 04:02:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0de3201e-06af-3f2f-97b8-a17e2421bd9b | -7.19553 | -44.08817 | 2025-07-30 04:02:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f87a2d42-fdab-31ba-8f0e-a7c0c3cdf9d7 | -7.0045 | -42.36754 | 2025-07-30 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b53d64d4-bdc8-3df9-acaf-f63e761b490a | -11.46743 | -45.10873 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 5af83f4e-e1d3-35d2-8df3-85835a13999a | -6.5283 | -43.33621 | 2025-07-30 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6fdbea26-110a-3a9d-8e7a-1f18f847fa08 | -9.25961 | -50.22894 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 93e038d9-3c1f-39cf-b938-487f293868ca | -6.98991 | -41.62141 | 2025-07-30 04:02:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d5c652ab-8fc5-3be3-b1ea-00b9c3db88fa | -8.60092 | -39.54263 | 2025-07-30 04:02:00 | NOAA-21 | OROCÓ | PERNAMBUCO | Brasil | 2609808 | 26 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1719f532-a859-3563-9cf1-9b97370b4dbf | -7.0849 | -42.14981 | 2025-07-30 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fe849a7e-5b2f-32a6-96bd-1f8cf4d9b9af | -5.24242 | -45.21802 | 2025-07-30 04:02:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1717d697-cd8e-380c-b486-6a2a83515e82 | -9.22467 | -48.59737 | 2025-07-30 04:02:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 568a5fc7-5e4f-33d4-8975-a79cf3e3dd27 | -5.47914 | -42.15601 | 2025-07-30 04:02:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c57f333d-3a43-3ea2-91e1-f038228b4648 | -5.67607 | -43.68258 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a7ca1dc-944f-3ed1-afe3-6d1de4b7f0e6 | -11.81876 | -44.25568 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b82703e2-cdbe-3e40-9bca-715580389a46 | -10.52557 | -42.55219 | 2025-07-30 04:02:00 | NOAA-21 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 48565f06-cfc7-3b55-9427-6079cfe20bcb | -9.56117 | -40.32445 | 2025-07-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59870422-a11c-3ba4-b121-30c816f77aa5 | -6.91688 | -38.56039 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 6.8 |
| c27b73b9-9e0e-3e79-ac13-7404c94d9203 | -6.49667 | -43.57177 | 2025-07-30 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d5046b77-c6b1-3406-bafa-330c94d19ef4 | -8.6237 | -45.88567 | 2025-07-30 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f7bfad5e-24bd-3410-857e-d027a1ebc372 | -7.77961 | -45.00391 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 88de06d8-3a15-32cf-8b78-b5d13c6dee57 | -10.62325 | -45.22977 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| baca83d1-cec0-3287-8aba-bdf3f473bdcb | -7.77492 | -45.00507 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a52cdda3-c1da-3b26-976c-58e1e781ee59 | -8.51891 | -43.3089 | 2025-07-30 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8d8d9ae9-661a-35e9-ad46-612aece92332 | -10.62245 | -45.23447 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 45ab8205-955d-38f8-b1f9-68c5199f2380 | -6.91423 | -44.73128 | 2025-07-30 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 391d0701-127a-3f60-9c3b-a7780c0bdc21 | -6.25423 | -46.1148 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05addaeb-1fa2-3b02-8447-c2c438abc7fa | -7.36948 | -43.76463 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 924c4a8b-9c3f-383c-a1b5-945a241e1bc9 | -11.46515 | -45.12244 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 1570e8ac-19a1-3167-b834-52eb56ee367f | -7.58922 | -44.8202 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 15a4f6a7-4e21-314d-9906-6a57b83bd7e3 | -6.70093 | -42.04693 | 2025-07-30 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3e76f5d3-4312-3320-99cd-912402fc26a4 | -9.17524 | -48.85025 | 2025-07-30 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 19fc1277-ede5-31b4-b905-0f73b07ce40f | -6.61885 | -44.04567 | 2025-07-30 04:02:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d6ed52d-2a38-3a28-83bb-b3683f23b6c2 | -10.7047 | -48.86555 | 2025-07-30 04:02:00 | NOAA-21 | OLIVEIRA DE FÁTIMA | TOCANTINS | Brasil | 1715507 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b119025-88d0-3c9d-8fa3-1a699ff135d1 | -9.40099 | -45.4944 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 23.0 |
| de7a7ff6-cdb2-3388-a9f2-dedd95f10b39 | -7.74352 | -51.09557 | 2025-07-30 04:02:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99185c8f-0466-3305-bda7-1ace295845aa | -9.87368 | -44.69172 | 2025-07-30 04:02:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4008bcf1-d623-3971-9e4b-5da5d4e379d3 | -6.49688 | -43.57033 | 2025-07-30 04:02:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 79fa782e-d456-3e81-9403-13170a2907a5 | -7.78436 | -44.9996 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| dad0d7b4-58d9-3718-9fb9-6b9ddfe43c02 | -10.61241 | -45.24747 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| ed277ebc-849e-37e0-be23-d70a6f0e06a1 | -11.2086 | -41.59835 | 2025-07-30 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 672563a0-fba2-361e-a4e5-c38e8059d2d1 | -7.15856 | -44.04726 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| fc1fe674-3707-3381-aef3-c56ef9da595a | -5.82594 | -46.35232 | 2025-07-30 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f714d334-219f-3504-a139-f6dcec7aea6e | -9.26189 | -50.22934 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 192d2e95-6286-36b8-8c79-d2070f101cc5 | -11.53931 | -44.25208 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db8edb39-9724-324f-838c-a608b8a41cd7 | -9.57603 | -43.87926 | 2025-07-30 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| fe5b1a31-f24a-3c7d-898d-a5a744558c03 | -4.89599 | -44.95872 | 2025-07-30 04:02:00 | NOAA-21 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d250e1a9-fd0d-392b-9323-defca3bb4e35 | -7.86384 | -47.87328 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 51fc2cb0-b384-3088-ab14-f6240686745a | -8.40464 | -50.11622 | 2025-07-30 04:02:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e6589558-4aff-3f93-9249-13e71c96c0dd | -5.40159 | -43.24553 | 2025-07-30 04:02:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f2d50d8a-e8a4-31b8-a12b-d06c1972e617 | -10.93968 | -45.78487 | 2025-07-30 04:02:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6623dd17-6044-338c-abea-dee16f0e78d4 | -10.61404 | -45.23794 | 2025-07-30 04:02:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 35e7d9d6-b55a-31d1-9885-71742975a9c0 | -10.40798 | -47.2541 | 2025-07-30 04:02:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 062bbfc7-da37-3acd-8d7e-be0497523536 | -8.0328 | -46.90934 | 2025-07-30 04:02:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d6968281-bb89-3518-8ac9-8c4bebeece50 | -7.35485 | -43.76224 | 2025-07-30 04:02:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c4c743d-0056-3db0-9537-7cdaff5bfe2c | -7.91003 | -42.6313 | 2025-07-30 04:02:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 07f15d42-d319-3dda-8053-798b4354652e | -6.70434 | -42.04748 | 2025-07-30 04:02:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 615743cc-143a-3b84-8ba2-5afb0be300b3 | -8.07233 | -42.95226 | 2025-07-30 04:02:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c56d7fba-7052-3838-8052-42be5a9b27f3 | -8.94947 | -46.73913 | 2025-07-30 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a2317f23-ba04-312c-9e05-58b98c4c545c | -11.46684 | -45.12139 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 73b1d83b-40a0-35da-99d8-12091bc1180b | -7.11944 | -44.47322 | 2025-07-30 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3669f63e-3369-32de-ad0c-58d1707cfbd6 | -8.02483 | -47.68433 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 429eefe7-f401-3619-b205-c1c6e4a447a0 | -6.45875 | -53.36177 | 2025-07-30 04:02:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c2ae9b4-11b5-3aa1-bd83-a45dd300978a | -7.23018 | -43.08808 | 2025-07-30 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2c00eec0-8c3d-34fd-8be1-ed49b2d3b4fb | -6.47053 | -41.6392 | 2025-07-30 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c2d17579-f09c-346f-9f97-c153f5c119e2 | -7.1048 | -44.9673 | 2025-07-30 04:02:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74027641-9513-31f0-bde5-ae8abbfb4fca | -9.25898 | -50.23242 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2569974f-cccc-3297-b202-3f0a5961cfe3 | -6.91036 | -44.73056 | 2025-07-30 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| abfc1083-0037-3b4a-8b87-cc35819bba90 | -5.68724 | -43.68429 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51751e69-be03-3692-bab9-0740d37c195f | -10.51619 | -44.89341 | 2025-07-30 04:02:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 269e9092-e8b8-3173-9295-e9313d2edb66 | -11.46296 | -45.11258 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| eb6c1df3-d12a-3766-a98a-cb9b25648e76 | -6.87787 | -38.54313 | 2025-07-30 04:02:00 | NOAA-21 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f85ad572-1041-339d-9b54-f2b30d3f293d | -4.38025 | -49.03482 | 2025-07-30 04:02:00 | NOAA-21 | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58c1dada-3553-3785-935d-3d60bf888adc | -8.33235 | -44.63617 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13ffa30f-801b-3d7a-b7f8-58e187fda77b | -5.47975 | -42.15221 | 2025-07-30 04:02:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a0a919a0-b6e3-3fd0-8a9f-90504fd81b5f | -7.68454 | -46.54022 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d63118ce-1543-3548-b997-1e23eb81151a | -9.17747 | -48.84653 | 2025-07-30 04:02:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ac5d189b-6d5f-3c80-9847-bfe9f76e60d4 | -10.50887 | -43.94281 | 2025-07-30 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4508d9b2-984e-3768-9516-0741e976f76b | -6.48052 | -41.62956 | 2025-07-30 04:02:00 | NOAA-21 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 690510e0-1646-310f-971b-8a14a5f4ea01 | -7.15413 | -44.05101 | 2025-07-30 04:02:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 343508ea-6192-3aba-b13a-c1fdf00cf174 | -8.64099 | -45.51096 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03746a3d-c61c-3ae7-bdad-8e8a584e594b | -11.81808 | -44.25977 | 2025-07-30 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9b1a89ba-01dc-34c0-af17-4fec087c917d | -9.05238 | -45.07367 | 2025-07-30 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 432b4ae7-dff6-308d-b16e-66a67d84ee62 | -8.6243 | -45.88219 | 2025-07-30 04:02:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6fa4582c-6071-360b-bac9-9b18f0130d4f | -7.85967 | -46.73303 | 2025-07-30 04:02:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc6aa99a-a279-34b0-8616-f79d657b2a75 | -7.14059 | -44.37061 | 2025-07-30 04:02:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb9f2069-df69-3e14-a1e5-ea76865d8314 | -9.23772 | -50.04461 | 2025-07-30 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ad79cc9-769e-3d31-a557-0b6ea723d304 | -5.7643 | -43.90383 | 2025-07-30 04:02:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d2f7ef9c-936d-38cf-8622-783cb42288e7 | -9.60248 | -40.56327 | 2025-07-30 04:02:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 19a31597-4d75-3d63-8963-d2291b3dc98f | -8.02103 | -47.67871 | 2025-07-30 04:02:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ae35d210-16c0-34fe-b476-718118057e7b | -8.41469 | -45.68721 | 2025-07-30 04:02:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4920e905-8516-3fba-a002-4799287b38a7 | -9.50117 | -43.16682 | 2025-07-30 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |


[Clique aqui para ver as próximas entradas](README14.md)
