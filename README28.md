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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 530a5b52-e9f2-319d-a0c7-4dfbe3e3cbd2 | -5.50814 | -46.1156 | 2024-10-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 572ba54d-2ef8-37a1-aa65-9d7eefd5ac0a | -5.38957 | -46.15657 | 2024-10-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cc4e940-a0f7-36a3-8491-1f5666b7b5b1 | -5.34899 | -46.1391 | 2024-10-24 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6f7a372-a8ee-3666-b59c-5b5cc4a1470c | -5.32518 | -45.93565 | 2024-10-24 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 48b91598-74fc-3eda-8fdf-3bfd42bbd769 | -5.32401 | -45.92068 | 2024-10-24 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d121098-b165-3968-ab2e-f0e3c5040105 | -5.25824 | -45.88861 | 2024-10-24 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 618fdd87-70e1-3c2b-bb0c-91051771350a | -5.23306 | -46.16215 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54dfa005-e55d-30ba-bafa-9e3ceb57a377 | -5.22859 | -46.16877 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5dce8bfc-69fd-3578-8183-021d1e50cd1d | -5.22523 | -46.16825 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 1aabf2cc-c5a2-3023-91de-fc8df18d8416 | -5.22468 | -46.17181 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 567cc257-1b72-3ea3-9485-08c5b116bc63 | -5.22299 | -46.16059 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2299f01b-f545-37b2-a4f3-ffb18474d2b8 | -5.22243 | -46.16416 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 40125b8f-821b-3093-9d65-a6e3b215e6a9 | -5.22188 | -46.16773 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac3c1a8e-4af4-30cf-aa91-ef449a939a3d | -5.21426 | -45.92669 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f7e065d5-c760-35f9-b910-8071b8b91b69 | -5.2137 | -45.93032 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4093e35c-4f98-363a-8b8e-d459f4cd58db | -5.21314 | -45.93394 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d568d043-708f-3fdc-a575-99831eb5a7b6 | -5.21032 | -45.92982 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8aeab4f-3ca0-3a08-9fa0-680e979e86f7 | -5.19344 | -46.21813 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b0d0d8b-ed52-3bce-8a4a-7afd56968e77 | -5.17436 | -46.18592 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1c8966e-0714-323c-ad7c-828f02f87be3 | -5.04961 | -45.94245 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b818584-57bd-365f-bb14-a97997fc71f4 | -5.04225 | -45.81115 | 2024-10-24 04:32:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 50d3831f-7f99-3282-a1d7-6da1ddcb94e1 | -5.14497 | -45.25914 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e66a0913-816a-3127-81f7-f41a4dc8155c | -5.1421 | -45.2548 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a843d2cc-cf93-3198-a7ea-9b13afa014d6 | -5.14151 | -45.25863 | 2024-10-24 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5349655-b5ca-3839-bb79-2ca22f88b195 | -5.12562 | -45.40729 | 2024-10-24 04:32:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9b146914-7621-35d5-9ae3-0be68659663d | -2.14017 | -45.81802 | 2024-10-24 04:32:00 | NOAA-21 | GOVERNADOR NUNES FREIRE | MARANHÃO | Brasil | 2104677 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07ade37f-103b-34d9-8736-a145097ee7e3 | -2.05016 | -46.34764 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f36228-edc1-3f0a-938f-5fd8db88f56c | -1.94797 | -46.54645 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7ed0929e-96c4-3b03-be28-52a2525a2197 | -1.94467 | -46.54594 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| dd26b9b7-50cc-365c-aee4-4ee25885c7b4 | -1.94414 | -46.54937 | 2024-10-24 04:32:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6004b313-4c6f-3ab0-b0f6-edfc8ae12d21 | -2.12614 | -46.7994 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 24027271-a664-331d-87af-ad00dcb7a6ce | -3.06135 | -47.38612 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49baa22b-bbd8-34f3-8ee8-8ab1fa11a612 | -3.05859 | -47.38217 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8d34fd71-af75-3485-8269-7f935770c30a | -2.55377 | -47.30199 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbc1e73e-098b-3ec4-8a38-dbbc60373609 | -2.54253 | -47.2229 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 04827005-8eaf-3b46-b58a-0faf330a8d9b | -2.54199 | -47.22633 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd2d257-7d42-3363-bc0e-4520c1e6a982 | -2.5231 | -47.34651 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 42155e01-cf0c-3f11-9df5-73748eb93b67 | -2.52256 | -47.34995 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f95ed2dc-c495-3c22-892c-736c84b56bc7 | -2.52202 | -47.35339 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef50f157-a5e5-3426-90ab-b3912346fdce | -2.5198 | -47.346 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a5375e17-6eb6-349e-a1b6-7bd89bf9edd4 | -2.51872 | -47.35287 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c8a00aa-e891-3e85-a260-6a4187131e21 | -2.51595 | -47.34892 | 2024-10-24 04:32:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf9ced7d-0eac-367a-bda0-5f3a7ebd1181 | -2.2657 | -46.77561 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a047e084-4156-35ab-a7b0-e2c0daef1a58 | -2.26516 | -46.77904 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7b93e315-c2be-3045-bdc3-3b550df6c37b | -2.26248 | -46.79616 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c04e141f-e534-37ea-86dd-97ee28e48b59 | -2.26194 | -46.79959 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f1efa4d-21c6-3167-86e6-659998958ff6 | -2.26187 | -46.77853 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5500dbdc-4fe4-3396-ad93-ab6e747364c9 | -2.25972 | -46.79222 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 142e34a5-dcec-339e-b7a0-be540df6df41 | -2.25918 | -46.79565 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd76e31b-92f1-31b8-869f-b1354735a603 | -2.25857 | -46.77802 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d588d7c6-bfcb-394a-b1c2-c3a1b59badd6 | -2.25803 | -46.78144 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9062032e-0b1b-3e67-9b7f-ff2c64f00b31 | -2.25473 | -46.78093 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e74d1dd-1cbe-350a-9aa5-39727024453f | -2.25251 | -46.77357 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| baa3f6a5-1ebf-3b47-b565-3552db594bbc | -2.25144 | -46.78042 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0dc1e91c-cc35-37de-bfbc-d3c4b7241195 | -2.2509 | -46.78384 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cf210620-f41c-3a12-abed-4df8766250c5 | -2.25036 | -46.78727 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80401f69-913d-3200-9518-8359cf616af3 | -2.24868 | -46.77648 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0db13fd5-d3b1-3ec8-9f3d-0836588bd448 | -2.24814 | -46.77991 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59ba680f-5e28-32fb-9bc8-d064cd07ba50 | -2.2476 | -46.78334 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7f8e9675-4c2a-3b35-a51e-0a76122f72ab | -2.24323 | -46.78967 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0c639c67-07f8-3ab0-8cd9-d06868bfe194 | -2.23717 | -46.78523 | 2024-10-24 04:32:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 54c526e0-92cf-3919-8b4f-51a934792a52 | -3.32037 | -47.01612 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1d594787-ff55-331a-99cf-73c2e22d66e3 | -3.31707 | -47.01561 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74a2c803-5bf4-3394-9427-5f43029739cb | -3.23345 | -46.50524 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bfdcd26-91f4-31a5-a37d-a495be6bb32c | -3.2225 | -46.53183 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89b4e0b-eb1a-3431-816f-4b312ca4318f | -3.2192 | -46.53132 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 962fd408-40f2-313f-99fd-646a3160794e | -3.21859 | -46.51354 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a799e0a0-97bd-3919-bf98-9d6825b2ea20 | -3.21589 | -46.5308 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f8248c34-7e7d-3010-a8b5-ca697341dd5c | -3.18652 | -46.48027 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a967120-ccf1-36f8-8645-268e7ecec394 | -3.18321 | -46.47976 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65365fce-7c63-3053-81f3-ad9eead4c34b | -3.18267 | -46.4832 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 22e9deea-a0e7-379c-8fc1-ccba3f240e45 | -3.10224 | -46.62608 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be97d0fd-adf2-30bb-b976-72b5a65bbcec | -3.03649 | -46.87274 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a841816-37c1-3929-a0f3-3e6ec22c2753 | -2.93768 | -46.78657 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f81757c8-3263-3554-bd89-7e89abf2de5d | -2.93714 | -46.79 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc22c1d3-1523-3851-acc3-e2dcf2ca171e | -2.81557 | -46.63388 | 2024-10-24 04:32:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8e4e718-7224-3f57-868d-beaab4c5ed10 | -2.77583 | -45.97412 | 2024-10-24 04:32:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1571caf9-7699-3842-9657-4b0d00a2b6ad | -2.77195 | -45.97712 | 2024-10-24 04:32:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fed86a8-20d7-3dac-bd60-596227276ef0 | -2.7714 | -45.98062 | 2024-10-24 04:32:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ab0ae5a4-f441-31e0-b0b9-eb4da644a78e | -2.76862 | -45.9766 | 2024-10-24 04:32:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 461132a7-cca4-3eee-97a5-023598f2bb25 | -2.76807 | -45.98011 | 2024-10-24 04:32:00 | NOAA-21 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2889e6d4-41dc-36db-8f7d-c9f0588e8a0e | -2.63915 | -46.0856 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 39c64566-b5d9-3239-9759-bbb04fc38fea | -2.60882 | -46.12721 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4468f305-dc23-36e5-9955-0881b6cc7dc1 | -2.60827 | -46.13069 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 093b5b99-c2e9-39a4-9748-dda9bca6f1d6 | -2.60604 | -46.12321 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 932d2af6-8f74-3562-b7f0-f49325c7c225 | -2.6055 | -46.12669 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70d47538-cf77-340f-8c1e-7086f3d3ab2c | -2.60495 | -46.13018 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ef586934-3bb3-3b7a-817a-95846cade445 | -2.60441 | -46.13365 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aad75ff-2203-3502-bc0f-5048b5d6da6d | -2.60272 | -46.12269 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c12bfdc6-dc3b-321c-b40d-567adb593e90 | -2.59722 | -46.13611 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cda7dc01-1f27-3a02-a207-502347581e57 | -2.59668 | -46.13959 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8df386f9-a6c2-3956-be36-3901a0692947 | -2.59391 | -46.13559 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fac8cc92-30de-3515-8518-32d8c3dfa10d | -2.57677 | -46.1365 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c741953d-82fb-3404-a535-bf0bb172e4ff | -2.57623 | -46.13998 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d28457dc-fb17-34ac-a506-31e140e122bf | -2.57345 | -46.13599 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23fedde9-1f87-3d73-9a21-9118e7fc3ac0 | -2.57291 | -46.13946 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0306fa93-0648-32d1-942b-f67c6daa4b67 | -3.80689 | -47.49329 | 2024-10-24 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6eac7260-3910-3d10-ba27-3c588ee25f68 | -2.51379 | -46.19076 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 527e6bf5-273e-3da3-9680-f9f6f2e2f34f | -2.51325 | -46.19423 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 44f22227-9852-3cf5-b6bd-66ea2e2c0f14 | -2.64357 | -46.536 | 2024-10-24 04:32:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README29.md)
