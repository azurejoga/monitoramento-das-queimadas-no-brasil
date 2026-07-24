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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d1c6b7ad-3f86-3405-bc34-a86d03aabdde | -9.17083 | -58.32671 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fed61aa-d462-33b2-bee6-54906a8e7eee | -13.42818 | -51.5326 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 439fa98d-1dd2-3203-b89e-fcc0ed64160c | -13.44326 | -51.527 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 53b077cd-0171-385a-8da2-4271f2a5f43e | -8.71335 | -54.54623 | 2026-07-24 05:48:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbe3e050-e356-35b7-9e58-995e5c1bc50d | -13.43608 | -51.52619 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2f9798e2-0bc4-34be-8eba-361b153d794f | -9.13123 | -61.0625 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67a077a6-3b73-347e-aab9-955e0cdeb462 | -13.67939 | -59.63288 | 2026-07-24 05:48:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4b2a763b-367e-3478-b609-020c90530eba | -12.71947 | -59.99333 | 2026-07-24 05:48:00 | NPP-375D | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5e3d15a9-43e7-37fb-8b45-752cf8061642 | -9.15714 | -58.32889 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fc94a8df-d773-3973-8f1b-4eb01d22240e | -9.1764 | -58.31892 | 2026-07-24 05:48:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 46d4ef83-c0b2-3e38-b181-74bb19493358 | -13.4331 | -51.53514 | 2026-07-24 05:48:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 21.3 |
| bd0524e8-7f23-3182-890f-46237393f128 | -9.1349 | -61.06306 | 2026-07-24 05:48:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 88bc3c7f-4ac1-31bd-83f9-42969941fc2c | -18.79876 | -53.14069 | 2026-07-24 05:50:00 | NPP-375D | COSTA RICA | MATO GROSSO DO SUL | Brasil | 5003256 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 50833faf-ee85-3c7d-8b15-4bdb45706a64 | -18.54207 | -56.82379 | 2026-07-24 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| d675fca4-b9c9-396c-a009-5aea7958fa5e | -18.54708 | -56.82275 | 2026-07-24 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.4 |
| 150efa78-5d95-371d-a884-4342c8bdb13e | -18.54758 | -56.82447 | 2026-07-24 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| ba93ee3b-7577-3290-b295-7be275bd20da | -18.54671 | -56.82648 | 2026-07-24 05:50:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| f4b31072-3ee2-358d-8ae0-f852583a06ec | -9.17052 | -58.32475 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 585b706e-baa8-3f69-b0a9-c85ce5edc799 | -7.32314 | -64.69958 | 2026-07-24 06:05:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02f8e12d-dbdc-370d-95ea-7bac7057402e | -9.13416 | -61.06196 | 2026-07-24 06:05:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9d02dd5-62d9-3e73-9549-c265dc3e9cab | -9.16324 | -58.32933 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bbe2c34a-37a0-358b-8c4f-8e7ee478a4b4 | -9.13369 | -61.06561 | 2026-07-24 06:05:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f32b46db-f2c6-33f0-a56f-3e55cac3cb8b | -9.01251 | -64.14533 | 2026-07-24 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f4446eb9-75af-3ab6-99bb-de32ea8a0e41 | -9.16533 | -58.32867 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76e6814c-d9b3-34a2-b05c-429ec4f5600e | -9.13532 | -61.05808 | 2026-07-24 06:05:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4cbd9725-2832-3f1f-875a-ab477cbaa32d | -9.17121 | -58.31909 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5d504ef4-24f4-3636-8bde-68694faf85b4 | -9.16751 | -58.3117 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 92a02b8b-47cc-37d4-94e3-60bb93f1c7c5 | -9.13463 | -61.05828 | 2026-07-24 06:05:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c4aecd6-6a9a-34f6-a353-c0c885c29920 | -9.15874 | -58.32771 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7aae34a8-6d16-37a9-a73f-3694a5c0a81e | -9.17337 | -58.31835 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2515850d-a2a3-335b-8937-1877818088ed | -9.17191 | -58.31329 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3aa08c3b-798f-3b5f-a7df-241f1505327a | -9.16531 | -58.31239 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9da75a04-96b4-3d49-9968-e3998236af7b | -9.16393 | -58.32372 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfd49db1-fed0-3614-917e-a0b56868f5bf | -9.00738 | -64.14915 | 2026-07-24 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92cb0a9d-6d05-3e9b-82e6-443ee1d24d97 | -9.13432 | -61.0654 | 2026-07-24 06:05:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| edff6a5a-a2ea-35d0-b8c7-ac391558db8f | -9.00802 | -64.14469 | 2026-07-24 06:05:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6a264317-82ab-3a5c-9eca-c00fc39f4e8a | -9.17782 | -58.31995 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 859c4684-a76b-3779-b1f1-cc66ac39fd21 | -9.15665 | -58.32836 | 2026-07-24 06:05:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b392dc93-aeed-3e86-9bfa-fbbf6469a30e | -9.13482 | -61.06175 | 2026-07-24 06:05:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1670dac6-a4df-372a-91bb-fcda00c944e5 | -10.0294 | -65.05034 | 2026-07-24 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2928d6f3-5af7-3a7f-b940-a94dbb460ad0 | -10.02454 | -65.05385 | 2026-07-24 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7fda62ce-199e-33fc-9d2c-fd7b7bd0de46 | -10.00361 | -66.85958 | 2026-07-24 06:08:00 | NOAA-20 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cb1c823d-9065-33d1-b24c-9758d25a6d2d | -10.47195 | -62.44903 | 2026-07-24 06:08:00 | NOAA-20 | JARU | RONDÔNIA | Brasil | 1100114 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d9469b2a-be30-310d-88f2-2c397c1cf9b8 | -10.02511 | -65.04975 | 2026-07-24 06:08:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8bf475de-73b2-3595-a1a0-c1b388279062 | -6.56413 | -55.14977 | 2026-07-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| dda40d9f-0ad6-3d7b-89bd-17473502e5ca | -6.5656 | -55.13969 | 2026-07-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| feab8408-7f75-38e4-89f3-ea377cb6eb93 | -9.16112 | -58.32308 | 2026-07-24 07:18:00 | AQUA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b5a24cf2-4f6a-30e2-a4d8-db6aa2ddc464 | -11.7956 | -61.3235 | 2026-07-24 11:40:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 54356b70-b8e7-3946-a2bb-ebcf154f3295 | -11.7956 | -61.3235 | 2026-07-24 11:50:00 | GOES-19 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 80.0 |
| d5849241-083f-3672-8be8-7c23cacf4d36 | -10.69 | -46.3 | 2026-07-24 12:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0778720b-2648-35c4-9e77-76ebde8e47bc | -7.544 | -49.7579 | 2026-07-24 13:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 2d5738a6-caf3-352b-9147-72bc767deb5d | -10.69 | -46.3 | 2026-07-24 13:15:00 | MSG-03 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b515a279-fee3-324a-b4b7-65a9ddb78321 | -13.3169 | -54.3221 | 2026-07-24 13:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 89a8624d-9236-373a-8928-3fba3683f6e5 | -11.7926 | -50.3948 | 2026-07-24 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| a2057587-73ec-3180-8951-3ec66453f1a4 | -12.0188 | -50.5398 | 2026-07-24 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 4dee67bc-66ff-391b-8f10-b868484004db | -17.6338 | -51.8581 | 2026-07-24 14:10:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 4e655fc0-a713-3081-9acc-6be7435b9974 | -17.6338 | -51.8581 | 2026-07-24 14:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| e84edb22-1701-372c-80ce-6c8435ab0785 | -11.6408 | -50.3695 | 2026-07-24 14:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| ab17da77-daf8-35d1-997f-bba919295423 | -2.9557 | -42.3056 | 2026-07-24 14:40:00 | GOES-19 | TUTÓIA | MARANHÃO | Brasil | 2112506 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 9e97385f-9671-3123-a881-4590283aa9b2 | -8.711 | -54.5455 | 2026-07-24 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.4 |
| 729edc41-8a9d-3bf4-9ced-44bd734f43d0 | -7.544 | -49.7579 | 2026-07-24 15:00:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| bd61e184-19fa-38ec-8cba-afda19bf2ef0 | -8.711 | -54.5455 | 2026-07-24 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 1cf8172e-b641-3c06-95a6-d916c5ec498f | -13.4554 | -51.5392 | 2026-07-24 15:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| fe388675-479b-33fc-9769-a53af8d53e68 | -8.711 | -54.5455 | 2026-07-24 15:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| a9a09ea5-d4d0-3191-ab71-db0a02029580 | -12.0 | -50.52 | 2026-07-24 15:15:00 | MSG-03 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b23272cb-f8f2-3c6e-9e1e-99bde8540da8 | -13.688 | -59.6284 | 2026-07-24 15:30:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 328d4780-c735-382e-8bf9-bc3b012d521b | -11.7735 | -50.3971 | 2026-07-24 15:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.2 |
| e67a2f84-90ac-30d7-94df-12d67f168f25 | -13.3169 | -54.3221 | 2026-07-24 15:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 85.9 |


