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
| f5192555-75fb-3d55-ac1e-6e8ec7c5d2c7 | -6.25316 | -51.82867 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7ccfdf5-31a9-35a3-a14a-651b698cc9cc | -5.28251 | -44.20106 | 2025-09-11 04:21:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74bdc132-9266-3d81-9db8-06058bdd3620 | -6.2537 | -43.42146 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c2c2a30a-8767-3572-8bac-c488f25c4a5a | -4.65357 | -47.03148 | 2025-09-11 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f9d19249-5f5d-321a-a403-b1892a376204 | -3.64609 | -48.32716 | 2025-09-11 04:21:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 21b5bed3-6398-36af-817f-2084482b2561 | -7.49212 | -48.25578 | 2025-09-11 04:21:00 | NPP-375D | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10613b04-d9ed-3591-bdeb-28a8bbb773e7 | -9.06081 | -45.72231 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18447101-6100-32ee-a0f2-7d13c319a5b7 | -8.0351 | -48.67167 | 2025-09-11 04:21:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a718492e-c534-3688-b658-a322a8745eb8 | -6.44093 | -44.7779 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4a78d966-f11c-3437-b833-3c6a6bb7a962 | -5.10414 | -46.06924 | 2025-09-11 04:21:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8e953769-ff1b-3269-9d48-c71686e3bec1 | -6.63542 | -44.07756 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 31a4c21d-76fb-3256-9ab3-c895795cf355 | -7.18333 | -44.97166 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56d5f073-0462-33c9-908e-aeb263c72a23 | -3.24542 | -50.79829 | 2025-09-11 04:21:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e44bebc8-2671-3de1-86b6-1cc39dc233ea | -8.19775 | -50.10606 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 63515371-8e16-3cba-94fa-a95245eb35c0 | -8.74544 | -47.11736 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6304716d-9d38-3b6e-9811-847f76572e89 | -6.0721 | -44.81881 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4aa2eb84-522e-3c12-a5e4-40e94d6f8c58 | -5.55706 | -43.0508 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64ad02fc-9638-3e1e-918f-1490e07a2e1e | -6.30596 | -45.65998 | 2025-09-11 04:21:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f6684e51-c6f8-30bf-be2f-2e182aaf83fd | -5.19639 | -43.03333 | 2025-09-11 04:21:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c22945bb-dc5c-386a-86a7-a5a4b46dee83 | -4.48361 | -48.11509 | 2025-09-11 04:21:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce2b1544-fc7d-33e7-8e0d-8b8635960486 | -4.7145 | -47.2354 | 2025-09-11 04:21:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de430780-21eb-3b9a-a6ab-79098e4e23f4 | -8.1925 | -50.11239 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b9be6846-b7cf-3561-897c-f2997428de48 | -7.22129 | -45.31342 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4dfe9d12-7a54-3fd9-860f-6839de2e94d7 | -5.77185 | -43.15029 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 34249b06-dd67-3b88-a961-b4ebfccb3981 | -2.78977 | -48.60427 | 2025-09-11 04:21:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 803accfd-4ac7-3046-a0c1-2836153ab2bb | -6.39059 | -43.50461 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 778242a9-168c-367e-8419-38f230acb342 | -8.20119 | -50.11025 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4c80369e-6c57-3dca-a0ef-b2db8ae7d174 | -5.97937 | -45.80156 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce6a3b75-0de3-34b6-b1ec-7f15acc0c735 | -6.3239 | -43.41401 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ce2fd7f4-1710-3dbc-806a-f9ebe6e0b5fb | -6.41587 | -44.39687 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1f4fd5ad-9ac9-3ea7-8377-cf6e87c8001d | -6.41363 | -44.38938 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4d04bd39-75d7-3ca7-85fb-32c23368cca7 | -6.47841 | -41.75008 | 2025-09-11 04:21:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 5f1dab8f-8ac4-3f80-8f89-79c0959bf868 | -5.23628 | -45.45839 | 2025-09-11 04:21:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88ceab9d-9803-3edf-ad20-97c61fd7d54b | -7.84974 | -45.40271 | 2025-09-11 04:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4763413d-6c81-39a2-b843-6aa9ff2840a1 | -6.54189 | -44.77952 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f049855d-c155-33f3-86c6-31800b3bd823 | -6.33859 | -39.85619 | 2025-09-11 04:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b0c6471b-7088-3754-afbc-5bec2285823e | -8.01945 | -49.04142 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4578354d-3e01-3f12-8e72-c559919ef83c | -7.26316 | -44.61711 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d66335b-db93-3895-a1e2-e3fefde16233 | -8.56049 | -45.59116 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 404758fc-e86f-3f2b-9b2f-0a8133e8f55f | -3.07976 | -49.46852 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b89e5989-bb46-348e-b9d6-f503587591a8 | -7.46775 | -45.28795 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 672db234-99bc-3550-9858-f3b8ad0cd735 | -8.02309 | -49.02448 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7998aa4-ee97-3fd4-a610-1e551ff652e8 | -8.34885 | -45.41048 | 2025-09-11 04:21:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f090e5d0-3546-38c0-bad8-03686887a3fc | -6.41254 | -44.39635 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88a89e6b-3c73-3005-bb6e-16d5bc911717 | -7.19219 | -44.95881 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d1be6ca7-ce77-31c9-a58b-fe0bc1ba1bc3 | -6.4386 | -44.404 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6c58cd1-db04-3414-a29c-789071e30502 | -8.02306 | -49.04839 | 2025-09-11 04:21:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ebff7701-8f74-3dca-ab9b-0c0a7982fd38 | -5.54689 | -43.04925 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 551b990f-7782-38b2-9ee5-89b0141e5043 | -6.47289 | -44.12045 | 2025-09-11 04:21:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1ba7ca61-987f-332f-83b6-4e054b25c1b3 | -6.85331 | -47.87196 | 2025-09-11 04:21:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a3a27c14-75ae-36b3-9491-798c05578b73 | -6.90142 | -47.9189 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| dde50e1c-0027-346a-a5f3-0c1f9b0126a4 | -5.15721 | -42.72671 | 2025-09-11 04:21:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 200d857c-a2c1-3c64-a72d-766c01d1c553 | -5.44044 | -43.41339 | 2025-09-11 04:21:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0edc9eb0-f375-386d-b2d0-43b695c77900 | -7.46442 | -45.28741 | 2025-09-11 04:21:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df754381-f968-3521-ba72-23d4dc2d09a9 | -7.71179 | -44.84105 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f14a006-02d0-328a-bea9-122f345e9164 | -8.51264 | -45.69855 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6b8197e1-d65c-3d08-9a2e-362dbfe73a29 | -6.30068 | -44.5915 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32eda8f5-1f94-30ab-8cd1-209754ed9e1b | -9.04742 | -45.78498 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e6de7c71-2c3b-3fe8-9c22-23be8f6caaae | -6.85125 | -47.8845 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 173908bf-b930-3df7-a7cf-2477893e3107 | -6.25763 | -43.41838 | 2025-09-11 04:21:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 28aa800d-1984-3743-90a2-5f4df7e6d40d | -4.58723 | -45.61191 | 2025-09-11 04:21:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| beec0eea-488d-3a21-9b7c-4d73c77b53a5 | -5.79067 | -44.86037 | 2025-09-11 04:21:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bc9f54a8-95e3-31eb-a1ba-3950471c2fd3 | -8.49942 | -44.65073 | 2025-09-11 04:21:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0610bd19-f66d-3da0-93de-d801f65df416 | -6.39844 | -43.49848 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ef0c70c-9844-34c3-a8e0-589420ee4980 | -6.3414 | -39.85508 | 2025-09-11 04:21:00 | NPP-375D | CATARINA | CEARÁ | Brasil | 2303600 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9972638f-7c40-36ea-aff4-8474ef465a96 | -5.79226 | -45.68113 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8b6731ed-c473-3874-8a92-08278e587d75 | -5.7299 | -45.41344 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ee803d53-9e22-3e56-a800-3d58e3014062 | -8.07762 | -50.1768 | 2025-09-11 04:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a9c1395d-f764-37b9-998f-19d713a07843 | -3.79285 | -51.16184 | 2025-09-11 04:21:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 343845a2-46d7-3031-b6f7-1b1c102f5d57 | -7.20714 | -44.95047 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1bfd8455-64ee-3578-9a03-33fbb707d077 | -6.31716 | -43.41296 | 2025-09-11 04:21:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6e194366-600b-3bd7-9a12-4ed467175ea3 | -7.23371 | -55.05034 | 2025-09-11 04:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6bd122a3-fb71-38ae-8401-7a3bb35cd76f | -7.94035 | -44.88803 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b78b59e-7035-3246-8252-383b788f80ae | -8.36601 | -46.97634 | 2025-09-11 04:21:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c0730cfb-136c-3624-90a5-d60fc33bdac1 | -8.73573 | -47.11194 | 2025-09-11 04:21:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 24daa0dc-995e-3b55-95a9-135a8b83ad0c | -6.37598 | -45.16689 | 2025-09-11 04:21:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f184259c-775d-3128-b2ce-df06afae0a9d | -5.87502 | -45.66806 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 643917df-c362-38c6-9d26-9cb297f79773 | -5.57561 | -43.44904 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 44217a3e-1f34-3931-ab76-04767296b42f | -6.82175 | -52.80258 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d3ad1c43-9d2c-38b8-a4f4-bf55ac878a2c | -5.81247 | -45.6843 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f44a8b74-a9b2-3f5c-81ab-74a66e6834e0 | -7.53519 | -44.67432 | 2025-09-11 04:21:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f380c330-e9f4-3f90-a56b-dec296eb6f65 | -9.06417 | -45.70123 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 812b40ab-533d-3ee8-bd3e-dc9a6a0a0d35 | -6.32949 | -47.74561 | 2025-09-11 04:21:00 | NPP-375D | NAZARÉ | TOCANTINS | Brasil | 1714302 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afbb5245-2597-3392-8f66-be22c4d6da46 | -6.40243 | -42.61656 | 2025-09-11 04:21:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 848f9f77-98ff-3fa5-a9c0-7f4fab5f3698 | -7.20329 | -44.97483 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c69f953c-397b-39b6-a3b8-6113a68516fa | -5.68347 | -43.33139 | 2025-09-11 04:21:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3c5452b1-820a-30f5-beb8-413a793c1fc9 | -6.34405 | -43.78037 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b694232a-0233-3130-a5f3-a313af092d3e | -7.20382 | -44.94995 | 2025-09-11 04:21:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 691486b6-bf17-3e33-9ed7-7ecada2f8c7c | -6.83694 | -47.90359 | 2025-09-11 04:21:00 | NPP-375D | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d7f54ae9-6319-3659-87fb-7e5360897e99 | -3.31815 | -54.91571 | 2025-09-11 04:21:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1c7ac26-b013-3564-bb26-aa0cf429cb62 | -7.60614 | -42.53656 | 2025-09-11 04:21:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a135e816-d251-3cb7-b090-b4e978eaac95 | -2.94778 | -49.35007 | 2025-09-11 04:21:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f6457dac-452d-3347-b1f5-edf9e6006365 | -9.09581 | -45.69556 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5e6945d9-9a0b-362a-977b-64cc77ac4ec5 | -5.8501 | -45.12661 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0743e5b6-7d7a-3f3e-ab89-f324cfdb30a0 | -5.65105 | -45.40091 | 2025-09-11 04:21:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9bff5aea-99c8-3471-885a-a2e55cdc3318 | -6.2932 | -42.19882 | 2025-09-11 04:21:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| d426e2cd-5a2e-3797-8d17-831f71d78b1b | -6.73354 | -43.02348 | 2025-09-11 04:21:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5c89013f-d558-389b-9495-e5f66a74fd56 | -5.94005 | -45.69298 | 2025-09-11 04:21:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c6fc037-fcf1-3834-9bf9-735a115d883a | -7.2637 | -44.61363 | 2025-09-11 04:21:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c52fa6e-c35d-336c-9fd6-d2c30e068836 | -8.58547 | -45.58433 | 2025-09-11 04:21:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |


[Clique aqui para ver as próximas entradas](README45.md)
