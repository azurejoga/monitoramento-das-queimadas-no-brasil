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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d55fd7e-f612-3963-835f-903ba3f132ef | -21.937 | -48.552799 | 2024-09-27 01:25:07 | METOP-C | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 63e68efe-adbf-370e-aafc-6dfe2bbc7c34 | -19.3867 | -42.569 | 2024-09-27 01:25:20 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 482ee3c4-37f3-3231-a737-e015ddb6c7cf | -19.377199 | -42.572201 | 2024-09-27 01:25:20 | METOP-C | SANTANA DO PARAÍSO | MINAS GERAIS | Brasil | 3158953 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 90d1a92b-d761-3311-bda0-5cabbb94922a | -2.6783 | -57.6087 | 2024-09-27 01:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 458c65c2-d3a3-3fa9-879e-e406702bd679 | -2.6783 | -57.5893 | 2024-09-27 01:25:22 | GOES-16 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| c44409cf-24c8-3f7f-b142-023e3df1ae19 | -2.8611 | -51.6699 | 2024-09-27 01:25:22 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 55a1f76e-0f15-3eaa-9a92-71927e30044d | -2.8795 | -51.6695 | 2024-09-27 01:25:23 | GOES-16 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 8ae9444b-12bd-38e9-b3f7-8f2715e7181e | -3.0107 | -51.0652 | 2024-09-27 01:25:23 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.7 |
| 83b24f63-8cce-3bca-a18b-39bed8fe070c | -3.2136 | -46.7843 | 2024-09-27 01:25:24 | GOES-16 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 9e5ff6ba-4bc1-3ede-88f3-1907e135c149 | -4.5614 | -48.0141 | 2024-09-27 01:25:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 6178031f-2872-3951-a410-45c1e0c230b8 | -19.981501 | -47.134102 | 2024-09-27 01:25:32 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| fbe45d64-4478-31c0-a386-91133c92a185 | -19.9863 | -47.151901 | 2024-09-27 01:25:32 | METOP-C | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 4af3b057-2276-346a-b7df-f09e935d11f0 | -19.5334 | -47.858601 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e9edc8ba-eaa9-3964-9186-e3b3fe15a91e | -19.5378 | -47.874802 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a52d17a6-56bc-3b1b-bc11-b769643cd1c6 | -19.5422 | -47.890999 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a9c69009-6cc3-325f-8209-60c5883d6b9d | -19.523701 | -47.8615 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e60643d-e12c-3ab8-a322-43cbc79df330 | -19.528099 | -47.877701 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 43eda198-bace-3e9b-b29c-cc0943ef47de | -19.532499 | -47.893902 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9ae972aa-929b-3d3d-b88e-368640324ca0 | -19.514099 | -47.864399 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| cf22371f-0170-37fd-bfb0-1e78195ced49 | -19.518499 | -47.8806 | 2024-09-27 01:25:42 | METOP-C | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 49d1ce72-2669-3592-b6ae-bf28acc355cd | -6.8199 | -63.1651 | 2024-09-27 01:25:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 229.7 |
| a7c46d80-eca2-3d09-956f-50686030c3a8 | -6.82 | -63.1463 | 2024-09-27 01:25:45 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 156.7 |
| e0247e16-369f-3702-97db-9cab7123df67 | -6.8383 | -63.1645 | 2024-09-27 01:25:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 76288396-0cfb-39bc-ad55-a5d8879bbb62 | -6.8384 | -63.1457 | 2024-09-27 01:25:46 | GOES-16 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 85.3 |
| f38ce664-387b-36a4-a537-6dcd9c835e0c | -7.0912 | -46.4412 | 2024-09-27 01:25:46 | GOES-16 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 82.8 |
| ff733244-72bf-36a9-a652-c720e21f7855 | -7.2006 | -60.6706 | 2024-09-27 01:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 3bf7472d-a413-3931-a224-54bb057ac522 | -7.2906 | -61.0869 | 2024-09-27 01:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 33947462-f1b1-3468-a568-0aed1fa85d59 | -7.3089 | -61.1053 | 2024-09-27 01:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 805bfb31-a504-35cd-a2a4-9dff080fc492 | -7.309 | -61.0862 | 2024-09-27 01:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 146.2 |
| ac848cb2-ff49-3583-a400-a1bc26ba03ec | -7.3091 | -61.0672 | 2024-09-27 01:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 6c80abbf-0229-3511-a89b-61ed1a547b5f | -7.5289 | -61.3825 | 2024-09-27 01:25:49 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| 5307f3fd-c782-3184-85ca-054792c69a0a | -7.5703 | -60.5984 | 2024-09-27 01:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 92719c1c-0c7d-3eee-abcb-fdcaebd8b6de | -7.5887 | -60.5976 | 2024-09-27 01:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a2e1f29e-93fa-3d2f-a07c-98b2198200b3 | -7.5888 | -60.5785 | 2024-09-27 01:25:50 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 4c5c2fad-031e-3b90-b705-bc4cc6efaf1b | -7.77 | -61.2015 | 2024-09-27 01:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 695fa92a-ac9a-3bde-a830-34c47eb662c5 | -7.7701 | -61.1825 | 2024-09-27 01:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 6c7f9cf6-858a-36cd-a536-6e16e3dd75eb | -7.8154 | -54.7453 | 2024-09-27 01:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| ce479174-1a61-394b-861d-4681917b78f9 | -7.8156 | -54.7252 | 2024-09-27 01:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 131.6 |
| ce8a0ea2-99a9-3210-8ecb-3497aa40aa89 | -7.7885 | -61.2008 | 2024-09-27 01:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0f40905e-a526-3bf5-8876-b0ef8d6f238d | -7.7886 | -61.1817 | 2024-09-27 01:25:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 6db4a603-114a-3adf-929f-f7c83b0f3f5b | -7.9174 | -61.2909 | 2024-09-27 01:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 4a58bf4a-e8c3-3001-9149-518e0fbfccd3 | -7.9175 | -61.2718 | 2024-09-27 01:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| 23fbcd36-eff1-3dbf-b687-ba8ffdecc5d7 | -7.936 | -61.271 | 2024-09-27 01:25:52 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 41f7388e-405d-309f-99e6-5a9a1cc14e29 | -8.1394 | -61.2817 | 2024-09-27 01:25:53 | GOES-16 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 69.8 |
| 1ff9a599-c0c9-34d7-ae0b-0f223c47a34b | -8.3153 | -55.0157 | 2024-09-27 01:25:54 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 427c4751-c5df-3a7b-ae1b-b4bd56a7d809 | -8.556 | -49.6112 | 2024-09-27 01:25:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 78424d78-8db1-344e-b25f-bc1c12d7a217 | -8.5748 | -49.6095 | 2024-09-27 01:25:55 | GOES-16 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 62.6 |
| dc36d35a-2c4a-3747-9769-ff80ed4a1dbc | -8.61 | -63.1415 | 2024-09-27 01:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 92ccec0f-499a-38f6-a6a3-ffc54a3136dc | -8.6101 | -63.1226 | 2024-09-27 01:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 103.5 |
| 6fc92879-bcb8-3c6c-b1a2-ad45753129be | -8.6285 | -63.1408 | 2024-09-27 01:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 137.1 |
| 0ca12dbf-e560-37f7-8220-81e28a14e92d | -8.6286 | -63.1219 | 2024-09-27 01:25:56 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 212.0 |
| ff3513df-40e7-3522-9dbf-4fc7d1ee567d | -8.6661 | -67.0287 | 2024-09-27 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.7 |
| bb340d07-ac1d-34ac-beb9-79f860d2f0ae | -8.7032 | -66.9907 | 2024-09-27 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.5 |
| b57b4a0d-f79d-3c9d-ad7a-d3d7b26cdedf | -8.7033 | -66.9721 | 2024-09-27 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 71.4 |
| ad4df926-935b-390f-b8bf-7ee8be3f4d2a | -8.7218 | -66.9716 | 2024-09-27 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 656efd8f-5394-3966-be94-b7b08689408b | -8.7219 | -66.9531 | 2024-09-27 01:25:56 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.9 |
| db9ad3c1-ad6b-30ba-90fa-95ca98a2fe00 | -8.7931 | -67.6921 | 2024-09-27 01:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 6bdec4f3-66c6-306d-84cd-889b146fcf7d | -8.7932 | -67.6736 | 2024-09-27 01:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| ec53d134-119e-302c-883b-106480efd5c9 | -8.8116 | -67.6917 | 2024-09-27 01:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 135.9 |
| 468b26d9-ff45-380e-8fd5-9ee2b3751cbe | -8.8117 | -67.6732 | 2024-09-27 01:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 4faf1485-4249-3e50-b813-fc791007eaaf | -8.8302 | -67.6728 | 2024-09-27 01:25:57 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 659d23c8-42f9-3db2-909d-211164982f2e | -8.9977 | -67.3909 | 2024-09-27 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| bbbb31b7-b526-35ca-b1b8-99b69749acc3 | -8.9978 | -67.3724 | 2024-09-27 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 184.4 |
| e081e38e-e131-31a5-b6c8-37226127a51c | -8.9978 | -67.3538 | 2024-09-27 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 106.7 |
| fc999cb7-b54a-3c21-b5d1-9fa6dfb583e7 | -9.0163 | -67.3719 | 2024-09-27 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 87.0 |
| b067d9b8-410d-3c94-ba45-adcda11f7aab | -9.0163 | -67.3534 | 2024-09-27 01:25:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| cf35c171-b3b4-3df5-a117-2c1223db65c5 | -9.0656 | -61.3934 | 2024-09-27 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b864962f-9a7a-372f-b8f2-26ff5a36e0dc | -9.0657 | -61.3743 | 2024-09-27 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 08eabdfc-2b85-3fec-a765-a55657be0269 | -9.086 | -61.1245 | 2024-09-27 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| e988386f-35e1-3bd6-a952-c57dcedf318a | -9.1046 | -61.1237 | 2024-09-27 01:25:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 864f7e60-80b6-3c0e-bb6d-de2024f22045 | -9.107 | -67.8881 | 2024-09-27 01:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| cda29487-8802-3ad0-bf21-1b2e9f9b96f4 | -9.1255 | -67.8877 | 2024-09-27 01:25:59 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| ae26f290-1393-35b5-997b-e927deb2f7cc | -9.3028 | -65.3528 | 2024-09-27 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 103d346c-2394-3292-812a-4960d2f947ea | -9.3214 | -65.3522 | 2024-09-27 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 8fcf5c81-9df6-340c-9711-16dc867bc934 | -9.3381 | -65.7255 | 2024-09-27 01:26:00 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 9a5423fc-1577-32a6-86c1-6308ff768da7 | 0.90735 | -51.99023 | 2024-09-27 01:26:00 | TERRA_M-M | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 7ec13887-2d55-3d12-b91c-2ec3fced85de | 0.90538 | -52.00416 | 2024-09-27 01:26:00 | TERRA_M-M | SERRA DO NAVIO | AMAPÁ | Brasil | 1600055 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 37f054eb-ce84-3abd-829f-72864e315e55 | -2.86206 | -53.31228 | 2024-09-27 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ae4d7f89-eaaa-37f8-9879-8befead432bc | -1.62421 | -54.77583 | 2024-09-27 01:26:00 | TERRA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 00fa5467-9f3a-35d8-b02f-e36ffb6a9355 | -1.18536 | -54.20775 | 2024-09-27 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| fd7101a9-d8c2-3cb2-9db4-0e5e8dca46be | -1.1784 | -54.15807 | 2024-09-27 01:26:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 61d69337-1fc9-35ca-a51d-d595fbf91a6d | -1.04524 | -53.35282 | 2024-09-27 01:26:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 487ed2ea-525b-3ac9-a17e-970cdd9494f5 | -2.94681 | -53.7005 | 2024-09-27 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| cbba1b0a-813d-345a-ba74-c9a221e2a8ed | -2.93739 | -53.70185 | 2024-09-27 01:26:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 23a2b3d2-306e-36c2-b9fb-6c327ff83a18 | -3.11869 | -59.13004 | 2024-09-27 01:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 64b26812-3776-32f9-a056-00caeefadbf3 | -3.12023 | -59.14145 | 2024-09-27 01:26:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 69bf3755-5dc8-3403-b504-5156357a0587 | -2.66114 | -57.52155 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| ea1dcb58-e93c-3f6d-9e76-77f3a6a83ca2 | -2.67156 | -57.59669 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.1 |
| f417c497-75c7-3e85-b031-5181c5998afa | -2.67286 | -57.60612 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 4b7b6843-d489-30fd-85c8-a5278e4ce837 | -2.67938 | -57.586 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 25.0 |
| 0ada1bc3-caeb-34e7-b957-90db0ad470e5 | -1.74469 | -55.2383 | 2024-09-27 01:26:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 2f1a7938-cafe-3cfc-bb8c-3f5762c9d2e0 | -1.45886 | -55.50443 | 2024-09-27 01:26:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 9a137336-d6fe-3136-849b-0d929f8dca72 | -2.7143 | -57.50788 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 4e3b31a4-2a97-3b44-bb1b-e41626999b8a | -2.71559 | -57.51725 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f63ae1fb-99c8-3d62-b0ab-3a7e5c0f4574 | -2.72341 | -57.5066 | 2024-09-27 01:26:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3836ba13-34ed-35fa-bf32-7d90f6079548 | -2.39366 | -51.28785 | 2024-09-27 01:26:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 18baeeeb-1b42-32c7-958d-78de9307c532 | -9.5829 | -50.137 | 2024-09-27 01:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 278d7a6e-efa1-3b0c-9ed4-e032174138b1 | -9.6018 | -50.1352 | 2024-09-27 01:26:01 | GOES-16 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 3f17bfaf-395f-331e-85e6-ac7047f726ae | -18.599501 | -48.800201 | 2024-09-27 01:26:01 | METOP-C | TUPACIGUARA | MINAS GERAIS | Brasil | 3169604 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| b3949154-4c05-38bb-9395-85b68246a4c3 | -9.949 | -60.2334 | 2024-09-27 01:26:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |


[Clique aqui para ver as próximas entradas](README31.md)
