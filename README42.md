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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e840a730-8951-31de-a5c3-eec8407d0486 | -7.30104 | -46.7942 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df7f5dcf-d574-378a-8b78-51ee563b1646 | -7.28819 | -46.78863 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c39172a-2654-3d70-ad2c-72f26ee5989f | -7.28762 | -46.79231 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aa26b576-17a6-30a9-b65a-5ace5f534c1b | -7.28484 | -46.78814 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af753ede-a6a4-334a-af95-d340451f8055 | -7.23175 | -46.42682 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6cc6f460-ce2e-3404-9400-1f29baa8aa02 | -7.20626 | -46.36728 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1abc8e6c-f0d0-38a5-b162-2e601011b475 | -7.20571 | -46.37092 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48033f1d-cbda-3188-810c-563f0eea6b9b | -7.20557 | -46.30347 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36ce3037-e63a-3589-9f6b-17bd5b1838a5 | -7.20463 | -45.87008 | 2024-10-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 71ceebd0-4b12-35e2-82c4-b918b8948db7 | -7.20405 | -45.87386 | 2024-10-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 709913b2-4b21-34fb-be88-10feba223f69 | -7.20287 | -46.36681 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74d46c9c-b9fb-39b3-8a65-d9119dd2218d | -7.20118 | -45.86958 | 2024-10-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 24c7c686-c066-3178-98d5-fa786f616c26 | -7.20061 | -45.87336 | 2024-10-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dab7ba2c-ad3c-3572-90b4-7ad9a0bfe96a | -7.17319 | -46.32534 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b981c8c9-cd1e-3636-85b1-a9bdd11dc4c4 | -7.17263 | -46.32899 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2f1a2b84-6206-31b4-9796-a7874a27d4b4 | -7.12567 | -46.6323 | 2024-10-24 04:34:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb8dbfa3-d3cd-38d7-a7bc-9be6722234ca | -7.04683 | -46.43946 | 2024-10-24 04:34:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 518d1cea-a573-3218-9975-ed6c10f5a508 | -7.0294 | -46.41817 | 2024-10-24 04:34:00 | NOAA-21 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c13a815f-8a9e-38ad-aeb1-3b6ce605c929 | -7.00669 | -46.01727 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 69dff053-1e30-370a-9242-446f3a174ee3 | -7.00009 | -46.67463 | 2024-10-24 04:34:00 | NOAA-21 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fdb9248c-2a22-3a6e-92a8-328f9c98ab88 | -6.96677 | -46.33038 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63f3facb-d57f-376e-840b-d5b598d0a99e | -6.96517 | -46.33065 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b3b86506-f325-3640-81c1-4a1b64861fe1 | -6.96179 | -46.33013 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e228c823-2844-3f7a-95ce-a8bc096387a6 | -6.94806 | -45.96593 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8eadbe3b-6db2-3d3f-ae67-c6c15a4453f5 | -6.88608 | -46.13937 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 322fe0c0-63ca-3b18-8930-e659ab952010 | -6.88551 | -46.14304 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dc5aa390-6018-38bb-a187-3500a2d96427 | -6.88211 | -46.14249 | 2024-10-24 04:34:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2589566-0d08-3750-9baf-089f65d06960 | -6.73638 | -46.55036 | 2024-10-24 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f8b7bc5-15ca-3934-bb75-91bc77325c76 | -6.73584 | -46.55392 | 2024-10-24 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3588f642-8073-3536-af6c-6f43eb320cf2 | -6.65881 | -46.1345 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 81ab0df3-d076-3627-91ea-c9de306fad85 | -6.65613 | -46.22719 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9c020afd-11a0-3584-8e44-a67fbfe924a2 | -6.56868 | -46.56092 | 2024-10-24 04:34:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 54826418-4e74-3741-83e6-0123eaa101b8 | -6.54168 | -46.07565 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 427ae591-8435-3d8f-b254-d925d4d3364e | -6.53828 | -46.07511 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b7712967-810a-313b-b2df-02c94141b622 | -6.53545 | -46.07089 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ebde773-5181-33f7-8597-8d4109c2100f | -6.53542 | -46.02582 | 2024-10-24 04:34:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c1358816-2d0c-3ccf-8575-d2dbea3691a1 | -7.84964 | -45.43702 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1c6e12db-5445-3bf2-8fd3-27b6875a6aac | -7.83845 | -45.43943 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f44cccf0-4d27-3d57-8d70-fadd7a441683 | -7.65589 | -45.3772 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cf86242f-cf83-36bc-9077-83ca829118f3 | -7.81511 | -46.60813 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 01a7ce18-f96a-382f-87ce-b0687d42dff8 | -7.62944 | -46.82637 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4fa36c99-2686-300f-9deb-6f6e081759b2 | -7.60324 | -46.84053 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc88f746-b0a4-326e-bef0-d74dfe3fd0e2 | -7.56358 | -46.83079 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0a584faf-8ef7-3866-a437-f0d6c04e2f1c | -7.53867 | -45.84158 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5e56b291-5d66-3092-bf0d-d12ba4e30712 | -7.53809 | -45.84539 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c955bf34-68d5-3583-8905-337fad9b452d | -7.53752 | -45.8492 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 17dd726e-f040-3577-989b-aecb616023fd | -7.53694 | -45.85302 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 39b26d2c-645a-333f-858d-b9fd94954a23 | -7.5358 | -45.83723 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526801b6-dd9b-3800-9eb3-a35fd5d66a85 | -7.53522 | -45.84104 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 9b8e5616-9813-34ed-a661-4ff3b47e980e | -7.53464 | -45.84486 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 30f9bac7-5c9d-3c4d-9da4-2c3b08d003fb | -7.53406 | -45.84867 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc5086e0-c8c6-31e7-8bc1-4cb225cafb3e | -7.47537 | -46.71856 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c497779-891a-3f68-b8cb-a2b5e9c11878 | -7.47447 | -46.6117 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 006f50c8-fe78-35e2-9e0f-21f415f60a20 | -7.47201 | -46.71804 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b10a28ec-2ffb-3926-925d-8f81f914105a | -7.47111 | -46.61118 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2693de29-7908-33d9-ad6d-c45f99c3b237 | -7.44391 | -46.8344 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a4a39e0-b348-35cc-9c5c-ac7c24d9fcbf | -7.84257 | -45.43603 | 2024-10-24 04:34:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a5232bc-9632-3db9-aed3-03e06ce66ad4 | -7.12663 | -45.36053 | 2024-10-24 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7357e96-f93e-3c80-a255-7773b29f7407 | -7.12604 | -45.36446 | 2024-10-24 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| df7dd5ee-f86f-3c51-8ebe-05920052c47a | -7.07709 | -45.30185 | 2024-10-24 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7063c27b-e341-35ed-af76-d0db8bc3c65b | -7.07649 | -45.30578 | 2024-10-24 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 38c6fdf9-1624-3c69-9eaa-bcbe137ce3d2 | -7.07297 | -45.30527 | 2024-10-24 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ea22508b-62f1-3127-8eb5-ae19d194fdfd | -6.99247 | -45.28625 | 2024-10-24 04:34:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 920887da-ecf0-37df-99ed-d43dd554fe9a | -6.96387 | -45.42675 | 2024-10-24 04:34:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 345c5bdd-b95c-32ab-a091-0ce3b5259d50 | -8.92301 | -47.05173 | 2024-10-24 04:34:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2aa77ce1-6e30-3c84-9fae-ea2a0aaacc58 | -8.51051 | -45.88176 | 2024-10-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0b14887-7844-3519-8c51-b75ac28e2734 | -8.45156 | -46.47716 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 888c2b8b-2572-3ead-9dee-428a1cdc1ecf | -7.89471 | -46.73116 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2e6ad77a-123c-3213-84f3-1a48a43e4d19 | -7.89416 | -46.73478 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ce88044b-fbcf-3d4d-94a9-3da7d7be2a2c | -7.89175 | -46.68266 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b2207cff-155d-3546-952f-eed2dcc39131 | -7.8912 | -46.68628 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d411abd2-e443-37be-a698-608a0762620f | -9.27138 | -46.22505 | 2024-10-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ca0a0502-052c-328a-a445-49d3300d1dc4 | -8.8704 | -46.16644 | 2024-10-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9850a370-5c59-37cd-8e27-c610c278ded7 | -8.51862 | -45.87523 | 2024-10-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5ff54958-13b9-35d7-a4c6-7769ee79301d | -8.51574 | -45.87071 | 2024-10-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 119d0f3d-13ff-365e-9250-447ea6d0ae30 | -8.51515 | -45.87459 | 2024-10-24 04:34:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| db61d4b7-98e8-3ee2-a773-6f54d820243f | -8.44816 | -46.47664 | 2024-10-24 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c02b955-877c-3925-8ef8-fdc9600308fb | -8.28767 | -46.47423 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2dcddc80-94bd-3c53-9727-2b27d26251fc | -8.11134 | -46.50069 | 2024-10-24 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 492d5579-3b86-3767-9fe1-358576976f5b | -8.04666 | -46.89845 | 2024-10-24 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b205b790-cab0-3205-9ca6-3a40baf4477e | -7.91825 | -46.53056 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae769fc7-957c-30f3-bee0-6ba6a90df77b | -7.89457 | -46.68681 | 2024-10-24 04:34:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe0cd676-8c85-3d66-835d-83a67ad2d194 | -9.56703 | -46.40487 | 2024-10-24 04:34:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 08857a8f-1055-36b9-891b-d6e98e13d141 | -9.53996 | -46.77245 | 2024-10-24 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f363661d-eb3f-3a0d-bf42-a5c19c052934 | -12.29057 | -46.72522 | 2024-10-24 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5fc137ed-8d89-349f-bb20-0335689865cd | -12.28709 | -46.72469 | 2024-10-24 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| be6da6e9-7d58-3e1c-a4a9-bd28d4ea8138 | -12.28651 | -46.72861 | 2024-10-24 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b61c4f6-0675-3469-ae97-21f639142f73 | -12.28593 | -46.73254 | 2024-10-24 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 83d95620-4562-38f1-84c9-276f5c916e70 | -12.28245 | -46.73199 | 2024-10-24 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8465a805-297e-3434-b6c1-ad7a9a65d339 | -12.21603 | -47.15564 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0dd81656-b0f5-3ea1-aa80-2b8db00db291 | -12.20697 | -46.72549 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b6b412b3-bbc1-352e-b27f-7e3b4774c257 | -12.20638 | -46.72941 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d7eae9f4-9215-3371-9123-e36164cf6e12 | -12.20445 | -47.48732 | 2024-10-24 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a30994b8-4973-3030-9813-d7facd4016a0 | -12.20348 | -46.72496 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| cc5484d6-3aa9-3d0f-9dfd-79fabbf97156 | -12.2029 | -46.72888 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1a01f170-a4f7-309d-bd3f-b402cc0cab4e | -12.19129 | -46.75909 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 87ecb257-ba28-3540-9e67-8e3a619429e9 | -12.18781 | -46.75856 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5303a549-386d-34da-a93e-3505c3f157e7 | -12.18434 | -46.75802 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| de522f07-923e-3cf9-ae27-23dfeba021d8 | -12.17332 | -46.73637 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd333d29-9292-360a-999a-e8899bc55929 | -12.17274 | -46.74028 | 2024-10-24 04:34:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README43.md)
