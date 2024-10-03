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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7bd4f9d1-c7b8-33bd-8dbb-0d6f676b5a8f | -12.5332 | -53.1003 | 2024-10-03 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 77e67375-fc8b-3e7a-942d-2962cd0f5f69 | -12.552 | -53.1191 | 2024-10-03 01:36:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| 2931eab9-947e-36f1-a3a1-b45a9f414f34 | -12.6295 | -63.1225 | 2024-10-03 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 30894003-4960-3fe1-8014-508f9642b4f6 | -12.6484 | -63.1214 | 2024-10-03 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 87.2 |
| b2ce96f5-f988-394b-972c-6265305db136 | -12.6486 | -63.1022 | 2024-10-03 01:36:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 7cd75edd-c295-3012-9d46-168f89c20964 | -12.8049 | -62.497 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 050c7d58-9867-3b2a-a2f5-6ec1d152d98c | -12.8802 | -62.5503 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| e5ecaec4-2ffc-340c-9387-8fc13c241ebb | -12.8808 | -62.4731 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 86f50821-c691-3d8f-aaa3-e0e0fd745183 | -12.881 | -62.4538 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 79.9 |
| b2036c60-bec1-3852-9d2b-e5176193e446 | -12.8996 | -62.4913 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 128.7 |
| a49baf62-99e1-373c-a514-a067f4237de6 | -12.8998 | -62.472 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 167.1 |
| ab2e5f6f-123b-3f81-ad4b-ef3c5cc00f7a | -12.8999 | -62.4527 | 2024-10-03 01:36:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.6 |
| 235d6367-251e-33a6-81e8-ce2f2b6f832e | -12.9167 | -62.7022 | 2024-10-03 01:36:20 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 2af78996-bb16-3ea5-bb66-3b520cdcd425 | -12.9741 | -62.6409 | 2024-10-03 01:36:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 92.0 |
| ca190ad7-9242-325f-9d92-84da08537102 | -13.5195 | -51.1467 | 2024-10-03 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 77.7 |
| 07c652c2-5c3e-3fec-a738-1461bb801839 | -13.5558 | -51.2704 | 2024-10-03 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.1 |
| 1792ee14-baf8-3efc-a23c-face83adb73d | -13.5562 | -51.2489 | 2024-10-03 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 203.4 |
| 28889093-46c7-3224-878b-49aa586b9f1a | -13.5565 | -51.2275 | 2024-10-03 01:36:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 68.3 |
| a7014c23-8d0c-3f2c-8e4f-b9dc74b74e05 | -15.65 | -47.2027 | 2024-10-03 01:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 218.8 |
| cc410d02-cfda-3899-987a-a60ab12d132c | -15.6505 | -47.1799 | 2024-10-03 01:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 107.4 |
| 3d4593d8-587b-36ab-a95f-2c6a411ec5c4 | -15.6697 | -47.1992 | 2024-10-03 01:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 5feca2c4-91a7-32da-ac60-c345ee882222 | -15.6702 | -47.1763 | 2024-10-03 01:36:33 | GOES-16 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 6ad1bf6c-9a2f-3775-b19e-b6ca2f45f454 | -16.7594 | -57.8328 | 2024-10-03 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 48.4 |
| 4349c6ed-0090-3642-ac37-901a6ba1c6f2 | -16.779 | -57.8306 | 2024-10-03 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 60.3 |
| 26dedbaf-c532-34ae-bd0e-4c356abeba0f | -16.7793 | -57.8102 | 2024-10-03 01:36:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 52.3 |
| 30817ee1-c1d8-3bf8-8ac9-eaa28153accd | -16.8983 | -57.6949 | 2024-10-03 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 63.7 |
| c75a3627-6587-337d-a7b0-9a1d55c12b4c | -16.9176 | -57.7131 | 2024-10-03 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.7 |
| e5f15e5f-5a04-38dc-99a0-196d03734c81 | -16.9179 | -57.6926 | 2024-10-03 01:36:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 58.4 |
| 3adb58ab-dd88-31dd-b7ba-92fb9ac817be | -17.197 | -57.3741 | 2024-10-03 01:36:43 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 50.8 |
| 3995b34a-873d-3fed-b6ec-66e06e3eb2b2 | -19.0337 | -43.2193 | 2024-10-03 01:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| 2cf1ca94-5f84-3705-b6ce-fb884833597b | -19.0344 | -43.1944 | 2024-10-03 01:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 142.1 |
| 83992466-237e-3e3c-b56f-81b4deead608 | -19.0548 | -43.1891 | 2024-10-03 01:36:51 | GOES-16 | CARMÉSIA | MINAS GERAIS | Brasil | 3113800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 728ce1a5-ad18-37c6-854d-d38cc9c68c9c | -19.3159 | -42.5976 | 2024-10-03 01:36:52 | GOES-16 | MESQUITA | MINAS GERAIS | Brasil | 3141702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 79.8 |
| 74054191-5ab4-3a8b-b565-415b73561ba7 | -19.8803 | -42.1132 | 2024-10-03 01:36:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| 316c5a1c-db96-38c2-a17e-aa90dcda5ebe | -19.8812 | -42.0877 | 2024-10-03 01:36:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 63.0 |
| 02f8481f-fbe8-3ab9-8275-6bcd0cc6da79 | -19.9009 | -42.1074 | 2024-10-03 01:36:55 | GOES-16 | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.4 |
| 9e8593ba-0f73-3b1e-bf60-606598df0bb6 | -19.9018 | -42.0818 | 2024-10-03 01:36:55 | GOES-16 | SANTA BÁRBARA DO LESTE | MINAS GERAIS | Brasil | 3157252 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.3 |
| 533d29fd-8b45-327e-95a3-569daa5e4303 | -21.3456 | -55.6841 | 2024-10-03 01:37:04 | GOES-16 | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 88.2 |
| ddf4a45f-26be-377a-b9bb-319f59676760 | -21.346 | -55.6626 | 2024-10-03 01:37:04 | GOES-16 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 114.1 |
| f1d43206-1548-3369-a949-f6d65aaf2629 | -22.0871 | -42.0819 | 2024-10-03 01:37:06 | GOES-16 | TRAJANO DE MORAES | RIO DE JANEIRO | Brasil | 3305901 | 33 | 33 | nan | nan | nan | Mata Atlântica | 111.8 |
| 898006ef-44b8-33e3-b869-852f720a8f33 | -22.3094 | -44.0633 | 2024-10-03 01:37:08 | GOES-16 | VALENÇA | RIO DE JANEIRO | Brasil | 3306107 | 33 | 33 | nan | nan | nan | Mata Atlântica | 111.7 |
| 5bcb737e-a368-3926-a201-3d3092687996 | -22.4452 | -46.8817 | 2024-10-03 01:37:09 | GOES-16 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 86.6 |
| dcb33f4b-dded-3d66-a9b3-50816e1a141c | -22.446 | -46.8576 | 2024-10-03 01:37:09 | GOES-16 | ITAPIRA | SÃO PAULO | Brasil | 3522604 | 35 | 33 | nan | nan | nan | Cerrado | 128.5 |
| eaf99386-9603-3591-896d-5806b6981e24 | -2.9616 | -54.6503 | 2024-10-03 01:45:23 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 49f2e005-67b3-32d9-bcb3-48d70d6e63f4 | -3.404 | -42.2858 | 2024-10-03 01:45:25 | GOES-16 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 28.2 |
| f5a99f8d-03df-35d7-ad55-f9e35f3daed5 | -3.4042 | -42.2621 | 2024-10-03 01:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| e60db05d-e5be-3a1a-8d18-b9b1af1dc774 | -3.4229 | -42.2612 | 2024-10-03 01:45:25 | GOES-16 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 058f1780-910b-3f4b-aa2e-2e6fa4ee5011 | -4.0949 | -48.4894 | 2024-10-03 01:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| a44a61e2-ba58-3d3c-965c-ac96f212704e | -4.095 | -48.4679 | 2024-10-03 01:45:29 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| c8c8efe7-676e-363c-943f-689bcc7167e5 | -4.5375 | -43.304 | 2024-10-03 01:45:31 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 97fe3aa1-5b7a-302f-96fd-ee8087da1ba4 | -4.5562 | -43.3028 | 2024-10-03 01:45:32 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| 49a8e732-8ed9-3e8b-83a0-0047b569f571 | -4.58 | -48.0132 | 2024-10-03 01:45:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| ca351f07-cae9-3f48-b20b-b8a0ba7fda69 | -4.9264 | -43.79 | 2024-10-03 01:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| 27ace9dc-89d7-3ba5-94ef-ea72812c9997 | -4.9265 | -43.7669 | 2024-10-03 01:45:34 | GOES-16 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 104.4 |
| d929dd8d-f6b7-3ec6-8f15-681958d9fc54 | -6.8777 | -59.0504 | 2024-10-03 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 4e93a818-27a1-3024-bacf-651ba2c3ed6d | -6.8778 | -59.031 | 2024-10-03 01:45:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 39.5 |
| 385ec9b8-c222-336a-85bf-4cdaefc6ef15 | -8.5925 | -46.5262 | 2024-10-03 01:45:54 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.5 |
| 9017a487-c2a0-33d0-aacd-6fa08b694883 | -8.8503 | -45.5313 | 2024-10-03 01:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 42.8 |
| 5a615a0e-a249-320f-9135-baadbd1cf691 | -8.8506 | -45.5086 | 2024-10-03 01:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 176.4 |
| 88c0a131-f447-3d6a-aa66-f16b78b556a2 | -8.8695 | -45.5066 | 2024-10-03 01:45:56 | GOES-16 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 41.4 |
| 786f54cc-1fcf-3281-ae98-7d403a835d3a | -8.8926 | -62.3348 | 2024-10-03 01:45:57 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 295a74f3-dac5-3624-8782-12a0b28a3b44 | -8.9791 | -67.4099 | 2024-10-03 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 58.9 |
| 5453ad18-138b-3571-b1c3-02ea6f9bba69 | -9.0149 | -67.7423 | 2024-10-03 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| dc575f90-ae4f-38c2-9c8a-6049a3749ec4 | -9.0515 | -67.871 | 2024-10-03 01:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| e5102d24-4b6c-3839-85b5-f803e199039b | -9.1566 | -61.6758 | 2024-10-03 01:45:58 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 22ead24e-8963-3ce8-ae98-385488306159 | -9.1752 | -61.6749 | 2024-10-03 01:45:59 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| bb82de37-4707-35e4-902e-e9b907c307e2 | -9.3839 | -61.0526 | 2024-10-03 01:46:00 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| c388861a-9486-38dd-aff5-cf5c3ad51fac | -9.4368 | -64.5419 | 2024-10-03 01:46:00 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 56d9b9e0-cd47-36dc-8de3-50fab38a6956 | -9.4679 | -62.4047 | 2024-10-03 01:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 35.3 |
| a15471d4-d5fc-3699-b0c5-751b0b6a5d5d | -9.468 | -62.3857 | 2024-10-03 01:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 56720814-02fa-3f20-b86d-6627e6b09051 | -9.4865 | -62.4039 | 2024-10-03 01:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 49.3 |
| d092fd7e-01be-3efc-979f-e9e3e075cf9b | -9.4866 | -62.3849 | 2024-10-03 01:46:00 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 57e17b9b-fd73-3579-b91f-141ea392e50f | -9.494 | -68.4895 | 2024-10-03 01:46:01 | GOES-16 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 38.9 |
| b3c096a8-e1d0-3586-9473-6690960c6ef9 | -9.7173 | -64.2302 | 2024-10-03 01:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 43.9 |
| d639ada8-f991-34dd-87fd-18830a102415 | -10.1802 | -57.2848 | 2024-10-03 01:46:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| eff14421-37b4-32e9-ae96-716cf74f108b | -10.1804 | -57.265 | 2024-10-03 01:46:04 | GOES-16 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| 8e23d2a2-ac65-3268-a4f8-6652c2c88b87 | -10.9579 | -46.5467 | 2024-10-03 01:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 37.3 |
| 5d2750f7-c47c-36fc-b866-030af3a8c3ad | -10.9769 | -46.5443 | 2024-10-03 01:46:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 714ab07d-e6f7-31fa-95b5-36e3b4b8d3da | -10.8942 | -63.8971 | 2024-10-03 01:46:08 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 1ca187a8-2d1f-39db-84d3-885c2ae3d2c1 | -11.2565 | -60.6019 | 2024-10-03 01:46:10 | GOES-16 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4e8af254-aa2d-3d50-bbd8-fb4853b9ef41 | -11.6742 | -65.0172 | 2024-10-03 01:46:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 64.5 |
| ef03f13e-4831-3252-9b2d-3a50e259d4c8 | -12.4038 | -63.0009 | 2024-10-03 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| 81a3a8f4-debf-3795-b5b6-e3327c4b121e | -12.404 | -62.9817 | 2024-10-03 01:46:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.7 |
| ef1305fc-02be-3820-9a22-00323a0f22f4 | -12.5329 | -53.1212 | 2024-10-03 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 5d4400ac-44d1-3ceb-bd18-8614be2585a4 | -12.5332 | -53.1003 | 2024-10-03 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 112.7 |
| 0b854aa0-1d9c-3ed8-a3e7-5c46124ab3e7 | -12.552 | -53.1191 | 2024-10-03 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 0499a697-92c2-3143-be81-7103bfca854f | -12.5523 | -53.0983 | 2024-10-03 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| a1ccbce5-9f08-3fe5-a26f-bac2041f4b91 | -12.6295 | -63.1225 | 2024-10-03 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 28f8fda9-fe64-3efd-b613-563ebd36a4ef | -12.6484 | -63.1214 | 2024-10-03 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 90.4 |
| e64d7fdb-5301-3568-b88e-da5599b3f7fa | -12.6486 | -63.1022 | 2024-10-03 01:46:18 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 04be2278-e396-39de-b254-19b25884c136 | -12.8049 | -62.497 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 36ee9559-be80-3942-894b-416debfaf773 | -12.8802 | -62.5503 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 69.9 |
| b518a4f2-781f-3688-ba2b-8de606a8c47b | -12.8808 | -62.4731 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 85.4 |
| eb41dc33-7254-33cd-83b7-a45b07a37c66 | -12.881 | -62.4538 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 4c52bf22-6785-3574-aae0-db758615f5b4 | -12.8996 | -62.4913 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 22047d65-d26d-37af-a888-dffe36da3b08 | -12.8998 | -62.472 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 159.3 |
| 8adb0a10-effd-399c-a684-41e3b75ccb38 | -12.8999 | -62.4527 | 2024-10-03 01:46:19 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 100.7 |
| c8425abc-bb67-3fb4-a723-92ffd1df0e57 | -12.9741 | -62.6409 | 2024-10-03 01:46:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| b4273fcc-19bf-36b6-8713-4a9272448508 | -13.5558 | -51.2704 | 2024-10-03 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 93741776-2ae5-3ca1-87e2-4d6fec48cf19 | -13.5562 | -51.2489 | 2024-10-03 01:46:22 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.6 |


[Clique aqui para ver as próximas entradas](README37.md)
