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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c12c7628-c019-397f-85fc-5b346b96ede6 | -3.09745 | -50.38219 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 78e8ec9f-fb64-34ea-9cf1-8381aad5c6db | -2.53926 | -47.79916 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b2db51bd-1f18-3dd7-90a8-50f2ca9551cf | -5.93028 | -40.88217 | 2025-10-13 04:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8e446205-1539-3f99-a51c-c5695c9b317a | -5.73579 | -40.76726 | 2025-10-13 04:21:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5de85819-92f7-3acb-be03-ecf05d66fa48 | -5.57075 | -45.27891 | 2025-10-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6d9b69ae-8dbf-34bb-9199-fbc17e6f67dc | -2.5423 | -47.80436 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e1cc841f-4272-3d57-914b-b23bbbb7455f | -4.28639 | -48.57359 | 2025-10-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65a4da47-94af-3154-bfdc-4ddfd19d4cba | -5.34585 | -43.44723 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d2c430bf-cb5f-337f-b8ce-5d00b9d9819f | -5.83628 | -42.31966 | 2025-10-13 04:21:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 125a4c55-e0d8-3142-9133-7a13724c5e7d | -3.86829 | -44.12723 | 2025-10-13 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9517d64-4535-36e7-acdd-5ea1716a1687 | -3.06794 | -49.40384 | 2025-10-13 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 26d4c6df-da89-390e-809c-2f5b6b011efb | -2.26046 | -47.85534 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| abc91c38-5719-3d73-97c2-89652d7acad1 | -5.8837 | -41.38375 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 478b0184-6cc1-3738-a8c6-00b9c3ef7fda | -5.898 | -44.73151 | 2025-10-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aa2b00bb-2124-3259-b600-b58729f35c8e | -3.86938 | -44.12032 | 2025-10-13 04:21:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4b6c2d80-58db-32d3-bbb9-17bad2d890b8 | -3.27652 | -53.27498 | 2025-10-13 04:21:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f42ee8b9-a9bb-34fa-96d6-d5acd2d697b0 | -4.40453 | -43.51394 | 2025-10-13 04:21:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9f9ddb70-9dbf-331b-bbf6-32500b21e23b | -5.48326 | -44.65894 | 2025-10-13 04:21:00 | NPP-375D | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fde55a1-fb02-3751-a514-84f64b344e70 | -3.81437 | -45.75824 | 2025-10-13 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6fc9e071-7185-3f41-8a30-ee1b18bc9cbb | -6.4817 | -42.05685 | 2025-10-13 04:21:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 646911a6-d99b-3c48-9f24-d5f4d4721fcf | -4.61832 | -45.77578 | 2025-10-13 04:21:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94d1bc2f-b33d-325a-9d73-ff7d6cf81fba | -2.79107 | -49.61971 | 2025-10-13 04:21:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60ebae5a-ec9f-38df-b80a-ebc2a8e4f41f | -6.21718 | -41.56607 | 2025-10-13 04:21:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 62b9086b-3919-3459-a5f7-833a832b4f8b | -6.48111 | -42.06075 | 2025-10-13 04:21:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 20d13950-e7ba-36e7-a22b-9a8a99348c3b | -5.83398 | -42.31148 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 410b00ba-3310-3a9d-89e7-838cfdc81d9b | -6.22093 | -42.48996 | 2025-10-13 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d5535ae0-ac65-3470-8782-b36268cea672 | -5.83226 | -42.29947 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 6918ae10-43cb-39f2-99e8-e1fa55bd3f26 | -6.08325 | -44.47604 | 2025-10-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5ebe87aa-4288-327c-9835-0e8e6c099231 | -5.93267 | -40.89161 | 2025-10-13 04:21:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 141f7d47-fa84-34d6-b970-7b6cd2ed592c | -5.93857 | -44.21511 | 2025-10-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 036c3d55-971b-3390-8d43-78b236945150 | -5.91849 | -45.42723 | 2025-10-13 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c8c3ecc2-ffde-3999-b9d7-04ce46c515d9 | -3.60519 | -41.62561 | 2025-10-13 04:21:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 962cee69-8e52-3193-89cf-8bef1e454591 | -5.62004 | -42.71956 | 2025-10-13 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 570a4a42-9cef-37b6-b675-3685db1b1f54 | -4.47663 | -44.94103 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 1cdac873-d5b3-38ef-8ab8-96fd37bc4809 | -5.33615 | -44.83825 | 2025-10-13 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea319907-6192-367b-a091-9fd6ddd65a60 | -3.39182 | -50.14831 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd62ac2e-b8de-3a30-8288-be0368ec3a10 | -5.84155 | -42.30871 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 552c7cba-6df6-34b4-8ed2-aeb248b15c81 | -4.91248 | -41.52971 | 2025-10-13 04:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d60f4bcf-4502-3a0a-a864-3e14fca0a83a | -5.4989 | -43.78531 | 2025-10-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 470d00b2-2f1d-36a4-8f19-a5c46b369256 | -1.89786 | -51.01218 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 510fcd82-53d8-39f3-8f5c-6f38ad1ee65d | -6.42072 | -42.54978 | 2025-10-13 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| d937800e-d403-3767-8579-cf43591b41cb | -4.86243 | -45.73325 | 2025-10-13 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 19efb7db-9e2f-37c1-99b3-0c779932effd | -3.73013 | -45.40863 | 2025-10-13 04:21:00 | NPP-375D | SANTA INÊS | MARANHÃO | Brasil | 2109908 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2cf72ab3-ac3d-340d-93d9-07090b3c3466 | -3.81379 | -45.76189 | 2025-10-13 04:21:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4bdc8a00-21a8-3779-ba21-8c8fc7f5f10e | -4.28561 | -48.57837 | 2025-10-13 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b831461-2312-3863-8b3a-911feb173101 | -5.10898 | -43.20346 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 252d4234-483f-3e75-8729-bb85d24f69bd | -4.86919 | -45.73431 | 2025-10-13 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc4f857-1623-30e4-aa2a-1babf31bce11 | -4.88855 | -37.50237 | 2025-10-13 04:21:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 5a88bc80-745e-37ee-b6cb-57170d444a08 | -2.88402 | -50.73996 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e1fb8c78-75ab-3b20-a17a-c9961c5b885d | -4.01797 | -47.35114 | 2025-10-13 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61d84951-0591-3eb5-a898-16c27f7fda5d | -6.76564 | -39.07328 | 2025-10-13 04:21:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 832f96b5-bee6-336e-b1dc-eefd0a7f7000 | -6.40507 | -42.53588 | 2025-10-13 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8aef5fc2-dff0-3575-b9a0-c2164a046621 | -6.23419 | -43.0116 | 2025-10-13 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 48e9e18a-2e66-352e-9ce1-71c287e377d4 | -2.5317 | -47.79787 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7380f26f-d7a4-3d18-aeb8-d7357f0d4fbc | -5.58417 | -41.1044 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 18b6a3de-6d6e-3e37-a12a-69dba8d5693b | -3.6102 | -42.74286 | 2025-10-13 04:21:00 | NPP-375D | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c44b5ff0-fe8a-3557-91f7-00a16182fbdb | -4.8353 | -43.35017 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 22fbcf88-bfef-3ef8-bfe5-a5972c751f5b | -2.88069 | -50.7312 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 016f614d-f10b-35fd-9c89-2924caf3c9d5 | -5.30464 | -44.26805 | 2025-10-13 04:21:00 | NPP-375D | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd2baa2b-f9d4-38b6-b218-6add49f465f5 | -4.18167 | -46.23071 | 2025-10-13 04:21:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4cac1b50-1b46-33b5-8fa0-4f0ab2e73851 | -5.45898 | -43.39568 | 2025-10-13 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6270fe12-14f9-3e0d-ab1e-253c6c03508a | -3.66355 | -50.95153 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9840d368-efba-3b52-a9ea-dbb44f2dbcfb | -3.40553 | -46.89833 | 2025-10-13 04:21:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41373267-da97-3c67-8b0c-7d4bfb10b2a6 | -3.85193 | -50.97352 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c11ce7b1-f167-301e-8215-445e75cda4e6 | -2.52792 | -47.79726 | 2025-10-13 04:21:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 295b2e57-3cff-308f-924c-3c089152c7c3 | -3.27285 | -50.05428 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 959e40f5-266a-3a0a-9db4-4a2f295c03c4 | -5.41376 | -40.98046 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8077edb0-a8a6-309a-a918-1d5a48052889 | -4.47487 | -44.93727 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 12d7c514-997f-36ef-b49a-49473c191a38 | -3.09301 | -50.38148 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9fd23ce7-3e27-31e8-b56b-fd172250d805 | -3.42446 | -44.30238 | 2025-10-13 04:21:00 | NPP-375D | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3f39143-2114-3852-99d8-53d181dfc3ae | -6.17402 | -42.54091 | 2025-10-13 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 88cd02af-f09f-3082-b4f3-6135904c1e9f | -5.56796 | -45.27488 | 2025-10-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9674f9ec-149f-387c-9663-bfce0e8a3a05 | -2.24607 | -47.87207 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 603d58d3-afef-3efb-abb7-e7e69d7dbfd5 | -4.662 | -45.69771 | 2025-10-13 04:21:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ccb8a0f9-5523-3e44-95c8-289985a2a00e | -5.06462 | -40.47186 | 2025-10-13 04:21:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ffa6825c-b168-3e82-bbcc-fa2ff86800d2 | -6.21747 | -42.48935 | 2025-10-13 04:21:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| bc8408db-2b92-3e5f-abf0-99ecaf5cafe9 | -6.24556 | -43.00594 | 2025-10-13 04:21:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 23.3 |
| ff87ce5f-c4db-3e00-9c16-b9e53b0cc6a3 | -3.46364 | -42.67633 | 2025-10-13 04:21:00 | NPP-375D | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9db8dc14-6d66-3307-a52a-49c8f2a7f2f5 | -5.8867 | -41.3885 | 2025-10-13 04:21:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4d2343af-0ebc-3d3f-a308-9cc09f38cad1 | 1.90501 | -55.68313 | 2025-10-13 04:21:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 684ee605-7751-3fce-9c36-dbe6aa83fbd5 | -4.83817 | -41.47844 | 2025-10-13 04:21:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ad638e78-e386-306b-89f7-94618aae08db | -3.17025 | -40.15517 | 2025-10-13 04:21:00 | NPP-375D | MARCO | CEARÁ | Brasil | 2307809 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fe3c25a5-2eb5-3a70-9055-8bd413b0e305 | -5.51399 | -43.46999 | 2025-10-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3798e6b-7d54-3f58-9813-f6726a6a1050 | -4.47775 | -44.93406 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a18d36bb-6f6c-3128-b462-2807e2204f7c | -5.56518 | -45.27085 | 2025-10-13 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 7cb3dbe0-eacd-3c08-bbb0-bbc1dde17203 | -5.63207 | -42.68717 | 2025-10-13 04:21:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e08cfd61-da82-3a2f-9ca2-64a0ec520911 | -3.34568 | -42.15818 | 2025-10-13 04:21:00 | NPP-375D | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1f51c043-f9ed-3d8c-ae4d-e5ce0ac72663 | -5.3262 | -42.56856 | 2025-10-13 04:21:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 61eeddbd-f73c-3d5d-b2cf-66ddd98ea9f3 | -3.83367 | -50.97042 | 2025-10-13 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d95fa2ae-728c-3dd0-83f6-acaa4d820707 | -2.24989 | -47.87269 | 2025-10-13 04:21:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 596d98a9-b80d-35ca-9e9c-5b94372f61b5 | -4.48108 | -44.93459 | 2025-10-13 04:21:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a7bb5e27-1817-3230-86d8-ae39da90410b | -3.09373 | -50.37712 | 2025-10-13 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| c53d56ee-9384-35ab-893e-d51e2b00724f | -5.10953 | -43.19989 | 2025-10-13 04:21:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 88fca998-d202-3efe-955c-1a0e03db3168 | -6.38333 | -41.77405 | 2025-10-13 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5b163005-f603-318b-abcd-9ebed849e62e | -6.07246 | -44.31074 | 2025-10-13 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7719daa8-752d-36d9-bdd9-f9986c5aac2c | -6.04158 | -44.13822 | 2025-10-13 04:21:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6656171f-c663-3a13-a191-43a71d0f8c95 | -5.65584 | -43.60797 | 2025-10-13 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca039abd-ffd0-3392-a763-948a07ba49b7 | -3.61279 | -48.91811 | 2025-10-13 04:21:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7c62de9d-6468-30bd-8800-6219a2724329 | -3.61866 | -41.63165 | 2025-10-13 04:21:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1d14e9d5-871d-37ba-ac58-7068921bc22c | -3.58521 | -47.28259 | 2025-10-13 04:21:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |


[Clique aqui para ver as próximas entradas](README17.md)
