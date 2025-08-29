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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd8b2483-ff26-3241-8925-cd69f1011061 | -12.82444 | -48.17085 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a62d3e4f-9134-31f0-82ec-f8b09708eb40 | -8.08163 | -45.01978 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 23438d87-f944-315d-95a7-bbfdd499663b | -12.8903 | -48.13765 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 149ac39f-b72d-3cf7-81a1-fa4f42c09552 | -6.33 | -42.51176 | 2025-08-29 04:40:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8c66e79d-5d7f-3b67-a3b3-401a7fe43b14 | -6.8759 | -43.61044 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6c1fd629-8f72-36a8-bfbb-996c2b43efce | -12.86012 | -48.12601 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 16c65230-10f7-33ca-959e-3601f1949353 | -12.86434 | -48.09731 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f82cf89-d16a-3d49-a500-ef7e6da3f501 | -6.33886 | -58.18497 | 2025-08-29 04:40:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8403fe86-4239-39e1-8aa5-1e71419bf209 | -11.941 | -46.70083 | 2025-08-29 04:40:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71f2cc4f-012f-3110-988f-aaf6df030667 | -6.2379 | -42.40105 | 2025-08-29 04:40:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 03432d50-8fe8-3936-913e-da423475e0ba | -7.15749 | -45.14316 | 2025-08-29 04:40:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c3f7b35a-0fab-3b20-a2a9-1fd414a1e490 | -9.46655 | -60.5683 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9966231-e447-3ee5-abdb-cdd3dec6ec23 | -12.70506 | -48.19542 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3f80451a-14a8-3591-927f-eed06e18afdb | -11.22376 | -55.06196 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19d544ae-7dd5-3ee0-8ecb-259fd5446fa1 | -7.39405 | -45.93547 | 2025-08-29 04:40:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d759978-9243-38cc-9593-a19fbc86e7e4 | -8.08111 | -45.02334 | 2025-08-29 04:40:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| da0966f0-5ad9-305c-9fd5-102a5a28213c | -7.63882 | -42.6632 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| ac034f53-1503-3e8f-8665-313169068d6e | -9.15784 | -59.58952 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f7d8526-7157-30b1-8795-d91c16cedcf5 | -6.41976 | -44.54316 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83075f36-7273-371a-a00d-050965cc38fa | -9.45452 | -60.56996 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 2f8e8ebb-c12d-32ca-b20e-4870154b011c | -13.18589 | -45.28298 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 65850de6-7bdd-33f6-a9e1-740043fa5d3d | -7.73308 | -50.28327 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef9a808e-d06c-367c-9ff6-b339e728fd8e | -9.51123 | -45.38278 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b21a339a-863b-3a2b-b7d1-ec4d39c88b1d | -11.37641 | -54.3462 | 2025-08-29 04:40:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abbace7c-09c3-3257-83a2-bc224e36d183 | -9.44107 | -48.24499 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf2ed5c9-1d39-391e-85b0-1e7b61cfa461 | -6.04748 | -44.47374 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 50239850-2080-3ad1-9ca4-5c187b000711 | -6.49175 | -43.5384 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f9d84b9-1835-3a08-b956-9cf58fbaca92 | -13.18907 | -45.29163 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0f0c3406-c9af-3226-a859-4907f9f36eb4 | -12.82973 | -48.1096 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6a23bfc7-c4d1-36ae-8571-8b1187536e79 | -10.95496 | -46.88771 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a33e5a2e-2afd-3efb-9445-4abcea41673a | -6.48494 | -44.09968 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6688d9d0-6d4d-39fa-a49a-254b697474f5 | -9.69303 | -47.05814 | 2025-08-29 04:40:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7b608d1c-5ceb-3bf4-a0fd-5fca8db595dd | -7.04593 | -44.38493 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f7dffbf2-e74b-314a-8f41-9611af7fde99 | -9.68965 | -48.31681 | 2025-08-29 04:40:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2d3f0143-b551-3d85-b136-6bb70fa91b38 | -11.08886 | -44.7464 | 2025-08-29 04:40:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5f5961f0-3a1f-36eb-9f10-15f3933a6d5b | -12.9153 | -48.11584 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 571a5905-8127-31c0-9e85-78306449b128 | -9.49378 | -45.39095 | 2025-08-29 04:40:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9832c5c5-cc51-3a1e-a64c-212bf0cda688 | -10.36754 | -57.82032 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ef114782-3146-341b-a4d3-d963019571c0 | -12.83806 | -48.10242 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c9f7deb5-2c01-3660-b7bd-342f21709c15 | -13.19013 | -45.28359 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0f69f8f2-f56f-3653-916c-6670fc265461 | -9.45185 | -60.55279 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2abb57a4-efc8-31bc-a3ad-ee048cc9cd0a | -12.82384 | -48.17492 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 733d50da-6284-3a83-a542-738903c86dc3 | -11.2284 | -55.05784 | 2025-08-29 04:40:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af6f28ee-f529-3fee-9cc6-3a8dc75f7f8a | -10.36667 | -57.82516 | 2025-08-29 04:40:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 05094740-ac32-3bfb-bd1c-2a357603c2e6 | -7.03873 | -44.37645 | 2025-08-29 04:40:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43bcc6b0-2440-3016-9fea-cadb1e88d249 | -12.8392 | -48.16929 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 26c5b8fe-aee9-3df6-95eb-8637cf9e45d7 | -6.54924 | -43.92759 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 7e1edf7c-fbf1-3db1-8446-e39648a6156b | -6.51504 | -44.84988 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 093e9ce0-fbe4-3644-bb18-e329b6d6c928 | -9.77666 | -64.26228 | 2025-08-29 04:40:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 096249cd-f07e-3a18-a98f-ae3b7d22e37d | -6.54198 | -44.09929 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5c6d0474-dcf8-3c9a-bfd3-b7dd1a7f9166 | -6.71355 | -43.14393 | 2025-08-29 04:40:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4b8086e-b2a5-30fa-bb40-f92e6eb7b747 | -7.81368 | -55.22399 | 2025-08-29 04:40:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 19ff5db9-55fb-33b8-8900-058c8827c03f | -7.79446 | -50.97126 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| efddf288-d221-3c15-afd6-7e5ad2fd02b1 | -10.85087 | -47.49994 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d30ed2ab-4a25-3ae9-8d39-e614c48cfc28 | -11.55609 | -46.36209 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 396739d2-347b-3cb7-8050-5f2cac0a7eef | -10.47431 | -57.96498 | 2025-08-29 04:40:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24d24acd-d1f0-3079-9c87-48fcb6d70062 | -6.97501 | -44.12359 | 2025-08-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 506f77cd-c71c-3c31-b653-1e1be3946164 | -9.16647 | -59.57266 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b3d1ad3-2ffb-3821-85d3-8e074151418a | -11.50462 | -41.52443 | 2025-08-29 04:40:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e49f1af3-7933-392c-bd3e-0f2b7bc8f73c | -12.08753 | -44.7253 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 91bdafd7-3254-3ae6-aad6-387d9459131f | -13.18642 | -45.27896 | 2025-08-29 04:40:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 8633c48c-5487-3f7f-857a-a044252a2807 | -11.59479 | -46.37906 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| daad515d-0b64-32da-b27f-964ce32a4fb1 | -12.70327 | -48.15785 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 876c9d5d-44ef-3126-bf39-90eda3233c68 | -10.97904 | -46.90483 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 9549747d-255a-3eac-bf3a-71a795b279ae | -6.70504 | -49.46459 | 2025-08-29 04:40:00 | NOAA-21 | SAPUCAIA | PARÁ | Brasil | 1507755 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 37877f1a-4980-3571-83ad-cd5e661e99b1 | -11.59159 | -46.37362 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eba2a145-1c93-3fd8-ba52-f0f43d6b0851 | -6.53668 | -44.10667 | 2025-08-29 04:40:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8244872a-bfe8-370c-a6de-8ae4b004e202 | -6.49025 | -44.40242 | 2025-08-29 04:40:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d7d0b61d-ed81-3c99-8d9f-e7f296ff6f44 | -6.87962 | -43.61522 | 2025-08-29 04:40:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 81468f5d-f8e9-3d13-8617-0e12958a902e | -7.65966 | -42.65055 | 2025-08-29 04:40:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 1b5c8489-94fc-333c-9f6a-ee1ad0026677 | -8.70127 | -50.3779 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 36725c46-6088-30f0-a4d0-f19058213898 | -12.93376 | -48.13932 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3f87eaf1-d843-3c6c-9977-c8184439cd4a | -8.55386 | -51.31176 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66fd13a1-b778-3232-942d-80beadf75dfe | -7.49647 | -45.04313 | 2025-08-29 04:40:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e2bde5c1-fa60-39b0-9a14-d7f2b343165a | -7.72375 | -50.29953 | 2025-08-29 04:40:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0c02a007-2350-3ebc-8908-e47082ae2fb9 | -9.23619 | -59.78046 | 2025-08-29 04:40:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4dceb975-72b9-3b60-821b-5788ba466a16 | -12.85121 | -48.13704 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1acc3f17-9737-342c-872b-3d1cab5c3a5a | -12.09618 | -44.72655 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.4 |
| dc426a13-1d14-3fc2-8d62-f517efe508d8 | -6.24836 | -44.43713 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1982cf16-f43e-33ac-88ca-089c36016fa8 | -12.90818 | -48.13992 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43942f04-d3dc-3d84-83e2-69dbc7579dd1 | -11.32764 | -43.56611 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9cfb723b-5a52-39a5-9e36-11f39597c2e5 | -12.80253 | -48.17156 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3355620-7986-3dcd-8b2d-853625b6db16 | -10.97704 | -46.90734 | 2025-08-29 04:40:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b1887137-40b6-3ad1-a1bd-53c885e88240 | -4.22933 | -56.00648 | 2025-08-29 04:40:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a622ba43-9425-351e-a5c7-91b7a0bf77d6 | -12.70207 | -48.19102 | 2025-08-29 04:40:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 3890090f-d12d-37b2-82b5-5a22089c9ad8 | -6.97921 | -44.12409 | 2025-08-29 04:40:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e96e45ff-e3c8-32c4-9f7f-069a35ec7aef | -6.44124 | -44.56507 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 053d7cde-4614-3ad1-be51-3a50c0bafd34 | -11.34196 | -43.52784 | 2025-08-29 04:40:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d3ce372-622f-31a3-ac81-e535f4b3b1e2 | -11.50503 | -41.52101 | 2025-08-29 04:40:00 | NOAA-21 | AMÉRICA DOURADA | BAHIA | Brasil | 2901155 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3ac7e0ba-a4f6-3974-8d63-95c7121a08f0 | -8.41832 | -47.36736 | 2025-08-29 04:40:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9afe75f8-f085-32dc-8183-3249c2e994a6 | -8.69687 | -50.38432 | 2025-08-29 04:40:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c4d113b-4773-3f99-b925-76692bb401fd | -8.56056 | -51.31277 | 2025-08-29 04:40:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8cb37e55-5f9f-3fa9-9d8f-ef83a0edcf74 | -7.63879 | -46.55506 | 2025-08-29 04:40:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3338e48c-b05c-3915-85aa-66125a0b812e | -6.16919 | -47.2811 | 2025-08-29 04:40:00 | NOAA-21 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e3960235-b954-39ed-8d8d-001ae668329b | -9.45748 | -60.55399 | 2025-08-29 04:40:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 37a3d0b8-df20-3862-ba64-cb487c702c2e | -6.38732 | -45.22654 | 2025-08-29 04:40:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 39.7 |
| 1e5eba35-74a3-3fff-b382-62265313f2ca | -11.61096 | -46.19879 | 2025-08-29 04:40:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8365dab1-c95d-343e-8873-141cc22d49d9 | -11.95518 | -44.84544 | 2025-08-29 04:40:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b6d0b23-3b1d-3916-8669-17375d33b94e | -13.54497 | -46.9457 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2348fac6-68ff-3ffe-b549-760f3e08a68a | -13.36802 | -46.87841 | 2025-08-29 04:42:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README53.md)
