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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 20fe8425-a5b2-33b0-81e1-74073f7d4be0 | -16.08155 | -50.34298 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a29251a3-9a36-3a78-95c6-cf8e3f2e3bd6 | -16.08093 | -50.34729 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 980b0f97-c88c-3bff-a6c1-2a6e084db75f | -16.07914 | -50.4096 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d8dee5f-6072-31ae-8e6c-443774986819 | -16.07856 | -50.41357 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63402517-11ff-3a6d-9e42-3474e1afb6ab | -16.07742 | -50.34646 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 778a63c1-416d-3f5f-b2e7-f27739ba64b2 | -16.07391 | -50.34568 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a36f5305-ebea-3158-840e-054ec246250f | -16.06917 | -50.35345 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55169bd3-e5e4-3a91-888b-b5c2e13c0243 | -16.06506 | -50.35683 | 2024-10-02 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18627af5-630a-369e-beea-1456f7925b5c | -15.37315 | -51.55792 | 2024-10-02 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c24d3d6d-0e98-3259-8a5b-87f55b4ba3bb | -15.36585 | -51.56056 | 2024-10-02 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9e378ab-6fb4-3bc7-8c6d-6619c93a1ad6 | -15.36529 | -51.56427 | 2024-10-02 04:49:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4f0e161-8703-36cd-b78c-98034d449792 | -17.62877 | -52.01838 | 2024-10-02 04:49:00 | NOAA-21 | PEROLÂNDIA | GOIÁS | Brasil | 5216452 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e2f1a2eb-9465-3da6-9cc4-3cf9b449fb7c | -17.36148 | -51.99594 | 2024-10-02 04:49:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96c20abf-90c1-3c40-9d2e-9c469ff13b3b | -17.29327 | -50.6106 | 2024-10-02 04:49:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 18b05c01-1342-3e96-9877-9a3e5cb013de | -17.28973 | -50.61002 | 2024-10-02 04:49:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91f35bbe-1549-3881-a2d9-7e1098655589 | -17.28914 | -50.61421 | 2024-10-02 04:49:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bf940877-63bb-3442-8d45-7443701ca8ff | -17.2856 | -50.61364 | 2024-10-02 04:49:00 | NOAA-21 | PARAÚNA | GOIÁS | Brasil | 5216403 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1349fdab-f664-3e07-bd90-9e27ee03eafc | -11.96071 | -51.8892 | 2024-10-02 04:49:00 | NOAA-21 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b363820b-2b7f-3d2c-91bb-da9b76bc2331 | -11.85462 | -51.80344 | 2024-10-02 04:49:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9876fc2f-ed28-3908-88c1-e039476c178e | -13.238 | -51.23228 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c26287a-0b38-3c09-98cf-851e051a308b | -13.23631 | -51.22081 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35cc1fcf-571f-35f6-92ad-310bab8b2cff | -13.19657 | -51.21077 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 44e4e144-30eb-3670-b61c-74e46d2b0b09 | -13.19266 | -51.21389 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 214d2ddf-fc03-32af-848a-598ca7b90f87 | -13.18604 | -51.25765 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63bdefdd-79ef-3417-b102-a2985f3c14ab | -13.18324 | -51.25347 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7138584d-2f5f-34c0-b608-072f8bf294bc | -13.18269 | -51.25712 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 14eefa02-0f01-3e96-bba9-31703b2db0df | -13.17988 | -51.25294 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25150096-07ef-3468-bd57-0c08b5a11716 | -13.17653 | -51.25241 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1f3e1d36-5f57-3bcb-9b17-f714232ecb9a | -13.17373 | -51.24823 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ad638a9e-b33c-319d-b7cf-41864e7a7131 | -13.17037 | -51.2477 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6415275e-c558-33a9-8511-5c3c374dbf7a | -13.16757 | -51.24353 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 426cd213-b632-3442-bb48-32b11e1bd062 | -13.16702 | -51.24717 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 79872e08-4a10-3095-97d3-b36223ba2f24 | -13.16421 | -51.24299 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5d2144b8-b9a8-3ce5-9748-efee00270b44 | -13.16086 | -51.24246 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 4762b8a8-980c-38c8-a234-57a54b19b0d8 | -13.15805 | -51.23828 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e3e14485-98a6-3745-bce3-033e6f2aed85 | -13.1575 | -51.24193 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82bd8d4b-e86c-3b44-acd8-81acaf41d762 | -13.15415 | -51.2414 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8ec92368-7da1-3ebc-962a-75143308878e | -13.15079 | -51.24086 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 448fa1bb-ff17-3ce9-9024-96c8bf917555 | -13.14346 | -51.22897 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7e816b2-43a8-3391-b2a7-63b8621021da | -13.1401 | -51.22844 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d6d5044d-ec40-3b8b-8d95-44080b9f5ae1 | -13.1373 | -51.22427 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6046edd9-6171-3444-9958-2fd269b8afc1 | -13.13675 | -51.22791 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| dbb9506f-a261-35a9-a109-b9c3a7dbfd1e | -13.13395 | -51.22374 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 34cf473b-6b1a-3757-a2e9-21ced536075c | -13.13339 | -51.22738 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0926ba77-f27a-387d-a525-59f437760685 | -13.13004 | -51.22685 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f53ee2a5-556a-31f3-bfa3-b6b6b47a8fe5 | -13.12668 | -51.22632 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e9e283bd-6cad-3144-8a3f-b4437f4c24b3 | -13.12333 | -51.22579 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 18801ead-3d41-3c52-be6e-287ee3639076 | -12.98301 | -51.20782 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a99efc0-d670-37ef-97c9-1d1de48b00dc | -12.98246 | -51.21146 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce65995d-60cc-3552-9d4b-9efce7c625e0 | -13.2481 | -51.27867 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9953512f-1ae9-34b7-9deb-4d944a148d56 | -13.13437 | -51.34988 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 59f77502-0825-3328-9eba-a9f753d027fe | -13.12902 | -51.43051 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 516e856a-35e0-3d38-b9b9-0e85116b0f5d | -13.12568 | -51.42997 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e4d0bf16-9287-33d9-8bad-109962d359e8 | -13.12513 | -51.43359 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fb92a743-5e36-3256-b362-9eb209478924 | -13.12234 | -51.42945 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 537846b1-7bb7-3c28-a15d-beb2205ca2af | -13.12179 | -51.43306 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e2862bc2-9432-37a2-9351-f1fc7534d7d0 | -13.11845 | -51.43252 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 98b39cf4-dd59-3b03-b81f-8771564fb23f | -13.11791 | -51.43613 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.8 |
| f35499ed-7b40-3587-a17a-5a116163b1c4 | -13.11571 | -51.43246 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| dfc67c7d-1d4a-34cf-be17-5acd61fd7d19 | -13.11516 | -51.43607 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| fe5223f3-89d8-36b8-bfab-1b800f0bce8c | -13.11348 | -51.42471 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| cd99c982-1ad8-3f68-9287-c348483d3613 | -13.11293 | -51.42832 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5c08b024-7ae9-30bd-9070-6282c1a293a3 | -13.11237 | -51.43193 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 3e2912f9-7a2a-3761-87ae-5903f5ad996b | -13.11014 | -51.42418 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| f62c2a53-a393-341f-857e-87c1a6ac9130 | -13.10959 | -51.42779 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| fe21d040-781b-3fca-89d2-47a23d4c29f2 | -13.1068 | -51.42365 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| a22436af-de5a-30d0-a728-db7f1f8fa43f | -13.1051 | -51.39009 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f994b01-ff91-3024-a02e-97ece1eaea74 | -13.10401 | -51.41951 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 92b0dafc-2f17-3235-9fad-6ea3ca7b0c8f | -13.10346 | -51.42312 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c1e67a80-95c1-3245-a37b-17d05a8994ce | -13.10175 | -51.38956 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dbc78f7c-71d3-38fb-ab39-0d9a9a4f7d97 | -13.09952 | -51.3818 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5ad6f333-db41-3444-9bef-4f1c1c3d2389 | -13.09789 | -51.41484 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 472807c4-f0c2-37a0-b980-5e1ef8590765 | -13.09673 | -51.37766 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c80f8549-1809-3c95-99e3-6638d9ff353f | -13.0951 | -51.4107 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 737402ed-0de3-37eb-ae0a-6b5a37756624 | -13.09454 | -51.41431 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 16360b06-f65d-3f18-9a4f-aa114025c64d | -13.09231 | -51.40655 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5945f703-d8ce-36a5-a9fa-03f560f4f760 | -13.09228 | -51.38435 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6646da57-8dbd-36ce-92a0-7ba0b5384c1d | -13.09176 | -51.41016 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9481711a-d370-3df7-b17c-0d4ade7f6bec | -13.0912 | -51.41377 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4400b95a-6730-3aad-aca2-3556188d5f77 | -13.08897 | -51.40602 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f2f5fbbd-fb85-3c20-9201-12e91097a155 | -13.08842 | -51.40963 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 960ce07f-75ae-398c-a7e0-5e762c588070 | -13.08618 | -51.40188 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b0985f95-fae7-36ca-a5af-35bd51cc9e4e | -13.08563 | -51.40549 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 966caa19-dda5-3e30-9b41-15d93fc1a86f | -13.08559 | -51.38329 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 56b3521a-20db-3d20-9b1c-faa511808ceb | -13.08339 | -51.39774 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4f74d27f-717f-3736-afcc-71322c8fa765 | -13.08284 | -51.40135 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 9d4fb387-1a48-3f92-af8f-c5bf1ba68cf2 | -13.08005 | -51.39721 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc452094-1f79-3b46-a0e6-e4679315926c | -13.0795 | -51.40082 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| dc3c7a04-8af9-342f-9999-55dca20c20f1 | -13.06719 | -51.36926 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5ddff4fa-a8c1-3334-947e-51d3ff970c91 | -13.06664 | -51.37287 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| f5394678-4694-35cd-a9f7-9ff5576db53a | -13.06609 | -51.37648 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 7e8f701f-4bb5-3d0f-8bde-c428babd4a8a | -13.06494 | -51.3615 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 015a059e-633f-3317-801c-d0645c5dc3c1 | -13.06439 | -51.36511 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a03a3ee0-0587-3918-a3c6-a56c65b87148 | -13.0633 | -51.37234 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c0b51756-b8d5-3bf8-bfb9-c71601c89897 | -13.06325 | -51.35012 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0382c1e-85d3-3b58-9066-f3921534a4ab | -13.06275 | -51.37595 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a7f9f86c-bfeb-3a13-aa02-9e679b6e19bd | -13.0599 | -51.34959 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9656f60a-4f0e-318e-9e41-8cdc19b26547 | -13.0594 | -51.37542 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d430fd69-a0e8-3124-b036-dd63600aad58 | -13.05835 | -51.40485 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 13.0 |
| c6d09ef4-7340-3c35-a46b-c77683397f51 | -13.05725 | -51.41207 | 2024-10-02 04:49:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README100.md)
