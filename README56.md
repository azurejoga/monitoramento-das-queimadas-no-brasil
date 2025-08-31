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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c0f3a41-1c7e-3845-a732-1018dbfb74e1 | -8.67305 | -62.41232 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb2c8923-1b88-3e1f-84da-375e4e0cbf69 | -9.06666 | -65.43129 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9ff613f6-6f40-3bc9-a7eb-6997b8691e21 | -12.52207 | -53.81872 | 2025-08-31 04:51:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6278f520-5e10-3415-a70e-af73ea95162d | -9.82411 | -63.85738 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 62c6cc42-8292-3bce-b44d-099568fa7ed4 | -8.35379 | -52.53261 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df0bc237-a11b-3927-a53c-4118fabefbe0 | -13.46639 | -46.97635 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d8378da4-a817-36a1-bff7-bb1e3caa1d66 | -11.0795 | -52.04126 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9060d823-f93b-35d8-b595-b53147a7b8fc | -9.59883 | -54.49345 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9870c14e-6ba7-3117-81d9-176f8968923a | -12.3999 | -46.47071 | 2025-08-31 04:51:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09df19a2-6bf2-3ce4-93e7-00b39d7c0574 | -11.2444 | -44.67992 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cba2de88-7324-3931-92fd-54f274f28a0d | -8.74045 | -62.39414 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a081c28f-d064-3c7f-8114-a70e22b72c39 | -10.08125 | -49.27544 | 2025-08-31 04:51:00 | NOAA-20 | CHAPADA DE AREIA | TOCANTINS | Brasil | 1704600 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3945f523-d0fc-3d30-a08a-53a7bdef825e | -9.24921 | -47.06475 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36387ad2-7468-315e-8cb0-90cc30e1d8cc | -8.65844 | -62.83252 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ec54483a-d436-30c5-b4d0-683a5b17100d | -10.96446 | -50.85802 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 99936d70-0553-3856-8cf6-3aae674945eb | -13.47052 | -46.98131 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 781376b5-9135-3a8a-8e6b-15e06910aaed | -11.06705 | -52.05456 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d7448df4-e858-36f1-ba53-c625332bc015 | -11.21969 | -48.45643 | 2025-08-31 04:51:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 509be679-f1c2-34f1-b20e-61f50e3573a0 | -8.66457 | -62.82997 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 438662ab-ca72-33ad-9e5c-c62948e578cd | -9.44097 | -62.34968 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5658f144-d988-3f52-a561-a19ff041cc59 | -8.6535 | -61.95604 | 2025-08-31 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4db2d8c-6ab7-36d1-94ed-79416e2a8edc | -10.31011 | -59.21152 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d71e41c-ef23-3f35-8385-fc7e0e243973 | -7.96739 | -46.4165 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 769f3845-8752-335e-890f-2aef20e0bd6d | -11.40899 | -63.24065 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1f09a43f-e964-35b5-9c60-ae399f0e7dbe | -13.51826 | -46.97957 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71a16694-e252-3cb1-9887-993be5aa9660 | -8.73207 | -50.37527 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ce5f362f-fa23-31da-b55e-00d1461822ea | -7.71264 | -50.2816 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff7aacac-743e-33dd-ae4b-fa76fbca3017 | -9.58718 | -54.48049 | 2025-08-31 04:51:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c95040d6-2419-3468-8492-cd56bfb06791 | -14.54188 | -51.96344 | 2025-08-31 04:51:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aedd6cf0-0857-356d-ad28-7b86ad3f62b1 | -14.35743 | -53.31675 | 2025-08-31 04:51:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61636e2d-e163-35a0-9307-949a96a9c182 | -11.65039 | -51.68709 | 2025-08-31 04:51:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7ad481e4-0cdd-39ae-a5ae-d924143f8a6b | -12.62665 | -48.20188 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f9767c7b-675a-3fc6-91ad-df929a86c2d3 | -10.74849 | -59.82438 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18fe5525-8689-3198-bb1c-fbfaa25cc321 | -7.09734 | -63.1377 | 2025-08-31 04:51:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97417dd9-e3f4-3752-b43e-54ec68262045 | -14.62996 | -48.06527 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 106cbc92-2583-37cf-8976-279c8f1675dd | -12.63199 | -48.1945 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fe0cc8ab-21c8-372b-a6bc-f86cff96e555 | -8.96975 | -48.19306 | 2025-08-31 04:51:00 | NOAA-20 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4ba1f839-7c72-3d67-92de-2ec72fec6901 | -7.71111 | -50.26813 | 2025-08-31 04:51:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a53e191f-6247-327b-8af1-cd38f48456b0 | -11.41399 | -44.68557 | 2025-08-31 04:51:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2af3fc8b-744f-330b-a752-758720ed46d3 | -11.81555 | -46.4365 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9fa8ed5d-4db0-3cdd-a9ae-e39a0f3e24bf | -11.91587 | -46.40734 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 89780bf3-5fa2-3224-b84b-c8d9cb5152e1 | -13.34428 | -46.98129 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22c0e656-e554-37ec-a049-ea10a10b839c | -10.61331 | -54.924 | 2025-08-31 04:51:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 82b4d357-561b-31d4-9ff6-0aee8d20ae52 | -8.73684 | -62.3935 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b8e53b20-97a0-3889-a373-8506745c6c8d | -13.01945 | -56.88798 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| da413f94-e3a7-3ff1-b7ee-0d76bd9505fa | -8.6718 | -62.41917 | 2025-08-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 13fff9f1-56e0-37d9-bbe6-da90d9563771 | -9.67477 | -63.17116 | 2025-08-31 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 99fcffff-80b5-37af-b6af-2701200f9211 | -10.96091 | -50.85748 | 2025-08-31 04:51:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4a067f12-4c02-37f7-ada0-d5666e1387f4 | -11.41821 | -46.91172 | 2025-08-31 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c7f3b5b6-ab0a-38aa-82a2-11d41fe6db43 | -13.00617 | -56.90223 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f58a9200-9416-3e51-9178-d9d74cdae4d5 | -14.26005 | -48.05414 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0572f3a0-6909-3775-a683-a514d18b87bd | -11.17931 | -55.02022 | 2025-08-31 04:51:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b1e92523-6338-39ca-a9fb-90be8d316b12 | -9.06871 | -65.42075 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 33a66bf4-b2b5-3d22-ae32-5ca5e58a72e0 | -8.39006 | -48.26899 | 2025-08-31 04:51:00 | NOAA-20 | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| af8e88c3-ce70-3f0b-adcb-4e213e36111d | -11.05177 | -52.04065 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4bbbf10c-1ebb-3381-98ee-93edd8f798d9 | -12.64257 | -48.212 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e9b3b8d-5b9c-36d8-86f9-6471080f4f87 | -13.37525 | -46.96135 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc36f518-f773-312f-a349-42491a3415a0 | -10.59984 | -44.32854 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7b375485-c80f-3a76-9eba-7b1699145d89 | -11.21902 | -48.45489 | 2025-08-31 04:51:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd810551-e8b6-3305-b4cf-6e66e1e0c8e3 | -12.43109 | -63.92913 | 2025-08-31 04:51:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| c70cd795-baca-3e65-8b81-26a3c5270f42 | -12.93485 | -56.98278 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d4ff7df7-f12a-3696-b75b-b3d434cee1cf | -13.48488 | -46.9427 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e319f7af-01d2-3582-ab44-2c030a1fb437 | -8.55956 | -51.30575 | 2025-08-31 04:51:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7527112d-6a47-312a-936f-d4722c2bb2c1 | -11.07893 | -52.04498 | 2025-08-31 04:51:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a2dd087-ec7e-312d-aa2b-c5cccf936a7a | -11.89488 | -46.72786 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 07cf6233-c44e-34df-9e02-45d0b467cbeb | -11.86174 | -46.48864 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2dfcb436-bd0d-362a-b33a-56643098fc93 | -14.22754 | -48.06363 | 2025-08-31 04:51:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1ecfec22-6f1e-38fa-99c3-27090acf8027 | -8.95598 | -50.00494 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 47cd68e0-03ab-33fe-985a-25c2634e141b | -13.34307 | -46.99109 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c84000eb-acc7-33ac-8b43-d90aec22ca92 | -8.28535 | -46.31544 | 2025-08-31 04:51:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82aecf27-1e7f-3c9e-b8d2-f61816843156 | -8.74393 | -62.38449 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 331b923c-7fe7-3a12-94e9-9e86b6986e76 | -11.88669 | -46.73032 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 42809ac7-e1b7-322e-afa1-5135b1f1ec10 | -11.87678 | -46.72152 | 2025-08-31 04:51:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 292aeccd-e0c4-35e1-9d04-b133d8f95336 | -8.88797 | -45.08978 | 2025-08-31 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11874036-8326-3da5-be36-cef757a1b146 | -9.45333 | -60.57361 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 09489cf9-d0c3-3b3d-a4b1-aba59a66f8fc | -9.44263 | -62.37001 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5704a5d-3b1a-3a1f-9930-ba75d22636b0 | -9.46304 | -62.34717 | 2025-08-31 04:51:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5b25d655-ac69-3b8a-aae2-87d99dc361fa | -11.05983 | -44.62233 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f981dbc-60a8-3f30-93ff-0eebe9ae3485 | -12.60635 | -57.01754 | 2025-08-31 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40f62847-b0c6-3357-8503-7774c3b77341 | -9.06768 | -65.42602 | 2025-08-31 04:51:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c1fead8e-7ade-343b-8490-e19742d0b597 | -11.21376 | -45.04247 | 2025-08-31 04:51:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9c0967ec-6b7e-3ca0-ac2e-2b2e533bccd3 | -10.75282 | -59.82503 | 2025-08-31 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c2887155-f281-32b0-b35c-fdcdde1a62a9 | -8.88798 | -62.38879 | 2025-08-31 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 1f81930a-3623-3630-b946-e31e2c7f5963 | -13.47734 | -46.96479 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d939c7e-b9b7-36cf-adc8-d7ee705dd4e1 | -12.85419 | -48.07979 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 75f134fc-8338-300c-82b4-6b11ed206c5b | -12.97789 | -54.75877 | 2025-08-31 04:51:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d1ccecf-3fa3-39da-858a-3945320c6c27 | -8.95898 | -50.00977 | 2025-08-31 04:51:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5074bcb7-3b2a-32a1-a967-4968d84af444 | -11.07785 | -44.60817 | 2025-08-31 04:51:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 348e32be-9b36-3365-8cd7-cac9f2d35803 | -13.48671 | -46.96597 | 2025-08-31 04:51:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2698b754-855d-3507-8940-92ba90e93838 | -8.66406 | -62.83045 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a983f7d4-377f-3db0-8a2c-ce4225ab3ae3 | -11.27877 | -63.2398 | 2025-08-31 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3551dc20-3e5c-3590-bcd6-6f01a72ac99d | -12.8752 | -48.08616 | 2025-08-31 04:51:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b6707871-1d72-38c2-93c1-7ef298842cf3 | -11.80154 | -46.45896 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6d06247a-d03d-37ee-9d81-c3540e16ce16 | -10.48497 | -51.62344 | 2025-08-31 04:51:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 751ff85b-f708-3923-a5ec-6fc7319a8e03 | -11.73012 | -51.76175 | 2025-08-31 04:51:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7bcf5cab-2f25-3a63-9b1d-058c5ba393d7 | -8.64637 | -62.83455 | 2025-08-31 04:51:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb5c40b7-f155-329c-ad7b-eaabc0f66997 | -10.03841 | -48.09342 | 2025-08-31 04:51:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2940687c-d779-324f-92d0-91f53708cb70 | -9.24981 | -47.06056 | 2025-08-31 04:51:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2461efb4-a2d0-3bbe-9e2e-7572ed02a433 | -11.42216 | -46.91677 | 2025-08-31 04:51:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cece20cd-6ba0-3d44-b78a-b32bfde621a9 | -11.90763 | -46.39663 | 2025-08-31 04:51:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README57.md)
