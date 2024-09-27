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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1637a2c6-55e2-356b-83e2-f5097a295225 | -12.8437 | -54.0422 | 2024-09-27 01:06:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 09a727c6-d503-3751-81dd-de1cc82ef993 | -13.2345 | -45.6476 | 2024-09-27 01:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 56.7 |
| bdf6acae-2cd9-384a-a46b-8424b10e5aad | -13.235 | -45.6245 | 2024-09-27 01:06:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 561d473a-4f76-3ede-ac7f-e19b78c43aa4 | -13.4413 | -44.0267 | 2024-09-27 01:06:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 84.3 |
| 51463b9c-a270-31e4-9fa4-ae34a8e79572 | -14.7109 | -45.5096 | 2024-09-27 01:06:28 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 0409be85-2e9e-30d0-8e5d-935e9a2e3b1a | -14.7305 | -45.5061 | 2024-09-27 01:06:29 | GOES-16 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 96c8766c-fcc3-36b4-b1fa-49c1172d95f6 | -16.7325 | -55.8445 | 2024-09-27 01:06:40 | GOES-16 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 60.6 |
| 4d7c75a4-9708-329f-8545-6f0c22fce186 | -19.6136 | -42.8159 | 2024-09-27 01:06:54 | GOES-16 | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 78.3 |
| fdd4ebe2-ca90-3221-815b-d7acb83a34e5 | -19.5266 | -47.8952 | 2024-09-27 01:06:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 58.7 |
| d6f69dda-22d6-34c8-88b3-d399c23dbbe6 | -19.5272 | -47.872 | 2024-09-27 01:06:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 71.3 |
| b45f6fa5-2664-3ff8-8672-3205b3a6e36a | -19.5469 | -47.8907 | 2024-09-27 01:06:54 | GOES-16 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 60.3 |
| 3004d077-a5f9-39f5-8d09-6bec964ea7a9 | -21.0986 | -49.1347 | 2024-09-27 01:07:03 | GOES-16 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.3 |
| 1e45eb8b-e0d7-3801-b878-5eda71199cce | -21.4123 | -42.9778 | 2024-09-27 01:07:03 | GOES-16 | DESCOBERTO | MINAS GERAIS | Brasil | 3121308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 84.1 |
| 3283ee8c-99dc-3e9e-af9f-c02e17647949 | -22.7442 | -44.7785 | 2024-09-27 01:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.7 |
| da56aa89-9215-3c9c-a2da-010305efc75a | -22.7433 | -44.8035 | 2024-09-27 01:07:10 | GOES-16 | SILVEIRAS | SÃO PAULO | Brasil | 3552007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 174.9 |
| 94207347-02d9-3ad3-9f78-5150046e8fda | -23.5816 | -47.3408 | 2024-09-27 01:07:15 | GOES-16 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 120.7 |
| 7498ab42-ffa5-386c-9d1e-40072f7acc68 | -2.6783 | -57.6087 | 2024-09-27 01:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 1b3700b1-ce0f-3707-a71e-cc3e74540043 | -2.6783 | -57.5893 | 2024-09-27 01:15:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 8336afe6-20c2-3392-b302-d40e0bf6a99d | -2.8611 | -51.6699 | 2024-09-27 01:15:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 79.4 |
| 8f7f47ca-a94d-3f21-bf93-ddbe306b610f | -2.8795 | -51.6695 | 2024-09-27 01:15:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 5a50436c-caf9-3fe8-b7ef-819203141114 | -3.0107 | -51.0652 | 2024-09-27 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 15734564-bdb8-3da6-92eb-e70c523ae83c | -3.0292 | -51.0647 | 2024-09-27 01:15:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 5daa1f9f-a071-37ce-b5f8-79c7f16ce933 | -3.2136 | -46.7843 | 2024-09-27 01:15:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 37795d78-2345-3482-826f-19d60d4b362c | -3.6437 | -54.051 | 2024-09-27 01:15:27 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 3e2df323-adf2-358c-9303-6254982ab857 | -4.5614 | -48.0141 | 2024-09-27 01:15:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f8ece88d-e7c2-3b3f-9c2d-341d33e3bbc4 | -6.1173 | -51.1185 | 2024-09-27 01:15:41 | GOES-16 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 64b42763-5b94-37ee-99b1-30e3c46190b6 | -7.0912 | -46.4412 | 2024-09-27 01:15:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 4ddf1cfb-3b85-3584-8f72-5b14c620706e | -7.1099 | -46.4396 | 2024-09-27 01:15:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| e775e798-0710-3566-be96-990d3c6c59f5 | -7.2006 | -60.6706 | 2024-09-27 01:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 8fe68b13-279e-33c9-a58a-d145ad1ab33a | -7.5289 | -61.3825 | 2024-09-27 01:15:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.3 |
| 3e3ceee9-27f7-355e-a9a7-3a57d1a8b728 | -7.5703 | -60.5984 | 2024-09-27 01:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 0709c2ee-9462-3818-8e47-a26a7597ef27 | -7.5887 | -60.5976 | 2024-09-27 01:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| e82d032a-2fd5-335b-b113-d8f6ac3cff84 | -7.5888 | -60.5785 | 2024-09-27 01:15:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 8acf7b7f-5a82-384e-85cc-13106165a0cb | -7.77 | -61.2015 | 2024-09-27 01:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 07ce4eed-e68a-3b70-923f-3c3574b1cf6b | -7.7701 | -61.1825 | 2024-09-27 01:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.9 |
| dc6f06c2-0026-3338-a415-c9063ecd5266 | -7.8156 | -54.7252 | 2024-09-27 01:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 152.4 |
| 1387afd5-d35a-3639-916a-ee83f58de84b | -7.7885 | -61.2008 | 2024-09-27 01:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| bf23eea3-e950-3de9-9d6f-9a60fcec02a2 | -7.7886 | -61.1817 | 2024-09-27 01:15:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 35178496-9b73-310c-b306-82765e0f3dad | -7.8341 | -54.724 | 2024-09-27 01:15:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 2c6a4765-d11d-3d86-8ca4-cb8241d33fe2 | -7.9174 | -61.2909 | 2024-09-27 01:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 22a5f9f9-11a8-3d26-aa44-168e1b4d29be | -7.9175 | -61.2718 | 2024-09-27 01:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.2 |
| 517c4590-8022-3f16-a3d1-2f440305a29c | -7.9359 | -61.2901 | 2024-09-27 01:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 58221c5f-f2c5-37f0-a446-b9e27bef0c28 | -7.936 | -61.271 | 2024-09-27 01:15:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| a2954f4e-3711-34cd-9551-d25c6d3ad34b | -8.1394 | -61.2817 | 2024-09-27 01:15:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 1ac15c18-f45e-387b-9a32-5960af8bd87b | -8.3153 | -55.0157 | 2024-09-27 01:15:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 3c219d51-e95d-332a-bda1-f888e138b432 | -8.556 | -49.6112 | 2024-09-27 01:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 98730355-5a6f-3033-863d-74c30cdffcf7 | -8.5562 | -49.5897 | 2024-09-27 01:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 7d504706-a0b2-329d-bb97-e9dea68535f4 | -8.5748 | -49.6095 | 2024-09-27 01:15:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 01418a85-5adc-31a7-8c82-e1b627305690 | -8.61 | -63.1415 | 2024-09-27 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 599f13ff-4093-3884-86fd-cf2f924e68e9 | -8.6101 | -63.1226 | 2024-09-27 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 158.9 |
| 425d0533-bddc-3035-a922-a432f288db91 | -8.6285 | -63.1408 | 2024-09-27 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 184016fd-961b-32e5-8eaf-ab6c77ee38f7 | -8.6286 | -63.1219 | 2024-09-27 01:15:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 7c81c5c9-aa4b-3d8a-9747-0c18f3241553 | -8.8116 | -67.6917 | 2024-09-27 01:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 92304e60-a04b-37a5-8952-26365678d000 | -8.8117 | -67.6732 | 2024-09-27 01:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 100.6 |
| 18871a64-91e8-3cc5-80dc-422f98d06809 | -8.8302 | -67.6728 | 2024-09-27 01:15:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| bec8bc9a-537a-3897-9501-e035a430e894 | -8.8588 | -61.8036 | 2024-09-27 01:15:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 2823b5f3-e734-38bc-882a-7e1a7c701c5a | -8.8589 | -61.7845 | 2024-09-27 01:15:57 | GOES-16 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 78815089-a4f7-3a02-82b3-c2b2bc820c2e | -8.9977 | -67.3909 | 2024-09-27 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.0 |
| ffe608f2-7131-3530-8bda-6514524b2991 | -8.9978 | -67.3724 | 2024-09-27 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 112.5 |
| aaddf271-08d1-363d-95d8-930ef9119b5c | -8.9978 | -67.3538 | 2024-09-27 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 05d6cfd5-19bc-320c-bf27-d086e48b52b3 | -9.0163 | -67.3719 | 2024-09-27 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| 2478bd3a-a2ea-3c6b-8ed3-891c3457076d | -9.0163 | -67.3534 | 2024-09-27 01:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 80669ae9-db10-3c87-8c92-be855f33e75e | -9.047 | -61.3943 | 2024-09-27 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 13f5f901-8c3a-378d-9968-04184f57d4ad | -9.0472 | -61.3752 | 2024-09-27 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 17a363e0-e99d-3db5-8e63-c57280887fea | -9.0656 | -61.3934 | 2024-09-27 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 62.9 |
| f70db903-975a-38af-8c01-39c51f637ff3 | -9.0657 | -61.3743 | 2024-09-27 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.7 |
| eb66bcdd-0c18-32bc-8af5-318a01031593 | -9.086 | -61.1245 | 2024-09-27 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 5bf1222a-526f-356a-a2d0-2686d1030825 | -9.1046 | -61.1237 | 2024-09-27 01:15:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 45636371-72e1-340d-8217-ae0a0d2ddb0f | -9.107 | -67.8881 | 2024-09-27 01:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.4 |
| d68143ad-f04f-3041-bb82-c0e4b89ce586 | -9.1255 | -67.8877 | 2024-09-27 01:15:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 1898270b-4ced-321f-8079-3c1f2262a902 | -9.5829 | -50.137 | 2024-09-27 01:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 58.2 |
| e3c57d9b-8251-373f-b84f-41e20d30ab48 | -9.6018 | -50.1352 | 2024-09-27 01:16:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 34536251-973a-31f3-9d51-654d0f79892d | -9.6149 | -57.7568 | 2024-09-27 01:16:01 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| e834156c-4e0e-3a31-8d77-84c1aaf0fbc5 | -10.3672 | -53.7858 | 2024-09-27 01:16:05 | GOES-16 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 95fb6f21-3fc9-3d6f-b6fc-dd3970aa055e | -10.6643 | -45.861 | 2024-09-27 01:16:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.4 |
| ab9d8c32-0903-3a8c-ab48-52e9fa23d19f | -10.9264 | -54.2692 | 2024-09-27 01:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 268.7 |
| e49b4e34-44bd-3a42-a620-3d48b80e29d2 | -10.9267 | -54.2488 | 2024-09-27 01:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 324.0 |
| 6b70f062-c7db-3af3-8bea-f7446c8a2890 | -10.9453 | -54.2676 | 2024-09-27 01:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.5 |
| 37ace064-541f-3634-96ad-552958345b19 | -10.9456 | -54.2471 | 2024-09-27 01:16:08 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 3072bf7f-fd01-3d29-8aa3-77b2517dc88f | -11.1409 | -50.8307 | 2024-09-27 01:16:09 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 75.6 |
| e2e0bb3b-86d3-3324-92ad-1021f48f7bf2 | -11.1349 | -54.1892 | 2024-09-27 01:16:10 | GOES-16 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 79.8 |
| 43725e10-139b-3282-bcdc-8178e57fdf3b | -11.5872 | -63.9596 | 2024-09-27 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 104.4 |
| c45c1be8-8623-3019-946e-0efc5c1db21c | -11.5874 | -63.9406 | 2024-09-27 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 75.1 |
| c6617629-a644-3d4e-8b81-7a22ffa479e0 | -11.606 | -63.9587 | 2024-09-27 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.2 |
| 406fabd1-43a4-314d-9c64-990a2a281eee | -11.6061 | -63.9397 | 2024-09-27 01:16:13 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e478efd2-19eb-342e-b5d2-86afb0da3d18 | -12.1672 | -50.8004 | 2024-09-27 01:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 140.2 |
| 0cf2c2bc-0969-3c57-801a-3e38dc94c122 | -12.1859 | -50.8195 | 2024-09-27 01:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 122.5 |
| a2332099-5639-3dfb-8f23-5380d9f27076 | -12.1863 | -50.7981 | 2024-09-27 01:16:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 178.6 |
| 122b54a8-ed43-3a74-a9f1-3d1487e30d77 | -12.6636 | -54.6782 | 2024-09-27 01:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 3c671487-ab1c-3844-b579-ae8cdd7b8a00 | -12.6824 | -54.6968 | 2024-09-27 01:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 136.0 |
| a00781cf-99d4-322c-9127-f1397c039fa7 | -12.6826 | -54.6763 | 2024-09-27 01:16:18 | GOES-16 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 134.8 |
| ea7c6031-b61f-36e7-9aa5-8494248ec494 | -12.8437 | -54.0422 | 2024-09-27 01:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 30b34f60-bd5e-3e42-b84d-065c7bad0886 | -12.844 | -54.0215 | 2024-09-27 01:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 44123bae-588d-37ab-a143-a6ed8732ca3f | -12.8628 | -54.0402 | 2024-09-27 01:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 8c110893-160b-3fa9-a5dc-1737cabda693 | -12.8631 | -54.0195 | 2024-09-27 01:16:19 | GOES-16 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 133.4 |
| 55cf69f4-7750-3417-96bb-f737d4985714 | -13.2152 | -45.6507 | 2024-09-27 01:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 44.9 |
| f064eb9c-eea2-3182-b944-4b57f01da5ec | -13.2345 | -45.6476 | 2024-09-27 01:16:20 | GOES-16 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 1c0047f4-09e1-339c-a274-81028c842e06 | -13.4413 | -44.0267 | 2024-09-27 01:16:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 81.5 |
| 4564993b-14a4-3d38-8d63-8166394e2a40 | -13.4418 | -44.003 | 2024-09-27 01:16:21 | GOES-16 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 17a2cae8-dd13-324c-a352-5d1bdfa4fc88 | -13.2105 | -51.2714 | 2024-09-27 01:16:21 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 89.3 |


[Clique aqui para ver as próximas entradas](README22.md)
