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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31e1c8e9-8d66-39b1-96ed-3a5156ba5e5b | -16.40111 | -49.93361 | 2026-08-08 03:51:00 | NOAA-21 | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ee809ac-8288-3d4b-9e8c-f15341141f00 | -14.92913 | -48.25701 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 1c95c92c-5973-343d-9315-e87186d3a2fb | -16.68974 | -49.38409 | 2026-08-08 03:51:00 | NOAA-21 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e784185c-4b7f-373e-958b-fcd3d0ff602b | -18.50986 | -48.34422 | 2026-08-08 03:51:00 | NOAA-21 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c0cbb35-e1f7-3b98-a035-b3f451981c88 | -18.88873 | -41.9887 | 2026-08-08 03:51:00 | NOAA-21 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2dfcdb81-22df-364b-93d8-4389f5f6c44f | -15.16766 | -52.74289 | 2026-08-08 03:51:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c5fa7699-a830-35bd-8b69-cf102492a10a | -19.64598 | -46.20546 | 2026-08-08 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 17a7972f-11f8-3a62-8742-6e38ff2569a6 | -14.41984 | -45.66 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6275759c-2a13-3ccf-bf84-bd393f38e451 | -18.35048 | -50.72654 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 1b153282-6772-3d27-a133-838efe996167 | -19.85411 | -43.46694 | 2026-08-08 03:51:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f939bc86-7e6f-33be-8c6e-f1766b7cb7c4 | -14.41446 | -45.66383 | 2026-08-08 03:51:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43c46b75-0f09-3eee-bd0a-0e0769a095e3 | -18.39359 | -50.69507 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 23.4 |
| d2af8666-0ff7-3923-a8b4-0c6c5e5295a1 | -17.87994 | -43.78043 | 2026-08-08 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| cfdde75c-b554-388f-bf14-7ecf9bec812e | -18.12053 | -43.97828 | 2026-08-08 03:51:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 66fdc1df-8c5b-3187-9f1a-4d049511df27 | -15.92278 | -43.52277 | 2026-08-08 03:51:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 59e96e75-f3fb-3a69-b7fc-140ac358bb4c | -17.89828 | -39.93748 | 2026-08-08 03:51:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 73f3a096-9c53-367d-8924-1a614f33df2f | -20.27388 | -41.78502 | 2026-08-08 03:51:00 | NOAA-21 | MARTINS SOARES | MINAS GERAIS | Brasil | 3140530 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 17ce4373-505c-3041-a3c7-8d801044c6b3 | -18.39448 | -50.69106 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| d28f1c8d-54ab-3019-88ed-3befbc76b798 | -20.36511 | -41.16722 | 2026-08-08 03:51:00 | NOAA-21 | VENDA NOVA DO IMIGRANTE | ESPÍRITO SANTO | Brasil | 3205069 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| cf156f59-7d00-359c-8a34-2eaabe1eb393 | -14.93623 | -48.24913 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6976597a-4521-3fb1-83a6-e753413e3f3a | -15.67164 | -48.26811 | 2026-08-08 03:51:00 | NOAA-21 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7545fe2d-927c-3137-af58-0406ae10e611 | -14.93108 | -48.2473 | 2026-08-08 03:51:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f8911ee3-dc78-318b-a2f7-ccdc93032e7e | -18.38965 | -50.68554 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 37.8 |
| c3e338b8-99c3-3cb6-8cc6-e387118f4e9a | -17.91917 | -39.74017 | 2026-08-08 03:51:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 52f2272c-2906-3f5c-bcff-51785332acfe | -19.64517 | -46.20963 | 2026-08-08 03:51:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 48eb21d2-7f54-30c4-a5c4-fb7615aef6a1 | -13.95545 | -41.86888 | 2026-08-08 03:51:00 | NOAA-21 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| fd50eced-dbec-30f0-8b21-e86195373f3e | -18.35145 | -50.72206 | 2026-08-08 03:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 02cceea7-bf72-373e-bfb5-c8a07cc84ca0 | -19.75761 | -44.06953 | 2026-08-08 03:51:00 | NOAA-21 | RIBEIRÃO DAS NEVES | MINAS GERAIS | Brasil | 3154606 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c19cc509-5114-378e-8992-e4cafe5ff7fc | -22.11011 | -47.00938 | 2026-08-08 03:53:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24698f74-ecf0-3a9a-ad15-5c47f0ecca65 | -21.3699 | -45.13845 | 2026-08-08 03:53:00 | NOAA-21 | CARMO DA CACHOEIRA | MINAS GERAIS | Brasil | 3113909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 41d1ce43-a5ca-36eb-91aa-2b40a66c8630 | -20.35875 | -53.86291 | 2026-08-08 03:53:00 | NOAA-21 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24c174fd-0dbc-38e4-af26-c2570a199ec4 | -22.1067 | -47.00397 | 2026-08-08 03:53:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae88f14-e4b3-3147-9fb7-0b9f168a82a2 | -20.39296 | -49.31046 | 2026-08-08 03:53:00 | NOAA-21 | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c6125ae3-4765-34a9-ac7b-95c877a820ac | -21.31546 | -45.93095 | 2026-08-08 03:53:00 | NOAA-21 | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 1ef31e7a-cf3c-3587-a20c-cd48188942f9 | -22.10587 | -47.00827 | 2026-08-08 03:53:00 | NOAA-21 | AGUAÍ | SÃO PAULO | Brasil | 3500303 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f009762b-8277-3d9a-bc02-763a1a7bffe2 | -4.2634 | -48.2016 | 2026-08-08 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 6d48604c-29f1-3394-a6f2-8cbf302b8bb5 | -15.6968 | -54.8534 | 2026-08-08 04:00:00 | GOES-19 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 36d6aee8-5619-31ce-b149-ae41cbbf851f | -14.3614 | -54.9907 | 2026-08-08 04:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| b1bbc3be-81ee-3fb8-a8a3-daa671f3d255 | -4.2635 | -48.1799 | 2026-08-08 04:00:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| aef1f3ec-506f-3ed4-bec2-a5bb148f334c | -12.5369 | -46.9385 | 2026-08-08 04:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 519cb63f-2134-376f-9b10-5fd93b21b18a | -14.381 | -54.9679 | 2026-08-08 04:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 68982ad5-37e5-3241-9468-8dd6e632689e | -14.3617 | -54.9701 | 2026-08-08 04:00:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 135.6 |
| b3ec0211-d410-3f05-9b67-320d2833b94b | -14.3617 | -54.9701 | 2026-08-08 04:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 13afadab-ef20-35b0-9256-e9d40bfd8d1c | -14.381 | -54.9679 | 2026-08-08 04:10:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 115.2 |
| bb96fae2-eb8b-3952-8bc0-5cf1e7cc7c26 | -4.2634 | -48.2016 | 2026-08-08 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 064fe5ed-b214-3f2f-9227-70e50fecaea5 | -4.2635 | -48.1799 | 2026-08-08 04:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 90754bc4-696b-3d85-a3ec-384e8657d7b0 | -18.3538 | -50.7044 | 2026-08-08 04:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 109.7 |
| 944d4b5f-5126-3181-9953-37449078580d | -4.2635 | -48.1799 | 2026-08-08 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 5e20e20c-d720-3177-9ea0-c227b68d2b33 | -18.3533 | -50.7266 | 2026-08-08 04:20:00 | GOES-19 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 163.1 |
| 6bb0521b-f72d-3018-a6c8-e7a7cf43177e | -4.2634 | -48.2016 | 2026-08-08 04:20:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| fef0fbaf-5188-39bd-9b86-2480eac0874f | -2.87545 | -40.29843 | 2026-08-08 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 75e6d5e5-a4ed-316c-a526-0499a131b642 | -2.87891 | -40.29897 | 2026-08-08 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0426ddba-813d-3c58-ad4a-6e54681ef78e | -2.87832 | -40.30275 | 2026-08-08 04:23:00 | NPP-375D | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 30d7a824-7c04-3c64-8a3b-3c213e750e26 | -4.88909 | -37.49948 | 2026-08-08 04:23:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 71505715-872c-375a-97e9-d6f8667c2f22 | -3.96854 | -48.11967 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d94d7cd-d125-3a0c-aefc-50207a9bfb97 | -4.26534 | -48.19845 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 50627c0a-2e68-3410-a17d-b38516ca60a4 | -3.95756 | -48.12672 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fc2cc56b-4e43-3706-b1ba-a0311d47fcc0 | -4.36443 | -47.77164 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 27e5db91-2c33-3073-a8d9-81d0a6b52908 | -2.69484 | -47.3588 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 561200ac-a5b9-3fad-9822-d00c7560dd56 | -2.76894 | -49.46819 | 2026-08-08 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 16002b4c-4104-381d-bb1f-8c53ea1de1cb | -4.88851 | -37.50324 | 2026-08-08 04:23:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cf047df4-9636-38fd-ae7f-73b1fb96881c | -2.76975 | -49.46341 | 2026-08-08 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88e9def1-3565-35f8-96f7-d808d4c18f42 | -5.52632 | -45.78112 | 2026-08-08 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9365c54f-540b-3eb2-846f-66d7c50d5130 | -2.69399 | -47.35847 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a0d817df-73fc-3790-9abb-07b48de6cfe1 | -5.42452 | -43.43334 | 2026-08-08 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2858c184-ba98-3fad-98f9-261888dde3f0 | -3.96294 | -48.11978 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ddba808f-c7da-3926-bb82-7b7bd0c6f8d5 | -1.58582 | -50.44241 | 2026-08-08 04:23:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c7c0cbae-d30b-3e37-be38-28f8361d714e | -4.26656 | -48.19098 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| f2d673b3-4246-3af4-a366-50af246081c8 | -3.96791 | -48.12339 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 10bf700a-5951-3f5e-b16b-023043868686 | -4.45624 | -47.917 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 6e903678-eb10-320b-83e1-ad24d5e8295e | -2.37751 | -48.23331 | 2026-08-08 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f94bfbf4-9191-3e49-b29f-8ab601003fcf | -5.52407 | -45.77255 | 2026-08-08 04:23:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1ee75805-685c-3a4d-9484-fc7905089ca3 | -3.96709 | -48.12043 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3637d7f2-6020-3c8a-aa61-e83a1e58a93c | -2.78792 | -49.52557 | 2026-08-08 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7861242c-3cbe-3019-bc74-0580034a128d | -4.64104 | -43.12445 | 2026-08-08 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1f179e0-d497-3fd0-bb7d-21a4d94aaea7 | -2.75536 | -49.47364 | 2026-08-08 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89abddd0-38ea-302d-84aa-ab5b8d2b1862 | -2.69344 | -47.36193 | 2026-08-08 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9714e504-3b30-3e86-91e2-bccde4a5d7e7 | -3.73024 | -49.27046 | 2026-08-08 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfbdeccb-7ec9-34b1-bc2c-b939c5335123 | -2.76078 | -49.4696 | 2026-08-08 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eef268ca-6316-3a29-bf92-23f91590216a | -4.26595 | -48.19471 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 082c7d60-ad23-3887-b794-7c1afca85efa | -5.60221 | -44.26982 | 2026-08-08 04:23:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4376444b-ccc3-3330-a091-77228e3ed2a8 | -4.89094 | -37.49894 | 2026-08-08 04:23:00 | NPP-375D | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c44bd22c-3ab6-3029-a225-b8c8bdf652e0 | -2.82992 | -52.30124 | 2026-08-08 04:23:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1df68e3b-0ffc-3692-8a11-ea687b9a3a2a | -4.90807 | -43.46882 | 2026-08-08 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 38f76087-9d7b-36f6-9ac5-e1b3977446f1 | -4.33522 | -39.36509 | 2026-08-08 04:23:00 | NPP-375D | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b24267b2-4c15-3ec9-a235-d3d7cb379e0e | -4.4597 | -47.92125 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 106f6d3e-0b48-31ca-927c-b729dccd49c5 | -5.43644 | -44.38305 | 2026-08-08 04:23:00 | NPP-375D | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2888a28d-ccf1-3621-bff7-02efc3f87005 | -4.64767 | -43.12549 | 2026-08-08 04:23:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8f4cb494-5419-391b-a7c0-24b199b54ce3 | -4.16764 | -48.77052 | 2026-08-08 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ef939b3a-74fe-3b0f-8a11-295b930d0d9e | -4.59803 | -45.58601 | 2026-08-08 04:23:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd3ee4ad-3a42-399c-9b8b-d1c15e130896 | -5.42507 | -43.42987 | 2026-08-08 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 925e4d6c-5985-315c-995f-71b557250d07 | -4.2618 | -48.19401 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d3e3f1be-78d7-362c-8fc1-e3dd6ec44115 | -2.37817 | -48.22928 | 2026-08-08 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a2bb5e4a-6db1-3c4c-ab19-c34d03e596b9 | -4.16697 | -48.77464 | 2026-08-08 04:23:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 49ef3053-2e2e-3b7d-b700-4d2ff0cdcad3 | -4.2707 | -48.19168 | 2026-08-08 04:23:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 38b3b4ed-e389-3e04-b144-eef6b7a49d8e | -5.13016 | -42.8797 | 2026-08-08 04:23:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b27683b9-d705-37aa-a1b0-216b6cc711fe | -5.42839 | -43.4304 | 2026-08-08 04:23:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59720f79-c21c-3a87-b90d-e7c8bcccf648 | -3.9534 | -48.1261 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 46671b48-9560-37a7-8d60-97c3d8ee5040 | -3.96233 | -48.12353 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 30db4553-a6ce-344b-a835-f8646a8666da | -4.36503 | -47.76812 | 2026-08-08 04:23:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |


[Clique aqui para ver as próximas entradas](README9.md)
