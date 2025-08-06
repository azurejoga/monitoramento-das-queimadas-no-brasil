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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f86c6bea-b2aa-3ed1-802f-e5587dcdb8ae | -10.44183 | -44.36139 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a972e2e2-04f9-3762-9079-409de7a2c7a8 | -11.91627 | -44.92645 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a247ee46-6270-3ba6-a002-ba6dc03e41d4 | -7.81935 | -46.88761 | 2025-08-06 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5c4a9cf7-8d4d-3b9c-93a4-493cd8ac3c2c | -6.36598 | -53.32019 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8666459c-3894-3377-907c-82152f9607b7 | -11.73357 | -47.52178 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db4629b9-f4af-37c1-b79c-4e00fd2a55f9 | -7.45431 | -45.70367 | 2025-08-06 04:19:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a51c0cb5-691d-386d-a365-6137e5019321 | -9.70363 | -51.94814 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d69f51d3-865e-3598-bd31-07c7588551fd | -7.08507 | -44.36182 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9df9b640-62fb-30b8-96b2-7a0b0e35315b | -11.72681 | -47.52068 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e33051ef-67c5-3aa4-b967-ca1ea933f215 | -5.9713 | -43.04872 | 2025-08-06 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 30b1b131-b102-34f2-ab76-44abfe6efa4e | -6.1989 | -43.7505 | 2025-08-06 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b595b499-28a2-3641-a415-ed40d26da191 | -8.37994 | -45.80188 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4866b992-bb56-3545-9550-d349e3b82615 | -8.00754 | -43.21892 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| f92f4ad9-0e5c-339e-a6b6-6ae9c79b0a83 | -8.53168 | -47.46927 | 2025-08-06 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 952ad0dc-80e6-3333-b8bc-73d4b17969e0 | -7.06691 | -44.39112 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6df4630-d064-3f63-9912-435ef7301bb3 | -6.04027 | -42.98474 | 2025-08-06 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c38c5ecc-dd49-3cbb-b600-b0f126542089 | -7.24699 | -44.6077 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 08165a99-4cdb-3d63-abc5-781ac1378726 | -8.24527 | -45.06444 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a82164ef-166d-3a38-89f6-5fa3a55a617e | -11.90127 | -44.97935 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a4dbec7e-5e67-37b7-b13a-1bbbaf519d91 | -10.47825 | -44.37089 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0dcb8a2e-5a02-33ad-ad2f-1cfaf5fa722b | -5.97186 | -43.0451 | 2025-08-06 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3700faa6-06fc-3375-93e9-222e72219082 | -8.00416 | -43.2412 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 7b6b2615-b7dc-38a5-b367-2402bda42810 | -7.52138 | -44.85028 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d274d9b-09f5-3f0a-ad09-2bc7ad096e27 | -8.00871 | -43.23429 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 260e5a5a-7044-3752-b173-cb2dbfc2cc58 | -7.57437 | -44.90115 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ddf74e2-f19e-3c4b-9c05-8967871069bc | -9.46495 | -57.85704 | 2025-08-06 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a4504b2b-ba91-3a00-b32b-3675ad51fb42 | -9.46515 | -46.30407 | 2025-08-06 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4c48df97-a621-3f47-b21d-7d728645a720 | -6.67105 | -44.44638 | 2025-08-06 04:19:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ea08dc4-aa44-3083-8011-bb6e74d475bd | -11.83967 | -43.72218 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9123360d-06b6-3413-bf60-706fa3e32006 | -5.90591 | -46.16092 | 2025-08-06 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d47986b2-6a7c-3264-9618-a72a20930f61 | -11.90677 | -44.94359 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 84746ab2-b4ae-3add-9d69-e5416ee20c2d | -7.82728 | -45.08686 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84c3acbd-6f68-3e2f-9d36-77d08150f08f | -7.65233 | -46.59447 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b885b2e8-486c-3c31-be7d-96b8ab382051 | -5.75806 | -45.1089 | 2025-08-06 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d1e902e-f90a-3a12-b146-6ed5e0daf25a | -8.51472 | -43.31393 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ee50470a-40e3-3494-b6ea-7cfe45091dc2 | -7.33218 | -46.06236 | 2025-08-06 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b259a75-e431-3f20-97bd-2ccbe2bf8ca6 | -8.24251 | -45.06045 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71dfb7a1-56ac-3864-98c0-66f82e28cc4d | -6.2616 | -53.63953 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b53ef014-23e9-38e7-a1c0-5f5ea2fa3031 | -11.4331 | -45.132 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| f2f4ff7a-2999-3d4d-b9d2-c9ec8a19d3a8 | -6.6934 | -44.32552 | 2025-08-06 04:19:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| af74e638-b602-3167-aa1a-7f51a0ec2e0b | -12.54757 | -44.74147 | 2025-08-06 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 331e147d-baf1-33c3-9991-5b41222eada2 | -8.06594 | -49.72046 | 2025-08-06 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 584a1b3d-0822-36c9-9b6b-8ac681691f4f | -8.2541 | -45.07295 | 2025-08-06 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c81ab608-6076-39b3-91cd-122f9521cb24 | -10.64985 | -45.23605 | 2025-08-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5f490004-d4cf-36ee-be6b-a01ee6e64f9c | -11.74195 | -44.99844 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ee0be2e-e674-3653-b70c-d8d1a98c6ac7 | -7.68132 | -45.10653 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b764d7d-4ee6-366a-97c4-b520648adac1 | -5.59333 | -51.13396 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8a9057a7-7c2a-301e-8388-72dd8da07044 | -11.75869 | -45.02303 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cf30c53f-66b8-3dde-a367-08e51c94be12 | -11.84372 | -43.71883 | 2025-08-06 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f6ad42c8-2f4b-385f-b2d9-c73ba45b20e9 | -11.64651 | -50.15028 | 2025-08-06 04:19:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b9eeb34-09bb-33f5-a226-c113f5ba777e | -10.64598 | -45.23904 | 2025-08-06 04:19:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 838bb738-e500-3101-9b2d-81df3fe754c2 | -11.42645 | -45.13093 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| c8472bb1-3e23-3c35-b7ab-4f45f3c3e154 | -6.26686 | -53.63832 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 06ad056a-8b02-31aa-9ef4-7917b02d123f | -7.91325 | -45.53063 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5498e3a-4c8a-30d5-a406-2f19454023ec | -7.5223 | -45.05972 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a910e1-0d58-386e-af86-f4ea109117be | -7.57768 | -44.90167 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 544a0297-6b33-39b6-b9c9-01df8460904f | -11.79203 | -45.00642 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2efe6e33-ab23-3b45-85d5-99f387d04e09 | -11.75466 | -44.96022 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 370521ba-3652-3bcd-b6c3-e90823bca731 | -6.43025 | -44.81199 | 2025-08-06 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90b97f3c-1460-3717-9448-25c316d949f5 | -11.0379 | -47.61552 | 2025-08-06 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6d035e3-f270-30d6-a282-be7421cb43ac | -6.3665 | -53.31718 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5ef64e6-4dce-3375-b281-5571d4c752a1 | -7.85752 | -43.85035 | 2025-08-06 04:19:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8072e250-38ef-3121-bb69-5f89a2408608 | -9.64533 | -43.84439 | 2025-08-06 04:19:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b9ecf8f2-5922-3285-ae43-99f62241ab60 | -4.82368 | -47.31347 | 2025-08-06 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b67a1642-1c8a-3528-a968-938f49bb10ab | -6.79198 | -43.24778 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| d0d2fc9d-b628-351a-b310-8fe0353a7a93 | -12.39423 | -40.9048 | 2025-08-06 04:19:00 | NOAA-20 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7b9c7898-af7b-365f-bc57-d4b8aa9fd7ad | -11.51219 | -44.36797 | 2025-08-06 04:19:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6510ba53-0a8f-3461-949b-5cd9e204f2fa | -6.94448 | -51.6352 | 2025-08-06 04:19:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96a9b808-b706-3bd3-8b1f-1f384b52c082 | -7.14584 | -44.08125 | 2025-08-06 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a678e64-4ca6-3a9c-a287-a94d89eef686 | -8.10331 | -43.02939 | 2025-08-06 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b6c6abe4-b780-3538-8f89-dca5f8570c5d | -7.6327 | -44.57266 | 2025-08-06 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8de94084-d6b4-3ef7-b793-4f8980bdf076 | -6.54868 | -42.79906 | 2025-08-06 04:19:00 | NOAA-20 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| eaa04bf5-7b4c-314b-8aec-03a6693ca5e4 | -7.10774 | -44.36891 | 2025-08-06 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7d28679a-9b18-355a-8dfd-12752fab6d44 | -8.98893 | -45.68879 | 2025-08-06 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3c19e3cc-a4ff-3686-93a8-466baaff5462 | -6.95508 | -50.45744 | 2025-08-06 04:19:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2e0094a0-5f13-3757-8968-6dd928af11cd | -6.83276 | -43.38783 | 2025-08-06 04:19:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d1f90897-97d9-35f1-83a7-412b8d5a6f0d | -8.84334 | -47.60152 | 2025-08-06 04:19:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8699b8d6-e00d-3329-bc2f-dc8dc39aafb3 | -12.75778 | -44.4137 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 2d21851f-5e25-36e4-8314-d1ba2c253600 | -6.41423 | -53.37552 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8ec205ed-10f1-34f2-9db0-95fd62865254 | -12.75721 | -44.41745 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 8ad4cfd3-46ab-36c0-bd5e-1df5e06d6017 | -10.47213 | -44.3883 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 343ade01-3865-3641-825d-b3e81feffef1 | -8.98563 | -45.68825 | 2025-08-06 04:19:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 157b8b42-50f4-3e8b-8cae-61df47c595c6 | -10.80692 | -46.50003 | 2025-08-06 04:19:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e1d65983-0d39-391c-9997-9d721ab9f7e8 | -7.55496 | -45.17491 | 2025-08-06 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8db2dc67-a98d-37d2-b3c6-920d1bd2a91a | -9.70134 | -48.87198 | 2025-08-06 04:19:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 8c30cc3c-27f6-3e16-a91c-cbd5786f71ec | -8.38713 | -45.79947 | 2025-08-06 04:19:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4889bfe2-ef97-32b8-9c81-573b228878e4 | -11.43865 | -45.14015 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| acf68b00-e680-379c-a0f6-0e7172781e8a | -12.43081 | -44.70539 | 2025-08-06 04:19:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43092fd3-36b8-3026-abff-e646c84a94f8 | -11.73238 | -47.52906 | 2025-08-06 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 955d4b7d-6046-399e-983a-4bc1d25e6386 | -11.91401 | -44.94106 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a30716d8-ee35-3226-be6e-112f4e246d37 | -4.82303 | -47.31754 | 2025-08-06 04:19:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d14daee6-e253-3e90-b92f-f08045867370 | -8.00472 | -43.23749 | 2025-08-06 04:19:00 | NOAA-20 | PAVUSSU | PIAUÍ | Brasil | 2207850 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d783b184-4ad6-316f-94b8-9792ecb6b262 | -6.2674 | -53.63516 | 2025-08-06 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 372c06bf-b860-314c-b25f-e16bc6b9adfc | -5.5889 | -51.13314 | 2025-08-06 04:19:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5ae5df94-a0c2-3bf6-8f1d-cb2cc3767bf2 | -11.74639 | -44.99184 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5b46ec83-38b9-3c5c-b0a1-30437fc074c6 | -11.75591 | -45.01893 | 2025-08-06 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 11e22c40-8d61-3e35-88f5-81cb3514866f | -7.21195 | -41.84928 | 2025-08-06 04:19:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 30348d79-200a-3e7a-b613-73f299e042ff | -10.59242 | -45.2554 | 2025-08-06 04:19:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b352fae-6f42-3a1c-9164-675a57999f2e | -10.47659 | -44.38168 | 2025-08-06 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8934889-0bf6-3f80-81ad-1bc4a54078b1 | -6.27578 | -45.27296 | 2025-08-06 04:19:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README17.md)
