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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2251acd3-c848-38a6-b551-a036f3972c37 | -5.57625 | -44.88382 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 82b00010-529f-390c-b09e-ce93c782a61a | -5.57404 | -44.87637 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 24f36342-84be-3993-ba20-7195103de062 | -5.57349 | -44.87983 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 6dbb01af-b531-395b-9e39-754f00526984 | -5.57073 | -44.87585 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a850aef7-cc8e-3195-958f-a6cec09c2590 | -5.57018 | -44.87931 | 2024-10-06 04:17:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 777b22f0-24b9-3ab5-865e-c8920b63783f | -5.56585 | -44.62742 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 71bd87e7-11b8-38b8-98a2-67fc91cc714e | -5.56363 | -44.62 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f10334f8-e076-33ab-b580-a79b59ac3113 | -5.56254 | -44.6269 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 785f1acc-0691-3f80-b5b7-22a9d0365212 | -5.56032 | -44.61948 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e20eae3-32f8-3ae5-bd28-1daaa50855cb | -5.7201 | -43.46899 | 2024-10-06 04:17:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 45eb5484-ab49-3c4f-9da3-cb7df457e4ab | -7.73061 | -44.88084 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 41b00773-a09b-3b8d-8d11-ea9d38c06165 | -7.54021 | -44.98928 | 2024-10-06 04:17:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 575dd927-46de-3c3a-8a6f-cc12456b1d41 | -7.5369 | -44.98876 | 2024-10-06 04:17:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb1024ab-63da-3153-8338-a216621688f6 | -7.5336 | -44.98824 | 2024-10-06 04:17:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 260d1f2d-0bfb-3b90-b0a5-72d77518b200 | -7.53305 | -44.9917 | 2024-10-06 04:17:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5aaf725c-984d-3af0-a554-011ef379655a | -7.53301 | -44.97041 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48e53052-776e-3539-a7c6-bf42943e6149 | -7.44367 | -44.73986 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6bcb6f46-e160-3ae2-8770-9ff65f6b65de | -7.39516 | -44.72514 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 89507200-0f08-3b67-9821-a80694c38691 | -6.98806 | -43.82682 | 2024-10-06 04:17:00 | NOAA-20 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e26c8249-2a49-369f-89f2-e66967b03e23 | -7.24601 | -44.93884 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| aa94e709-f221-3844-a1ac-682efaa3faa2 | -7.2427 | -44.93832 | 2024-10-06 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| af4bb2e1-1e70-3d13-8028-82323f8d8787 | -7.06825 | -44.4041 | 2024-10-06 04:17:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71ffb156-a348-3363-a0bc-79ddb431407a | -6.73348 | -44.56705 | 2024-10-06 04:17:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ace2cfaa-2713-3864-8433-3cbdf4e163c0 | -6.73239 | -44.57397 | 2024-10-06 04:17:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7b61c765-6a56-3bf6-bdcf-83cfd075e78c | -6.73017 | -44.56654 | 2024-10-06 04:17:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6ce5aab1-ffe8-3042-93f0-339e697c60c8 | -6.67845 | -44.83097 | 2024-10-06 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ea57e646-b350-3b5b-a7f0-aa4d8bd67463 | -9.18918 | -45.56202 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 4f5086a4-7584-370d-b9e6-558b27155400 | -9.18588 | -45.56149 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea143886-cc12-3d49-91c3-1ab98b0ebf99 | -9.18257 | -45.56095 | 2024-10-06 04:17:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f781e8c-f4d7-3b3a-9ae3-9e4e3f22abd8 | -8.99831 | -45.19986 | 2024-10-06 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d1f67a7d-eac7-3dd0-a155-089e7b26a2d7 | -8.56802 | -45.08514 | 2024-10-06 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab5ba3c2-9e69-3edb-bc67-b579c2e07933 | -8.15834 | -44.40438 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 518b0795-5e82-3c99-8c35-f421feb6a61a | -8.15502 | -44.40386 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94b8d8f7-a5cf-32ac-9ce2-20a2c32b1c21 | -8.15062 | -44.41032 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1344edcd-b72f-3ef2-900f-4384ad03fc4d | -8.14953 | -44.41729 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 19c52334-16fa-34dc-8b0d-461aa39a5617 | -8.14899 | -44.42078 | 2024-10-06 04:17:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bdc8ad57-8a18-3580-a974-29b6ffc0c3ad | -7.96213 | -45.00657 | 2024-10-06 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 067e5440-f436-322a-901a-5bb80b51088a | -7.95882 | -45.00605 | 2024-10-06 04:17:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3389229-696b-3f04-8477-3072d2af9d3d | -6.41276 | -45.82376 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31f50845-1e04-327b-b474-0a737c450e22 | -6.41219 | -45.82731 | 2024-10-06 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b166a71c-7216-36c5-bfa0-be14a655b6e5 | -6.40941 | -45.82323 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 825267ea-de8d-335c-a19f-8fe3bf59fe6f | -6.40884 | -45.82677 | 2024-10-06 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fef23177-ae03-3496-94cd-69096cc50510 | -6.37543 | -46.49747 | 2024-10-06 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 27b89d0c-b516-3e5f-a159-928912a8ea76 | -6.35309 | -45.70848 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3416e11b-dd6a-3c70-aa68-1243e9034d9f | -6.34974 | -45.70799 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1a22388f-7804-3658-af14-5c1df05304a9 | -6.34696 | -45.70391 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ae421474-d3aa-3cdf-bd2a-60b9098d2010 | -6.34639 | -45.7075 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d7fb6d1d-00d1-3901-9da6-49b03cdf7e39 | -6.34526 | -45.71466 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f846174-4e2e-3c26-bbde-f4bfc1c4c30b | -6.34305 | -45.707 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1aa79ad2-ea88-32b1-b4cc-b7f8d8557d98 | -6.34248 | -45.71059 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 208fc809-3c91-37c8-be7c-0d037b3b5603 | -6.34192 | -45.71416 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8cd289ec-da84-3186-a31f-b4d509218c7f | -6.33914 | -45.71008 | 2024-10-06 04:17:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1ed63cb8-f86c-3b5a-b6b3-31f02e970173 | -5.97566 | -45.49329 | 2024-10-06 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6bae602-e2f6-3a24-8ca9-e9a0c3b6b2f8 | -5.62421 | -45.29043 | 2024-10-06 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6f53cda8-1cc4-388b-a7ef-ce18105bcb05 | -5.55011 | -45.20019 | 2024-10-06 04:17:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dd6209ae-d8f3-3fc7-97e0-0fcac28eb554 | -5.85269 | -46.23786 | 2024-10-06 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10d367d3-cfb0-3f5a-b0ee-5503832a1a87 | -5.84988 | -46.23366 | 2024-10-06 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e9a6977d-3cdf-3b0e-b36c-f549147e48f1 | -5.81379 | -46.12756 | 2024-10-06 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8f5e8fad-7add-31d0-bd1c-18e75f34a56d | -5.73201 | -46.48515 | 2024-10-06 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 179e2bd6-1df1-3cf4-b1ba-5cb55353de03 | -5.72635 | -46.47657 | 2024-10-06 04:17:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8e9a0963-d662-33c4-a015-f19da879167c | -5.7217 | -46.17671 | 2024-10-06 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1546cb1-8302-3a21-b334-6d2f04ab8216 | -5.46614 | -46.21917 | 2024-10-06 04:17:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f3a49b5-c83f-3a5f-a704-6433d86ed521 | -5.36434 | -45.89341 | 2024-10-06 04:17:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8b180bc3-3e4a-3dcb-8d17-999f57a0b1ba | -7.75867 | -46.14003 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad4683f4-283a-34bf-ad6e-d128893c0854 | -7.7581 | -46.14357 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7d2cce0b-eb37-3b12-9605-49c69b6195ec | -7.75753 | -46.14711 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5bf1f54f-8a09-3972-a178-29ae0308024b | -7.75475 | -46.14303 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 87eb49d9-eb5b-37c2-83c6-53c856cd8537 | -7.46523 | -46.06451 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af5ca3f2-8beb-3a0d-a0d9-9453815d1322 | -7.46466 | -46.06807 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ebed60f-2000-3d77-9d2f-26ecaf42559b | -7.38502 | -46.13582 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d946cf54-75fe-360c-83ab-f684fa126e8f | -7.38444 | -46.13941 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 69f46716-2dfe-3ab8-810d-fdcd15482060 | -7.38108 | -46.13887 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5321dbc2-41c6-3942-a551-a9e0364a169a | -7.35088 | -46.20742 | 2024-10-06 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3b842f8d-fe70-346d-8a9a-b91f6a46d329 | -7.26376 | -46.34133 | 2024-10-06 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 382108b2-5752-390a-946a-8558216fb133 | -7.2598 | -46.34438 | 2024-10-06 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f0463416-cc85-3b43-802a-f693e2e3f1a9 | -7.25922 | -46.348 | 2024-10-06 04:17:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1b6e6f95-3241-3f4e-bb75-66de0be5fe0d | -7.07495 | -46.59628 | 2024-10-06 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e770ae4e-d23d-3ab0-8807-9c965509d1bc | -7.07154 | -46.59573 | 2024-10-06 04:17:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 94200900-6808-359d-a0f0-26aff6c1ef6b | -6.76073 | -45.64303 | 2024-10-06 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f1bfc122-fc57-3a46-9bc6-7b90e460d713 | -6.76018 | -45.64656 | 2024-10-06 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21b6d474-e868-3069-bef3-27eddfb852e5 | -6.75351 | -45.64549 | 2024-10-06 04:17:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e41598a1-a156-3b10-8e19-7d1a902fb7b3 | -6.70268 | -46.31951 | 2024-10-06 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aacfa2a7-067b-3cea-9ce8-c265987c58ef | -6.67198 | -45.96302 | 2024-10-06 04:17:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 31f7ab61-977f-3fff-9ab7-9c541aeb880a | -6.46044 | -46.51491 | 2024-10-06 04:17:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d9cd19d-2fd5-3f65-b8f3-d6e463e34c3a | -6.6334 | -45.31034 | 2024-10-06 04:17:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e59a7506-22e3-3a9c-8255-22900f0afb22 | -7.80659 | -45.45494 | 2024-10-06 04:17:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4434616e-31b3-350e-bc39-9562ec090e0f | -7.3471 | -45.50324 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 70c0957f-45cd-3c55-a242-05b36dd3f0cc | -7.34434 | -45.52069 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3faedc65-22b1-3a2f-872c-a0ea97ad266f | -7.34268 | -45.50969 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48b12940-26cf-3674-90cb-b0f5b6e1e8f2 | -7.34157 | -45.51668 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 095b6f14-b180-3289-85c1-f16c2692573f | -7.05309 | -45.32068 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14819869-8ee5-34ae-9005-042d30a6adc1 | -7.04922 | -45.32363 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6d6f473-6be8-32c9-8b93-3d6d3294b36a | -7.00229 | -45.38395 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c352ce6-7bfe-3e1c-8739-275de980f9d7 | -7.00174 | -45.38744 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 254720bd-2c74-351b-ae6b-a0909dbebe8f | -6.99898 | -45.38342 | 2024-10-06 04:17:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5d76fb9-2eac-3ea9-84e2-0bd7f91b4f51 | -9.03441 | -46.58001 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45b0c6ee-d694-3560-b0ed-d949cf70a5ca | -9.03162 | -46.57584 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 52230efb-ac62-3477-8d7d-5dde730d62e9 | -9.03104 | -46.57946 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8542d592-9119-3d33-b026-a14d0acf3bf6 | -9.02826 | -46.57529 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 47f466b4-bf9b-3bb0-93a8-e534a573fb59 | -9.02768 | -46.57891 | 2024-10-06 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README66.md)
