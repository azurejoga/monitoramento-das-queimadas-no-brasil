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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef040393-c99f-32e1-8d97-1c4607dd2076 | -10.4794 | -46.7637 | 2026-10-01 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 128.7 |
| c064b643-b0d1-346f-a941-c4771e98b85d | -14.4422 | -51.2382 | 2026-10-01 01:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 2bb143d6-0a6c-3339-9f9c-4447667def79 | -3.295 | -53.8597 | 2026-10-01 01:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 119.9 |
| d863b03f-7090-3714-b342-fb75666c6cc2 | -10.46 | -46.7885 | 2026-10-01 01:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| dc5d4616-4f72-347c-8555-395b16175c34 | -3.1655 | -54.1045 | 2026-10-01 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 363.6 |
| 323e689a-f76a-3adf-9f21-ae8ccd785539 | -6.895 | -43.7066 | 2026-10-01 01:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 39.7 |
| fab6f85d-60ed-3812-8fad-d980f2f336cf | -14.4225 | -51.2624 | 2026-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 135.8 |
| f88996e7-630e-31a2-9e2f-9b4aad66fbdb | -14.4418 | -51.2597 | 2026-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 127.9 |
| c8e0125f-9398-3225-859e-22b5720c1dd7 | -13.6668 | -53.9522 | 2026-10-01 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 69.9 |
| ce5053a4-92b9-31a1-a404-248f654b517d | -6.6758 | -58.8654 | 2026-10-01 01:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 891413b0-6dce-371d-94a3-c81abb74f6cd | -3.5808 | -51.4832 | 2026-10-01 01:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| f3b95f80-3688-3995-8b8a-b13f694188a7 | -3.1061 | -50.2686 | 2026-10-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 8bb16599-b177-3528-8dce-ee7d14231e85 | -13.6671 | -53.9314 | 2026-10-01 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 102.9 |
| fe9a1764-5e5c-3189-a590-8ca493128ba6 | -9.1408 | -64.3836 | 2026-10-01 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 12577e71-846f-3ce2-86a6-bc6ad849423e | -9.1222 | -64.3843 | 2026-10-01 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 148.9 |
| cc2f74ed-a0bc-3b9d-a049-1afc6dd36523 | -11.81 | -50.4999 | 2026-10-01 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| 8fb6d106-c305-3ad7-93ae-1eb1c7737580 | -6.0179 | -49.5648 | 2026-10-01 01:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 85.8 |
| a1021e69-0694-3fd6-917d-d8fbfeb03c90 | -9.0046 | -65.6988 | 2026-10-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 98.5 |
| 4f4172a9-8fe8-38cf-87e6-093357964597 | -10.4791 | -46.7862 | 2026-10-01 01:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| e07a3166-ca5f-30e2-aa9f-ad7cf67df4a9 | -5.7355 | -43.2916 | 2026-10-01 01:10:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 53f6b949-8c2c-33ec-b3d5-8d55d1946cc3 | -12.1857 | -48.4345 | 2026-10-01 01:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 6215ae1a-5b94-3fc4-970f-df7f6635bbd2 | -6.2797 | -43.2711 | 2026-10-01 01:10:00 | GOES-19 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 00a04a33-e638-30d8-8df8-462fa51d92c3 | -9.0231 | -65.7169 | 2026-10-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 88547b15-2f37-39af-af71-b9ca5bf8f1dd | -3.1838 | -54.104 | 2026-10-01 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 317.5 |
| ee3f0300-d5c2-3319-b772-9b44d7152793 | -11.791 | -50.5021 | 2026-10-01 01:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 50298200-3984-3ffa-aa33-7c27a5a56ba9 | -8.9861 | -65.6993 | 2026-10-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 5222a994-094c-3e61-ad58-def90ab2e2bc | -9.1221 | -64.4031 | 2026-10-01 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 105.6 |
| cd60e85e-ba19-326d-90ad-75153bc8effc | -18.0458 | -51.1336 | 2026-10-01 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 7bfb861c-ed7b-3270-b146-a1f4eaf1fea9 | -3.106 | -50.2896 | 2026-10-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 70de7b91-cd55-3d35-8256-e50256190832 | -4.0477 | -54.2394 | 2026-10-01 01:10:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 173339ae-2d30-3bd2-bfa6-737009251f9d | -3.1245 | -50.268 | 2026-10-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| a44403e3-6e14-3a54-b00e-dcd4491807ad | -9.0045 | -65.7174 | 2026-10-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.1 |
| d5ebce19-6f74-3a5d-8c19-e2bb3110ad9c | -18.0658 | -51.1301 | 2026-10-01 01:10:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| e8b8a539-fc1c-3317-baf4-66af13a77332 | -2.908 | -54.151 | 2026-10-01 01:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| aeba0487-4c16-34a4-920b-d545ee3f656d | -3.5623 | -51.4838 | 2026-10-01 01:10:00 | GOES-19 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 66.3 |
| c347cf3a-a78e-3223-94cc-6c1aa2beb16d | -3.1655 | -54.0844 | 2026-10-01 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 297.1 |
| f8c89af2-4c7a-3936-b71a-3a99d45157b8 | -3.1656 | -54.0643 | 2026-10-01 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 0c68d981-7d8e-3bdb-ab46-66eb20ca6abe | -13.6479 | -53.9336 | 2026-10-01 01:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 2eabcb4d-8f02-36c6-924f-5cfd8fe1260f | -9.1407 | -64.4024 | 2026-10-01 01:10:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 69.5 |
| eb76dc08-b76a-3f62-80e8-e4947e9e2faf | -3.1842 | -60.0607 | 2026-10-01 01:10:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 43.6 |
| e5c59bfe-bbe7-31ca-927c-cd7ecc55fc91 | -5.9993 | -49.566 | 2026-10-01 01:10:00 | GOES-19 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 4b701417-468e-3fe8-ae74-7ea829e17a0a | -5.7563 | -45.152 | 2026-10-01 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 109.6 |
| 4511ca83-71e5-3706-9050-a1b663869da2 | -5.7561 | -45.1747 | 2026-10-01 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| f500f13a-27c1-3fda-922a-cf84bc6fdcf9 | -4.1667 | -48.894 | 2026-10-01 01:10:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| b42e4c51-5e09-3662-b047-07a4896ec971 | -3.1471 | -54.0849 | 2026-10-01 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 0575b0bf-ece2-3db9-88e2-9d607d501137 | -14.4228 | -51.2409 | 2026-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7d2eec86-9538-35d3-bda0-ec7e2c7283cd | -3.1839 | -54.0839 | 2026-10-01 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 175.1 |
| df248ed9-19b6-3375-bd09-4e84c40157d2 | -3.295 | -53.8597 | 2026-10-01 01:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 3a95f47b-e1ec-3324-a5a2-595c0f88f8c8 | -8.986 | -65.718 | 2026-10-01 01:10:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 92.6 |
| ef92ef6c-529a-30f4-a343-8f43afdf9596 | -3.1245 | -50.289 | 2026-10-01 01:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 82.2 |
| 97a48f1e-2898-31bf-9bad-19d00b3f86ea | -14.4414 | -51.2812 | 2026-10-01 01:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 90.0 |
| c876fe34-5155-3ad4-93d0-2e4913882df9 | -9.1183 | -64.390198 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17632bfb-1e68-3ad8-8994-10239b6b236b | -9.125 | -64.374199 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f3567422-3b04-3bf9-9bf9-a1e606cdea57 | -9.0146 | -65.721802 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d601b231-a925-38b6-a890-b04f9c059e6b | -5.1235 | -56.0383 | 2026-10-01 01:11:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 967b0280-0add-3b83-ac6b-b7feef2e544b | -8.9149 | -67.609497 | 2026-10-01 01:11:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 812f17bc-3d7f-34a4-a026-a06a1cabf7e2 | -3.2878 | -53.871601 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5251b96c-48ac-34ef-8a59-98613ca2210c | -8.9166 | -67.617401 | 2026-10-01 01:11:00 | METOP-B | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4e94384e-3d54-3725-bb96-b05034001fcc | -3.2782 | -53.874001 | 2026-10-01 01:11:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8d69ef64-c084-3567-b8f8-67916ed9cd71 | -3.1608 | -54.141701 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b8cb9c11-0e3f-3511-a393-c986e9d79984 | -8.553 | -66.986801 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2b4c8629-c629-3700-a866-9af2b415342c | -18.0338 | -51.145302 | 2026-10-01 01:11:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 3bb922af-7b84-34db-a172-21e80d7ffd2c | -8.9903 | -65.705299 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3a9c4714-e1d7-341c-8780-0fa569d88de5 | -13.6573 | -53.937099 | 2026-10-01 01:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f66ba78-2bfc-3b56-b376-d405aeaf8fd6 | -9.0115 | -65.707901 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a7768646-3821-3228-ab9f-ada17497419a | -13.6381 | -53.942501 | 2026-10-01 01:11:00 | METOP-B | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 07fa1946-701f-3ae5-87af-283930945dec | -9.1645 | -61.4063 | 2026-10-01 01:11:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 81362f06-cbc0-3980-846b-df4eee3711e4 | -9.4807 | -62.008801 | 2026-10-01 01:11:00 | METOP-B | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a1aac933-5fac-378b-a9a2-d459ece08da6 | -9.1168 | -64.383301 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 006d537a-c80d-3d51-8793-208662342d4e | -14.4316 | -51.297001 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2aac0665-2689-3e4d-ba19-f1c52634e11d | -9.0099 | -65.700897 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 01736d26-ce75-349d-ad5d-bebf02788e5e | -8.9986 | -65.696098 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 359520f0-8505-3712-8de2-bbb018b76499 | -4.0325 | -54.255299 | 2026-10-01 01:11:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c84bcc5a-1839-3fcd-b424-95f49f5e1a6d | -6.9202 | -59.296101 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f22843cc-20d5-3a1c-b134-2b6018008133 | -18.043301 | -51.1422 | 2026-10-01 01:11:00 | METOP-B | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 123d4a6c-93eb-3edd-8a53-fb3b35a09c05 | -6.6846 | -58.872002 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5921aaf7-9257-3fae-a66b-a17e6eff4444 | -14.4221 | -51.2999 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| cdf71e3c-0362-36f1-ac32-a1033e8fe866 | -8.5514 | -66.979401 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b429a7fb-a55f-3ffc-b567-d10e5175c492 | -10.0671 | -63.0742 | 2026-10-01 01:11:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 766cd85c-45cc-389a-91bc-4a1a6d030492 | -6.9173 | -59.283901 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| b723c257-ef3b-3597-81cd-940af1dbf701 | -9.0033 | -65.717102 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7e210a93-4a6d-3224-9861-1894d45e0cb2 | -10.0687 | -63.081501 | 2026-10-01 01:11:00 | METOP-B | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 87724a2f-bb01-372e-8744-4b28b360de95 | -3.6856 | -60.5522 | 2026-10-01 01:11:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 666c54fa-656f-3fcf-be32-d5dd1d29a67f | -14.4037 | -51.271301 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 365b1352-5d79-3a69-9ba8-0e8d40bdb49e | -9.1297 | -64.394897 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 42d7639c-3b51-352a-8287-5fb36c459338 | -3.6829 | -60.541 | 2026-10-01 01:11:00 | METOP-B | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fa5d947f-58d9-35a8-86c3-19437943e76e | -10.5226 | -57.782501 | 2026-10-01 01:11:00 | METOP-B | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ecb37765-3848-3701-9d63-92ac6975d327 | -8.5661 | -66.999603 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 46c4ba00-4e1e-3e4d-a563-3b0fb5da215d | -9.1313 | -64.401802 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 7edc31a9-f88d-3d90-9ef1-ec76dcf40dfb | -8.9888 | -65.698303 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2860b4ea-97cc-3dae-b370-d985fc0985f7 | -7.7585 | -67.161201 | 2026-10-01 01:11:00 | METOP-B | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d0caf817-38ee-32bf-b3b2-96a310cac19a | -3.1626 | -54.1077 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b0543b-51d8-32f5-a482-6a22c784cd2c | -6.6878 | -58.885101 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| eb385c66-7e1b-3a3f-ba4d-affae8125043 | -14.4132 | -51.268398 | 2026-10-01 01:11:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0bf94bf-51e6-32ca-a3a9-d4f6acbf5576 | -6.6748 | -58.874401 | 2026-10-01 01:11:00 | METOP-B | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f03f579c-dd06-31d7-a3dd-4b9a87200459 | -7.4923 | -55.014702 | 2026-10-01 01:11:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6b84226c-27eb-3d71-a323-31ed9586f761 | -8.6533 | -62.6693 | 2026-10-01 01:11:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 47b895b7-7c5f-311c-a844-44d52b22fba8 | -9.0484 | -66.106697 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 041ec920-d209-356b-b206-239b369322f5 | -8.5678 | -67.007103 | 2026-10-01 01:11:00 | METOP-B | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c9b7d574-0af7-3cd9-8f60-294c3c4c888c | -3.178 | -54.171001 | 2026-10-01 01:11:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README13.md)
