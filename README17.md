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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e0ff39d-e7fd-35bf-a231-61986d273555 | -3.61513 | -44.02187 | 2024-11-01 04:06:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 62f2e26e-3268-3596-b8f3-e45f0b9e90d5 | -6.25105 | -43.56767 | 2024-11-01 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 73d77c1e-b11c-3a96-a5c1-ebde5c3eb153 | -6.11753 | -43.96394 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a1a1a461-ff1b-3f19-a86f-7b3dfe5167d8 | -6.11528 | -43.9555 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e9748c83-3cf5-3055-8945-e1cc4152021a | -6.11464 | -43.95941 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 7fb6c95c-2f7c-3ba9-a338-4ffbf8b07634 | -6.11336 | -43.9673 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c3cba22d-0f7b-30be-acb1-74efdc499f45 | -6.11112 | -43.95882 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 343ab3f9-d71c-32b7-8810-c73bf8585ca2 | -6.10823 | -43.95433 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7b3d1c78-85f3-3bb9-a8a5-44e8dc6c9259 | -6.10342 | -43.96162 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a3d9d9e0-e717-314f-b37d-26f1b826ea0f | -5.07364 | -44.23299 | 2024-11-01 04:06:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3f570310-3ad2-3809-bbe7-dd3b6cd6fe11 | -5.07002 | -44.23242 | 2024-11-01 04:06:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f5c5c45f-3ee7-309b-902f-d448040f83b7 | -6.53395 | -43.95531 | 2024-11-01 04:06:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 46b38e80-94d4-3e7f-b313-c9c6c5658046 | -6.25042 | -43.57154 | 2024-11-01 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c0c0180-782d-3546-bff2-2caf3013b4a3 | -6.24758 | -43.56717 | 2024-11-01 04:06:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebaa9302-a2ec-3440-a961-1e0894d7ec88 | -6.11689 | -43.96789 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 17408504-df6b-3ec2-a99b-f87cc5616f5b | -6.11272 | -43.97128 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 450dc28a-7304-38d2-9e26-3422efb48a1f | -6.10695 | -43.96218 | 2024-11-01 04:06:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3cf0eb22-1038-37fe-a485-df97d85edd72 | -5.57334 | -43.57713 | 2024-11-01 04:06:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f18777d3-75ce-3794-802d-0aacef425d7d | -6.15073 | -44.749 | 2024-11-01 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48cbd58c-480b-3398-804e-271238f1ed03 | -6.14927 | -44.75126 | 2024-11-01 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0167f5b9-c807-3251-b8a0-896e6c646a40 | -6.05848 | -44.69545 | 2024-11-01 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 01571efd-4177-3ad8-a3bc-8d907048d99a | -6.05818 | -44.69446 | 2024-11-01 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e780a57-847a-3a43-8e08-8bb328179db1 | -5.53206 | -44.83007 | 2024-11-01 04:06:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1359655-45e1-3215-9f9d-9c7e060b9948 | -7.16982 | -44.72415 | 2024-11-01 04:06:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 470e8321-1a1d-3088-9dc1-0a0318a1cbd9 | -6.87901 | -44.7652 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7359570b-57b8-3cdb-a27e-281a21dce25c | -6.87607 | -44.76036 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 07e646dc-7be7-3758-80ea-e1338daea2eb | -6.87538 | -44.76461 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| db498e44-479b-35e8-bb2b-bd1b8d09711e | -6.87313 | -44.75552 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| abf199bc-32c3-39c3-8e1b-effa6ef67d89 | -6.87244 | -44.75976 | 2024-11-01 04:06:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6e463fbb-dae3-3233-99bc-ba2b7eb480b6 | -6.53745 | -44.46151 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| eb711287-b0ed-3f78-b0d9-c48e3f3a2616 | -6.53677 | -44.4656 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7891b50e-85d1-3691-9962-4539d82ebedb | -6.53386 | -44.46089 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bdc213a7-dab7-35f5-91c3-550301f0af36 | -6.53319 | -44.46497 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f9dc1c3-c3bd-3a2b-af16-55de0d47b78d | -6.53251 | -44.46905 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4abe747c-36aa-32e8-b03b-b30da6908ce6 | -6.5296 | -44.46434 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee47398f-392a-3c79-8285-0ac895f7db74 | -6.52892 | -44.46841 | 2024-11-01 04:06:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b391462a-f79f-3c41-962e-49d1d1fda8a8 | -6.52806 | -44.46468 | 2024-11-01 04:06:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be3bb3b9-9456-3cc7-b655-3ff13ee0c3e1 | -1.99159 | -45.61056 | 2024-11-01 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9039194e-c5bd-3b4c-ad98-691e5c343458 | -1.98693 | -45.61349 | 2024-11-01 04:06:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d1e4d5e6-f3ae-393b-833f-38d392dfe2c9 | -3.46726 | -44.9373 | 2024-11-01 04:06:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e237c8-f1bf-3a67-935e-11fe9b6625ae | -3.37481 | -45.91177 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0c860e8-28f3-3cc6-bce8-69faf7dd49f2 | -3.37246 | -45.90835 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d62d666b-931f-30ca-b686-a924f8f2de07 | -3.37188 | -45.91197 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b3bb4ccc-743a-3054-b009-f5b769869b0c | -3.37072 | -45.91114 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d5914418-b693-3a8d-9b45-860c7aacea27 | -3.27861 | -45.71384 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 001722d8-dca4-3f55-a8a6-bf82e2acf561 | -3.27457 | -45.71318 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 09e386d9-0138-3090-adb5-95c5d1b43599 | -3.27024 | -45.79246 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cedf4b5d-cfca-3f5e-94a1-8226a622ee16 | -3.26281 | -44.55424 | 2024-11-01 04:06:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 794df2df-8e3c-3d07-84ce-1d8a983382f0 | -3.26212 | -44.55635 | 2024-11-01 04:06:00 | NPP-375D | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b25e3367-6af2-3db2-ab0e-46151fbcd1b0 | -3.25438 | -45.97148 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57a39531-a26c-31ca-a67b-7993662ba772 | -3.25298 | -45.97082 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e715e846-4c4b-3413-abd0-2dc9c9f38d85 | -3.16198 | -45.31269 | 2024-11-01 04:06:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6864a48a-156d-3a2a-ae74-514f6a4723f0 | -3.14116 | -45.66669 | 2024-11-01 04:06:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a3439b3e-a38c-3687-baa3-01f19c12a824 | -3.12251 | -45.11165 | 2024-11-01 04:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9cceb629-1f0b-365d-be83-8299560516f7 | -3.11862 | -45.11101 | 2024-11-01 04:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2d7c3546-15b6-345f-8f9b-3ee6780f21d6 | -3.11666 | -45.29837 | 2024-11-01 04:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9e0c915-753a-3227-98d7-74271e05377d | -3.11272 | -45.29773 | 2024-11-01 04:06:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9fe02a6c-73ff-3e36-a2d4-b81075d83c83 | -3.09443 | -45.56617 | 2024-11-01 04:06:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 382307fb-4d2a-3611-b2a0-44fb2d2a8140 | -2.6258 | -45.14212 | 2024-11-01 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7d36aee-9474-313c-83c7-db305c26c2f7 | -2.6244 | -45.14436 | 2024-11-01 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fb19f25c-9fa2-3a1d-a465-76157d1e0efa | -2.62109 | -45.14644 | 2024-11-01 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78676ed8-8ae5-394e-be2b-224e60ec8e20 | -2.62047 | -45.14371 | 2024-11-01 04:06:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b4f1128-fd8b-3b63-9a24-93d091ac7459 | -2.57091 | -45.33506 | 2024-11-01 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e0babb1-af98-381b-8427-61aa6069cedb | -2.56693 | -45.33441 | 2024-11-01 04:06:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 42299116-d067-3041-8e60-8956c2335080 | -5.05517 | -45.53452 | 2024-11-01 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fb1cb47-2af2-3afb-af3f-a9b0e0cd9bda | -5.05146 | -45.53606 | 2024-11-01 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 003c80b9-4ba9-371a-a70d-87b4313204a8 | -5.05128 | -45.5339 | 2024-11-01 04:06:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 75a5b1ec-e5a6-3461-871d-3712bd4721c9 | -5.01123 | -45.83392 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd00e701-048f-3de6-a005-6b34bfbf9e16 | -5.0104 | -45.83912 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f866a0ed-88ad-3577-b1d0-e6e50e946094 | -5.00935 | -45.83553 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d63f349-d834-3d24-9c29-128e4c0d594b | -4.94384 | -45.62708 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 626fa09e-3630-32d0-b774-4a4f3c0ade5c | -4.94238 | -45.70864 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3bfed361-07f2-3603-853f-db4581a00d6d | -4.9393 | -45.70286 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2a4c59f-9c1e-3528-a528-77ccdd04f6a5 | -4.93538 | -45.7021 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab37be53-78bb-3be4-8b15-da97a9ea07c8 | -4.80987 | -45.66682 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c216a42b-937e-3a18-aadf-20b5cf14e629 | -4.80956 | -45.66378 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 371f27a0-8565-379d-be91-0460443cda07 | -4.80908 | -45.67173 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e174431a-dd2e-306a-b0ea-5fa2b4a6e0f0 | -4.80873 | -45.66869 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9716981d-008f-3c93-a534-818fd718b4d5 | -4.80791 | -45.67359 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74d61108-2057-3c28-a7b7-64cd0d5c78ef | -4.79623 | -45.74317 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b69bb63a-1e1c-37dd-9bf5-8b60c70b856c | -4.78277 | -45.56059 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 40190cee-4a4d-3a40-9775-de7f0a340557 | -4.76856 | -45.84758 | 2024-11-01 04:06:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c8eb867f-a282-33c6-bb2b-fbac62ae6876 | -4.75272 | -45.35596 | 2024-11-01 04:06:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| df3989ff-1d8a-3cfd-a178-d25710111b2e | -4.75226 | -45.35395 | 2024-11-01 04:06:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 50d7bccf-0c58-30be-a9f2-b4aae93c0a8a | -4.73334 | -45.6895 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d057f95e-b338-3b15-af42-9266eddd86cb | -4.73198 | -45.74692 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 94657948-9eb3-3105-a0c2-a3a9df7f602c | -4.73112 | -45.75214 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 3bc08ad1-6d55-3217-8714-7e2896803adf | -4.72941 | -45.68879 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f61c05a6-48bf-31d5-b8cb-614429bebe3b | -4.72802 | -45.74627 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a2a9a3c3-4e42-3f87-8053-4efdc73b59d5 | -4.72715 | -45.75151 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e7188dc2-bf8a-3043-909c-d880d30f2775 | -4.68449 | -45.81186 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a59d0d62-a6ab-3b58-aece-a334a23c9925 | -4.63913 | -45.36566 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c7a8129-66f1-38be-8010-fca33e24cd19 | -4.63853 | -45.36333 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 27ff7594-3cf5-3e72-bce9-e4f701440091 | -4.63774 | -45.36829 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73f3d76d-47d5-3bf7-bb98-901e417ce8cb | -4.63117 | -45.63037 | 2024-11-01 04:06:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e2922aa-ead1-36fa-8d99-79eeebe68b94 | -4.54183 | -45.71236 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b2925bec-fb0a-31df-8bc1-21e56ddc3571 | -4.541 | -45.71744 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1a037e58-affe-3a4e-9480-403e756e6c99 | -4.53789 | -45.71158 | 2024-11-01 04:06:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a9237e04-c850-3cd9-b78f-c988db52058d | -4.50903 | -46.04006 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e2c997b0-3fef-3fb0-9418-5421466a1c26 | -4.505 | -46.03932 | 2024-11-01 04:06:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |


[Clique aqui para ver as próximas entradas](README18.md)
