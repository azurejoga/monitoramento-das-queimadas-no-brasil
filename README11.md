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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61e53ec3-a97d-3db2-bdf6-7164b016c1f7 | -2.7354 | -54.1189 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fda45a6-faf6-3911-b2bb-40e95d16ed23 | -2.7289 | -51.821098 | 2024-11-20 01:02:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e88f336-6189-3380-b98d-b40b5c9585b1 | -3.8096 | -47.811798 | 2024-11-20 01:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 432db275-0e06-34bf-b6b2-465750f49619 | -1.437 | -47.1077 | 2024-11-20 01:02:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44104c02-23f6-320a-9a88-ce4618553e5b | -2.5809 | -51.716702 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12263699-56ee-3bf7-a1ae-bfdb808d935f | -1.451 | -47.123798 | 2024-11-20 01:02:00 | METOP-C | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5e262c62-097d-3ecd-b8df-fe2ddf8af41c | -2.8942 | -53.065201 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2636bd14-4c66-3786-aaa2-29e348c9644f | -2.9058 | -53.070499 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d00fab9-fd90-306d-a89c-58b5b0744d7a | -2.7436 | -54.064999 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ccf37df-dc9e-36bc-b9e0-91addcfa92ff | -3.2079 | -53.8414 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914e105f-219f-3cb9-b8b2-35781356b0ad | -17.114799 | -57.494801 | 2024-11-20 01:02:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a2739446-5e35-3390-840d-b42d7d5d285d | -3.0949 | -53.7542 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d43b410b-16d3-39eb-8113-0714531b9bcf | -3.806 | -47.7967 | 2024-11-20 01:02:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 962efc1c-1b22-3df9-8cca-6664d62ca543 | -2.2969 | -48.490002 | 2024-11-20 01:02:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 93c2f953-9c64-3a44-8bc7-a72fc2106aba | -23.2687 | -51.4035 | 2024-11-20 01:02:00 | METOP-C | ROLÂNDIA | PARANÁ | Brasil | 4122404 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 16b405b0-14a4-3fb0-8ec5-33d1c50d2ce2 | -2.7954 | -51.7967 | 2024-11-20 01:02:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e292868-f2c1-3838-aa9d-17d7acb25718 | -3.5054 | -53.7892 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21f10f1f-75b7-32cf-bcea-3476afdcc0bf | -1.9916 | -46.5993 | 2024-11-20 01:02:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9bb82a24-3202-310e-93df-44501532f6c6 | -2.742 | -54.057999 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91c2583b-b4a9-31cb-a2bb-a0121bbdfc05 | -22.298599 | -49.7561 | 2024-11-20 01:02:00 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a991dcf2-be34-34bb-80c6-da2626cdbc96 | -2.9138 | -53.060699 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f8a7312-fc10-3d1f-9980-35a16e5dca7c | -3.2798 | -53.840099 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b80d53e-ea36-31f9-aac2-ca0da09eb6bb | -2.6209 | -51.7999 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 273030a3-4e01-398c-a128-bc1dcc78bb8b | -3.3977 | -50.1017 | 2024-11-20 01:02:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b07eda3a-591d-389f-bec7-8bab5fb392f2 | -1.8624 | -47.824299 | 2024-11-20 01:02:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a682ac99-506f-382c-81e8-f0fefc59c89c | -14.3021 | -51.506599 | 2024-11-20 01:02:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 48797f82-f5a0-36b9-a10f-72476409c466 | -4.3721 | -47.757401 | 2024-11-20 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef677561-27df-3242-97b6-7d05c7584ae1 | -12.2392 | -53.227001 | 2024-11-20 01:02:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2dc40c6b-7772-3e0f-b91d-7c2357a0d597 | -4.15 | -43.9632 | 2024-11-20 01:02:00 | METOP-C | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 514c0b25-7775-3dca-a4b8-21553b75e261 | -2.7282 | -51.729401 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 081d2a2e-2913-3779-9756-1e5ad4899865 | -3.1361 | -49.125801 | 2024-11-20 01:02:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40dd94b5-e1c8-37ce-a37d-17c8cf90fa49 | -2.9943 | -45.4538 | 2024-11-20 01:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 00104d54-e4d8-30ec-bbcb-f8b61afefda9 | -22.5054 | -46.387402 | 2024-11-20 01:02:00 | METOP-C | BUENO BRANDÃO | MINAS GERAIS | Brasil | 3109105 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b13d4f23-824d-3cd0-96eb-098e85d44aaa | -2.8122 | -54.094101 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e658b19-959a-3a52-b234-1149b9e49973 | -3.1263 | -49.128101 | 2024-11-20 01:02:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 83257ba8-3fde-3ecf-8506-aeb619f3d8c5 | -11.0813 | -54.631302 | 2024-11-20 01:02:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7360b3d5-b36b-374c-8c9e-f1de8f1ce059 | -3.2666 | -45.144901 | 2024-11-20 01:02:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f529bfbc-5f73-33ef-a028-50a20ecbe8b4 | -12.2376 | -53.220001 | 2024-11-20 01:02:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8be0e74f-fece-31c7-8d60-508aa8362de8 | -2.994 | -51.014198 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d5097921-32d3-3070-9153-a391fa2eb397 | -2.6131 | -51.810799 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| baecb8ed-4c87-3a2a-a887-9f6399bd8172 | -2.7829 | -54.0117 | 2024-11-20 01:02:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44f17040-90f2-3f48-a7a8-469ac6dbf3d4 | -4.5489 | -48.021702 | 2024-11-20 01:02:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e33467a0-4a1e-33c3-9943-b12563a95201 | -3.0203 | -51.523102 | 2024-11-20 01:02:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d8f1896-5756-32ae-ad93-c155d0d4cdd1 | -3.3313 | -53.303902 | 2024-11-20 01:02:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bd2931d6-4c7b-3175-be44-ec597616c03c | -3.7749 | -44.055302 | 2024-11-20 01:02:00 | METOP-C | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7f77d11c-01df-3a10-acf6-ac17a01ea376 | -4.3854 | -47.769901 | 2024-11-20 01:02:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e1b0f24e-72c7-323d-a9de-bf82f7d82c17 | -22.300301 | -49.763599 | 2024-11-20 01:02:00 | METOP-C | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f96e6803-1f4a-3c91-9998-46813a44bec4 | -3.3498 | -54.098701 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32c8df07-3723-3f71-8c08-4fa86a0fa33c | -2.817 | -45.101898 | 2024-11-20 01:02:00 | METOP-C | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 54e4c305-a7ae-3cb9-ab43-09ca6f423e79 | -2.7262 | -51.720699 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16d3c3fa-bbd3-3e22-8d48-ff3b24510aef | -3.0299 | -49.4599 | 2024-11-20 01:02:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5ceb52eb-da42-3555-b78b-b0c795d704f1 | -2.2602 | -45.459 | 2024-11-20 01:02:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0ace6fbd-eb1b-38d6-9a34-f8c3ac38a7f3 | -3.6708 | -52.366402 | 2024-11-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9284420f-4d03-371b-be7e-b398413707a4 | -2.9888 | -45.431198 | 2024-11-20 01:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d1a1ceb-7c5c-3cbd-8fcd-4bb8c051f8a3 | -2.2054 | -46.466301 | 2024-11-20 01:02:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 615f7458-fb5a-3ed0-83cc-6ae76b613e25 | -3.103 | -53.6996 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 266fdb04-78e5-3b0b-8be1-5134104b8bc2 | -3.0398 | -54.410099 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f1c0f43-3915-38fb-97ea-14e2988bc4b8 | -2.9984 | -45.428902 | 2024-11-20 01:02:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| defc6963-d684-396d-8271-30fd8160a1cc | -3.2935 | -50.359001 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47220757-a86e-31ac-a52b-249bd7189406 | -3.0016 | -51.002499 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92c92afb-3134-3e84-ab27-f6eeca3a7864 | -2.8131 | -45.128201 | 2024-11-20 01:02:00 | METOP-C | PALMEIRÂNDIA | MARANHÃO | Brasil | 2107605 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b8629481-cfc5-39f8-88fd-1015f271e34e | -1.7688 | -46.136398 | 2024-11-20 01:02:00 | METOP-C | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5d42fe39-a0d3-396f-a71c-7354b5ccf15c | -3.2608 | -45.121399 | 2024-11-20 01:02:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 12ca2c81-9e67-3b19-8019-a03e7ddc4f96 | -3.1856 | -54.326302 | 2024-11-20 01:02:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9e019de-6130-34bc-84dc-36b8349675ff | -3.0933 | -53.747101 | 2024-11-20 01:02:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c940213-0947-331b-b2bc-9df2a12b1701 | -2.6091 | -51.7934 | 2024-11-20 01:02:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c253fcc-dbca-30f9-b5ce-bf11e1fd75c4 | -16.8713 | -57.498901 | 2024-11-20 01:02:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6c9dab20-fde1-3a30-a2c7-422051a2d316 | -3.257 | -45.147202 | 2024-11-20 01:02:00 | METOP-C | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 73bf567f-e305-332a-868a-ea6c66cb644b | -1.9962 | -46.618801 | 2024-11-20 01:02:00 | METOP-C | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3ad4799c-18ef-3f35-adeb-b3f20986ef53 | -4.2312 | -53.669998 | 2024-11-20 01:02:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ef55ac7-f66c-3839-b512-8ad4c6b79eee | -2.3002 | -48.5042 | 2024-11-20 01:02:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28e9a1c-3a7b-3c05-b2bd-ed820880e2ff | -1.6155 | -52.620701 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc3c462d-7568-3ef5-9329-73dd55152bdd | -0.9449 | -51.7271 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 758e5f75-bc98-36af-96a4-a07cd835fb9d | -1.2615 | -53.409401 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce4fb000-f194-3723-9732-210a1a6140b9 | -1.1911 | -53.6852 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7fbbcb-578b-3437-b551-93bb44afb0b1 | -0.7645 | -51.748299 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 663dd04a-ed52-369b-9a0b-e2a428cc0cd8 | -1.5992 | -52.416698 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76227a66-f50c-3a98-a91b-b9cd4a327875 | -0.1054 | -51.435299 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 684d36f5-a659-3d9c-8324-bca982e93f07 | -2.2632 | -53.637501 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95e196b6-0181-32f8-8b29-6841dff93982 | 1.5616 | -55.757 | 2024-11-20 01:04:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71568349-16de-386a-af3f-8334db2b88e5 | -1.1399 | -53.508202 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2776c4f5-3744-381e-91f2-8fab77ee5322 | -1.2937 | -52.255001 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20747886-0010-3768-99e0-bcb6cbf23392 | -1.1236 | -53.661201 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8061fdd5-c961-37da-9d15-c3d98317bea3 | -1.1913 | -51.767899 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e82583-acd4-3041-a803-c36ad7f11f86 | -1.2424 | -51.7659 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd4327ec-14c9-3b99-87f2-34ff70a650a8 | -2.5882 | -54.0182 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3216fa5-84fc-3a7d-9932-a55ab4778927 | -2.3286 | -54.772701 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a97766f3-081a-3dec-91bf-c81f363f9faa | -2.273 | -53.6353 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed2cd9c2-4e1b-3d44-94da-2224ec4c16d1 | 1.5468 | -55.911598 | 2024-11-20 01:04:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9b2b095-2091-37dd-a7be-88ed9700668f | -2.2404 | -53.673302 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c54a6fa-ca1f-33ad-81f3-c71d5f97c294 | -2.1793 | -55.0653 | 2024-11-20 01:04:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3250db0a-6fe7-3852-9d45-c8c753565b3f | -0.7667 | -51.757599 | 2024-11-20 01:04:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bceeb7fd-c6bd-37d7-a64a-50cd1a8544c6 | -1.7189 | -52.800499 | 2024-11-20 01:04:00 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86b023c1-08e9-3798-afd5-8c0ab434bfa7 | -1.1859 | -53.662899 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 38ad2357-bd16-34f2-b1d8-6f81b3e95b9f | -1.8717 | -50.973202 | 2024-11-20 01:04:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eebe69e8-9a08-378f-a8d8-3d662ee3004b | -2.5817 | -54.034599 | 2024-11-20 01:04:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72824d46-af4a-3fc4-9810-d9cdaddfe876 | -0.8721 | -51.723999 | 2024-11-20 01:04:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4bd68b97-b452-335a-acc9-32988080edef | -1.2977 | -52.405701 | 2024-11-20 01:04:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5c8c90-5973-3a9e-b8f4-6aefc7555aa9 | -1.4696 | -54.447201 | 2024-11-20 01:04:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0320c72d-ff3a-3fbd-87b3-44c345ad047a | -1.1309 | -51.685101 | 2024-11-20 01:04:00 | METOP-C | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
