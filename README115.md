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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d2591da4-a8e5-3c4c-b590-499920da4367 | -19.14683 | -46.62696 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2fea9339-73f4-3227-9fc3-be93dd040cd7 | -19.14636 | -46.63081 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d6fc2c83-a1bd-3abe-b4d5-25724a065623 | -19.14591 | -46.63454 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e881372f-04e8-3820-b087-bd9a4d00de7c | -19.14544 | -46.63836 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a683dc2c-b0d0-3bc6-bf93-684b7a8c201c | -19.14478 | -46.62886 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 75fd8da3-4170-39d7-843f-fe4437a8d242 | -19.1443 | -46.63263 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| b058ce9b-6775-3d1a-929e-d7c3a7d04f96 | -19.14382 | -46.63633 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 970f82ee-86f1-30df-ab2c-12317199fb76 | -19.14332 | -46.64023 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| d3bbba06-c14a-302a-9463-3d7b99379892 | -19.14013 | -46.63222 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| ffbb0bb8-fa31-32a7-85c5-cc200249b72a | -19.13965 | -46.63596 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 20.8 |
| de1b45f6-00bd-3497-959b-dbcb25e7d23c | -19.13916 | -46.63979 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3139e69f-8766-303c-957b-a29e1e2e81a0 | -19.13796 | -46.61624 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 267f7a19-a979-3a04-b3ad-93962a5faa43 | -19.13746 | -46.62012 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d7e7b71-df7b-3be2-a2b4-309f4df884f6 | -19.1333 | -46.61967 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad7243d7-1d46-3c01-b456-18c6026ba48a | -19.056 | -46.44902 | 2024-10-05 04:40:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b678a041-8422-3910-8301-22d18b4169ac | -20.90655 | -47.40783 | 2024-10-05 04:40:00 | NOAA-20 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 390367f6-4e17-3ca1-8e30-811e90371ea5 | -20.79186 | -47.75494 | 2024-10-05 04:40:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f75690f6-a1e1-343f-937b-f0d7254cb306 | -20.79118 | -47.76028 | 2024-10-05 04:40:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d00e451d-98dc-3d87-a217-7a4a2c684473 | -20.78791 | -47.75434 | 2024-10-05 04:40:00 | NOAA-20 | SALES OLIVEIRA | SÃO PAULO | Brasil | 3544905 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f053bdd7-7d7b-3735-9b4c-ed4ef2e3fdf8 | -20.66878 | -47.09346 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fa0965e-f462-3379-b561-31fbe50d5b0e | -20.66566 | -47.08494 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1d0faca1-5f76-3dbb-bf8e-5fdfcd2e0894 | -20.66517 | -47.08886 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4d8dd6ea-9d0a-3f46-aba3-212bfbe65220 | -20.66468 | -47.09276 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b0785aa2-18d8-3e47-b096-ba7583e1499b | -20.66156 | -47.08428 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 20f96b67-f74e-3333-a780-b973cd0251d5 | -20.66107 | -47.08821 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8eed6b58-ead4-3c9e-a3b0-032390379d36 | -20.66059 | -47.09208 | 2024-10-05 04:40:00 | NOAA-20 | CAPETINGA | MINAS GERAIS | Brasil | 3112406 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6c5bc87-3664-342a-89e5-0590c5458833 | -20.48069 | -47.01305 | 2024-10-05 04:40:00 | NOAA-20 | CÁSSIA | MINAS GERAIS | Brasil | 3115102 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2af7ce38-2f77-36cb-9459-6b55c02825d4 | -20.28253 | -46.88024 | 2024-10-05 04:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 18c4f74d-2ded-30f0-a351-efda2c5df346 | -20.27834 | -46.87999 | 2024-10-05 04:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7a3cb5d-95f5-3122-8f5a-167aa943888c | -20.23475 | -47.09292 | 2024-10-05 04:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 877cb85b-5db2-3a33-bbd6-2aced0cbc810 | -20.23068 | -47.09218 | 2024-10-05 04:40:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0395b932-be3e-3e2e-978a-55f95b627584 | -20.19193 | -47.4614 | 2024-10-05 04:40:00 | NOAA-20 | PEDREGULHO | SÃO PAULO | Brasil | 3537008 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8fc6b3e5-09d2-3380-92b1-73021dde55f7 | -20.08996 | -47.54385 | 2024-10-05 04:40:00 | NOAA-20 | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54dcb316-b0f0-3a95-bfbd-16143acf130a | -19.83843 | -46.75845 | 2024-10-05 04:40:00 | NOAA-20 | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 547524b1-6522-3305-bace-596a24c30d03 | -19.75072 | -46.66921 | 2024-10-05 04:40:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62ca5a52-5d94-376e-b023-14fc69177926 | -21.31188 | -47.60683 | 2024-10-05 04:40:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a429a659-bc7f-36d0-9f4b-b1282232d214 | -21.28776 | -47.39942 | 2024-10-05 04:40:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9645e691-1713-39ae-971c-1f6ba249ad91 | -21.28368 | -47.39895 | 2024-10-05 04:40:00 | NOAA-20 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b0af6c70-76f2-34e8-b103-24a1caab8e0f | -21.27866 | -47.40597 | 2024-10-05 04:40:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 891b4e98-8d54-33d5-a90b-3691ff707519 | -21.27459 | -47.40545 | 2024-10-05 04:40:00 | NOAA-20 | SANTA CRUZ DA ESPERANÇA | SÃO PAULO | Brasil | 3546256 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f019cb0-7f42-3d11-b9b3-81d90b9042e4 | -14.00411 | -47.26583 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5b7f3bda-76c6-3c98-8c88-6c1f46c5744e | -14.06313 | -47.91735 | 2024-10-05 04:40:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 85f2265e-40f3-3562-bd62-c60d6bc9c622 | -14.00527 | -47.26869 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c70686bd-1e2f-3a26-b3ff-ae029a26a4b0 | -14.00153 | -47.2682 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| cca7350c-78f4-360d-86ae-6c7c435ae138 | -14.00091 | -47.27271 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 1fc2f9e1-c5ed-38b2-a8a7-2b389ab04019 | -13.99907 | -47.27437 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 44629e53-adef-344b-b24b-41a0499549b5 | -13.99531 | -47.274 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a0aec5f-86c1-3a9f-907b-e7ea193b98f7 | -13.7294 | -48.15733 | 2024-10-05 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5c9815af-2d21-3c91-9ef9-dcb6afa7aa60 | -13.72648 | -48.15252 | 2024-10-05 04:40:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dfae1644-5519-35ef-9116-410791c0d29e | -15.24842 | -47.1446 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5c35e23-e63b-351c-815e-de85a3f9c294 | -15.24459 | -47.14413 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f0f73f7-7aba-3119-82e9-a0c0bf958c05 | -15.24388 | -47.1493 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5b7b8d59-9e2d-3275-9425-b676ffbbf6fa | -15.24006 | -47.14878 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 73d61b46-18de-37f6-bc4d-c0013d4dd07d | -15.22297 | -47.15999 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 00c7dbcb-977b-3bd5-9c95-e01c57a28d1b | -15.2192 | -47.15911 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 2dcfa21a-bd1f-3266-8bb1-4939ac1631fd | -15.20324 | -47.49957 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 15d82b1f-3a00-3f5b-ad67-1394a17eb89e | -15.20252 | -47.50475 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9abe4948-467e-350d-884d-bcd2232ef9ea | -15.19953 | -47.49884 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fd387910-571c-3b1a-acc5-b6ec21e58d1a | -15.19883 | -47.50388 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db681a8f-abac-3135-9cf3-be60a4dbdcab | -15.19806 | -47.50937 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5eb3b307-d8ad-337b-ba67-c01ff99843cd | -15.19439 | -47.50837 | 2024-10-05 04:40:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d4fbf3a8-66fc-3d03-b3ab-af0f4b61f003 | -14.95146 | -47.06325 | 2024-10-05 04:40:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 04fdc631-b9cc-3f5c-9bb2-27f9393d866f | -14.009 | -47.26918 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| e923bbe0-e5b9-3028-a402-e437e197b5e1 | -14.00839 | -47.27357 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| c9ce9905-24b8-3825-92c4-f197e0726777 | -14.00282 | -47.27474 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 9e922370-7a24-3920-a134-b1a9f0708e89 | -14.00028 | -47.27722 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b51a6ab7-1e9e-3d05-bb04-b3f090376531 | -13.99653 | -47.27688 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b6465039-b9ec-3ab0-b518-e9be138c905b | -14.00465 | -47.27312 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 643d95a1-c97a-3e7d-9767-5eb439a0795d | -14.00346 | -47.2703 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fe359abf-0860-37ef-907b-ffdf5188f567 | -14.00037 | -47.26531 | 2024-10-05 04:40:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| fe9d40cc-aa7b-38ab-a901-3d2f686cbdc5 | -14.79484 | -48.09712 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02ca5af4-16d0-315d-9916-b3b003454f3b | -14.77569 | -48.05029 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| db8b72cf-b48f-3bdd-898a-10ca9d792585 | -14.77329 | -48.04113 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2da4d666-4d31-348a-8ade-a2f1747a166f | -14.77269 | -48.04542 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1293cea9-963b-3bfa-ad59-d70ff50bca1c | -14.77209 | -48.04965 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f0004a5c-fbc1-33c3-9ca3-fa8701b8540e | -14.76908 | -48.0448 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e1b09727-2222-3b1a-b4ea-b0221e5cdcf1 | -14.76367 | -48.03086 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b908635e-e8e4-3b68-90d5-06428f3683ad | -14.76306 | -48.03514 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eb35bf04-725b-3b90-9e49-a4905ca49af9 | -14.76247 | -48.03941 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3f05f415-256f-332f-8ccd-bd35a899d903 | -14.29457 | -48.16852 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f426fce9-1264-38a8-b328-ed7717cf6a35 | -14.29396 | -48.17268 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 999b8203-36e0-366e-b98c-2b9c93d4f6d7 | -14.29039 | -48.17217 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| daf80fd3-884c-3627-b4e7-1148861b4110 | -14.28621 | -48.17578 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1d66a4e-c012-35c2-9434-46bb6b7b32d5 | -14.27966 | -48.17058 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cf90af1c-0e73-3dd5-ac01-453d1146117e | -14.27609 | -48.17004 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1a187e54-6e9a-3f2c-8dec-e4223328819b | -14.27372 | -48.16123 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c3274f57-d267-348f-8377-9e2e10230277 | -14.27312 | -48.16536 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 53105245-ecc9-37b1-8192-8c1c707f758d | -14.27252 | -48.16949 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e3750440-164e-3007-8dc3-855ae5b0ecd1 | -14.27074 | -48.15658 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3f416493-3750-3096-8e52-84125b86012e | -14.27015 | -48.16069 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f143761a-8351-3489-8078-47bfc4f1ed13 | -14.26955 | -48.16483 | 2024-10-05 04:40:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 7a8b8dc8-edb0-3d54-8147-001358bebe5e | -16.24152 | -48.01772 | 2024-10-05 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d608a9d-4873-34b4-8bf7-7dfd71ee49f0 | -16.24089 | -48.02221 | 2024-10-05 04:40:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bbbd61b-b977-376c-8b21-529facfd143a | -16.21184 | -48.70485 | 2024-10-05 04:40:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 21aedb53-09f3-3333-816d-a4dce7c9b5f5 | -15.70339 | -48.32042 | 2024-10-05 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a231972-bc07-3a21-8897-f10bb547f7bb | -15.7028 | -48.32464 | 2024-10-05 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e015fb9-1e47-3fca-9afe-725ca76da254 | -15.3794 | -48.59919 | 2024-10-05 04:40:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 048ecfd9-55db-3a7e-97dc-93dcbf61a810 | -15.18637 | -48.07382 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf87d9df-835e-381c-b2d9-4b0910b5f6b4 | -15.18529 | -48.07506 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1564a999-b386-3ba0-b969-77e6c418fb19 | -15.18273 | -48.07336 | 2024-10-05 04:40:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README116.md)
