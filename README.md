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
| 86cf3e3e-ae91-3ce0-9804-4f183717411f | -20.1953 | -46.4546 | 2026-05-04 00:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| fac30cc7-8e54-3363-bb58-a86bc8edc731 | -20.1748 | -46.4596 | 2026-05-04 00:00:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 72.3 |
| dd51b8a4-3a09-35a4-b1cd-92de8d1931ad | -10.9784 | -45.0877 | 2026-05-04 00:01:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0bb3f909-9d77-3c8d-9fa4-4cfdcdfe786e | -20.1752 | -46.472401 | 2026-05-04 00:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c927331e-338a-35a0-a2a3-bfdc7220aaef | -10.9686 | -45.0896 | 2026-05-04 00:01:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 36838b0a-599a-3f33-9e00-4d38a78a5747 | -17.4041 | -42.635601 | 2026-05-04 00:01:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 207b445a-d2f7-339e-941d-abffebf315de | -9.7327 | -37.249699 | 2026-05-04 00:01:00 | METOP-C | PALESTINA | ALAGOAS | Brasil | 2706208 | 27 | 33 | nan | nan | nan | Caatinga | nan |
| c79cac00-505a-3af8-907f-a8dc76c3d767 | -10.9818 | -45.104801 | 2026-05-04 00:01:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e840d010-a3a9-3cc3-aa8b-a92a23ac5149 | -20.165501 | -46.4739 | 2026-05-04 00:01:00 | METOP-C | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| b7c055bc-1fd6-3ec7-adee-a1edc41c85f2 | -17.4014 | -42.620899 | 2026-05-04 00:01:00 | METOP-C | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| bab26259-56bc-33bc-b3d5-fa1b6490fe21 | -20.1953 | -46.4546 | 2026-05-04 00:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| b617057f-2e66-3fb5-9855-8428eba88bee | -20.1748 | -46.4596 | 2026-05-04 00:10:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| f5b42cac-d34a-3237-bae1-2dfc0e794361 | -20.1748 | -46.4596 | 2026-05-04 00:20:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ea4444b6-e49d-3729-bd14-ba52dd98ab04 | -20.1748 | -46.4596 | 2026-05-04 00:50:00 | GOES-19 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |
| da3094a0-ae9c-316a-805f-687fc9895159 | -16.59581 | -58.24047 | 2026-05-04 00:52:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.9 |
| 9bf9b05e-e7a2-3cfd-88be-1378225bec77 | -20.18402 | -46.48153 | 2026-05-04 00:52:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 95c7e1b1-29d7-3c1a-b3db-f36f2a481937 | -18.04996 | -52.99927 | 2026-05-04 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4fdf3e68-bb94-3ba3-8133-388015ebec70 | -20.16689 | -46.47992 | 2026-05-04 00:52:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 54.9 |
| 05da942b-a4d3-30a5-aa19-b118cda8cf5a | -20.17434 | -46.47569 | 2026-05-04 00:52:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 4bcd4edd-503b-3a14-8a62-e9aef787de49 | -14.32758 | -57.73753 | 2026-05-04 00:52:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| c27d2ba4-7bed-3ccb-b52a-164d7e3bf5f0 | -18.08471 | -52.97359 | 2026-05-04 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 98d06e0e-7f93-3956-a613-a7a6eb1987aa | -18.05562 | -52.99239 | 2026-05-04 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 2fa95d99-3ffa-385f-a2f9-e49a7c4d228d | -18.07429 | -52.97545 | 2026-05-04 00:52:00 | TERRA_M-M | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 12.7 |
| a60a8573-10e2-3069-91a6-b9517f1cec36 | -11.92067 | -54.82042 | 2026-05-04 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 80faeb91-21e1-333c-952a-6fec9f7b4571 | -11.91052 | -54.82203 | 2026-05-04 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 335e004a-c912-3eaa-a031-d087bbf69d46 | -12.3649 | -50.03556 | 2026-05-04 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 865cbd4f-9107-38e5-9cc3-e06a4f6c79ab | -12.44212 | -54.2152 | 2026-05-04 00:54:00 | TERRA_M-M | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| b903ca7a-9db0-33ba-89b6-a82c7e4ea128 | -11.84676 | -55.00969 | 2026-05-04 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 979ea1f6-16c2-3f39-ae5d-94c39c55836a | -11.84854 | -55.02152 | 2026-05-04 00:54:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 17508a92-6998-3576-84f0-66ae9f227658 | -12.3657 | -50.02976 | 2026-05-04 00:54:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 45.0 |
| dfa9919c-971b-3bfa-8587-fccb50d88dbf | 3.41204 | -61.08199 | 2026-05-04 00:56:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d9df8713-6d8b-36ce-9bf2-075747ce6a93 | -16.5972 | -58.231701 | 2026-05-04 01:07:00 | METOP-B | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 563aa7fc-d821-38f4-9069-10113c6a1f02 | -12.3501 | -50.024601 | 2026-05-04 01:07:00 | METOP-B | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c1ab2e33-d6fb-36fd-9155-581d2e928b6a | -11.9108 | -54.808498 | 2026-05-04 01:07:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5bb6ec9b-8fcf-346c-bc8a-c37a9d46b816 | -18.0786 | -52.956699 | 2026-05-04 01:07:00 | METOP-B | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 4194da76-56ae-3c1c-92c1-f8c2027b9a88 | -18.0456 | -53.0013 | 2026-05-04 02:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 8f2f27b1-1b6d-3d56-91a0-a2c743ce1790 | -18.0654 | -52.9982 | 2026-05-04 02:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 54.1 |
| ceb62714-8486-3e93-a1a2-39a4367d62a9 | -18.0659 | -52.9766 | 2026-05-04 02:40:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 53.8 |
| fc9493bd-9147-3496-8152-e286cf5859c8 | -10.58435 | -44.32766 | 2026-05-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7c4e7f93-532e-3b00-a8b4-823449d90364 | -10.58709 | -44.32632 | 2026-05-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d47b77af-404c-3e12-830d-e604ef6f8c31 | -11.88717 | -43.8074 | 2026-05-04 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a1434ce0-ae73-3322-9f81-40b7fa2108e0 | -10.58882 | -44.32849 | 2026-05-04 03:49:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e3056da3-e80c-3b71-96c8-475c0b57989a | -9.66673 | -37.04147 | 2026-05-04 03:49:00 | NOAA-21 | JARAMATAIA | ALAGOAS | Brasil | 2703700 | 27 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd231bd5-53f3-30eb-a97a-a5ebdc7a30b4 | -10.98001 | -45.09698 | 2026-05-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ffd570ea-b6b5-3470-b1fc-0cbafd5aeb8a | -10.98651 | -45.10125 | 2026-05-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de18df55-8d90-3f52-91e0-2ad3307639a1 | -11.88367 | -43.80263 | 2026-05-04 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cf693fa0-f3c8-353b-8f48-2acf0e9d0047 | -10.98273 | -45.09533 | 2026-05-04 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 03ed70c0-7668-3dfe-a4f8-c7625d23f7fd | -8.20996 | -43.71506 | 2026-05-04 03:49:00 | NOAA-21 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 524ec34d-cd10-3348-887b-15c6c013e38d | -12.28236 | -44.62714 | 2026-05-04 03:49:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ecc2af6e-1f3b-39f7-84f0-694261abdb68 | -12.82188 | -38.41851 | 2026-05-04 03:49:00 | NOAA-21 | SIMÕES FILHO | BAHIA | Brasil | 2930709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 6716a200-4518-371c-a550-8abd7ba77b5b | -11.88294 | -43.80664 | 2026-05-04 03:49:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 631f5e57-1298-3ec4-b33e-b45d637debc6 | -12.36318 | -50.03164 | 2026-05-04 03:51:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0e7f6277-42f6-3570-bcf3-af08668af339 | -18.07931 | -52.97028 | 2026-05-04 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f095b03c-4a77-3b24-b5a0-b864f763cc9b | -18.05228 | -52.9963 | 2026-05-04 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7ea83ad7-3dcb-3578-9b07-4d95d46b12df | -18.04962 | -52.98978 | 2026-05-04 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ee497bba-72ab-32fd-8b40-37df54b0df06 | -13.95301 | -47.25361 | 2026-05-04 03:51:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a96db70-5cac-3bff-8848-2fe13d1d97dd | -18.04817 | -52.9959 | 2026-05-04 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4bbd3952-8626-3a68-a692-c85192a0ff8d | -13.95245 | -47.25648 | 2026-05-04 03:51:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c7b23f70-469c-3e31-adc4-490a64c241db | -14.62453 | -43.66764 | 2026-05-04 03:51:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b23dc9e3-d97d-3210-a8eb-ca81125573cc | -13.9504 | -47.25502 | 2026-05-04 03:51:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6df04bc4-2833-3be4-ae57-9afdf0c3825c | -13.95815 | -47.25452 | 2026-05-04 03:51:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 05032aa3-3395-324f-96e1-8bd4aec4ffe8 | -17.50308 | -42.35576 | 2026-05-04 03:51:00 | NOAA-21 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed756088-8e88-351b-bf54-b637537f94ac | -13.97023 | -47.22015 | 2026-05-04 03:51:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d6f325b-f756-349b-ae6c-a920efb9c49c | -12.36214 | -50.03676 | 2026-05-04 03:51:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 29025aff-7508-31ef-ba56-be604911fb09 | -13.95555 | -47.25583 | 2026-05-04 03:51:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| fe125139-552c-3a45-8784-1f30223df9da | -12.35588 | -50.03549 | 2026-05-04 03:51:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 25c9416e-bba2-31d7-91ba-c9a56af5f1ff | -17.40777 | -42.62122 | 2026-05-04 03:51:00 | NOAA-21 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5eaea5d2-0cf3-30ba-975c-6c85e5bccd05 | -12.36839 | -50.03807 | 2026-05-04 03:51:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c4e814a7-2626-3224-b61a-c929195ab42a | -13.95611 | -47.25287 | 2026-05-04 03:51:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9745040b-4154-3184-b802-b7b6d078a2e0 | -18.25621 | -51.2622 | 2026-05-04 03:51:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bcd7c89-d150-3628-bdfb-0943afdfc9c9 | -18.25019 | -51.26079 | 2026-05-04 03:51:00 | NOAA-21 | APARECIDA DO RIO DOCE | GOIÁS | Brasil | 5201454 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5d122903-7e90-3ac4-9206-0ab1df597926 | -18.0456 | -52.99471 | 2026-05-04 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78482979-3558-35f7-8bc7-798e6daf9938 | -18.05367 | -52.99021 | 2026-05-04 03:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9fe92120-efe4-3677-b2f7-25da55c84085 | -20.17727 | -46.48766 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d449f2f0-d65f-340a-99a8-5af7d973a9ec | -20.17361 | -46.48324 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 72f2792f-0452-326f-b85b-ee0eb315436d | -20.17867 | -46.45705 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d2b8f1c7-a474-30d1-9ed7-43c670989cdb | -23.16052 | -48.35811 | 2026-05-04 03:53:00 | NOAA-21 | BOFETE | SÃO PAULO | Brasil | 3506904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0e0a0e8d-2a07-3a88-83e6-8589fc9227ba | -21.49526 | -51.77043 | 2026-05-04 03:53:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 6d88aca7-c14e-38cf-a72f-150269b091d1 | -21.50108 | -51.77193 | 2026-05-04 03:53:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 91e24e71-da70-3043-b8e9-0f0a48aaf867 | -21.28726 | -49.19244 | 2026-05-04 03:53:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 267e53fb-eb38-3e2c-977f-08d903fe5fe1 | -20.17538 | -46.47408 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cc9da8f4-f8f7-3ba9-a9da-4b65963c1919 | -20.17813 | -46.48319 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c063b194-2abf-3617-a887-077b7403d018 | -22.29241 | -48.53571 | 2026-05-04 03:53:00 | NOAA-21 | JAÚ | SÃO PAULO | Brasil | 3525300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d216059b-e9b3-349c-bfe3-6be03826b265 | -20.18312 | -46.45733 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02b6621f-50a8-3676-843a-e4c59d84f065 | -20.17275 | -46.48772 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 155b40ff-cd7c-33a6-8b35-bbe0116c68f3 | -21.4971 | -51.77039 | 2026-05-04 03:53:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 28497045-8e70-3086-9d0d-0456ad124327 | -21.50292 | -51.7719 | 2026-05-04 03:53:00 | NOAA-21 | OURO VERDE | SÃO PAULO | Brasil | 3534807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| f764fe10-e898-368b-8a77-4bb88f15e573 | -20.1779 | -46.46104 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a0a40e3-e36d-3f65-8cc3-fbcc1c6f24dd | -20.17089 | -46.47403 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8401c276-2e3b-37f5-9794-308341b6ad92 | -20.18392 | -46.45317 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d94f3083-bd3b-3595-8fee-62231a25587a | -20.17175 | -46.46955 | 2026-05-04 03:53:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 51ee110a-7417-32cb-9db2-56a66050227b | -10.55119 | -42.44329 | 2026-05-04 04:21:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 025367a1-7931-30df-9b1c-36e7b65dba5b | -8.20917 | -43.71576 | 2026-05-04 04:21:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 21bdb5af-2a0f-38d4-8ac4-3e906162fc99 | -8.20972 | -43.71228 | 2026-05-04 04:21:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| dcea77ca-ee4b-38c1-b991-9b9f0d11b2f0 | -9.46854 | -47.795 | 2026-05-04 04:21:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce1cfcca-598b-3a5a-a89c-9fb1c819049e | -10.98023 | -45.09377 | 2026-05-04 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6132b749-b928-3ad5-b70b-0e3f4039aa99 | -10.58818 | -44.32799 | 2026-05-04 04:23:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 661efb36-6086-3925-afb7-c1bfca612c2c | -12.09245 | -45.62247 | 2026-05-04 04:23:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2fe75367-1496-3ad1-a0af-48844cbf48b9 | -10.983 | -45.09787 | 2026-05-04 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8dd74ce3-11c1-3694-b6e8-bb12a0c20284 | -10.98243 | -45.10144 | 2026-05-04 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README2.md)
