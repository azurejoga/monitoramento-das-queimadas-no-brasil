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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da239404-e252-38e1-8837-3c7a1a9c054e | -5.77689 | -45.07782 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 02c9dbea-e765-3a5f-a4cb-54a88b4ecab2 | -5.42743 | -43.43329 | 2026-09-09 04:44:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59eb004a-c462-31af-b8dd-e5a4ee068971 | -4.37754 | -55.04469 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ad0f2fda-a8a8-31ef-ae5e-3a60cb5fc645 | -3.36216 | -59.42936 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d970761-5a83-3500-9e58-ce7c25f06cab | -3.26814 | -50.07999 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0e4568f4-75d1-37e1-8674-1fb636dafb60 | -3.55093 | -48.18643 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24a65bef-cde3-3175-97d0-3c64ef09b90d | -3.25001 | -47.24811 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed919206-0963-3bb7-be3f-c36858fa061a | -1.03698 | -53.73463 | 2026-09-09 04:44:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ebee3af-4368-3e67-b9bb-96870bfbe5d3 | -2.93542 | -50.47839 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 32b04da3-4307-3dd1-a372-662beb6d5bf2 | -6.41424 | -47.50708 | 2026-09-09 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 74d0b62e-8d1f-3abc-a3aa-8ed3f71c22fe | -2.94394 | -50.46858 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22802f1f-f25b-313e-b118-3f7551e69125 | -3.77072 | -53.41454 | 2026-09-09 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b1c6beb7-49a7-38fe-87f2-ce37589e7324 | -2.02607 | -52.10069 | 2026-09-09 04:44:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44ed4d1a-c076-396a-b079-2c6c8635f27f | -5.76527 | -45.07594 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 81704b56-abc6-3d07-b1ac-ea258c54e2eb | -3.95877 | -59.35986 | 2026-09-09 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7dc9be4-bd05-3ba1-ab83-d366d8385d1c | -3.36596 | -50.3977 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0157e0f2-36cd-3abe-9540-16dd6563c2e4 | -3.89345 | -59.60383 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e77334c5-f5e1-3569-8bc2-17a069ac0b75 | -3.26367 | -50.08651 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 46825594-29d2-3f8a-b5ff-360bcdb918d2 | -2.83861 | -49.50986 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cd68c973-83fd-3709-b5e5-8ab926de98b9 | -3.96382 | -59.36485 | 2026-09-09 04:44:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a10ca694-495f-3a86-9c6b-a7aa426e8bcf | -2.93261 | -50.47421 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5626bbdf-6ef0-3f12-9cde-b4a1fd909681 | -2.93494 | -50.45972 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3807a4a5-ea98-3ad5-8c56-7b219572f79d | -4.00446 | -51.02807 | 2026-09-09 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 0463f2ea-b8e9-378d-904e-b855359d7ffa | -6.16561 | -44.65331 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 613ded46-b669-309e-932f-c5246088442b | -4.02099 | -50.4458 | 2026-09-09 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b33f59d-c9b2-3014-a41e-22dc9cc2af2e | -3.89244 | -59.60405 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c5b09995-8f49-3929-8ff5-00d7d0b60799 | -5.85312 | -49.76138 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54c167d8-bfac-3054-900a-c7079ce89b3c | -4.66795 | -55.62862 | 2026-09-09 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f9a17229-c612-33f8-b682-a15f3dd5dc1c | -3.95386 | -49.01131 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2d787807-ecc8-3583-a287-d6accd48ab4a | -3.55203 | -48.17947 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d87af401-8fcc-389d-b50d-0a47e03772e3 | -6.75908 | -44.57803 | 2026-09-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a7a52e5c-d1b8-33d2-a4e9-e6ba026c014d | -3.35561 | -59.43494 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18ddfd0b-7061-36ef-b60a-e7483780e7ce | -2.93997 | -50.47166 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 53253519-8663-3979-ac22-e3a1d5f9da26 | -4.29863 | -49.08688 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 70734d1a-006c-3930-8fa7-eb8f85b5ce6a | -5.76914 | -45.07657 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 805188af-7ce0-37bf-a5cd-ef332ad3928c | -6.62305 | -42.22848 | 2026-09-09 04:44:00 | NOAA-20 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 7fb32241-1181-33bd-905a-5c0f5fb3150b | -4.38115 | -55.0493 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a47bf802-36ba-3f26-b907-06b445dbd765 | -1.6683 | -55.66996 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c59302fb-8f9d-30f8-a96a-6699287c593f | -2.55948 | -54.7419 | 2026-09-09 04:44:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96af6a4f-bcdd-37d4-bf07-2aa7a0889dd3 | -3.24209 | -47.25433 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0f643cf6-c3ab-3e0c-9bbd-b9c3d918ef19 | -2.76556 | -48.57674 | 2026-09-09 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a030630f-be6c-3a9b-92ff-c2df17426252 | -1.18966 | -55.71961 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 0c3a68ee-922a-35f6-b8e5-929e591c97ce | -3.72436 | -45.27184 | 2026-09-09 04:44:00 | NOAA-20 | BELA VISTA DO MARANHÃO | MARANHÃO | Brasil | 2101772 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 30e344f5-631e-3216-91c0-279dccec16ca | -2.93436 | -50.46334 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43d9996a-f0ea-378c-8ac3-faf2817ca013 | -3.85131 | -49.05866 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca65c236-c1b8-37e9-84cf-e480b484e48c | -4.00788 | -51.0286 | 2026-09-09 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9ca8c16e-48cb-3d56-ae98-8decbf1f7a7b | -2.93822 | -50.48257 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 579d0a92-7424-3a7a-89d9-5e477961214e | -2.38842 | -47.60671 | 2026-09-09 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| da502e25-5257-393c-beb2-25227478962d | -5.75101 | -50.18919 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a74db71-9251-301a-aace-cc99fc003801 | -6.37055 | -43.59267 | 2026-09-09 04:44:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92aa8e7c-59c6-3e2f-9292-c48e9e118c6d | -1.19601 | -55.71029 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0f28a00a-0b7f-3a48-85ec-8933f75330aa | -2.95392 | -48.58907 | 2026-09-09 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ffe1870-c54b-3cc2-a190-f7099c85f2eb | -3.24379 | -47.24342 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ace28b6b-a470-3f7b-8897-abd235847e78 | -3.76242 | -49.10423 | 2026-09-09 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 82e424b4-0d8c-3b50-ac6f-9e27a865f0a5 | -3.52811 | -51.47845 | 2026-09-09 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 899ad537-1a5e-31ca-babe-0f38127229a0 | -3.89756 | -59.60918 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15ad9f63-fb24-3ab9-be14-ecf3bdc9bedc | -5.77301 | -45.0772 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| c2d808aa-c84b-3b32-bce3-68f62fadc380 | -3.68379 | -58.5236 | 2026-09-09 04:44:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ebd77cc-0fce-32d3-a2b5-652c58b64e62 | -5.79948 | -50.20438 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3be01b3c-6dd1-3f6d-afe3-af2dff14761f | -6.16002 | -44.6632 | 2026-09-09 04:44:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 487f206b-5950-358e-a48f-e85ba3fba823 | -2.936 | -50.47475 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a5944ac8-e378-3868-9eb4-f55c45f0b687 | -3.44636 | -47.27048 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e50da252-bddc-390e-95be-3946d3ea61d2 | -2.94113 | -50.46442 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 3180bf1d-f6dc-3a91-9578-a45da9dc24ef | -1.19271 | -55.71746 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bf6ca277-99e8-367e-8cb7-763640f2b0cf | -2.89099 | -48.27864 | 2026-09-09 04:44:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a8e3c7a-964b-3f01-9465-f2cb9b17cf05 | -1.1888 | -55.72477 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 239c1027-076e-3480-9450-e3f12a0fd8fd | -2.93319 | -50.47058 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 998f5492-994b-392b-8832-b1b1eb238c87 | -2.94616 | -50.47637 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| bb1c67e6-58e0-34ae-bbd8-e191bece4f92 | -3.76985 | -58.85207 | 2026-09-09 04:44:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d51de35b-b372-3f7b-bae4-af7d37aae86c | -3.23983 | -47.24654 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9c05995d-0451-3142-9583-18b34e33752a | -5.77763 | -45.07292 | 2026-09-09 04:44:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| cc7e831f-a996-3c96-963a-c03c675d0757 | -2.93097 | -50.4628 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 29039783-5436-3be9-973e-8fca0378d0b9 | -1.61122 | -54.9141 | 2026-09-09 04:44:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9f7ed64b-7647-3932-b146-15db52c822d2 | -5.41935 | -44.79333 | 2026-09-09 04:44:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dae6ac13-36b1-3f7f-a913-6a40418789d6 | -3.24768 | -50.82658 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85585316-71a5-393d-b80b-e39891e5ddec | -4.0182 | -50.44171 | 2026-09-09 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e0c66e-2960-3672-847b-ce865a0d233f | -2.93155 | -50.45918 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c58e0888-22b3-3bad-a9b5-11836e8f1089 | -3.24827 | -50.82288 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| fed608a2-9547-3771-887a-583232f2b115 | -2.94171 | -50.46079 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 84404b8b-2e40-3f3d-8fa3-91f639910846 | -2.94278 | -50.47583 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 74c35642-ca4b-310c-81cc-983ae800df31 | -4.49684 | -55.49326 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6ce78e8-5a60-3ff9-8563-4479d1787d5c | -2.94336 | -50.47221 | 2026-09-09 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b3ebcf56-f16d-3762-ad21-695cc2a136dc | -4.91534 | -55.82372 | 2026-09-09 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23d72889-8323-3031-8c1e-17654e8d6c45 | -5.80004 | -50.2009 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0436eff3-d89e-3578-bf91-b2831326eb24 | -5.79671 | -50.20038 | 2026-09-09 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7cf0242a-87cf-38e0-86b8-0c1af77b6a6b | -3.97153 | -47.58437 | 2026-09-09 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 40807ae5-9cd9-3246-ad82-f66e942ea58d | -2.83806 | -49.51332 | 2026-09-09 04:44:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a638e2e4-6798-3f35-9fb0-2da518e69d1a | -1.61475 | -55.13678 | 2026-09-09 04:44:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dcd8e8f1-bcdf-349a-9fb4-5072f7a93dbb | -4.53984 | -54.92813 | 2026-09-09 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 1c89dd2a-7604-3291-9ff6-3661d77d628a | -3.29852 | -52.10926 | 2026-09-09 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1073f317-098b-353d-9c94-c566343f8795 | -1.18722 | -55.72177 | 2026-09-09 04:44:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 970f95e8-d0a1-3dc4-aabc-5a714e5c3ec5 | -6.83375 | -39.4077 | 2026-09-09 04:44:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 800c4752-302c-3c36-98b2-84ded869bf1c | -6.41161 | -47.5069 | 2026-09-09 04:44:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 16cf313a-4266-3526-81e8-dcd50c4fb6bf | -3.37451 | -59.42726 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 19c2b8ff-37d5-3ffe-9bef-c2ced799a6aa | -6.76011 | -44.57088 | 2026-09-09 04:44:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90476ced-1dc1-3f8e-9152-5b8c9b02a84a | -3.43285 | -59.26197 | 2026-09-09 04:44:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b732a3b6-cd98-3671-897c-0fa96f393a71 | -3.36212 | -59.43178 | 2026-09-09 04:44:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 392e41dd-f4dc-3507-ab6d-e1ca620feadf | -3.4458 | -47.27413 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d8ea7e99-e38a-3c2a-84d6-2602c07c8bb6 | -3.96814 | -47.58387 | 2026-09-09 04:44:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 621a2cdb-8db5-34c9-b07a-d90ae632c086 | -3.54761 | -48.18591 | 2026-09-09 04:44:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README20.md)
