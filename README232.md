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

## Dados Diários - Página 232

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 234942be-5a91-3940-b170-d2789659b648 | -16.8743 | -56.7352 | 2024-10-09 12:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 104.9 |
| 02eb73d4-adae-34be-99b7-e2812f365448 | -16.8747 | -56.7146 | 2024-10-09 12:26:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 101.6 |
| 909e9486-600a-368a-8c86-c0c349b987f6 | -16.8943 | -56.7122 | 2024-10-09 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 108.2 |
| 1fdc8191-0f34-3a9f-a714-9060da19c303 | -16.8939 | -56.7328 | 2024-10-09 12:26:42 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 97.9 |
| fa438f1b-81b0-3eff-844d-371d009c6cb2 | -6.7798 | -60.0552 | 2024-10-09 12:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 247.6 |
| 595a1562-7a0e-353c-b522-a3731b0105f2 | -6.7615 | -60.0367 | 2024-10-09 12:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 8be4c43e-cd2a-3219-acf7-69839c088630 | -6.7799 | -60.036 | 2024-10-09 12:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.2 |
| 71cce3a6-65e0-37fc-9bfa-a58d970430c5 | -6.7614 | -60.0559 | 2024-10-09 12:35:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 156.2 |
| 75bbe4bd-b6d4-3c9c-95d0-0400690cabae | -8.4919 | -48.6476 | 2024-10-09 12:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 118.4 |
| f416811d-c40a-368e-a4e1-7cab7b7929b7 | -8.4921 | -48.6259 | 2024-10-09 12:35:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 60.1 |
| 0ba81334-aec0-3045-b7c0-d1a95996f098 | -8.5107 | -48.6459 | 2024-10-09 12:35:55 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 105.8 |
| b34d71b5-2941-3634-b2a2-fad7610ab607 | -10.5746 | -48.0178 | 2024-10-09 12:36:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 652aee9e-e9dc-3816-a93e-b0aa4875cfba | -10.6476 | -50.9249 | 2024-10-09 12:36:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9f593be9-5d99-35ea-8e84-68e2e7dd9712 | -11.3046 | -51.3222 | 2024-10-09 12:36:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0d31c272-9ea9-3908-b97c-0ae08f45a2eb | -11.3235 | -51.3202 | 2024-10-09 12:36:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 137.1 |
| da7df3e1-2540-3f17-8dfb-56110675003d | -11.3232 | -51.3414 | 2024-10-09 12:36:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.5 |
| dd831970-75ed-333e-b203-1b2f305c2d62 | -11.7749 | -44.5335 | 2024-10-09 12:36:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 3c8e199a-a5ba-3f8d-8c6d-a984c0afb575 | -11.6883 | -49.74 | 2024-10-09 12:36:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| c3c89d09-32be-3996-9987-c10103c78998 | -11.7946 | -44.5072 | 2024-10-09 12:36:13 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 133.3 |
| c46512b0-0cbc-36aa-9e0a-31e53ef3e3e9 | -11.7041 | -49.9539 | 2024-10-09 12:36:13 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.2 |
| ee2b4a12-690b-3e12-94ba-e285bccdd455 | -12.011 | -51.0531 | 2024-10-09 12:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 3ecb4648-b81d-37a5-9a7a-862c77ccb6f4 | -11.992 | -51.0553 | 2024-10-09 12:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 119.0 |
| b2be34ed-4c9a-3a65-9be9-6f05f36aa09c | -11.9729 | -51.0575 | 2024-10-09 12:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 59b8ebd9-175b-3eee-8950-3017d6dc8a7a | -11.9923 | -51.034 | 2024-10-09 12:36:14 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 284.0 |
| f78a2c2e-685e-3c62-b6d3-65bf3d3fe96b | -12.1086 | -50.8926 | 2024-10-09 12:36:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 45124f83-e964-3c00-8113-e459d0f97ef2 | -12.6875 | -62.9656 | 2024-10-09 12:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 0d2ce77d-300c-3af1-aa3b-e5007020e949 | -13.2877 | -53.704 | 2024-10-09 12:36:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 264c61df-2e37-3b88-9d79-e0bb236ddd1a | -13.288 | -53.6832 | 2024-10-09 12:36:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 119.1 |
| 84ac7429-7c10-3831-946f-823142b011a6 | -13.398 | -61.9182 | 2024-10-09 12:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 106.7 |
| 5cf23edf-274a-3081-950d-3872052d5915 | -13.3976 | -61.957 | 2024-10-09 12:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 60db1dae-d35c-395b-bd04-dc886c2f503a | -13.3978 | -61.9376 | 2024-10-09 12:36:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 77.3 |
| f6c83dcf-1393-3e42-9abf-ba85e41bd98a | -13.8364 | -44.5927 | 2024-10-09 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 5a026b67-d201-3272-b800-83165868d8f0 | -13.8369 | -44.5691 | 2024-10-09 12:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 1c23058f-8380-3eb3-99b8-21c1f7bd6e50 | -14.0778 | -51.116 | 2024-10-09 12:36:26 | GOES-16 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b9ce8a6a-f92b-3642-b17c-b2cf54e082ac | -14.8228 | -46.6419 | 2024-10-09 12:36:29 | GOES-16 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 206dff0c-e902-3e16-bfb8-5f18c5df07d6 | -15.7076 | -59.3726 | 2024-10-09 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 170.6 |
| 58f49c14-28b6-3e66-9d8a-70802cfab24d | -15.6487 | -59.4381 | 2024-10-09 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 88.9 |
| 8a6d1879-0983-3e30-ac48-e6ff6dabf57d | -15.6686 | -59.3963 | 2024-10-09 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 0f4fb1d9-ede1-39d7-8e3c-88f3f71e6f6b | -15.6683 | -59.4163 | 2024-10-09 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 92.3 |
| d67cdad7-6277-32c4-9f4f-1c550367b7d9 | -15.688 | -59.3945 | 2024-10-09 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 062aeb74-4e6d-38b8-8246-027f3f65b2e5 | -15.649 | -59.4181 | 2024-10-09 12:36:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2dbd92eb-0eb7-32b2-a615-a17cada69f6d | -16.8358 | -56.6987 | 2024-10-09 12:36:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.0 |
| a0133579-5648-3c09-9f28-c322b1a10f85 | -6.7614 | -60.0559 | 2024-10-09 12:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 44f5847a-40ab-3fda-bcfb-b25ef939d573 | -6.7799 | -60.036 | 2024-10-09 12:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 2436460e-e263-3285-ac2b-1044f5779ee6 | -6.7798 | -60.0552 | 2024-10-09 12:45:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 228.3 |
| 7808d7ca-87da-35fb-901d-ab01aefb2fd4 | -8.4921 | -48.6259 | 2024-10-09 12:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 78.8 |
| b6c4202a-c310-332a-9753-caf41d58df3f | -8.4919 | -48.6476 | 2024-10-09 12:45:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 142.5 |
| 4b48b257-c051-3d33-91d9-6e566dea3665 | -8.5107 | -48.6459 | 2024-10-09 12:45:55 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 207d5bbb-e5c9-37a4-90bc-e887507dc758 | -10.5746 | -48.0178 | 2024-10-09 12:46:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 373acd9e-b1a3-3f87-b730-cd601a42b801 | -10.6476 | -50.9249 | 2024-10-09 12:46:07 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 1b4c4cd8-47bf-39d5-9e43-9cd615298663 | -11.3046 | -51.3222 | 2024-10-09 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| d184550b-cec2-379b-a409-e9220edbfc37 | -11.3043 | -51.3434 | 2024-10-09 12:46:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 2575c5d9-4f6f-359f-9202-dc3ed9766332 | -11.328 | -51.0018 | 2024-10-09 12:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 56d2460b-41b2-3b84-8dfc-47d0c74a28fe | -11.3232 | -51.3414 | 2024-10-09 12:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 84.9 |
| fcb968ef-c1f0-3981-b07d-087f98e78e7a | -11.3277 | -51.0231 | 2024-10-09 12:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 844ca9cb-9aba-3e5d-bdeb-b27405aae8c7 | -11.3235 | -51.3202 | 2024-10-09 12:46:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 183.6 |
| f48e07e8-a98d-314c-8fd5-4a2be0f054e7 | -11.7749 | -44.5335 | 2024-10-09 12:46:12 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.8 |
| 7f55ea7b-9198-3fae-848a-ec22d2af8fc6 | -11.6883 | -49.74 | 2024-10-09 12:46:12 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 54173859-7ab7-30e2-86fc-3c889bc31769 | -11.7946 | -44.5072 | 2024-10-09 12:46:13 | GOES-16 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 8ba1080d-6ef4-330d-b05b-3593393ebc8d | -12.0895 | -50.8949 | 2024-10-09 12:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| f9201ff0-769f-3ac0-a292-7c8f5cd6d89f | -12.1086 | -50.8926 | 2024-10-09 12:46:15 | GOES-16 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |
| 6e7edfd0-703e-3a81-9f49-e66071f0f333 | -12.4588 | -47.0173 | 2024-10-09 12:46:16 | GOES-16 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| c83a3028-f691-3f23-8ab4-0482f6611379 | -12.6875 | -62.9656 | 2024-10-09 12:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 42503d7e-77f6-3108-97ae-049f282a5873 | -13.288 | -53.6832 | 2024-10-09 12:46:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 39540ddf-3b89-37ee-83ff-7c13c59241bb | -13.2877 | -53.704 | 2024-10-09 12:46:22 | GOES-16 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 113.2 |
| 6d6567e0-c0a6-3d1b-9fd7-ca85e67abefd | -13.3978 | -61.9376 | 2024-10-09 12:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 9a22e7c6-e3b4-370a-823c-ad4a28d8ef24 | -13.398 | -61.9182 | 2024-10-09 12:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 29883342-1c0f-3bf9-b47c-ae723acd60bc | -13.3786 | -61.9582 | 2024-10-09 12:46:23 | GOES-16 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 88.7 |
| b7ba7dd2-0b2e-365f-955a-d0071f6469b3 | -13.8369 | -44.5691 | 2024-10-09 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 2cabfffd-0355-3725-aeed-e873733d5f48 | -13.817 | -44.5961 | 2024-10-09 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 71.9 |
| ac5fd322-0cd1-3eee-a0a6-b4911ae0e7aa | -13.9143 | -44.5788 | 2024-10-09 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| a0129348-279a-33f6-8549-83bc399aded5 | -13.8564 | -44.5657 | 2024-10-09 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 825f9446-f2c8-3578-a276-5a125e31e060 | -13.8933 | -44.6529 | 2024-10-09 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 13bf09b6-1fed-3cb7-85ac-f1dfab0c58df | -13.8364 | -44.5927 | 2024-10-09 12:46:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| ff933b55-a18f-3420-9b7f-303b9f89dfd7 | -14.8228 | -46.6419 | 2024-10-09 12:46:29 | GOES-16 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 718a823a-29f9-3342-a293-ddb1985eb66d | -15.6487 | -59.4381 | 2024-10-09 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 84.5 |
| 833d6bee-a0ae-3a2f-845e-63986ce3c1d8 | -15.6683 | -59.4163 | 2024-10-09 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 98.0 |
| 29609d45-6031-3f35-85ac-6218825cd96e | -15.688 | -59.3945 | 2024-10-09 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 109.1 |
| 2c5ef2da-5dbf-387c-8aef-32f67bc7df3d | -15.7076 | -59.3726 | 2024-10-09 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 96cc0745-6fdc-326a-a73a-38545659caff | -15.649 | -59.4181 | 2024-10-09 12:46:35 | GOES-16 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 97.8 |
| df52dcbc-62c7-320b-8633-ccbd66b27816 | -16.5661 | -57.7118 | 2024-10-09 12:46:40 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 95.2 |
| a34c29ae-9429-39cc-a382-6ca752da7f65 | -16.8358 | -56.6987 | 2024-10-09 12:46:41 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.9 |
| 8e30aa3b-7f97-3b2d-b38e-55a9c96e14f0 | -6.7614 | -60.0559 | 2024-10-09 12:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 83.3 |
| a54459d2-1856-3022-a67a-747590f69be1 | -6.7798 | -60.0552 | 2024-10-09 12:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 240.5 |
| e4fb4563-fdd9-324a-8f98-e42615d38afb | -6.7799 | -60.036 | 2024-10-09 12:55:45 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 109.5 |
| 8e849fa7-474c-3e75-9bd2-286206acc95c | -8.4919 | -48.6476 | 2024-10-09 12:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 178.2 |
| e3fc8d8d-e90e-3e48-9c47-3029a7c73d2c | -8.4921 | -48.6259 | 2024-10-09 12:55:54 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 115.5 |
| fd6d3f19-8a5e-38fc-bcab-27b057383349 | -8.5107 | -48.6459 | 2024-10-09 12:55:55 | GOES-16 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 27312cbc-c7bf-32d4-946f-1a704cf1af52 | -10.5746 | -48.0178 | 2024-10-09 12:56:06 | GOES-16 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 189.6 |
| e78aabe3-a6b1-3d92-a811-771a4cacab9d | -10.6256 | -55.9154 | 2024-10-09 12:56:07 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 7d7fb024-3bf5-3c16-b8d1-61f64ce4ab52 | -10.7434 | -50.8302 | 2024-10-09 12:56:07 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e74679ec-f531-3588-904c-1a0d80898314 | -11.3034 | -51.4069 | 2024-10-09 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 1a68d881-d142-3129-b261-cdaa2f762784 | -11.3093 | -50.9826 | 2024-10-09 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| c0798881-78d1-3c01-ba0b-8d235ee4bc49 | -11.3096 | -50.9613 | 2024-10-09 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 85d7408c-5fa7-3fb1-a8e3-35631de4332f | -11.3037 | -51.3858 | 2024-10-09 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.8 |
| 64a5fcd2-7f1b-37fc-b123-95cd45437192 | -11.2467 | -51.3918 | 2024-10-09 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 63.0 |
| cad16e91-75ed-31ca-a69e-1b4c148b5d8b | -11.309 | -51.0038 | 2024-10-09 12:56:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 72.0 |
| 9469ad2d-abb1-3c14-8c05-58603269c322 | -11.3274 | -51.0443 | 2024-10-09 12:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 34bd0b6c-5ca7-33fb-8081-f1d7d478fe50 | -11.3277 | -51.0231 | 2024-10-09 12:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 4b77fb5a-ab43-3361-93f5-3032235024f1 | -11.3235 | -51.3202 | 2024-10-09 12:56:11 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 152.9 |


[Clique aqui para ver as próximas entradas](README233.md)
