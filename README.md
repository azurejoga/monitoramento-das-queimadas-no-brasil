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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a52e7833-87e6-3698-902f-d071381380a7 | -10.0082 | -36.2463 | 2026-03-17 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 143.8 |
| 212c71a1-232d-3acd-8b93-1aa04028b4bc | 0.8295 | -60.3342 | 2026-03-17 00:00:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bac6aea3-99db-3bb8-9ac6-d747a2d8dad5 | -10.0087 | -36.2192 | 2026-03-17 00:00:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 259.3 |
| bcc289c3-b995-3000-8c3c-02e8b673fbaa | -10.0662 | -36.2359 | 2026-03-17 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 89.4 |
| 8ee1e453-f97e-328b-b7d4-31d0c969cb88 | -10.0855 | -36.2324 | 2026-03-17 00:10:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 76499ca9-db37-3702-9d12-70fc993a012b | 2.7798 | -61.1864 | 2026-03-17 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 12f9527d-3cbd-3bf1-96f3-bdce1ff22545 | 2.7981 | -61.1861 | 2026-03-17 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 55.6 |
| 8c5a1dea-b85e-32bd-b9df-80a7b41b0f27 | 2.7798 | -61.1675 | 2026-03-17 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 89.5 |
| 57f2dda3-87e7-3ff1-8b43-67cb955ed442 | 2.7981 | -61.1672 | 2026-03-17 00:20:00 | GOES-19 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f8e2ce60-ce78-3a60-be7f-455bf864ac21 | 3.146 | -60.7265 | 2026-03-17 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 124.4 |
| 068e8261-13de-3288-bdda-0759b69eb49e | 3.146 | -60.7075 | 2026-03-17 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 90311baf-ae4a-330d-9b34-0e5a1c1052dd | 3.1277 | -60.7268 | 2026-03-17 00:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 931a0a2d-369f-3093-a825-e5a446a1f476 | -21.35937 | -47.06948 | 2026-03-17 00:39:00 | TERRA_M-M | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 45a1450a-2af4-38bc-a00d-8d4f21893929 | -21.70712 | -48.44543 | 2026-03-17 00:39:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7cd51d8f-ada6-3ed9-b648-4e87b13fc4a7 | -21.70505 | -48.43281 | 2026-03-17 00:39:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 8e75417f-0b6b-3769-b4a1-7677b112e5fc | -19.98757 | -54.73802 | 2026-03-17 00:39:00 | TERRA_M-M | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1a8dcf9b-52e6-3590-a8ec-26bbba6e3daf | 3.146 | -60.7265 | 2026-03-17 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 9aaad620-1f0f-3f25-86dd-101422f78be9 | 3.1277 | -60.7268 | 2026-03-17 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 0fdedd8b-8d51-3607-9679-8b3ae74d45d4 | 3.146 | -60.7075 | 2026-03-17 00:40:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 2063f729-8b7b-3680-98e2-0c76dffc6148 | 0.83578 | -60.33533 | 2026-03-17 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 84263e20-81d7-3e1a-b806-6e88dbefa9a1 | 0.83419 | -60.34697 | 2026-03-17 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| dd39b8b8-42e6-3f4b-a5f6-12f7b0db800f | 0.83461 | -60.3414 | 2026-03-17 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 24.7 |
| d2880212-c338-371c-b04d-7c7accdaebb0 | 0.83627 | -60.3298 | 2026-03-17 00:45:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 86fc2ece-9ab0-32c8-8696-06bc82f9650c | 3.10864 | -60.82713 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8260e3e3-c58f-3fe3-b906-b2c799a653fa | 3.18837 | -60.12762 | 2026-03-17 00:48:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 53886ed9-c2c3-322d-8d38-2ea94bf33b9d | 2.79434 | -61.16881 | 2026-03-17 00:48:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b86c057a-cfc0-39a3-87ee-3903a4bab67f | 3.14181 | -60.73751 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 4ecdce60-07b5-3191-9c54-d180b61b07e0 | 3.13368 | -60.7952 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| b252b95e-9943-388f-b8b9-cd43264d4163 | 2.7822 | -61.17974 | 2026-03-17 00:48:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c756cfea-0cf7-39d3-8e10-a1c6f3f2a23a | 3.14565 | -60.85626 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 06a8de1a-d631-3998-a844-e3a05fe4de38 | 2.74459 | -60.43173 | 2026-03-17 00:48:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0067be64-7bd6-305d-8902-39688079484c | 1.47982 | -60.04327 | 2026-03-17 00:48:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 3f52c57a-8247-3f18-8654-f527c75be1fd | 3.14343 | -60.72603 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 132.9 |
| f0131a13-543f-3493-8c31-7021fa52ffaf | 3.72942 | -61.2883 | 2026-03-17 00:48:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 87a98b60-5271-3fac-990c-ace56eb1748c | 2.74305 | -60.44287 | 2026-03-17 00:48:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 92c13672-117b-3910-92d9-31bac28b2b78 | 3.72769 | -61.30061 | 2026-03-17 00:48:00 | TERRA_M-M | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e36e0a04-8e9d-3fdf-ab67-61e260c541b8 | 3.14505 | -60.71455 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 22.0 |
| d3ff33cf-659a-3b59-b0cf-0198b9479fd1 | 2.4007 | -60.2566 | 2026-03-17 00:48:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 234c70b9-562e-3691-a731-9302404fbf77 | 1.47829 | -60.05422 | 2026-03-17 00:48:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a7b7d466-2f2d-353f-81ad-993e3370259e | 3.14402 | -60.86797 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 203e5bf9-b718-36dd-a244-f8bd79804d52 | 1.32632 | -60.70692 | 2026-03-17 00:48:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9d75d106-f5a0-3a61-ac1f-3d8f1cb18b54 | 3.13181 | -60.73608 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 4578ca29-9e7f-32ff-b77d-c1398631627a | 3.13557 | -60.8548 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 411612e5-8b46-3fae-b647-08cf869ee5f5 | 2.73318 | -60.44147 | 2026-03-17 00:48:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| e99d3fd7-3eef-3839-9b1c-f7ea3b15b1eb | 3.13344 | -60.7246 | 2026-03-17 00:48:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 6069f3c8-153b-327e-9a23-3e3b49300bcb | 2.79258 | -61.18122 | 2026-03-17 00:48:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 673f3030-e0da-3116-bbfc-d1376014d1c4 | 1.64065 | -60.28216 | 2026-03-17 00:48:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8563df62-34fb-3a49-9bda-7e842b190c96 | 3.1277 | -60.7268 | 2026-03-17 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 83.0 |
| cee92bfb-2c91-36ac-a35a-58928488e4d4 | 3.146 | -60.7075 | 2026-03-17 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 56.6 |
| e3c0e7c3-50e0-3ca0-bbda-2ae217feb377 | 3.146 | -60.7265 | 2026-03-17 00:50:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 98.6 |
| aa9523ed-e777-3185-9f21-500bc153167d | 2.7478 | -60.431702 | 2026-03-17 00:57:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 57636f09-6dff-3d5d-a07a-543289482931 | 1.6407 | -60.275002 | 2026-03-17 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1712d5ee-658d-3b2c-b282-b5eea6d6080c | 0.8346 | -60.333599 | 2026-03-17 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 277cb6a9-3188-35a5-a174-53dcb8e5da05 | 3.131 | -60.787498 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| c71ae8e3-e048-387c-956b-d328a8cc86d5 | 1.3303 | -60.692101 | 2026-03-17 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d2c34c6a-0e8a-3f81-9f85-1c9278f5333c | 2.7398 | -60.421902 | 2026-03-17 00:57:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a6c9e1ee-eb63-3ab1-9766-e39948970749 | 1.3286 | -60.699402 | 2026-03-17 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| de98f05f-457d-3a04-b3e6-9096cab5b572 | 3.1463 | -60.7197 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e2bc2cb-112d-3511-9c92-36b3732f2d85 | 0.8363 | -60.326099 | 2026-03-17 00:57:00 | METOP-B | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| a74738a7-86a3-3afd-b983-55132d7275c3 | 3.133 | -60.7327 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 672c15c9-f3d1-3826-9d31-b0cf8133d846 | 3.1364 | -60.717602 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 47f6ec18-9648-362a-a3b9-71c98f75c1f2 | 3.1372 | -60.851799 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f69d27ad-8c15-3d64-9fbb-0c101a64d555 | 3.1389 | -60.844299 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0dd57e58-3afd-3324-b0f3-740f383fed87 | 3.0854 | -60.7617 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 136ebd33-125f-3fcf-a214-d97aa454f027 | 3.1347 | -60.725201 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d72f18e6-b43e-3499-a6b2-1f72f6c641d5 | 3.1887 | -60.117401 | 2026-03-17 00:57:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6183a59b-5b36-3e47-9d2e-5c5aa392dbc0 | 3.0186 | -61.104698 | 2026-03-17 00:57:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| cdf1bc42-7597-37a6-9ceb-a84004e2bda2 | 2.7363 | -60.437302 | 2026-03-17 00:57:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| e3280d9a-1cb9-33d4-bdfc-f51caed41758 | 2.738 | -60.4296 | 2026-03-17 00:57:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| f017368d-4376-30dc-b4a3-93495918cbc2 | 3.1355 | -60.859299 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 230314c9-798b-3021-a3cb-150fe610ec65 | 2.7881 | -61.168301 | 2026-03-17 00:57:00 | METOP-B | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 7e8a6f20-91fb-3120-bd44-fbea3fd59a96 | 3.728 | -61.292301 | 2026-03-17 00:57:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 64403964-a6ce-3052-9629-2bcc8471f1b9 | 3.7296 | -61.285 | 2026-03-17 00:57:00 | METOP-B | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| dc1c6a8b-7015-38a2-8c7c-8e4883468b30 | 3.1381 | -60.709999 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 1788c5dc-c0a8-30d6-8918-7b037e739ec8 | 1.4782 | -60.036999 | 2026-03-17 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 2bcca85e-2e55-3ed6-98ec-f50b6dcfb4c3 | 1.4764 | -60.0448 | 2026-03-17 00:57:00 | METOP-B | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 69173c86-e07f-39d5-9f92-3a4477aacad5 | 3.148 | -60.712101 | 2026-03-17 00:57:00 | METOP-B | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| d72a6e84-efa1-3f29-8360-81338ecc0846 | 3.1277 | -60.7268 | 2026-03-17 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 2875d3d2-84e5-3744-9241-b0af3d2cd436 | 3.146 | -60.7265 | 2026-03-17 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 07994c7e-3e05-3af6-94f4-29c43cfa12af | 3.1277 | -60.7268 | 2026-03-17 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 655edc57-b406-349a-a3c6-0f9607252836 | 3.146 | -60.7265 | 2026-03-17 01:10:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 3c29c33e-1bc5-3677-9291-7fa395bf5a4a | 3.1277 | -60.7268 | 2026-03-17 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 64.7 |
| 491a1549-50d0-39fc-809a-584603d031ee | -10.0656 | -36.263 | 2026-03-17 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.2 |
| 9c7155ad-8691-3d40-b55d-62ee3639eb14 | 3.146 | -60.7265 | 2026-03-17 01:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 4d1725a4-c7c9-3c5d-abcd-4acc25750227 | -10.0662 | -36.2359 | 2026-03-17 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 100.7 |
| e0611de4-eadd-344d-9518-9df445af7565 | 3.1277 | -60.7268 | 2026-03-17 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 57.5 |
| dc607f13-d1f0-3255-892a-1bcd0c0bb1fb | -10.0662 | -36.2359 | 2026-03-17 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 229.8 |
| 7afc4d5c-e5a3-364d-8bef-ca2df723f8a7 | -10.0855 | -36.2324 | 2026-03-17 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 118.4 |
| e26285e3-671b-3ac1-a780-d2a158c9739c | 3.146 | -60.7265 | 2026-03-17 01:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 61.8 |
| f949ee3c-d327-3499-ac8d-4a07a2a98801 | -10.085 | -36.2595 | 2026-03-17 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 108.9 |
| a3c37dc6-452f-3bd1-85e7-64f748e91ac9 | -10.0656 | -36.263 | 2026-03-17 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 251.9 |
| 9bfbf4ce-f9f1-35d9-9b96-1928b32f9d13 | 0.8295 | -60.3342 | 2026-03-17 01:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 43.6 |
| cb4709dd-6e09-3d92-b680-66472b69a54b | 3.1349 | -60.7365 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b5155496-1c12-317a-bb9a-b5c1bc207d6e | 3.1051 | -60.8228 | 2026-03-17 01:31:00 | METOP-C | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| bd2365c7-237f-3617-85c1-b19b9445659b | 3.2282 | -61.1884 | 2026-03-17 01:31:00 | METOP-C | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 5bd0f284-1979-3023-a904-1d192c218df5 | 0.8373 | -60.3367 | 2026-03-17 01:31:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 568652c4-1a0c-392f-962d-abdc61ed0a18 | 1.4712 | -60.040298 | 2026-03-17 01:31:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 6ac40292-4259-3709-b4d7-e13707893597 | 1.3207 | -60.7005 | 2026-03-17 01:31:00 | METOP-C | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 331f9de4-fd3d-3e21-be53-387e69983829 | 0.8275 | -60.334499 | 2026-03-17 01:31:00 | METOP-C | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b41aacea-2150-3ca2-aca4-a4d93964c8fa | 2.742 | -60.426701 | 2026-03-17 01:31:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
