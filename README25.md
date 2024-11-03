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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b0d2f84-69d5-345c-af36-665ea2d8ff58 | -2.80268 | -48.65802 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2ed7c0d-df3e-37a7-9b8c-6b2ac5eb9bc2 | -2.8019 | -48.6626 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7ee68025-371a-376f-9778-20a60bbca16e | -2.65784 | -48.50392 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd278424-a2ac-3743-b97f-a4b2ac4e60d5 | -2.65709 | -48.50847 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cab7719e-5e6e-3891-bfbf-eeb01ccd7ab8 | -2.64661 | -48.5717 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 7b45a3e5-7609-353e-8235-bff379c456de | -2.64586 | -48.5762 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 500cf5db-98c2-3292-b139-248cf4484c7e | -2.6451 | -48.58078 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 17fb5f54-bbea-3122-a013-3f0327c98924 | -2.64433 | -48.58548 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 362ee3db-32bf-3dcc-bfb5-c947c598dcb8 | -2.64132 | -48.56613 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ada24065-9d8f-36fd-881f-8fbe22c0f8d1 | -2.64058 | -48.57061 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 0cbdb7b8-c75a-3022-8a53-452886e04eaa | -2.63982 | -48.57515 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2add8049-07c2-3f3d-8e6b-df16dbe481f3 | -2.63907 | -48.5797 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 46607e09-7c62-39fa-90a5-63af4adbb928 | -2.6383 | -48.58435 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 956634e8-9cfd-3f82-a69b-2363f4a1b1a2 | -2.63529 | -48.56505 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| de312349-c707-38ea-b7f5-5764f0999519 | -2.63454 | -48.56955 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 10a5b4e1-f7aa-318d-b590-67e097a5bf27 | -2.63379 | -48.5741 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 12deca4d-18fc-3530-a76a-6d6db6853020 | -2.63301 | -48.57873 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c3d71e21-96c9-3e4b-af9b-ca3864bc10f2 | -2.63224 | -48.58337 | 2024-11-03 03:53:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2224cf7e-527f-3e64-85fd-507c4ef2429b | -2.61805 | -48.33771 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2a2af9bc-f452-3ee4-95d9-f495c9e515b6 | -2.61211 | -48.33663 | 2024-11-03 03:53:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6f125e73-b50e-33a8-b646-03aa31db79a5 | -4.75706 | -48.00473 | 2024-11-03 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3477eb6d-1313-3ad6-9eb3-28fbbda1d45b | -4.75641 | -48.00847 | 2024-11-03 03:53:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 73f5d8b5-39e2-3507-a6a0-6070e7f1fbc7 | -4.23687 | -48.04008 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5b6e0b8e-daa9-3f3d-bbc8-9905c6ef0c86 | -4.08245 | -48.31801 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 91272c35-5bdb-3ec5-ac8c-092372906937 | -4.08175 | -48.32215 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e3620a5-5e96-33aa-ac16-a3a2b63ca5f3 | -4.07809 | -48.30849 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a36dc4c5-0442-3e75-9812-8dc7194dbdab | -4.07738 | -48.31264 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6b3e326c-4b13-3bb1-96ef-d311d85369b3 | -3.96779 | -48.15071 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 42accfd0-2f52-3537-9a15-0bf1cdc76d07 | -3.96336 | -48.14198 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 60de0206-9438-3415-a236-fb85d153eb28 | -3.96271 | -48.14579 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 420619ec-8872-3a5f-842b-a37b55a47640 | -3.96201 | -48.14981 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 60c15ded-88ea-37ef-874c-53f5c2500a5a | -3.95693 | -48.14489 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af25e007-10d4-3ad8-9f1c-eb94ea52320b | -3.95185 | -48.13999 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e7ba6b7c-3c2c-3779-a8c2-e71536700852 | -3.95117 | -48.1439 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b066278-887f-311b-ad1a-e53497e6fe62 | -3.94905 | -48.36486 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e828fab3-2d2b-3453-897e-b6957a586ac7 | -3.9483 | -48.36927 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5aeed34d-0bfe-3cd0-b506-409b6c3b9c22 | -3.94539 | -48.35109 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7eb14b80-5d17-3f2f-9f56-4dd3017f1c2d | -3.94468 | -48.35528 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 031dfa81-2fe5-335f-81f5-4f86e4e8fcd4 | -3.94029 | -48.34581 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3f40406-4a57-3b52-adea-a1aaba639d22 | -3.93957 | -48.34997 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fab82533-8cca-3d77-8121-18a7d2b2b7cf | -3.93886 | -48.35415 | 2024-11-03 03:53:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 94e6ed52-42e7-307c-922e-8f814eb5db1a | -3.90023 | -48.3758 | 2024-11-03 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1212b70-0234-3964-9a37-4a7362228ac9 | -3.89939 | -48.3736 | 2024-11-03 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5c13ef28-66cf-383d-9f70-ec6214f73efa | -3.89439 | -48.37473 | 2024-11-03 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de9f04fc-c565-3a94-8dce-ad81b6037e6c | -3.89355 | -48.37258 | 2024-11-03 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4b8d3e82-ad9e-367a-9fd7-6509a88053c3 | -3.84085 | -48.96087 | 2024-11-03 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bb5477e8-7bbc-3a3d-a10b-1b9d5979df04 | -3.83477 | -48.95986 | 2024-11-03 03:53:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2c3460b5-0e03-3194-913c-2959738a35e1 | 0.03269 | -49.55009 | 2024-11-03 03:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7fc87e91-11dd-33ee-8ef5-f3df10e14498 | 0.02607 | -49.50909 | 2024-11-03 03:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 97ad5af3-4a2c-34c9-8f09-af2349693c4d | 0.02508 | -49.54535 | 2024-11-03 03:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c41c709-9ab8-392f-9bce-200f7ac5e7fe | 0.01842 | -49.54644 | 2024-11-03 03:53:00 | NOAA-20 | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 66c43ae3-2979-3333-8b07-32167deba6f3 | -2.19946 | -49.18013 | 2024-11-03 03:53:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 172567b8-a3f6-33ee-9a33-4c372040eb9f | -2.15657 | -48.83328 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bcb1da30-48f0-3bc7-8fcf-878942f442c6 | -3.60691 | -49.3262 | 2024-11-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d1cb3b2b-02a3-35bd-ac4b-d8a4d77645ff | -3.60369 | -49.31957 | 2024-11-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 495ba51b-e247-32a5-a10d-786c10532963 | -3.60284 | -49.32461 | 2024-11-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 673db696-5616-38a2-b528-fbe7acfac48f | -3.60199 | -49.32963 | 2024-11-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| af16a19c-e75f-35c8-b380-44a2ba0a5d5c | -3.6016 | -49.31985 | 2024-11-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 429d9a61-a0a5-373e-89c5-e9b4be592c20 | -3.60072 | -49.32484 | 2024-11-03 03:53:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 417b239e-150e-39eb-baf7-a866d4a1b964 | -3.54473 | -50.29712 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9f7b24d-ac41-3088-837a-63ae8cbd0671 | -3.54312 | -50.29145 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8b70411c-d1eb-35c3-95b0-905e8317c0f0 | -3.5391 | -50.29016 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8eb573c-ac20-369e-a067-ba57dce8e1f0 | -3.53814 | -50.29573 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5b7b385-cdc8-3e8a-94ae-8d69befab4ba | -3.47565 | -50.3805 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c6eff352-c4fb-335b-9181-ec489a842073 | -3.47459 | -50.38658 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 70ecefcc-a92f-3b48-ae42-63dbc98b05a7 | -3.46898 | -50.37937 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 52c198d9-d82b-359a-9836-9287e3226283 | -3.46792 | -50.38546 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| faed4a49-732b-373c-be36-87d7338de4c8 | -3.46519 | -50.37945 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 11927b2c-2d13-3bb3-9579-2b282500aa1d | -3.46417 | -50.38559 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5bf3b499-fa3f-37d2-bfb5-1b500de17c20 | -3.46374 | -50.48874 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43a8c13c-f41b-3652-b98f-e3082c9c07e7 | -3.46273 | -50.49458 | 2024-11-03 03:53:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8b35f502-a4ef-3d5d-a5bc-ba0915ec7150 | -2.49759 | -49.08262 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9800d163-409f-3ace-a956-6920a9d42006 | -2.49674 | -49.08761 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| afcc838d-a947-374d-8b7a-91c4a4442aa7 | -2.49405 | -49.08055 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d7bcd16-3c7b-3af8-8c61-ce252be8418c | -2.49324 | -49.08554 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 59b6671e-84bf-3787-9764-ae483c2889a7 | -2.49135 | -49.08146 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 09426957-9ce7-3a6f-bed9-7e7e485308b4 | -2.3978 | -50.31798 | 2024-11-03 03:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a9c73d11-26f0-3ecb-b7a4-23b641ff667b | -2.39356 | -50.31646 | 2024-11-03 03:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96731893-72fa-3202-9c60-ce3752feb2dd | -2.39253 | -50.32249 | 2024-11-03 03:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bf0ad0f4-5636-352e-929e-0bc5ffc454c0 | -2.39006 | -50.32286 | 2024-11-03 03:53:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2af18dcb-852d-3cfd-be29-0522f61cf7b1 | -2.36368 | -49.10608 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 81920b4c-ab31-3c34-b156-11262e2dd499 | -2.3614 | -49.10378 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce4f62c3-d4c9-3976-9f33-391c3940de51 | -2.36055 | -49.10873 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19d8f5ba-d10b-3b3b-b541-3c7f9eb8221d | -2.32379 | -48.92167 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 14215c45-2fee-3785-b6e6-f8ad0afea902 | -2.99485 | -49.24182 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 294f0e9c-5d9b-3adc-9f05-a3ec842614ff | -2.99266 | -49.23948 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e94156fd-81d4-3769-b341-df74a767ec73 | -2.9918 | -49.24444 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68b03944-115b-3ddd-ac8d-2a72f92c063a | -2.98879 | -49.52732 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fc88ee57-94ae-37ac-987e-3c64ecf497c9 | -2.98327 | -49.5212 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 52171bc2-1bc7-3e35-acb3-2eb9e2d2d441 | -2.9824 | -49.52628 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| eae2cd3d-bfaf-3fe5-9fc6-f6d73600fb0b | -2.97688 | -49.52019 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c806d2f4-acae-32a0-a745-d311b249386f | -2.90038 | -49.41837 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 56b8c9b6-5b19-3c5c-b345-da173468ce92 | -2.8995 | -49.42356 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adc0f385-0763-32db-a93b-1abac633adc5 | -2.89861 | -49.42881 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aeaea5cd-c927-3015-b105-3a8d9c6df271 | -2.89404 | -49.41728 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c804b377-f9c1-3651-abee-9fce0dabfa80 | -2.89136 | -49.43304 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 64298752-9608-39d3-a6a5-f80b9a3ef04c | -2.88502 | -49.43191 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8115c302-7291-33fd-b464-20acb20d91ff | -2.87888 | -49.46786 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c7855686-4792-3d4d-8194-503010fd474d | -2.87799 | -49.47306 | 2024-11-03 03:53:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 175f7be1-85cb-340e-a61a-8acf7df51bb4 | -2.87216 | -49.33882 | 2024-11-03 03:53:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README26.md)
