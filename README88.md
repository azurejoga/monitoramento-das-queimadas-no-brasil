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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 52b3db96-fa05-3fa4-bd80-e652a6678a5a | -10.60425 | -46.29019 | 2025-09-29 12:19:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| dc21f0ed-dff4-33ad-979d-01341117cbb7 | -15.39497 | -41.09364 | 2025-09-29 12:19:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 43.7 |
| 9e4cad0a-8476-34ca-bb2d-9e0a03e58857 | -14.57895 | -48.23067 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 05b3ccfe-472e-3362-a728-996cf401d91b | -15.0752 | -47.24545 | 2025-09-29 12:19:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 85edc9c1-56b0-3778-880e-d2fd76aac0d9 | -14.60659 | -45.03554 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 9977fcf0-f827-3322-a91d-25570c336c46 | -15.22595 | -50.11139 | 2025-09-29 12:19:00 | TERRA_M-T | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 61fcff55-9798-391c-ba86-6f2738bdb2fc | -15.40763 | -44.97812 | 2025-09-29 12:19:00 | TERRA_M-T | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| f4b73721-98d3-3c30-be40-acf56ced64a4 | -11.66209 | -47.48351 | 2025-09-29 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 7590f00b-caeb-3409-ae7e-8a11cab9d212 | -17.72598 | -46.68682 | 2025-09-29 12:19:00 | TERRA_M-T | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 01543aaa-a3ac-3f1c-9d70-9a13819bc695 | -10.28687 | -45.19458 | 2025-09-29 12:19:00 | TERRA_M-T | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c5f92bb1-e9f1-338f-a785-9e7b88091b1c | -9.71111 | -47.7769 | 2025-09-29 12:19:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 85d3461b-44f2-33ab-aaa5-cc2ec26cdea8 | -13.18008 | -50.71139 | 2025-09-29 12:19:00 | TERRA_M-T | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 151b67d8-a9a9-308c-9641-e2b0724d2837 | -10.46233 | -48.19658 | 2025-09-29 12:19:00 | TERRA_M-T | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 94720c64-06e5-36e5-88ca-707a12488b57 | -11.44314 | -45.04626 | 2025-09-29 12:19:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 24.5 |
| 0dc8ce75-82b4-3a1b-9c36-c82065b350e2 | -15.2585 | -48.76196 | 2025-09-29 12:19:00 | TERRA_M-T | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 71cb6c63-7db6-37a3-8fe4-838e2f24a7e1 | -11.26711 | -48.37009 | 2025-09-29 12:19:00 | TERRA_M-T | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a52bc41f-899c-3693-9979-795fe24d6e9d | -11.80922 | -47.61808 | 2025-09-29 12:19:00 | TERRA_M-T | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 617a2d8f-8073-3d27-9137-98ecef95b54c | -15.91042 | -46.22666 | 2025-09-29 12:19:00 | TERRA_M-T | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8c117c66-c5d9-373b-beba-7bcfbd067461 | -14.53067 | -48.43072 | 2025-09-29 12:19:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 0505692f-8212-3f25-bea5-3ba66dba3c69 | -10.4059 | -48.13646 | 2025-09-29 12:19:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 17.9 |
| cdf21a10-3554-331a-8604-84ff7a2c2fee | -20.36115 | -44.85393 | 2025-09-29 12:19:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 363baa56-73bd-3959-926e-049954d0df6d | -14.70581 | -45.21569 | 2025-09-29 12:19:00 | TERRA_M-T | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.0 |
| bb8a4068-4936-324e-a0b0-b70eb55c066b | -14.89612 | -51.05523 | 2025-09-29 12:19:00 | TERRA_M-T | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 5d3fdfdb-e781-3217-8a60-d7c793e82b7c | -11.3638 | -45.057 | 2025-09-29 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.4 |
| a47151ad-e57a-3f58-a43e-eb2024c3d660 | -10.823 | -46.6538 | 2025-09-29 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 4750f306-779d-3897-aac7-5767090b16dd | -15.219 | -50.1071 | 2025-09-29 12:20:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 06c5f4fa-b480-3c36-a657-611fb54b5736 | -7.8163 | -47.0003 | 2025-09-29 12:20:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 120.6 |
| c1f2aa89-0c81-3ce0-8ca3-0b4dfb5c83ff | -7.8566 | -46.7527 | 2025-09-29 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 6e13c32e-7743-3096-98e0-4e7b3dece0dc | -13.235 | -50.9476 | 2025-09-29 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 22f75d0f-9afe-32fe-88d3-6b9be5ff3707 | -10.8227 | -46.6763 | 2025-09-29 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 87.7 |
| 0e790ee3-cf14-3153-a465-ae865b3ee750 | -7.2402 | -44.7812 | 2025-09-29 12:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 5e2824d5-4a16-3c7f-8502-32be3990a21e | -7.8378 | -46.7544 | 2025-09-29 12:20:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 85.8 |
| f898683b-9794-3782-bbe1-6f75a26b70be | -13.2346 | -50.9691 | 2025-09-29 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 771.9 |
| 2372b027-d5d6-3d9f-b6d9-b428981617a8 | -11.3634 | -45.0801 | 2025-09-29 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| 3424d27c-8fba-3c81-8cf2-e7c21b188f8f | -7.4676 | -46.2974 | 2025-09-29 12:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 65.1 |
| c3229984-790c-39ac-955c-e1a44d07d62a | -7.2214 | -44.783 | 2025-09-29 12:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 46c89669-5c55-3e23-859e-338f090b2fd3 | -14.6049 | -45.0161 | 2025-09-29 12:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 140.1 |
| 3d6b5982-b845-333d-87bf-e7b769545ec0 | -9.7674 | -46.1971 | 2025-09-29 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.3 |
| abb1cd21-92b8-3e83-861d-dbd8f7f04a5e | -8.2662 | -45.5018 | 2025-09-29 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 80fa2fae-dc63-3270-a58c-4c19c99440c9 | -10.804 | -46.6562 | 2025-09-29 12:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 0da0cc27-87fd-329f-b8c6-15af678dbf90 | -8.2848 | -45.5225 | 2025-09-29 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 288.0 |
| 6f8b8d95-9f3f-3ede-810a-acad9c2a1dc3 | -8.2659 | -45.5244 | 2025-09-29 12:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 84fe7863-3c29-3bdb-93bd-f4d5a01c8bd4 | -13.2154 | -50.9715 | 2025-09-29 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 80eb37a6-6175-3172-82b0-dda4e29e4efb | -10.8055 | -45.3637 | 2025-09-29 12:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 874af6c3-6fef-372f-b4d1-3b87eb76ac51 | -13.2005 | -50.716 | 2025-09-29 12:20:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 87.8 |
| b4030704-1c4a-3036-80d4-25131efce702 | -9.8852 | -45.9122 | 2025-09-29 12:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 79.3 |
| 5d2e9f0b-f40c-3742-b831-11e6b8d9b094 | -21.22021 | -45.61769 | 2025-09-29 12:21:00 | TERRA_M-T | CAMPOS GERAIS | MINAS GERAIS | Brasil | 3111606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 3423bdfd-12f0-3ed3-8549-ceb3c56c4cff | -23.24651 | -48.005 | 2025-09-29 12:21:00 | TERRA_M-T | QUADRA | SÃO PAULO | Brasil | 3541653 | 35 | 33 | nan | nan | nan | Mata Atlântica | 30.6 |
| d7625291-6cac-3390-93c9-0a29c434527c | -23.05536 | -50.93774 | 2025-09-29 12:21:00 | TERRA_M-T | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 58.9 |
| 9bfc0191-0b5c-366d-a663-25d86b3e1eba | -21.01774 | -48.04786 | 2025-09-29 12:21:00 | TERRA_M-T | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 846ee97c-af61-3619-947f-f7b81fba653b | -23.06424 | -50.93922 | 2025-09-29 12:21:00 | TERRA_M-T | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 74d64fa4-ba58-3c94-908d-dfd52fcef41f | -21.41866 | -45.38767 | 2025-09-29 12:21:00 | TERRA_M-T | TRÊS PONTAS | MINAS GERAIS | Brasil | 3169406 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.7 |
| 5a8354af-fe0c-34a9-937e-0d51f005376d | -23.05677 | -50.92812 | 2025-09-29 12:21:00 | TERRA_M-T | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| de656868-e852-355d-ae3b-6eb518268e0e | -21.10834 | -45.88104 | 2025-09-29 12:21:00 | TERRA_M-T | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.9 |
| df961c86-0a12-3397-bf0f-a44655e40a4b | -21.32635 | -53.90423 | 2025-09-29 12:21:00 | TERRA_M-T | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 29.0 |
| ea91e2cd-2010-3b55-9388-0f05c31b7576 | -23.31257 | -50.4333 | 2025-09-29 12:21:00 | TERRA_M-T | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| c67b4c2e-b29f-3fea-8bc5-e993507a6e45 | -21.09614 | -45.8933 | 2025-09-29 12:21:00 | TERRA_M-T | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 57f78b29-05f8-3ea0-9671-949bcc20b81f | -23.31393 | -50.42371 | 2025-09-29 12:21:00 | TERRA_M-T | ABATIÁ | PARANÁ | Brasil | 4100103 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| b5f8fd65-b2d0-3616-b6bc-06be22ed5701 | -21.06288 | -46.25557 | 2025-09-29 12:21:00 | TERRA_M-T | CONCEIÇÃO DA APARECIDA | MINAS GERAIS | Brasil | 3117108 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| 022866ce-8310-3650-8f06-a3839e5efe9c | -21.25274 | -44.83149 | 2025-09-29 12:21:00 | TERRA_M-T | ITUMIRIM | MINAS GERAIS | Brasil | 3134301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 4b81ffa1-bed0-39af-a9dc-04b5060da3de | -22.92028 | -45.42842 | 2025-09-29 12:21:00 | TERRA_M-T | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 96fa3211-6b75-369f-b290-69fa14174f6f | -23.57469 | -50.40605 | 2025-09-29 12:21:00 | TERRA_M-T | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 53d7f50e-4ce6-35e1-817f-6be717009d44 | -23.63571 | -51.68707 | 2025-09-29 12:21:00 | TERRA_M-T | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 15.9 |
| 7d3a11fd-d76b-3a0f-a3e7-37fee2dcb6fb | -21.09776 | -45.87973 | 2025-09-29 12:21:00 | TERRA_M-T | CAMPO DO MEIO | MINAS GERAIS | Brasil | 3111309 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.9 |
| 50630a48-03f4-355e-8020-01e4faa6d014 | -23.58356 | -50.40751 | 2025-09-29 12:21:00 | TERRA_M-T | CONGONHINHAS | PARANÁ | Brasil | 4106001 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 3e4f21a3-f14f-3dc8-a3cf-553394a0b003 | -21.01637 | -48.05824 | 2025-09-29 12:21:00 | TERRA_M-T | PONTAL | SÃO PAULO | Brasil | 3540200 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 215daedd-4429-3c36-859e-2036826bb5d9 | -22.22612 | -49.9712 | 2025-09-29 12:21:00 | TERRA_M-T | MARÍLIA | SÃO PAULO | Brasil | 3529005 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 15a50527-e0a9-3be8-b27d-1891069a067f | -23.24795 | -47.99383 | 2025-09-29 12:21:00 | TERRA_M-T | QUADRA | SÃO PAULO | Brasil | 3541653 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 7b260c2a-a4c7-36e6-9d46-50ca5038b46c | -25.06183 | -49.35341 | 2025-09-29 12:21:00 | TERRA_M-T | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| ace90f0e-c15b-3009-ba10-3a96aa359e54 | -23.25139 | -48.00078 | 2025-09-29 12:21:00 | TERRA_M-T | QUADRA | SÃO PAULO | Brasil | 3541653 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.2 |
| f5a119de-19af-386a-9fa2-5ade7380f4da | -23.63718 | -51.67725 | 2025-09-29 12:21:00 | TERRA_M-T | JANDAIA DO SUL | PARANÁ | Brasil | 4112108 | 41 | 33 | nan | nan | nan | Mata Atlântica | 19.9 |
| 52ed1e23-aa5b-3d0e-9f90-d612f3f6f6ac | -23.06565 | -50.92961 | 2025-09-29 12:21:00 | TERRA_M-T | RANCHO ALEGRE | PARANÁ | Brasil | 4121307 | 41 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| b492ed6d-443a-3f35-b617-1912bbcb0f20 | -11.925 | -48.0273 | 2025-09-29 12:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 7112d3e2-e6c6-3a09-b2cc-f3204cc34c51 | -15.219 | -50.1071 | 2025-09-29 12:30:00 | GOES-19 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 61.0 |
| f87baa33-9e18-317f-8518-70ec380a50d4 | -14.6049 | -45.0161 | 2025-09-29 12:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 166.5 |
| bf2b7f84-5886-35b8-9146-9eebada14e2d | -9.7674 | -46.1971 | 2025-09-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.4 |
| 2819ce6b-64bd-3eac-a510-a0024d13b69c | -10.6242 | -48.5167 | 2025-09-29 12:30:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| bf02ddda-546b-37e8-ac9e-009471e7e10e | -11.3638 | -45.057 | 2025-09-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 128.4 |
| a693790b-faec-3b3c-aedb-f40ce5fd9fe9 | -11.3447 | -45.0597 | 2025-09-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 0967ced9-304a-3e2c-b975-7932933d515c | -13.2346 | -50.9691 | 2025-09-29 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 485.2 |
| 7e01be29-c9bb-3999-a853-cbf83c322054 | -7.8378 | -46.7544 | 2025-09-29 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 947a2034-5eef-3f72-a602-f8abc557e006 | -9.7677 | -46.1745 | 2025-09-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 3352082e-7b7d-3f26-8e78-304cada407da | -7.2214 | -44.783 | 2025-09-29 12:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 86.4 |
| 89914b04-6228-3e67-88f5-de1d2a9f6ecf | -10.8055 | -45.3637 | 2025-09-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 125.5 |
| 993619f7-d7e6-3b50-849f-6aa9218e0a15 | -7.8566 | -46.7527 | 2025-09-29 12:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 108.9 |
| da06f326-6ba8-3320-8ae4-e7359a7a7e91 | -7.2216 | -44.7601 | 2025-09-29 12:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 61b55752-c532-3d2d-b6b1-70eeb1142414 | -8.8229 | -46.189 | 2025-09-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 8050c6f2-aa15-3f26-86c3-c9660943c65d | -11.3826 | -45.0774 | 2025-09-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 9aaf11bd-6180-38e5-a02d-977a70aa596d | -7.4676 | -46.2974 | 2025-09-29 12:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 1a8f95ab-f280-3255-98b4-7f188976fc64 | -10.823 | -46.6538 | 2025-09-29 12:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| cc173506-d42a-3efb-8bbb-0263265a2199 | -12.863 | -46.9582 | 2025-09-29 12:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 72bb7a32-6102-3d6c-bdac-46b3393dba92 | -13.2005 | -50.716 | 2025-09-29 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 5f00b29d-429d-3a39-855c-14c92ba99a6f | -7.8163 | -47.0003 | 2025-09-29 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 142.3 |
| a5c7c1af-6557-3d28-bd83-6dfd0b00a529 | -6.9883 | -43.7678 | 2025-09-29 12:30:00 | GOES-19 | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 67.6 |
| d2bc7861-9cdb-3db1-ba23-00760236c7b2 | -11.3443 | -45.0828 | 2025-09-29 12:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7970209c-fecd-39c9-83ba-e3735b99e252 | -7.2402 | -44.7812 | 2025-09-29 12:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| ae750858-2edd-3dea-a81e-7403010f170c | -13.1816 | -50.6969 | 2025-09-29 12:30:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 99ee1533-ce8e-3290-b75e-92fe4fb5a298 | -9.8852 | -45.9122 | 2025-09-29 12:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.1 |
| cc829063-462d-35fd-8134-9e32d7b49507 | -7.8165 | -46.9781 | 2025-09-29 12:30:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 0359039c-9e85-3550-86d8-75e060342af4 | -14.5331 | -48.4491 | 2025-09-29 12:30:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 78.1 |


[Clique aqui para ver as próximas entradas](README89.md)
