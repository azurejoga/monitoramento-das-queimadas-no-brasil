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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb03fab8-7c2b-3479-be9f-3ec75ccce3fe | -10.64203 | -53.67151 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2236d64f-bec2-3dba-9551-acf7b1fa4e04 | -10.64159 | -53.67345 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc69c1e4-4117-3ede-9167-6686949c96d3 | -10.64102 | -53.67716 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99445d66-d5a0-3519-bcfe-95cdc686eb5e | -10.63708 | -53.67056 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7aaf6d6-5bea-30b8-af05-82ac6e3312e5 | -10.63663 | -53.67251 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 048aa512-6227-3c8f-80b4-d1ce9a04d3c6 | -10.45528 | -53.65248 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c3d7abe1-41d7-33b4-a8ae-0e235313b540 | -10.45421 | -53.65828 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d59f1beb-5fe2-3afb-87fe-89ff083070b0 | -10.94893 | -52.37074 | 2024-10-10 04:19:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 374c2df9-f657-346e-9301-8481e679d9ba | -10.82266 | -53.75092 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 687686ce-fd88-3eda-8f68-44df3bb64151 | -12.98049 | -53.49586 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 83cc79e4-6fdf-37a3-9dec-ec1c91a22817 | -12.97954 | -53.5009 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e705e0e7-905d-361f-9c7a-1d34534e9e8e | -12.97484 | -53.49999 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0eb9b6cc-cf90-3038-8072-20cb77301f85 | -12.8847 | -53.48059 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff0bd596-e156-3a76-8cd7-afcc08d7edd0 | -12.88001 | -53.47962 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 422fd459-3abf-3e83-9cae-27b3e6aa06d0 | -12.87626 | -53.47366 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2686a37c-cecf-31d0-aaef-362fd288b56f | -12.8597 | -52.82664 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 49e9a9b2-0a97-3333-a4bb-e5481faa7c1c | -12.85764 | -52.81905 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41d1be2d-48fc-3d12-b070-921208505f5a | -12.85602 | -52.82119 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 169791c1-9949-3a07-b754-ad678e733329 | -12.85314 | -52.8182 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6cd3241a-8f49-345d-9e2c-d0b908e7f0b8 | -12.85228 | -52.82278 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8795dbe-4ad1-3846-8584-eeb777bcec98 | -12.85152 | -52.82032 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3f15fe75-feaf-3117-a721-1d9f293b869d | -12.84864 | -52.8173 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2a84f6b8-7ea4-3070-b59a-a53f78b3f0db | -12.70293 | -54.12098 | 2024-10-10 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 381cf487-f2fe-315e-977b-8b4b17e84155 | -12.63925 | -53.10838 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c008e23-93cf-3f4a-92fa-96e622275b56 | -12.63465 | -53.10747 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e50cc05e-3538-30a3-9f22-9a7c67ed287e | -12.63375 | -53.11234 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ab07f66d-2dca-383d-ad58-bfac4fcfb2bf | -12.62735 | -53.12115 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b148e78-3e62-3e38-95a1-5f65fd0f0a79 | -12.6229 | -53.14519 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f59b055-4ffd-33ba-9177-1467095a3b8d | -12.62007 | -53.13466 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 627f609c-cd68-3011-8cc2-50379a515708 | -12.61917 | -53.13948 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c81e1768-0e5a-36ce-b4f2-0e47378e5678 | -12.6159 | -53.02915 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1172e950-339a-3cf4-b3eb-6edc4451d4b9 | -12.61132 | -53.02831 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7de74b45-0397-3aa7-a926-cf4e6877546d | -12.60608 | -53.03502 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5c381685-bfcc-37cf-8b27-eb91b8dd6fd8 | -12.60495 | -53.03695 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57029ae8-79b2-3a5d-bdb2-0c93cc22e589 | -12.58342 | -53.05529 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b187fa9b-57a2-36a6-a9b9-d2a0ea25fd17 | -12.58254 | -53.06013 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5b1c441-d597-351b-a326-81387c1b6d94 | -12.58211 | -53.05723 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 366f950c-781c-3673-9755-84a2d44aa28b | -12.58079 | -53.06982 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| eaa2cbca-8bcb-33f6-b8b0-c508714888e3 | -12.58029 | -53.06688 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d4e0b13e-3892-3f4e-a26f-d5a3d982773a | -12.57992 | -53.0746 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 70442ab5-6eaa-3e39-beb5-cbf85a856adb | -12.57938 | -53.07169 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1d1f91d7-96e1-386c-8364-62732f20d8ee | -12.57706 | -53.06413 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97d1766d-b597-391d-b9b3-e1b7693c44dc | -12.57619 | -53.06893 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| d8e520ee-da48-3bba-ab46-20af4c119f69 | -12.57532 | -53.0737 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| af6b9e26-7c92-3b2a-8eac-a3cc212f0121 | -12.57245 | -53.0633 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 46f857ea-c64a-3339-ae8e-f937e38edd8d | -12.57159 | -53.06804 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f502cbe-28a4-3291-a408-022d2eb1654c | -12.56699 | -53.06718 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f092fd50-c4b9-39ac-8299-9dd1254947c2 | -12.48357 | -53.15656 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b8fca18-7c5a-35d1-a6bd-5175dfd762b1 | -12.47895 | -53.15564 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0fc649a4-ff60-3c91-84e9-d0a03892821a | -12.47685 | -53.15364 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0f1aff5-eeff-3f60-8033-e43eef01bf3b | -12.4731 | -53.14784 | 2024-10-10 04:19:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2460c980-3305-33df-80f3-51dd214f1c69 | -0.38048 | -52.04763 | 2024-10-10 04:19:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 571aaa47-aedf-312a-800f-72e48ae45e80 | -1.53319 | -52.95132 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 752c4bef-5007-3034-bdb0-5344ad5775dd | -1.53224 | -52.95374 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13f2461f-10c4-345b-b0d6-75d41baf70d4 | -1.68022 | -52.12434 | 2024-10-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54982b66-577e-3f5d-9207-3b488b1a4eb6 | -1.66156 | -52.14045 | 2024-10-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d40d24d-1bf9-398b-b00c-5ab1de2db6e6 | -1.66125 | -52.1406 | 2024-10-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1229cd39-ae59-3b56-84ea-20a9f133e83d | -1.66103 | -52.14363 | 2024-10-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 11fa582c-b224-3dc2-9dac-3690c4d7142f | -1.66076 | -52.14375 | 2024-10-10 04:19:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 017e2c98-eb88-339f-a0e9-0f70702f0819 | -1.5381 | -52.95597 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7ff1eef2-15a8-3135-9e7d-142d6102caf8 | -1.53774 | -52.95466 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0dab796d-a1e7-3da7-b543-bca9b1f69144 | -1.53285 | -52.95005 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f4d3817c-c537-3b1c-b10f-b221d55e7bd5 | -1.53261 | -52.95496 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 931830c6-bd16-3e50-b0e5-7f893a724429 | -1.53163 | -52.95738 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| e53e3926-3a55-380e-bd64-cd29163cf972 | -6.60434 | -52.89443 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a1b68dc1-cdd2-3d7e-a3ee-9beee677aede | -6.09366 | -52.82675 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 310e355f-541e-35cf-a227-61546b4ab6a1 | -6.09318 | -52.82948 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3bc31484-dd30-3f7e-bf58-599d5e0e9863 | -6.60382 | -52.89738 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 618e8ac0-49f5-321f-906d-2c749a08e5f9 | -6.59845 | -53.07671 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 592c2073-fd67-3b3a-ab51-c4ba9cec8953 | -6.59387 | -53.07283 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e92cf6ac-bcf6-3843-b60f-33aec8231b87 | -6.59897 | -53.07375 | 2024-10-10 04:19:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9b5fbd9-adb3-3837-a486-dba48e642d47 | -8.61801 | -54.59628 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d09b9a8-05c3-3880-8343-8ee7b2c6fbbc | -8.61738 | -54.59975 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2f71f538-7f3b-3707-99dd-b024638310d6 | -8.61675 | -54.60322 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aad4c307-8daf-374f-8c63-27730df1a6c0 | -8.61612 | -54.60671 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 190f00b5-4d7d-3e39-8c53-44df713faa70 | -8.61548 | -54.61023 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a052d5c2-8afc-38f0-80f9-b7c783d7c7b2 | -8.61385 | -54.58813 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f7ade0e8-e286-31a6-ab9e-a504c467b10e | -8.6132 | -54.5917 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 169c7dc7-0c71-3a1e-bb97-3e94634c9e4e | -8.61255 | -54.59526 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 602b6999-01c2-3ca9-aec4-1fb1029f8b74 | -8.61192 | -54.59875 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b1578340-23da-3b5f-be5a-a8cd088ed15d | -8.61129 | -54.60221 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 57af140e-0269-328f-9256-6bc5f3238d21 | -8.61066 | -54.60569 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed23938b-b9a6-3965-91a5-01060d26e6bc | -8.61002 | -54.60919 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2d52fd14-8fd0-3bbf-963e-c1ebf83046c7 | -8.60774 | -54.59072 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 05956485-6c9e-34f3-8d79-47f666625442 | -10.62101 | -54.23368 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63dc5165-35f9-30b7-8c38-699f17bde223 | -10.62045 | -54.23671 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd7dc02a-d6f5-340d-a4b5-1431e74a6db0 | -10.38393 | -54.17752 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19c59d55-4637-321c-a8d8-0de4e14ae876 | -10.38337 | -54.18056 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c885c0b9-2a71-3cc5-9def-774e32262bc6 | -10.37824 | -54.17948 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed7e6c95-40ef-3b98-921e-2064260ad98b | -10.3121 | -53.70641 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| d8e5c4be-4bf7-3e5e-bde9-21e0d44ed0b0 | -10.31146 | -53.70743 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0856d542-3e91-3a6f-9901-fc4f1d3330c5 | -10.30713 | -53.70538 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 91eaa6d2-c201-37fb-ae21-9803bf439fa1 | -10.30648 | -53.70641 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8a4308b0-e9fe-3bf6-a267-9c0425d6235b | -10.30608 | -53.71117 | 2024-10-10 04:19:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 64db4a48-8bf8-35ca-9bce-344966045567 | -10.22056 | -54.30363 | 2024-10-10 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 22f42df2-3c87-345b-b106-2feee96029e5 | -10.21996 | -54.30681 | 2024-10-10 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af9f2e4b-2f13-3563-b083-989db4718811 | -10.21538 | -54.30253 | 2024-10-10 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96e36483-3ccb-39e0-a813-7e2afcc9bebf | -10.21478 | -54.3057 | 2024-10-10 04:19:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f46e6f0-ea64-3498-867a-2bcb94334950 | -11.60355 | -54.68877 | 2024-10-10 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2a4ddb2c-a1df-3b47-b869-e0d625c50e99 | -11.60294 | -54.69202 | 2024-10-10 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README81.md)
