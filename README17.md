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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf90f226-05bf-33cc-899a-b4de2c9424fe | -13.07086 | -42.13982 | 2025-09-20 04:27:00 | NOAA-21 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 16.9 |
| 12c476f7-cb98-3e4d-b933-faecb140ede9 | -9.39365 | -54.69372 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 58b1ba2e-3149-31fd-8968-4ed083ca065e | -12.25469 | -45.28545 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d7e79ade-8d25-3727-8280-015fc9358d57 | -7.79358 | -55.02058 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b63477ab-5d22-3097-8c0a-d5a47feb08c8 | -11.09372 | -41.07293 | 2025-09-20 04:27:00 | NOAA-21 | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 793d8a25-5e41-37b4-9ee4-6f11e7e04080 | -14.43498 | -46.51033 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07315547-432f-368c-9bc9-f444cd5eb09b | -12.08365 | -44.84201 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 76f9c365-5c5f-3a75-804a-300748430f7e | -9.4098 | -54.68595 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2b9027cb-5a5b-330f-bc32-c3ec3537a029 | -12.0866 | -44.84654 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4c7d04c1-7aaa-3614-ab3d-016796d3f593 | -12.08369 | -44.81724 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d6c3edbf-0618-35a4-8562-e28bfeab9014 | -11.45358 | -43.5396 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1ce9b6d3-b4e2-3bef-afe9-0b9aea062a4d | -13.96616 | -45.04919 | 2025-09-20 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 05dd7e60-be4c-3236-97df-91933d6e4cf5 | -13.66436 | -44.30957 | 2025-09-20 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 30a4b29a-3717-38da-a10a-913e63437832 | -9.17448 | -44.63962 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 76a7bc66-6ba1-3dad-b630-19fc309036b0 | -12.09138 | -44.81423 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 87c05e6b-bf90-3a99-a3de-7ed54851bad2 | -9.15515 | -44.8835 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a8d1b67c-7578-3ae9-89ce-4468f0b3f537 | -10.25698 | -48.04055 | 2025-09-20 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec9c5aa9-d7d0-3c2c-8430-b29cdb6d50d9 | -12.44635 | -44.3089 | 2025-09-20 04:27:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aa1383fd-1ffa-36ac-8bb0-a4a29555f74c | -9.51262 | -54.66354 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ce036079-d63f-321c-b1e5-7aed8712d02b | -10.11685 | -44.75619 | 2025-09-20 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6749a46b-a66e-3691-9677-a1c29b32cfdf | -9.33034 | -43.6983 | 2025-09-20 04:27:00 | NOAA-21 | GUARIBAS | PIAUÍ | Brasil | 2204550 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 506af21a-7d5c-3c25-8450-be41af353ab0 | -10.33442 | -46.48038 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b66837f0-06f7-39fe-b552-868748730803 | -9.39911 | -54.68742 | 2025-09-20 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a38b8586-e08f-3fb4-b233-3b6bfc75748c | -10.80101 | -44.08221 | 2025-09-20 04:27:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92d04aae-c38d-3f00-aa15-f06b9424800a | -13.96677 | -45.045 | 2025-09-20 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2354ce76-7cf4-3e8e-9ae6-266bc651266f | -10.02019 | -46.2464 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa40fba7-29c9-3e70-991e-cf363e3eeffa | -12.85572 | -52.99811 | 2025-09-20 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f696e762-bc8f-380d-9087-843f75fc537b | -12.0813 | -44.8334 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 38d32069-09d0-35a7-8cda-37f0b947b5a9 | -10.86017 | -43.1696 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| baaed847-a583-31cd-a38b-56cfe7541ddd | -10.94927 | -44.83212 | 2025-09-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ce86739-cdd2-346b-9653-591a6092be18 | -11.27839 | -47.41343 | 2025-09-20 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8562f756-5611-30a3-85d1-f8d8955fce00 | -11.2634 | -41.50203 | 2025-09-20 04:27:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 90f1c93f-edb2-3f2c-8e3c-d40af2a8ecdc | -12.15276 | -44.93841 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 106dbf24-877f-3fd0-8f27-0319dd6804f5 | -9.17389 | -44.6435 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 18ec63ec-6677-3807-abda-4f2abfb4a076 | -9.02125 | -44.88707 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7782663d-3d09-3fee-9487-d2d8ebb9f575 | -10.0368 | -46.22711 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d6b121e7-ac9f-3050-8f48-cef2fc5c8efa | -10.88476 | -53.74891 | 2025-09-20 04:27:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7addb60f-f3b7-369c-8f8c-6cd108c3e7d1 | -11.67014 | -41.74564 | 2025-09-20 04:27:00 | NOAA-21 | CANARANA | BAHIA | Brasil | 2906204 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ad9fae8-bd82-31b6-aa16-80ab8040714a | -12.8538 | -53.00137 | 2025-09-20 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| d5da3fbf-30c7-3ceb-893f-945d1850dc66 | -10.02462 | -46.23981 | 2025-09-20 04:27:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e75ac990-5623-3352-aed4-232fdb45a883 | -12.85507 | -53.00174 | 2025-09-20 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 0ecce265-f0e2-355a-8334-29a864df0eb9 | -9.11901 | -44.67835 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| b7a89d05-74e0-3335-82e9-fb82d56e660a | -14.43218 | -46.50589 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3acfd00-a20b-3f60-830d-9f3b44722729 | -10.65386 | -44.23598 | 2025-09-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9874a5d8-ed50-3cbe-9316-c9e9ecfb8eaa | -11.15059 | -48.09269 | 2025-09-20 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46148187-326d-3b6d-9278-a34896d63050 | -9.17219 | -44.63125 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| c17b59d7-46f4-315b-a8f9-85b06c823a65 | -13.8756 | -43.4929 | 2025-09-20 04:27:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 7e2e46b0-3729-3aa2-8149-bea3bf42ceec | -11.50994 | -43.6279 | 2025-09-20 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 24c3217f-b795-3699-b768-50b33ce320a3 | -14.44517 | -46.51178 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ab559331-4b7f-3712-99cd-11cbdc408e26 | -14.4412 | -46.51508 | 2025-09-20 04:27:00 | NOAA-21 | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce10d264-9689-350d-ac3c-2c1ebd74faa5 | -10.61145 | -46.44755 | 2025-09-20 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb45fa65-3039-3d64-ae40-687bfa86a35f | -9.40387 | -54.68825 | 2025-09-20 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 72e1abaf-50ca-3713-b20e-e900fdc34a4f | -10.60654 | -49.64129 | 2025-09-20 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0de1b2a9-dea5-3035-aceb-c3d888621c20 | -9.11611 | -44.67405 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 54cb0e67-8e64-3305-b7b4-d1ae6789f0b0 | -10.2343 | -48.05487 | 2025-09-20 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4efeaf23-463c-3adf-9e37-9ad0b6cd76c0 | -12.85908 | -53.00246 | 2025-09-20 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85781d97-fb93-36d8-9b92-05dea1718c63 | -16.32959 | -43.96132 | 2025-09-20 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 137df4cd-80e0-3d9f-9338-b76ac2740e38 | -11.0965 | -44.88571 | 2025-09-20 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c76f226-2ec6-35cf-8b48-a9c6bf89ed21 | -11.28553 | -47.411 | 2025-09-20 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d8c62ce7-ceef-3b88-8671-dd745218aa6a | -12.09014 | -44.84705 | 2025-09-20 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5cf462d0-abcc-3753-a273-d9cd070b2cff | -12.15393 | -44.95494 | 2025-09-20 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b196218a-0c52-382a-b085-1313358e3797 | -16.32869 | -43.96451 | 2025-09-20 04:27:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f4b656c5-04c9-3cd6-b5c5-dbe284d5e7e4 | -9.01429 | -48.02004 | 2025-09-20 04:27:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7f5dd453-faf4-3087-8ca4-55d3d3482fa3 | -12.40001 | -43.81903 | 2025-09-20 04:27:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1bc8d004-7d97-335a-9d99-b8a03a4e5c01 | -10.27429 | -36.33666 | 2025-09-20 04:27:00 | NOAA-21 | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 91f7b8c6-987f-3235-8a63-fe795b3f33ed | -11.14672 | -48.09568 | 2025-09-20 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98b34bca-4580-3584-8a01-1d8d12802a0e | -12.85318 | -53.00499 | 2025-09-20 04:27:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8532d8f0-cebf-39c7-a9f2-bd26b1d02e24 | -9.01048 | -45.05008 | 2025-09-20 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4736b1e-bd01-3535-ac4f-cd9ea5b0bc87 | -19.54736 | -48.04003 | 2025-09-20 04:29:00 | NOAA-21 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd038d24-929e-3674-860c-8b6697cb6d05 | -15.3029 | -56.81518 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| defadc4e-f47c-380a-8607-49ce2e5a0bba | -15.29792 | -56.81445 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0627eae-979a-33ab-b936-86d6a633cf19 | -15.27639 | -56.84643 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| a2596902-0a78-390a-a948-0a232b815f70 | -22.16042 | -42.94042 | 2025-09-20 04:29:00 | NOAA-21 | SÃO JOSÉ DO VALE DO RIO PRETO | RIO DE JANEIRO | Brasil | 3305158 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 61998e4e-617a-357b-9304-719ed9dc7a53 | -22.6387 | -44.52258 | 2025-09-20 04:29:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 98d1fcc1-f1ac-3b09-b99b-289f3cb50574 | -16.11499 | -53.8143 | 2025-09-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67118751-5cde-34a0-b664-61a28eb33b0a | -18.03584 | -50.95185 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 3f6017c1-6f87-34f4-afb8-97051e108e3b | -16.68648 | -54.96775 | 2025-09-20 04:29:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a0b91d2-8e82-3d90-91e0-0fe9bb0b4f1c | -15.28288 | -56.86602 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d47c0ce4-31ab-3e18-9d9e-d9d69089697b | -18.03777 | -50.94036 | 2025-09-20 04:29:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 30697855-08da-34b9-a1f4-4d3a600e8eee | -22.63918 | -44.5185 | 2025-09-20 04:29:00 | NOAA-21 | SÃO JOSÉ DO BARREIRO | SÃO PAULO | Brasil | 3549607 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| fcf7bde1-d7c8-3f20-8843-b5ec3da64573 | -15.92477 | -59.43031 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 33aa31c4-c5cb-30f3-8b39-4e025305ff37 | -19.61639 | -57.74344 | 2025-09-20 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 867fc242-ed33-3173-a4b6-1e8ec53b0771 | -18.3278 | -55.04066 | 2025-09-20 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 10fc3829-39e7-3e2a-8158-a03f3a991f2e | -18.33121 | -55.04549 | 2025-09-20 04:29:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 12.7 |
| df8ab31d-901b-35e1-8b83-2486a182c559 | -15.33916 | -59.40272 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ab26d8a5-f598-3a75-a3c2-dd2c10c7b2c4 | -15.29305 | -56.82052 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c71023a0-f38e-3314-a08b-6616ca398de8 | -15.28703 | -56.81785 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6bfe041d-f95c-3ae0-8cf0-75236586a328 | -14.58287 | -56.92317 | 2025-09-20 04:29:00 | NOAA-21 | DENISE | MATO GROSSO | Brasil | 5103452 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fdc4d09f-099b-3765-bc56-aaccfd2044c0 | -19.60677 | -57.74129 | 2025-09-20 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 9e6ce4f1-2b49-3d65-8d79-76194d9ec047 | -16.81084 | -42.98063 | 2025-09-20 04:29:00 | NOAA-21 | BOTUMIRIM | MINAS GERAIS | Brasil | 3108503 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ae30636-65f5-3335-b957-c5d4ee716e6a | -19.61524 | -57.74905 | 2025-09-20 04:29:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 3f1d20be-4650-3eb7-9d55-fcf84cba5660 | -15.92068 | -59.44982 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1d95e0da-d145-398f-8734-a2e05ee83de4 | -14.83902 | -60.25597 | 2025-09-20 04:29:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 11b4b1bb-5b9f-39c9-a05b-4938d89e505a | -15.31166 | -56.82289 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| beb4f7e8-2da9-3096-8e5a-cfd7306f250c | -15.31005 | -56.81234 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fd9804fa-8851-321c-b0f7-8e82494ad20f | -15.30888 | -56.81068 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 17f527eb-d57a-39bc-a199-df18e4e85783 | -15.91986 | -59.45377 | 2025-09-20 04:29:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4d41d6e1-35b0-380d-961e-6359bb4faddc | -16.11165 | -53.80996 | 2025-09-20 04:29:00 | NOAA-21 | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| df04e43c-dd23-31cc-9733-8e6407df4b2e | -15.29195 | -56.81888 | 2025-09-20 04:29:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3731a1c6-ba98-3896-891f-98bc63d51bb7 | -20.84526 | -49.35974 | 2025-09-20 04:29:00 | NOAA-21 | SÃO JOSÉ DO RIO PRETO | SÃO PAULO | Brasil | 3549805 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
