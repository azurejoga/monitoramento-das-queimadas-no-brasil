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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 43fc5d07-ae8c-3866-b0d0-a5807c768d45 | -4.71637 | -48.33236 | 2025-11-08 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8a2f2f26-9ac0-3927-8671-9b22288ef617 | -3.468 | -48.97544 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a5d6eadc-a1bc-3687-a4e6-29fa808d25a1 | -4.68575 | -46.40288 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c6de6ad8-52d0-3eea-a177-8e3968ca1989 | -3.14774 | -50.61307 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78a3cbde-74ed-3b09-bfda-4c4670efee1b | -2.42418 | -48.59674 | 2025-11-08 04:36:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 999be68d-ed9c-3672-bb8d-4e9e1d8126c1 | -8.02623 | -38.53275 | 2025-11-08 04:36:00 | NPP-375D | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 5047a6a2-5dfe-3a40-98cc-dd5d165a9647 | -8.33441 | -46.25468 | 2025-11-08 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52d20ab8-8eb7-3804-b089-c5066f5bc15f | -3.45434 | -48.81973 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| edb510ac-fdea-3707-8a83-11335c85448c | -7.03824 | -46.98396 | 2025-11-08 04:36:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| c1af8b9d-a834-3157-83a1-52dbdb001eab | -6.18901 | -44.53001 | 2025-11-08 04:36:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ef1798b-74b7-398c-ba22-4fff77f3a75a | -4.61691 | -44.38399 | 2025-11-08 04:36:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b804f22-9f74-3d83-bf6e-3601ca85944c | -3.0931 | -50.3276 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b3daba2e-5b8a-331e-931f-7f5bd470ac5e | -2.8506 | -50.46561 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3c3447da-0f16-3a7c-8387-10f05101c37d | -3.45542 | -48.8348 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ec9d3384-1cc4-3356-958d-60f1c2e3d4a9 | -3.31253 | -50.12761 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 464ca439-0025-384c-8da9-4b2b6181f97a | -4.81172 | -45.66011 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c93d6bed-0518-3b1c-8478-76f5a7493403 | -3.06224 | -49.37325 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4efabacb-84f4-3b64-b0d5-137246456bc9 | -3.29226 | -50.03728 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62d2f938-9a01-39da-903d-0ecd4b263b02 | -4.47037 | -43.21444 | 2025-11-08 04:36:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8c6a9042-5975-3752-beae-6f783a724d17 | -4.4265 | -47.60246 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0499e06d-01f5-3472-811c-034a36af16f0 | -5.61628 | -45.0474 | 2025-11-08 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33324475-9b1a-305f-81b2-3502670dcf45 | -5.74889 | -40.79462 | 2025-11-08 04:36:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2d97ecf9-9d65-36f0-be7b-b60adc3c118f | -2.72177 | -47.40428 | 2025-11-08 04:36:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a71a33ae-816c-3274-ab16-f7e3ea394c92 | -3.30819 | -50.05227 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0652572a-d87f-3c2d-b5f4-5fc505427537 | -6.37196 | -41.74511 | 2025-11-08 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6a6025fd-0a9e-3617-95df-892d07aa95ea | -3.25645 | -53.27557 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bde27717-c264-32d7-bf99-13786a741ba3 | -3.63105 | -43.65232 | 2025-11-08 04:36:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 062d0630-d4cb-3fb5-9ec0-f52e1eab42ea | -3.98254 | -49.86933 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 11ef4d37-f94e-3103-8156-9c2f104d1de7 | -5.75215 | -40.80462 | 2025-11-08 04:36:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1bbe24c4-68d0-3de6-877b-2549667f51a9 | -3.85471 | -47.40612 | 2025-11-08 04:36:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 170c01be-f9f2-31e3-85f6-ab230cee656a | -2.51147 | -48.26404 | 2025-11-08 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eeacd79c-6176-3241-9c8a-580ad2d7aa49 | -3.12316 | -50.14132 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ae0fc2e-1a46-3efe-b1fb-f713216f5d25 | -4.84552 | -45.62348 | 2025-11-08 04:36:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42fc2db0-5cb2-37eb-bdd1-39e4ed0fba3c | -3.64533 | -45.88591 | 2025-11-08 04:36:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ff408f3-66ee-39a3-ad1f-ab7d8c3127f6 | -3.40828 | -50.27158 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2f3d303f-c4d4-36eb-9e6d-c88291f06454 | -3.8329 | -49.81359 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f64f7530-7aac-3ce0-a8f4-6a4e22644f21 | -3.25677 | -52.90881 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f38dadef-a079-3c86-bf03-f97afaa24899 | -2.61779 | -49.22307 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dea78f72-a95a-30ce-9980-58449bbd83cf | -2.84438 | -48.10569 | 2025-11-08 04:36:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f3117c2e-b7bd-39c3-8758-c6b08b44ada4 | -4.69246 | -46.40392 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| af8f1535-9894-3aba-bafb-bcaa9f7cbb58 | -6.8533 | -39.11377 | 2025-11-08 04:36:00 | NPP-375D | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4e90fa4d-c511-3c29-b0d7-8cddda1e6037 | -4.3828 | -45.68196 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e079a5eb-ea37-3cc1-9e5e-14ff5d338ba9 | -6.47245 | -43.22923 | 2025-11-08 04:36:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5311959a-f019-31ef-a901-ef992c021ad8 | -4.01092 | -48.04463 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cc6b0910-37d4-3b7a-871d-8399fc63f91b | -3.32026 | -49.13482 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f07984f-ba16-32f5-94bd-711d36667ff2 | -3.30722 | -50.16022 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11d7bbcd-b7d1-307f-b769-d7cc3a65b5db | -2.89337 | -53.1297 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c4f3df80-2275-32d1-8336-0a3fc2dc28de | -3.14693 | -50.29339 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86141c0c-b3e3-3b45-8a63-45ae7c33bc51 | -7.46244 | -46.63818 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9043806d-32f6-3bf5-9885-fa25ae2e3b0f | -4.29776 | -45.69192 | 2025-11-08 04:36:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8844226d-3198-3300-84ad-31159b98546f | -4.11114 | -48.01032 | 2025-11-08 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9896beec-97dc-3d2a-9cfc-a2f5ad980475 | -2.6839 | -49.55197 | 2025-11-08 04:36:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4694d2a2-74f5-33dc-8602-279b07a5bf47 | -6.22414 | -47.0131 | 2025-11-08 04:36:00 | NPP-375D | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a5d1ceff-ef48-340e-9b30-41f5072174af | -5.84628 | -43.4109 | 2025-11-08 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a454964-6d2a-3861-ab2f-cd89865c772f | -3.43652 | -45.59483 | 2025-11-08 04:36:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a6c64ac4-4c0f-363e-8a4b-7d720529cf8b | -2.62638 | -50.07232 | 2025-11-08 04:36:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a587b7bf-e6c0-35b6-aa62-da9cbb89171d | -3.49578 | -49.95704 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 084714b4-4d8c-3e23-9f55-cf6dbd43d418 | -5.7484 | -45.87638 | 2025-11-08 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f6dc3ee-205d-3543-9c44-a7c3faddf55d | -3.15213 | -50.60933 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1126c414-9d5c-3620-b209-ad17076edf58 | -4.90886 | -45.10125 | 2025-11-08 04:36:00 | NPP-375D | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 751b57a8-1441-3052-b293-7faf426e9922 | -3.35437 | -45.29307 | 2025-11-08 04:36:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8bf3c15d-ba85-3551-afcd-47deecaa5caf | -4.69757 | -45.85743 | 2025-11-08 04:36:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2563f911-37a3-358c-8373-bdff78df4f1d | -2.82623 | -49.83159 | 2025-11-08 04:36:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e8e930be-6942-3afe-9286-07251c748bcb | -5.84554 | -43.4157 | 2025-11-08 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 41d0a118-cd64-3ec4-9a1c-736ea8416540 | -4.95103 | -45.55145 | 2025-11-08 04:36:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f76aa205-1c8b-383a-b4d9-f97cd93ae5bb | -8.75569 | -44.23185 | 2025-11-08 04:36:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6426f8dc-b9e2-3633-bd35-c1f879fd64e3 | -5.37209 | -44.73335 | 2025-11-08 04:36:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a3943d4-91c5-35b2-9cb5-b96df8d0e086 | -3.13006 | -49.10205 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bfb34f5-a977-3814-9285-18db3ca9239a | -3.32085 | -49.13111 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dca74604-aebd-353c-9ea6-655d1e1bdbfc | -4.80148 | -49.60515 | 2025-11-08 04:36:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0dda4f0-8cb6-3c03-9473-b7237685d052 | -3.34638 | -53.22191 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 680ef4e0-2123-34f3-9f60-7d7778866756 | -3.78147 | -49.84146 | 2025-11-08 04:36:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bc54ea4-a30f-3c15-84ea-7918b0b1e3f5 | -3.33419 | -42.35535 | 2025-11-08 04:36:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 74b2ab8b-eb53-3edf-895b-f00d6b7dfb98 | -6.01265 | -49.13416 | 2025-11-08 04:36:00 | NPP-375D | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c9791b9a-b5bc-3885-8b25-ad02a3b06a85 | -3.17333 | -49.24254 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 108d6d59-0888-3ec1-b9a0-6dea65112359 | -2.9656 | -44.5951 | 2025-11-08 04:36:00 | NPP-375D | CAJAPIÓ | MARANHÃO | Brasil | 2102408 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12941360-320b-3c45-96b9-4eda83c1f9e1 | -5.01135 | -44.6031 | 2025-11-08 04:36:00 | NPP-375D | SÃO JOSÉ DOS BASÍLIOS | MARANHÃO | Brasil | 2111250 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fbe33146-5255-3cbb-9139-a87330242991 | -5.78458 | -46.5613 | 2025-11-08 04:36:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e4cbcf53-08b0-30bb-963c-9cca99261ebc | -5.58969 | -47.15776 | 2025-11-08 04:36:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20cf8704-e8c3-3fb3-836d-15cb9b4b9278 | -5.05478 | -43.31551 | 2025-11-08 04:36:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03d52cd6-041f-3528-8eb4-650ab98a87cb | -2.92979 | -49.5017 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c841d889-2cc8-3d75-9320-bf42d5265709 | -3.44958 | -43.15297 | 2025-11-08 04:36:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9eaaf58e-26ad-3f9f-b80b-9feb29bf25b5 | -3.0967 | -49.2234 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92ee8545-7793-3833-9d0c-c44e039a034a | -3.33505 | -50.10209 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17be2ee9-d93f-3a59-b3ce-7ea71d6d14fd | -3.42929 | -50.11972 | 2025-11-08 04:36:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f5862358-52a3-3391-be06-d7d81abb822c | -3.52867 | -47.54238 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9b3e677f-22de-3720-9435-5b94480933bc | -3.53145 | -47.54628 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5f503419-ea1a-313e-b76e-b6710439a80b | -7.11342 | -46.48097 | 2025-11-08 04:36:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 91b4b7a2-b5d0-35eb-8118-868b8a9a6390 | -3.26475 | -45.9767 | 2025-11-08 04:36:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 58b3e560-b415-3dac-a665-9ac5ddf42144 | -3.14992 | -49.21184 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a83bee41-88ea-314c-a5b4-02520dfc274a | -5.72477 | -43.52756 | 2025-11-08 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ff4c721b-5ce9-31e0-adfa-cac692ac0ae7 | -3.98333 | -46.02948 | 2025-11-08 04:36:00 | NPP-375D | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f7d408e6-2241-3abb-b9e6-9c08f923295f | -3.32266 | -53.36375 | 2025-11-08 04:36:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 56590037-6f9a-30dd-a9c0-bd0e2115250c | -3.04786 | -50.25778 | 2025-11-08 04:36:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6d2fa80a-5450-390e-9133-e4d159ad6ee0 | -4.921 | -44.56174 | 2025-11-08 04:36:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff3f825e-6690-39b9-8abb-d8588dd0cedb | -2.62066 | -49.2274 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b6c65a9a-792a-378b-a8fb-8646881bbe68 | -3.32369 | -49.13537 | 2025-11-08 04:36:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 132eba3f-90e2-322a-9665-5aa8b10e283f | -3.53254 | -47.53944 | 2025-11-08 04:36:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 6ccb70c8-6114-324a-b4b7-3a558d7bb8e2 | -4.28234 | -46.41256 | 2025-11-08 04:36:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 211e69c9-b66c-30f9-aabb-883d2fab05f3 | -4.40748 | -42.32537 | 2025-11-08 04:36:00 | NPP-375D | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |


[Clique aqui para ver as próximas entradas](README21.md)
