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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6344ba1-5888-3895-b477-e641b64bc820 | -3.1607 | -50.4556 | 2024-10-11 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3b905600-f249-3c14-a0a7-f560ec29c096 | -3.1608 | -50.4347 | 2024-10-11 01:45:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 2b8f4031-876f-3d59-ad47-2906d70fee37 | -3.3096 | -50.1781 | 2024-10-11 01:45:25 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 9d6feb90-8e67-35be-b1a8-e866c98d96f9 | -3.614 | -44.7783 | 2024-10-11 01:45:27 | GOES-16 | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 2bf00b46-6bbb-3977-9354-eebc73505798 | -4.1148 | -48.2515 | 2024-10-11 01:45:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| b2a88dc9-541a-34ef-9d05-f199b76cc0ae | -6.5404 | -60.0259 | 2024-10-11 01:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.9 |
| f3804ff3-c009-3670-b4d8-006dcbb28eb8 | -6.5589 | -60.0252 | 2024-10-11 01:45:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| b0849684-2028-3965-b6f0-e977dc0fdcea | -8.4231 | -55.4704 | 2024-10-11 01:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 18b51286-0712-3412-9e43-7ff3863d3582 | -8.4417 | -55.4692 | 2024-10-11 01:45:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| e647dc2a-406f-3b1d-a4b2-59b9cc9947aa | -8.6119 | -46.4796 | 2024-10-11 01:45:55 | GOES-16 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 926f8674-9da1-3a7e-b525-971b97cc13bf | -9.6575 | -64.9658 | 2024-10-11 01:46:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 7aa114a9-28ba-3c1a-a518-21275eab25a5 | -9.9481 | -58.1092 | 2024-10-11 01:46:03 | GOES-16 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 41.5 |
| b9204fee-f485-344d-b3be-bdf549f342e7 | -10.4713 | -49.9838 | 2024-10-11 01:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 022e0ab5-34f2-396e-aa85-c802a57076e7 | -10.5755 | -64.0438 | 2024-10-11 01:46:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 44b2a35b-3c91-3671-af20-1c7a8e4afbe0 | -10.6962 | -53.0354 | 2024-10-11 01:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 101.1 |
| a46d4131-44b5-398f-a1ed-64004d2d5ce2 | -10.6965 | -53.0147 | 2024-10-11 01:46:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 946ea603-6da4-3b16-bc18-18938c4f0dfa | -10.7059 | -64.1138 | 2024-10-11 01:46:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 9c85d95e-e554-300a-ae87-416bd556cb81 | -10.8935 | -52.3517 | 2024-10-11 01:46:08 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 8e12bf26-73e7-3530-be5c-1e8321ce9299 | -11.2407 | -53.2738 | 2024-10-11 01:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a752c70d-0eaa-3359-8d68-ec01a05ca9b4 | -11.2597 | -53.272 | 2024-10-11 01:46:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 62bc3a6b-4fe1-3a6e-a0e0-5a0e38547684 | -11.2763 | -60.4844 | 2024-10-11 01:46:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d1ee9b7c-4d11-3f12-9564-518d021e5847 | -12.3463 | -43.7638 | 2024-10-11 01:46:15 | GOES-16 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 80.4 |
| cb2a52ac-bc04-3ccc-8690-9666033c2361 | -12.1138 | -50.55 | 2024-10-11 01:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| d003a4b4-2377-3551-ad9b-367efe214dd2 | -12.1326 | -50.5692 | 2024-10-11 01:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 2887ab08-a92c-3254-88a7-ce7f13e696a5 | -12.1329 | -50.5477 | 2024-10-11 01:46:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 135.6 |
| c54ca7a5-1b2d-335a-9baa-db43d62dde0a | -12.4182 | -53.1544 | 2024-10-11 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 721ca62b-ad3a-30a8-b81f-1c0322628411 | -12.4373 | -53.1523 | 2024-10-11 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 124.2 |
| a4cfc4c6-e748-3da7-bf40-31f8aa699726 | -12.4376 | -53.1315 | 2024-10-11 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| c2235388-6487-31b0-85bf-462fc5fab9cc | -12.4563 | -53.1503 | 2024-10-11 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.3 |
| a5f66f8d-df56-3ad3-9402-e8c85e7d97d9 | -12.4566 | -53.1294 | 2024-10-11 01:46:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 8fdd4bcb-7911-3474-8823-f815b48c1a24 | -12.7673 | -44.8904 | 2024-10-11 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.2 |
| 24bed839-fbf8-304b-b3e3-82aa56d26f4b | -12.7678 | -44.8671 | 2024-10-11 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 4f89d684-989f-36e2-bce6-355a349da590 | -12.7866 | -44.8873 | 2024-10-11 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 06afd053-df4a-3dbd-8d54-500d32969a7b | -12.7871 | -44.8639 | 2024-10-11 01:46:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.9 |
| e2ffc68e-29ef-3f0c-a12b-32ff05828b55 | -12.8708 | -53.4799 | 2024-10-11 01:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| bda51633-dad4-3274-ac15-26dab4e97f41 | -12.8711 | -53.459 | 2024-10-11 01:46:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 9c72c325-421a-3476-bda9-6bc743e81883 | -13.9663 | -45.8025 | 2024-10-11 01:46:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 081a5b39-89cc-33be-a097-9cc66872e337 | -13.7346 | -60.6079 | 2024-10-11 01:46:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 51.5 |
| b5a539fc-6009-3646-9421-359713f18e08 | -2.6716 | -53.3502 | 2024-10-11 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.1 |
| f9a96ec6-15c9-38f2-b1f4-31d3bdb00376 | -2.6533 | -53.3506 | 2024-10-11 01:55:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| a28ffbb9-bb95-39e8-ab54-ac39a64eaa02 | -2.7848 | -52.4728 | 2024-10-11 01:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 67.2 |
| dc6ae1a6-05b1-3626-9c1c-170a2bc558cf | -2.7847 | -52.4933 | 2024-10-11 01:55:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 230809a5-a0a4-3bf1-896c-ee794239487b | -2.7395 | -49.5412 | 2024-10-11 01:55:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 36c64369-d788-3999-b3e1-71824f561378 | -2.9857 | -52.8961 | 2024-10-11 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 154.0 |
| 9f520a25-20ad-3056-8ec0-e8599dd0ac67 | -2.9857 | -52.9164 | 2024-10-11 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 149.1 |
| 52b073a1-352e-393b-9b5b-c061f6a01101 | -2.9673 | -52.8966 | 2024-10-11 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 22ca9869-aa4c-307a-900b-f792e23adf66 | -2.9673 | -52.9169 | 2024-10-11 01:55:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 116.8 |
| 3a80890e-8f00-37e2-9376-2792972c6466 | -3.1608 | -50.4347 | 2024-10-11 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 124.9 |
| 9006f632-a72b-364c-9639-088452b5b518 | -3.1607 | -50.4556 | 2024-10-11 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 329c4d05-4682-329a-9ced-ee17eee06203 | -3.1423 | -50.4352 | 2024-10-11 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 6a5cb114-c5a0-3d4c-ae60-79487d9dcf71 | -3.1422 | -50.4562 | 2024-10-11 01:55:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| d9bb1589-571c-3eca-b5de-2ca5faac0f9f | -4.0962 | -48.2523 | 2024-10-11 01:55:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| ce3cb28d-29b5-35d1-954e-7de5fc954b4f | -4.1333 | -48.2507 | 2024-10-11 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| ee615b19-03ba-3e48-a520-2fa6d291d242 | -4.1149 | -48.2299 | 2024-10-11 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 095142f3-a60d-3bed-9a7f-a5551e77606f | -4.1148 | -48.2515 | 2024-10-11 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 299.8 |
| 913626a6-5e0e-3717-b4f6-882d079bfcc3 | -4.1146 | -48.2731 | 2024-10-11 01:55:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| f62bbc95-bf07-37af-9020-ef2e696f6da8 | -6.5589 | -60.0252 | 2024-10-11 01:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 8c573ac7-da7c-3aad-bbe8-992acc3ac455 | -6.5404 | -60.0259 | 2024-10-11 01:55:44 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.1 |
| 1bdfae6e-1492-378d-baa6-d739cc8b7b96 | -8.4417 | -55.4692 | 2024-10-11 01:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 60c97ab0-3a65-3274-8c8d-3171188d9bb2 | -8.4231 | -55.4704 | 2024-10-11 01:55:54 | GOES-16 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 3bbcfdba-9419-3b2c-a6a5-a346eb8d6441 | -9.6575 | -64.9658 | 2024-10-11 01:56:02 | GOES-16 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 4f708851-449e-3bbd-afd1-db51fa5c1d3e | -10.6965 | -53.0147 | 2024-10-11 01:56:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 85.7 |
| 08539d9a-8df8-3e8c-bd43-3fbbd9c267a9 | -10.6962 | -53.0354 | 2024-10-11 01:56:07 | GOES-16 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 70885246-375d-3e16-be60-2ca03e25d80d | -10.5755 | -64.0438 | 2024-10-11 01:56:07 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 59.6 |
| ed647749-4c28-3481-905a-6cbbb5f7d435 | -10.7059 | -64.1138 | 2024-10-11 01:56:08 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| c6b3851a-10ab-3687-82fe-d21aa6b9ce16 | -11.2597 | -53.272 | 2024-10-11 01:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7d4d5c8d-96a0-359a-894b-b90b595a344c | -11.2407 | -53.2738 | 2024-10-11 01:56:10 | GOES-16 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 54378b8e-0d5e-3807-b797-95968f07dbe6 | -11.2763 | -60.4844 | 2024-10-11 01:56:11 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 316c8064-49aa-336a-b5a1-bbacf9d0e693 | -12.4373 | -53.1523 | 2024-10-11 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 52b54f74-6a06-3d99-a516-82b33cf2fd2d | -12.4182 | -53.1544 | 2024-10-11 01:56:17 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 361ed078-d1cf-3f0e-b1ab-31a0b5e787ed | -12.7871 | -44.8639 | 2024-10-11 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 4fca4efa-04af-3452-9518-a656941ba010 | -12.7866 | -44.8873 | 2024-10-11 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 105.2 |
| c77365b4-aee2-3dc8-bdb7-ebb65164bbb7 | -12.7682 | -44.8437 | 2024-10-11 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 367c2454-daeb-3b18-808b-b48b08809597 | -12.7678 | -44.8671 | 2024-10-11 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 232.7 |
| d97985f9-686a-3377-8c85-6ae5cc6b459f | -12.7673 | -44.8904 | 2024-10-11 01:56:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2b3fc005-5f4a-3f5f-bd20-a70e0ed17df3 | -12.8708 | -53.4799 | 2024-10-11 01:56:19 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 11d40285-9888-346e-849e-f1469cde3732 | -13.7346 | -60.6079 | 2024-10-11 01:56:24 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| 08720d7b-0423-362a-87a8-d0b2fc3671cd | -13.9663 | -45.8025 | 2024-10-11 01:56:24 | GOES-16 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 81.9 |
| deae893d-5291-3828-a4af-2ab1ccc02d10 | -12.79 | -44.9 | 2024-10-11 02:04:11 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a1506f83-dbbe-3ad9-8c5e-31b47829b3cb | -12.76 | -44.89 | 2024-10-11 02:04:11 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aaea9f49-b467-36bc-bedc-a8721a79aa2c | -4.11 | -48.25 | 2024-10-11 02:05:04 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b44450b2-ae14-3936-84c4-942eb69ed8fb | -2.6533 | -53.3506 | 2024-10-11 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 10e20133-6102-3ed4-a005-9486aa1371ed | -2.6716 | -53.3502 | 2024-10-11 02:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 5a202644-c90b-3d62-9022-ae2d5191d5fe | -2.7395 | -49.5412 | 2024-10-11 02:05:22 | GOES-16 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| fbe12c3f-25df-356e-aa63-c465f7b74c96 | -2.7847 | -52.4933 | 2024-10-11 02:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f5cac555-d00c-37f6-a29d-40420e80b8c2 | -2.7848 | -52.4728 | 2024-10-11 02:05:22 | GOES-16 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 33c91e0c-4271-3346-a589-2508c4c9d9b0 | -2.8081 | -51.0084 | 2024-10-11 02:05:22 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| d6fd9cd9-874a-376b-8e09-2b8549689a71 | -2.9673 | -52.9169 | 2024-10-11 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 110.7 |
| 251a450e-68bf-3d97-996e-960c55b56ead | -2.9673 | -52.8966 | 2024-10-11 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 53cb6bef-d75b-3c44-a970-804e14a77233 | -2.9857 | -52.9164 | 2024-10-11 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.7 |
| a1e1914c-fa4f-32ec-86fc-742c3caaf43f | -2.9857 | -52.8961 | 2024-10-11 02:05:23 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 130.4 |
| 8cc594be-c97d-3fed-998f-810eba3ea782 | -3.1422 | -50.4562 | 2024-10-11 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 9d04c3ed-956b-3aa1-86da-fd7d18da15d8 | -3.1423 | -50.4352 | 2024-10-11 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a96d07c3-cba2-3113-88c4-418253324710 | -3.1607 | -50.4556 | 2024-10-11 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 1949425c-baef-3f1d-a486-c538b7642bce | -3.1608 | -50.4347 | 2024-10-11 02:05:24 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 131.9 |
| e1040908-4e2e-3bb2-aafd-4c9ce7d512e2 | -4.0962 | -48.2523 | 2024-10-11 02:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 02f80d67-1c69-3f82-a601-c825186aa16d | -4.0963 | -48.2307 | 2024-10-11 02:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 6c07a33f-f3ec-3071-be0d-6f4c81750e51 | -4.1146 | -48.2731 | 2024-10-11 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 70928715-721e-3783-b35f-6c4d396fb6d3 | -4.1148 | -48.2515 | 2024-10-11 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 293.8 |
| c2c71889-1a85-395f-a1b7-e10af5e1935f | -4.1149 | -48.2299 | 2024-10-11 02:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 117.7 |


[Clique aqui para ver as próximas entradas](README27.md)
