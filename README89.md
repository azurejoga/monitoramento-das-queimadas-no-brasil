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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6b4be758-0764-39bc-a845-23d7c283923c | -4.1515 | -60.7068 | 2026-08-29 16:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 388b448d-b2b0-308e-8dc8-14946af4617b | -9.0057 | -65.456 | 2026-08-29 16:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.7 |
| c4070ff0-ef62-39f3-b831-6cd54256888e | -7.3665 | -55.1534 | 2026-08-29 16:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 84df7736-7a65-389a-a848-193baef506a6 | -11.1729 | -51.2516 | 2026-08-29 16:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 2f9133c1-849a-32b5-a045-422f0c26bc82 | -6.8004 | -59.6704 | 2026-08-29 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.9 |
| d9414747-c44f-312c-b477-f78e99b85e65 | -8.3902 | -62.7152 | 2026-08-29 16:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 00605b6f-6692-300c-99b8-fd7fae5517ec | -11.2106 | -51.2688 | 2026-08-29 16:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.6 |
| 1ed95b7a-c72b-35b1-bb21-fa5bf9c8b2d0 | 1.785 | -55.8226 | 2026-08-29 16:30:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 4483782b-2d31-37e9-bbdf-92a84035ea56 | -10.8235 | -50.5026 | 2026-08-29 16:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 102.6 |
| ced6a492-a437-3792-854a-0f0756065e09 | -8.6495 | -66.5468 | 2026-08-29 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 46868186-54f3-35a2-b013-c299d1bd3936 | -12.9054 | -59.8857 | 2026-08-29 16:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 41.4 |
| c792a3f2-24d8-3568-a3d1-32df37a108ff | -6.6726 | -59.4445 | 2026-08-29 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 2c792642-7f6d-317e-8351-8d9e8fc4f7f7 | -9.0983 | -65.4717 | 2026-08-29 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 123.2 |
| cea7a8ec-c8cc-361f-aff9-39e674ea4d24 | -11.1998 | -55.0805 | 2026-08-29 16:30:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 1cb5d7a0-9a84-375a-8933-4589d8e95322 | -9.2465 | -65.5043 | 2026-08-29 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 44c32d82-9fad-318e-8497-d97da269cb16 | -8.2133 | -70.4998 | 2026-08-29 16:30:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 37.9 |
| 7929b25a-4ca8-3666-b2ec-8d8c998234da | -6.7507 | -58.6687 | 2026-08-29 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.1 |
| 5aff993b-a619-3a49-9520-78b6579081e9 | -9.9288 | -60.4277 | 2026-08-29 16:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| e58a8fc5-930d-353c-9a1a-3b817f96060c | -6.8192 | -59.5927 | 2026-08-29 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 5daba9e6-1c1d-3d98-9a04-67cd7b8019eb | -11.1939 | -53.9993 | 2026-08-29 16:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 108.2 |
| be134e8f-04d0-3e63-a790-736ed0fe5206 | -8.574 | -66.9569 | 2026-08-29 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| a01afe7d-0bb1-37a3-9eee-f86bca045138 | -9.0982 | -65.4904 | 2026-08-29 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.0 |
| 51033564-4051-3fa4-8f06-e0034b66c7eb | -8.631 | -66.5473 | 2026-08-29 16:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 50a14d9e-98ef-3481-8b9d-4dae34e0a55e | -6.7094 | -59.443 | 2026-08-29 16:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.0 |
| f94a2e44-687b-3421-b0b1-b46315a989b6 | -6.8357 | -59.9571 | 2026-08-29 16:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 307e5f82-4615-34a1-a818-50a1b570a725 | -6.1795 | -45.9097 | 2026-08-29 16:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 53d908a1-a788-3b27-96f9-a82299643420 | -6.641 | -58.4987 | 2026-08-29 16:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 7d4004ec-0681-3487-8250-19c8ce3e289a | 0.1367 | -60.393 | 2026-08-29 16:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 154.3 |
| b683c60f-6e4d-39c1-a199-284443a94284 | 0.1914 | -60.5067 | 2026-08-29 16:30:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 83.7 |
| db12249b-043c-38b5-9332-25032f607e9d | -8.6311 | -66.5287 | 2026-08-29 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| 5141a4e2-5f2b-3a23-91a9-7f5a5f157846 | -9.0647 | -69.5867 | 2026-08-29 16:40:00 | GOES-19 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 45478c65-2e2c-3210-bd58-6395f563f71f | -11.1726 | -51.2728 | 2026-08-29 16:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.0 |
| 2e79e626-ecfd-327b-8ba2-3f6483985ab6 | -6.7123 | -58.9412 | 2026-08-29 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| a8b5092f-6c17-3c6e-a129-821099de021c | -8.5971 | -54.7553 | 2026-08-29 16:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 24633c70-beeb-3ede-a054-e5d3dfd228ea | -6.641 | -58.4987 | 2026-08-29 16:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.0 |
| 9aece6ba-7145-3127-af27-eff347451808 | -10.899 | -50.5159 | 2026-08-29 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 2ba4d447-6902-3489-b4b1-62f34f123e29 | -13.2839 | -51.4755 | 2026-08-29 16:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 39.1 |
| 2d42b429-d4e2-3b1a-b4f1-e5bd421580a9 | -6.7279 | -59.4423 | 2026-08-29 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 5f9f54f2-4a42-3c59-a157-4adfef3fd409 | -9.0982 | -65.4904 | 2026-08-29 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 90116db3-1820-3933-aaff-4e48f47add78 | -8.631 | -66.5473 | 2026-08-29 16:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 780b4611-c3a0-33e5-9908-9e0b1af85dc4 | 0.1914 | -60.5067 | 2026-08-29 16:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 94.4 |
| c650c688-3e5e-358e-ab34-7a82d61de37c | -10.9559 | -50.5098 | 2026-08-29 16:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 74.4 |
| ccfe625c-2f7f-3f49-9856-07d60c70d894 | -7.0058 | -59.2382 | 2026-08-29 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 1015e594-9494-390c-8203-cf56cc70a69d | -6.8411 | -58.9939 | 2026-08-29 16:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| f9ee059c-471b-3d8e-bec4-efda4128afc8 | -6.9872 | -59.2582 | 2026-08-29 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 369785a6-bbfc-33bd-af13-5249ce576e7c | -10.5406 | -50.4469 | 2026-08-29 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 3b6d7280-4773-3528-b3e4-72a8b60deaed | -3.4185 | -61.3273 | 2026-08-29 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 1698d803-f0a3-3cb9-8e04-815c8a6537f0 | -6.7094 | -59.443 | 2026-08-29 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| ba329eda-caa5-3299-9f76-8e5ab326e9e2 | -10.3202 | -49.9782 | 2026-08-29 16:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 0fa5e3f8-a189-3e9a-a156-083fd5a78dfd | -8.5962 | -54.8563 | 2026-08-29 16:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 699c080d-c4c1-3b20-9209-83de75cf7ebe | -9.0982 | -65.4904 | 2026-08-29 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 9bf04568-3b0c-3163-8b84-a17d7dad2037 | -12.2475 | -50.534 | 2026-08-29 16:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 13513661-bdce-31b8-8bb7-45dce20fdcae | -8.3717 | -62.716 | 2026-08-29 16:50:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 3fc4c79b-f5ae-39a9-8345-ec6e21cc3a12 | -8.574 | -66.9569 | 2026-08-29 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 11dcb3d9-9046-350a-9be3-bc47039a1bf8 | -6.8192 | -59.5927 | 2026-08-29 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 7834d8cd-c10a-380f-9b26-68c317c62ca2 | -6.7451 | -59.6533 | 2026-08-29 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 6ee6f437-e8a4-3a84-b2f2-de23ed05db9f | -6.8412 | -58.9746 | 2026-08-29 16:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| eb56ba5e-16fc-3b05-b46f-1b760af6cbc2 | -8.5964 | -54.8361 | 2026-08-29 16:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.6 |
| e73ee90e-8fd4-3ae9-a261-7dbf022770dc | -11.1998 | -55.0805 | 2026-08-29 16:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| a78b9659-fc44-397f-9ebe-ac94fd18b5f6 | -3.4002 | -61.3276 | 2026-08-29 16:50:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 9189aa6d-7f39-36ed-9a82-04e178b074b1 | -11.1939 | -53.9993 | 2026-08-29 16:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 95.0 |
| 9e0d724a-ba76-31d5-874a-7d1f0f87f00f | -8.6311 | -66.5287 | 2026-08-29 16:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 46.9 |
| bc438120-bf1e-3471-b4ad-7c04615748e6 | -8.2318 | -70.4812 | 2026-08-29 16:50:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 44.3 |
| e0120cc7-2609-35cd-8e39-fc1357b9c0f0 | -10.8993 | -50.4945 | 2026-08-29 16:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 67ff9077-66bf-3d07-8143-4e8331b81941 | -11.1723 | -51.294 | 2026-08-29 17:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 6cdbc45d-90e9-39b0-9d26-0ef64a5ac0b5 | -10.8422 | -50.5219 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 711e93da-9f41-3d7f-9812-b92ec4bd6598 | -6.7123 | -58.9412 | 2026-08-29 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 8be9af54-b4c1-38cf-8cc7-e756a222ff7a | -12.2284 | -50.5363 | 2026-08-29 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 2e7003fb-6ff9-38ab-9a67-4c640093d8f9 | -10.918 | -50.5138 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| f4025057-f045-31b6-aaa0-47196537ce30 | 1.7849 | -55.8423 | 2026-08-29 17:00:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 28b9f7ba-50a2-3534-ad3f-e3e1273edb54 | -12.2093 | -50.5386 | 2026-08-29 17:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.7 |
| 6f8ff4a5-aeee-3c65-9991-aec0df394951 | -9.0982 | -65.4904 | 2026-08-29 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 5b87eaca-6ec3-3ded-99b4-fafdceeeb25b | -8.2318 | -70.4812 | 2026-08-29 17:00:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 9c583809-dd6d-3ca7-915b-380953bc712e | -10.937 | -50.5118 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 62926f40-11c0-3fc3-842f-b0d247b3571f | -10.8425 | -50.5005 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 5c53166b-d34d-3488-be9c-ac462b5da12d | -10.5404 | -50.4683 | 2026-08-29 17:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| e1935cf8-5096-32df-9533-0fd497d034e9 | -14.5638 | -52.013 | 2026-08-29 17:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 129.1 |
| d8fc9f66-bd98-33ec-acda-16b28fc18df0 | -11.1939 | -53.9993 | 2026-08-29 17:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.9 |
| aaec7c9e-315b-3489-85d0-fa17ee7a8aa3 | -6.7451 | -59.6533 | 2026-08-29 17:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 74af5580-a0ae-3cac-9806-af747587d447 | -10.8235 | -50.5026 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 46c4d8a7-b87a-3545-b6c4-96e4d211835d | -8.631 | -66.5473 | 2026-08-29 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 13525a9a-26d5-34ab-a6f7-928fff3de45b | -3.4185 | -61.3273 | 2026-08-29 17:00:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 0528b3b4-4c41-3d3f-8ca2-bede543528ca | -8.574 | -66.9569 | 2026-08-29 17:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 3b39925b-233e-3a78-ab98-dedd123bff6d | -10.8993 | -50.4945 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 3b6d62eb-89f1-32af-9087-d8694661bef3 | -11.1998 | -55.0805 | 2026-08-29 17:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.2 |
| f18ee67b-f28c-3c00-a9ca-66efe37f8e70 | -10.899 | -50.5159 | 2026-08-29 17:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| ff5226f8-fe8b-3950-a6f3-57307f658148 | -12.1902 | -50.5409 | 2026-08-29 17:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| d1f7ac6b-3a51-3536-8570-a93464ba0b44 | -11.1998 | -55.0805 | 2026-08-29 17:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 3aacf8d4-4e9d-3e52-8dc4-cc1c3d6fc358 | -8.574 | -66.9569 | 2026-08-29 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 073a3494-9520-3c68-be46-2786c5f4fc06 | -11.1916 | -51.2708 | 2026-08-29 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 301e54d8-3a85-3001-a24e-d7feff260731 | -10.559 | -50.4876 | 2026-08-29 17:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| fcd59205-af24-3d4f-8834-e99ea4252825 | -6.6726 | -59.4445 | 2026-08-29 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 901cd5cd-7e1b-3558-befd-6acac7f4eae9 | -6.7451 | -59.6533 | 2026-08-29 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 13e2871d-4427-353e-96ff-aafc62fc21e1 | -10.7649 | -50.6366 | 2026-08-29 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 87.1 |
| c73f0d3e-c13c-3a8b-b852-0fa847ea4691 | -11.1939 | -53.9993 | 2026-08-29 17:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 119.9 |
| eb9ad157-3dde-3853-b658-011bb543d168 | -6.6929 | -59.0966 | 2026-08-29 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.0 |
| be02fac9-c58b-3a3f-9b8c-952d9173b14b | -11.1726 | -51.2728 | 2026-08-29 17:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 222.8 |
| e4d93b4a-84e9-31a3-9483-1b0e7af1bd4b | -8.6311 | -66.5287 | 2026-08-29 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 85733712-d928-3ea4-ab7e-6826cc2e81c1 | -8.631 | -66.5473 | 2026-08-29 17:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 106.9 |
| ec232354-b3fc-30a8-95be-8b2cad40b90a | -6.7507 | -58.6687 | 2026-08-29 17:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.0 |


[Clique aqui para ver as próximas entradas](README90.md)
