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

## Dados Diários - Página 174

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef1f14dd-53af-37d9-8f04-0ef3c6863af0 | -14.9018 | -51.4965 | 2024-09-26 08:16:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 40.1 |
| d655232c-2722-3e3c-9d72-cd0a1987ce6a | -20.6074 | -51.5209 | 2024-09-26 08:17:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.9 |
| 8e0532c5-a450-34e1-9511-440d1bc64b0d | -7.2905 | -61.106 | 2024-09-26 08:25:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 460b8840-0e2c-3f24-ab5c-1e4435ce4805 | -7.8156 | -54.7252 | 2024-09-26 08:25:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 978b7f72-1c61-3b8f-a296-35a1f3aaefd2 | -9.1217 | -61.3334 | 2024-09-26 08:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.8 |
| 32acf079-bb5d-3ef4-9615-3c8114adb38d | -9.1216 | -61.3526 | 2024-09-26 08:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.4 |
| df7a2be9-2cdc-3966-be43-72ce1e25a116 | -9.1032 | -61.3343 | 2024-09-26 08:25:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| c56fe89d-1e4c-31f3-a425-c63cdcabebb3 | -11.2036 | -54.7548 | 2024-09-26 08:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| bfca7c90-4880-3cdd-bf73-77bd8148db12 | -11.2034 | -54.7752 | 2024-09-26 08:26:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 6d7ba8a7-15f5-3935-b5af-4e3bb137e32a | -11.2788 | -65.2793 | 2024-09-26 08:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 43.3 |
| d36d89f9-1267-3390-8f2f-6354b97c40b9 | -11.26 | -65.2801 | 2024-09-26 08:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 273329b3-e39f-30b6-9327-35a48c84cfb2 | -11.2599 | -65.299 | 2024-09-26 08:26:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 40.4 |
| b3d1b11f-25a1-3b36-bbd0-11373ed48e07 | -11.616 | -60.3463 | 2024-09-26 08:26:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 254f9851-1bb3-315d-8bc6-a46dd22ea523 | -20.608 | -51.4986 | 2024-09-26 08:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 82.9 |
| 25e37e2d-cff5-3833-b395-89111d36397d | -20.6074 | -51.5209 | 2024-09-26 08:27:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 165.4 |
| 2b413c0c-b2af-321e-b97e-32741d711b21 | -7.8156 | -54.7252 | 2024-09-26 08:35:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| 10700545-6162-3e21-bf2c-3cfdd14733ec | -9.1216 | -61.3526 | 2024-09-26 08:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 02756f85-e4c9-36ad-9767-37001df86df7 | -9.1217 | -61.3334 | 2024-09-26 08:35:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.7 |
| fd1dc273-bda0-3de9-b2aa-36f5fc9a6e18 | -9.2738 | -67.8471 | 2024-09-26 08:36:00 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| 2a9edc81-1b41-37cb-9db8-49e620b81a27 | -11.2034 | -54.7752 | 2024-09-26 08:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 123.8 |
| 9957a02f-afe9-302c-aec0-eeee1d534f7d | -11.2036 | -54.7548 | 2024-09-26 08:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 562a3d92-13ab-32c6-9f06-4ee7d53af38b | -12.8106 | -51.1502 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 54.2 |
| fdf8effa-e7b2-3855-93f2-6804c6fefa02 | -12.8294 | -51.1692 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 83.1 |
| a4db31a5-9f99-36e9-9bba-353dddb79cd3 | -12.8297 | -51.1479 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 120.4 |
| 9cb8f03c-6d21-345b-9b5d-79e0d8cfb4ce | -12.8486 | -51.1669 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 3dc282da-7106-343f-9afa-f157b8222eb1 | -12.8489 | -51.1455 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 61588487-8659-3252-bd60-13c93ad1012b | -12.8862 | -51.2049 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 4a2a1a0d-a4f8-3dc2-9423-563b12e5e065 | -12.867 | -51.2073 | 2024-09-26 08:36:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 60e2ea07-891f-3307-a0ba-76b843e5ce7b | -14.882 | -51.5207 | 2024-09-26 08:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 0aca7ef3-a2f7-3290-971b-97deffc57b1f | -16.0985 | -51.9896 | 2024-09-26 08:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 122.2 |
| 9e63c7ee-de44-384a-89c5-b3ae038b8b23 | -16.0989 | -51.968 | 2024-09-26 08:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 2c75cbf3-ec60-3178-88d6-157a8d7295f0 | -16.118 | -51.9867 | 2024-09-26 08:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 61.1 |
| fa8f1163-60a9-3b4c-8d57-d49e820b211e | -20.6074 | -51.5209 | 2024-09-26 08:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 108.0 |
| c248ea72-59c6-34ea-bea4-29ee27aac427 | -20.608 | -51.4986 | 2024-09-26 08:37:01 | GOES-16 | ITAPURA | SÃO PAULO | Brasil | 3523008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 70.9 |
| 5ecd8e76-15ee-3ba2-bd9b-044c6b50e339 | -7.8156 | -54.7252 | 2024-09-26 08:45:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 53d5f314-2093-3bea-bddb-ba7b45736059 | -8.9229 | -67.5965 | 2024-09-26 08:45:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 4ef657eb-3d31-32dd-b7b2-22bc0dabab04 | -9.1217 | -61.3334 | 2024-09-26 08:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 71497c07-9818-3188-8f51-e6490c133732 | -9.1216 | -61.3526 | 2024-09-26 08:45:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| eb1d6e31-51b5-342e-9a3c-5f8b0d3daf62 | -9.2738 | -67.8471 | 2024-09-26 08:46:00 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 41.3 |
| e269740b-7fad-3a9d-bf14-1d16eb97900a | -11.2034 | -54.7752 | 2024-09-26 08:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 101.7 |
| aee653b3-3153-3694-ad0e-7f3b0e5f1264 | -11.2223 | -54.7735 | 2024-09-26 08:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.7 |
| c092b885-576f-353c-8675-fba2f06e8813 | -11.5972 | -60.3475 | 2024-09-26 08:46:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| b164158b-bbeb-34fd-b7ea-e24765d6a821 | -7.2905 | -61.106 | 2024-09-26 08:55:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 26.8 |
| 00838486-89a6-3403-a107-eb2a1852f548 | -7.8156 | -54.7252 | 2024-09-26 08:55:51 | GOES-16 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2bf32ed0-616b-3dfa-8925-2f6d8d1fcfb8 | -8.9414 | -67.596 | 2024-09-26 08:55:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| d5b6833c-df57-3218-b7c6-c9e779d4dd6e | -9.1217 | -61.3334 | 2024-09-26 08:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| dd15d39a-7fbe-30a9-9c67-371d62d376c4 | -9.1216 | -61.3526 | 2024-09-26 08:55:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 3f4b9095-c4ee-32f4-8991-5618dd95c5dc | -11.616 | -60.3463 | 2024-09-26 08:56:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 64.4 |
| 40c445a4-c84d-38a5-849a-1d505306090d | -16.8231 | -57.4994 | 2024-09-26 08:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 49.9 |
| 56709ec5-7943-397f-9d94-456c20f00670 | -10.01 | -53.48 | 2024-09-26 09:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fabf502d-9ed5-33d9-abac-2c938b4d34a0 | -10.04 | -53.55 | 2024-09-26 09:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f287bff-1be3-3f23-9d96-28329091eed1 | -10.04 | -53.48 | 2024-09-26 09:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d12e21ad-bb8e-386d-8bbe-dd884431f301 | -10.04 | -53.42 | 2024-09-26 09:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eddf435b-8472-3489-88cd-921887299113 | -8.9229 | -67.5965 | 2024-09-26 09:05:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| 90bf05c6-20e4-392b-b1d9-cf9c4b9c44d0 | -9.1217 | -61.3334 | 2024-09-26 09:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| b2be772f-6c33-39e0-8510-981965747040 | -9.1216 | -61.3526 | 2024-09-26 09:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 4aefe123-1469-3e08-89f2-ef26ea8dbb8d | -9.1032 | -61.3343 | 2024-09-26 09:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 9547875b-88c5-3027-9182-c49e7d22c15d | -11.5972 | -60.3475 | 2024-09-26 09:06:13 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 59.3 |
| cad35b5f-2a38-37da-a20a-ed95a7124702 | -7.2905 | -61.106 | 2024-09-26 09:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8ce7f25b-4b3e-3c7d-8505-0c21a3b7c97e | -7.2906 | -61.0869 | 2024-09-26 09:15:48 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 06ad8c03-c22f-33ef-8af6-3b70de6851d0 | -8.9414 | -67.596 | 2024-09-26 09:15:58 | GOES-16 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 40.2 |
| d337ac2a-9a96-3c9c-9cd4-2777fce59f89 | -9.1216 | -61.3526 | 2024-09-26 09:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 37.2 |
| 95aeb144-bc3d-3a31-a169-8d5fc370e731 | -9.1217 | -61.3334 | 2024-09-26 09:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| d8341bf8-c5d8-3804-933c-237b7517bed6 | -9.1032 | -61.3343 | 2024-09-26 09:15:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 1ac708de-7e4a-3eb1-9c47-1808761dea1d | -14.882 | -51.5207 | 2024-09-26 09:26:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 6ca30d5c-17be-3b55-a222-5c0ee513831e | -18.999 | -41.0669 | 2024-09-26 09:26:51 | GOES-16 | CUPARAQUE | MINAS GERAIS | Brasil | 3120839 | 31 | 33 | nan | nan | nan | Mata Atlântica | 141.1 |
| 3f69a8ff-eacd-3e0b-bc47-d4474ca8b99e | -18.9998 | -41.0411 | 2024-09-26 09:26:51 | GOES-16 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 161.4 |
| f98bb7e1-e067-353c-9bbb-7bfa918ae651 | -11.2034 | -54.7752 | 2024-09-26 09:36:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.8 |
| fc4f6371-14ff-36a8-a5cc-bd92c4694af0 | -14.9014 | -51.518 | 2024-09-26 09:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 128.5 |
| 704f1b8c-a5b3-3759-82a4-a0de1739a835 | -14.882 | -51.5207 | 2024-09-26 09:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 180.6 |
| e75710bb-be8b-32c0-86db-cee1f0ce4991 | -14.8824 | -51.4992 | 2024-09-26 09:36:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.5 |
| c2c163d5-dee7-3948-aa23-e10a6f78d22a | -16.098 | -52.0111 | 2024-09-26 09:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 5ed05b29-fbca-38f6-a4ae-6e6ff03c8654 | -16.1176 | -52.0082 | 2024-09-26 09:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 196.6 |
| 81162c0d-bf51-387a-8285-a668bda19414 | -16.118 | -51.9867 | 2024-09-26 09:36:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 120.8 |
| b74142c3-6ac5-3f1f-a433-a0829df3aff0 | -18.9998 | -41.0411 | 2024-09-26 09:36:51 | GOES-16 | ALTO RIO NOVO | ESPÍRITO SANTO | Brasil | 3200359 | 32 | 33 | nan | nan | nan | Mata Atlântica | 142.3 |
| 97e23aec-fc48-3f04-90fb-51302fe850fe | -11.2034 | -54.7752 | 2024-09-26 09:46:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 122.5 |
| 620ed6bf-d5e3-3d04-8fe8-21cb6406f8e1 | -14.9014 | -51.518 | 2024-09-26 09:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 403f73a9-0e6e-37c7-b68a-3e452c71f735 | -14.882 | -51.5207 | 2024-09-26 09:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 147.9 |
| bb2f7b70-1c3b-3c6d-bbbc-de996a2dac35 | -14.8824 | -51.4992 | 2024-09-26 09:46:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 0fa61997-702e-3a65-8482-12d0e4d4af65 | -16.1176 | -52.0082 | 2024-09-26 09:46:37 | GOES-16 | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 687700a2-6e4a-3e96-9640-4d9655971433 | -16.8588 | -57.7197 | 2024-09-26 09:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 309.8 |
| be2a97d7-5140-3df6-9f5c-75d39884e278 | -16.8591 | -57.6993 | 2024-09-26 09:46:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 338.5 |
| 181837f2-5e44-32e6-8896-567e08c41d21 | -16.8784 | -57.7175 | 2024-09-26 09:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 321.2 |
| a4315aeb-c67c-39ce-9cad-0b259dedf7f4 | -16.8787 | -57.6971 | 2024-09-26 09:46:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 273.9 |
| 0b036501-aa9d-38a0-b105-978fbfae3d40 | -11.2034 | -54.7752 | 2024-09-26 09:56:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 111.4 |
| 07882183-1d37-3b08-a13a-a49dc0f592e4 | -14.8824 | -51.4992 | 2024-09-26 09:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 138.1 |
| b2c4ec5a-9d48-3a5c-97e6-a732b14fcdce | -14.882 | -51.5207 | 2024-09-26 09:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 259.7 |
| 57a47e0b-986c-3eeb-9c14-ff6bfc23c6f4 | -14.9018 | -51.4965 | 2024-09-26 09:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 183.8 |
| 161fa94d-0b69-3e3c-96e5-d39f87f90776 | -14.9014 | -51.518 | 2024-09-26 09:56:30 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 362.2 |
| 29303991-34b6-36c5-9405-3fa16a8eb666 | -16.8591 | -57.6993 | 2024-09-26 09:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 204.2 |
| 20d75cec-8a17-3127-ae97-80c945242cbe | -16.8588 | -57.7197 | 2024-09-26 09:56:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 174.0 |
| 323f17b2-9517-35f7-8356-2e57da12ab8d | -16.8787 | -57.6971 | 2024-09-26 09:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 193.7 |
| 6386ad76-aa56-3fc4-bdb4-a57c200f1bed | -16.8784 | -57.7175 | 2024-09-26 09:56:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 266.6 |
| f2b8cba1-4afd-36d9-8235-9489c14c0b1c | -10.01 | -53.48 | 2024-09-26 10:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc9777b4-712c-3167-89b7-7e42a30e058c | -10.04 | -53.48 | 2024-09-26 10:04:28 | MSG-03 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e446cadc-6548-3258-a32f-eb49a9d4713b | -11.2034 | -54.7752 | 2024-09-26 10:06:10 | GOES-16 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 104.7 |
| 89a45281-ece0-3365-a23e-8a515bc0a597 | -16.8588 | -57.7197 | 2024-09-26 10:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 299.2 |
| c505dbda-8647-366b-9692-232de72b9784 | -16.8591 | -57.6993 | 2024-09-26 10:06:41 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 266.8 |
| 0f2afb80-bbd2-3cd8-8dc4-32da7ae1e1a3 | -16.8784 | -57.7175 | 2024-09-26 10:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 544.6 |
| 1aabaa09-4d0a-384f-b1d2-bc4742f8df57 | -16.8787 | -57.6971 | 2024-09-26 10:06:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 395.5 |


[Clique aqui para ver as próximas entradas](README175.md)
