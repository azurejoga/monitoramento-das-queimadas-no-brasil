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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5e5cba92-1b7f-356e-8959-b61a8988028d | -6.45451 | -43.94741 | 2025-09-08 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 14b47887-a135-3705-9bb9-7b88041f31e8 | -7.22482 | -46.20253 | 2025-09-08 00:52:00 | TERRA_M-M | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 92f31ce2-3674-3b11-aa4b-67e61336b016 | -9.32728 | -55.19298 | 2025-09-08 00:52:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| bb48d7bc-711f-3273-bf87-a0ba28e57a14 | -3.22895 | -52.23 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a631c554-5e77-35c5-9bea-2bf2c057234d | -6.86989 | -47.91256 | 2025-09-08 00:52:00 | TERRA_M-M | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 7ba4b986-b65b-3db3-b777-22c07c332b41 | -5.6085 | -48.09162 | 2025-09-08 00:52:00 | TERRA_M-M | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| bce05234-a5ff-3853-a317-57a0a3fe1922 | -6.20122 | -43.60948 | 2025-09-08 00:52:00 | TERRA_M-M | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 33.7 |
| e6190054-7dc1-3707-8dfb-91a3390bd64b | -4.27534 | -48.19439 | 2025-09-08 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 28.8 |
| deebf524-ef9c-3c82-b9eb-3b749b3bae60 | -6.64221 | -53.36689 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| f703936e-2bc6-34f2-960f-af6ccde36b47 | -7.65609 | -47.94198 | 2025-09-08 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 7e68fa02-256e-3714-8227-ddbd64ea5da2 | -6.80581 | -52.8127 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b4c85c09-5c10-353e-9da0-5f77d45695c2 | -7.67189 | -50.28694 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ca089778-ff7f-3014-b9e1-3cd26c129683 | -8.09435 | -54.76337 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 2a3cc43c-5f3d-301f-8b07-fc0ad7da8aec | -9.45446 | -61.83748 | 2025-09-08 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 6cf3192e-64a4-35c6-bddc-3d895578fcaa | -8.09306 | -54.75369 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 4e0c0897-52c0-3a88-b3f2-4fe72ef4bde9 | -8.06607 | -52.33775 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e59a4a0c-5883-39cb-8019-fd284c1745d6 | -10.04757 | -59.34529 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 9be643a3-8125-3af9-bec5-a8e36a2260ed | -9.47842 | -60.48581 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.3 |
| e251a136-46e4-3401-a179-a412fac81350 | -6.46802 | -43.9734 | 2025-09-08 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 283b1946-8254-3292-8f52-f760e33e18d9 | -7.08718 | -43.90028 | 2025-09-08 00:52:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 34.9 |
| 3f5b2346-42e5-3990-af05-3be2ad3729fe | -9.44565 | -61.84381 | 2025-09-08 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 87.8 |
| e78f7b90-73bd-332b-a52b-0687a9b52b46 | -6.8134 | -52.8026 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5fb61aa-2cf8-308d-95d7-bc615e574a9d | -6.64343 | -53.3757 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 61544854-23c4-314a-9198-41ffa05413ae | -8.38958 | -52.54481 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 0cd57eec-1fec-3693-a93a-ad9017e6dda3 | -6.8411 | -52.80764 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ac7a78b2-2fd1-364c-a963-2d01bc81ecc5 | -8.19512 | -50.14891 | 2025-09-08 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| ecec7daa-dcfc-3a8c-98ef-1abf1fd29729 | -8.06483 | -52.32885 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 96265e8f-afc1-3075-b03b-8d8a8a5b5010 | -7.39956 | -61.61171 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 805773b8-1f32-356b-9d3d-2a3fadb8c232 | -9.46748 | -56.04816 | 2025-09-08 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c293db7e-226d-3090-a079-206c67a7950f | -8.04329 | -52.36835 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 258aa4a8-3c4a-3e76-96f2-5d30a0e20911 | -6.6334 | -53.36813 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7a92ac38-3a59-3acc-8923-dfeeb8ecc3bd | -7.4031 | -61.64137 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 278.7 |
| 5326b8f1-e22e-3aea-b36f-17a829af47fb | -3.544 | -49.37925 | 2025-09-08 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1cf1827e-6259-3399-b6aa-a8e8f2098506 | -6.35039 | -55.55894 | 2025-09-08 00:52:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.8 |
| 75cd8099-431b-319b-bf42-3dc268dcf570 | -4.99045 | -56.25438 | 2025-09-08 00:52:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| 167be110-236f-3ca2-b347-c4c151f289de | -6.83105 | -52.80008 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 3f6c3dd4-b796-398d-a007-e711269cf759 | -6.62216 | -53.35175 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| a35d5798-d83f-3941-8fdb-01c441e80517 | -8.08514 | -54.76469 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| a6632edc-e6ad-3428-91bb-f27c993c3eb4 | -4.27277 | -48.17751 | 2025-09-08 00:52:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| b110e92d-4b39-3943-80df-c0d35641b632 | -4.53229 | -54.84356 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0714d863-e011-3e4f-acbe-11b4ed9508b4 | -7.38702 | -61.61838 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 18.2 |
| 3e316dae-9c69-30c7-b855-fef239681e6a | -8.19361 | -50.13856 | 2025-09-08 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| af15a954-19ae-35f2-bc9e-dc7a291fafb8 | -6.62581 | -53.3782 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 1da4b6c4-c07d-3b1f-b12a-76817042d197 | -7.67353 | -50.29815 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 48fa2d2e-898b-3784-a8ea-28859fa45fa8 | -6.27268 | -53.42569 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2aba54ef-58ad-3402-a6d4-6617d582dfd2 | -9.17633 | -59.37859 | 2025-09-08 00:52:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 44d823b9-f12f-38cd-aa51-33991dd14ded | -6.82222 | -52.80134 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 1cf16795-881e-3797-97da-39ce62d8e3b8 | -6.83987 | -52.79879 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ecaffc5f-9d8f-3184-bc6d-6dda6ec10f1b | -8.60134 | -54.69295 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f1db0d95-9909-3fa9-a3a4-b919e438d98f | -6.55078 | -54.99166 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 78d8b57f-1431-3ba6-b37c-176b5105efe4 | -6.84726 | -52.85188 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e20910f9-160b-3e84-b283-1cfbc0d9087d | -8.04455 | -52.3773 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a4a5e043-0d2a-31c5-827a-8cc64ebe3ee9 | -3.63237 | -49.2005 | 2025-09-08 00:52:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| e1165e96-48fa-3e1b-b8a4-c697d4e68b92 | -6.81464 | -52.81145 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 75f0029e-68cf-31d4-8b97-6e5f954ae296 | -6.20962 | -51.46188 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 21.5 |
| d7d17218-7ab8-35f8-a06e-41d264fb9713 | -7.39074 | -61.64796 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 77e301af-01f0-3758-a669-c706c91f8b74 | -7.73861 | -50.3145 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 0287af68-394e-34fc-9886-bb5071cf478a | -9.05236 | -50.46559 | 2025-09-08 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d32e97d8-e7d9-3c6e-937f-9a95504900af | -8.50782 | -51.35128 | 2025-09-08 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| a39c5dc3-7846-36f4-ae13-9f11f5c00bf4 | -7.42994 | -49.26884 | 2025-09-08 00:52:00 | TERRA_M-M | PAU D'ARCO | TOCANTINS | Brasil | 1716307 | 17 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 8fbe39ea-0335-3c46-805d-d9e799c1770a | -7.6585 | -47.9575 | 2025-09-08 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 18.8 |
| 5c8e4ad9-659d-3cd5-89ae-50e6d50312c3 | -10.05988 | -59.35986 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| ac466434-a00c-377e-8735-a3462e1d1aed | -6.47064 | -43.94534 | 2025-09-08 00:52:00 | TERRA_M-M | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 137a9bfa-27bc-3913-9770-f2a27bd04cb3 | -6.63218 | -53.35932 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 1f88aaf4-6a74-3372-ae97-7a90a7a3ce9d | -6.62094 | -53.34294 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 4fed6195-fd65-3eed-9f4a-fea4429c0cd0 | -3.92394 | -56.06704 | 2025-09-08 00:52:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f6284c89-0b47-3a35-bc8b-4c17815376c8 | -6.27146 | -53.41688 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 4de13c4c-1e69-347a-86c1-15bf15c7a7dc | -6.62459 | -53.36938 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| dcd42854-7ca5-3009-a3a2-6069250569d0 | -7.40226 | -61.61657 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 147.5 |
| 4c9948b7-6186-3f41-b979-128c3a99a044 | -7.40665 | -61.67112 | 2025-09-08 00:52:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| 3c03eff3-603a-364f-b576-4aa7e2e97be1 | -6.20825 | -51.45219 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 0a0fd0b2-7e03-3b87-8fc9-d2f0006c8407 | -7.78649 | -52.12159 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 8cb09889-ec67-31bd-98dc-bfe1530301de | -6.63462 | -53.37695 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| dcb56969-328b-3c2b-a8d4-3f3cb29a55c4 | -10.06247 | -59.38169 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 39a2f56f-6dfb-3415-96b0-2f87d6ba1f32 | -8.34672 | -52.56 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5551d599-1bd6-397a-a567-104b3f16da61 | -9.4815 | -60.51181 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 41.6 |
| fe1b5646-f642-31d5-8b4f-10e72fe0002f | -6.22165 | -49.41553 | 2025-09-08 00:52:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 0930882b-0a9b-3045-97d5-8a1ec3e7df6b | -3.87012 | -50.76979 | 2025-09-08 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7cf2942d-8d49-393e-9bb1-a3d17630ffca | -8.1422 | -48.48562 | 2025-09-08 00:52:00 | TERRA_M-M | COLINAS DO TOCANTINS | TOCANTINS | Brasil | 1705508 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e7721635-0d57-35e2-810e-aa82744425b9 | -8.88451 | -52.06312 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 0957b0ed-4075-30ae-9edc-0d342d70937a | -9.4416 | -61.81047 | 2025-09-08 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 98.1 |
| 7c4ffdaf-7686-37fa-a248-984b35b37b6d | -8.18547 | -50.15032 | 2025-09-08 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0312f54d-ba9f-368e-9b4e-7e0c048a9f44 | -9.45061 | -61.80407 | 2025-09-08 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 48.1 |
| f3d46f79-647b-3591-a5a7-1d162b946dfb | -6.22353 | -49.42813 | 2025-09-08 00:52:00 | TERRA_M-M | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 6c0a2e69-b41e-3051-8989-1a39de61a9a2 | -7.65851 | -47.94828 | 2025-09-08 00:52:00 | TERRA_M-M | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 73d590c9-d5b8-36b0-9354-ee619f43a2f7 | -6.5416 | -54.99291 | 2025-09-08 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| da0d5add-681c-34f0-9899-986f5937bc47 | -3.84053 | -49.28843 | 2025-09-08 00:52:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 34241c22-1af7-3e8d-acc7-24814fa85817 | -8.34549 | -52.55117 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1b1dd966-c15e-3330-899a-f798f870ad1c | -7.78792 | -50.75693 | 2025-09-08 00:52:00 | TERRA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 055c5760-e205-3f33-a28a-e0d983e1e7e8 | -9.0617 | -50.46395 | 2025-09-08 00:52:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| b5113448-ed19-3c61-96cb-1b653eb06fd4 | -8.20476 | -50.14735 | 2025-09-08 00:52:00 | TERRA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| edac9bd8-ab74-3e31-a2fb-12da0732c4a9 | -6.82346 | -52.81017 | 2025-09-08 00:52:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 1c07700f-0d68-38c8-aaef-1164a0db0b87 | -9.85505 | -56.04539 | 2025-09-08 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 98e7721a-2615-37b0-bc09-a1763042d19d | -6.5326 | -49.50429 | 2025-09-08 00:52:00 | TERRA_M-M | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 20f9077b-0727-369c-9070-a16ec3c73c9a | -9.45736 | -56.04943 | 2025-09-08 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 90a3d6af-e3a4-35c2-b7bd-b1c6fbff5dc7 | -9.24121 | -57.06636 | 2025-09-08 00:52:00 | TERRA_M-M | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| bc9fe1a3-a205-3d70-8cdc-3854eeb4a710 | -10.05025 | -59.36667 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 146.2 |
| 2121917e-4eeb-3d14-ac2f-6c4066ccdaea | -9.84488 | -56.04673 | 2025-09-08 00:52:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c896b03b-a67d-3fac-949e-15037ecc42c2 | -9.43848 | -61.83934 | 2025-09-08 00:52:00 | TERRA_M-M | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 0f52051f-405f-385a-9d01-13f9a8b173e5 | -10.04663 | -59.36162 | 2025-09-08 00:52:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.8 |


[Clique aqui para ver as próximas entradas](README13.md)
