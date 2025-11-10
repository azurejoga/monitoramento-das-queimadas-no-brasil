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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2eac192d-8bf6-3215-ab41-ab844c3cfd6d | -8.65386 | -38.14237 | 2025-11-10 03:57:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 386eec92-b37d-3289-b8db-38b7b67f5616 | -9.76113 | -36.45931 | 2025-11-10 03:57:00 | NPP-375D | LIMOEIRO DE ANADIA | ALAGOAS | Brasil | 2704203 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1d6d521c-7392-3076-89aa-cce3590304b8 | -4.91551 | -46.73275 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 548d3f15-7ef7-3a78-9083-cef2314c5543 | -4.91602 | -46.72974 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d1ffd1b-cbc4-3805-8dc5-21f6aa20f632 | -4.85755 | -45.78185 | 2025-11-10 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9d4eca6f-211a-3858-9ea9-a90a97d9bae3 | -3.32869 | -49.92763 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8df6b2d3-dcb9-3451-a9aa-b1e55e968e31 | -4.07776 | -44.13179 | 2025-11-10 03:57:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 005015d9-de1a-3161-897e-6da7589ac570 | -2.99297 | -48.05572 | 2025-11-10 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7abfe7a-cd32-338c-9c78-d1682f4df639 | -8.0146 | -41.60065 | 2025-11-10 03:57:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 74f7e377-f618-34ee-a4ee-6bfeea07310f | -2.19824 | -48.24513 | 2025-11-10 03:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3fa23883-cd27-33cc-a4ae-92d1038e9fa0 | -6.21803 | -44.3763 | 2025-11-10 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 16aff30c-d72c-3ba7-9fc6-268e10fe26dd | -8.01393 | -41.60472 | 2025-11-10 03:57:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 0228b9c6-4258-38dc-860e-7999d295fd1d | -5.37341 | -44.72921 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b9508f20-59f1-3884-ba60-f8e78046250c | -3.13732 | -50.27467 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d640ef1b-6062-3f9e-98d8-1a3f7a0b72a4 | -5.64254 | -43.00501 | 2025-11-10 03:57:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 4.6 |
| beba3aed-e74e-31f0-967a-aaede1814065 | -8.01036 | -41.60415 | 2025-11-10 03:57:00 | NPP-375D | CONCEIÇÃO DO CANINDÉ | PIAUÍ | Brasil | 2202802 | 22 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 09a3ae3e-3dde-3d7e-b25e-0d3eba900d70 | -2.99345 | -48.05943 | 2025-11-10 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dea47b8d-d9b5-318e-969e-a2e3c40692b7 | -3.8944 | -43.44783 | 2025-11-10 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca9c4170-4743-31dc-98c7-866dc510d8fd | -4.7475 | -49.50817 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c71135c-5199-327a-9372-2978c72e9fbb | -4.73105 | -45.85112 | 2025-11-10 03:57:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9e1f063-992a-3b68-a913-4c450f7e29e4 | -4.59601 | -45.55001 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 90aacd13-881f-3031-9c6d-26a8c6d8996d | -4.5729 | -45.54009 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77da2216-eddc-3a23-811c-fabfaa27c7d0 | -3.03685 | -49.49781 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6dbe8c4-539f-3a79-b57d-788e19a21b14 | -3.85816 | -51.41724 | 2025-11-10 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4211c0ab-016e-34ab-89fe-4aa2600677bd | -4.11843 | -47.28137 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4164f766-a894-3d0c-a4ec-cafdb6d1ab0e | -6.17472 | -44.38712 | 2025-11-10 03:57:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b3de01f-5d34-329e-a1df-7b25a8c07ad8 | -3.11017 | -50.19207 | 2025-11-10 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 511244b7-173c-37a5-ab3e-26ed47166f3e | -4.11295 | -47.28057 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 868aef67-48d4-38d9-aec6-773fc91d6f35 | -3.94738 | -47.05902 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 784d9ebf-5f9f-3f88-a068-ba5f1220ff07 | -3.98419 | -42.13099 | 2025-11-10 03:57:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c237a9a5-9d6f-3aaa-b721-d9dd914eedd5 | -6.06355 | -42.73203 | 2025-11-10 03:57:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 5a742cd0-f761-3785-80e2-80cf70fff4ee | -5.22303 | -45.03534 | 2025-11-10 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ea2d9f0-5f6c-3473-a01c-e21ca9e65747 | -7.88716 | -48.39458 | 2025-11-10 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a17cf053-f32d-3c63-8e34-12f3cc806983 | -8.7054 | -41.13352 | 2025-11-10 03:57:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| fedb01b8-97ef-3022-a7fd-2e55a795bdfd | -2.44419 | -49.34192 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e0b1f71-b365-36a7-943c-ce87312c4960 | -3.50743 | -50.08678 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebd05d57-5ec9-38b3-9be9-3349ecab678f | -3.90802 | -50.02842 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 543ba0b1-d89c-3fd5-abf7-7a797036406f | -7.88782 | -48.39097 | 2025-11-10 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4c3a6ce-bfd8-3a81-9c2d-ebd2492ca1ee | -3.33534 | -49.92326 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d3f8acf-032c-3b10-8a4c-950ea67cc3d5 | -8.04079 | -39.69042 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| dda7c3be-9864-3f0f-beae-33f4a5d874e5 | -9.23896 | -40.63047 | 2025-11-10 03:57:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 10875d95-662a-3910-9819-1f76fc581b59 | -5.21844 | -45.03453 | 2025-11-10 03:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72465cbe-2042-3713-b436-5eba98e4f51a | -7.04757 | -47.36284 | 2025-11-10 03:57:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2c05bc53-32c4-30b1-ad3c-f431fd0f0923 | -8.0462 | -39.69124 | 2025-11-10 03:57:00 | NPP-375D | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 104b8659-487e-3a83-ae09-a215b983f560 | -3.34033 | -39.99586 | 2025-11-10 03:57:00 | NPP-375D | MORRINHOS | CEARÁ | Brasil | 2308906 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b07595c0-9a6c-33c6-b055-db3b6313c31b | -4.11904 | -47.27785 | 2025-11-10 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ff469c25-bc55-377e-b296-7fb1a02abb5e | -5.02169 | -46.83694 | 2025-11-10 03:57:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd3c37b2-83aa-3140-9609-7f09d27355ae | -3.89861 | -43.44855 | 2025-11-10 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0c5d85a0-7f95-35de-bb66-c375141aa6ca | -2.92047 | -40.00682 | 2025-11-10 03:57:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| ddb82517-8655-3dc3-81f2-40fd232f1dca | -2.43863 | -49.34153 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a1d0b73a-1f4d-348a-9b87-e847861b7213 | -8.44697 | -40.53682 | 2025-11-10 03:57:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| beffdbdb-ebd2-3f7b-8518-0ca1f2a933de | -2.43781 | -49.34078 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46aadae3-702a-3060-9c03-f89fcc342bdc | -3.92198 | -38.40975 | 2025-11-10 03:57:00 | NPP-375D | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| e1a847cf-da85-3d61-89f6-8083f48cd243 | -9.87268 | -37.56982 | 2025-11-10 03:57:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7aae7cd5-87d4-34a5-b020-ac71a6dcfed7 | -6.85925 | -40.15511 | 2025-11-10 03:57:00 | NPP-375D | CAMPOS SALES | CEARÁ | Brasil | 2302701 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9202f0c7-70f2-3367-b427-77e10d7261e8 | -5.37419 | -44.72472 | 2025-11-10 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fd0bbc07-90f9-3db3-9bc1-77d89233c109 | -2.91696 | -40.00627 | 2025-11-10 03:57:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 76ba8570-74a6-35c9-b1b4-b5aa9f46f21f | -6.56367 | -38.69742 | 2025-11-10 03:57:00 | NPP-375D | UMARI | CEARÁ | Brasil | 2313708 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 49f8267e-ae7e-3e2b-878f-b3937ba00c07 | -9.81716 | -36.47193 | 2025-11-10 03:57:00 | NPP-375D | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9fca5a45-13a8-3053-9a3b-c27ab7ff5958 | -5.12455 | -44.72672 | 2025-11-10 03:57:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f6212189-84cb-3e89-938c-c6189adb5352 | -6.93953 | -39.76234 | 2025-11-10 03:57:00 | NPP-375D | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 94472f65-437d-3cee-90c1-07f494dc0879 | -3.40663 | -50.45135 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4e5552c7-e7d4-34c8-88a7-7e33eec36af2 | -2.40782 | -44.78699 | 2025-11-10 03:57:00 | NPP-375D | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ab5f050-1a60-39d9-8e43-0ecdd07a531b | -3.28168 | -51.12245 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 36f57f12-71b3-393d-96b5-fe95601fbb00 | -5.1688 | -38.74256 | 2025-11-10 03:57:00 | NPP-375D | BANABUIÚ | CEARÁ | Brasil | 2301851 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8eb81bb3-425a-36d7-8f52-43dd8494d79c | -4.8048 | -46.72264 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 41f6b731-4ab9-3bcb-98e8-ed1cc7921378 | -6.87386 | -40.73788 | 2025-11-10 03:57:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ecba39e0-da40-3fd1-8602-ab56fae32b9d | -5.63058 | -43.91305 | 2025-11-10 03:57:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7d312d0f-1862-3c51-a1bd-c2fd6f4ce1bc | -5.05232 | -49.56398 | 2025-11-10 03:57:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 484383c0-1a02-342a-b284-e44935f9ba47 | -6.69853 | -44.14486 | 2025-11-10 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 43430146-c4e7-3c71-a911-fbbe24a5a0d8 | -4.61174 | -46.65972 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84a5bc86-328a-34dc-b0a2-e604399b75d8 | -7.89265 | -48.39571 | 2025-11-10 03:57:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aeee2afc-b3ab-3328-98d4-ac3885159295 | -8.20991 | -43.55066 | 2025-11-10 03:57:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1b24bf0b-5d9a-3e58-b0f9-f2acb386fac9 | -2.3445 | -47.03431 | 2025-11-10 03:57:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 77417594-efef-3fd8-aa98-346393d90c78 | -6.6434 | -44.19159 | 2025-11-10 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e02072e-a485-361f-81a6-ab71d2f79e3d | -6.57511 | -42.90924 | 2025-11-10 03:57:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| afde973d-1ac8-3531-88d7-e90d11f10d28 | -1.79076 | -48.06833 | 2025-11-10 03:57:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d90d947-3cd7-34ca-be33-1c36ee635add | -7.34885 | -35.21211 | 2025-11-10 03:57:00 | NPP-375D | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| d696d354-5284-36e9-9cb5-fb9fb02e5d01 | -5.92139 | -43.93456 | 2025-11-10 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a3533f2-4c17-3c1d-8e0f-2119daf63acf | -4.07731 | -44.13115 | 2025-11-10 03:57:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9c57ed32-7c42-3286-a94b-be23a2ebad26 | -2.11301 | -48.18772 | 2025-11-10 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb2ac61-27c7-3b67-832e-f8b5cb5f3599 | -6.43685 | -37.13367 | 2025-11-10 03:57:00 | NPP-375D | CAICÓ | RIO GRANDE DO NORTE | Brasil | 2402006 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d5862165-3dc5-3cec-a957-44bc140b32f8 | -4.02347 | -41.6333 | 2025-11-10 03:57:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| e4dc131d-9518-340b-a5fc-df68e0fe07b8 | -5.89085 | -43.96155 | 2025-11-10 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9cb749c-aa23-34d3-9fdb-75904f8358b8 | -2.26937 | -47.84597 | 2025-11-10 03:57:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f72dffc0-809b-3ee0-af85-e191a4c4c544 | -4.57789 | -46.66861 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 79def4f9-1783-3da0-b3c4-b804e9bbed25 | -3.90704 | -50.03384 | 2025-11-10 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0c15611-b5db-3d01-9337-4c95725881dd | -4.58308 | -46.66951 | 2025-11-10 03:57:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e7f230e8-234d-3176-8fbd-8af8b4d76151 | -5.63349 | -43.92147 | 2025-11-10 03:57:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c519c24-4663-3f55-a4cf-c673787dcae6 | -2.99226 | -48.05988 | 2025-11-10 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a246b13c-3686-3572-80e5-9314e5c648c7 | -3.85933 | -51.41058 | 2025-11-10 03:57:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 17f28fd3-6a17-3a24-ba45-6bd0dffeeffe | -4.63832 | -49.5945 | 2025-11-10 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7449496-419a-3744-b862-85a41ea9dc42 | -3.03625 | -49.49674 | 2025-11-10 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 46be2ae0-deb4-3d48-87dc-d004a26a22bc | -9.30963 | -41.05487 | 2025-11-10 03:57:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c3c2b2f4-20c5-3059-a289-39b1b1e96ccd | -7.63312 | -39.82157 | 2025-11-10 03:57:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ecb287e5-a811-37b3-b3b5-569038bc6d5e | -4.59122 | -45.54903 | 2025-11-10 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ce7a645-e7dd-3820-9ce9-c31c86db720c | -1.79481 | -48.06719 | 2025-11-10 03:57:00 | NPP-375D | BUJARU | PARÁ | Brasil | 1501907 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1e0b4ce4-fbb7-3e19-852f-d82ce426d859 | -4.69391 | -39.41075 | 2025-11-10 03:57:00 | NPP-375D | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a51da282-1d78-35aa-b05c-9f70e1ce97e7 | -2.44591 | -49.33748 | 2025-11-10 03:57:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f42b4df-63d3-3fe9-b57e-3e17abfb191e | -4.91506 | -44.88826 | 2025-11-10 03:57:00 | NPP-375D | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README7.md)
