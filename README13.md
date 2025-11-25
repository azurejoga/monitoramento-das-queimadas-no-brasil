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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4182b3d2-4389-3824-923b-20279374c8c6 | -4.12983 | -48.84581 | 2025-11-25 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54d7c64c-9cb7-3ca2-befe-e6ca0559919a | -2.49257 | -47.82854 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a66f3891-ab9c-397d-a486-6d111299218c | -3.77281 | -44.04266 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b679acc1-abae-396e-9db4-c0a6003d670f | -5.39859 | -47.66269 | 2025-11-25 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d822ae05-53fb-3f71-a7ad-92afb8fbf231 | -3.38779 | -47.1867 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 473c3288-b5f9-3f32-9b4b-65d10b2e5cd6 | -5.54968 | -51.53634 | 2025-11-25 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9876cdf3-4060-31e8-8119-b9b74af6db6c | -2.87213 | -51.80452 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed1a90f4-81a2-3ad8-b60e-80d85216f264 | -3.9472 | -50.61626 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23f71653-9289-3426-8deb-d3fda4238500 | -3.95059 | -50.61679 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0a7d096e-5db7-3ea6-88bf-6ec23f86b485 | -4.08815 | -47.09862 | 2025-11-25 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bccb45f1-af60-3606-b762-adbd1016eb0e | -3.21188 | -46.83048 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| de180536-ddc1-3f57-aef1-88ba30094bab | -3.88739 | -47.23751 | 2025-11-25 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 424b45f5-35e2-3d20-90b2-a8965f9ce60b | -4.33347 | -44.3354 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99f5a066-6337-33a8-b7d1-039c646f9b86 | -1.88488 | -50.21761 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f21907e6-2301-3d9a-ad7b-09fadf5b74c2 | -4.06509 | -44.597 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3f078100-9bb5-380a-8018-253705cf5b18 | -1.85548 | -54.05897 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5bb67f45-3ac7-373e-9cb0-76b6d0301c07 | -3.81638 | -45.5938 | 2025-11-25 04:38:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a163584d-96be-3c1d-9067-f307202a635d | -4.43885 | -47.30153 | 2025-11-25 04:38:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 582da963-7dc6-3fd3-a97b-ecce1a736b29 | -4.16845 | -41.62393 | 2025-11-25 04:38:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| e585cdbc-71e4-337c-af90-3e7d3b731002 | -2.93941 | -48.22805 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fd20d4a6-141e-39f6-a1cb-627db240b2e6 | -3.23319 | -50.8034 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 761c32c3-c569-3d76-a9b7-2aa6615af1ac | -3.20731 | -46.83736 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| d273aa0d-2873-3ba6-9c52-d52738d94116 | -2.92893 | -48.22996 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6237f511-d99f-3f95-a069-9bd7635d6a6f | -2.97546 | -47.73916 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b304bcf2-0c7a-36a2-bcfe-135c2c20c437 | -1.29669 | -53.14832 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7a59e13-2e1f-3749-b7fc-c40ab07a899a | -2.43292 | -50.26142 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bbf729b2-c038-38da-a214-a43b339f348e | -3.5939 | -40.98316 | 2025-11-25 04:38:00 | NOAA-20 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66b681bf-4ca6-3b17-806a-c26f6680d100 | -3.10071 | -44.49921 | 2025-11-25 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1693198a-57a3-32f2-8718-eb19436b3cee | -4.82476 | -43.82828 | 2025-11-25 04:38:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b0ab6c66-3d87-3fe2-aad9-6eb80353e8de | -4.59685 | -44.88167 | 2025-11-25 04:38:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 981aad5d-0999-32aa-9050-e06f11be34a9 | -3.20846 | -46.82994 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 189aeb2e-5e2f-3a88-9b81-c92a79de9bcb | -4.06895 | -44.59759 | 2025-11-25 04:38:00 | NOAA-20 | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 268181dc-b930-3775-bbf0-0e299b58947c | -3.35647 | -45.56848 | 2025-11-25 04:38:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 493f7a6f-6cf5-3ad0-bff0-06195455e9fe | -2.39843 | -45.62647 | 2025-11-25 04:38:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 15f528fb-8aba-320a-91eb-0b687aa6a636 | -6.684 | -43.94709 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2509f003-d2ed-3dae-8772-0c5aa0ac92ca | -3.20561 | -46.82571 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6aa0e332-8323-33e3-aeb2-d259023a267c | -1.15239 | -54.19797 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78c5316a-21f3-341b-a9d4-7e6cea508f06 | -3.22163 | -50.58955 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc68a549-43a7-39f7-9fb0-6e397b564f8a | -3.82007 | -48.87076 | 2025-11-25 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1c3bd59-262d-3f82-ac0a-16cd50e75e3e | -4.33449 | -44.3345 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fee51144-f7bb-3f90-a3c3-a855906db0f9 | -2.46713 | -48.22832 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 618b4837-d9cb-3134-a823-c2ab88e884e4 | -4.04683 | -42.5209 | 2025-11-25 04:38:00 | NOAA-20 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4583397a-60c6-32a1-a3f3-442ff55a4611 | -6.68876 | -43.94375 | 2025-11-25 04:38:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 39453e0f-2791-36ad-89ab-c562d68e3190 | -1.15665 | -54.19865 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3de940cd-6515-3585-93cb-6611776c60c8 | -4.21325 | -39.73509 | 2025-11-25 04:38:00 | NOAA-20 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 25639d6a-ad12-3ec2-b815-e7d80ea9896d | -5.77976 | -44.05301 | 2025-11-25 04:38:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 82f08b92-002c-3195-ad54-c1f3c091e218 | -1.33876 | -53.15652 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 09c85249-f677-3d16-b7aa-659c25ae9c49 | -4.74966 | -44.45152 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10f66905-a5f0-3cc1-becc-9ca5eb9323c5 | -4.17944 | -43.8303 | 2025-11-25 04:38:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dd2eaae1-59f5-36fb-a37c-a63ae6bbde47 | -2.48233 | -47.83048 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9b5431e6-f1ff-39bc-8b1c-d62cd3cad95e | -2.92948 | -48.22651 | 2025-11-25 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d495985f-f9b8-32b9-a843-cb15c792b0cd | -2.98803 | -51.0631 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| eede25af-8a18-3888-a0c1-9de0f2551883 | -3.10146 | -44.49445 | 2025-11-25 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91f913e6-4a06-310e-9d6d-8d16f9684efd | -3.81952 | -48.8742 | 2025-11-25 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 24ef5c7f-9c67-317d-9bea-0e026be0ffbd | -3.15763 | -49.17133 | 2025-11-25 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 89362c80-30a1-3b4e-91d2-03c4398d7ad8 | -3.22221 | -50.58589 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 848e48e7-c5a9-35ed-abc0-4afd6a44ca79 | -4.33528 | -44.32945 | 2025-11-25 04:38:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bbce6911-ac65-3958-a76c-b64884c1ba57 | -4.00756 | -47.25859 | 2025-11-25 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d80ada84-7e85-3397-a8f8-82bce8df4ed4 | -4.60138 | -44.87753 | 2025-11-25 04:38:00 | NOAA-20 | IGARAPÉ GRANDE | MARANHÃO | Brasil | 2105203 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41785d0f-f4a3-3023-a859-8b09b727012b | -5.9023 | -44.00958 | 2025-11-25 04:38:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee05e9a0-93f6-3cdf-bc25-e0003db5b791 | -2.87279 | -51.80041 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0acc94c1-b0ca-37cd-990e-d6b3b88a5a80 | -4.21534 | -45.53031 | 2025-11-25 04:38:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 54aea598-4f84-3f6c-847d-89539d1f0b6a | -0.99443 | -53.17172 | 2025-11-25 04:38:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5939e122-1fdf-396e-8108-e834ebbd4c93 | -3.84613 | -50.21039 | 2025-11-25 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bfdffad1-80ce-370a-9e52-c64554e61f30 | -0.79087 | -52.41977 | 2025-11-25 04:38:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fae7b248-fca6-3ed9-b12b-a9dddb519966 | -3.4191 | -45.45592 | 2025-11-25 04:38:00 | NOAA-20 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd4c4742-980d-3a41-ad9e-261d646126fb | -1.84098 | -45.6095 | 2025-11-25 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 75d7a5ff-b229-3321-beb5-a1c4b8f4dbb9 | -5.41812 | -43.65591 | 2025-11-25 04:38:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 73eeacc8-2ec7-35f5-9e2d-853685f630ac | -4.13261 | -42.9107 | 2025-11-25 04:38:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 1a256a6e-3588-3467-9080-798dd223800b | -1.64031 | -52.05585 | 2025-11-25 04:38:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| aa842380-c1fc-3122-97e0-87e38e313623 | -3.40984 | -49.46616 | 2025-11-25 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02289b1c-5aeb-3c01-9556-91ae5e4e415a | -2.49007 | -47.82456 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7fce45ca-0776-325b-bbbe-f0228d95b170 | -5.35024 | -44.88296 | 2025-11-25 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d44903b2-91ba-3d84-9ecf-616f9e84aed1 | -2.81061 | -52.99964 | 2025-11-25 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c1524fcc-dbc8-306d-8de4-3cf8369d9fe5 | -1.14245 | -48.09401 | 2025-11-25 04:38:00 | NOAA-20 | SANTO ANTÔNIO DO TAUÁ | PARÁ | Brasil | 1507003 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f5b517cf-fe66-3b19-ab9d-cd8555c3d34f | -4.31197 | -50.74453 | 2025-11-25 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2d773c2-433c-3aec-9b57-9faef91239ec | -6.4605 | -43.55445 | 2025-11-25 04:38:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a550eb69-1c16-331c-94d7-b929c148bf72 | -6.12235 | -42.94925 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 78af767f-0763-35c8-92d4-d4d8ccfa4497 | -1.82826 | -45.57459 | 2025-11-25 04:38:00 | NOAA-20 | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a312369e-d2a8-3f58-a9d7-aaf9ba9c3f0b | -4.60961 | -38.68506 | 2025-11-25 04:38:00 | NOAA-20 | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2a77bb4d-ecbb-3eab-841a-7f63962843d1 | -6.89705 | -42.84218 | 2025-11-25 04:38:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3533e5bf-c8b9-3516-beab-c2b94b8e2cc7 | -4.94894 | -42.70946 | 2025-11-25 04:38:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c0a7f56a-b3bd-3de7-bbea-5f968d4995bf | -3.21073 | -46.83789 | 2025-11-25 04:38:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a3d1d631-601d-301f-8b56-6ee8bed5b2d6 | -4.67395 | -45.01118 | 2025-11-25 04:38:00 | NOAA-20 | LAGO DOS RODRIGUES | MARANHÃO | Brasil | 2105948 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 07a7145e-8dcb-3df9-93e6-315aa31fcd6f | -2.0989 | -51.25176 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 270426b9-488e-3ec0-87b3-4625ff431c69 | -5.5886 | -45.18181 | 2025-11-25 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9b75b68c-45ba-3e75-871c-b8e02f7ed9ce | -6.05262 | -43.77601 | 2025-11-25 04:38:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c3096429-3ca2-3603-b1e8-383ec917f8fc | -2.8967 | -50.23349 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e072f769-e3e8-3088-8d0e-879ea1978f86 | -3.97577 | -49.0048 | 2025-11-25 04:38:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a342e806-60a9-3411-b664-473f5429107a | -5.83389 | -42.92744 | 2025-11-25 04:38:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f4bab6f6-7451-3ae9-bfcd-e65f7813b457 | -3.57017 | -43.81546 | 2025-11-25 04:38:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ec1bcd4-2876-3160-b87e-4e8f284bcc07 | -2.4851 | -47.83447 | 2025-11-25 04:38:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1bcb292b-b4df-3016-921f-10dade8b75a2 | -5.34952 | -44.88786 | 2025-11-25 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cda0e90b-af3b-322f-a5d5-b8c4401ed1ac | -3.09304 | -44.49804 | 2025-11-25 04:38:00 | NOAA-20 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 71ef38c2-3836-35b8-931b-93be59f79664 | -3.47317 | -50.79453 | 2025-11-25 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f467aeaa-b363-3acf-9470-a3131d86faae | -2.88225 | -51.81036 | 2025-11-25 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e637027a-30b1-3bba-abf2-facc0597dd3a | -3.1949 | -44.41354 | 2025-11-25 04:38:00 | NOAA-20 | ANAJATUBA | MARANHÃO | Brasil | 2100709 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 549487c3-b636-39ad-9e89-ddea2ecc7f57 | -2.46746 | -50.24084 | 2025-11-25 04:38:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9108f817-8366-3af2-82c9-da7cdde35f71 | -3.76777 | -44.04898 | 2025-11-25 04:38:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 905503e6-ca82-3320-b5c9-604ff65685af | -1.15315 | -54.19963 | 2025-11-25 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README14.md)
