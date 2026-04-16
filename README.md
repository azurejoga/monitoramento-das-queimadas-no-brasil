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
| 9dd5023d-d9ec-3a88-823f-ea2ea8806bf9 | -21.1903 | -47.3688 | 2026-04-16 00:10:00 | GOES-19 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 45.4 |
| c1b1f6fd-24aa-36a2-960c-c7c3619dacd2 | -11.9571 | -44.0145 | 2026-04-16 00:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 3afcc96b-c50a-3d80-a729-bb51b8844651 | -11.9571 | -44.0145 | 2026-04-16 00:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 8060a5ed-0e6f-3cea-8557-de58f1b4cbbc | -11.9571 | -44.0145 | 2026-04-16 00:30:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 644dea6f-6ae3-3c2f-ae9d-f9b411d37a3e | -21.1903 | -47.3688 | 2026-04-16 00:30:00 | GOES-19 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 71d6475f-b778-3ce1-8df9-1386e3099913 | -21.187799 | -47.368801 | 2026-04-16 00:35:00 | METOP-B | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| a2a538fb-b05e-3de1-aa07-5a6ad65be467 | -18.497101 | -51.604401 | 2026-04-16 00:35:00 | METOP-B | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| efce6f40-a0b7-38ab-9db0-ffb7237ab8ce | -20.5331 | -49.4804 | 2026-04-16 00:35:00 | METOP-B | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| db5baefc-8099-30fb-9844-859cd354c05b | -21.7096 | -48.429501 | 2026-04-16 00:35:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 5f7f4fab-5899-37bf-981a-158a51bf219b | -21.184999 | -47.3577 | 2026-04-16 00:35:00 | METOP-B | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 95d9823b-4d06-37dd-a342-e41076a4e8f5 | -18.498899 | -51.612099 | 2026-04-16 00:35:00 | METOP-B | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 5db7a6ac-cb8b-39b1-8b0b-0b7d19c34555 | -21.707199 | -48.419899 | 2026-04-16 00:35:00 | METOP-B | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 4f30c56a-0a23-3eb2-9458-f7462d676e8a | -11.96 | -44.0172 | 2026-04-16 00:35:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e9dee997-91a9-3cf0-b0e7-df3e6b7eaab5 | -11.9531 | -43.991402 | 2026-04-16 00:35:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8d6d79ae-0927-3f4e-8d7a-2e2b5193fa91 | -20.41 | -49.745899 | 2026-04-16 00:35:00 | METOP-B | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 46ff935c-68e0-3ae9-bc4b-cfe116c17e30 | -11.9504 | -44.019901 | 2026-04-16 00:35:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ea7e6aba-d80e-3866-80a1-d185a4cbf478 | -11.9435 | -43.994099 | 2026-04-16 00:35:00 | METOP-B | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 302cd169-63ca-307e-9678-328034c0d0de | -20.5352 | -49.4893 | 2026-04-16 00:35:00 | METOP-B | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 58e41e27-fb6c-35dc-8dc8-dc233c18780e | -20.1679 | -46.584702 | 2026-04-16 00:35:00 | METOP-B | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a0bac277-4d8b-3c84-9fbb-01fd630edcfe | -21.71611 | -48.4348 | 2026-04-16 00:35:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 61d4076e-4437-38d9-aa69-c22052d43480 | -21.71422 | -48.4229 | 2026-04-16 00:35:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b5dec90d-58e5-3d40-9d6e-7d125ce3902c | -21.70631 | -48.43677 | 2026-04-16 00:35:00 | TERRA_M-M | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 34574f5e-30bc-3520-95e8-73cabe37feda | -20.68615 | -49.40128 | 2026-04-16 00:35:00 | TERRA_M-M | IPIGUÁ | SÃO PAULO | Brasil | 3521150 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a8ded975-bf15-34fe-a34c-7b3cfb118258 | -20.17583 | -46.59417 | 2026-04-16 00:35:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| ded4a062-e12f-3f72-b0aa-367fcfa5e2b3 | -20.17548 | -46.60394 | 2026-04-16 00:35:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 0ffc9d37-4fde-38d3-8757-273057c259c5 | -20.53529 | -49.49566 | 2026-04-16 00:35:00 | TERRA_M-M | MIRASSOLÂNDIA | SÃO PAULO | Brasil | 3530409 | 35 | 33 | nan | nan | nan | Cerrado | 36.4 |
| fe66a39d-0918-3120-b8ec-de51336dbca2 | -18.49447 | -51.61528 | 2026-04-16 00:35:00 | TERRA_M-M | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 8.7 |
| f2177635-3197-38d8-ada5-1b736ec3d8f2 | -20.40957 | -49.75939 | 2026-04-16 00:35:00 | TERRA_M-M | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 4c246ddd-fd5e-3b53-b0a2-7a9861363459 | -11.97103 | -44.04123 | 2026-04-16 00:37:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 032aa047-a0ba-30c3-a548-4617714ff89f | -11.95392 | -44.00002 | 2026-04-16 00:37:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 37.9 |
| 8f150075-f780-347a-815e-0d9c345e34ca | -11.96052 | -44.03611 | 2026-04-16 00:37:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| a77ed547-8446-3fc5-88c1-87ab2d3f22e9 | -11.96472 | -44.00513 | 2026-04-16 00:37:00 | TERRA_M-M | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 276ac482-6c5d-3f1b-ba42-d3fed4e813e3 | -21.1903 | -47.3688 | 2026-04-16 00:40:00 | GOES-19 | CAJURU | SÃO PAULO | Brasil | 3509403 | 35 | 33 | nan | nan | nan | Cerrado | 36.9 |
| ff276156-30c7-375a-a925-7e349dcff1b1 | 3.23746 | -60.74245 | 2026-04-16 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 15ed52f3-ccab-3aaf-9d94-fe92dd8933d3 | 1.282 | -60.31839 | 2026-04-16 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0915d047-06fe-3016-a39f-1cb1b201b7c2 | 2.42361 | -61.35537 | 2026-04-16 00:41:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2607b356-f26f-3964-a880-525f51906b02 | 3.30444 | -60.77055 | 2026-04-16 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e53c91ea-01d1-34ec-95e8-2b5da6c50390 | 3.237 | -61.19956 | 2026-04-16 00:41:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| b800aa67-6724-30d6-87bc-1cd5d6379507 | 2.07885 | -60.96132 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 3674eb95-e1e5-3484-8ffb-383cb4996c7f | 3.24281 | -61.19264 | 2026-04-16 00:41:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 1b770c9f-de79-3196-8b42-202d210be00d | 3.30624 | -60.7582 | 2026-04-16 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ed9566f7-ae38-3256-86a3-93b82ce1aa46 | 1.94927 | -60.37967 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| eaaa73b2-ee72-3547-b1dd-d1ca4f9c853a | 2.07323 | -60.96785 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fc2d422c-431f-34ce-9e13-baffd4a803ee | 3.24086 | -61.20595 | 2026-04-16 00:41:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 88a7e51b-1289-3950-8edd-0b6e216135de | 1.90721 | -61.10411 | 2026-04-16 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 5.8 |
| b7d5ac2d-bb96-3271-af56-baf176f69094 | 1.81566 | -60.9463 | 2026-04-16 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| c0332516-d5e2-3db0-8472-416be149aa22 | 2.51321 | -60.6535 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 19.8 |
| e22b5899-3c62-3074-8245-7931aadc9c41 | 1.28027 | -60.33072 | 2026-04-16 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 45d3fb97-8b57-34d5-aff7-46dc3ad0cfa4 | 2.07507 | -60.95449 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 942ad37c-3d7b-3925-b435-f1abe3777d0d | 2.02949 | -60.59233 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.4 |
| c17391d9-4c56-3578-91da-027c36b87207 | 3.27485 | -61.19722 | 2026-04-16 00:41:00 | TERRA_M-M | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9346e497-4b57-38bd-a4a0-d47ce9c86c62 | 2.02767 | -60.60485 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 1ee9c6e9-90cc-3cc2-ba68-074d9f8c4522 | 2.06815 | -60.95981 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d13c5bd2-aed4-37ac-8190-53ac7d4a6f92 | 1.28373 | -60.3061 | 2026-04-16 00:41:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| ed1f3a05-0d3a-3bff-9003-bc7c41e0e29a | 2.23995 | -61.27418 | 2026-04-16 00:41:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f30ffd4c-0528-399d-9616-cb7746830bc4 | 1.93901 | -60.37826 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 575eeab3-cc08-3505-9382-41835f674777 | 2.52358 | -60.655 | 2026-04-16 00:41:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| a03a57ed-b8f6-3d19-8a2d-85e47155fbdd | 3.3103 | -60.7805 | 2026-04-16 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 15ade6ba-fc70-30f7-adb2-f802d149e178 | 3.3103 | -60.7615 | 2026-04-16 01:00:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 104.9 |
| 20744f22-4485-36db-aa86-9ef384dc1519 | -12.97125 | -40.69032 | 2026-04-16 03:19:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7b592d34-7083-3ac9-a712-8eba70f3bfbe | -12.97226 | -40.68545 | 2026-04-16 03:19:00 | NPP-375D | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0946a730-8345-3a2b-8dfd-01c4041fdac5 | -19.59082 | -40.0779 | 2026-04-16 03:21:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b48b028b-e807-355c-9923-a7eacb0bcb9a | -19.5961 | -40.07914 | 2026-04-16 03:21:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| aa94a1a3-6b54-36a7-9b8e-bbe6c4741083 | -19.60062 | -40.08391 | 2026-04-16 03:21:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e5b6b1c4-c256-3901-b338-7f7777f020aa | -19.59156 | -40.07447 | 2026-04-16 03:21:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8bb1df1b-b50d-3aa5-ab81-496db9b705f7 | -19.59535 | -40.08263 | 2026-04-16 03:21:00 | NPP-375D | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| c4f223c0-7cf7-3949-91c3-d10b1e5666bf | -19.12522 | -40.38396 | 2026-04-16 03:21:00 | NPP-375D | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 850224cb-e5c8-3a22-a553-e7dec71129e4 | -19.4691 | -40.64234 | 2026-04-16 03:21:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| bbf7b340-a1be-3a23-af0d-7a0d9e5889b0 | -19.12606 | -40.38 | 2026-04-16 03:21:00 | NPP-375D | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7cb605f4-e7ba-36e8-ac30-98d31bcc0d80 | -8.03546 | -36.02398 | 2026-04-16 03:38:00 | NOAA-20 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a28ba150-4e3d-3624-8753-0bb483e5f5c6 | -15.28438 | -43.66948 | 2026-04-16 03:40:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b0e7374-6984-3383-9c60-0acf597e771a | -11.79925 | -40.33153 | 2026-04-16 03:40:00 | NOAA-20 | MAIRI | BAHIA | Brasil | 2920106 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 295e5908-bb45-31ac-88bd-f91015b2be49 | -11.96166 | -44.01446 | 2026-04-16 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0a6e8397-40ca-32c7-bf23-f4fea1609db3 | -11.95227 | -43.37658 | 2026-04-16 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 732820dc-dbe2-38f5-8285-649c1f292fc9 | -11.95668 | -43.38081 | 2026-04-16 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4305b93d-9773-3f98-8a14-017ed2209c0f | -12.83858 | -43.81972 | 2026-04-16 03:40:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 394540a7-9190-373f-b53f-e67874bd219b | -12.2423 | -44.21963 | 2026-04-16 03:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 769e8414-f0bf-3c67-b90b-b1616d438b08 | -11.96213 | -41.3283 | 2026-04-16 03:40:00 | NOAA-20 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 072506bd-9b76-39b7-b0cf-0ddcc8f00400 | -16.60093 | -43.36279 | 2026-04-16 03:40:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f4d3accc-f177-328f-b627-59c288131a6d | -11.96102 | -44.01769 | 2026-04-16 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 2b9ef632-ba59-3f13-a32b-33bb1d1bd7f1 | -11.9614 | -44.01661 | 2026-04-16 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 52137183-8fec-3b21-95d5-7ddfe88cc7e9 | -16.60188 | -43.35792 | 2026-04-16 03:40:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d1cd185-e8c1-33ca-9009-c86a3bdee1ef | -12.45735 | -43.78075 | 2026-04-16 03:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 84546986-c433-3110-9342-c18c800d839e | -12.84366 | -43.82076 | 2026-04-16 03:40:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 66d0e8d1-c390-33b9-b34e-cea405bbafdd | -12.84308 | -43.82379 | 2026-04-16 03:40:00 | NOAA-20 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5dd36c58-b366-3ec7-b12d-123b98126c71 | -12.45432 | -43.78341 | 2026-04-16 03:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 969f7ce6-42a4-3c5b-bf2e-d2118e4a3026 | -11.95288 | -43.37331 | 2026-04-16 03:40:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8e96a544-e3e2-323a-bd44-088372b1bc36 | -16.84837 | -39.54687 | 2026-04-16 03:40:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7307c688-3fd4-394c-aee1-a353516a0d86 | -12.24294 | -44.21626 | 2026-04-16 03:40:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1b890377-b6dd-37ad-92a1-31298cfc6a5d | -12.01451 | -45.34356 | 2026-04-16 03:40:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9a75796-83cf-3876-a7c5-a8cb354c60ed | -11.96079 | -44.01985 | 2026-04-16 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 88b4755f-5ec1-322c-aa0f-00a4eecb1d97 | -12.4549 | -43.78032 | 2026-04-16 03:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b6782861-260f-3cbe-b2fe-26ad2e155bed | -12.45166 | -43.78276 | 2026-04-16 03:40:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6bac570-bfdc-3d46-820c-3a1f8bebced3 | -11.96201 | -44.01337 | 2026-04-16 03:40:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| a95a96d8-97e9-32cf-a93d-b88823277164 | -16.85201 | -39.54762 | 2026-04-16 03:40:00 | NOAA-20 | ITAMARAJU | BAHIA | Brasil | 2915601 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3efb4096-a406-3873-a1a3-ce322b71fd60 | -12.97038 | -40.68598 | 2026-04-16 03:40:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 933de670-26ed-3a22-9e53-e832350ebb5a | -20.16927 | -46.60336 | 2026-04-16 03:42:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e758ad9d-e18d-3536-9233-9af3ba632e94 | -19.59255 | -40.07642 | 2026-04-16 03:42:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| a1e7617c-2189-3bb5-a2d6-5b51f92daa05 | -19.12448 | -40.38232 | 2026-04-16 03:42:00 | NOAA-20 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 47f20da0-3e05-3436-be8e-1dffc31c8f1c | -21.08434 | -43.09977 | 2026-04-16 03:42:00 | NOAA-20 | DORES DO TURVO | MINAS GERAIS | Brasil | 3123304 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |


[Clique aqui para ver as próximas entradas](README2.md)
