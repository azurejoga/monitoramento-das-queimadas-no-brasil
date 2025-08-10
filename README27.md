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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d6d39e2-002d-31c5-b8a2-4d00912d6e77 | -9.55647 | -62.72062 | 2025-08-10 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 096a1ddc-8e17-35ac-9e1c-ed6eece3d9c3 | -8.68766 | -64.2226 | 2025-08-10 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2dc1e2a4-3b01-37ff-af9a-bcba9b82be0b | -9.20496 | -59.67463 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 939ecb50-ec8c-3a04-8b1e-2f2a65d78ae0 | -8.92723 | -60.75483 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd419f15-9abc-3c99-baab-433277a598ce | -9.37042 | -61.53417 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d0a03e00-de74-303b-8164-33c94cc9246c | -9.37222 | -61.52177 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0f5db48f-bc2c-3e60-be80-a67c1bbac0cf | -9.85523 | -65.21334 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a532e60-93bd-3c7c-b591-8c5512f7b4c5 | -8.93053 | -60.73261 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c47f6de3-bb15-3e51-a02a-2134574c3bd1 | -10.04391 | -64.90016 | 2025-08-10 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b753be4-d7c4-32a3-992e-46f08f4c5640 | -10.04722 | -64.90069 | 2025-08-10 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6e662d8d-b4b1-3c95-8e86-54f109b6660d | -9.8243 | -63.01466 | 2025-08-10 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b1ed7aa1-7031-33c0-8f79-76e042ce66ae | -8.93532 | -60.75151 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 2b9545a0-1f70-32a4-9ed4-c398d41f3d91 | -8.93253 | -60.75864 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 422e65c2-1760-3d9d-8d9d-cf547609ffcf | -11.71503 | -51.62293 | 2025-08-10 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9c9103e8-bb24-31e9-a64b-2c88670a1a2f | -8.92921 | -60.7415 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70c93b0d-e45c-3b45-9cdc-082f1f7905cd | -9.67153 | -62.88654 | 2025-08-10 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 570aafd2-8816-39e0-90ad-2626749737e6 | -9.03061 | -59.75055 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 626e9a38-0825-32c2-90cb-a1fc42e52e27 | -9.3734 | -61.53886 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 045f6a3f-20ea-3585-9bd5-a93df9e4ad4d | -8.93095 | -60.75539 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5ba7d087-d284-341b-ac83-8ea60bd90201 | -16.30154 | -52.92218 | 2025-08-10 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06abaa94-c660-3ad6-bb0f-4f5eb6e80b7d | -9.71459 | -61.2954 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d0bab4b-9680-32ec-b777-40d1941e19af | -9.36854 | -61.53131 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 43ba319d-7232-39d2-a20b-d28aebfca3a3 | -8.93688 | -60.75477 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 18f3e63c-2212-3277-ad0e-6bd0d0699c8f | -9.36982 | -61.53832 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b688c0bf-2134-3f4e-a1d5-608f494311b6 | -9.36978 | -61.52306 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69470447-1cd2-3212-a9b0-e9ed6a4c3be5 | -8.93293 | -60.74207 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f9219710-955b-346a-a465-d54175885612 | -8.92352 | -60.75427 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10e545a2-55f2-3b8f-9fe5-dcc45ac9c4eb | -9.19628 | -59.67866 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d3d9611f-0dcf-3381-8df6-8c8b176c0dc6 | -9.37102 | -61.53004 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 92900b1f-dd25-3489-bce0-6b4bf85f4937 | -8.92747 | -60.7276 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 31ece0f3-0463-319c-a54f-465c1acefff7 | -8.93425 | -60.73315 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 859a4839-d051-3a99-9620-258105d462c4 | -16.30779 | -52.92863 | 2025-08-10 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 37e2783d-8cd5-3ee3-978a-a97ac50b2f38 | -9.19782 | -59.67774 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c5aca36-e425-356a-b23f-a85a3a67e4db | -8.9397 | -60.74762 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bd958d06-e1cb-3b44-82de-69a4876f1f4c | -8.93664 | -60.74262 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 397a4c41-ca78-395d-bba3-5250ae89e497 | -8.9255 | -60.74094 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95f1aa25-76ed-3977-96c2-ae54b3d0da43 | -8.92615 | -60.7365 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f141e59b-7190-3926-a9d4-e939c8fcd1b1 | -8.93878 | -60.74141 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 7ffdb44c-10a1-36c2-a9ab-8314af62621f | -10.0876 | -68.9659 | 2025-08-10 05:38:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4e273330-3980-3924-ae95-2d17f60dc20c | -11.7157 | -51.61656 | 2025-08-10 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 77e14e5e-869c-347f-9a40-94ebcf2d6263 | -9.85192 | -65.21281 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d3f221a-d7e9-3784-b693-43312916fca5 | -8.92789 | -60.75039 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5eb900a2-d062-323e-ab48-a6c731a4e126 | -8.93226 | -60.74651 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 3070a2ab-222a-39f0-bb17-640627a084c1 | -9.3752 | -61.52646 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 934846aa-8511-3748-a333-abbfbc1d78b4 | -8.9091 | -60.54007 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 121090d1-2244-3402-ad6e-cd39a16c43dc | -8.93731 | -60.73816 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3217ed95-05a1-3bff-8208-870018af5d27 | -16.30104 | -52.92766 | 2025-08-10 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b00afbd2-f028-3821-9563-1db0fc907323 | -9.3746 | -61.53059 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 038c9322-f4cb-35df-b51d-3e771419cb5c | -9.36916 | -61.52718 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b39f9061-31d6-3a4f-ba5f-25731201a196 | -9.70541 | -61.30715 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ddae1688-df2b-3118-9de9-a0d4e1e26d91 | -9.36803 | -61.52536 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ba212927-547b-3760-a473-cb2953996697 | -8.92418 | -60.74983 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5d9257-bf5d-3bbc-926c-07931ab3ab96 | -11.71562 | -51.62201 | 2025-08-10 05:38:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 38ed48c0-6a1b-3993-9b31-bff7c0380dbe | -16.30613 | -52.9241 | 2025-08-10 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82c15024-0004-3fb2-889b-4797a4a208e1 | -9.374 | -61.53473 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 8c0132a6-a451-3548-a422-7bfab605766a | -9.70604 | -61.30288 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2dc544fd-c2b7-35e7-bb40-0dfd1537b545 | -8.57277 | -62.64492 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0778efb1-ae40-30ae-b465-2ad62cd6f1e0 | -9.3758 | -61.52232 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| e5f8c9c3-fa1d-3fcb-8756-599085b9bbea | -8.92987 | -60.73706 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9d5e97c3-76b1-3d17-91cb-b55a1eb47ca6 | -11.10281 | -59.91113 | 2025-08-10 05:38:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0bb4993-2109-30cc-8403-68734f2710eb | -9.55703 | -62.71689 | 2025-08-10 05:38:00 | NOAA-21 | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 32b064c2-371f-3dfd-a51b-4f9dafce2e61 | -8.93359 | -60.73761 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e4c982a-25ff-3439-92f9-032469517380 | -9.20255 | -59.67314 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c59a7e29-2f49-3b35-959b-59ef02bbeefd | -8.90844 | -60.54461 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 82fbf2ef-9ece-3737-8e44-2df9e0f7851d | -8.90778 | -60.54917 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 98045381-cf69-3466-ae9f-877506e84dd3 | -8.93598 | -60.74707 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| e3a36a4c-40b5-33d9-8234-669ff0db2f49 | -9.83163 | -63.01201 | 2025-08-10 05:38:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4103665-5e85-3f0f-9ddb-c5279a6bb813 | -9.20169 | -59.66888 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| be037218-b973-35f5-b8f7-d7cd7a5053e4 | -8.95134 | -64.34296 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ff393d09-2a81-3dcc-84ef-7662405358b7 | -9.37162 | -61.52591 | 2025-08-10 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 1c6f5005-46e2-38cb-b814-795a1a8cca26 | -8.57561 | -62.64914 | 2025-08-10 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f4f6fbdc-3cc5-3ea1-87d6-a32b646201a3 | -16.29938 | -52.9231 | 2025-08-10 05:38:00 | NOAA-21 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 09150a1a-e6a5-3d54-bbef-47b599e0c6c0 | -9.362 | -61.5324 | 2025-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 5bced75e-adfd-3a3b-9843-ce52cf6fc3c2 | -8.9215 | -60.7297 | 2025-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 99c8aa0d-c1bf-3fcc-bf23-5010705e622d | -8.9401 | -60.7288 | 2025-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 37a69f36-9eb1-38c4-824a-474ad1140606 | -9.3806 | -61.5315 | 2025-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 127.9 |
| 6a7f2440-3ccf-3ec9-b517-9bf26efebe00 | -8.9213 | -60.7489 | 2025-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 3e1635cf-ee52-3fee-a3d4-ee429c37becb | -8.9399 | -60.7481 | 2025-08-10 05:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 93.0 |
| 453c16f3-3d76-3145-9146-2ccfdf8dd6ae | -8.9399 | -60.7481 | 2025-08-10 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.1 |
| a2725fff-7bbc-34fd-baee-bc73c6597ab5 | -9.3806 | -61.5315 | 2025-08-10 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 5ee53766-cd23-30f9-8717-9faedb4d14b8 | -9.362 | -61.5324 | 2025-08-10 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 85.6 |
| f73a57cc-458e-3dfa-9990-833538e03ea9 | -9.3806 | -61.5315 | 2025-08-10 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 94.0 |
| cb4a1a63-8117-3fa7-b3d8-ce0a643ad891 | -9.362 | -61.5324 | 2025-08-10 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 99845648-db32-3133-b4f4-a4a676ba5521 | -8.9399 | -60.7481 | 2025-08-10 06:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 8ffdda45-4d9e-3088-8ff0-17ab6a950e57 | -7.40181 | -60.00475 | 2025-08-10 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fd0d0667-3f7b-355c-871e-86a66d325a56 | -7.39719 | -59.99568 | 2025-08-10 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb914bed-a0ef-33b2-9547-9e51040ca5eb | -5.34714 | -55.90718 | 2025-08-10 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d2d81099-6876-318c-95f2-40b079af1f5f | -7.40236 | -60.00075 | 2025-08-10 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eef08583-4a64-31db-b16c-a64e2f6a1c66 | -7.4029 | -59.99671 | 2025-08-10 06:01:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 220bb8e2-31cd-37d9-8da5-56daf6d49359 | -5.33992 | -55.90643 | 2025-08-10 06:01:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3f8df9c-6f22-3e80-b910-e84cd938a087 | -8.9292 | -60.753 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7a71393-424d-3116-af54-baecf317ad1b | -8.93627 | -60.74271 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 025f4d17-2fc9-3f74-90eb-f91d07a3330f | -9.36744 | -61.52648 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94875a0c-94d7-3198-a59b-2672371daeff | -9.37683 | -61.52399 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d92051c1-62e6-36c0-adfd-b6504af3201d | -9.37367 | -61.5206 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| dae01f11-01a8-39e9-9ae4-3e889a37e834 | -8.93478 | -60.75377 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a05cad2-0a90-3488-9929-2fdeab3d1dd7 | -9.70647 | -61.30286 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b663920a-b047-3610-ac10-e65a4a3c9f01 | -8.93192 | -60.75932 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cddce781-c91f-3116-a80a-ec3cc5060e3c | -9.37764 | -61.53131 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7fdb7ccc-df2d-31e9-9b3d-ccac13a34bb6 | -8.93429 | -60.75739 | 2025-08-10 06:03:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README28.md)
