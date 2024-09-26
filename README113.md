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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89a839ff-4f92-36ea-9615-e3ba99baae91 | -14.56848 | -45.69999 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 5c37917b-d234-3f66-ae00-ad3fac860079 | -14.56806 | -45.70386 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| a0289fef-4200-3082-8790-435ab9731c9b | -14.56649 | -45.69611 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7aecf861-37af-3b1b-a4cc-b59ad82a13e0 | -14.56633 | -45.7196 | 2024-09-26 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cd8c1d60-ba80-3ac2-9e88-9430b8c3db09 | -14.56604 | -45.70001 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d5f63498-a25a-3639-98d3-cd37e2e3c979 | -14.56589 | -45.72364 | 2024-09-26 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 72584a5c-2653-3b98-97d7-a3251c5fc93a | -14.56584 | -45.67126 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d256626a-daff-39de-91ae-791ed2b10488 | -14.56559 | -45.70388 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7eff4554-d955-3f45-a570-c975f57e1178 | -14.56541 | -45.67525 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 47bbbab5-cc08-3116-9f83-0c1bf41927e9 | -14.50505 | -45.62643 | 2024-09-26 04:59:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 05acc5d4-797c-3558-bf27-9ad69126ce30 | -14.41699 | -45.30341 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 906e4f0b-6694-3fae-bac2-08c3a5a992b5 | -14.41653 | -45.30764 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cf7be659-2bb1-3dcc-a776-7d422129dd5b | -14.41606 | -45.31187 | 2024-09-26 04:59:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| dcd07184-aaa9-3c36-88bf-100927839c7b | -16.56127 | -46.93578 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8442e266-3034-3e72-900e-f1960ee4bee4 | -16.55588 | -46.93515 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9070106f-be65-3e5f-96e8-93ff929b91a4 | -16.55302 | -46.93661 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8400a27-0e02-3f09-8403-961ec5034b33 | -16.55007 | -46.93843 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1420a243-bd46-37c4-a52f-3c73734eaab3 | -16.54968 | -46.94213 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a73419b6-ccd5-3ffc-b751-000960eaa3d8 | -16.54763 | -46.93602 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5ea2479a-9b69-3519-b399-2edbc0aa45dd | -16.5472 | -46.93975 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2e59162b-f2f3-3bc8-acc5-73de519e15eb | -16.54603 | -46.99761 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c85378bd-9128-35ee-a74a-f1ae6f32dc19 | -16.54563 | -47.00107 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 181ea3b2-6901-3793-87a9-78f4a54801df | -16.54469 | -46.93773 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d7386a0-6729-3fc8-98e5-5bfcbc4e0d1b | -16.54425 | -46.99289 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 45023c97-65ce-330f-b1eb-4de5cc9fda94 | -16.54354 | -46.99945 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8903190c-6d06-375c-a962-990229b1c076 | -16.54137 | -46.99078 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b4d21e3e-e4e3-3be8-b6d4-be67674d2bc0 | -16.54099 | -46.99411 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5970f01-b80d-3cf4-be72-17033888b6c0 | -16.51254 | -47.00532 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 991d072a-1595-3d75-b804-5c49241b3a2f | -16.5072 | -47.00449 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fa7239da-b294-39d5-857d-76b55fd57c53 | -16.49074 | -47.006 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d7c028f9-f4c4-3bdc-a1fc-2aa528e5399d | -16.48541 | -47.00512 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19166cbc-d0a5-302d-9096-1bcffdd3f612 | -16.48499 | -47.00892 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22aeb836-c040-3af5-acea-164852204bca | -16.47966 | -47.008 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ff9559fd-2fc6-3ecb-83c6-b9dcdee71491 | -16.47392 | -47.01081 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| df108682-f0ca-31eb-b4fd-c973d62fa611 | -16.5927 | -46.94804 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c493f6b5-5f37-3258-89ab-5a394fe9afbb | -16.5923 | -46.95166 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3111cff1-4122-3fc0-a372-5d2a5c1a2ba5 | -16.5873 | -46.94753 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 93b0507b-48fa-3b78-ad26-8b96047ff5cc | -16.56667 | -46.93638 | 2024-09-26 04:59:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e8f47992-e328-3967-913a-131e03268c7a | -12.18486 | -46.75038 | 2024-09-26 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 738050ce-f758-3d66-bbc8-1beedc94bfd9 | -12.18203 | -46.75086 | 2024-09-26 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 65238b82-10d1-3f34-a46a-e60b4dd2a5c5 | -12.17972 | -46.74968 | 2024-09-26 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b8cf86e-f5a2-3c87-8a07-00c376ddd7e5 | -12.17496 | -46.74596 | 2024-09-26 04:59:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07e58aa9-112f-3e2a-bbe0-a0ae55e50847 | -11.93105 | -47.34278 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 47c854f6-34ef-3934-b92c-d49f6db65e98 | -11.93034 | -47.34839 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b00a3e01-7d10-3fd7-b185-ae78d30ed335 | -11.90836 | -47.15982 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80a239ab-b97a-30f8-a04e-0c59f2e14c45 | -11.90764 | -47.16572 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e94d6a71-cd1d-3294-be56-9622ae148701 | -11.90753 | -47.15984 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 456a3d4d-0a5b-37ec-b1ee-ff089b640cbb | -11.90676 | -47.16573 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6c70913-deb7-3b85-bcb0-0166618fb499 | -11.89756 | -47.15846 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b592069-c348-3855-be35-a1043191cf56 | -11.89184 | -47.16356 | 2024-09-26 04:59:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0c41a9fb-e1ac-321d-af87-dc07488da26c | -11.51393 | -47.55834 | 2024-09-26 04:59:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 940b489d-d997-331e-827e-b5321283c7ac | -11.47831 | -47.29451 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 74a5118a-e558-3e70-a655-68e6692c9374 | -11.47761 | -47.3001 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab172f7e-5752-35fa-bf36-d6f765bc2616 | -11.47622 | -47.31125 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 34ff8662-c2f0-374c-b157-404f9b16b0cd | -11.47612 | -47.29271 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c166620f-def4-364e-a3b8-df75028a395f | -11.47538 | -47.29827 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9a5084c9-8f3a-357c-b9e8-30b14d7838f9 | -11.47464 | -47.30384 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3f036031-0d45-370a-8a55-4673b9dc698c | -11.47409 | -47.28827 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d6a4b249-b02d-34c2-a500-1c2640f9c8f3 | -11.47391 | -47.30941 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9f2cfaa5-a5f9-33c0-87ad-5681cfe778fa | -11.4727 | -47.29941 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 583a17a4-bdbe-3048-b1c2-052368fef1f0 | -11.47201 | -47.30499 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ec62542c-7c3d-36d9-9874-e11835bfc0b4 | -11.47194 | -47.28649 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6c02798d-8a76-3ec4-b616-c60766d5194a | -11.46974 | -47.30316 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d76f0ea9-1afa-3486-a1a9-2c1d2d3b20da | -11.46921 | -47.32743 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35d00536-33d8-3c49-b81a-8158c192d280 | -11.46604 | -47.33118 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1cdb46b2-be04-3132-ab73-6914a31b7f1d | -11.46362 | -47.33239 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5828abe1-39b2-3cce-8385-da0ba2dcce7e | -11.46188 | -47.32489 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1ea37de7-f2ae-37ba-8e9e-540e0afa5c19 | -11.45942 | -47.32606 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32556aec-8c61-38ff-9897-f639b7fe59a6 | -11.43958 | -47.30479 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8b614fc8-c943-3268-acda-aa497c404a37 | -11.43467 | -47.30418 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 806f602d-f331-3f21-b015-583e73a3ceb3 | -11.27952 | -47.00256 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9ceee99a-797f-3fe2-8b40-1952716c925f | -11.27914 | -47.00549 | 2024-09-26 04:59:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5385e46d-e4a1-3cc7-b7ba-526fb6dc4c35 | -11.32067 | -46.3144 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 523ab40b-a26d-3574-b565-8bbac351cde1 | -11.27339 | -46.26509 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2eacffa8-6100-37a3-ba79-5e65110f251f | -11.27296 | -46.26849 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef043f67-fead-3b89-8a83-628350518fc4 | -11.14405 | -46.18826 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dac0eff0-7601-3cfd-b226-f5f67ba5859c | -11.13119 | -46.16271 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0055e09e-7784-37b5-b4c8-fee116d975e8 | -11.13077 | -46.1661 | 2024-09-26 04:59:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 67b2d48a-82a7-35c4-8f4e-f1d0c472ee19 | -11.67546 | -46.34204 | 2024-09-26 04:59:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ab48e6a-2773-3e86-b75a-94af9d284fe6 | -13.56969 | -47.71171 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1349abba-0173-3098-87e9-0d8b93ab1939 | -13.56736 | -47.7113 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aa3547d2-ff1a-3466-97e7-eabc7c0c7b98 | -13.56539 | -47.70596 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d53bf1af-b4f9-315e-9443-48d85734a7d2 | -13.56476 | -47.7112 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f135543-6ba5-3b67-aea8-3840b48b13a1 | -13.56309 | -47.70564 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3788668-f34d-39fe-8b16-a18158f92b8d | -13.41247 | -48.04553 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8dc8741a-6088-3376-82b3-c062ce6e6cdd | -13.41228 | -48.04616 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46a2c8be-2729-32a0-9688-76d2a0c93895 | -13.40768 | -48.04486 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 874f8c18-9c3b-3781-aed4-a802bb5bc6c5 | -13.40749 | -48.04548 | 2024-09-26 04:59:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48802a52-258b-3dc1-9ed0-ce6b1ad7adb6 | -12.91935 | -47.70734 | 2024-09-26 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cbf0e5d3-b188-3f7f-84a9-63cb391902eb | -12.91771 | -47.70747 | 2024-09-26 04:59:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0cb1cda2-0d72-320f-87a3-3a8fed30884a | -13.43012 | -46.93457 | 2024-09-26 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2a8d1a3-72cc-32e2-950b-59117a19bccc | -13.42978 | -46.93736 | 2024-09-26 04:59:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac52ade6-c72f-36ec-80eb-2bd7113d2457 | -14.6314 | -47.60751 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2158be22-487f-34f5-9161-78b6aeba8d3f | -14.63103 | -47.61057 | 2024-09-26 04:59:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea81c13d-bbfd-3866-875e-25e15d5ed142 | -14.15264 | -47.8133 | 2024-09-26 04:59:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 40c2acf3-365d-3eee-ab4f-f233c2e72c5e | -13.82806 | -48.03668 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6df49562-2152-32ee-a7c4-0ad6e167ad95 | -13.82332 | -48.03539 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8a0d18a4-0219-3150-bf00-637c8c6e1e25 | -13.82215 | -48.12196 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0baee0f0-322f-3c57-beff-f9ac3cc6fd5b | -13.80322 | -48.07848 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d9db8681-5bbf-377c-8907-ff07c29609c4 | -13.80254 | -48.1228 | 2024-09-26 04:59:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |


[Clique aqui para ver as próximas entradas](README114.md)
