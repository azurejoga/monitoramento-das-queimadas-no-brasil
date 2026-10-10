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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2c539f43-aa61-3803-8598-b055c5a2ff91 | -1.43701 | -52.83062 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7e93e7f7-3f50-386b-bf3a-9664ecbda6d9 | -3.17731 | -50.58469 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ed6927b-3bce-3446-bec4-1cb236c0e936 | -3.58424 | -54.71498 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c4825f29-8dbd-39ab-83a3-e6810f17dd08 | 1.67734 | -55.61174 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 52748584-e7ae-37a4-90d7-39158fc6ee46 | -3.18173 | -50.58093 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38105342-8173-3286-9940-adca326fbb3d | -3.11644 | -53.791 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a0da30a-d3cf-3555-97d1-fdb0d2660808 | -1.21107 | -55.6596 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87015088-72f5-316b-a99f-84e6dd843a24 | -1.62789 | -54.43493 | 2026-10-10 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| dfcd2576-1fff-3675-872c-128178d6ea13 | -4.11972 | -50.98308 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aaebc8e9-7c7c-35c6-922b-e0f4487ba5dd | -5.99622 | -41.37493 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bf1f20ee-9d61-36b7-84ef-f56e8fef3677 | -2.39724 | -57.89557 | 2026-10-10 04:44:00 | NPP-375D | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 69624910-2b91-34ee-8f0a-0512fe7a24b2 | -3.86847 | -55.987 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 82ad4617-0e70-3716-813a-bb91e5c73197 | -3.31938 | -54.16793 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11f4a5ad-acab-39e7-83e5-a3d75673c67a | -2.82314 | -51.28039 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13f4edd3-e3df-3569-a618-be2102936b50 | -3.27614 | -50.02407 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8483f6c6-76a4-396e-9d34-873f99d487b3 | -3.18259 | -50.59901 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3e7773fc-af74-3849-84da-9037d6f0cdf9 | -4.15996 | -54.33734 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 52aa3511-e8b8-3cbd-8af8-24b3b7f95bb1 | -3.31124 | -54.00154 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 2d127e64-f544-3a3c-b45b-a1b468591837 | -3.78488 | -59.37568 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d9c48610-69cd-3406-bb37-b0705df19747 | -3.27974 | -50.02465 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d70de44b-4e44-375e-87df-844dc4782c64 | -5.0909 | -46.13776 | 2026-10-10 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a4905bf-bf83-3a4e-9393-c78960165229 | -3.66958 | -55.54403 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ad1a5a41-887f-3cc2-848a-a4124179b427 | -5.35317 | -45.68511 | 2026-10-10 04:44:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 536cf87e-d49a-3272-abe8-8f36b408db2a | -4.73739 | -55.6739 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56e7e44c-97b1-31b8-909f-4a2c8bc4998b | -1.26961 | -55.75653 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b10c04ed-df7c-3acf-9d66-16fb27c60e86 | -3.57137 | -54.38065 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 9b644627-0885-3240-a929-5200b7cd2d5f | -3.36599 | -50.48396 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9353e81a-707d-3f1b-b888-1dc67e1ee345 | -3.26542 | -50.39077 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b4a1bcc-c402-3dbc-ae57-84c4696c2fd5 | -6.06141 | -44.6583 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c62ebafe-9da0-3f29-a0e0-d7a17b0e8b86 | -3.91225 | -59.59137 | 2026-10-10 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ce66bf12-fe04-36f5-ae90-673f39aabf38 | -3.16924 | -50.45607 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4947cbef-fcd2-346d-840e-4ece61e6c239 | -2.75632 | -54.10469 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd207ad4-b95d-3278-9746-1ec57038348f | -4.59048 | -55.71978 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 85f04b95-bb6e-3b37-b089-9b549eb30db1 | -4.24378 | -56.30796 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 45a077db-87e2-3e0f-b8f6-3aa166f8c8d1 | -5.88954 | -43.27396 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af122737-dde0-3ec3-a3ff-58570b5b2253 | -2.98556 | -54.17577 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c45c305b-cff5-37ee-be14-639ab260e0f8 | -4.59354 | -50.97332 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d1e81dad-bb7c-33e2-b962-861b12b3f883 | -5.60536 | -47.27703 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 526d2cbb-1a0a-31db-90e5-4cc5cd4ade1c | -3.29718 | -50.32858 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1b7aa8cf-7fa8-3775-a144-a588fe51e2ca | -5.7519 | -45.13031 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0ea71522-1b80-3c46-b238-50c790bb4b07 | -6.4338 | -43.50734 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 608b801d-047c-37da-93ff-054e4d9cf57d | -3.98014 | -59.35963 | 2026-10-10 04:44:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 162281d7-14ab-3f49-beae-a6810fe6197a | -3.06601 | -51.13113 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cc9e46fc-b512-3fc9-ae3c-2a8e2ae43ea8 | -2.57659 | -48.25346 | 2026-10-10 04:44:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 069f0189-fc7e-38f6-9e21-c6d40c68a9b8 | -3.861 | -44.04835 | 2026-10-10 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6b758491-31e9-3f77-9e49-10b68a9acca4 | -1.73851 | -52.24414 | 2026-10-10 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5bc73f84-4055-3536-9b96-65b0195bdcbb | -3.50588 | -49.94217 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9328ad2-784d-3b6e-b787-6bea0d946b45 | -5.71877 | -53.49051 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b32f8231-725f-3604-aa34-d0b463845f8a | 0.28934 | -51.4115 | 2026-10-10 04:44:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa03dba7-4be0-3186-9907-c5104afedb63 | -3.97869 | -52.1552 | 2026-10-10 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| abf9c69e-cd51-3a6c-96fd-920a66b7f572 | -3.48843 | -50.48973 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e7b90df4-eaba-309a-81ea-874a108d579a | -2.60812 | -56.48352 | 2026-10-10 04:44:00 | NPP-375D | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 184faff5-e20c-37b3-900f-6f49088d1720 | -1.26535 | -55.74888 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ac6ae1b-d220-3bc1-b50a-eca3bc6c2d09 | -4.19824 | -49.89989 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af0d7cef-a11d-380b-ae66-81e74dfab13e | -3.57333 | -54.69156 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8200fb94-be92-307e-b912-c3da91fdb2c5 | -2.2866 | -48.75459 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcf737d5-aa84-3a59-b6f7-0e85ff7df21c | -3.30851 | -53.70686 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 05a0175f-d18c-3115-b3ce-10e056441d3e | -3.10808 | -53.78489 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8a65679e-ba36-3991-95af-03e0bed03f69 | -7.1881 | -41.99566 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| d48619b5-c066-320e-8974-6361cbcd65dc | -5.58761 | -47.28136 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a3642b2-2120-301e-9d60-814a49bf9ab9 | -3.01259 | -54.04463 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 557e7e0e-77df-35c2-a265-5c7925d89b39 | -4.89328 | -49.05085 | 2026-10-10 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 26fcfe21-54cf-3c2f-838d-765aac7c883d | -3.57636 | -54.70292 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8155703-d910-30b1-a1d6-cf85f35ea840 | -3.22048 | -49.43028 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| c6b92e40-6252-3426-b63c-58d6fdb67201 | -0.8862 | -48.71381 | 2026-10-10 04:44:00 | NPP-375D | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 11eacbb8-2726-3010-96d7-836db842e82b | -5.55687 | -43.96446 | 2026-10-10 04:44:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc275183-1644-3a0d-a340-01b034314087 | -3.00688 | -51.01136 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5cc13b0-c349-3095-b7d3-923d1ceb3e7d | -2.52586 | -56.26921 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3721f556-45e2-3b94-b057-a70f366b9794 | -2.49812 | -56.06673 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| bfbd9b81-57ce-3c19-879b-cce5aa5d0ce3 | -1.99957 | -47.95124 | 2026-10-10 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 020d40e5-58b3-3dc2-9571-63f2efbe58f1 | -3.35495 | -50.4119 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b2f41ef2-500b-38a5-95ae-87b64960276c | -4.12453 | -46.86589 | 2026-10-10 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ee267e4e-6faa-3e9d-92f2-f3fc6e1c9128 | -3.54975 | -54.69139 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dfc449b5-e5ad-3e5f-814a-8211555c1c51 | -2.74615 | -54.10801 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 187d4b62-b5ab-3f92-8059-e20599b3e5d0 | -3.11438 | -54.16325 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e2e92e78-4ad8-3b2a-9489-357d51c7cf0a | -4.12105 | -54.02975 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9730df57-0345-3baf-b77b-db8a19415010 | -6.51914 | -43.38706 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 93024d07-0570-3cf9-8aba-3898ad6f9413 | -3.30202 | -54.00001 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b5d302c7-1442-3bc3-935c-9898e381476e | -5.87967 | -43.5573 | 2026-10-10 04:44:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 003c837e-ebff-35c9-a2c8-ff5407a14c6b | -3.5753 | -54.38619 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 7f9ce290-23d8-35f5-8639-969ab5778caa | -2.51526 | -56.1638 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1613a0fc-6f24-3639-b51d-fd86b9751867 | -3.59307 | -54.60409 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 1b4aebd4-d2a1-388d-8970-6c42e41cdd15 | -3.83696 | -55.79224 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69a8ddaf-c709-3c72-9533-8ee614b19fe2 | -1.95574 | -54.40163 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6b4e943f-6994-30b3-a689-4c6e67627035 | -5.30222 | -55.98695 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 239bc6cb-9c3d-3cac-b9ab-286d3ae59920 | -3.19924 | -53.85484 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b5d6e646-1e50-3ebb-86d6-d949cda8c82e | 0.48518 | -50.78473 | 2026-10-10 04:44:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a577a131-9219-3b05-90e6-9480e3256d45 | -5.8935 | -43.41034 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 216cb5de-f518-30c0-91db-f005b88eb41d | -3.88314 | -55.99125 | 2026-10-10 04:44:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1afb8226-b703-3242-874c-2fdb32c65f2a | -4.60956 | -49.20667 | 2026-10-10 04:44:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e01ea87a-c5fe-3cf0-b17d-b5e3cf2206c5 | -2.47063 | -56.06565 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f9a37b4-71ac-344a-874c-54aca30c8e66 | -4.82773 | -56.08508 | 2026-10-10 04:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 396e811a-72f1-3003-9469-8c1c89761121 | -4.15687 | -54.33956 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac7e3ef3-3228-385b-979f-3bcd149795b8 | -3.22072 | -50.55141 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6bebca60-cdf9-3dfd-b932-1f06f9bdc164 | -2.52643 | -56.26572 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bc79633c-400a-3221-b4f1-4c33dfeb2cb6 | -4.09394 | -53.99636 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9568b956-baf9-33e3-b4aa-cb6018954be6 | -3.25168 | -50.40606 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 872960fa-fcbb-319c-ae4f-ae4e69f78d7c | -6.53877 | -44.27866 | 2026-10-10 04:44:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21927638-c767-3f16-8f72-173babec6551 | -3.30507 | -54.01026 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1aade658-0553-3868-bb9d-0410b72f735b | -3.31353 | -54.67009 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README63.md)
