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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7e251d50-4593-3ecf-97e9-e0718f272f22 | -0.96175 | -54.06068 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 060a4d20-4267-3357-8368-83e9776b1d80 | -0.95443 | -53.39658 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf2c65d0-3302-375d-9426-6d4bb262fc9c | -0.94963 | -54.09291 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 35c8a859-d3bd-31e8-b3a9-c466bae763ab | -0.94907 | -54.09653 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ba6ebc4-511d-376f-a20e-0cb44d152e9b | -0.94786 | -54.12651 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f3ab15a-2722-35a4-8fb2-7b96957c35a4 | -0.9462 | -54.09235 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0dfc916-1c0a-38c8-8fe7-654bfd4d0a5d | -0.9422 | -54.09542 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 246cb432-bbd2-3820-b73d-67ad2d62c673 | -0.92454 | -53.60908 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7ced900d-f626-3490-8f02-55b059faae45 | -0.92394 | -53.61289 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 84b17b2c-cc85-37d2-a987-83117b8c571f | -0.92334 | -53.61673 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 92c157e6-4a2f-36cc-8f9e-5bf39ecee45f | -0.92107 | -53.6084 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b09a5a4f-fc69-3852-a314-8bbe7d035b23 | -0.92046 | -53.61224 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e063ecbd-304d-3ff6-bac9-48d90aa4ed1d | -0.91758 | -53.60778 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0e3d6f93-d10e-38d1-93c6-2e64a883c59b | -0.91697 | -53.61164 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 794d0c8e-4356-34cf-9b24-a3130535ef89 | -0.91409 | -53.60717 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59173815-1133-3965-b3b1-84f0999a89ae | -0.91348 | -53.61105 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0bf88e5e-247c-32e0-9e02-b2f0b822858e | -0.90998 | -53.61048 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c51d5ec8-818d-3f05-9cbe-39928b1c12e5 | -0.90649 | -53.60992 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9494dbe6-8bd2-39a8-8014-a6a9ab661c4e | -0.89339 | -53.323 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1ee9d42d-e42b-3595-a849-ad807e7b33ee | -0.89274 | -53.32724 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9efa24a-2174-3d87-9503-2656dfd76d31 | -0.8619 | -53.68915 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c0de690b-7dcc-3436-b55f-15b2e57464ec | -0.85842 | -53.68861 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9925b06-943c-3b7f-8313-79af5412efb9 | -0.81047 | -53.67056 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4633edd-aacf-3bc2-a4b0-d3ea5f80e090 | -0.80129 | -53.66084 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 167031f2-fa82-3e1c-b6fc-6c898ee9ef0f | -1.06706 | -54.16703 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a102a815-e450-3a31-abc1-f65ae6f7c010 | -1.05525 | -54.10815 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b1ebcb14-9943-3479-9b67-e09a745bd2f8 | -1.05181 | -54.10762 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ae5cae7-33ec-3cc4-a459-5f7a421754a1 | -1.04971 | -53.34126 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7db18f6-0ef8-3c09-b6df-d4fc41f4be4b | -1.04889 | -54.12617 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0b44706a-e7d5-3256-8ed0-715f2612ea0d | -1.04656 | -54.141 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f363616a-5178-32ef-a321-d853226e9b23 | -1.04615 | -53.34074 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c1257868-d7f2-3e65-ac93-2347fb8dc436 | -1.04598 | -54.14471 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3e32828b-dec3-376a-997d-1a8f9fb3eedf | -1.04546 | -54.12563 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33a2a327-6942-3f05-97d7-14f8972b5111 | -1.03965 | -53.86858 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2310a97d-e71a-3be5-873b-7f3868c4d6c7 | -1.03907 | -53.87233 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 42bf87d0-4711-35fe-a8d4-f4d704dd76fe | -1.03656 | -53.97962 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5b76b04e-f8b6-3e98-964b-8573f24666fe | -1.03619 | -53.86805 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d6c620a1-4443-3e7f-a5ae-fdfbfa56f58d | -1.03597 | -53.98343 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4eda469e-4273-3462-8027-254eb455da05 | -1.0356 | -53.87185 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cb59a4bc-bf89-3b88-9f12-d17bc7d8143c | -1.03333 | -53.86357 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94e5c657-2d60-37a0-878a-3e29ebb73c33 | -1.0331 | -53.9791 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 47540bdb-27c1-345c-9b18-d924ac623ed4 | -1.03273 | -53.86746 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2d7f177-5974-33e7-ac10-1c06af1b1212 | -1.03252 | -53.98289 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ddf360df-2e23-3a83-baf0-05f189dd7b89 | -1.03213 | -53.87135 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 595d55cd-dcdd-32cc-91ab-69f0cd3819c1 | -1.03154 | -53.87514 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f092ac0-071b-3dce-b3bc-ec23c676c19b | -1.03023 | -53.97484 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3432fa9a-6643-3079-ba01-3532579f32e8 | -1.02988 | -53.8629 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8427f355-fe8d-38dd-8003-4509ae9fb047 | -1.02965 | -53.97858 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 476db62f-0753-3bdf-a3f3-160710749f58 | -1.02927 | -53.86686 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d81b98c8-6ac0-3c5e-9ae9-287d72351c5c | -1.02866 | -53.87081 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b3698cb-7144-35e8-86c1-b99b83286475 | -1.02823 | -53.61616 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bbd4c9f-1e38-3cfb-8ded-55398747d04e | -1.02807 | -53.87463 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ec7c101d-3ef4-36bb-bc8c-b241b75d2fee | -1.02595 | -53.60787 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc70138d-1bea-34a5-b27d-9a1ec6462528 | -1.02581 | -53.8663 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56ac9481-a26d-3ff2-b1cc-cf58b95d5b5e | -1.02534 | -53.61175 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 568fbd2f-3a37-36e1-a46d-a75e63e65a59 | -1.02474 | -53.61558 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78a1f807-5e64-3d02-8677-6626296e3153 | -1.02245 | -53.60732 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e5db108-1c7c-3ec7-85ce-7c62cc6c4a3c | -1.02077 | -53.86645 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b952782-1d78-3490-82bc-a4138c6df381 | -1.01987 | -53.64653 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15310853-3176-3048-aa81-4aebf460eb00 | -1.01925 | -53.65047 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0559555b-70cc-3053-8327-d848cf0303ed | -1.01863 | -53.6544 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f9ac55c3-9a9a-323f-878a-b5056f44cc15 | -1.0173 | -53.86595 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49b1a6fa-071f-36d7-8f17-9138e7973c41 | -1.01698 | -53.64212 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8a77ab0-a4a4-3bc6-b2b3-99c4ec08b080 | -1.01636 | -53.64604 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7b5d76d5-ebf6-312a-bd7b-6eb8d23aa7a0 | -1.01574 | -53.64998 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 734fb9a0-f146-3130-b3a9-99bd89201901 | -1.01347 | -53.64164 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c43da09b-49cd-309c-8254-8080861bbb36 | -1.01286 | -53.64555 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9298a6bd-350e-3795-9584-d53097d69413 | -1.01224 | -53.6495 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e975d9c7-ed66-35e6-894a-d1c8380f52ed | -1.01162 | -53.65344 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a3706ab6-4043-398f-a81c-6ad9f7e25e4a | -1.00996 | -53.64114 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 935ab9a3-56b2-3756-bdcb-3086026b8f00 | -1.00935 | -53.64508 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e926360c-d939-3d6b-8564-7cf498cb4c0d | -1.00812 | -53.65292 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6aec2649-92de-330e-925f-9973b1f3a2fb | -1.00753 | -53.47244 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2e48ae0a-3880-3964-a39e-05ef4ada5a41 | -1.00584 | -53.6446 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df7d0c4c-2d21-3e6a-b8f7-9c0c20b2b84b | -1.00342 | -53.8639 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 53501492-9b6f-3cb6-9e14-e67071be4a28 | -0.99997 | -53.86324 | 2024-11-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9b0c7e98-8348-3b44-8ae5-e2c49531451d | -0.99788 | -54.13759 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eb09c721-dac8-3aa6-a11b-9efb6d23572e | -0.99445 | -54.13705 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aee12b84-5f2d-3bb0-b1cf-7f21d04312f7 | -0.99387 | -54.14077 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e34cab3e-5285-3112-8700-8e56c71e5384 | -0.99286 | -54.04233 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d708be2b-5ff5-3060-a3a3-c5c1ba89630d | -0.99167 | -54.04986 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f027d123-d12b-359d-9f35-df1ebfd2c5ca | -0.99001 | -54.03807 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a9690fbc-ae23-3303-9c23-e95f976feb2d | -0.98941 | -54.04182 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 379e0e15-85c8-3545-ab95-4cd1500bb4d5 | -0.98882 | -54.04557 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8a1399d-fb59-31b4-ba46-21369a1a7db2 | -0.98822 | -54.04935 | 2024-11-03 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d640bd61-a666-358d-a533-1e21098760c2 | -0.97796 | -53.3394 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2bb00d39-c081-3d63-9215-eebb52864ebf | -1.19588 | -53.55955 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0dac8986-5be6-31b8-a331-253607003190 | -1.19527 | -53.56345 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c3887bb2-4d05-3403-89e1-f239d21eda2d | -1.19175 | -53.56295 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2c8bb36-28d0-390c-9d26-e4ee21c3a523 | -1.13472 | -53.41824 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 05dab56c-cf18-3615-9aac-d4c84f58c930 | -1.13118 | -53.41769 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d195efe9-a7a6-3d05-9664-c3f32a8a6d3c | -1.11086 | -53.36151 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bcba81bb-0893-39a4-88d3-1fb4e56ba310 | -1.11024 | -53.36548 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 9965cf3b-caac-391f-8b56-959f8c2a86d2 | -1.10976 | -53.34504 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 97ca3754-fafe-3d0d-9e11-25f4b62e823f | -1.10967 | -53.32998 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b1c751ff-8fe6-3422-9df3-8cbbbfd67a50 | -1.10963 | -53.36946 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 3dc7087a-3dcd-350c-9db7-e4e842b80aff | -1.10914 | -53.34904 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0cf88694-3c5f-36f8-aa78-c7cd58654753 | -1.10901 | -53.37346 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9f43fee7-8c7c-3558-87a3-fc6b2c247bbf | -1.10867 | -53.32851 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 59faefb5-a012-3e1a-95be-8a0a191ce39d | -1.10853 | -53.35304 | 2024-11-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README67.md)
