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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0ed7e4f-c12b-33cc-82f3-18e7296a2aa5 | -12.80993 | -53.49396 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 6938194e-82ac-300d-a9cc-f38bb703a823 | -12.80936 | -53.4978 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 30b87bb7-9d3f-322b-8943-84846d4cc33f | -12.80878 | -53.50164 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| c178e8f9-23ff-3261-841b-136d306f99c9 | -12.80821 | -53.50547 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| dd5a89d9-6591-3767-b01a-bddfa04936a9 | -12.80764 | -53.5093 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3851eb29-5158-3496-872a-33d86c45ecbb | -12.80707 | -53.51312 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3512611f-3251-35e2-acbb-5ecd0a7a1b5c | -12.80534 | -53.50109 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| cb923d8b-a452-3980-8a2f-b580cd69f00a | -12.80477 | -53.50493 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 880c7d93-08e6-39e6-a1f2-13881b3ebc9f | -12.8042 | -53.50875 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 5a20b2e2-a73d-3cb9-b8b9-f3bf254bf8f5 | -12.67282 | -53.18341 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd202be4-70db-37fa-8e28-8aad96b13051 | -12.63554 | -53.11039 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc91a2e4-4021-3ce2-aa6b-0b9af6bdc153 | -12.63495 | -53.11434 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57d877ed-43ed-31f6-8519-b00ab84b537f | -12.63144 | -53.13811 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| def860be-1136-3af6-9677-2200372c55d3 | -12.62796 | -53.13757 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 79fdee6b-2d29-3a25-be66-fede64e474ed | -12.62556 | -53.29741 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fc2e7520-3892-3217-9118-405a74765b52 | -12.62389 | -53.14098 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60941fb4-a0f1-3aa7-ae96-f6c3d02ebe8a | -12.62389 | -53.01927 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 60e6ec8b-2112-3dcb-baf0-a33b10f74263 | -12.61573 | -53.02613 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a048bffb-bbf3-3c17-b54d-815212075408 | -12.61165 | -53.02956 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d54d3392-c10f-3b52-85dc-ef5c9aaf6674 | -12.5907 | -53.07516 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cbd02125-167a-3a29-8675-4221dbc536d2 | -12.59012 | -53.07914 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7c8fcb6f-a860-3581-a3ed-aaf9d8174886 | -12.5872 | -53.07462 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e01210fc-b5bf-398f-90af-081d6adaf521 | -12.58371 | -53.07408 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6cf0308-f360-3210-b04b-5131887a0746 | -12.58079 | -53.06956 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8c9b602e-d66b-3a42-8df1-725bcc21e699 | -12.57906 | -53.0815 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4556bcd1-eaa7-3899-8e3e-c8728dad0faa | -12.57651 | -53.06597 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3a45c895-28d9-3acb-97e8-7e45dd9cef97 | -12.57591 | -53.06994 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2ac68877-f108-3b78-afde-f63258876a82 | -12.5738 | -53.06848 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fdc54ba2-4d57-39c0-9ccf-4636f5e258af | -12.57354 | -53.08583 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a770ab9c-6ff9-3714-9d37-dffb794620df | -12.57302 | -53.06542 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 118ed5c0-47ac-3b8f-b0bb-ff31eff88060 | -12.57064 | -53.08133 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a259a511-849b-3500-9cfa-21e7211ad2f8 | -12.57005 | -53.0853 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1bf881d5-8c68-3a27-8471-b7faaece2940 | -12.56543 | -53.06832 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89d78c4b-904f-3939-96ad-641e116875f5 | -12.56484 | -53.07231 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a19fde2-8041-3dde-ab67-f8db6abb3562 | -12.56135 | -53.07177 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bd7ce07e-9e4b-3ec1-bf7f-9eba502fbd71 | -12.52979 | -53.23569 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d82256e4-ad65-3a41-ae84-e8034211fabd | -12.52632 | -53.23515 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00143cf7-6038-3ba4-85e6-9734b5618e00 | -12.52227 | -53.23854 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6bee2c20-068b-3924-b303-fcfc31e64864 | -12.51835 | -53.52113 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb3dca54-f4eb-3a2c-9f92-de247a488385 | -12.51779 | -53.52495 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89977b38-845d-38e0-95ed-3d76f9edcaee | -12.51475 | -53.24138 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 21a3511a-314a-31dc-a143-ff6e4932b7c4 | -12.5138 | -53.52824 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 349bac15-0110-31ae-9502-0a78e2987ec7 | -12.51361 | -53.22519 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b87339f-705a-32d7-b8cc-5420cfae1ac8 | -12.51324 | -53.53205 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4b4e2308-2f59-3961-889a-56a2c2cf3f81 | -12.51303 | -53.22909 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 75dbf206-032f-33fb-b4e4-98ac3abefabf | -12.51242 | -53.25703 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b4d0c9a-8ba8-32cb-ba6b-7539265555df | -12.51186 | -53.23692 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d13cf2f-e49a-34a8-aafc-492e058ed219 | -12.5107 | -53.24476 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94f427a8-9596-3503-a87d-1dc25bbea3a2 | -12.45968 | -53.15693 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e0f2cd5-a121-37c4-ac23-432d0e219a73 | -12.4195 | -53.12706 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c902fa94-a319-3e86-b4ed-848217d85ae7 | -12.32584 | -53.44928 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 438e9469-0646-33c2-ba02-16771ffc2bcb | -12.97135 | -53.53754 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 01e57ac7-56f6-3fae-96af-945aaf92e9e2 | -12.96791 | -53.53701 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a19bb92-c808-366f-9f89-d23d6ece456d | -12.96734 | -53.54084 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5071f28c-38e7-30d4-931f-4221a86dd9e8 | -12.96503 | -53.53265 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f146d81-b331-37e9-bbbb-d98870b79f39 | -12.96447 | -53.53648 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 312d62a9-ca4c-3305-b494-0f4b9dd29e3f | -12.9639 | -53.54031 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 649f4a08-054d-31c1-9f6d-27f5b03ac49f | -12.96271 | -53.52444 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8ce55843-3d67-3909-980f-62e8e0c22107 | -12.96159 | -53.53212 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ccba8bd-32f4-3fbc-8ca0-1769c6e1ab77 | -12.96102 | -53.53595 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0c41cb3c-724f-3f84-a7a6-b19ad78e17bc | -12.96046 | -53.53978 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8b73a326-3c08-3c45-882d-e6aa87fadd1f | -12.9599 | -53.54361 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1b4a6ca7-8836-39a5-88dd-3ef4fad7493f | -12.95927 | -53.52391 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f49a014-1343-3b2c-87e8-9377aa59820c | -12.95814 | -53.53159 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1c2afaed-c9fa-3ff6-832b-9ecf859facf5 | -12.95758 | -53.53542 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| ea2922b2-83a1-3448-a17b-dff131c69467 | -12.95702 | -53.53925 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 5fe5b082-aeac-30dc-92ee-ab77d31ba41f | -12.95645 | -53.54307 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 8991dd0e-e209-3eb4-861d-d418c069978c | -12.9547 | -53.53105 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6f8a33a2-dcf7-36c1-b76e-e038ac20531c | -12.95414 | -53.53489 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 961c4e07-ef2a-3c9a-95ce-bf6b76a987b0 | -12.95357 | -53.53872 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| d366bb67-61e4-3d66-95de-cd74e6d8bcb9 | -12.95301 | -53.54254 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 92525022-c2a0-348e-a338-f2be056ff3f3 | -12.95182 | -53.52667 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 7ae6b55c-9392-33cf-a7fd-4f2f74396ad3 | -12.95126 | -53.53051 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| ecd9e767-bf99-3283-9abf-766dd4b0cab4 | -12.95069 | -53.53434 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| b17525f9-cf0f-3db0-8f82-905344b8ca61 | -12.95013 | -53.53817 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| eaeeb08a-0500-3991-86d0-04765373a681 | -12.94957 | -53.542 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| ffca4414-ec56-3e0d-9dbf-744e5df394f2 | -12.94781 | -53.52996 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 9bbf6ad0-3816-36d6-951e-0a1088506805 | -12.94725 | -53.5338 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 7ba07317-2096-3170-ad93-8ef2f7ebbb57 | -12.89269 | -53.52621 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ab41cebc-d911-32e2-a7db-bdcbfcf308ff | -12.85372 | -53.52793 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4b1b7d8-d010-3212-b3e7-b7a75278c390 | -12.85084 | -53.52357 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7ed04c0b-ef4b-3feb-bbb0-c846907617bb | -12.85028 | -53.52739 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 77413d83-a625-350c-a6bb-825fbf7595d6 | -12.84684 | -53.52686 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f658e907-877f-3fa0-8501-bc10a46011c8 | -12.83939 | -53.52959 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6cdb8b2a-e8d5-3d57-9cba-46840d6fa884 | -12.83595 | -53.52905 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 22407446-7924-3e73-912b-d1e9b7b56b5e | -12.83307 | -53.5247 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eb51db43-2d32-39be-83a6-44e316658971 | -13.28926 | -53.75725 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 75cbee20-5ab0-32e6-bdd3-596f14a91833 | -13.28583 | -53.75673 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 455b1430-caac-335d-99d1-262859395160 | -13.28527 | -53.76056 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5dff35e3-5df3-3698-9727-f5d4bc35a71d | -13.28241 | -53.75622 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 411b5e31-c055-3f02-b36f-33cd9e26d1c5 | -13.28184 | -53.76004 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f8633bcb-e2b3-3b83-a5f3-0ca5df790be8 | -13.27955 | -53.75189 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e1d8641-ddf0-3fd6-8ea4-82b62bc60a54 | -13.27898 | -53.75571 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 173a68dc-a2c2-3840-83df-61342cbf6126 | -13.27556 | -53.75518 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee44766b-ce8c-3548-bf6f-813440b5229b | -13.27326 | -53.74703 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5f3b46d9-0a9b-3fad-90b1-a8bc7517d275 | -13.2704 | -53.74268 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 905f86f5-a42c-3591-99ec-634985af0c05 | -13.26983 | -53.7465 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c3ebfcf-9a37-3b84-80c8-3c3143a22a88 | -13.26927 | -53.75031 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ba378b0-a774-36a1-82bc-f2070c787325 | -13.26641 | -53.74596 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df1add65-6f52-3c68-97d6-cdcd710c6a1d | -13.26299 | -53.74542 | 2024-10-12 04:59:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README74.md)
