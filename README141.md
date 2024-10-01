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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 628ff6d1-acb3-3298-b7a4-78fb3eba7dc9 | -12.95682 | -51.4191 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| e9aa44a7-64d2-3b2b-975d-d5eecdb36c39 | -12.95641 | -51.41572 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| eca1cc3f-7dad-3361-91fd-f2273a49d952 | -12.95624 | -51.42448 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 395d06ef-552d-366b-952a-392a79d76d3b | -12.9558 | -51.42107 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 3e0fb3b0-2ab2-3e90-b535-f2c81a4c296c | -12.95567 | -51.42988 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7d98c2bd-51e1-3e33-a64b-f210e85f4bb2 | -12.95519 | -51.42646 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| c79fe784-53a5-373a-9864-bcb99b4d3406 | -12.95458 | -51.43183 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| ab2a27b7-6b1e-3c7a-84f6-475c4dd9bdc3 | -12.95395 | -51.44598 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5fda6144-f1de-3226-93a7-983263774050 | -12.95338 | -51.45136 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 539f6032-7ca4-377a-9e86-e27c9f99e938 | -12.95276 | -51.44787 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3f1c6b8f-4d5c-3517-af9a-228681bf8a90 | -12.95216 | -51.45324 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58f552c1-cc41-33bf-92d0-087da60f7db4 | -12.94995 | -51.41497 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| ce033c8a-eef7-321f-9d05-a51709cfcc96 | -12.94935 | -51.42032 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 4b2164c6-5978-3195-9fec-e8c2fb632796 | -12.94875 | -51.42568 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2f67fe4c-f605-359c-8149-cf37c598c1df | -12.94572 | -51.45248 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3bd8ae15-e956-361c-b034-9aea27fe0e5b | -12.94109 | -51.43563 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e671f001-a1a9-3a43-823a-530c56db3684 | -12.93867 | -51.45712 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8593fa1b-2eb5-3ec0-9fa6-d8066f6a8cd7 | -12.93473 | -51.19684 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0d8668ae-34fe-3f84-baf0-6b18f61e4bfb | -12.93465 | -51.43488 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 733e2d6b-3fb3-3a66-892f-4c076808e35f | -12.93405 | -51.44024 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3927e8d1-0ab9-392f-8a79-fbb1e6b72856 | -12.93344 | -51.44561 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 627ea07e-eff5-38c3-b492-e19bcfae3a17 | -12.9282 | -51.19603 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8a40904-5646-3b29-b7e3-420193023d6d | -12.92759 | -51.2016 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f4a50812-984a-30e0-b061-13323ae696cf | -12.92438 | -51.18409 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1a6c99cb-9b60-3921-a922-0e654d4df260 | -12.92374 | -51.18964 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8950b9c3-6a2c-3bf7-aa07-b00f1cc7c942 | -12.9231 | -51.19516 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 7fccedba-d2eb-37a1-bf73-804cb7d8aa93 | -12.92287 | -51.18414 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5bbfcacf-de73-3e0c-b0e4-67118a710056 | -12.92246 | -51.20071 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 4a35aa59-78da-375f-87a2-bc6de8c4d4b6 | -12.92227 | -51.18971 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| a5cd4c38-5272-3738-94b1-6ceee0ec4dbf | -12.92182 | -51.20625 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 931a0ccc-9dcc-3030-870a-3db563d2cb77 | -12.92166 | -51.19525 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c1995536-db0c-3eb4-97ce-5f395bb2ed08 | -12.92045 | -51.20637 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a1be9d0-2cb2-35b1-b601-87bc14ffe625 | -12.91999 | -62.67695 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 41067bf1-4cdd-3b95-af1f-b17a08a4ab5d | -12.91997 | -51.44944 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 91c0fcaf-3169-3f08-a0f2-94f0fe0d95ba | -12.91944 | -62.68055 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7a6b9144-b460-3ffd-8c94-6a04fb624971 | -12.91937 | -51.45481 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 67b11b38-d560-30b0-920e-708ed21655ef | -12.91878 | -51.46017 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a86ffa95-76fa-3171-8237-5c803b8e97e7 | -12.91818 | -51.46554 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 897d3028-c9c3-31f7-abc7-d9d6d7d624ea | -12.91784 | -51.1833 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 68d79bc8-323f-3098-ab66-11ba7615f674 | -12.9172 | -51.18884 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 1b36e9ca-9fb0-35fc-800d-0d5808bd5cef | -12.91664 | -62.67642 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 14a66019-7db5-3719-95b7-8f715a109dad | -12.91656 | -51.1944 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 64151dc6-463d-3655-b5f4-907eecf0a30f | -12.91609 | -62.68001 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 7cbf221b-fcf1-3cb8-a769-9e0fb71f0fcf | -12.91592 | -51.19994 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f3df34c8-7647-39a0-a31a-e73875e357b6 | -12.91573 | -51.1889 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 691bea4d-ebd5-37ed-992f-f2000ef30a10 | -12.91528 | -51.20549 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 24958397-8790-306a-bbd1-297dda489427 | -12.91513 | -51.19447 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 78fbe354-8c7a-3644-ac34-7f9618ea1bf3 | -12.91465 | -51.21103 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dd0222a1-20a9-3c1b-9a23-ad58fdef024a | -12.91453 | -51.20003 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9d10f379-ad7f-3c03-b7ad-dbc6d0a57816 | -12.91392 | -51.20559 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 3d09e1ba-fa7c-36a5-ae94-ba35a650b32c | -12.91332 | -51.21114 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9f245fe5-23b5-3097-8514-eb033b29b0b5 | -12.91274 | -62.67948 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff1178ef-ac73-34b5-adf9-f9209509635d | -12.91219 | -62.68306 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ef01a259-215a-3e05-8110-7d64678c6a5c | -12.91164 | -62.68666 | 2024-10-01 05:29:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2a30159f-1d53-3181-b337-5f2f3db9c576 | -12.91096 | -51.29992 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7ea681aa-1e85-3d5f-b625-0ab12be4d72f | -12.91023 | -51.30015 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f117661f-6345-3e88-995e-2ab0a8338989 | -12.90964 | -51.30562 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3c485f7-8433-36d1-9398-1fdf07d1af18 | -12.90939 | -51.19918 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d00aae91-9c83-3d9f-a032-9f1efd9900d0 | -12.90875 | -51.20473 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| dbae8760-0484-3f9d-b0fa-807c58c2b044 | -12.90739 | -51.2048 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e34e9f3d-6b2d-3ad3-a177-809b74d65b7f | -12.90529 | -53.88208 | 2024-10-01 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52d7b521-f304-384f-9953-38d714edbc8e | -12.90517 | -53.88282 | 2024-10-01 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a068d6a6-0f54-3fa4-9226-5e7d0a26c587 | -12.90487 | -53.88563 | 2024-10-01 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4aec56b5-f28e-3dc6-ac29-27dd3867dd89 | -12.90474 | -53.88636 | 2024-10-01 05:29:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 006d1e13-5295-3065-8633-38acc7402254 | -12.90447 | -51.29914 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d6a8fed6-98d4-30c3-9760-d58ffca0c361 | -12.90384 | -51.30459 | 2024-10-01 05:29:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5026b4be-7d15-3aa6-8278-cb6b8ec6ba50 | -12.86062 | -62.84014 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 804e5d3f-efc2-31e6-b218-076dc43197fc | -12.86007 | -62.84371 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6aa96a40-e767-3e2e-bb59-7a3b3ac5975a | -12.85952 | -62.84728 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 52543ce7-3eac-3922-b88e-daa46b6fc102 | -12.85508 | -62.8539 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a86a1855-7555-380d-9a92-5a16aa2c6918 | -12.85453 | -62.85747 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b5054e9-4b37-32e2-bb77-d5da7f59800d | -12.85382 | -62.85311 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b511e53f-00fa-3181-879b-dea53e345ef4 | -12.85326 | -62.85668 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2b95c26e-f6f1-3e82-b5e5-a8402e88f8cc | -12.85048 | -62.85257 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a0c87a4e-06de-3061-bc50-3d8caeea7a28 | -12.84992 | -62.85615 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 58f5f080-4af8-31b9-bd58-00b9730e29c9 | -12.84824 | -62.84488 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3f9a239-f1de-3dbf-bfec-ccd49136c7aa | -12.84769 | -62.84846 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cc020f4-bb21-37c0-b27e-46e2fe3b0610 | -12.84713 | -62.85204 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 69022926-c057-3de3-a4ce-659300bc8bf7 | -12.84658 | -62.85561 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| a5b55662-cd6f-3e08-9be6-7e82282291c8 | -12.84598 | -62.79321 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 591676ab-cdad-3acc-a10a-2f58bd58cb83 | -12.84435 | -62.84792 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f315d821-5e07-3404-9e2a-3dca79cddba2 | -12.84379 | -62.8515 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8297fdb4-beba-3bb6-8d33-947582dd86a6 | -12.84268 | -62.85865 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b26a2c4-d1b3-321f-aba6-3f4ba530a0e4 | -12.84265 | -62.81467 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74b69828-60a4-310b-b9d5-a3218899e0c7 | -12.84264 | -62.79267 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 219def1a-a190-37cf-8922-9deb5c6d8646 | -12.84045 | -62.85096 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3c4c9dc-e844-30e7-9f46-911154019d2b | -12.83934 | -62.85811 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ff5768b8-a82f-39c5-a801-a69f9b7e1632 | -12.83879 | -62.86168 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d699c06-8b36-3377-8d63-8d552cb9f9b3 | -12.83044 | -62.87132 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8e82cfb6-70cd-3a99-948d-37eb3244b20d | -12.8271 | -62.87078 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e4a834d5-e88c-342d-86b1-1a846416cb18 | -12.826 | -62.87792 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2ecd9330-0a52-36d4-b8e4-6ed0b2186875 | -12.82266 | -62.87738 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5ed2e8c4-bab5-3559-8d8a-e84cc9cc32b8 | -12.8221 | -62.88095 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3678e64-b5c9-36ed-928b-c700988bfeb1 | -12.82155 | -62.88453 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 801a0730-a246-3bfb-aace-0a8c11b72e28 | -12.81821 | -62.88399 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8ca46d82-cb74-3bb7-b7dc-f01e18b2041e | -12.81598 | -62.87631 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aba5f3fd-edbb-3dde-bd29-ddb25e90fbc9 | -12.81542 | -62.87988 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a8cc0880-788d-37dd-9b71-3bafa86a8d69 | -12.81487 | -62.88345 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee85a5f0-6af0-356a-a8aa-491170ecc7a4 | -12.81264 | -62.87577 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 362ac77b-bd55-3b02-8ba0-2c37866ed8fd | -12.81208 | -62.87934 | 2024-10-01 05:29:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README142.md)
