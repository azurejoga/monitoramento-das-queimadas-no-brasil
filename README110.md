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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c113ee43-2bf4-328f-9ca4-27cf1b29c375 | -6.09503 | -52.82973 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 422c7a26-5c2a-3d68-81e3-1f31747ca561 | -6.09445 | -52.83338 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc976bfb-b1b4-3ad9-b829-9436700dbc9d | -6.09219 | -52.82557 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae15e1c0-0d60-3576-8ceb-a40128bd3eb5 | -6.09044 | -52.83655 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 956788e8-a64c-3b4c-82af-ecbe87d97eea | -6.08984 | -52.84027 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 949e16a7-2ff2-32ec-bfc8-c6a10598bc27 | -6.08877 | -52.82507 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68a58874-5b09-388d-912a-234b48c72669 | -6.08242 | -53.40766 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f6340de6-3e69-39fd-81e8-a85918083bd5 | -6.06798 | -52.86723 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f38d5f67-0112-30e9-b8ca-360625c9b5dc | -6.01154 | -52.84704 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b31fea8e-0f47-3726-b684-bcc7bfe1c3ec | -6.0081 | -52.84663 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b83f6c6f-143e-3d91-94a0-ca3c02805f21 | -6.00539 | -53.3006 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aae614d0-06ce-3af3-bfd7-8332d4218a16 | -5.93058 | -53.74168 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6416033-cd5f-3535-bc48-781c7cae9c14 | -5.91914 | -53.43435 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 06f74bd2-81b9-3117-8e89-41b4892e78a7 | -5.91875 | -53.43086 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31d67cc2-c51e-35b3-b7ba-d2bf5199663e | -5.91813 | -53.43479 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c72dedf8-28fb-3735-babd-cd49d7371dfd | -5.91525 | -53.43029 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4418b0bb-faad-3411-9384-5272cb11cf34 | -5.914 | -53.43811 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2eab0681-21e7-3766-8af9-63d37f94e25c | -5.91339 | -53.44194 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b2ca96c9-a89d-3fea-bbd4-34ad468da296 | -5.8025 | -53.38879 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55b883f3-67f3-3afe-99ca-a3a3408f2a31 | -5.80188 | -53.39269 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4eee21b8-d387-30df-a504-f8682855c240 | -5.78912 | -53.38263 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5390a012-94e3-3b82-ab23-88ae7df8d7fa | -6.59951 | -53.07344 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 13c76a9c-22ec-30b8-a223-bbfca334ff66 | -6.59891 | -53.07718 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d3232c8-8020-309d-afdd-cf61a86501bf | -6.59608 | -53.07288 | 2024-10-10 04:44:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 528307c9-1274-38cf-a54b-f96e4415054c | -9.02314 | -54.53033 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e8117ae1-404d-37d2-ae49-c679dec245d4 | -9.02245 | -54.53441 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f4fc26d5-2bd1-3020-aab6-c2acc00edbad | -9.01094 | -54.5157 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58aa2864-8fac-3d84-b4ad-1ae245c62ffb | -8.86217 | -54.70067 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a9903d2-d429-3de4-89a2-751c6f997b49 | -8.85994 | -54.69167 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7cda8d8f-f77d-315a-b7c8-a3eb983e525e | -8.85702 | -54.68694 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e97b0ca5-04c3-3652-8b68-87154138c2e2 | -8.85477 | -54.67807 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e7a7039c-80eb-3807-bf07-f7fb148c54bc | -8.70455 | -54.84027 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5891fa1b-fcc7-30a4-b262-bc01607d2fd7 | -8.61715 | -54.59863 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ac16c2e9-7c84-3711-a42a-d807a8d32495 | -8.61647 | -54.60276 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 08328f45-ca20-3a86-b26b-6934756d7939 | -8.61579 | -54.6069 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f7f85ab6-9466-3102-ac99-30fbe41abc99 | -8.6151 | -54.61104 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eefe38c-56c7-39e7-b7f5-59d3eb29514a | -8.61493 | -54.58973 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 789b386a-be09-3438-8f02-84a7e9dd0c1b | -8.61424 | -54.59389 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ed4ad06f-ba82-3d6c-9420-5cd3dcbd0765 | -8.61356 | -54.59803 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 841b4d33-19f0-3ca9-90b7-daf879c0e3f9 | -8.61287 | -54.60216 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9eac7e1d-1897-32a9-881c-385902cddd3e | -8.61219 | -54.60629 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 29b95714-f769-309f-ae5c-3745a0c086d9 | -8.61151 | -54.61043 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0d865db3-a6a5-372b-a0f9-9086e6b2f45d | -8.61133 | -54.58913 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 569e96be-f064-3ca6-b1bd-7ed375efd1a0 | -8.61065 | -54.5933 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3aa35031-726a-39bd-a370-c3dfc44a6ea6 | -8.60996 | -54.59745 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3986e960-4bb3-3c7d-89fd-5f8f4bdbb0f8 | -8.60928 | -54.60157 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c766b23-3947-3395-976e-76844210e5fd | -8.6086 | -54.6057 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 50426aaf-54f7-3da7-b6f0-d3649d204144 | -7.91626 | -54.38865 | 2024-10-10 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cc3ba1f3-25d1-35e6-b886-ac27c9e7471d | -9.39039 | -54.74865 | 2024-10-10 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c8d6fb6c-a0ae-39b1-ad31-67472ac6528a | -9.81736 | -54.53052 | 2024-10-10 04:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2344f4a-c625-3c57-82fb-2db6543fbbad | -9.54014 | -54.80165 | 2024-10-10 04:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 17d2da52-b3e0-3b92-bd45-10e84579623f | -9.53944 | -54.80583 | 2024-10-10 04:44:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3e71097-1684-3aab-b14b-250bad0a3422 | -10.58983 | -55.07452 | 2024-10-10 04:44:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 546899ef-bc54-3410-9666-64402c0a4fdc | -10.58624 | -55.07393 | 2024-10-10 04:44:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c08af60a-940e-387e-94a5-cf5eed7789b1 | -10.58484 | -55.08228 | 2024-10-10 04:44:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2021f0bd-9800-3513-a67b-4c6a5a4c4b99 | -10.57565 | -54.93984 | 2024-10-10 04:44:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ab6e228-1aae-3ba6-a8da-480a79769ce4 | -10.55055 | -54.48471 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a90c103-21f5-37a0-8841-6953c4325525 | -10.70993 | -54.11594 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 17a8e224-5d67-3c1d-82d8-b2af62f016f7 | -10.6239 | -54.23629 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3ac2fbe4-40c6-3c85-9ead-80d90a7b0ed3 | -10.62044 | -54.23568 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e912c23d-a511-38b5-9618-25a30c0ac8de | -10.38344 | -54.18074 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee8ed6b1-84d9-3210-a012-b638aab89ba1 | -10.37998 | -54.18014 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 31510fd7-7193-324a-94bf-7e53c65569e5 | -10.37652 | -54.17956 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4894ed0-76b4-32a4-a504-73be1829e6ab | -10.34609 | -53.74683 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 121bfb7c-3d07-3ffc-9d94-ac36cc774db5 | -10.34548 | -53.75055 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8aa6be18-ef1d-3c80-992b-16f7a339d686 | -10.33218 | -53.76749 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d5802e8-e429-3d9f-8eec-3582dd306555 | -10.3103 | -53.70751 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 89439412-bede-3811-afe7-669ef767f3ac | -10.3069 | -53.70693 | 2024-10-10 04:44:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| acb22340-a9bd-3bdc-9a27-c842510754b8 | -10.22922 | -54.27273 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c716a1e6-ee6f-3dfa-b263-40c738c9721e | -10.22574 | -54.27212 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 29ce9528-c931-34a9-97ec-a8cfb64ece85 | -10.22066 | -54.30329 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddd5c436-8c6b-3bdd-9422-ea4226b9d52a | -10.22003 | -54.3072 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d78e897-32e7-3d17-a9a4-e9b2b9c3db02 | -10.21718 | -54.30268 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ed050d9-92f6-3a39-b7e4-7020610cc569 | -10.21654 | -54.30659 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4f64776e-6ad3-3efb-8b37-58c0121aea53 | -10.21306 | -54.30599 | 2024-10-10 04:44:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 299bd95e-2db9-3740-a7f3-aae03e15237b | -11.2355 | -54.18599 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55ccb714-c849-31cc-810e-6e842180bf33 | -11.23259 | -54.18583 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b37fa39-522a-39bc-bcb3-4bb174e3faa7 | -11.14039 | -54.01921 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f1f6226-f53a-3d89-9676-29cf091fef87 | -11.13916 | -54.02678 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ef8e1d8-a11c-3f35-8d60-1565edaff316 | -11.13758 | -54.01485 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f3f34887-4da5-3769-b836-164c27a5079d | -11.13697 | -54.01864 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4db3c15d-77fa-37f9-bc53-b516cc61cdae | -11.13635 | -54.02242 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a0f727b-24bf-352f-8ea5-0173efc267af | -11.13416 | -54.01428 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ea660512-0903-390c-ba66-cab60a7e7153 | -11.13355 | -54.01806 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d720b55-92fc-3e5c-90b7-a23db97f8637 | -11.13293 | -54.02184 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d10f6b05-e1d4-3da8-8960-66bd2bc7aec0 | -11.13258 | -54.00238 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 875723c7-719a-3211-b484-0099c9babae2 | -11.13232 | -54.02563 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 531d6ff2-6307-385b-b77d-e058e310dc4e | -11.13197 | -54.00615 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3cad48b-1019-3a6d-8be6-e645b74e60e1 | -11.13171 | -54.0294 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d65d2fe-8b61-3194-add5-ea42afe889c4 | -11.12951 | -54.02127 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1575d726-8d18-34e3-b971-9d56598e71b7 | -11.1289 | -54.02505 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 03475434-969d-3b6d-91da-8fdbb99b156d | -11.11601 | -54.29211 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 49961e7c-2251-3e3b-a548-eff14d09b13a | -11.11256 | -54.29154 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 82b779cf-ac6a-3c05-a88b-995caccf8233 | -11.11192 | -54.29538 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07b1cf67-c511-364a-96f0-59bc1e939502 | -11.09626 | -54.03122 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe235c05-d419-3deb-8350-73aea2ff6dd2 | -11.09284 | -54.03064 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b3dfe523-21cd-340c-89ef-a3bd212bd40e | -10.99236 | -54.26049 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fc19b22-ec32-34d8-a0ed-4904660b1187 | -10.97844 | -54.00001 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 92f3eeb2-8c3e-3a11-838b-3b621b36d91e | -10.97782 | -54.00378 | 2024-10-10 04:44:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a649f6a7-f206-3cf1-b276-6a7fc150311d | -11.28937 | -54.57911 | 2024-10-10 04:44:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README111.md)
