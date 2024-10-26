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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d729f7a4-63ca-3d6d-bc68-52364d83ab3f | -7.55844 | -46.79183 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1033ca4d-21d9-398d-9567-19ded57101c6 | -7.55793 | -46.79468 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| df3a4468-ff30-38ec-8dbc-067f5ae42bcc | -7.55743 | -46.79752 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc6bff51-6c11-3a9a-b93d-d422bd26b70f | -7.54227 | -45.83961 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| da9e7eb0-7814-39e1-98be-0d24de1a9605 | -7.54142 | -45.84456 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0fa2037c-84b6-3ea2-953d-8bcac24b4073 | -7.53761 | -45.83878 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7af94c97-f273-3819-888c-9cbd0abd8e56 | -7.53676 | -45.84372 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| e0566784-ffe9-3a21-b6b6-6bf83659d271 | -7.53591 | -45.84866 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8274efaa-e8ae-31ad-b7ec-d3730f33c54a | -7.47448 | -46.71196 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1244f095-09ee-327c-b4fe-7e62921f9242 | -7.47347 | -46.71767 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5f12581a-4706-3ad5-9c89-593eeb2e6589 | -7.44651 | -46.84176 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b17e30b-dec9-3686-9248-5d629032f6e6 | -7.44191 | -46.75164 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 583cc360-3c17-334e-938b-5a5771fe71e8 | -7.44139 | -46.75454 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2caeff75-0704-326a-b3d8-5576d234e816 | -7.42721 | -46.65366 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 517e042d-9642-3fbe-b4d4-688bdc3bf603 | -7.4092 | -45.57027 | 2024-10-26 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 81538ca3-9793-35e9-a009-aa3692d09df2 | -7.40837 | -45.57497 | 2024-10-26 03:55:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5df8bc8b-5f33-3cae-b8db-0e8bcea5606a | -7.29122 | -45.54407 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7a3c300-2df3-377c-a298-178cce05e44e | -7.25903 | -46.05566 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b00ceaeb-0574-3904-b91b-b29a33f8d753 | -7.25817 | -46.33886 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 66693d5e-cf45-3072-a0d6-4a308df4d7c8 | -7.25504 | -46.33643 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6b2a324f-4c6a-3258-8679-3e16c3adac45 | -7.17597 | -46.33172 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f1189c74-30f6-3db4-aba5-c7cfc2589b30 | -7.172 | -46.32591 | 2024-10-26 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 43fc73ac-25c4-349b-86cf-7dad4c54f215 | -7.17104 | -46.33132 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 800b849e-a579-3a25-b85d-e728c8791f44 | -7.16461 | -46.17232 | 2024-10-26 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37d6969f-de48-34e9-8abf-295444532f4d | -7.12448 | -46.46682 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22331c37-d2a2-3a43-923f-9bf7e65d12c8 | -7.12094 | -46.37045 | 2024-10-26 03:55:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bdab2b23-8d57-3803-9857-ae493df4e3cd | -7.03413 | -46.69439 | 2024-10-26 03:55:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 792b3050-64d0-33a1-85e1-bc068b6695eb | -7.03362 | -46.69725 | 2024-10-26 03:55:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c6fd9d2-3283-3934-8b31-8f8f07b8c15a | -7.03312 | -46.70011 | 2024-10-26 03:55:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 540cc780-c55b-366d-87ab-73e3d38f63a4 | -6.92906 | -45.62136 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 06b4ff97-31cf-31d2-a0de-76edabbd3b83 | -6.86834 | -45.8919 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e423f138-0c78-3c54-8138-255bd28424ec | -6.86754 | -45.89658 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 16eb9642-9bee-3863-8d71-d399dd3856f7 | -6.86671 | -45.90136 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 62d641cf-1fbb-3c81-84d5-58570e701bc0 | -6.86367 | -45.89073 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cb99ee6-9417-3210-b367-db92cce2ab5a | -6.85902 | -45.88946 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 472fd620-e23f-35ba-976e-6e781d187591 | -6.85519 | -45.88343 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a0e36ad4-8b69-3c8d-9738-2e08c0e7ea56 | -6.85439 | -45.88803 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 4287f7d4-6bb8-3a15-880c-85ad68d617b5 | -6.84969 | -45.88705 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 87440d3a-eadb-3c2d-a374-7fc45a08fb05 | -6.84879 | -45.89224 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d722ee52-0efc-3bec-88f1-bf4fb8fc69b8 | -6.84406 | -45.89146 | 2024-10-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e1149b6c-fcd3-357a-b16d-8e980a4413f2 | -6.55473 | -46.66373 | 2024-10-26 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bfa1bfad-ddbb-3f0a-a110-601a33a0532e | -8.76403 | -45.89248 | 2024-10-26 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1c530d6c-b186-32bd-8f89-17405d4ac758 | -9.13863 | -47.10428 | 2024-10-26 03:55:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6865259c-eca6-3ab1-ab43-df9a58515fb5 | -8.74536 | -46.46109 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 645b1f23-9115-3021-9ec5-80810c2b0b99 | -8.74526 | -46.46457 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 15fb8000-cab8-3fb2-8baa-87acde4be2e0 | -8.74443 | -46.46644 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1f14756b-1edd-3f86-a502-8d0e903840fc | -8.74048 | -46.46384 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| d101100e-2ced-3c78-a7da-b7a44ac036b6 | -8.73965 | -46.46566 | 2024-10-26 03:55:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6e64ed1d-30a3-32e1-8e9c-b7c278f9b3ec | -7.89755 | -46.68425 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 6197e08a-b96f-3336-98bf-f4c2e5107877 | -7.89657 | -46.68977 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| dfd783b7-51b1-35d2-b155-0a7f4e408db4 | -7.89265 | -46.68338 | 2024-10-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 5badc6b6-8850-3015-a336-3a1d17dba259 | -9.50361 | -47.23074 | 2024-10-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| eb65f3d1-0a7c-36de-8524-bf31163654ea | -10.26572 | -46.7624 | 2024-10-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 88043f1b-0412-3253-9520-c07f4423bf18 | -4.91497 | -47.7266 | 2024-10-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.2 |
| da7dc47d-00cf-3413-a2e3-214b89d8baac | -4.36694 | -47.48284 | 2024-10-26 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dc6fcf6-142b-3d0b-9295-668dc5a43fab | -4.36689 | -47.48095 | 2024-10-26 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 889b1558-3140-3787-af51-94aeb96262fa | -4.36628 | -47.4846 | 2024-10-26 03:55:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6642ef73-c665-3125-ad55-d208c231c536 | -4.15126 | -46.83223 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 57a3d036-4109-30e0-84d3-d9f2f9123f93 | -4.15069 | -46.83573 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98dec014-f3d3-3a83-b26e-611c12ae098d | -4.15064 | -46.83271 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f746cccc-218d-3a91-bae9-448dd359ca95 | -4.15003 | -46.8362 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f6a61d78-c583-3520-9f0a-7c34efd51b52 | -4.14598 | -46.83141 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97c060ae-c55a-313e-b7d8-c7581ed1f686 | -4.14539 | -46.83494 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 36148c1f-0e7e-3096-a063-704e3dfc4f61 | -4.14534 | -46.83192 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a00f49c5-a6ed-3db2-bfd0-37314bb2bb63 | -4.87649 | -46.88178 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1267abfc-c0e5-3e47-a4de-97f2d3d62fb6 | -4.87121 | -46.88119 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07aef82f-b820-3122-98fd-6ecdc93d2988 | -4.54343 | -46.46619 | 2024-10-26 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e90e25e-1594-3e68-8001-2d646e9b3a80 | -4.54291 | -46.46918 | 2024-10-26 03:55:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 26423eef-4589-3747-aff5-ca6bcc55c8f5 | -4.18714 | -46.62147 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33752b4b-3a24-35d6-954b-4ac09aba2227 | -4.18564 | -46.62389 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b68a027-bcad-3608-81c6-212b387057c9 | -3.99263 | -46.48587 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 53b045b8-c50f-34ab-ba29-a1c01c60f120 | -3.98844 | -46.47902 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52448b3c-b1b1-3507-a543-a893397fe3bf | -3.95358 | -46.43336 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e3d469a-ea36-37f5-9475-db9efbe39c22 | -3.94896 | -46.42932 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| babc5c2e-e08e-375b-b2fd-222bc51f373e | -3.94846 | -46.4323 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1c64e137-2fdb-3a66-990d-765f3857a542 | -3.94796 | -46.43528 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 44727905-f4c7-3ba3-afaa-3f436320e442 | -3.94333 | -46.4313 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fde46943-1be3-3524-b096-f7ea8730d032 | -3.94282 | -46.43436 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31cfe75e-a225-3610-acc8-4836c22bf17d | -3.93818 | -46.4304 | 2024-10-26 03:55:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23afdfa3-9d43-3c10-99e1-cf90dc93dbe7 | -6.45415 | -47.65682 | 2024-10-26 03:55:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18fcd1b5-c85d-3b3a-b5bd-adb55a575bf1 | -6.45358 | -47.66004 | 2024-10-26 03:55:00 | NOAA-21 | SANTA TEREZINHA DO TOCANTINS | TOCANTINS | Brasil | 1720002 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| afba27d4-d8e1-3750-a24a-a182ab910bcf | -6.13529 | -47.00576 | 2024-10-26 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3214102e-86da-32ed-bdde-0a3d0424cc18 | -6.13477 | -47.00881 | 2024-10-26 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 972f81a2-7792-372d-96ae-f414cd54efd4 | -6.08706 | -46.91735 | 2024-10-26 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| be304500-15db-372b-b83a-df96f6cacba5 | -6.08215 | -47.21925 | 2024-10-26 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 94fc49e1-5f88-3ec3-afc0-5e4572207005 | -6.08159 | -47.22248 | 2024-10-26 03:55:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 52b40908-9586-3713-9b9b-9a3dfcbb5be2 | -5.84352 | -47.28664 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 45c2ab1e-a617-33ab-b09a-b8dcfac2fe6d | -5.83331 | -47.19009 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 60c6867f-bad2-3447-a1d0-42452a69d361 | -5.82805 | -47.1892 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38b69327-6b59-3260-b090-7c17a7388a08 | -5.76804 | -46.53657 | 2024-10-26 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 90b9653d-7606-3860-a4ec-259d8cac9d54 | -5.76756 | -46.5394 | 2024-10-26 03:55:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 40f487d9-6525-381b-837e-16085868da9c | -5.75229 | -47.03569 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d975fe4c-776c-38c2-b543-18c08c9b0be2 | -5.74766 | -47.03154 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b95d41ff-a44c-3b28-bb61-9b10f4b165b1 | -5.7471 | -47.03473 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fde0dd38-b5bd-3e42-8f26-bbffe46c8c1a | -5.71779 | -47.1091 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3f168df7-059d-36bf-ae18-6035240b56df | -5.71767 | -47.10965 | 2024-10-26 03:55:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 99554ab1-e970-3c62-b63b-74b4baf2fea8 | -5.55886 | -47.02881 | 2024-10-26 03:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ebc6887d-f190-3ca5-a37a-ee0582cda579 | -5.55832 | -47.03193 | 2024-10-26 03:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f0d5a72-1162-3e66-9097-91d9dc2ecb09 | -5.51647 | -47.20971 | 2024-10-26 03:55:00 | NOAA-21 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 28c8ead0-4687-3012-ac7a-d1529eefba15 | -5.4526 | -46.45342 | 2024-10-26 03:55:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README32.md)
