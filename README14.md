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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3fcdb20-6c36-3fd0-a239-d78b0028d656 | -18.62399 | -43.92127 | 2025-08-13 03:51:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 14b457c3-1b7c-3914-95d2-0492cbe53f0e | -23.13548 | -46.60132 | 2025-08-13 03:51:00 | NOAA-20 | ATIBAIA | SÃO PAULO | Brasil | 3504107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b471d9dc-0866-3c4f-8d87-049aa1a35b0e | -19.994 | -44.40052 | 2025-08-13 03:51:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ebe584e1-009c-3273-a8a0-da2a92beac0b | -18.05877 | -46.02054 | 2025-08-13 03:51:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9fa3a34c-2a2b-3639-b641-f6b09c49170c | -17.65445 | -46.68365 | 2025-08-13 03:51:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 353982ba-626c-302e-b3da-67ffbea6f95b | -20.92123 | -45.24987 | 2025-08-13 03:51:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7fab6b03-8051-3c79-8f33-1f408dc78510 | -18.52952 | -46.05657 | 2025-08-13 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d4047242-b5a8-3a09-abab-994d035b73e2 | -16.30968 | -52.91566 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8322489f-2477-3070-8b51-b83ee4e80d4c | -21.81106 | -49.88863 | 2025-08-13 03:51:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 8277c241-7814-379c-b310-c72edc7da23f | -21.76078 | -46.59317 | 2025-08-13 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| aa61b9dc-bb78-3121-9bd2-e708bad145c9 | -20.19696 | -45.43042 | 2025-08-13 03:51:00 | NOAA-20 | SANTO ANTÔNIO DO MONTE | MINAS GERAIS | Brasil | 3160405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 57a03961-faae-3ebc-ad8d-aaecfd0e3851 | -18.86584 | -47.27053 | 2025-08-13 03:51:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11bc7110-8fa8-3d43-9e66-d46d23366971 | -19.29648 | -48.43295 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6eb13898-d7ac-33f7-b725-17b4ecd0888a | -22.37883 | -45.47769 | 2025-08-13 03:51:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 9376572f-444a-310f-9451-483e53705392 | -22.6868 | -47.30667 | 2025-08-13 03:51:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c2250b32-ea02-350f-acc0-0cb804df8e88 | -20.92235 | -45.24789 | 2025-08-13 03:51:00 | NOAA-20 | CAMPO BELO | MINAS GERAIS | Brasil | 3111200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 18428634-7544-3ba5-8d11-f335e04eba6a | -21.16004 | -41.62788 | 2025-08-13 03:51:00 | NOAA-20 | BOM JESUS DO ITABAPOANA | RIO DE JANEIRO | Brasil | 3300605 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 0d36e162-ec5f-3a6c-b51a-bf544eb28cf1 | -18.53381 | -46.05746 | 2025-08-13 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a610b67f-8b2d-3986-b077-f5ee693ad13d | -19.99734 | -44.39857 | 2025-08-13 03:51:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 4ba2da37-eb1a-3b2c-8214-87d103eb8e96 | -22.75111 | -47.19654 | 2025-08-13 03:51:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fbdb2d16-9137-3f29-bcba-655152d33d47 | -17.04897 | -51.79694 | 2025-08-13 03:51:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6e24e006-7711-38ad-b5ce-6f54f49ad59b | -18.919 | -48.22149 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8265cbe1-2b5f-3794-8eac-8a6cc96c17ae | -18.91538 | -48.22184 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 2674ed42-77cc-3222-8bb2-d65c72f7064d | -21.76033 | -46.59404 | 2025-08-13 03:51:00 | NOAA-20 | POÇOS DE CALDAS | MINAS GERAIS | Brasil | 3151800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| 81d7eab0-4187-3361-96e7-665a982fc9c3 | -23.19381 | -48.96766 | 2025-08-13 03:51:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 39faa8a8-3ad3-36d5-a875-6ef614732cd7 | -22.47584 | -51.96947 | 2025-08-13 03:51:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 081a5baa-600f-345f-ac9b-60a9f6a79aaa | -22.37597 | -45.47142 | 2025-08-13 03:51:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9e99667f-072b-3519-846a-d100a170f2e3 | -20.85642 | -49.07369 | 2025-08-13 03:51:00 | NOAA-20 | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 09f0c864-0d2d-3b11-910b-877606e02136 | -16.30845 | -52.9174 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f927c3bd-1ba5-3f39-b470-01237e79cd96 | -18.5381 | -46.05838 | 2025-08-13 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| e66b986e-15c6-3cc7-bee7-bf37c13c1d95 | -19.73244 | -45.60297 | 2025-08-13 03:51:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7080635f-2539-3b25-a8cf-c623d00a78c4 | -23.22306 | -46.8895 | 2025-08-13 03:51:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d1d5d43-7de2-30ea-879f-5d7f3722ac5f | -18.61015 | -43.9331 | 2025-08-13 03:51:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f15b2500-2a46-39f4-a332-8e85f019cc4b | -19.8738 | -46.39219 | 2025-08-13 03:51:00 | NOAA-20 | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0312d371-7878-331b-856d-ca772ac6b96d | -16.30781 | -52.92385 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 93f63318-5a9f-3b78-ac42-79e487cb22e0 | -19.76131 | -46.43179 | 2025-08-13 03:51:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a6ad1434-418d-317d-b0f2-f1edd51cda80 | -18.53462 | -46.05325 | 2025-08-13 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9f7ad18-8e8c-320a-b2c1-7bd91c08a7d3 | -18.54237 | -46.05933 | 2025-08-13 03:51:00 | NOAA-20 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 2d7cb2f5-85e1-3e97-9919-28da21dc5d68 | -18.9141 | -48.22045 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e090161-44af-35c0-a63b-9007847a28f3 | -21.81175 | -49.88544 | 2025-08-13 03:51:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 1c5fcdac-d1ed-3462-85c1-4c12ffe6aeac | -22.75199 | -47.19219 | 2025-08-13 03:51:00 | NOAA-20 | PAULÍNIA | SÃO PAULO | Brasil | 3536505 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d00450d-6413-3de2-b778-2c6a178b10f4 | -19.07956 | -48.15312 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cd11e6fe-8213-3f0c-ab6b-3b3f1cd809c3 | -22.08456 | -46.59211 | 2025-08-13 03:51:00 | NOAA-20 | ANDRADAS | MINAS GERAIS | Brasil | 3102605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef4f9741-8299-3336-9c3c-5f55bc4613ae | -22.38659 | -45.47927 | 2025-08-13 03:51:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 84cbe3bc-0f28-39ca-a9eb-e7d50b0fe7ff | -22.29142 | -41.76517 | 2025-08-13 03:51:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 40fd63a7-783a-3776-9174-95d6b95ae2bc | -19.57487 | -49.43018 | 2025-08-13 03:51:00 | NOAA-20 | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0fcb73ba-c1fc-3065-8305-f5c7ff578c8b | -16.31461 | -52.92539 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df939748-5ea0-34da-847c-cfd200597702 | -22.3876 | -45.47385 | 2025-08-13 03:51:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ccb6ed87-8de2-3418-9bd5-360c1702ae7a | -19.76049 | -46.43598 | 2025-08-13 03:51:00 | NOAA-20 | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7abcf0ad-474b-3dcc-98cd-3a8f13e6ee69 | -18.65696 | -46.83553 | 2025-08-13 03:51:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08819b31-e69d-3443-a1ea-b161fda263c8 | -18.05283 | -47.94402 | 2025-08-13 03:51:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b97c1bb3-55f7-3d4c-846f-addd748fdf98 | -19.08072 | -48.14748 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 560e6f26-2dad-371f-be88-ec290041e0e6 | -23.12941 | -48.77739 | 2025-08-13 03:51:00 | NOAA-20 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 022302ce-30c5-328a-998f-33b3bd23dcbe | -22.30747 | -45.92327 | 2025-08-13 03:51:00 | NOAA-20 | POUSO ALEGRE | MINAS GERAIS | Brasil | 3152501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 788ee747-b4c5-357c-8baa-1c26aec288a2 | -16.29986 | -52.92394 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0b83ab98-9e84-3e22-8d52-c716be5c667f | -18.61391 | -43.93392 | 2025-08-13 03:51:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 56f1248e-86ae-385b-bc65-9b2ec45653c4 | -23.22382 | -46.88561 | 2025-08-13 03:51:00 | NOAA-20 | JUNDIAÍ | SÃO PAULO | Brasil | 3525904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a1d334ce-eab1-3be1-9222-247afb7047e6 | -21.81037 | -49.89183 | 2025-08-13 03:51:00 | NOAA-20 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| b7e352e6-07d3-3aa7-8ee8-6a5a060a008e | -22.37984 | -45.47224 | 2025-08-13 03:51:00 | NOAA-20 | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 930fcc5a-c7fd-3272-958c-c4cde00b306a | -18.54318 | -46.0551 | 2025-08-13 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 1887c239-1a47-3469-9220-4bd519633922 | -18.9129 | -48.22644 | 2025-08-13 03:51:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f538740f-a1b2-33a0-8aa1-b66dfbcd10ef | -20.37 | -46.55407 | 2025-08-13 03:51:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2731a6a4-9396-3fa1-a02c-d8d8b194a46f | -16.30663 | -52.92558 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f9ec58e4-fe90-34d0-ad4a-6276386d1cbf | -18.61479 | -43.92901 | 2025-08-13 03:51:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 17a2018b-6f6c-3670-b930-5ede6c467807 | -19.99488 | -44.39559 | 2025-08-13 03:51:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 245987fc-0e31-3d08-8cd5-fcca1d7c30c4 | -21.29534 | -45.926 | 2025-08-13 03:51:00 | NOAA-20 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 7341c377-4a6c-3db2-ab0c-42edb40d18f5 | -16.301 | -52.92236 | 2025-08-13 03:51:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 339a88df-abb4-3b4a-bef7-f8ac0ab4568d | -18.53033 | -46.05234 | 2025-08-13 03:51:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1e60c35b-06cb-3308-8ca6-b93f6f38002a | -27.11493 | -50.57187 | 2025-08-13 03:53:00 | NOAA-20 | CURITIBANOS | SANTA CATARINA | Brasil | 4204806 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| ea36a05c-5594-3780-bdb2-ef706915b27d | -8.106 | -55.5701 | 2025-08-13 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 6d80c3ca-9ce7-3137-b285-42c16d1736a0 | -2.9108 | -48.254 | 2025-08-13 04:00:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 63cfc2c2-b5a8-39be-a79a-ed168d6b355e | -7.0935 | -60.0237 | 2025-08-13 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 833157ed-5ed5-374b-bbcd-e9e517ea521e | -12.4981 | -46.9666 | 2025-08-13 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 58.8 |
| d04e9af5-5b78-3326-9237-8e9b1ddee8b2 | -7.1299 | -60.1182 | 2025-08-13 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| dfdf7e18-7b15-33b5-a583-ecab365ab4ee | -12.5746 | -46.9781 | 2025-08-13 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 47926607-0a35-368f-9477-e3e5c7f12354 | -8.1246 | -55.569 | 2025-08-13 04:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 5b9fa597-200f-3310-8da7-8a151e98240e | -12.5173 | -46.9639 | 2025-08-13 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f6545295-9338-317d-9253-b46217f4ae79 | -8.1246 | -55.569 | 2025-08-13 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| 736d30a4-0b79-3dd9-b630-51f0214ae08c | -2.9108 | -48.254 | 2025-08-13 04:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| e5551650-a007-3e99-b198-b09f55683d71 | -2.8923 | -48.2546 | 2025-08-13 04:10:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 43889013-a9c6-3b42-b6d7-c2a36ef4728f | -18.5499 | -46.0606 | 2025-08-13 04:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 4797fadd-ec39-37d3-b7ec-9cd990a30b10 | -7.1299 | -60.1182 | 2025-08-13 04:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 8873ee67-8b27-3f86-bcc7-9b9a63089d07 | -18.5505 | -46.0369 | 2025-08-13 04:10:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e7326f26-a934-3cb9-82b8-3e70cbfdcd8e | -12.5938 | -46.9753 | 2025-08-13 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.9 |
| fac9d02b-bce7-3c58-896a-d5004404e0fd | -18.5303 | -46.0414 | 2025-08-13 04:10:00 | GOES-19 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 585c4658-540c-3b4c-bb0c-72356e79ce20 | -12.5746 | -46.9781 | 2025-08-13 04:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e11d4f89-d48b-39ec-ae0c-9a7b66113047 | -8.106 | -55.5701 | 2025-08-13 04:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 76.2 |
| fbb18ac3-b214-388a-bebd-6be86429231b | -8.106 | -55.5701 | 2025-08-13 04:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| eb1900a0-8564-3467-98ef-2b680fddb166 | -7.1299 | -60.1182 | 2025-08-13 04:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 85c251b1-52c9-36d9-b220-86baf2fc825c | -18.5505 | -46.0369 | 2025-08-13 04:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 1a835d2d-1e9f-3ce0-aa6a-3825514fbf5d | -18.5499 | -46.0606 | 2025-08-13 04:20:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 30c52f27-d11f-38fb-b20d-2cbf1938604b | -12.4981 | -46.9666 | 2025-08-13 04:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| c2ef4971-4431-3e6e-ad04-ab91c78bffe9 | -18.5499 | -46.0606 | 2025-08-13 04:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 75.5 |
| f3c653c7-e43a-3819-8b12-b8fbd9a2f8e9 | -2.9108 | -48.254 | 2025-08-13 04:30:00 | GOES-19 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| d472e3c8-e713-3581-ab10-19d0eec5c508 | -18.5505 | -46.0369 | 2025-08-13 04:30:00 | GOES-19 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 79a05009-ca0f-355f-a523-bf75875963fc | -8.106 | -55.5701 | 2025-08-13 04:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 52.7 |
| 406e53e3-d3f8-3fc2-b64c-8a8293fc5eb9 | -16.3153 | -52.9201 | 2025-08-13 04:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 49.6 |
| e058b3f9-b45f-3e4b-af27-0b1070e16e59 | -2.8984 | -48.24741 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0c0b8ca1-aef1-3108-8dae-d3187cae540b | -5.45114 | -43.57153 | 2025-08-13 04:38:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 501a4e9b-18f2-3cd9-b073-e2263d980e6a | -2.90781 | -48.2524 | 2025-08-13 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |


[Clique aqui para ver as próximas entradas](README15.md)
