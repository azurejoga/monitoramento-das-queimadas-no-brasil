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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2089a02b-88d3-399a-a1dd-92f627b2e6c5 | -3.25457 | -50.2033 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ac5a2e2-e6e7-3c0d-99dd-ee871c9c10a8 | -3.25386 | -50.20776 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 597f2560-2f50-3e62-a521-8406edfcfd0c | -3.25368 | -50.20107 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cb7493e8-6df1-3619-8dd1-95196239a169 | -3.25295 | -50.20539 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eef15bde-50a6-396f-b30a-be3e99f9467f | -3.25015 | -50.20256 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cbfdc7c6-67ec-374b-afd6-5a7b24f82656 | -3.23455 | -50.18685 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eacff0d0-a2ff-3290-a725-e51a55b3bf9c | -3.23386 | -50.19117 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6fc17e65-7e2c-3216-bdff-deba4cc09b4b | -3.23012 | -50.18623 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 02179e1a-5453-3028-a5af-3d21dfc0c802 | -3.22943 | -50.19052 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b3bf2abc-e7d8-3170-bac1-b4369de072f9 | -3.219 | -50.17103 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f94770cc-0082-3630-b767-8b8fa0e1e978 | -3.21459 | -50.1703 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1122f20b-82cb-39f8-a3c2-6c175814627f | -3.21389 | -50.1746 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f6d355d-ac34-35dc-bdf4-1397c92b6f64 | -4.816 | -50.88967 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 37e0af7f-d704-3621-b1b5-7cc8cd61d2c1 | -4.72856 | -50.79385 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68df65e1-946a-30d8-b6e8-e87e78cf6cd4 | -4.72406 | -50.7932 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2194b96-bc66-3b50-862c-7e6becb97bd1 | -4.65738 | -50.76957 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 886aabb9-f5ce-3ead-a3fc-0839b60489b4 | -4.65663 | -50.7741 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7e5cae98-acb4-3168-9769-111b9f6dd372 | -4.6265 | -50.65081 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d802269-8466-3d68-bdba-7eb7331dc7b8 | -4.62206 | -50.64994 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6fde535-e465-35cd-bc1d-ad6e8ce15378 | -4.6213 | -50.65448 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7a9edf91-aca1-3f71-b654-9d3c86e9d737 | -4.41655 | -50.56153 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 791e6625-47ec-3fc7-9aab-8b137003cf39 | -4.40643 | -50.73221 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 693eb2bd-151d-39b5-ad21-ec75e14df3b9 | -4.40569 | -50.73668 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f1421f0-1db0-39f7-9b79-1e7503464ebe | -4.4012 | -50.7359 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a2f32109-f10c-38a4-bbec-651845ee51fe | -4.39739 | -50.51994 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8a392c00-8328-3aa6-b2bd-07c0f86191f0 | -4.39669 | -50.52428 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87aaab5e-1d74-33fa-a8a4-52422b197ee2 | -4.39599 | -50.52863 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42cd9c95-7f32-35e6-8f0c-27a9702f9d2e | -4.39578 | -50.52238 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72c0acf6-bb08-31ec-b184-c8fd24cc2e8b | -4.39505 | -50.52672 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60bf3f62-b470-32fa-84ab-527c7823526c | -4.29802 | -50.73448 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7be28830-9775-3974-80a6-1d4bdb597ec9 | -4.29727 | -50.739 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b64c166a-c8ff-30a2-b16a-8025f5fa1387 | -4.29352 | -50.73368 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9cefc88f-598f-3514-bb75-d57a715f4239 | -4.29276 | -50.73826 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e861c64-c894-3f1c-a7e0-a423db5a84f0 | -4.23025 | -50.63307 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 70cead45-ecab-3b86-9b26-b426ab9a6fd0 | -3.81916 | -50.23498 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c7bde1e-1135-396b-9d8d-57629bd43687 | -3.81846 | -50.23918 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb754f78-380c-3f2d-83b3-0675897a1497 | -3.77794 | -49.83216 | 2024-10-26 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f6327834-74bf-3e4c-a1bb-c4ec877ff372 | -3.77432 | -49.82761 | 2024-10-26 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 754ffdfa-3ada-3c8d-9a97-ea122d90a1e9 | -3.77366 | -49.83155 | 2024-10-26 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f8d1235a-b27c-36ab-a840-767bed824334 | -3.70037 | -50.16572 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 390e6eaf-b008-37e8-9ec7-aeab798adb5d | -3.69612 | -50.16299 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2d85d776-ef2b-317c-9261-e43fc0024bc2 | -3.69601 | -50.16495 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0812d18e-728b-3050-b29b-353c09eec0d8 | -3.66648 | -50.12553 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f78366a7-b626-365e-995c-50ea4106f8dd | -3.66279 | -50.12071 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ae187a50-ef1a-3595-a5ba-90e52dcfd7e0 | -3.66212 | -50.12483 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c212260-1eda-3a70-8418-22e35e138ebe | -3.65842 | -50.12003 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f59a7fa6-b47c-3b28-a1ce-6bf653aa787c | -3.65775 | -50.12415 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94c1dbea-f6b4-3634-963e-05a6961189e3 | -3.65707 | -50.1283 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0346a5e0-844d-3404-b41d-d3e7b7e8b501 | -3.65405 | -50.11934 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1d282dea-8990-34f1-b325-e2971e55ccf3 | -5.11785 | -49.51865 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2bd8d8b-7a42-3021-9f14-66e44ae496d0 | -4.99033 | -49.86707 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2bd95694-f391-3bae-8bbe-33627f8de518 | -4.97562 | -49.77445 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d6311833-fdad-38f5-80c9-272074c5b16c | -4.97207 | -49.77001 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c16af473-d3df-31a1-988a-9434e64eed26 | -4.97144 | -49.77379 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 21cf2249-a25b-3693-bad3-98ae6e944ca2 | -4.9684 | -49.89511 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bf0cde78-56fa-36be-9454-737b004dd94a | -4.96776 | -49.89897 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 71ecd31e-6ddb-32d9-8a41-30c0ec3b220f | -4.91384 | -49.83172 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51a3906d-3741-3c55-b71e-4f0b680ffae5 | -4.84131 | -49.87862 | 2024-10-26 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 22ab3e6f-f220-3694-ad51-0296b6f56494 | -4.64136 | -49.36332 | 2024-10-26 04:17:00 | NPP-375D | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 451acc5b-0078-39cf-b59a-d582e020b6f4 | -4.5862 | -49.49306 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eeb7b000-79e9-3a3d-b528-0ac8caf5bf13 | -4.43815 | -50.12976 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aee9d7e9-1c9f-33cb-a122-e70da489a03e | -4.18424 | -49.41299 | 2024-10-26 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3b74bd7d-f2a2-3ac1-9b50-7c0ffef7b7e5 | -4.09298 | -49.99262 | 2024-10-26 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 786f8221-4bd7-37be-8139-22397a436328 | -4.006 | -49.41578 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5a7e4c19-778f-3405-985d-763fbf3717f0 | -3.96094 | -49.89788 | 2024-10-26 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ecb7221c-0cb5-32ac-ab3e-855aed5c5310 | -3.95912 | -49.89495 | 2024-10-26 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea7d0b13-367b-304b-a0ed-ddfa159fd28f | -3.95848 | -49.89897 | 2024-10-26 04:17:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6761e5b9-0640-32e9-8efe-2c940e280541 | -3.92036 | -49.38191 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6ad39a04-fe3d-3a7a-9732-250165c14263 | -3.91622 | -49.38127 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1258940a-4374-3338-b548-ce1bf9b746b3 | -3.91563 | -49.38496 | 2024-10-26 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4fdffc78-4826-398b-a69c-e9391b668f5e | 2.30893 | -50.76428 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 25dfe79d-d21c-31e2-ba48-3970248e30e7 | 2.30836 | -50.76341 | 2024-10-26 04:17:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6c1fb254-d6b9-38c1-b4af-20c3bdf8903c | -2.24227 | -50.53531 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9df35664-09c9-373d-ba69-3b07687fe895 | -2.23382 | -50.52914 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2ec8072f-b35b-35c6-89b9-f9b0446f1534 | -2.22701 | -50.7107 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e70d0624-5a5c-3037-9345-4400c7ee32e4 | -2.18708 | -50.49751 | 2024-10-26 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8010eee7-6a69-3bed-9b64-45dc7c72e8c6 | -2.18632 | -50.50223 | 2024-10-26 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 91185779-a73f-3a9d-80c2-c8cf99527269 | -2.18174 | -50.50147 | 2024-10-26 04:17:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b65042d-d1a1-3b0d-9fb0-4bf4312301ea | -3.60805 | -51.46946 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a27e7834-9d37-3c8b-a011-653877df1853 | -3.58678 | -51.21315 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 13aab704-ce1f-39c0-afce-4652d03ebb46 | -3.58595 | -51.21817 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b33a5b9c-93a2-3a07-9954-f9c04350e298 | -3.58288 | -51.20743 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| 6dc30f93-f186-3110-961d-199f5c2efc83 | -3.58206 | -51.21241 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 26.0 |
| e3c13b3c-2458-3538-9335-72d88f37844a | -3.58123 | -51.21742 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| d792466a-8d53-3d69-8995-58a32e29fc83 | -3.55976 | -51.43706 | 2024-10-26 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ee7413df-500c-38ce-917b-3540bd109db4 | -3.51614 | -51.01859 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1487c57d-f63a-3717-91a4-027292d62203 | -3.51535 | -51.02345 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 27f443e4-58ef-3f94-bbe0-223de41e9fc3 | -3.51148 | -51.01785 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 269a489c-e466-3483-9f5c-4bf4eab12bd0 | -3.51069 | -51.02269 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 96670e27-59f9-38e4-9f59-74a92faaee6f | -3.38831 | -50.96573 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca511c9f-30d6-3a40-b751-914544707066 | -3.33823 | -50.81892 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3230cc2b-f843-3567-b2f4-b07ad2b0c27c | -3.33746 | -50.82363 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6ffd245-961b-3755-b492-5f95f5e3d00c | -3.33363 | -50.81813 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fab817fe-70dd-3070-b5a7-4ab9a31f1660 | -3.29324 | -50.7485 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbfe15ef-e07e-3559-b458-fdab7ab12655 | -3.27245 | -51.07498 | 2024-10-26 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81b4414d-98e0-3093-9676-b8bff4cd946b | -3.26597 | -50.77417 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| df3a6528-b91e-3e56-8f1b-12a4f9321d0c | -3.26559 | -50.77283 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c9dbf15-d575-32b8-b027-68b1c61d7424 | -3.2648 | -50.77753 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c774d99e-b22e-3512-a994-1a3970c00902 | -3.26138 | -50.7734 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91022c72-649d-3023-bcfa-d262e937a23c | -2.69867 | -51.79284 | 2024-10-26 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README45.md)
