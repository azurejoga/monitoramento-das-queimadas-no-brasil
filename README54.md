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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 036aefd3-ea91-3a23-b585-dbde1e1f6a5c | -3.44213 | -58.40255 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0ebe273a-b3ae-33b7-96f4-277411ea13f8 | -2.68822 | -57.58595 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e9c6722-4dc4-36a2-9282-f16922172bb1 | -2.90522 | -50.43272 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| d705a7ca-3cde-35c3-b23c-d0835c414d4f | -3.42882 | -58.22395 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 745873f0-2e95-3182-8a3e-2efe2542d8d8 | -3.40391 | -58.18842 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 43f89277-c1a6-38ef-b5eb-e7bbfb7dbf98 | -3.42105 | -58.20867 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b0775a8c-1cb9-34ca-9827-0107baa77618 | -2.66876 | -57.55809 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7d19de0c-a7ae-32f2-9d61-b781458ccaff | -2.70821 | -57.61031 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32581319-02f7-345e-a154-f77243855d55 | -5.00454 | -56.09006 | 2026-09-15 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19ff6869-cb5f-333c-a6df-7b2aea1241c3 | -2.92076 | -50.42944 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e19fa2ee-31cf-3d8c-bbb3-7b63b598f34f | -2.91093 | -50.42802 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 73a50678-6d7a-3402-b124-489148a4ca55 | -3.16359 | -58.64016 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca3bbe2a-32de-3559-a9c2-14439f0b3708 | -2.8954 | -50.43123 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 459e62c5-0943-3ada-bb99-5aa522495dce | -1.22462 | -54.13922 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4876bace-f920-35e1-ba36-6c1fefdff419 | -3.44543 | -58.40306 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04a7a042-8ffa-3043-bfeb-9aa6df5e3db5 | -3.64719 | -58.6137 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 80b0ebfd-578b-3ac3-ac18-b7379ba24317 | -2.82884 | -49.23363 | 2026-09-15 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a43dd124-6a06-3316-abe6-e61d163c1964 | -4.13781 | -54.02086 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a7fce3c-b144-3c0c-96a1-5adf60fb09ff | -3.79363 | -59.35141 | 2026-09-15 05:16:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 47fab136-6172-3479-a462-257c644c7c5b | -2.83951 | -57.64107 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3899b852-3cf9-31a4-8548-d10c9d85e351 | -4.51478 | -54.96713 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 16773546-5090-3b0f-bb76-672ad6b3f488 | -3.42671 | -57.97688 | 2026-09-15 05:16:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c7dc7781-cfd7-3bcf-9f85-74bedcd45141 | -3.25654 | -47.08945 | 2026-09-15 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 771313e7-9f1c-3331-96de-4e7e1bfca2a8 | -2.95349 | -50.41214 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fcc3653b-dd00-3d1b-bf6d-1f0885f99718 | -2.91659 | -50.38943 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bdfc1a94-56b0-3fc3-b103-f73ce0d4c01e | -4.18292 | -49.40313 | 2026-09-15 05:16:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d3953235-d656-3d0a-9b90-b2536c6684d8 | -3.72632 | -61.74878 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 39deec3f-04b4-3111-827c-553971040bdb | -2.66383 | -57.56799 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 246dcf61-4aed-309c-872f-c48a015d32b4 | -4.55518 | -50.46444 | 2026-09-15 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f09e30b-2729-31e5-82a2-c939dd76affa | -3.36042 | -58.18525 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 487a23cd-30c7-395e-b9a5-005c57f4eb1f | -3.42435 | -58.20918 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20238161-0b8a-358a-b06d-5e24a730acee | -3.41337 | -58.21452 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| eba72b06-3cd4-33bc-8005-b0583a44e0f4 | -2.8659 | -49.62918 | 2026-09-15 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 42b95c65-24ad-3f94-b733-6fe8522a544b | -3.23566 | -50.58712 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7c6a85f1-2b9e-3d1f-8f3f-e805edca3200 | -3.45863 | -58.4051 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 96da2cd3-f1c7-39b6-a1f2-337e82258319 | -3.74145 | -61.74687 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9f0a2694-7f39-3595-ba94-72a1edbc59a4 | -1.19696 | -54.12016 | 2026-09-15 05:16:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9569b944-5a6a-34f8-9f70-bc4b544f6d7c | -3.7306 | -61.74517 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 16d62b91-c0d4-32e0-b157-f1b3d6c42ce1 | -3.42328 | -58.21605 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e41ad9c7-d4b4-3417-b4fc-b07958888e53 | -3.41614 | -58.21847 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 869155f4-fd3d-38c9-8e28-22d799202887 | -4.44482 | -55.01302 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 99421618-9234-3636-9132-94b4087ef97c | -2.99589 | -59.36241 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b654ef5-900f-33d6-851b-e5ad42cd6f66 | -3.11199 | -53.94949 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4fe8b6e8-75c9-3caf-8f57-bdbb6d2407d8 | -3.25702 | -54.52008 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3fc00263-2aca-3879-b011-4b40127b3b05 | -3.38033 | -50.77047 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af5aed44-5120-3bb7-a5bf-7ce6487e5096 | -2.66586 | -57.53279 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 201407c3-7abd-346b-bea6-95e0d42fb884 | -2.89129 | -50.42497 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dee2a85d-f2e7-303c-bcf3-fed5dd0e2c30 | -3.39704 | -50.75204 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 468b68ea-2765-3740-89cd-a211b765bc72 | -3.34497 | -58.17583 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8f71eab-759b-3261-b7b4-a35cdc80b761 | -3.2601 | -54.52521 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 836d9cdc-cdb4-314f-ba66-b00207f7fea7 | -2.91497 | -50.40048 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| aca430c8-b000-3f4b-9882-17e151bd4e50 | -3.38725 | -50.39204 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1e271bc0-4bd7-34af-9a5c-e24f030ac10e | -2.84005 | -57.6376 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b71ac939-a541-3d79-b77a-a1baa614f2de | -2.70714 | -57.61724 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c65d7d65-1544-38db-902d-7b8cfcc5fd5b | -3.55174 | -58.67979 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| dfc689b7-4053-384d-abee-142e4832fa8d | -3.78417 | -51.34908 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 185e3688-eefd-3419-bfb0-809afa47e7ad | -3.26078 | -54.52066 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7e40a27b-5afd-3321-9250-56b6eddadd54 | -4.52583 | -54.91879 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| db92ab62-1b40-3474-994f-e0b7872195c6 | -3.77415 | -51.35227 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04920148-fcbe-3fb0-bd0d-0897ea683cfd | -2.8995 | -50.43749 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4661ab09-efd8-3826-87d6-c8e0c1260f86 | -3.73848 | -61.74215 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8d3b3263-a14d-39c3-8b48-2412a3e91c5a | -3.42605 | -58.22 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c318ef02-83d2-3fa2-aabd-2e04a66f025a | -3.33749 | -54.19096 | 2026-09-15 05:16:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e55c9bc7-50c6-3e2e-afcf-cc707a9f2b7f | -2.96333 | -50.41363 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33c90ea3-6063-316b-aef8-fb8354a9aab4 | -1.00944 | -53.04425 | 2026-09-15 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b7013ba3-7906-3578-a104-a262c17e8f6f | -3.72573 | -58.87293 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2eb41d1a-0a96-302f-9574-35b8b0e0c519 | -2.97462 | -54.15346 | 2026-09-15 05:16:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6f0e2f24-b84c-37d0-a390-6ac63fa310bd | -3.41284 | -58.21796 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6e03f0e-01bb-34f8-bd5b-8ac2cf2a9c7b | -3.25942 | -54.52974 | 2026-09-15 05:16:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b9ff02c8-36a8-3ab9-a022-25ff5409e8ee | -3.19066 | -61.12331 | 2026-09-15 05:16:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 13249672-2d35-33bc-86ab-0681036258ec | -3.85984 | -51.98467 | 2026-09-15 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6f5ac06-6f7b-3a32-9a07-dd48b15b7857 | -3.4106 | -58.21058 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 59675e54-9ebf-3ed7-a632-a0ecbca1027f | -2.90595 | -50.39337 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8663f364-8ca3-370b-9c61-2085c2e6f381 | -2.77676 | -51.36977 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf986994-6113-3ccc-9956-eec2b545a7e5 | -3.17625 | -57.86055 | 2026-09-15 05:16:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ffdef204-2bc3-354e-85a0-16d336e37ad8 | -3.3826 | -61.30821 | 2026-09-15 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 54bef850-8223-3b65-8152-12ad8b3d7d2b | -4.91921 | -49.22978 | 2026-09-15 05:16:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5252b3c-41bc-308b-96e6-446047d56cdc | -3.42551 | -58.22343 | 2026-09-15 05:16:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c49c26f-91c3-36c4-9ae9-7c4bd305303c | -3.72019 | -58.86503 | 2026-09-15 05:16:00 | NOAA-21 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9949a25d-fae2-38fc-aa88-a9b818090d7d | -3.25034 | -47.08884 | 2026-09-15 05:16:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f6ab26d-2518-3370-9af1-b2ac5d662fc8 | -2.6918 | -57.51898 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| bf901980-48b6-371d-8794-b5044a9a11bb | -3.77488 | -51.34734 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 53e3cb32-bc63-3ff0-9009-b0f1320ae391 | -3.91887 | -54.52259 | 2026-09-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f40b07fc-1e13-3015-a69c-cc7187847e56 | -3.73783 | -61.74629 | 2026-09-15 05:16:00 | NOAA-21 | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 61997d3b-7de7-3678-b117-49b21e31720b | -2.70095 | -57.59145 | 2026-09-15 05:16:00 | NOAA-21 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd1f0bc1-b2d2-39f9-b906-9d5aba338c04 | -2.9207 | -50.39574 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d568968a-91c0-3f3d-b713-2c4de88c5b51 | -2.90924 | -50.40523 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fc58dfd-0493-396b-a008-6f90e28c1ecf | -2.78145 | -58.14366 | 2026-09-15 05:16:00 | NOAA-21 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 443e6a98-784b-3caa-becd-ac929b024468 | -3.37487 | -61.31112 | 2026-09-15 05:16:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 83d18b1e-0e2b-3784-80a2-049a8d46f58c | -4.24229 | -55.16182 | 2026-09-15 05:16:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b497db06-f3f1-3acd-9055-b8f5411f4cc2 | -4.54723 | -54.90336 | 2026-09-15 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a1fc4f1-380b-3f0e-a682-b4c42a822efa | -2.96006 | -50.40184 | 2026-09-15 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3e37cb38-073b-3d30-a27b-3d137c16c37c | -3.04545 | -51.26893 | 2026-09-15 05:16:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5b21d99d-7048-3e7a-8fc5-077482606740 | -3.8962 | -54.57101 | 2026-09-15 05:16:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f5fa84e-62ce-32df-8405-0599be8b9be8 | -6.1577 | -55.71505 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f891a5d2-6d43-3733-9a63-d61f48e83f94 | -6.16197 | -55.7114 | 2026-09-15 05:18:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7cf57984-14cf-3ba1-8193-c9fccb81c337 | -9.36065 | -50.09665 | 2026-09-15 05:18:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e5299c8-ca1d-3c77-ab27-f0959481c748 | -5.81233 | -53.79726 | 2026-09-15 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 755527bf-a31a-3187-8161-e440559a909e | -9.38219 | -57.45606 | 2026-09-15 05:18:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7aad4bd-c051-3d39-9867-9ab76bd8ea63 | -10.50283 | -53.56743 | 2026-09-15 05:18:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README55.md)
