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
| 6ec43434-0ead-3ba6-8ae1-7cbf8141a295 | -2.65442 | -46.78376 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3fd6a358-b535-317a-8344-b96e68dbab2f | -2.8675 | -47.82318 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 20e3983a-54e0-30fd-b4b0-1d62c36338ff | -2.11502 | -50.69726 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| f2a0e041-de60-351b-90b9-25dcbe7d1a32 | -2.65494 | -46.82404 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae0766f8-a385-39f4-8058-967d4fdc200d | -2.62221 | -46.17052 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0986602b-56da-3a44-a223-8f61f7761119 | -2.94169 | -49.3668 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dbd60af8-b035-32b0-82f5-d06e06be9b34 | -2.77839 | -50.30132 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 29cafe35-affa-3cbc-aec8-a9338d0f37ba | -2.15122 | -49.00732 | 2024-11-12 04:25:00 | NOAA-20 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 515f1156-b9d6-3816-b5df-672cf7fa883c | -2.125 | -50.71413 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 991e66ed-1327-313e-b64a-2099645ea80b | -2.40707 | -50.30847 | 2024-11-12 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1b595fdd-8553-3fe2-86b3-3110c7ee9b15 | -2.62167 | -46.17398 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8ebf4dc7-248b-3da4-bddc-703a0e7b8796 | -2.65832 | -46.80262 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 978c3d00-cf62-3771-a5ef-d518b554adff | -2.64713 | -46.78628 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 958fa292-5b4d-3d52-ab80-6c9fd3118d6c | -3.02649 | -47.97801 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc9c83df-1117-30a5-b4af-fc620524def0 | -2.82148 | -46.65386 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee6ba4d1-e8f9-358e-86f9-fda9027bebf4 | -3.1984 | -50.28481 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a6ca72f9-2e5c-3e39-a196-cf57eb057c4f | -2.17386 | -48.7275 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96c9f879-0791-3865-847b-8f9be852b166 | -2.73278 | -49.29106 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 12aeb5ec-3bba-3856-9a6c-110f987bc6e0 | -2.12447 | -50.69115 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 1ff7eb0d-5b07-33f3-8042-e9614de44134 | -2.11793 | -50.70542 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6840852a-c028-3967-9f57-e78c4c5ba0ae | -2.0955 | -50.37757 | 2024-11-12 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4264ae00-3ea2-38a9-b765-ded152e44e7b | -2.65663 | -46.81332 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 434f0ee5-6c74-3b58-8607-0e9e0c323d8c | -2.77948 | -50.29445 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 66a6f40d-8813-3d9a-9877-4c5c94b72e64 | -2.93794 | -49.36619 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 527b1478-7728-37a3-b724-37d1045a4ff9 | -15.89039 | -43.45771 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 57907956-4589-3b7a-86a7-7ce3fd24d01a | -15.88966 | -43.46301 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8c6cee2-d8d9-3dc8-8e4a-69b3feb2f639 | -2.36464 | -48.51784 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90201d27-88d7-364a-a33a-3c70a8deded0 | -2.36891 | -48.51427 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e5e6be5-e579-3835-9b0d-7a4ef94faf21 | -2.89867 | -48.30537 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46bba7fc-0d7e-3b76-a437-7ef417777f18 | -2.7802 | -50.31573 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6e9faa-2c3f-3ff5-9bf2-cde5d5414a79 | -2.60507 | -46.17138 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e6b8b1c7-74fb-3d3d-bdbf-1180bde6809a | -2.65327 | -46.81281 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6c040b77-3e8b-3eda-835b-d73f2810e932 | -2.60949 | -46.16497 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8a54cf2-79c5-317a-971a-70ad338a6e85 | -2.17411 | -48.72627 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| adb6fa5b-f718-3b02-9bd1-32677685acf3 | -3.26226 | -48.75614 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 47ea1981-a976-3221-a6cc-505ca07c33f5 | -2.11088 | -50.69663 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d20d0b7f-44d1-3c82-b86c-22a33d304568 | -3.13658 | -50.44057 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83a49713-481d-3477-a986-b4d2c933b917 | -15.89138 | -43.46481 | 2024-11-12 04:25:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a56ba448-22b9-3383-be1d-c19c3311aa5c | -2.54454 | -46.31852 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eb0c84d2-c7c1-37c2-99ae-4b1b57c9864e | -3.91451 | -42.87214 | 2024-11-12 04:25:00 | NOAA-20 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 49ede09d-83f6-3064-bf06-64ed0e573be1 | -3.09204 | -49.59242 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a6ba918a-1aaf-3eab-bad7-82e2e5cbf6fb | -2.11681 | -50.68614 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 6643d34a-6b16-3a86-bf68-96f12089fb6a | -2.48188 | -46.34815 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ceff0094-5fa6-31e4-b793-aa573e796152 | -2.12087 | -50.71349 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c1bae822-9213-3507-8e3b-c25fab06c8cd | -2.89778 | -48.30863 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afa4d3bf-b0d4-3c6d-a6ce-b16944bd1e2c | -2.37216 | -45.01759 | 2024-11-12 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 90b573f1-ddfb-3eb7-b661-1726f16c362c | -2.60672 | -46.16099 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5dc3c7ff-ef03-3ae9-bffb-50a88441064d | -2.49155 | -49.10586 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9f333b9b-30e6-3c66-9abc-f42e86ab19d0 | -3.05173 | -49.52913 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 507d94ea-0998-382d-bea8-171b4c0ed631 | -2.11914 | -50.69792 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| d37d6b5e-ca6c-3c72-a468-ac5d54e90aee | -2.83495 | -46.64863 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c703d8ac-4009-377f-abb1-0315ee442785 | -3.13714 | -50.43712 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbc5cd09-a4e7-3133-9521-43f19e677cdf | -2.13918 | -50.70494 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fef06011-806f-35c1-92b7-56a84a93b2e1 | -2.78581 | -50.30605 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f44ef08c-e8f2-3b47-8f32-e1ea5ebd84af | -3.1696 | -50.43913 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3651740-7828-3117-a400-9d62d8c0c747 | -2.12387 | -50.69485 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| d991425b-2311-3013-ab53-4f32c3758767 | -2.12154 | -50.68309 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5de72a4-11b7-3c69-adaf-9abc648f5187 | -2.82481 | -46.63267 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8539649d-e008-316a-be6a-c35f667a4394 | -2.12506 | -50.68745 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 17873693-d59d-3c17-ac1a-a389d2f0fa7d | -3.13255 | -49.12442 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47ecd967-1a56-304f-b7d2-be1c7134209e | -3.0317 | -48.05851 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70d0b65f-1d80-3598-b060-71e6795abef9 | -2.69699 | -46.81956 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2faddecd-878f-3166-affe-b8048181bee3 | -3.02361 | -47.97359 | 2024-11-12 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b3845a03-e49a-37d8-a2b9-e5d5a81a192a | -2.78527 | -50.30949 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d600eba9-48cb-3492-8f46-cd9e203f008a | -2.78473 | -50.31293 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bdfc7d12-6f2b-376f-8f28-a038115794ee | -3.26798 | -48.75175 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c1dc8eed-774e-39c6-bf24-0c2d3a5ee4e3 | -2.69949 | -46.81649 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6492dc7a-3cec-3d76-8602-64c338b3c6cb | -2.78129 | -50.30885 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 40a51ae2-775b-3118-b41a-afef0e8c52fe | -1.54355 | -48.40352 | 2024-11-12 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 554f9b29-047c-393c-af2f-78d831206197 | -2.13092 | -50.70363 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c6a536-0d76-3e80-b1c3-49451a9ad327 | -2.3942 | -48.89477 | 2024-11-12 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e1f177aa-c15e-356b-bf25-f05287a42bff | -2.60562 | -46.16792 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 29d70dc3-e8f3-38b7-963f-236fe1ebbd8d | -2.62553 | -46.17103 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a77000d5-5bee-3c67-82ae-27bad6be3082 | -3.13258 | -50.43992 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c04f6602-938c-36a1-a1c9-f09f5892945a | -3.19526 | -50.2791 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 17964c09-c243-3994-a156-9926d41b2c41 | -3.2673 | -48.75589 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 293ae91d-08e9-36e1-b7ae-bbe0f8e867d5 | -2.89843 | -48.30462 | 2024-11-12 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa034482-0f1f-339c-83eb-5d0b47ec0902 | -2.37851 | -49.83569 | 2024-11-12 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 35001f28-8812-3ca0-80d3-42bd46afed50 | -3.2616 | -48.76031 | 2024-11-12 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d67fcd9a-0090-3aec-a939-9a3ab66c9704 | -3.40706 | -44.09126 | 2024-11-12 04:25:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4951ba7-9ebe-32a9-bbec-2e6a8a070653 | -2.91202 | -49.81846 | 2024-11-12 04:25:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ad10193f-0cdd-3475-a8df-902e18dcf81e | -2.13212 | -50.69619 | 2024-11-12 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 16ea2f32-ecea-38a9-a042-3e9f161b8b77 | -2.63217 | -46.17207 | 2024-11-12 04:25:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1baf949-57e6-3550-a753-8c041cbb2f31 | -2.65271 | -46.81637 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5fe2fa25-8b39-35d0-adb7-92a526430c87 | -2.68354 | -46.81746 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d92dfa23-e4c0-3c4e-b4a4-2a6f43272d0c | -2.69362 | -46.81903 | 2024-11-12 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 888a7192-c5e6-3c4e-a3a8-297c02e58802 | -15.30268 | -56.50891 | 2024-11-12 04:27:00 | NOAA-20 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a35e6594-2c73-3d40-8d45-790669b8925b | -19.45333 | -39.75727 | 2024-11-12 04:27:00 | NOAA-20 | LINHARES | ESPÍRITO SANTO | Brasil | 3203205 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.1 |
| 9f61023f-7c88-3652-96e4-49b5293397e7 | -22.53776 | -48.81279 | 2024-11-12 04:27:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a1867f1-f42d-3ae6-a12a-00e5072c43fd | -15.99658 | -59.383 | 2024-11-12 04:27:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be9154cb-a331-34ce-a333-52279287c17c | -15.76246 | -46.17704 | 2024-11-12 04:27:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d29e9d3-68fa-3d80-9fa0-26ec673b321f | -20.636 | -48.83609 | 2024-11-12 04:27:00 | NOAA-20 | BARRETOS | SÃO PAULO | Brasil | 3505500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8c435d91-aedf-30a7-bdda-8fd66e1c4ca7 | -17.28463 | -57.48132 | 2024-11-12 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.1 |
| 746f5d31-073f-3651-b19e-01d2669cf4a1 | -20.741 | -50.53769 | 2024-11-12 04:27:00 | NOAA-20 | AURIFLAMA | SÃO PAULO | Brasil | 3504206 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 870dab58-7db2-33e5-a080-a2ec6f7f00d2 | -17.27465 | -57.47909 | 2024-11-12 04:27:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| b4a425f7-bb93-36c5-ae61-181b6553ecb7 | -18.90044 | -49.76883 | 2024-11-12 04:27:00 | NOAA-20 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cf2c38f7-b487-36b2-959f-2a2f5be01066 | -18.3463 | -40.01562 | 2024-11-12 04:27:00 | NOAA-20 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ecdafb73-b835-3174-8783-da9df1ed3358 | -18.39523 | -45.98133 | 2024-11-12 04:27:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7952a1b3-1b40-35b7-a3e0-57037a8a310e | -21.1964 | -44.93778 | 2024-11-12 04:27:00 | NOAA-20 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 38a42cce-c364-31fe-90f9-394181bf5e4d | -19.34647 | -50.8226 | 2024-11-12 04:27:00 | NOAA-20 | LIMEIRA DO OESTE | MINAS GERAIS | Brasil | 3138625 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README17.md)
