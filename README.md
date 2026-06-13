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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7d4b65bc-9576-30da-930f-a73018ae90e1 | -10.0623 | -48.0978 | 2026-06-13 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| fcd931bf-391f-346d-80fb-bf93b7de9c32 | -11.6497 | -48.5473 | 2026-06-13 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 105.5 |
| dab9fc92-9948-3a0b-9440-faed3da3f090 | -10.0626 | -48.0758 | 2026-06-13 00:00:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6587eef1-5ed1-3e4e-9120-45086f3fdbe4 | -12.4087 | -58.4657 | 2026-06-13 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 603339fe-24d8-3df2-b420-3c768560154c | -11.6309 | -48.5277 | 2026-06-13 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 08252629-1884-34c5-add2-4db5add9a13c | -12.269 | -57.4039 | 2026-06-13 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 71.0 |
| 56447942-629d-34dc-9761-b01c02c616ad | -11.6306 | -48.5497 | 2026-06-13 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 277.2 |
| 38a7ce7f-df0c-33e1-9c51-65d6ac7ec90c | -11.2408 | -46.7124 | 2026-06-13 00:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| fff8d2d6-809f-36b3-817e-24ca056d057b | -12.4085 | -58.4855 | 2026-06-13 00:00:00 | GOES-19 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 44.6 |
| afb636a0-8769-3779-8de2-0714a407ab2d | -12.288 | -57.4024 | 2026-06-13 00:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 28795302-d59d-3a07-9d14-47354d0dbcd7 | -12.269 | -57.4039 | 2026-06-13 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 254a94b0-9b6c-3cfb-94a2-9fe7014504d3 | -10.0623 | -48.0978 | 2026-06-13 00:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 70.4 |
| cf00c745-b05f-30c1-93f0-eb556b7e0352 | -10.0626 | -48.0758 | 2026-06-13 00:10:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 102.8 |
| 68b68447-0c16-343d-b26e-dcc25f4f888c | -11.6306 | -48.5497 | 2026-06-13 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 253.3 |
| 533aadb4-0f19-365a-98be-c1a728784915 | -11.6309 | -48.5277 | 2026-06-13 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 128.9 |
| 77001db7-cd0e-3488-8ae2-eaa00337f60d | -12.288 | -57.4024 | 2026-06-13 00:10:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 65eb9013-ffe6-377a-9e96-14af38a1dfdc | -11.6497 | -48.5473 | 2026-06-13 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 105.9 |
| 8c62093f-f8db-3b64-b594-462942f2c37c | -10.6489 | -46.8549 | 2026-06-13 00:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 77.5 |
| d992676f-115c-3ab7-a7ad-f25a691224a0 | -12.269 | -57.4039 | 2026-06-13 00:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| f4dc820b-e19f-349c-9785-2032fd61ff77 | -10.0623 | -48.0978 | 2026-06-13 00:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 336db680-8032-3989-a487-370f06cb3052 | -10.0626 | -48.0758 | 2026-06-13 00:20:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 8603cae4-7f8a-388e-86e2-82cc02b7e2d2 | -11.6306 | -48.5497 | 2026-06-13 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 218.6 |
| db341e21-abdb-3695-9fdb-254d2a0426c4 | -11.6497 | -48.5473 | 2026-06-13 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| 96fb28fc-a7a1-3a04-93b6-a329e29e07a7 | -11.6309 | -48.5277 | 2026-06-13 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 124.0 |
| 9114a8be-d2fc-3afa-b28d-66cd5abf5537 | -11.65 | -48.5253 | 2026-06-13 00:20:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| ad6e13a5-db5a-36cb-b2db-b4eedaaf4bfd | -10.6295 | -46.8797 | 2026-06-13 00:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| a6927232-4ae6-316e-b869-70bff530f787 | -11.2408 | -46.7124 | 2026-06-13 00:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 77.2 |
| c0ba20f6-8477-3282-b30f-c4483829597b | -12.269 | -57.4039 | 2026-06-13 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7014f733-5498-36d3-b6fc-87097c40100b | -10.0626 | -48.0758 | 2026-06-13 00:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 3e11e6be-4792-35bb-ade7-c38dd95cdf76 | -12.288 | -57.4024 | 2026-06-13 00:30:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6a56e5fc-ada4-30ac-a1f0-c4b6f625f9f7 | -11.6306 | -48.5497 | 2026-06-13 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 162.2 |
| 27774e15-8cf3-30a3-97df-dd6f1030f6ea | -11.2405 | -46.7349 | 2026-06-13 00:30:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 871a5640-7c18-3a67-8e5d-d7f8ea12d476 | -10.0623 | -48.0978 | 2026-06-13 00:30:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 0838a1a7-921a-3d4c-9ae6-90eaa3136fee | -11.1828 | -46.7649 | 2026-06-13 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 9c6602bd-f4dc-36b2-b56d-960288cbe256 | -11.6309 | -48.5277 | 2026-06-13 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 2cf1f63c-37da-31ae-9b09-5d157ddd3e03 | -11.6497 | -48.5473 | 2026-06-13 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 117.2 |
| f88d8956-798a-3afa-9e44-18d070a14e2c | -11.1634 | -46.7899 | 2026-06-13 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 7aa9288e-7b3c-354d-863e-b6c50a8bc1d1 | -11.1638 | -46.7674 | 2026-06-13 00:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 142.7 |
| 751d6113-bdcf-3401-8d1b-bbf47b9de93a | -11.65 | -48.5253 | 2026-06-13 00:30:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 77.4 |
| a2a6fbcd-7803-3023-9031-aff6cb225fb4 | -11.1825 | -46.7874 | 2026-06-13 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 193e3f1e-268e-3fb9-822d-3195b29800f5 | -11.6306 | -48.5497 | 2026-06-13 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 212.4 |
| 01a9c1fd-9cb3-3fad-9e1d-3dd85039d4b7 | -11.1634 | -46.7899 | 2026-06-13 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 127.5 |
| 20436542-65ba-3eaf-b36b-c33c272e491a | -11.1828 | -46.7649 | 2026-06-13 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 172.4 |
| 3d618816-8328-353c-bf61-3c5e2ae4b953 | -11.1638 | -46.7674 | 2026-06-13 00:40:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 224.2 |
| 5bb1c997-1691-3317-8109-2f841ff685e3 | -11.6497 | -48.5473 | 2026-06-13 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| 99579500-12af-37ca-8023-97732b4ed0b8 | -10.0626 | -48.0758 | 2026-06-13 00:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 101.3 |
| e1bffa6b-6c6c-3791-93f7-ea141aefd953 | -11.2408 | -46.7124 | 2026-06-13 00:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 89.2 |
| a27fcd9f-44e1-39fd-811b-548acae13e07 | -12.269 | -57.4039 | 2026-06-13 00:40:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 2fc9eb5b-c5e0-35e9-8aa3-b65b15864e1b | -11.2405 | -46.7349 | 2026-06-13 00:40:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 95.0 |
| 7350e500-67bb-3c3c-b553-03aa4344a171 | -10.0623 | -48.0978 | 2026-06-13 00:40:00 | GOES-19 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 0ed1ed3b-2e2f-37ae-8350-9b9634d0c653 | -11.6309 | -48.5277 | 2026-06-13 00:40:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 637d6a01-dc65-374b-b707-f3eea9359b7a | -12.2775 | -57.396301 | 2026-06-13 00:42:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0fa41559-b51c-37b0-8836-68579faa7e4f | -11.1768 | -46.713501 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc7fbe3e-9f11-3f2f-beee-9513f282f7d0 | -12.4279 | -58.471699 | 2026-06-13 00:42:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f200f3d-dfe7-3f52-bce0-d7d8a00b4b92 | -10.829 | -53.725601 | 2026-06-13 00:42:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d1038e44-dd4f-38e4-99f6-c8231f202ddb | -12.2661 | -57.3913 | 2026-06-13 00:42:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b05b8175-7ccb-3b73-8741-7d8a51305718 | -12.2677 | -57.398499 | 2026-06-13 00:42:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c822df83-5109-31b2-8fb9-ae9c5b03f152 | -12.1474 | -48.439201 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cb2c0860-4fc0-3c05-86c2-98206e0bc1b4 | -12.9033 | -54.2099 | 2026-06-13 00:42:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 04398a64-6563-32ff-a352-71df316f3eb9 | -11.1727 | -46.7374 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e8ec2c6-d8e0-3385-8ddc-d1e74bb450be | -10.8407 | -53.731098 | 2026-06-13 00:42:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f2aab577-460d-345b-9817-c138109c1b2d | -11.6221 | -48.527 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b0236ba8-ab94-393f-837f-9a8e91f8d219 | -12.4246 | -58.4562 | 2026-06-13 00:42:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aa03a061-846c-3465-b1ed-d48bbf94e5d7 | -13.52 | -54.2883 | 2026-06-13 00:42:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c3a9d04d-c8df-3efc-84e9-455c7bca53e2 | -11.5994 | -55.323799 | 2026-06-13 00:42:00 | METOP-B | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4f6ade6b-e80d-3366-8247-7e86ca69fbf1 | -11.5722 | -54.5718 | 2026-06-13 00:42:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fef482bb-1ec9-3444-b703-18abfe18f7b5 | -11.6261 | -48.542801 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0ed303fb-e42d-3267-942f-7cda42eb9cf7 | -13.5217 | -54.2957 | 2026-06-13 00:42:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| efda7523-0e9b-3671-852c-ed06160f6752 | -10.7121 | -56.234299 | 2026-06-13 00:42:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e9d0e18a-ac5d-3dac-8d43-1f3593367940 | -11.1631 | -46.740002 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7cc8832e-2dfe-312c-bd7c-22e5c859ee27 | -11.1686 | -46.7612 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3bdba0fa-cb58-3fbf-b388-62489993e2fd | -11.225 | -46.7006 | 2026-06-13 00:42:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2f133725-6f7f-3f75-899a-fd0ff54452d5 | -11.2346 | -46.698002 | 2026-06-13 00:42:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 635080c9-b260-3641-8ce9-3f31a0675bd2 | -11.1823 | -46.734798 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3521ecec-9471-3ce2-8403-cf1d67c3a393 | -11.1782 | -46.758598 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8e695a4e-f16b-3b47-8537-8a6af91eca7e | -5.7261 | -49.087299 | 2026-06-13 00:42:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd3b58c2-ad8d-3ed7-bb08-574c1a2543e5 | -11.5494 | -52.790001 | 2026-06-13 00:42:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d585ff29-fa8e-3897-8363-546d09f7c37f | -11.2401 | -46.7192 | 2026-06-13 00:42:00 | METOP-B | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e946e9b2-c668-3cd8-a4b8-1fdc1750374d | -12.4148 | -58.458302 | 2026-06-13 00:42:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 49aa20e8-fe35-33a7-a5f8-44dec64c8067 | -12.4164 | -58.466099 | 2026-06-13 00:42:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a169125f-24f1-3f8b-b235-47e374432192 | -11.6415 | -48.5219 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6beae6d4-9acd-334d-94b2-583d20a8ecc0 | -12.4262 | -58.464001 | 2026-06-13 00:42:00 | METOP-B | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eae1a473-8918-38d0-a216-a27d2bb65e86 | -10.0576 | -48.054699 | 2026-06-13 00:42:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1205e2ec-3b40-3209-9829-57f8f5c446b2 | -11.5104 | -56.117298 | 2026-06-13 00:42:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 836baeb1-361a-3023-9370-db0cff7bfac6 | -12.2743 | -57.381901 | 2026-06-13 00:42:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1be71945-e165-34dc-9c1c-1dcec20d4c9b | -11.8855 | -55.1301 | 2026-06-13 00:42:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5d37977e-8c79-334c-bfcb-d6342e4c3146 | -10.0524 | -48.075199 | 2026-06-13 00:42:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 72314968-21fc-396d-8c1d-aa256bc8b005 | -12.2759 | -57.389099 | 2026-06-13 00:42:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 40dc5812-d986-36dd-ae6b-f1b7e0b3f01d | -10.5736 | -48.015701 | 2026-06-13 00:42:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da8e0f56-e35d-326c-a724-81ef04863d9f | -11.7153 | -54.475899 | 2026-06-13 00:42:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 320ce6c4-d7c1-3912-9695-a8eb7901c00b | -11.1493 | -46.766399 | 2026-06-13 00:42:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b1a4f7ba-b242-3a1c-a62d-e96830fea24d | -11.8839 | -55.123001 | 2026-06-13 00:42:00 | METOP-B | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5853b8b8-0f70-376a-ad3f-7c0d9e5e0a65 | -11.6318 | -48.524502 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac4c9f99-f82e-36eb-bfa8-1b2e05fdf2cc | -11.5739 | -54.579102 | 2026-06-13 00:42:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b98a8718-e983-35c6-b691-ff0db710355d | -10.0621 | -48.072701 | 2026-06-13 00:42:00 | METOP-B | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4dcb33a7-8b47-3db7-9c3b-e0459f06d4e6 | -11.0416 | -56.925098 | 2026-06-13 00:42:00 | METOP-B | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| daf2ee0c-0ddd-3611-88c0-4aef2fd31160 | -10.5364 | -53.7108 | 2026-06-13 00:42:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1e8a64a9-790f-3ec4-871f-2d6fc12a5fa3 | -12.905 | -54.2173 | 2026-06-13 00:42:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f389a653-eea4-3b0e-bacd-1676f4d17ba6 | -10.5639 | -48.0182 | 2026-06-13 00:42:00 | METOP-B | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da4c0a99-8c17-3512-a917-3f2c07507365 | -11.6358 | -48.540298 | 2026-06-13 00:42:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README2.md)
