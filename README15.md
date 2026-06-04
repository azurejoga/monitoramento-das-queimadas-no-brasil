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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 30bf63d2-0448-3b25-8b52-5a9c35fd3e6c | -14.09008 | -59.38224 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88ff4b5f-c532-3ea6-ad83-b20132e84ed7 | -19.16998 | -55.1868 | 2026-06-04 05:04:00 | NOAA-20 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| ee42ea95-1f72-309b-b95c-c5852ddbff6e | -16.12789 | -58.51059 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 64880f61-e443-3769-93dc-c0f72db3f66a | -20.55679 | -46.35886 | 2026-06-04 05:04:00 | NOAA-20 | SÃO JOÃO BATISTA DO GLÓRIA | MINAS GERAIS | Brasil | 3162203 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 337b8096-ceae-31d6-98f9-029344dd7774 | -16.43898 | -57.26543 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 0d63ee15-46e1-3ded-9641-f3e3698453d5 | -14.16689 | -58.94136 | 2026-06-04 05:04:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b966755d-fa8e-3c27-8ab3-027af016265f | -16.74678 | -49.93617 | 2026-06-04 05:04:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8de4ec03-eaf4-3b59-8269-03815fce8fc0 | -15.68366 | -56.03693 | 2026-06-04 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 37987727-1aab-3eaa-a48f-a7c6ec765619 | -16.60342 | -58.25093 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 441f497e-52e5-3c52-92d6-4b9fa31d4dad | -16.14142 | -58.49314 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b08b13ba-d9f7-3928-a77c-7ab3f061a82b | -14.08932 | -59.38654 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 452f8fa5-52de-39c4-be94-2f2a23edd548 | -14.44761 | -48.90531 | 2026-06-04 05:04:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2b4af0a1-f3ef-3656-9c7f-586039283b0a | -16.8024 | -54.17293 | 2026-06-04 05:04:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3da8fcfe-d048-3d70-b6be-176721362d12 | -14.08896 | -59.3883 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b41a920-5257-3143-be85-36718844ae8c | -16.60406 | -58.24715 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| c9f19060-50b1-30fc-b689-97b974b70bbe | -16.44172 | -57.26964 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 4baf554c-ac22-308b-bd16-68a1294189ea | -16.16053 | -59.32139 | 2026-06-04 05:04:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96d9cbe0-8ee9-3d71-8c3e-4522fe535759 | -14.77522 | -52.67255 | 2026-06-04 05:04:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b6784198-e9ef-34e0-b453-5ae8cce8105c | -14.09024 | -58.88217 | 2026-06-04 05:04:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cd5c32f3-3f57-3886-b95a-6d2c907e010c | -16.12511 | -58.50611 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 1a1947ca-332c-3c53-b829-fe680192c9f0 | -15.31683 | -55.73463 | 2026-06-04 05:04:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f777d098-23a6-383f-b8c5-c468da8ee947 | -14.09379 | -58.88281 | 2026-06-04 05:04:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ef749203-cba2-312d-8389-ea935a962ce4 | -19.73825 | -53.55137 | 2026-06-04 05:04:00 | NOAA-20 | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| bd79715d-52b3-33c9-85b5-312c3a26f358 | -14.08857 | -59.39085 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b0a4ae9a-d700-3569-b760-4aed6ffa84db | -16.59176 | -58.23715 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| b4e4163d-8e81-33a4-bb9b-4ad74a7454b7 | -13.51262 | -54.31413 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d5730b87-9cb9-3d0d-81ff-7dd374633c46 | -16.59727 | -58.24595 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0408ef91-e804-36b2-a805-e4bab9419d24 | -14.08059 | -53.38293 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4c976259-73bb-346b-a1f2-09d69848b849 | -21.55331 | -48.60032 | 2026-06-04 05:04:00 | NOAA-20 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c647b3b3-97ec-36f7-9130-2071067dd4c7 | -16.18298 | -58.4768 | 2026-06-04 05:04:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| eee0a28e-4960-3428-bd11-9179e0009d0a | -14.09446 | -59.3786 | 2026-06-04 05:04:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63017c7e-4f62-3460-8077-08cbfe832f58 | -14.05629 | -53.3962 | 2026-06-04 05:04:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16bc44bd-53f7-3865-a366-253cacbc26f8 | -18.46423 | -54.70813 | 2026-06-04 05:04:00 | NOAA-20 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3077a2ab-b6f4-3927-a85d-ad80650a88cd | -15.501 | -56.03289 | 2026-06-04 05:04:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1cfaf2b6-d459-34f5-b355-79f47c044ae3 | -22.97008 | -52.69445 | 2026-06-04 05:06:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ebf22ecc-8240-3e8f-98b6-3ed785a288cc | -25.79226 | -53.29627 | 2026-06-04 05:06:00 | NOAA-20 | SALTO DO LONTRA | PARANÁ | Brasil | 4123006 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 12910453-ddc3-3065-90f6-64319523b87a | -21.95095 | -57.59483 | 2026-06-04 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cab85913-e2cc-3641-91bf-90bea7735a8f | -25.27051 | -50.65426 | 2026-06-04 05:06:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 5d59b155-d260-3b2d-94ac-75a700eba6af | -21.95427 | -57.59541 | 2026-06-04 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6b2b1db-f4ec-3e65-ba60-bfed7f6d26ac | -25.26989 | -50.65448 | 2026-06-04 05:06:00 | NOAA-20 | IMBITUVA | PARANÁ | Brasil | 4110102 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| ea6b2db0-9247-3d02-a4a4-6da0ba19cb9d | -23.074 | -55.17919 | 2026-06-04 05:06:00 | NOAA-20 | AMAMBAI | MATO GROSSO DO SUL | Brasil | 5000609 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 50de89c8-47f4-362d-9654-092e0b0ccae1 | -21.95369 | -57.59914 | 2026-06-04 05:06:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2d9b7f25-b200-3b11-aeb7-8f732395aabb | -12.2327 | -57.2672 | 2026-06-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| c3b33b5b-244b-3474-89e7-8bdd398fa0a4 | -12.2136 | -57.2888 | 2026-06-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| b13350bc-e6c8-38b2-986e-44240267a40c | -12.2325 | -57.2872 | 2026-06-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 9e8515fe-afa9-3dab-b732-9c1b4c33bd44 | -12.2138 | -57.2688 | 2026-06-04 05:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| bb9752d9-1566-3cbb-86e6-852cc985ac96 | -12.2138 | -57.2688 | 2026-06-04 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9dd0885f-6fda-38f6-aec1-9590dc148f27 | -12.2325 | -57.2872 | 2026-06-04 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 69.5 |
| 1a03970e-ddef-3df4-ac8a-92a486ba9af8 | -12.2136 | -57.2888 | 2026-06-04 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 115.0 |
| d94d5486-0c58-3589-a081-0e880ef0bfa4 | -12.2327 | -57.2672 | 2026-06-04 05:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 7f879fd7-4075-3e92-950c-a9dee163232b | -12.2138 | -57.2688 | 2026-06-04 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d5aec9d5-471a-3e44-8d6f-d3aff8c8070f | -12.2327 | -57.2672 | 2026-06-04 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| e0f2fbf9-9c74-30e9-a707-ee86cd7fe7a2 | -12.2136 | -57.2888 | 2026-06-04 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 91.7 |
| c80b8aec-af11-3cd9-b157-7478b6db09c3 | -12.2325 | -57.2872 | 2026-06-04 05:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.4 |
| 9120050a-c960-3f0a-b3d1-7439fdbaa580 | -12.2138 | -57.2688 | 2026-06-04 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 64a4efc7-54a3-353c-9cf2-2f39deacbf5c | -10.3839 | -49.4554 | 2026-06-04 05:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 39.3 |
| a46a6010-1f70-3339-9859-0e5666ca5fe2 | -12.2327 | -57.2672 | 2026-06-04 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 68.4 |
| 4766b21e-9d60-3fc1-b004-abebea96cb4e | -12.2136 | -57.2888 | 2026-06-04 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 0f651ea4-9496-3c74-8077-92a55bec21f4 | -12.2325 | -57.2872 | 2026-06-04 05:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 8dfec958-20df-3754-bdf1-05e08d8ae483 | -12.2136 | -57.2888 | 2026-06-04 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0879c530-cb29-3453-8542-49e04e6e5103 | -12.2138 | -57.2688 | 2026-06-04 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 57.2 |
| ba9424ab-721b-3eea-8d85-8ced479c7649 | -12.2327 | -57.2672 | 2026-06-04 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 27f039a8-d12a-3562-86ef-3a5b69600500 | -12.2325 | -57.2872 | 2026-06-04 05:50:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| e6662abc-b357-31f6-a8fa-3a824c7fd98b | -7.93998 | -71.46284 | 2026-06-04 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0a8a09bc-4460-3925-8f85-b0fd917ad045 | -12.21659 | -57.28726 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 923da408-11dc-334b-a73f-80c26cb2ec61 | -10.81986 | -56.59167 | 2026-06-04 05:50:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aeb7cca9-8307-3dfe-affc-e97b43b30fe1 | -11.88487 | -57.83635 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 25ab01c5-dcf7-3593-8aa8-19565714da8a | -12.23448 | -57.27511 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a2072788-d071-37a3-86a4-0ca568c8a862 | -9.85986 | -62.37667 | 2026-06-04 05:50:00 | NOAA-21 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3c03657-42a8-3761-a065-19f456c0b579 | -12.4651 | -58.46879 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9ae681f3-7c9b-3611-8e2f-1aec640314ba | -11.63486 | -55.19205 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 29a7048f-67d9-39fd-898a-0d9335444ae4 | -9.64321 | -67.21555 | 2026-06-04 05:50:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b9168c91-176e-3377-b354-aec711df5371 | -9.61227 | -67.17512 | 2026-06-04 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 05ff19a1-888e-3465-9f1b-e7acee2daaef | -12.43999 | -58.39891 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e2f2e0ab-2306-3687-b1e7-9bd43d26f055 | -12.46464 | -58.47256 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7c0a233b-6ff3-35dc-a695-de9e02594ed0 | -12.21626 | -57.27709 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 577d4670-2e5f-3279-9022-7c3ad5623c6b | -12.74019 | -54.20292 | 2026-06-04 05:50:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 974aad69-9818-31d5-96db-a12319834ce2 | -10.56904 | -57.32195 | 2026-06-04 05:50:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5bffccf0-11fe-3e3b-8f77-ecc8b7627386 | -9.60944 | -67.1497 | 2026-06-04 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3239a8f8-5d28-3a15-8f79-dd71a929c33e | -11.59001 | -58.50768 | 2026-06-04 05:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acc8a43b-5685-3084-9414-4277e4d723b2 | -12.21172 | -57.27796 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 984153f4-f13b-35f3-8359-8f3a549c955e | -9.18388 | -58.0568 | 2026-06-04 05:50:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8048e6e7-da57-3962-96ba-4d0a0c299b11 | -12.43869 | -58.40984 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dd600052-df32-321f-a358-8883a0cab6e6 | -12.44973 | -58.41101 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f5e6ef74-0ae8-3052-a391-a22ee0944f16 | -11.62884 | -55.18528 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 45357ac2-ccec-39f8-899e-3ecb2df12ad3 | -12.22168 | -57.28218 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| 8eeed7e8-7576-3a0c-9746-b12020bdae27 | -11.62217 | -55.18442 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6fb33ecd-c4ea-3a45-ad5f-f989f308db15 | -12.43912 | -58.40618 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 03d4492e-9942-3270-893b-197394484286 | -12.2225 | -57.28799 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 6ee85654-e112-31a8-80a0-dd10c85171c8 | -12.4587 | -58.47561 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 77b42163-fd52-3d77-9b52-7ae07b8219cf | -12.45368 | -58.47105 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f47b10d1-76c7-36ac-b18c-670db5a78ac7 | -12.20842 | -57.29353 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 27dcb70a-b41a-3d4d-bab2-252a2c0e4454 | -12.44929 | -58.41467 | 2026-06-04 05:50:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 927c6056-383f-37f4-aff5-0199e17e765a | -11.62152 | -55.19035 | 2026-06-04 05:50:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a2d9a074-3f4e-3388-898d-2fcf91af516d | -12.21069 | -57.28653 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 147b02b1-06dc-310e-b8ef-1787fd8e22e5 | -12.22857 | -57.27427 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 93e68806-ddd7-3828-9c35-f4ca469953db | -12.21762 | -57.27869 | 2026-06-04 05:50:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 8c2a4677-9899-364b-9c8b-5f790c5391b6 | -10.03204 | -59.33966 | 2026-06-04 05:50:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53cd0ce0-780e-3569-aace-ceb8f12c7807 | -12.45961 | -58.46806 | 2026-06-04 05:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| dc7193bf-6a4f-383b-b7d3-3e6357f7b38f | -9.62723 | -67.20956 | 2026-06-04 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |


[Clique aqui para ver as próximas entradas](README16.md)
