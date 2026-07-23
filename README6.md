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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 23d29ed8-c0b5-350f-82a1-1a6a05355f76 | -11.9069 | -50.3815 | 2026-07-23 00:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| f95f2b64-18f6-394f-9ea7-ecb30a9a023d | -11.7738 | -50.3756 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 44433207-5664-3592-b1bf-9ce02c90403c | -11.8066 | -47.1082 | 2026-07-23 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| ecc06d0c-1eb4-39d8-88ce-6813895e8d4d | -11.7875 | -47.1108 | 2026-07-23 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 517b14bc-c91f-3d00-a272-e3b458fc69b2 | -11.9835 | -50.351 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 29d1bb6e-5017-3d05-ab6e-6194dd3256c2 | -12.0214 | -50.3679 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.8 |
| 8ef36cf2-ddf0-3459-b0f6-34fa03d4ba12 | -11.9832 | -50.3725 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| 2238497e-e7f3-322a-b6b1-c7ddff2530b5 | -11.8879 | -50.3837 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 5313b8cf-fca7-3802-8251-db84d80d79e1 | -12.0023 | -50.3702 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| a09e64bb-05ee-3925-b8f9-1abad7128415 | -11.6792 | -50.3437 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| a9576c64-e906-34da-a0cb-0fa4ae61ffc8 | -11.9069 | -50.3815 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.7 |
| f5c561fd-9b8f-38e1-bb41-e28d2f04b5bb | -11.9454 | -50.3555 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 823e7b47-a415-3040-aa8b-7ec76463a6ec | -11.926 | -50.3792 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 145d662d-0b58-3ca2-9111-7f62d7874eb5 | -11.6983 | -50.3415 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| cb61b156-66bc-3071-b770-abf4a1c1cd43 | -18.7804 | -51.2453 | 2026-07-23 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 93d867a4-f66a-352f-aa95-0737a849f91a | -11.6602 | -50.3459 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 43a61d61-879d-3fb5-90c3-9b1fc84e055e | -18.8004 | -51.2417 | 2026-07-23 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 196.5 |
| 976bcd36-243a-3d26-ae68-efac7456736a | -11.9645 | -50.3532 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| bcd4859d-d81f-3f38-a44b-56edbb179b4d | -11.698 | -50.3629 | 2026-07-23 01:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 7a5b27e5-6165-3eb4-93f2-3e771b9978e4 | -18.7999 | -51.2638 | 2026-07-23 01:00:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 82.5 |
| a672edcc-2d83-3a37-9ac9-6f4f93e0ec40 | -11.7879 | -47.0884 | 2026-07-23 01:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 113.4 |
| 8b0bee58-7c94-3191-8404-75567d3a6332 | -18.7999 | -51.2638 | 2026-07-23 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 78.7 |
| 0a50d3af-e74f-365a-b3fd-88e477917ac2 | -11.7683 | -47.1134 | 2026-07-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| eb68745c-1cd0-3dbb-a8e3-d8f4f90ffa6b | -11.7687 | -47.0909 | 2026-07-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 51.1 |
| 19089a73-d3c9-3560-b385-47673571eb39 | -11.698 | -50.3629 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 102.7 |
| 08aed962-9b3d-3ac2-a375-f1f0cf436702 | -18.7804 | -51.2453 | 2026-07-23 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 120.9 |
| 195bf089-f1af-38b3-8b49-2676a6395d28 | -11.6789 | -50.3651 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| ea0021b4-2640-39ea-8529-f6b6e865cdb5 | -11.6792 | -50.3437 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 113.7 |
| b72bfa4e-8b5f-3da7-9834-b422cb1ef030 | -11.807 | -47.0858 | 2026-07-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 68255d45-281f-3edf-9e04-56dd38172b8b | -11.8066 | -47.1082 | 2026-07-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 430e7b7e-aab5-33d4-932a-921767b59e67 | -11.6983 | -50.3415 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 294ccaf5-57eb-3438-85a6-e8a2f5277929 | -18.8009 | -51.2196 | 2026-07-23 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 75.9 |
| eed283cc-8370-3701-bf05-d6ff48a9329c | -11.7875 | -47.1108 | 2026-07-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 197.2 |
| a2c7723b-2d58-3f3a-b1e7-5f20c03f6614 | -12.0214 | -50.3679 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 07e1e5be-ae12-36a6-a9df-08a73ac8535f | -11.7929 | -50.3734 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 56.2 |
| d6ebd4e6-d800-3793-81be-e2313776cdd0 | -18.8004 | -51.2417 | 2026-07-23 01:10:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 202.9 |
| 9917545f-330a-338d-90aa-27ac4e08922f | -11.7879 | -47.0884 | 2026-07-23 01:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 190.4 |
| c9d39bae-857e-3115-be79-a78040038dcb | -11.6602 | -50.3459 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 80.8 |
| fc49e0de-c322-3403-9d6c-9d464e5805d9 | -11.7738 | -50.3756 | 2026-07-23 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.6 |
| a40f942e-63e6-3354-b9ea-b84f0f36f534 | -11.9069 | -50.3815 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| c67100cc-4509-39e1-ad32-995b2c6763b8 | -18.7804 | -51.2453 | 2026-07-23 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.2 |
| eda0437d-68e5-3eaf-831c-1d558cc8e386 | -11.6983 | -50.3415 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 323c9555-7e49-34d1-980d-0b6990f60f82 | -11.6602 | -50.3459 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 663b232f-c5f4-3585-8841-707bcbc81ca0 | -11.7875 | -47.1108 | 2026-07-23 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 126.2 |
| c0616f68-da36-3e21-8d39-2667da378a67 | -11.7879 | -47.0884 | 2026-07-23 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 397aca1d-47c6-3d13-a743-7451a8c5e668 | -11.6792 | -50.3437 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.0 |
| bc9ca61f-54d0-3fd6-a5a6-86f773ae89c0 | -11.8066 | -47.1082 | 2026-07-23 01:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| b137d8f5-88be-3cf7-8bc9-02d73341ad07 | -11.7738 | -50.3756 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 03781a23-3086-377a-96ab-e5d689b96ba2 | -11.6789 | -50.3651 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| c6b6d64a-31b3-3db7-a791-3fd84dd275f7 | -18.8009 | -51.2196 | 2026-07-23 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 66180aa2-fdaf-34b9-9cc4-1ce32feba427 | -11.698 | -50.3629 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 106.1 |
| f1de7846-1d62-39ba-b582-3cbcbc758b62 | -18.8004 | -51.2417 | 2026-07-23 01:20:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 169.3 |
| 0ffa4cb8-9e6b-3ec9-a1d1-b407019482e4 | -11.8879 | -50.3837 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 531d5d1b-d3cc-3ac1-9799-8d13516f8adc | -11.926 | -50.3792 | 2026-07-23 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1d56a0bf-9da3-3a84-80a2-e5d022572612 | -11.9835 | -50.351 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| 8727fbad-84bb-33f8-9233-c0ce4cb11d33 | -11.7879 | -47.0884 | 2026-07-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 147.6 |
| 0f9e60e1-fcda-3aa2-919d-27ec0479c2c1 | -11.698 | -50.3629 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.2 |
| aa60fb81-a327-3670-83be-fc3610acca18 | -11.8066 | -47.1082 | 2026-07-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 473a435d-2446-34c2-a44d-393998bd1b37 | -12.0214 | -50.3679 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| 5ab86fcc-4e4e-39d4-98fe-f0f7f8ea88de | -11.9832 | -50.3725 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.9 |
| ab6a5a6c-3cd1-3073-a999-aaa6740657a0 | -11.9645 | -50.3532 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| ad84de09-9675-360e-83c2-110523bf2a5c | -11.9641 | -50.3747 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 4d6c7a2a-ce5c-3590-8422-ca74ad92cf30 | -11.7683 | -47.1134 | 2026-07-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| efc5ad44-f7ed-30b2-bb54-8f45991c8c58 | -18.7804 | -51.2453 | 2026-07-23 01:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 73.6 |
| da3241fe-b65e-33aa-90bd-14a3ef75933b | -11.8879 | -50.3837 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.2 |
| dc98b8f8-1dda-3e92-9142-d9252b9600b4 | -11.807 | -47.0858 | 2026-07-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| b7dfbc2f-a4c9-3359-9849-2e15cf53714b | -11.7738 | -50.3756 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 760ea857-9d51-3a8e-85ea-16fcbf8515c1 | -18.8004 | -51.2417 | 2026-07-23 01:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 214.7 |
| d41686bd-a6e7-381d-8c4f-8ec2c8ce30dd | -11.7687 | -47.0909 | 2026-07-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| a3bc8bdb-589d-353a-826c-26cbcc4b03b2 | -11.6792 | -50.3437 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 117.4 |
| de45594e-80e1-365f-80b2-449e85b9c776 | -11.7875 | -47.1108 | 2026-07-23 01:30:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 210.5 |
| 56121fbd-8335-38f5-ab14-5a27c719dbbc | -11.9069 | -50.3815 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| 107f9e6c-aaa8-3c72-9421-8568d7ca4215 | -11.926 | -50.3792 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 60c239aa-95bd-3f2d-b262-9d4d76060eb3 | -18.8009 | -51.2196 | 2026-07-23 01:30:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 68.4 |
| f46c28e6-6db7-3726-815f-8811b577a6ff | -12.0023 | -50.3702 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 4308367a-aaac-379a-9a20-b61371d248ff | -11.6602 | -50.3459 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| dd185c22-a295-31bf-9b8d-e0723ed5d367 | -11.6789 | -50.3651 | 2026-07-23 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| da259a35-589c-3c77-9ef8-c9242d6d5248 | -11.6792 | -50.3437 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 03574882-5b5e-3662-8d9a-02c9ea980da0 | -11.9069 | -50.3815 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 18101a9b-fa2e-302c-b7a2-1b7e16ec9ecd | -12.0214 | -50.3679 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 991d9bcd-d00c-36c1-b8a4-20de7ba18099 | -18.8004 | -51.2417 | 2026-07-23 01:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 239.9 |
| e3dd17e0-30e1-36cc-ae1e-daff4d7d2596 | -11.9835 | -50.351 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 87dd5b27-2a19-30ac-a9ea-e6ac8e7ee3dc | -11.7875 | -47.1108 | 2026-07-23 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 187.7 |
| e6658c34-a460-3263-83d4-b4be18409a9c | -11.7879 | -47.0884 | 2026-07-23 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 184.5 |
| e221274f-2696-3d32-9906-007276c84c8e | -11.6602 | -50.3459 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| dc949096-a8a1-360b-9df7-218a68ecb619 | -18.7804 | -51.2453 | 2026-07-23 01:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 79a82219-78f4-3546-b7d6-bfb7156921d9 | -11.717 | -50.3607 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.3 |
| 372e19a7-6f4c-3485-8bec-365eaa724d33 | -18.8009 | -51.2196 | 2026-07-23 01:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 103.8 |
| ea31e043-c84f-3801-a353-5a193754920f | -11.6789 | -50.3651 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 0a953549-14e5-382b-9cdb-732ed5776876 | -11.926 | -50.3792 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 232ea6c4-e6da-3987-bdbc-b476890cbdaa | -11.8066 | -47.1082 | 2026-07-23 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e4c00811-34cc-3c17-9866-7f681184df36 | -11.9832 | -50.3725 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.3 |
| ad8674a2-f15f-388f-acb0-b87a4d0a5cac | -18.7999 | -51.2638 | 2026-07-23 01:40:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 69.6 |
| 00cc0212-d16d-3521-b23e-81687fb6c6e3 | -11.9645 | -50.3532 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| c3b5d910-8444-3a2e-83f7-2519c378bb44 | -11.698 | -50.3629 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 107.0 |
| 3c2c779b-517e-33b6-9aba-e2cae6354c6e | -11.807 | -47.0858 | 2026-07-23 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f9d1a141-37aa-3edb-ab6e-43b96a332367 | -12.0023 | -50.3702 | 2026-07-23 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 5f79f325-8f4f-37d6-81a8-856140634815 | -11.698 | -50.3629 | 2026-07-23 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 733df28e-a0fd-39a7-b75f-528e4591da82 | -18.7804 | -51.2453 | 2026-07-23 01:50:00 | GOES-19 | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 1378e730-800c-37de-81b8-dff7fac08ee6 | -11.8066 | -47.1082 | 2026-07-23 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 71.5 |


[Clique aqui para ver as próximas entradas](README7.md)
