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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e04e0219-33cc-3d23-8e32-c953e52c2b95 | -4.79363 | -43.04669 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 93c099cc-a9d6-32a1-af67-2611beda9c76 | -7.77318 | -46.19853 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bfbc8e44-df10-3708-8ce8-58c8b2a5c5d7 | -5.38745 | -42.26436 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c651ce34-a233-3791-9336-d40511ff4a87 | -7.28012 | -42.99019 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3ff2d34a-d78f-3190-97f2-9a92c6b6b8d2 | -5.31032 | -42.74553 | 2025-09-24 04:00:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f1e69536-ce7e-3a63-bccf-376089e1777b | -4.31344 | -48.10207 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 61941543-e620-36d5-8fd3-b37c8c7e56de | -4.00956 | -43.2668 | 2025-09-24 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb248bcd-5a81-3c90-82cf-968cb54fa6d5 | -5.73337 | -42.61193 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c73fa26e-5d86-3c82-ae61-7bffa837e467 | -6.90125 | -38.57412 | 2025-09-24 04:00:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d4638d2d-1c09-3dc6-8a7f-0711d7b9735b | -3.39615 | -47.50219 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d74818ec-b07b-391b-af91-aa12ce36ac5d | -5.91295 | -43.86169 | 2025-09-24 04:00:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 54f11107-f1f7-31f0-91ae-ff877c1a1f05 | -7.49735 | -38.999 | 2025-09-24 04:00:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d73f1dee-f07c-32e3-bce6-bac7b4d96342 | -3.69128 | -49.01433 | 2025-09-24 04:00:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc0d046d-b88c-36cd-83be-69f94b2fcf91 | -8.32007 | -46.22261 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b8e068f-0fa3-3d35-8f5a-ab6e0c40cd66 | -4.82195 | -46.00558 | 2025-09-24 04:00:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c3f0326d-ad8e-39b9-9bb2-4762170da5ef | -6.59654 | -44.31163 | 2025-09-24 04:00:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90282edf-8078-3ba6-a7b2-f62ef9c36e29 | -4.01259 | -43.27198 | 2025-09-24 04:00:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 239f3ac7-8067-3a45-9d21-13958a59e1db | -5.61202 | -42.9889 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| bfebf33c-819f-3b86-b4c0-94cbac5f759d | -4.73494 | -42.08822 | 2025-09-24 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1056424e-526d-3807-8b82-e8ceb82921c9 | -3.51592 | -49.4501 | 2025-09-24 04:00:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 066b0aaf-76df-31e8-acf0-6d6d35479db1 | -5.75544 | -42.56581 | 2025-09-24 04:00:00 | NOAA-20 | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5bc0c9a9-1484-3119-8568-2d55bffa3d4c | -8.52828 | -40.61097 | 2025-09-24 04:00:00 | NOAA-20 | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cd697ddd-9cc9-31fb-b472-ab6d6603cdfc | -7.01584 | -41.96865 | 2025-09-24 04:00:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a34e49ac-8aaa-3f9a-a436-333f1ddcfcb4 | -5.21535 | -42.34401 | 2025-09-24 04:00:00 | NOAA-20 | COIVARAS | PIAUÍ | Brasil | 2202737 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c9e435c7-9970-3eb9-836a-eb3d620328da | -5.63474 | -45.73633 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a150bae4-2d8a-38a1-94ac-b0ab3b080b1c | -7.81347 | -40.16904 | 2025-09-24 04:00:00 | NOAA-20 | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3d940bd1-9762-325c-85ab-e4486738a22b | -4.29206 | -48.26275 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ac9d6c1f-9a36-3eac-b3d1-8b3a68c71201 | -7.17138 | -42.24049 | 2025-09-24 04:00:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f9a68aa9-3fa2-3a67-88c6-999cb9ec3226 | -7.77751 | -46.19904 | 2025-09-24 04:00:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 07ffc0e2-3b9f-3a65-82be-930207a54d3d | -7.74737 | -40.26507 | 2025-09-24 04:00:00 | NOAA-20 | TRINDADE | PERNAMBUCO | Brasil | 2615607 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b631f013-9202-354a-86cf-ec78227323cc | -4.39704 | -44.37526 | 2025-09-24 04:00:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 422ab1bd-b86b-3649-888c-3e285441c32c | -7.97363 | -43.86822 | 2025-09-24 04:00:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9bf2de89-9c4f-32e3-92bb-8f77fdd235a0 | -5.03253 | -43.60463 | 2025-09-24 04:00:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb117d40-1372-32be-81ca-2ef9a8c72c61 | -9.52102 | -43.07535 | 2025-09-24 04:00:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0e9525a3-cbb9-3ebe-afd4-0cd37e1fca32 | -7.51237 | -44.3243 | 2025-09-24 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| f770b876-854f-323c-900e-6d98e6009f7c | -5.8434 | -42.64927 | 2025-09-24 04:00:00 | NOAA-20 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 00fbb1c6-d3b6-329b-a4b2-f75a1a79eeed | -4.31292 | -48.10519 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df35973b-984e-38b3-8564-740a00f80564 | -7.38093 | -47.03873 | 2025-09-24 04:00:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4f7979a3-d925-31df-a2f6-0cf2aee9978e | -5.63247 | -45.7236 | 2025-09-24 04:00:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 40382821-edb0-3bb5-9d53-60f7dc0100d0 | -5.78161 | -42.56178 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5dc88cbd-46af-3259-b5a0-b0cbab6fd7ac | -5.37626 | -42.26661 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8b92ef1-5734-3dab-8801-69bdab01b509 | -4.73845 | -42.08879 | 2025-09-24 04:00:00 | NOAA-20 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 83a453f1-3177-3a16-8a34-6bbb7932ce34 | -8.26193 | -44.38955 | 2025-09-24 04:00:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a1d36df1-36ee-390a-9b3b-d4c77d6276c9 | -5.49456 | -39.17134 | 2025-09-24 04:00:00 | NOAA-20 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 4.3 |
| c8f49d30-79ed-358d-96a0-1b3ae1be8028 | -5.73984 | -42.61712 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 0cb01b19-1ba7-3a75-86b1-81fee00368cb | -8.54733 | -44.96469 | 2025-09-24 04:00:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9446027d-ea6d-3a12-bb0c-7d371690c15d | -4.30828 | -48.10115 | 2025-09-24 04:00:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 043afc40-1720-35f5-a370-8dcb9b07f93c | -6.20018 | -37.62344 | 2025-09-24 04:00:00 | NOAA-20 | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 815a3904-0319-3b4b-bf34-a7d427fcd446 | -7.94938 | -44.10233 | 2025-09-24 04:00:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 434006ed-d94b-3dd9-a559-9bd667ae4ca3 | -6.34422 | -43.78812 | 2025-09-24 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 51e239f7-709a-355f-9cba-5f96e79c4ce6 | -3.39712 | -47.49634 | 2025-09-24 04:00:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4f41ff46-9245-394e-84e2-b264f6498922 | -8.84296 | -46.18279 | 2025-09-24 04:00:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d073b423-7d97-356f-9e1c-ccc6410084d1 | -5.7327 | -42.61604 | 2025-09-24 04:00:00 | NOAA-20 | MIGUEL LEÃO | PIAUÍ | Brasil | 2206308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a0371077-3293-3786-a923-f000e82328e9 | -7.44431 | -44.10371 | 2025-09-24 04:00:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2794cfa-19ee-3256-8d5f-8398b1f4bfc5 | -5.97325 | -44.12643 | 2025-09-24 04:00:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f1625f7-6eb7-3864-b823-7aacbd1940d0 | -5.38492 | -42.28017 | 2025-09-24 04:00:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fe3778dd-88a8-3e82-9abb-18b086827a3d | -5.7658 | -42.59203 | 2025-09-24 04:00:00 | NOAA-20 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| df0b55c1-fe62-32fc-9f06-ff2da105b007 | -5.76679 | -46.76107 | 2025-09-24 04:00:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f3571f81-06a2-32dc-8c19-c2de375666a0 | -7.27656 | -42.98963 | 2025-09-24 04:00:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9f72302a-0e54-32d6-9f64-a4efaf97137c | -6.66385 | -47.74886 | 2025-09-24 04:00:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 540ece5b-c16e-3127-876f-67e1424564e0 | -6.34493 | -43.78591 | 2025-09-24 04:00:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ef6f603-4a3c-3642-8648-2cffe260069c | -5.78295 | -42.79467 | 2025-09-24 04:00:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 41ecbafc-07f2-3a2f-a7d3-4f0208d49ed7 | -5.2456 | -43.72524 | 2025-09-24 04:00:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b008d66a-e1e4-39be-a688-cd891d02342f | -16.51217 | -43.55066 | 2025-09-24 04:02:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbe744fd-732a-3481-b9e6-05dd0c14b5a1 | -12.66977 | -44.35143 | 2025-09-24 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 425d60af-b1e7-3cdf-990b-70f2e9ec33f8 | -11.52275 | -43.66232 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d7742624-2269-3bf5-90c7-b4ea8333d079 | -9.57123 | -47.58085 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7c68d13-bc40-3686-8fcf-2edc2df21a24 | -11.51421 | -43.64866 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b2da2014-8955-3896-bc31-736813ae4759 | -10.58432 | -44.06748 | 2025-09-24 04:02:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3014c18b-395f-3523-b382-ad8c42e7f721 | -10.85018 | -45.41262 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 371834a4-ed55-3683-8022-e1b3d85f09c4 | -11.51858 | -43.66568 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 74612373-7dba-397f-86c7-89d265b2868b | -13.61394 | -43.97784 | 2025-09-24 04:02:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 61370ea0-6926-3bf7-a629-28b04c54abcf | -9.95911 | -46.28687 | 2025-09-24 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cf669330-8876-3ab0-b4bb-3de34fbefc7f | -11.63286 | -44.36656 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7b35c6a9-3ed0-3c0c-aeb4-8a7e0cde7c7d | -13.38873 | -39.94859 | 2025-09-24 04:02:00 | NOAA-20 | ITAQUARA | BAHIA | Brasil | 2916708 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| e1f9bed7-851a-354a-9a67-957ecba412b5 | -11.67924 | -44.37912 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75595cf9-81f6-3e09-9126-be7da4e14a11 | -13.81609 | -43.2295 | 2025-09-24 04:02:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 9ab36e2e-0748-3f2a-8fbc-718bcf9941df | -15.80854 | -45.36288 | 2025-09-24 04:02:00 | NOAA-20 | CHAPADA GAÚCHA | MINAS GERAIS | Brasil | 3116159 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bb6bb74a-2cf0-370b-a835-15e034384912 | -11.52141 | -43.6703 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0fe60db5-82ef-3aac-8a4a-9b3aa4bddf5e | -12.07696 | -44.77522 | 2025-09-24 04:02:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 04c0af75-1ba8-3d6d-a786-fed8163ec581 | -14.28769 | -41.83921 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b3ac5bd6-e7a1-3ea6-a5ed-8ed0fc19e034 | -14.29706 | -41.84442 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| b552ec79-526d-32eb-b1a8-330b8941ce20 | -9.96856 | -45.31644 | 2025-09-24 04:02:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 241b2f85-c5f2-36b0-afe2-157f3715b644 | -9.69021 | -48.90401 | 2025-09-24 04:02:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 69f37153-fca8-39f0-b3c3-6f58c1574651 | -13.57178 | -42.47015 | 2025-09-24 04:02:00 | NOAA-20 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a91a43d9-036a-3d68-984b-2e293cc8a9d8 | -11.63356 | -44.34035 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7af72549-4ff6-3eec-873c-6264756a7a3d | -9.56171 | -47.55487 | 2025-09-24 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 452e7e36-83f4-3749-b645-872cac384c9e | -11.63864 | -44.3544 | 2025-09-24 04:02:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 977b98a3-5d6f-38a2-b0d6-0cb92eabf9f4 | -9.10375 | -48.89948 | 2025-09-24 04:02:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f1a41e95-682d-35a2-beab-b78dfb80287a | -14.30093 | -41.84142 | 2025-09-24 04:02:00 | NOAA-20 | MALHADA DE PEDRAS | BAHIA | Brasil | 2920304 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 3e9d3a5f-35bb-3bd5-b570-67468e5afbd6 | -12.01468 | -47.79427 | 2025-09-24 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 048a22c2-80b3-3dca-81c7-f32b76e5cc20 | -11.66843 | -44.88654 | 2025-09-24 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6d1a663e-349d-361d-897b-3e9fb02d60ff | -10.85208 | -45.42118 | 2025-09-24 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b4c03dcf-fdc9-31bb-b8ca-0f819d743a82 | -11.0091 | -44.50216 | 2025-09-24 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1284bd6-85eb-342a-adf0-2e117a50990b | -11.53242 | -43.64766 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 59fc79f9-6672-3ab4-92c2-e0b847a792d1 | -11.53308 | -43.6437 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5652af6b-a99a-3943-9691-84e6a7b90410 | -11.51354 | -43.65262 | 2025-09-24 04:02:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6ff5994-05f2-318a-bd90-8461536f3aed | -13.64583 | -43.81027 | 2025-09-24 04:02:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 300b366a-8883-3c6d-bcf5-09cdd8d229e9 | -14.83721 | -40.90862 | 2025-09-24 04:02:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 185797c9-dc70-372c-b806-314d8ba36667 | -11.00834 | -44.50656 | 2025-09-24 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README10.md)
