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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5a98104-761c-34c9-8328-68628dc7d959 | -10.67739 | -54.17246 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a4767d25-c064-37e1-b06a-8730b615502b | -10.66892 | -54.16154 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 38e75e95-5979-3a44-83c9-e16ff3e865fb | -15.06552 | -48.5606 | 2026-09-14 04:34:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c207f718-ab5a-30ed-a3a2-633c27030272 | -13.3154 | -51.30793 | 2026-09-14 04:34:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0959476a-ea4f-35d4-820f-3dbe38b2f86c | -13.65613 | -43.92565 | 2026-09-14 04:34:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 39ffc8dc-42dc-3928-9531-9887ab81bb3c | -14.18093 | -47.39563 | 2026-09-14 04:34:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 15.7 |
| f4bd03fe-ed38-3ade-9154-b12bc12c4cbf | -10.67567 | -54.1694 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 4dff1a6f-374e-3a8f-b16d-c13e492b9918 | -15.55346 | -48.79676 | 2026-09-14 04:34:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a7fb6b1e-8827-356e-ae10-eadc1a9c3c64 | -10.03522 | -52.12569 | 2026-09-14 04:34:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1bfb2502-6222-33c2-9180-b73cc7422348 | -11.42492 | -45.1361 | 2026-09-14 04:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3343422b-0b5f-327a-b4bd-db981d201176 | -14.87383 | -49.94649 | 2026-09-14 04:34:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1487beaf-f8e7-3733-82b3-ad03b8b14720 | -16.48213 | -43.4201 | 2026-09-14 04:34:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fcf8cb31-6d0e-35af-a9f6-cb919a0ab29a | -10.65996 | -54.15342 | 2026-09-14 04:34:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 09b214e7-ee34-3adb-a283-15874faf423f | -11.18819 | -42.81028 | 2026-09-14 04:34:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e7049c08-5312-371f-91a0-3d9ad1934790 | -20.72296 | -48.67493 | 2026-09-14 04:36:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18e4dd98-a95c-362c-9236-497d63c5426a | -20.72356 | -48.67122 | 2026-09-14 04:36:00 | NPP-375D | COLINA | SÃO PAULO | Brasil | 3512001 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7000ecd9-7b39-31c0-9ef7-1e93dceb39ba | -19.36427 | -44.30429 | 2026-09-14 04:36:00 | NPP-375D | PARAOPEBA | MINAS GERAIS | Brasil | 3147402 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24f85ac2-4517-30d6-a94b-532e2ddf009b | -18.25709 | -46.24621 | 2026-09-14 04:36:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02c6cb9d-0eea-3203-ae3e-0696a50ed942 | -18.25371 | -46.24565 | 2026-09-14 04:36:00 | NPP-375D | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16fe1375-80c1-3a9f-8fc5-a493889d2696 | -4.34438 | -48.9646 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| a58e4274-2976-318c-932d-2399c9dc06d3 | -2.9319 | -50.39196 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f1df59eb-cde4-3183-8d5c-ff273d9028c8 | -2.90281 | -50.44728 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a155f6f8-d723-3d7c-9c2a-052565ab4b2d | -2.95179 | -50.41621 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cc2b8f7b-1d49-325c-ba93-0e52f0452af1 | -2.88624 | -50.42355 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 3b568674-8d72-314d-b00e-8e0e6f4a0699 | -2.90608 | -50.42666 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.7 |
| 24deb604-b7e6-33b3-891c-225d74976a3a | -2.93362 | -50.42393 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6e298bad-4119-39e7-9c4e-e80f18a00096 | -2.96552 | -50.3937 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0593a474-efea-3e4f-8db5-0e0181531cae | -3.85803 | -51.97878 | 2026-09-14 04:51:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32fb6294-52b0-304c-b3bf-461fcfa14018 | -3.37587 | -50.39842 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 91de3a50-8015-3d73-837c-e9b92a2dc35e | -2.90218 | -50.40844 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 81154182-3835-3cfe-9acb-513cd1ac1168 | -2.6732 | -57.54912 | 2026-09-14 04:51:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a5747b5c-7d31-3105-b2f3-23a5c098bdaa | -2.91767 | -50.43905 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ea561d7b-4fa9-375f-ad00-b76d700a4ca2 | -2.95949 | -50.41037 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 584cecbc-dbac-3c89-b6df-64df83024d2b | -2.95505 | -50.39558 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d73ed237-f180-3ce9-87a6-b1c557991ed9 | -2.92479 | -50.4155 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fcaabe35-06b1-3c81-b7fa-70a1208a39b5 | -2.8885 | -50.45209 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8c008935-6165-3188-afef-b45e4e7beac4 | -3.78257 | -51.34653 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ac8c7bd1-c350-3a50-8d99-d529611ffc6d | -2.89339 | -50.42115 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f2d995ea-d420-37c8-b0d2-6336409beddc | -2.95396 | -50.40246 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 89bb2694-1b30-3188-9757-9f402d39a58e | -2.93467 | -50.39592 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74817b3d-35fa-342b-903a-91272e4a3f43 | -3.1627 | -58.64159 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1d746ba6-f414-3b4e-92f0-5ca846a4a11a | -2.6298 | -51.76021 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db01ab9a-f0a4-394c-81fa-eb65c71ea963 | -2.87657 | -50.41811 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b5d63f4-909b-3c01-943b-b4d2481f982f | -2.91704 | -50.4002 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 29514245-7170-39b0-ab0a-415ba8e75768 | -2.89009 | -50.42064 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 99229d49-6853-3141-8a0c-088be4e8ef42 | -2.94132 | -50.41809 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bee3390-fa78-385b-b2bd-041571aacc49 | -2.91868 | -50.38989 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 796ea19e-6b96-3ca5-850f-dca73f8d9a5d | -2.95233 | -50.41277 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cdc97f78-22f4-356f-91c0-da9a3e6365d6 | -2.93965 | -50.40726 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77468be1-9403-3dfe-8fa3-e111b7187e42 | -2.89888 | -50.40792 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 58181c32-f49b-3645-bcff-c5d9139def4f | -2.90331 | -50.42271 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 08413fec-6aec-381d-82a4-bf938b472db3 | -2.89674 | -50.44281 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e93b1776-c756-3a53-8419-73b9d755e0df | -2.92202 | -50.41154 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 61f61a0a-eea9-3386-98ad-c10d4a0ca10d | -4.55537 | -50.45729 | 2026-09-14 04:51:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42778915-72da-3223-ab2a-8bbf4f14d1d2 | -2.87854 | -50.42939 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5d9ea270-9d21-3cf2-b8b0-f4291b89cd12 | -3.23016 | -43.03456 | 2026-09-14 04:51:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 214ffefd-491d-30c6-ad14-3f570f5eecd1 | -2.94463 | -50.41861 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b1c3b25f-9b7b-3f13-8a5f-b4c58383d4da | -2.86581 | -49.62809 | 2026-09-14 04:51:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a22241c-d52e-3415-a00d-bf2dbb1d8e98 | -2.89118 | -50.41376 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 19fc745e-005b-31f6-ad4b-e6eda6f86af8 | -1.19221 | -54.12296 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e26d2926-c756-380b-bbf2-04e833069f20 | -4.24601 | -48.64963 | 2026-09-14 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fe04f153-dc58-338e-8157-48c0a7727c66 | -3.16675 | -58.64711 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8b6946c3-d403-3ec4-a46a-659b325a11fa | -2.87439 | -50.43186 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cdea04f-dc3c-3540-bc64-d73ee7141fe9 | -2.90168 | -50.43302 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 24041922-2f58-3de7-9747-2201e615d4c5 | -2.94187 | -50.41465 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0b439e9a-1156-32d9-a557-67d28a9d7397 | -3.39319 | -50.76078 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7672c385-42b6-3fe7-8111-7b574fa23a2e | -2.91106 | -50.43801 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| 231d0e1d-ceb2-3396-a39b-0f489e265205 | -2.91658 | -50.44592 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fe5e81a8-8256-34bb-ac66-fa20be9d6214 | -2.90825 | -50.41291 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 3b9b9f02-819d-36a5-8ea4-802541339f48 | -3.75925 | -51.15098 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a8958049-36e3-3514-b76d-2835203d8961 | -2.90105 | -50.39417 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9eea4869-0159-35c3-9dbf-ac2576622336 | -2.88402 | -50.41616 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 14622c14-bf2a-3a48-8f0b-e623072d7e6c | -2.9088 | -50.40947 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 5c13abab-3e85-375d-a0db-3b0a7475660a | -2.92642 | -50.40519 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 30dabf0b-db79-31a3-ac59-a009e8b8d5e1 | -2.92257 | -50.40811 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 293bcc3b-94e7-3223-b7a1-0549396358aa | -2.89172 | -50.41032 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| cac0a8ef-f0c0-31cc-8902-ebf09c509943 | -2.91097 | -50.39573 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| f5851c88-7ade-3aa9-949c-1f7e2d63d242 | -3.04413 | -51.2696 | 2026-09-14 04:51:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24d39387-8b98-349c-b7b0-91c85dded8c2 | -3.39097 | -50.75338 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 583a0270-df4c-3c22-9c73-450eb09bda95 | -3.39073 | -50.39017 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 68e83320-74cd-3530-be19-ec280b7b364d | -3.11611 | -53.94798 | 2026-09-14 04:51:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1fd56899-94f7-325b-9cc2-3c40ba130bd7 | -2.91813 | -50.39333 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 6e59fd6f-6d9d-320c-a3ef-83a9e1c8631c | -3.54751 | -50.14996 | 2026-09-14 04:51:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7572d597-236c-3f5e-b5d9-e3e6dda4de3b | -2.93471 | -50.41705 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9d506d17-d34e-3f73-81ad-45c350e88fc8 | -2.91386 | -50.4631 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d62d24-7a1b-39fa-9bac-6b0cc91054a0 | -2.96719 | -50.40453 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1f8f8097-041c-399b-a57d-41077400c0be | -2.9386 | -50.43528 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb83ff30-7acd-3f0f-b7ba-aecba0d2fbb7 | -4.26841 | -48.6416 | 2026-09-14 04:51:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e663345d-993d-3408-a980-8aa637950a58 | -2.89561 | -50.42855 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| ccb24094-7863-379d-8269-2546a7e55325 | -3.37641 | -50.39498 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4a0e5f5d-58c0-3cae-9632-b7999853d68b | -2.82214 | -51.34166 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 33cea283-bcce-3e23-8e32-366437f43279 | -2.9116 | -50.43457 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| fce72f87-509d-31ae-8c57-4a0ec2db0ce4 | -2.88184 | -50.42991 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 048c1e85-a6c2-35c7-9e13-7e8a2d74632e | -4.34496 | -48.96092 | 2026-09-14 04:51:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0577da5-7ea2-30c0-9c2e-0af866b65f43 | -2.91876 | -50.43217 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c2a270d6-c1bb-3bab-8010-ccec9ac7f7e7 | -3.16572 | -58.65392 | 2026-09-14 04:51:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7223da5a-b76d-3def-a282-6dff19dbca9d | -2.89226 | -50.40688 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 92f87db5-cd68-3185-b5f5-52004c1da468 | -1.19906 | -54.19789 | 2026-09-14 04:51:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2f0f623d-7519-3926-ac44-c06e4ffd7aff | -2.93806 | -50.43872 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d25d2877-8477-3b93-a4e2-6036f92b96cf | -2.90277 | -50.42614 | 2026-09-14 04:51:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |


[Clique aqui para ver as próximas entradas](README33.md)
