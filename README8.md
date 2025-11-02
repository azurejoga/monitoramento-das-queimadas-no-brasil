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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4aa0921d-a4be-3e4a-b2ba-00d4a59e19fd | -4.54409 | -46.02353 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bee154a9-03fc-3c35-a648-6cba2ce9b02d | -3.82827 | -50.48945 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6acce7e7-c5e6-379f-8a68-0cc6fcad0a93 | -4.71605 | -45.69527 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e32786-6ead-3c1f-bf3d-82dff165972d | -3.23206 | -50.58271 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91202fe5-104b-3364-afd3-96c6b0759be4 | -5.03318 | -43.61744 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| bfb89d74-fafd-307d-8f12-5b7a6ff11fc5 | -4.56426 | -45.69347 | 2025-11-02 04:18:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84958b9d-2f75-3f1d-9db2-7e1b0fa202be | -5.07196 | -43.67306 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 48cd5e5e-cb2c-3484-a278-ac7300b752f7 | -5.13173 | -43.37649 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5de813bb-ed60-3faf-ac40-58a647099115 | -5.17592 | -44.25014 | 2025-11-02 04:18:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67449e10-1e0d-31aa-995b-0193244fb7bf | -0.68597 | -52.3709 | 2025-11-02 04:18:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0cfbfa2a-7770-3f05-97ec-e825a8aac2d2 | -4.12247 | -49.16561 | 2025-11-02 04:18:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0c6b1b0-d50c-394f-af07-2926cc382417 | -4.01964 | -50.45674 | 2025-11-02 04:18:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 34861061-c6f9-370e-baf4-08f25435627b | -3.80874 | -52.41536 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4456eb89-f66d-39a4-b8fe-0f9d451479d8 | -3.65387 | -50.71041 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9f16bf73-2cf3-347a-9dab-8b77d86d2c7f | -4.63953 | -38.56406 | 2025-11-02 04:18:00 | NOAA-21 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 538157a0-4ef3-3229-9f20-4d15204363ad | -3.45295 | -45.5724 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e57b38b6-0a2b-3b78-898c-808938acafe8 | -3.42783 | -45.90811 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| be0e544b-4364-3a85-86d5-bf22798715fd | -3.24436 | -50.79842 | 2025-11-02 04:18:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f1240fef-0e06-3bf1-adce-53f55e78af49 | -3.13233 | -49.23992 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd15e7e3-4499-3898-9ca4-8a06f4fc7f53 | -4.67561 | -44.61915 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0d8fff4-3559-3728-9f38-241e71245ce9 | -3.80291 | -46.1116 | 2025-11-02 04:18:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a67a9bf4-5a35-32f8-862d-a0155bfac49b | -5.39466 | -41.22004 | 2025-11-02 04:18:00 | NOAA-21 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 73c7e190-da45-373e-9f4b-fcb847cc7921 | -4.68222 | -44.62017 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fbf3f6eb-010b-31ac-9cf6-c49be31bc279 | -3.14524 | -49.42081 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 51f905f0-c875-329b-bac5-fcfe1afdc42b | -3.27892 | -46.50901 | 2025-11-02 04:18:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0b64948-0cfa-3296-9180-33ff0fcc2467 | -4.14099 | -47.33058 | 2025-11-02 04:18:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7dbb4537-07cd-39c0-bfce-16bbcdf23b8a | -0.84509 | -48.61538 | 2025-11-02 04:18:00 | NOAA-21 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cedc5cd6-2519-302d-9176-8d87d99f2af7 | -1.41894 | -55.23492 | 2025-11-02 04:18:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f937335f-39ba-32fb-bcc0-8991cb7f0da6 | -4.50022 | -45.79146 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| aefa5952-a17e-3d70-b3fd-8d2aa5606e7b | -3.71088 | -53.37621 | 2025-11-02 04:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c91627c4-1526-3137-bbe8-64a9524b1540 | -4.41431 | -48.30441 | 2025-11-02 04:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 312b8c44-eefb-3128-8f73-7925723d3a51 | -3.46587 | -50.22218 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 311781bf-d7d8-32d8-b6ae-c06c0887713b | -3.72427 | -50.05016 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f92f01ef-8807-3bb8-a161-0af61e34db80 | -4.18275 | -47.65234 | 2025-11-02 04:18:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c7134fb-de73-3c5f-8e38-c61a705fb362 | -3.38107 | -52.3693 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a939fada-95b3-3112-a91e-cff32003c2d5 | -1.49832 | -47.80481 | 2025-11-02 04:18:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f466f3a8-7392-3f6f-ae63-0cb13d88f301 | -2.31568 | -48.58673 | 2025-11-02 04:18:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9c3883db-4435-3db5-99e9-bdf73b30fba7 | -3.83276 | -51.31466 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f46caeeb-6446-3d71-8dec-c4828a3f2037 | -3.63268 | -49.89249 | 2025-11-02 04:18:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18398c5b-d305-3904-adb7-01801963bc1c | -4.70403 | -45.87934 | 2025-11-02 04:18:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ac3724a9-f60e-3f70-96ad-43870c997040 | -5.53793 | -40.71227 | 2025-11-02 04:18:00 | NOAA-21 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4a8fb4d9-729d-32b4-9959-cd98cf7b4b80 | -4.22037 | -45.06747 | 2025-11-02 04:18:00 | NOAA-21 | BOM LUGAR | MARANHÃO | Brasil | 2102077 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 453b40d4-d025-3eaf-9d96-8b54eabcde22 | -3.65552 | -50.70863 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b04d3aad-e8b2-3456-9bd4-1218f1ec2854 | -4.18241 | -48.58882 | 2025-11-02 04:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a669a35-6ca1-350b-ba50-ba967b86969f | -4.30692 | -41.44586 | 2025-11-02 04:18:00 | NOAA-21 | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06d3ea72-8ae7-337c-9d91-f48aab22b961 | -4.3197 | -45.6439 | 2025-11-02 04:18:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6257bdc7-188c-3ab3-af34-dbb6dbff5b2a | -5.03649 | -43.61796 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 5b832310-d0f8-3948-b487-aeda3393cf2b | -3.57211 | -54.58594 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ba38901-ff9d-30ce-a6fb-b80d94206da5 | -3.71492 | -45.89151 | 2025-11-02 04:18:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c0a508e2-358e-31c4-9b46-e4216df615de | -4.54428 | -45.79824 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 37ab97d1-5ba2-3da8-bebf-b7026f6569af | -5.06973 | -43.66563 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6adc4a52-2098-3f29-a7bb-325c9f104eab | -3.50549 | -49.95256 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3062ef42-2131-331b-afab-26c91825faa2 | -4.23146 | -45.80533 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf5a105b-47b4-345e-a2cf-bdca84049d8c | -3.0813 | -51.24802 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f8b4933b-10e3-3a63-b880-dc01abce1647 | -2.34718 | -47.54152 | 2025-11-02 04:18:00 | NOAA-21 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4135eb8-8bb4-3f66-9cf3-2609aae965d4 | -4.72677 | -45.69309 | 2025-11-02 04:18:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4755026e-b1c4-39d9-a6f0-23fb8a08c565 | -3.08517 | -52.92184 | 2025-11-02 04:18:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9602c54-a1dc-33aa-b100-e35cb99bd0ef | -3.6584 | -50.71118 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29b83621-e1ec-33b9-ac91-efc72315ff2d | -3.01906 | -53.96809 | 2025-11-02 04:18:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 69ca808e-2e24-3c53-9e5d-7b64986e58d0 | -2.83051 | -49.40733 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f0ad87d-458d-33e0-9c2f-f39344b02dec | -0.6865 | -52.36761 | 2025-11-02 04:18:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a269b445-3a84-3a42-9c1c-efaa10cd603a | -4.56088 | -45.69294 | 2025-11-02 04:18:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bca501fe-3011-332d-b5d5-ab39c63da266 | -3.68865 | -49.54885 | 2025-11-02 04:18:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5494ef6f-e5ee-302b-91a3-ce7c6e29ef70 | -3.83273 | -50.49015 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc32f74f-73f9-3989-981d-410c5d3cf057 | -3.58088 | -51.5595 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 799ab659-441a-3d54-a8dd-49b7144e76bc | -3.99839 | -50.85359 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 16756ba8-72db-39ed-ba88-6d7e88acffff | -3.61954 | -51.4739 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a5924c59-5d0b-3521-8039-78dc7ef9cc17 | -3.50753 | -54.37188 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7e37b3bf-1e70-35fc-a7f2-852089fbbddf | -5.09097 | -37.60666 | 2025-11-02 04:18:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| e2dedc18-f4a4-3cb8-a018-5906ad2ee15e | -4.26633 | -48.71759 | 2025-11-02 04:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 14defdbf-00b2-377a-8896-242d4fa2ce9c | -3.83346 | -50.48574 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a72ab605-9c71-3e3e-a682-e5534edcb41f | -3.90265 | -45.74693 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 96d0d16e-3551-3c01-bb97-c238992b1244 | -3.23467 | -51.48044 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53013228-e9c9-3d32-9472-db40d076597c | -4.87246 | -43.27173 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1494e1d8-7365-3ab0-b166-7887e520ca15 | -4.54767 | -45.79878 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ea6ee73c-d4aa-36e0-ab30-590d71133b2a | -3.52233 | -50.31818 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5af48a05-761a-3b0d-82aa-a892cb0ca312 | -0.4649 | -51.75803 | 2025-11-02 04:18:00 | NOAA-21 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18bc59df-cc44-383b-8026-b0a4282af74d | -2.63328 | -47.30455 | 2025-11-02 04:18:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a204121c-2830-381b-aba9-31edd5eb8c9f | -4.13346 | -51.14344 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d8c51dff-a716-32a3-b2ff-aa5f9c1e41d8 | -2.61178 | -50.00272 | 2025-11-02 04:18:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ff97c5db-b43d-35c4-8354-e08c8850fd43 | -3.56545 | -54.58944 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| de8b3a82-7430-3f53-b75e-f4bab0bc7a33 | -5.12841 | -43.37598 | 2025-11-02 04:18:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3087fce7-ec1c-3c38-b263-bc5968aafdfe | -3.57201 | -50.26417 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 251b16d6-3efe-3443-a21a-8329104de9d1 | -4.23486 | -45.80586 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccd5c085-3cfb-3cf5-a912-4f7d02d1fc1e | -4.13724 | -51.14922 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| f48f66d8-c4b6-3f00-8f98-1f24441687df | -4.30764 | -45.89588 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d5cb8d3-6624-3029-8e45-ba94ffbaac21 | -3.89867 | -45.75005 | 2025-11-02 04:18:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df921ce1-293a-3bbd-955f-b2ca167d6bc3 | -3.38156 | -52.3663 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a8efcd42-7cb1-31b9-9c7f-52c4874e12dc | 1.02434 | -51.19635 | 2025-11-02 04:18:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6f33e98e-41b6-3b89-bb18-97e13b9f395a | -3.43126 | -45.90865 | 2025-11-02 04:18:00 | NOAA-21 | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6a61d7a7-560e-366a-9158-f004144cdd49 | -3.51339 | -54.37263 | 2025-11-02 04:18:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 13c9c78c-4aa9-3109-9085-ea168faac2d7 | -3.58524 | -50.26623 | 2025-11-02 04:18:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 574a3b3f-7324-3eb4-b63b-0d11af825fc4 | -4.67615 | -44.6157 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6183c611-6572-3efe-8584-9ad7d258d02f | -4.52007 | -48.83825 | 2025-11-02 04:18:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bb526008-68de-3520-9733-8a55f30803c3 | -4.58397 | -44.78903 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 76268875-55b4-3fde-8596-c2396d552419 | -4.67507 | -44.6226 | 2025-11-02 04:18:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 715a17e5-a612-30e2-86e6-1744f4d57bf6 | -2.7879 | -49.45653 | 2025-11-02 04:18:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 09965238-dce1-32f3-8509-aecaef4b9bce | -3.82321 | -52.36119 | 2025-11-02 04:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcb82bfb-6914-3511-9c57-886d389cdd86 | -4.13376 | -51.14983 | 2025-11-02 04:18:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 79481f14-9bfa-3a06-b64d-a3237db3aeda | -5.0398 | -43.61848 | 2025-11-02 04:18:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |


[Clique aqui para ver as próximas entradas](README9.md)
