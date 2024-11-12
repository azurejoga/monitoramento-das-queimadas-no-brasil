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
| 638948fc-8711-3cb9-bb97-058b7f7c6b7d | -3.21671 | -50.38964 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c9bcc3e-decc-33b9-8fbe-f05a0366dbe2 | -3.74027 | -50.18846 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8b487c39-d1ab-34ee-a5e6-ec009c557ef8 | -4.09059 | -50.33245 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4773497a-a16f-3867-9782-c0adafe73ad6 | -3.97887 | -48.41373 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b4989ed1-65d7-3bc9-886e-2ee4857c2b38 | -3.94334 | -48.16012 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14f39578-80d8-3ba7-b366-0610d7ffb967 | -3.62433 | -54.71092 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e1dde61-fd16-3e1a-bbbf-1b90f89e2708 | -3.43288 | -54.53629 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eccdc1e4-9489-3dd9-995d-347db9058e2c | -3.95133 | -48.17719 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| bd323e8a-9c74-3595-bf09-2fe73a6292d0 | -3.84793 | -50.21789 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 90b66677-5d0d-3aff-89f9-c7e102940c82 | -4.34022 | -55.36758 | 2024-11-12 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| daaa3fc2-92ca-39d1-bb77-5cb755fcfd77 | -3.94566 | -49.00661 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea1e893a-63fb-3eaa-82b2-a626eed495e5 | -3.26271 | -50.43325 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 166090e6-d8a2-3f9d-8670-c784c91f4d8d | -3.75744 | -50.1812 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eab21e6-a03c-3953-af73-fdb513161ff1 | -3.40891 | -50.37544 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 660324dd-a2b1-3982-897b-3ba909e27450 | -3.96057 | -48.18652 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f83af29e-72a6-3160-9c1a-59287d0d6f14 | -3.80661 | -48.96374 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fb06866-77d3-3d3a-be94-131851465c72 | -3.24996 | -50.31122 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d06c1b02-86cc-38e9-91af-f29a52716ae6 | -3.24913 | -50.31628 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e920815c-12b9-3c42-b9f0-3fcc1c2908b5 | -3.43212 | -50.30619 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 30fe3aea-1678-3409-98f1-91571b49e37a | -4.24138 | -55.86781 | 2024-11-12 04:23:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 53ab6607-7620-3a60-8c9b-fd0c0ab79086 | -3.96254 | -49.96176 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc3df694-4bf0-3758-b852-fed61c78d856 | -3.69893 | -54.39468 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 689e8737-33f0-3dfd-a44b-1bae983e0636 | -3.94458 | -48.15234 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 787eac73-42f6-351b-aead-baaf02eb874d | -3.67148 | -50.21519 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f6308b2-7a22-3076-b15a-7890f0f79156 | -3.95194 | -48.17336 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 388b8b8e-3c1b-3dbb-a9d7-1896cb41be46 | -3.38803 | -50.1303 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f2190496-6cbc-352f-bce2-d2b2ce892c6a | -4.41701 | -49.72198 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b5fbdf6-953a-3232-ab6b-3f678614899f | -4.47011 | -50.12894 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f6cde6a-d784-378c-92aa-d71759dbea29 | -3.943 | -46.41375 | 2024-11-12 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 95a6d835-0ddd-316d-ba64-5dd679a76c65 | -3.62856 | -50.18295 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b26b356f-4e37-3a6c-a3ab-7b757d8f8549 | -3.40576 | -50.36969 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 253d7a9e-e9b5-3704-bc1f-3e1eae910840 | -3.85356 | -52.37954 | 2024-11-12 04:23:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1817fcc-c520-3849-98dc-351cb9453e3e | -4.33166 | -43.89177 | 2024-11-12 04:23:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5de657ce-1016-309e-843c-d7038e3abfbe | -4.11866 | -48.51227 | 2024-11-12 04:23:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9515bdf-4074-3006-a150-905dd9c6fdcc | -3.4343 | -50.31326 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 73362f91-5acb-366b-bda0-552e28fa5c5d | -3.81023 | -48.96432 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 94492fab-74a2-3c22-8b40-4d8db9f50af0 | -3.70851 | -50.43501 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d000ad89-2720-33fd-86b8-be80aec81b76 | -3.65505 | -50.21762 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74cefae1-c1ff-36fb-af56-d44e6411fe92 | -3.95345 | -46.71189 | 2024-11-12 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| abc29982-ccf0-3002-80e8-3c8f3e9e3212 | -3.99521 | -49.28078 | 2024-11-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c4c205bf-c054-314a-be6e-85afcb09d245 | -3.84403 | -50.21728 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2299e329-139e-3599-a81d-fdecef5233d2 | -3.94632 | -46.41425 | 2024-11-12 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d85bfda3-d584-36fb-9573-c5de385ba1ea | -3.59879 | -48.9511 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7cf12502-7808-3b78-98a8-34a6f45450ac | -3.29632 | -50.02773 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31bbdad7-4504-3bed-abc1-50eaad08e016 | -3.94271 | -48.16401 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf485b1f-8fe9-3254-9161-21a877c66835 | -3.43598 | -50.30318 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 51f76450-c054-3931-9060-b19a021c6ac3 | -3.46086 | -49.20374 | 2024-11-12 04:23:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd9fc14a-d015-39a3-aa7e-b71930d479f8 | -3.69814 | -54.62266 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c400d512-5950-3526-ab33-b366f7c08475 | -3.95256 | -48.16951 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e433fa13-b383-3934-8cda-201d58e19289 | -3.66595 | -54.65726 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c950ac70-ead5-3ae9-9ff8-fd250004186c | -3.79939 | -50.0433 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f845fdee-4bf2-3c23-a752-2aa764e297f0 | -3.23426 | -50.4571 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f781eed5-b013-3573-91d4-f87c907b9364 | -3.69842 | -54.39776 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b43c551-0e61-349d-8c60-46f185e4c207 | -3.43132 | -50.31123 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 94993ff3-b472-37c3-8340-2eb1f9c43052 | -3.95647 | -49.92693 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 83675906-4739-3a70-afed-25eddb270d2b | -4.27908 | -50.67767 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b0fa7d8-bd4a-3a71-905e-002e2c92cb91 | -4.05284 | -48.31247 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 00329e1f-1fc4-3110-aab4-336200a22f7c | -4.04067 | -48.29866 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44675ce2-36da-3a2e-a8d7-04180ab9aab9 | -3.62489 | -54.70763 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| febbc400-882c-3bac-a8b8-c715681383f3 | -3.6714 | -50.21766 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d730e997-d937-3ec7-9044-e0d5210d0da4 | -3.27802 | -51.06021 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a7b73aa3-b32a-37d9-9ada-7d62cc939752 | -3.95071 | -48.18106 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 941be62e-dc20-3d2c-837a-432bfdd0e97e | -3.89623 | -50.09084 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed2975e6-8212-3a0d-ada4-0998eb10a03f | -7.42846 | -35.23685 | 2024-11-12 04:23:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 32fce4ab-3ceb-359e-998b-61f3056de430 | -3.6683 | -50.21214 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eeff8e99-8f55-32cc-9fe3-a01771be0962 | -3.51259 | -51.35183 | 2024-11-12 04:23:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e65d228-7d36-3331-91cf-e659a557b2e1 | -3.89237 | -50.09018 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed6a3d48-e209-342c-a1a5-eb30ef906426 | -3.94521 | -48.14842 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b7b2773-0bcc-3aa7-aa47-f0a95de0d491 | -3.75354 | -50.18054 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9454fdb2-35c9-3da4-9090-06712c20458e | -3.28633 | -51.06156 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fda50b7e-fab4-3b10-9f08-abd2b3b60e6d | -3.26449 | -50.14875 | 2024-11-12 04:23:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 469af924-ac68-36a0-bad4-9979f3032c40 | -4.02044 | -49.00834 | 2024-11-12 04:23:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d123903-3bbc-35d3-9c7c-73f77f358556 | -3.78627 | -50.10067 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| f789f5ad-8ff6-30e3-8ebe-114f69523ade | -3.92295 | -49.9235 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cb07122-0c30-3056-a4e1-4e42d96e93ca | -6.97588 | -40.02948 | 2024-11-12 04:23:00 | NOAA-20 | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| bdda6a42-bdd6-372d-9d5d-c73bd416219e | -4.09035 | -50.33487 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e353eeba-766e-3d3e-bb6c-59593188b4c0 | -3.95646 | -48.18988 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 84f06a18-1569-3d13-892c-3de7c0bc6ad9 | -3.95009 | -48.18495 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f1cf97a8-28b1-37fd-a485-fa33cb308555 | -4.05861 | -48.32137 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6fa6fb04-85aa-35e2-9c3c-35075f64b27d | -3.95708 | -48.18599 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa24b313-70ad-32df-a601-fdf8d3ad10cf | -3.70732 | -53.75667 | 2024-11-12 04:23:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0cd6ca64-071b-3356-a740-d65881992c95 | -3.74416 | -50.18916 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2767eebc-fa4a-3b51-8f99-27ceab462eae | -3.9577 | -48.18209 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 96a54458-9734-3616-9e04-c1379cc3791c | -4.11409 | -50.23484 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c13ab10a-64e4-3716-816c-54d8bf139e21 | -3.66013 | -54.65964 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 149d7764-6b20-3e38-9481-0629ec1f8afb | -4.66588 | -50.55159 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c56cd7b0-0927-37ff-9f80-f5d042e95c69 | -4.08922 | -47.70958 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 5989e57c-6766-30d2-96bc-a9e5985c154e | -3.88239 | -49.9558 | 2024-11-12 04:23:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cdf53c9-588b-3665-b96d-706007be39de | -4.25172 | -50.25705 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4589b51-acf3-39c0-972f-82b827cef64f | -3.95359 | -48.18546 | 2024-11-12 04:23:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 467355a2-ecc8-3924-9d6c-e9d88a97b3fe | -3.69805 | -50.20194 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 074d5a0c-6a39-34c0-a717-e20ad81308e8 | -3.36776 | -50.0544 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c5d563b-a825-382a-a538-93d9c10852b8 | -4.31412 | -50.81562 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0dd50ed-93a1-34a4-9e89-9855f9fdbfc1 | -3.67065 | -54.66167 | 2024-11-12 04:23:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 28ad46c3-d0c9-3709-94d1-e32b2cd0f3b6 | -4.42152 | -49.71804 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| a7f237f7-e982-3ff0-8f74-638450418e95 | -3.66667 | -50.22197 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d1896d76-402f-3e1a-9c0d-3aaeb1d5d3b7 | -3.67302 | -50.20789 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2ca61f8-64b4-32cb-b645-33d72b98775b | -3.3109 | -50.08535 | 2024-11-12 04:23:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a24772eb-d740-3faa-99d6-fd484c30404a | -3.94355 | -46.4103 | 2024-11-12 04:23:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8023bed4-b5ba-309c-9701-6635c319d064 | -4.42077 | -49.72256 | 2024-11-12 04:23:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README13.md)
