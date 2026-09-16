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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c2a89838-a9db-3fad-9868-55b5da501501 | -7.61224 | -67.25594 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7de0181-4762-3fec-90e2-fef564a37781 | -9.5087 | -59.50261 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fe4d8bc-a4e6-3c4d-bdba-cb61f056035c | -2.70673 | -57.61231 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ddef07d4-c25d-3e94-8bb3-c390dd1a0896 | -10.1373 | -61.18325 | 2026-09-16 05:55:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07e8b577-323b-36bb-8517-10640d28c09e | -7.05553 | -59.22672 | 2026-09-16 05:55:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b5ac780-afff-3c46-bda6-9a0a41fd1006 | -2.7072 | -57.60923 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d1e0b02-a751-37f7-ab65-b9548505bffb | -8.6505 | -66.58853 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 57772add-4544-30d0-b7ef-9905ac3e74a9 | -8.37376 | -54.72512 | 2026-09-16 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6ada249d-c5ea-322b-ba54-01119bab921d | -9.05986 | -65.92966 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| be6f0276-05eb-381c-8db1-c735260f5d02 | -13.37355 | -57.02541 | 2026-09-16 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4bed3f8-167e-3e5a-8971-f6189cd34649 | -9.78061 | -62.16102 | 2026-09-16 05:55:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd8bd578-4842-3d7f-9572-e49734af3e21 | -9.21968 | -60.29341 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 28642773-b519-3d60-907e-995b85c68b64 | -8.53607 | -66.97498 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bb2dbba-fa76-3162-8066-40db00101325 | -9.10243 | -65.92495 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 28c49995-0e3e-3847-93d7-7106ff9f5816 | -9.15295 | -68.22754 | 2026-09-16 05:55:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f92d0574-f16d-3d02-a7f0-646fdb02a272 | -8.6494 | -66.59563 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 92d6aa27-a952-35ed-b906-381f9282fca4 | -7.65351 | -67.1665 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e52341d0-e43b-3828-b1cd-ab3bdf2bb635 | -7.61719 | -67.24606 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7aacab62-c79e-3549-85a8-3d5e9b4cf119 | -11.19196 | -55.03755 | 2026-09-16 05:55:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c5025d2b-1805-3e6a-9baf-648aa87934f0 | -9.10527 | -65.92917 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57e6b5eb-359b-3db8-91a7-53073837388a | -2.70014 | -57.62083 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a36571ab-adf6-365d-925a-041c931e8d1e | -9.2012 | -66.07991 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 18a5b430-9f42-3a8a-ada4-0244d0c968c1 | -8.64995 | -66.59209 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34954d73-7d15-311a-92c1-f34989461486 | -8.5468 | -71.49146 | 2026-09-16 05:55:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a4dd90e5-c5dc-3ade-8015-7a595769b6ee | -9.05663 | -65.92587 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f865f3b9-ee54-37e6-946b-18efc02c3489 | -3.05573 | -57.14547 | 2026-09-16 05:55:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 62571ac2-f01f-38d0-a352-519954c6fc52 | -11.19863 | -55.03172 | 2026-09-16 05:55:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6cca497-92ad-32e9-b3a1-d72a351a7c51 | -9.10471 | -65.93287 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f92d992a-d0f4-31f0-b2dd-d76f24d88ada | -12.11083 | -57.19219 | 2026-09-16 05:55:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d822f19d-b47e-35e4-8d04-ac94f06f3faf | -8.63789 | -66.52146 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1464b832-e0cb-3ed5-bb9d-d520d3ba98d3 | -3.11505 | -57.68267 | 2026-09-16 05:55:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7f88388d-4ff0-3e1d-9470-762636c888bd | -8.66091 | -66.49913 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea540928-77e1-3552-ac0d-3ef8ac1f65ef | -11.80917 | -60.46674 | 2026-09-16 05:55:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3e593aa2-7e79-3b72-abcc-717fe8f4d834 | -9.05701 | -65.92543 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6921059c-6cfe-337d-b02f-2541729357c1 | -11.19673 | -54.12787 | 2026-09-16 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 322d57cb-9f5f-3f28-aa96-92426327fb10 | -2.70349 | -57.5291 | 2026-09-16 05:55:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 863d9faa-4be6-32b3-b5f5-efeec631e596 | -8.63115 | -63.00594 | 2026-09-16 05:55:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d527e3bd-7db3-365f-a843-b832db39830e | -7.61609 | -67.25299 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a926c22-3c42-3359-a486-81481587edce | -9.72252 | -64.90907 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 04d06f45-454c-3652-85b4-d385b61a2a95 | -8.8264 | -62.47863 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e5f05219-2248-32c1-a9ac-fe743e94608d | -7.6502 | -67.16597 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 493e2e77-5553-35a3-bc97-27f8a8a26e8e | -8.64267 | -66.57275 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cb8ca1f-d3cc-3079-bcdc-ae4c8e76a1a0 | -9.07008 | -65.93125 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 812c612c-aef9-37df-b32b-076f69194b67 | -9.71058 | -64.9156 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f6c4d277-1f79-315a-9ad6-7e4c0d8ad8c8 | -7.61443 | -67.24207 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48b4ed27-3fa8-3310-a0fe-72702047300c | -9.38924 | -60.30564 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5558a547-db90-35b1-a771-c6173da0d036 | -9.12405 | -65.85217 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99eeb368-f933-33c9-a052-96a45f7dff57 | -9.56533 | -59.3141 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8349dd1b-a95f-34e7-b0fc-e22973c6b747 | -9.51192 | -68.27842 | 2026-09-16 05:55:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 3f10c30f-b83c-34d6-8c9f-2766a0c7dd74 | -7.64027 | -67.1644 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 858a39d4-e838-3d63-b3ce-50f9d8b458f2 | -10.65982 | -58.76108 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b53bfdd3-058b-30c4-82fd-1d5fd72dc777 | -7.63863 | -67.1748 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f5d83baa-6128-3cbc-8ae9-038aa05e426a | -3.10988 | -57.68188 | 2026-09-16 05:55:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ffe0f505-5aa6-3650-958c-b44d39be73ec | -9.83046 | -57.70481 | 2026-09-16 05:55:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 00bf46d1-0e4d-3455-a9e9-b10f8ea30794 | -7.64303 | -67.16839 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ab568823-74c4-39a3-bb18-1297b63e141e | -8.64602 | -66.57329 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 074b734e-a051-34a2-9dd5-4886baf474e6 | -9.05606 | -65.92957 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e0c0f28c-4b9c-399e-a0b2-6b5003eb8768 | -12.06055 | -63.3793 | 2026-09-16 05:55:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b5e23a7-c7a5-3f30-abc9-068fb68667cd | -7.85659 | -55.46001 | 2026-09-16 05:55:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ef61595a-d067-3a0a-8386-06390afc176a | -10.65938 | -58.76455 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc744b99-2e54-3cda-9076-972cbc550469 | -9.05495 | -65.91423 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa76ae14-86f4-3887-aa91-7930b4d25915 | -7.61278 | -67.25246 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e4910b2-3400-33bd-b6d3-a1f949a57ad1 | -3.16984 | -58.64353 | 2026-09-16 05:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8588df5e-bc5c-39b8-830a-a8dad30fbf74 | -9.13146 | -65.84951 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b44461ed-219d-34b2-81ea-75316691b881 | -7.64249 | -67.17186 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 55370408-15b9-3470-a506-cf56662e343a | -7.60893 | -67.25541 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4b016070-3256-3a8c-8c2f-4538ba2ad567 | -9.78005 | -62.16493 | 2026-09-16 05:55:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17e0867b-0570-323b-b767-aaac4dea874d | -9.12804 | -65.84898 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36d2348f-d24e-3f22-b2b5-10e36741a50b | -8.37303 | -54.73101 | 2026-09-16 05:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d695674c-1f33-3d7f-bc65-1f07a67fad66 | -7.60947 | -67.25194 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 302a387d-bba0-38a2-88e7-6ae82c88b39b | -8.64661 | -66.59156 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13fb7789-3ecc-39b3-a548-fa02f9d2e0b2 | -7.55682 | -62.32798 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae520f7a-612a-3a19-9e7a-218ad8c8b163 | -9.02435 | -61.03947 | 2026-09-16 05:55:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ac6fd3ac-a7a9-35ff-b796-47704a10d0bc | -9.81298 | -67.55774 | 2026-09-16 05:55:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1f3c19b-9c84-36e6-9273-330961b5f4eb | -9.17633 | -65.60241 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1737f6ec-c82e-36dc-b9c2-de7685fbe470 | -8.4866 | -64.03191 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dc033e17-f2f0-30b8-97aa-9ae3cd2c4eea | -7.64525 | -67.17585 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a4131d2-06ce-3f53-a056-59b4003e0d46 | -9.17288 | -65.60187 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f7f71648-eb61-3119-a4f0-0878929b64f0 | -9.72066 | -67.0862 | 2026-09-16 05:55:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca536310-a524-3a27-9fe4-277769d8c6ae | -9.71477 | -64.91206 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb30e79f-e3aa-3a6e-996d-20b7439dff65 | -9.40586 | -68.93918 | 2026-09-16 05:55:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ccef43b-d018-3526-b667-4c027682a907 | -9.41042 | -62.71619 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 98eb5107-5fe2-37c3-97d5-329841163f11 | -7.8051 | -66.91656 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c478902f-fbb3-3150-8e47-692e7062d969 | -8.60047 | -64.0966 | 2026-09-16 05:55:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4143773d-b934-367f-a49a-c88e1c5fc8b7 | -7.61002 | -67.24848 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ce31b2a3-58c6-31fc-b1e6-72e875c478e0 | -8.63599 | -66.5717 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9dd4365-3d77-300e-baf4-00e5ffb195eb | -3.15609 | -58.63598 | 2026-09-16 05:55:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2d67e517-7b19-300c-9ed6-4fd23b9e124d | -9.04359 | -65.92004 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6904a9f-e228-3d34-9313-e1f1b230eb4c | -8.87456 | -62.51857 | 2026-09-16 05:55:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2b335eb5-cdb3-380d-ab6e-700da4d70ea2 | -7.56085 | -62.32858 | 2026-09-16 05:55:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 094dba87-6bb3-325f-918f-d007f801748f | -9.80966 | -67.55722 | 2026-09-16 05:55:00 | NOAA-20 | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 406bd29e-92c7-3de7-9f1b-5334e28580d2 | -9.38782 | -60.31599 | 2026-09-16 05:55:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| feb2663d-94bc-3c80-9ee4-b6d71843d8b0 | -7.80179 | -66.91605 | 2026-09-16 05:55:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6346526-68d4-3163-8e8d-5463696fe6d2 | -9.72671 | -64.9055 | 2026-09-16 05:55:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 24.3 |
| f0affca8-d26f-36ab-a239-8250ca946c4c | -1.84717 | -55.80796 | 2026-09-16 05:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56a36f5f-e341-320a-94d3-3756b33bc748 | -9.10661 | -65.5574 | 2026-09-16 05:55:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3867fa1e-1766-3713-a33b-1405700434a2 | -10.69589 | -54.18074 | 2026-09-16 05:55:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e57ee556-932f-3ee4-bb68-6d1bf2a7738e | -6.344 | -62.6904 | 2026-09-16 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 2db3c6ee-7b6c-337b-9585-e01738a6f52f | -18.0298 | -50.9606 | 2026-09-16 06:00:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 497f485d-d30e-3ac2-a81e-ebadc46d503c | -6.3256 | -62.6909 | 2026-09-16 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 88.1 |


[Clique aqui para ver as próximas entradas](README66.md)
