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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcfd0e5e-e154-31c8-aa79-ce6f99c1a2b2 | -4.9515 | -42.9739 | 2024-10-10 00:45:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 7f98e89f-1a4b-393d-8fb2-7027ee435e4c | -4.9513 | -42.9973 | 2024-10-10 00:45:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 65.8 |
| 35fc5c80-8a7f-32f8-b8a3-234d60e3c2d0 | -5.2361 | -44.8018 | 2024-10-10 00:45:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 1a757ca2-963b-3953-b0fe-7296c1bd10d6 | -5.4833 | -44.2822 | 2024-10-10 00:45:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 6beb4b55-ac80-365f-bedb-41a1d80c3abd | -5.7152 | -43.4563 | 2024-10-10 00:45:38 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.6 |
| 8a3ff89a-08d2-33bf-b15e-24f0b2ccb25f | -5.9034 | -45.4353 | 2024-10-10 00:45:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 5b36b15f-272b-35fb-8c48-ac05b73370fc | -5.9036 | -45.4127 | 2024-10-10 00:45:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 9c08571e-7ed1-3e20-9f3e-626e51614a31 | -5.9223 | -45.4114 | 2024-10-10 00:45:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 1d7e6afd-4c5a-33c9-92e2-1545b266bd70 | -6.5218 | -60.0649 | 2024-10-10 00:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 7cc73053-56dc-3cf9-a03b-cf20cf4050d2 | -6.747 | -59.3259 | 2024-10-10 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 88a35d35-7eb5-35e3-a33a-70b033121d34 | -6.7654 | -59.3252 | 2024-10-10 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 141.2 |
| baec8ed4-5b19-3230-a1c0-9032854402f4 | -6.7655 | -59.3059 | 2024-10-10 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| fd7f383f-6f6d-33b2-b18a-ffef8ca8011d | -6.7798 | -60.0552 | 2024-10-10 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.8 |
| b0c20b3e-53b6-3e1e-a2b3-b1c06e1b51e9 | -6.7799 | -60.036 | 2024-10-10 00:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 4421b792-0e2e-39a1-8763-c0f252ba27f6 | -6.7839 | -59.3245 | 2024-10-10 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.5 |
| a5ca262c-20cb-3b32-848f-c2a26f63e77a | -6.784 | -59.3052 | 2024-10-10 00:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.4 |
| d2faea0e-5275-31aa-98f5-f62f2dbb1b0b | -7.0234 | -59.3725 | 2024-10-10 00:45:46 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| f16690b1-5c54-3858-97e1-3361a80a3a02 | -7.0416 | -59.4296 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 35450c5a-b90b-3f3f-9e96-3e001c621901 | -7.0417 | -59.4103 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.3 |
| e7e565ea-4844-33c3-a9f3-cf3b865a090d | -7.0419 | -59.3717 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| d537b142-68bf-38c4-b846-117f00e46583 | -7.06 | -59.4288 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.8 |
| daa53c73-a0bc-33e9-b94f-c7e76b110018 | -7.0601 | -59.4095 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 95d1ff07-9152-33de-9973-977e2561ead6 | -7.0785 | -59.428 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| 1b8f3907-605d-36c7-ad12-d010c87a175d | -7.0786 | -59.4087 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 179.8 |
| c7d297ce-67e1-3e23-8a19-2a720a5e03d1 | -7.1341 | -59.3871 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| c641f8fa-5a13-3053-b86d-92e76afe1a17 | -7.1346 | -59.3099 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 7193f3d2-d6e2-30bd-b84f-910f1aba1367 | -7.1347 | -59.2906 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 9fcdf841-e449-376f-b525-b715093a49ed | -7.153 | -59.3092 | 2024-10-10 00:45:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 42b9b990-b4a6-32bf-9d99-1063d6b0f79b | -8.6843 | -63.1009 | 2024-10-10 00:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 60.3 |
| bd7c885a-595a-3687-85f5-49d8104d0dbf | -8.6844 | -63.082 | 2024-10-10 00:45:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 62.5 |
| a88a2c4b-6ff2-360a-9759-f3d05c9e93f6 | -8.9111 | -62.353 | 2024-10-10 00:45:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 48.8 |
| db585971-657c-3aba-bfb2-a50838b333bd | -9.0084 | -61.6253 | 2024-10-10 00:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6f8b1032-8dd7-35cd-9c37-0d9cf24fca47 | -9.0085 | -61.6062 | 2024-10-10 00:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.4 |
| f5a7ea2b-a388-3258-a4f4-3e189437a602 | -9.027 | -61.6244 | 2024-10-10 00:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.1 |
| ace99d15-1fca-3bf4-a99c-f275a1613983 | -9.0271 | -61.6053 | 2024-10-10 00:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 63b2469e-c5c7-3107-ba60-1252eda7b966 | -9.0656 | -61.3934 | 2024-10-10 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.0 |
| d031efe8-ea48-361c-9736-9bf52a5113cc | -9.0841 | -61.4117 | 2024-10-10 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 6aeb42a7-5bc9-313b-95d8-889c7bc5aa44 | -9.0842 | -61.3925 | 2024-10-10 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 101.8 |
| b9f5a1f7-1a38-34fb-9eed-4991f2a14d7d | -9.1028 | -61.3917 | 2024-10-10 00:45:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 81fb489b-e6d8-352a-a44f-3b126808ea2b | -9.1221 | -61.276 | 2024-10-10 00:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 593ca79b-66fc-34d4-b0eb-89b466646469 | -9.4633 | -63.1451 | 2024-10-10 00:46:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| f9d04617-bed4-37d6-97ea-af2174c1af12 | -9.4818 | -63.1632 | 2024-10-10 00:46:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 33ddbe37-a56d-34dc-a022-31caacb922dd | -9.4819 | -63.1443 | 2024-10-10 00:46:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 162.4 |
| 393f2090-7a7c-38bc-aa05-6a43dd865d79 | -9.482 | -63.1253 | 2024-10-10 00:46:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 857ac149-75e8-391a-8b9d-0f84dcad684c | -9.5005 | -63.1435 | 2024-10-10 00:46:01 | GOES-16 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 9ff9f342-f3f9-38ab-a8ba-d6ff1c07562d | -9.9105 | -58.1313 | 2024-10-10 00:46:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 935224dd-39cf-34d0-a945-62f90cc1882e | -10.4287 | -60.9979 | 2024-10-10 00:46:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| cddea8a1-d22a-383a-a1d5-7f2a0284a3f3 | -10.5746 | -48.0178 | 2024-10-10 00:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 76.0 |
| f3157d20-a055-3f3c-b86b-3a1ddd789f35 | -11.0252 | -57.2436 | 2024-10-10 00:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ac9e222e-f36a-3918-b187-22ab0040541e | -11.0254 | -57.2237 | 2024-10-10 00:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 221.7 |
| bdf74b9b-6e74-3ca3-aa00-13eb856943ec | -11.0256 | -57.2038 | 2024-10-10 00:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 211.5 |
| 309b63e1-ce7c-32fc-b257-23c08ff5e0be | -11.0443 | -57.2222 | 2024-10-10 00:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 295.0 |
| 5677dda9-d261-3e3f-9aae-1389fbdf588d | -11.0445 | -57.2023 | 2024-10-10 00:46:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 256.8 |
| a5d052c0-c184-3b5c-a78a-e5a2e9e69422 | -11.2582 | -60.4079 | 2024-10-10 00:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 31e0f19d-4be9-3152-85f4-7b2e9d0f73f0 | -11.8188 | -58.8459 | 2024-10-10 00:46:14 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 49.3 |
| dced1cd7-de4a-330c-9902-a93b8fdd0a7f | -12.27 | -43.7289 | 2024-10-10 00:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 5895fbd1-99cc-3e80-9df8-31224ab4d18a | -12.2888 | -43.7495 | 2024-10-10 00:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 152.5 |
| 499b3d05-c801-3cbf-b974-6e0b9f9d29ae | -12.2893 | -43.7258 | 2024-10-10 00:46:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 250.4 |
| dfe1030b-0544-370f-b41f-0fcd7a14f2db | -12.1958 | -46.717 | 2024-10-10 00:46:15 | GOES-16 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 4e1dc840-81e0-35bd-9206-5426064efb27 | -12.3067 | -59.1641 | 2024-10-10 00:46:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 2cee832c-263f-39c0-8262-392faaa9f83a | -12.3254 | -59.1824 | 2024-10-10 00:46:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| 0920f5e1-83df-30a0-819f-a654c2c23ef3 | -12.3256 | -59.1627 | 2024-10-10 00:46:16 | GOES-16 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 5fd4cc63-6ac8-30ac-a515-522b00cb76ca | -12.4177 | -54.5797 | 2024-10-10 00:46:17 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1813644a-3060-3835-8c00-d8c539656fe3 | -12.663 | -54.7193 | 2024-10-10 00:46:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 281a78e6-3594-3bb3-bde0-d9c848ee4d2d | -13.8179 | -44.549 | 2024-10-10 00:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 77.7 |
| bcc01d4e-08d7-39e0-8fa7-1a478ad74421 | -13.8184 | -44.5254 | 2024-10-10 00:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 98.1 |
| d0b39d11-bd15-3c1a-a80a-f0f43deb283e | -13.8374 | -44.5455 | 2024-10-10 00:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 1436e91e-c6d1-32e7-b4ab-6b3067a58596 | -13.8379 | -44.522 | 2024-10-10 00:46:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 151.3 |
| 8e6999d4-4572-363d-8fd6-48bbb21f9787 | -13.8569 | -44.5421 | 2024-10-10 00:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 85.8 |
| 1b960218-c2fb-3ec2-a92d-ae8f475f17f7 | -13.8574 | -44.5185 | 2024-10-10 00:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 5c8df197-412d-36aa-a05e-2ba4587f833c | -13.7346 | -60.6079 | 2024-10-10 00:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| f7047420-944d-37e4-a50e-88f44f56f0e3 | -3.2571 | -54.1824 | 2024-10-10 00:55:25 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 3f13cbb3-bfa7-30fd-b443-7a5d53bff725 | -3.3341 | -53.232 | 2024-10-10 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 366b7e2c-7597-3789-9a57-1983a3894a9e | -3.3342 | -53.2117 | 2024-10-10 00:55:25 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 3d44689e-ed5c-3f44-9cc1-01131cbb6ad9 | -3.4677 | -44.2834 | 2024-10-10 00:55:26 | GOES-16 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 53.5 |
| 5c69714e-f886-3ca0-99ec-ba3d7822ec53 | -3.706 | -44.9782 | 2024-10-10 00:55:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 33d0cbe5-1872-36cd-b091-8b280b69e630 | -3.7061 | -44.9555 | 2024-10-10 00:55:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 61.9 |
| eb9964d7-7766-333a-bd48-bbab9e2699e6 | -3.7246 | -44.9773 | 2024-10-10 00:55:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 34559e65-7a57-3fc4-9c83-64adf8acef4b | -3.7247 | -44.9547 | 2024-10-10 00:55:27 | GOES-16 | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 101.6 |
| 1f6d3fe2-3a18-3923-aca3-3202e111e663 | -3.7961 | -45.4927 | 2024-10-10 00:55:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 839201bf-9e12-393b-9bb0-d446627dc33d | -3.8146 | -45.5143 | 2024-10-10 00:55:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 82aacbf6-05d7-3e77-bc82-59d888fcc7e3 | -3.8147 | -45.4918 | 2024-10-10 00:55:28 | GOES-16 | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 66adca95-f69a-346f-b9b8-824cf6765a88 | -4.0814 | -51.0292 | 2024-10-10 00:55:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 2debac27-ee43-3785-b7e3-3bb0944a45e3 | -4.0961 | -48.2739 | 2024-10-10 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 141.3 |
| 4ad433fd-1bf8-32f3-b551-0a7349af6f66 | -4.0962 | -48.2523 | 2024-10-10 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 115.7 |
| 4369ce59-1ea9-370d-ba79-93b7085ad0cc | -4.0998 | -51.0285 | 2024-10-10 00:55:29 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 6363e8ab-3dfb-3669-9cac-31e56d580187 | -4.1146 | -48.2731 | 2024-10-10 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 264.3 |
| daf54293-5165-389d-a27e-17708ff5fad2 | -4.1148 | -48.2515 | 2024-10-10 00:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 200.3 |
| bf823ade-dfec-329d-9f1e-2c58d4c8417f | -4.4776 | -46.5956 | 2024-10-10 00:55:32 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 8ec03481-2406-356b-a594-b466addac700 | -4.9513 | -42.9973 | 2024-10-10 00:55:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| c696bc3f-9184-37b8-b422-e84ef416f779 | -4.9515 | -42.9739 | 2024-10-10 00:55:34 | GOES-16 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 397ccda5-a257-389e-b3b0-d92d0e59b371 | -5.2361 | -44.8018 | 2024-10-10 00:55:36 | GOES-16 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 56.5 |
| c2768621-33ea-3787-9031-1dec39d5de95 | -5.4833 | -44.2822 | 2024-10-10 00:55:37 | GOES-16 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4f93e95a-e2f1-3c7d-990c-9545ab99473a | -5.9034 | -45.4353 | 2024-10-10 00:55:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| fe04fe6a-0d0c-31b2-aa4d-59d780c744aa | -5.9036 | -45.4127 | 2024-10-10 00:55:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 120.2 |
| c92b0997-beec-3617-a201-e1206c513bae | -5.9223 | -45.4114 | 2024-10-10 00:55:40 | GOES-16 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 69eed0d9-9a4d-3636-81ce-0ec4e6bfd0d7 | -6.4021 | -52.7159 | 2024-10-10 00:55:43 | GOES-16 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 5f6db44f-b3a9-3800-b633-ab9d2105be20 | -6.5218 | -60.0649 | 2024-10-10 00:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 517e6587-9f0e-390c-9c4d-a3879900471a | -6.747 | -59.3259 | 2024-10-10 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 98e2240c-225c-3daa-8942-6e7359149dca | -6.7654 | -59.3252 | 2024-10-10 00:55:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.9 |


[Clique aqui para ver as próximas entradas](README18.md)
