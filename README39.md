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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d8bcb925-18d0-36b5-99dc-40f4d534fa1e | -5.59368 | -45.51732 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bf3d2bf-612d-3628-bb63-d04b81535509 | -5.59608 | -45.52703 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3d5aee2d-be71-3d90-a17d-8c0d5b5ab85f | -3.75993 | -54.8171 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3328122f-f40d-35db-91c3-c045d338a56d | -4.11392 | -48.01617 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 6e3d8c53-ee78-3513-8bcd-14925d0b8f27 | -2.74217 | -48.69973 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71ad85f3-d42a-36bc-8250-a9052a5b33a2 | -5.88797 | -43.19632 | 2025-08-29 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bc1faaf5-bc1b-3878-87df-97a04bb7901a | -3.97242 | -47.15509 | 2025-08-29 04:38:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5e3e1b90-dfa0-36e4-893b-a839fd3bc233 | -5.70335 | -45.96168 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f2277652-2458-3aca-9f37-70eb5cfb131f | -5.59301 | -45.52188 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 642d9138-8010-306a-9f4c-d3d9545054b8 | -5.59743 | -45.51792 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6dd9e53e-a601-3536-a3ff-0abe17591646 | -2.7709 | -49.18962 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54d896df-12f2-34f6-9b98-0002f968f8a0 | -3.42685 | -49.04288 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 51e0e2e8-3c73-3f11-a50e-308eb08e589e | -4.63962 | -48.79291 | 2025-08-29 04:38:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b449756d-48a0-356b-b2d1-2d87df24ed46 | -4.41024 | -40.69411 | 2025-08-29 04:38:00 | NOAA-21 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f80712e2-9bbb-3479-a357-a7609d9560dc | -5.6955 | -45.96286 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 768ee047-8fce-39ce-9b0f-191ab78c3bfa | -5.85174 | -42.91248 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| d38ab8bc-e131-36f0-84dc-04444ee92c43 | -3.98683 | -47.95693 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d8dcff5f-ebd2-37ca-91ce-001fa7404987 | -4.10236 | -48.20098 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9ac10a66-a2fa-376c-9da3-ccfdfeab2b81 | -5.86768 | -42.96035 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 7c54be88-fea1-3687-a52f-c01fe300b491 | -5.59233 | -45.52641 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ba77b82-ed58-39c4-a4ff-34db3b38b554 | -3.76485 | -54.81365 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48bfe2d2-42b6-31ed-a38c-614b8b1a2ba2 | -5.63255 | -42.60454 | 2025-08-29 04:38:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 97f13e71-cdcc-3ed1-b850-0da85f783140 | -5.61908 | -45.01443 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1ba341d3-bae0-3cf2-954f-226b9440c251 | -5.60086 | -45.205 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 707106b1-bf64-3cb1-a6d0-308ca11a3502 | -5.71813 | -45.5382 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0917cf39-a3ca-36b6-95a3-90b101d63341 | -2.98504 | -48.60373 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 51e0f27f-706c-3f0e-9ea2-1086ab80e607 | -5.62516 | -45.00049 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 57f4f550-99b8-3b4f-9506-ad545e76e927 | -3.42301 | -49.04581 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| c2c0641e-cede-328e-ad2a-3a2177d74bbc | -5.18073 | -46.07693 | 2025-08-29 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 99f968d6-085f-3157-a628-220a279b7480 | -6.0593 | -43.4351 | 2025-08-29 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 22753b44-a0e0-34a4-b5b7-82d9f7c04e54 | -5.97559 | -43.36103 | 2025-08-29 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| cd678aa9-4923-3bc1-8c01-2e8e323f3c3e | -3.04623 | -49.43085 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 40b316a2-388f-33ab-9f41-bc3b81a84e1f | -4.4856 | -47.67659 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bfde4e9b-fc02-348c-b7c7-dac1cc437118 | -5.60154 | -45.20749 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5be09e34-e82d-3225-ac49-1e914e2c541c | -4.74376 | -41.43927 | 2025-08-29 04:38:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4894d0f7-12a7-3669-991e-ed1aa38b8d5f | -4.07252 | -47.9558 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26f65a41-dc9a-382e-9095-93ee2604452e | -3.51535 | -47.2067 | 2025-08-29 04:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9e2a93f-8ea8-3d03-9718-8a9cfa438d6f | -4.49461 | -47.68529 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bc7dc9b5-aa5f-334b-b3f7-707ce3c8d1d1 | -3.55466 | -51.01578 | 2025-08-29 04:38:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| af7995e3-1ea9-37c2-9ddf-cabe76f213ac | -4.63455 | -43.09005 | 2025-08-29 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e132b69c-5984-31f0-9c17-eb21c7f9a2ca | -3.7635 | -54.82177 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 98291e63-becd-33a2-b701-763dbf223e51 | -5.69535 | -45.96486 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d6526ca-8609-3cf9-a6f9-c95d5751039c | -3.73571 | -48.94028 | 2025-08-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d33d36e9-2ff1-3e19-b2bb-8a9c0c084e6e | -5.61959 | -42.59777 | 2025-08-29 04:38:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| dc560c49-bd49-3c8f-b254-e8be7bedddbc | -5.61741 | -44.99933 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0633384c-cb5c-3a90-8af5-3ff9b5bda71f | -5.62309 | -44.99749 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 8e87656e-67c2-3436-9d51-c09ab8649db2 | -5.79234 | -42.5721 | 2025-08-29 04:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1f8f2341-0b16-3afa-a2e8-9a0803895298 | -5.49973 | -44.57667 | 2025-08-29 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f15ab800-926b-33e5-9971-89e39cb130f4 | -4.07642 | -47.95278 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c95b96b-b44f-3be1-8236-3be2480b70eb | -5.7871 | -42.60903 | 2025-08-29 04:38:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| baa5263e-48a9-3c31-a218-750e7e24b18a | -4.08569 | -48.04408 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c349229-b954-3f7e-84e9-b773fcc83383 | -3.53001 | -52.86946 | 2025-08-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bbb32118-24ce-3250-a26d-624b1bf80c88 | -5.62697 | -44.99803 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6d50e03d-17e2-3d32-bae8-ad49aa95d18a | -3.75925 | -54.82115 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 45ec6622-024e-3183-adb4-6229bf0eb100 | -3.41917 | -49.04873 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 79d5fc51-f931-325f-9e51-e643a39cb3ec | -4.07307 | -47.95226 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8348e1f8-55b6-395d-badc-b5876e80cc9c | -4.74452 | -41.43385 | 2025-08-29 04:38:00 | NOAA-21 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 57a7fa33-1556-3080-b3d9-3841515a3ba9 | -2.92955 | -53.69183 | 2025-08-29 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bfbe75ef-473b-381b-895c-2d63c7ad6ff3 | -5.62625 | -45.00299 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f67644ab-44e6-3b0a-9cb3-53dc409b25fd | -3.97626 | -43.24728 | 2025-08-29 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| a0e4ec0e-546a-359c-ab54-82bae3620af4 | -5.15656 | -47.84856 | 2025-08-29 04:38:00 | NOAA-21 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ea25b94-af23-3175-938b-c47b5fae5dcd | -3.08856 | -40.11132 | 2025-08-29 04:38:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 436c0d31-084a-3fe0-9008-e14bf2816120 | -4.58865 | -43.31607 | 2025-08-29 04:38:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 008a21bd-0ff5-37ea-95bd-55ac91cf1387 | -3.76319 | -54.8255 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d9bdb4ff-afad-3bac-b246-f28b4b255d9c | -3.044 | -49.42343 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a8ddce5-df5c-3a23-b1cb-62d055af9d5b | -2.44577 | -47.33204 | 2025-08-29 04:38:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 956d40f7-03f7-3493-b06d-f74ef31d0376 | -5.18135 | -46.07277 | 2025-08-29 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2b705ca0-3568-3041-84a7-2d4ad9eaf03b | -5.62237 | -45.00243 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d17e047a-5592-3ba8-9d36-891bdb0fa945 | -4.36188 | -46.56027 | 2025-08-29 04:38:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d2b95433-cfd8-3669-855a-feaf3ec14e0d | -5.4331 | -45.52488 | 2025-08-29 04:38:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 23278512-967f-3556-a8ed-a0d279431e2d | -5.61981 | -45.00964 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| cf2e63c5-a938-3534-bd9e-0f4943e8ff9f | -4.1118 | -48.20601 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1af6a3c5-2ef8-332b-978a-ac3b5857fa0f | -6.13291 | -43.05823 | 2025-08-29 04:38:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 50f99352-4d26-35cc-9235-dcbf2207b346 | -3.75894 | -54.82487 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| df5e2051-5cd9-388c-9e94-e15f9554e787 | -5.60017 | -45.20972 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a52dd144-7117-31d3-901d-34d1ed9e83a7 | -3.42355 | -49.04237 | 2025-08-29 04:38:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 98e86d68-dfb6-3655-9c08-21f10a2f51cd | -5.79231 | -42.60513 | 2025-08-29 04:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 8619bb92-97f6-369b-83a4-e16dbcbae397 | -3.97684 | -43.2433 | 2025-08-29 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5b0169b9-3ded-31b9-a81b-94901bd637b8 | -5.62167 | -45.00729 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 2a4abf3a-a9cc-3104-a77f-03561cca02ee | -4.1516 | -38.47898 | 2025-08-29 04:38:00 | NOAA-21 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 82955ba5-ffbb-3988-87a3-06c9f1917d25 | -3.38616 | -47.49429 | 2025-08-29 04:38:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75626140-5b43-3925-963d-8dd2086d5430 | -4.4914 | -45.90432 | 2025-08-29 04:38:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a89a3ce5-c19f-314e-a16b-ca7b315aaefe | -4.09904 | -48.20046 | 2025-08-29 04:38:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ca005a03-6f1f-34fb-b23c-422fd68d6b7a | -3.04954 | -49.43136 | 2025-08-29 04:38:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 198f0f87-0866-354d-a0b8-e1fcbdc316b0 | -0.75425 | -47.75071 | 2025-08-29 04:38:00 | NOAA-21 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f7a33da-27d4-3661-a28e-e97b88357915 | -5.79165 | -42.60979 | 2025-08-29 04:38:00 | NOAA-21 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| f4ffa839-c228-3ab0-a977-896afdb4a32d | -3.27726 | -43.52623 | 2025-08-29 04:38:00 | NOAA-21 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bb261a42-3f9e-3f13-beee-1441fac44df0 | -3.76447 | -54.81743 | 2025-08-29 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| a73d4568-5769-3ea3-8cb4-c575201e99d0 | -3.62066 | -43.54197 | 2025-08-29 04:38:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e42bc342-059c-3d90-9e41-ead85b3c1279 | -5.6171 | -45.01149 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 606dc06e-a697-3118-b557-403afb6d0a9d | -5.01736 | -44.47858 | 2025-08-29 04:38:00 | NOAA-21 | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab4d1b91-2f1e-3bf2-ac4b-72ee622f0f92 | -5.18435 | -46.07747 | 2025-08-29 04:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f03e3fb8-4070-3cb6-a169-3b7efd31ed70 | -5.97729 | -43.35927 | 2025-08-29 04:38:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 5547e03f-7d14-3438-8880-7487329ff697 | -5.86133 | -42.94115 | 2025-08-29 04:38:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 363b0919-e6d7-3e94-be7a-8c9d41e9e3f3 | -5.50422 | -44.57375 | 2025-08-29 04:38:00 | NOAA-21 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4ac36a2-1c26-3a60-873e-9eeccc3850c4 | -3.80552 | -48.64471 | 2025-08-29 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3eaf00f-6e43-329d-beee-05e34da5755f | -5.43209 | -47.54019 | 2025-08-29 04:38:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| de38d9e3-44e4-3bae-85e9-23d30a7bd632 | -3.1832 | -48.7723 | 2025-08-29 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b754d1f-1715-34bb-80bf-384617d23a01 | -5.49242 | -45.8223 | 2025-08-29 04:38:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e0ba4ffb-3417-301e-b6d6-01d54abb384a | -5.72257 | -45.53426 | 2025-08-29 04:38:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README40.md)
