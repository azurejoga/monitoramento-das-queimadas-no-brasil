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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bff8d297-8d22-396d-a2c4-1eba957fe29d | -9.03073 | -52.09542 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f9b86b4-e67c-3542-a0c2-60dad8fda38a | -8.9389 | -52.12092 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36178be1-88b3-3a62-814c-743e3ec8bd9a | -8.93244 | -52.79557 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9d3f17dc-5e8d-39d2-9008-23b114a8cf7d | -8.92414 | -52.84406 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1fe22465-941d-32ac-b5e2-d318685278ad | -8.859 | -53.01531 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ef21fd7a-25f7-32a9-9c68-0a11fceaf61d | -8.85541 | -53.01026 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dda4da22-cbe6-36ad-baea-7a0634c04d70 | -8.85399 | -53.01843 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 28505402-6aae-3ffb-a7c0-0728f999abc3 | -8.85399 | -52.99284 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b3e3545-7ee9-3778-8431-3b304067333d | -8.85326 | -52.997 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b82be3df-fe9d-3d14-aba7-b49536a11a71 | -8.65639 | -53.06176 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6c6029c6-0f12-3586-885f-8f8d70f0c682 | -8.65564 | -53.06613 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 01d7ba00-1362-3193-a060-7a341ff0276a | -9.04289 | -52.09789 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 731e8c10-5749-3e44-b5a1-7199262d5219 | -9.02665 | -52.0948 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3d9aecb4-0d7d-3bbb-95b2-84b80f14e97d | -9.02255 | -52.09424 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2569a0ba-278d-3bad-a324-9de6ecb01859 | -8.99881 | -52.086 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 26a205a9-ff0d-31fc-b90d-187c073eb152 | -8.99822 | -52.08944 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 28b6f6e9-1bd4-3f84-ab19-7dd7df12ddd2 | -8.94169 | -52.12929 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a67b399-513b-3fa8-a61c-1a444a23a668 | -8.93946 | -52.1176 | 2024-10-11 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3880d7bf-bb15-37b3-9df7-879535f66c3e | -9.78748 | -53.16576 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b157193-7ffe-3fb2-801c-0255aaa31432 | -9.74363 | -53.15141 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 328de2b7-2f48-3ddc-9c45-4c74c6b2aa46 | -9.71276 | -52.82761 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c5713fb5-7566-3b01-8e9f-480aba09628e | -9.71118 | -52.83448 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6f7c6194-5fab-3a79-b4e7-60377400a2bd | -9.70781 | -52.83115 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2574c24f-81fb-30a0-9359-4d7c30587af1 | -9.70615 | -52.83827 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b41d109-258f-3bd5-aa59-08ee559f7619 | -9.66041 | -53.11888 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6e475855-108e-3ce2-953f-c37cc1aba123 | -10.70522 | -53.03984 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60b2f142-d4f1-37f3-aeab-42079ecfe334 | -10.70382 | -53.0478 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9b7c4f44-3486-3339-af17-b17edd3005bd | -10.69961 | -53.04697 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f727836b-bc02-3d1c-96f7-852120d32443 | -10.69823 | -53.03017 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7acad1c-3169-3a9b-8dee-095db38c119b | -10.69473 | -53.02539 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8dbd953c-32b7-3ff9-96a5-173545f4798e | -10.6947 | -53.05016 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6b7bf506-1aa3-3470-b56c-d5a2e3334bf1 | -10.69403 | -53.02936 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b7be89c9-e375-3fdf-82e5-733a7923d6ab | -10.69332 | -53.03336 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 892a0d9d-312b-3e2f-86b8-6c51af3b454b | -10.69052 | -53.02462 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1707fb1b-721b-3eed-adbb-60c13b13c93e | -10.68982 | -53.02858 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 857d71e3-0ce8-3b08-bfac-64637fb99325 | -10.68911 | -53.03257 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 23b6fe82-2a28-35a4-b13f-e7d0e5a409fe | -10.6849 | -53.03182 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a81e2a6c-2bca-3d01-be57-2d93333b6381 | -10.63756 | -53.67888 | 2024-10-11 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 317a7cae-daed-3c84-8525-03a1ad8a18a2 | -10.63392 | -53.67374 | 2024-10-11 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 305f90f5-e1d7-3164-b910-7d32851d3035 | -10.62952 | -53.67294 | 2024-10-11 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0d639f40-5129-30ec-89d2-f4f593e06385 | -10.62512 | -53.67213 | 2024-10-11 04:25:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc7e163c-a8ad-37e6-9132-83d67df06422 | -10.6065 | -52.88455 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 682a3408-f8fa-35a6-8ce1-42463fbc753e | -10.60582 | -52.8884 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fcd8d8b0-e331-306e-a43b-b34522b8916e | -10.24075 | -52.7617 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5109fdf-7870-31ba-9488-7fa134bfda78 | -10.23659 | -52.76092 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4ed97e96-919b-3b24-9ac9-55f68bf14147 | -10.23242 | -52.76015 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cd79477f-303d-378f-91e8-dd2d1e7d6359 | -10.23175 | -52.76402 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2580786b-d84d-311e-80fa-a611ba84dc1e | -10.22825 | -52.7594 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8154f9f3-4032-3637-ac9b-6e64017b87e6 | -10.22758 | -52.76325 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6a94585-29b1-32d4-a782-5c6e01c43110 | -10.21884 | -52.69025 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 977d1c89-d629-3669-a3e1-e50e49a696fa | -10.21816 | -52.69412 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27fceb6e-322d-3c58-89b1-15f5aff356cf | -10.20985 | -52.69267 | 2024-10-11 04:25:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e4de649-7a24-3991-91df-11d78fffc41e | -10.89916 | -52.33889 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 884e055d-1a6a-3daa-ab3d-232078d1a2c8 | -10.89854 | -52.34243 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 913dfed3-bfdd-3746-823b-3c719e2c230b | -10.89791 | -52.34598 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f55ea0c8-dfe1-3cf1-9a0f-e2e1f884c19a | -10.89728 | -52.34958 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 84118869-88ed-31cb-bc13-ced43f526c19 | -10.89515 | -52.33817 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8109ce45-754d-3994-91ea-f76b6ea545fe | -10.89452 | -52.34172 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67df6b34-47c6-39e1-8fff-7b85be6e2ae3 | -10.89419 | -52.4379 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 806a1489-5920-333e-bcfe-90d9cf6fda8b | -10.89389 | -52.34529 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7ca458a4-a84b-37cf-b6c4-bb00835469b9 | -10.89326 | -52.34887 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 147345f6-c993-3a56-a5f5-2c87f40ccecd | -10.89112 | -52.33751 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7255fd18-949f-31c3-a5c1-aee97d033243 | -10.8905 | -52.34106 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c6807a60-54e1-3319-bb72-a114c87bd2c7 | -10.88987 | -52.34462 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8b32b05-85f8-3ddf-8b9e-9f2226f7c34f | -10.86892 | -52.38906 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6025fa3e-ab7c-37b4-be24-f697e4e6fc3c | -10.27103 | -52.17607 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0dc64af8-1ac0-3f9c-ba0d-4722bcb7a67e | -10.26764 | -52.17183 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a7eae4bc-cfef-39e2-93fa-d7bdf5109251 | -10.26702 | -52.17537 | 2024-10-11 04:25:00 | NOAA-20 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 074798d7-10e6-3205-9275-ac8980a722d8 | -10.05204 | -52.08244 | 2024-10-11 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b169f33-faee-3ed2-abc1-d05cd599f6e3 | -10.05145 | -52.08598 | 2024-10-11 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8a6538f3-4a80-35dd-a313-62555cc2fdd9 | -10.02442 | -52.09933 | 2024-10-11 04:25:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 04ba1d49-add5-38c7-9f6f-629bc41e69cf | -9.71424 | -52.84454 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b079e840-2a25-31ed-8cdd-798167b2b95c | -9.71398 | -52.84327 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8b0a7a89-c785-37bc-bccd-570b77061f44 | -9.71262 | -52.82643 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7c464221-3105-3952-9bad-7104d80c79bf | -9.71208 | -52.83162 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0c09e681-0521-3002-91f8-8b8355aaea8d | -9.7119 | -52.83045 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 917c121a-37ff-37be-88c1-2362d1b537cc | -9.71139 | -52.83569 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5b4a7e6-1b3a-3e2c-8895-2c3556d42216 | -9.7107 | -52.83977 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a00090e8-bdd1-36b1-ac10-b929a42fbf19 | -9.71045 | -52.83857 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ef82548-1601-3c97-bf84-fad8be75d3e6 | -9.70999 | -52.84389 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0f5b9dff-de36-329e-b906-61948116fb82 | -9.70972 | -52.84269 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 649c6f53-a25a-3569-843d-c3ddc58cb05e | -9.70763 | -52.82996 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e97d048f-e0c8-3cfb-974d-11587e07a1f9 | -9.7071 | -52.83531 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ff4338a0-2b54-393c-a3b1-1a66f2fe3ee0 | -9.70689 | -52.83411 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2046fdde-5408-3356-ad0e-66f52b398ae0 | -9.70639 | -52.83948 | 2024-10-11 04:25:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34c41022-dd64-351f-8a8f-7df153c1bef3 | -9.63754 | -53.16385 | 2024-10-11 04:25:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1aac14c3-d8e4-3cea-870b-0a27a0c14a74 | -12.04992 | -53.52208 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94936b63-22d6-354a-a2ab-fc1a42971c97 | -11.53916 | -53.84857 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b97c0e3c-6ce8-37af-849f-98c6d5b91047 | -11.53839 | -53.85284 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| de7f3333-53ae-3715-a546-154cf691034d | -11.53761 | -53.85718 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 532490aa-19de-37dc-9ff2-68cd3d3ef0b7 | -11.53477 | -53.84778 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f88590b6-e4ed-380f-b1b6-a70e07b5554f | -11.534 | -53.85205 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35ec84e7-f880-3311-8f1f-de3130965374 | -11.53323 | -53.85637 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2e7e36a7-c061-3116-8105-4f7c2bbc756d | -11.53244 | -53.86073 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 90e33575-47bd-3d48-9083-ac4f034daaa2 | -11.52961 | -53.85127 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aba07304-a511-3dc3-8eb1-da5681332a5b | -11.23376 | -53.27147 | 2024-10-11 04:25:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 31c19841-f5e9-3719-a788-61c3b3e36625 | -12.85921 | -53.4722 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 9d442b6e-48fd-3eee-8f65-ea9a434382c9 | -12.85915 | -53.49347 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6fe0b9bc-62d3-3de0-8c7e-ac5dfb197525 | -12.8586 | -53.4519 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f6d74a25-4d2c-3b38-9340-f53c561a2282 | -12.85846 | -53.49742 | 2024-10-11 04:25:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |


[Clique aqui para ver as próximas entradas](README64.md)
