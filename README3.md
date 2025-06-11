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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2af80e46-58bc-376b-896e-fa5b6ce07679 | -10.2432 | -52.234001 | 2025-06-11 01:04:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 511874ae-379b-3efd-9c04-8f703b39f6d1 | -11.0561 | -55.039101 | 2025-06-11 01:04:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c9ad2fc-e7b4-3774-b529-667a5ced5656 | -4.5558 | -48.019901 | 2025-06-11 01:04:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 06ab2a6d-944e-389d-b873-acfab1a6dad2 | -7.4848 | -45.513401 | 2025-06-11 01:04:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c7b5e51b-7153-345d-8d38-05a91e3e418c | -21.041201 | -55.632301 | 2025-06-11 01:04:00 | METOP-C | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| d469c5c1-122d-3641-b0f4-66531b1607a2 | -20.105 | -50.8694 | 2025-06-11 01:04:00 | METOP-C | SANTA CLARA D'OESTE | SÃO PAULO | Brasil | 3546108 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 2372b472-5a1f-3b6d-831e-b78e4e164280 | -11.1399 | -53.942001 | 2025-06-11 01:04:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9945745d-9900-31b5-ab1b-82ad6e9ef2dd | -10.1933 | -49.581299 | 2025-06-11 01:04:00 | METOP-C | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| bc922e2d-9f42-3ca9-92ae-8e5695a1e257 | -10.2449 | -52.241299 | 2025-06-11 01:04:00 | METOP-C | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e543bb55-eafb-34bc-a74f-ade521e847a8 | -10.6492 | -49.4267 | 2025-06-11 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 9b9f2b79-370e-33b3-b66d-c934b0b49184 | -7.4763 | -45.5099 | 2025-06-11 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ead21bc5-ace8-3b4a-bba0-fbe8695b8a54 | -7.4575 | -45.5116 | 2025-06-11 01:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 121.0 |
| 63114916-f19a-3e18-a616-a65907ec4fca | -10.6681 | -49.4246 | 2025-06-11 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 37.9 |
| e9b7ba7f-a55f-3907-bfb1-44f96313ab14 | -21.81932 | -57.5465 | 2025-06-11 01:15:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 70f9f4c3-922d-3030-a6e6-2169d61e545a | -20.54544 | -54.12834 | 2025-06-11 01:17:00 | TERRA_M-M | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4641ccfc-b066-3eac-a9b5-771523163741 | -21.04441 | -55.63382 | 2025-06-11 01:17:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 17.3 |
| 4e160a39-0001-3ba2-a9fc-e6c0deb74687 | -14.03337 | -55.14071 | 2025-06-11 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f0c4a592-36e3-3683-8402-5087ba15ea2e | -16.29332 | -49.93699 | 2025-06-11 01:17:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| c38fc36b-ed9b-3138-b6dc-e4609d13b691 | -14.66989 | -53.37422 | 2025-06-11 01:17:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1fe5a8d4-bb52-3fd0-a91c-89d1559f7864 | -13.58693 | -54.28913 | 2025-06-11 01:17:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 082e026c-a0ba-312e-b456-e658c3158b25 | -13.09014 | -52.29129 | 2025-06-11 01:17:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 00816842-86ad-3195-b595-bf9b9a239456 | -21.04311 | -55.62439 | 2025-06-11 01:17:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 762d5025-7ed9-328e-85ca-e0239dcc8cef | -13.58973 | -54.28288 | 2025-06-11 01:17:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bc64a454-5800-33f8-a1d6-fa4f1d17b151 | -12.78653 | -48.73085 | 2025-06-11 01:17:00 | TERRA_M-M | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| 5241bfdb-b7e5-38ef-a3a9-7decf29e8c5f | -14.67175 | -53.3862 | 2025-06-11 01:17:00 | TERRA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 28.1 |
| a17111cc-a2d9-37c9-a63d-0e8dcfb6da21 | -16.29272 | -49.9434 | 2025-06-11 01:17:00 | TERRA_M-M | ANICUNS | GOIÁS | Brasil | 5201306 | 52 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 4c40de59-9296-326d-a09d-8b13b5b16045 | -13.09033 | -52.297 | 2025-06-11 01:17:00 | TERRA_M-M | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 3b7cba81-3aa5-3efa-bb5c-ded1492142e1 | -14.04252 | -55.1392 | 2025-06-11 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a189d919-d86b-3f12-983e-e39f4655b7b5 | -14.03193 | -55.13086 | 2025-06-11 01:17:00 | TERRA_M-M | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 26210557-2f6c-3987-b4ee-ee5d18e5583d | -10.6681 | -49.4246 | 2025-06-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0f93693d-7c75-30d2-9610-98820c65cd7f | -7.4575 | -45.5116 | 2025-06-11 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 172.0 |
| 985d5c4e-fe42-31f2-bf7d-4c341109410f | -7.4763 | -45.5099 | 2025-06-11 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 94.2 |
| 6bdbaf68-d82f-3346-886f-623695c7f5da | -7.4387 | -45.5133 | 2025-06-11 01:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.9 |
| 17c722f2-7918-391e-b0c8-bdb38158ae5f | -10.6492 | -49.4267 | 2025-06-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 8fa72c91-fdac-3133-9d50-23fa129d1689 | -12.52853 | -57.20467 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| fd64fd02-3501-35da-bda7-0cbe1019cc1f | -12.52346 | -57.23291 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| ef20f621-32ba-3ea9-8663-57ced70ce56f | -11.91504 | -54.83521 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1adbb34c-1229-35bb-86e0-498201763e45 | -10.65511 | -49.43517 | 2025-06-11 01:20:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 7df42ff1-0f13-37a6-ae72-1706727941c0 | -10.86765 | -54.32611 | 2025-06-11 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 0c9be83f-5ec8-39c9-95b7-47487a743351 | -12.52097 | -57.21495 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 21.8 |
| 96ebeeb5-1d5a-3e21-b230-95cb7714394d | -11.90398 | -54.82619 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 7827676d-1bfb-379e-9703-88adeee146fb | -10.88771 | -54.7442 | 2025-06-11 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38f0e00d-3230-392b-94b7-701c4caa49b5 | -9.78515 | -57.42478 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b42f1cf3-ca23-32d3-a446-3fb0e0e8a73f | -10.69762 | -49.51067 | 2025-06-11 01:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 39.1 |
| d79694b4-8430-3ddf-ae49-005b199c9dc0 | -12.2016 | -54.27419 | 2025-06-11 01:20:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| cd520c7c-aafd-3244-b56b-a665d07c332e | -11.91351 | -54.82471 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 17.7 |
| d96b4ac6-42b4-3816-a238-1bbe6aafc5aa | -13.22777 | -57.12603 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c97e9198-855f-387c-997b-68dc025f8113 | -10.878 | -54.74568 | 2025-06-11 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 32.2 |
| ef52841a-3514-391f-ac3d-ea959e04add8 | -12.51464 | -57.23421 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 41b6d030-cc35-39a8-aec5-03ec874646cd | -10.23726 | -52.23692 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 27.2 |
| a5f0e2de-ebbd-3446-bd48-1fd47abd8332 | -11.0465 | -55.0366 | 2025-06-11 01:20:00 | TERRA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2123320d-be03-38bc-95bb-03efc3071f58 | -12.20263 | -54.26772 | 2025-06-11 01:20:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| ad30ce5e-7a7f-38bc-82bc-8a9318aafd45 | -9.86284 | -57.64398 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0ff603f2-afd5-3c62-aa47-99e87749d81c | -12.28155 | -57.27151 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| cbc3ed31-6e31-3b2d-8b17-2fc80d02deb6 | -11.3786 | -56.55784 | 2025-06-11 01:20:00 | TERRA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e036369f-ceb3-3945-988a-37b5de0ba1e4 | -11.14513 | -53.92835 | 2025-06-11 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| fe37f7ce-36c9-3685-9b4e-2336ebd0135e | -11.90552 | -54.8367 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 59b2af05-d55e-3742-8f43-888641449d75 | -10.69873 | -49.50393 | 2025-06-11 01:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 3ce105e6-ebe8-35f7-a545-77074d27fac4 | -9.77632 | -57.42606 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 3f5ddd74-858c-3519-a749-94e962dc5f86 | -11.77793 | -54.37786 | 2025-06-11 01:20:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 36b54180-a152-3ba3-8a0c-539cc846677f | -10.70335 | -49.53074 | 2025-06-11 01:20:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 634dc309-de4c-372c-9bcc-00641ffadbff | -12.19994 | -54.26296 | 2025-06-11 01:20:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 171eb9be-c4ae-3c03-b20f-9458adc4d45b | -12.52221 | -57.22393 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 36.8 |
| 889b9b93-16af-35da-83ad-0a8c4900ede0 | -12.26316 | -57.61032 | 2025-06-11 01:20:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 24.9 |
| d9072879-5458-3c34-b6f4-dbd38fcff0d0 | -10.07328 | -52.75235 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 21.1 |
| 8f7632c8-1369-3688-b39c-b8c5405861c0 | -12.13703 | -54.6619 | 2025-06-11 01:20:00 | TERRA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 288c994e-fd33-361a-b7db-04cf821732e7 | -10.8796 | -54.75659 | 2025-06-11 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| cac0829a-306c-373b-bc4f-9d8f4ab0c750 | -9.82281 | -61.40369 | 2025-06-11 01:20:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 35902ac0-63ec-39aa-85a8-5480d430557e | -10.24355 | -52.22937 | 2025-06-11 01:20:00 | TERRA_M-M | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 16.3 |
| b298d19f-dd5d-357c-bd14-69eaaad541f9 | -10.87761 | -54.32451 | 2025-06-11 01:20:00 | TERRA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e9ff8aa2-f418-310a-ba4e-07e60c92660a | -7.4763 | -45.5099 | 2025-06-11 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 107.9 |
| 3fedfe8a-c095-3532-b589-1d03ebb55e8f | -7.4577 | -45.489 | 2025-06-11 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 4fcca6b3-1d73-387d-9731-06d411c10d09 | -7.4387 | -45.5133 | 2025-06-11 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 45.5 |
| d101ec31-f5d5-3595-9af6-2d6efd88f769 | -10.8832 | -54.742 | 2025-06-11 01:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| dd289720-00c7-363a-abc6-0fa409a59c4f | -10.6492 | -49.4267 | 2025-06-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 620de733-ecf0-3fa9-89dd-fa28562a3d87 | -10.6681 | -49.4246 | 2025-06-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 2212737e-ae5d-327f-a6cb-a196e963bd18 | -7.4575 | -45.5116 | 2025-06-11 01:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 164.5 |
| d739dac4-a495-392c-a865-d903e1a23a1e | -7.4575 | -45.5116 | 2025-06-11 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 139.4 |
| 8c7d8588-9cdb-3277-93fb-81c72cefb736 | -10.6492 | -49.4267 | 2025-06-11 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 44.2 |
| 47d1d05a-c3f9-37ba-a511-e8386ae925f8 | -10.6681 | -49.4246 | 2025-06-11 01:50:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 48.0 |
| b9dd503f-040a-35f3-8e43-25652dda796d | -7.4763 | -45.5099 | 2025-06-11 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| ed51fa5b-4d4f-32fb-a099-f185fa93fce4 | -7.4387 | -45.5133 | 2025-06-11 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 7aa30247-e5e4-3704-ae1d-302cb892a64a | -10.6492 | -49.4267 | 2025-06-11 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 93e04cd0-d9fc-3005-b572-ee06ab359672 | -7.4575 | -45.5116 | 2025-06-11 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 121.1 |
| 374e44b6-34b7-3835-8ecb-3eed5bd4dbea | -7.4763 | -45.5099 | 2025-06-11 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 56.2 |
| 655b8c06-4f16-37eb-853d-9854eac07944 | -7.4387 | -45.5133 | 2025-06-11 02:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| e694933a-b05e-3ed2-9993-d01d23e21284 | -10.6681 | -49.4246 | 2025-06-11 02:00:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.3 |
| c73d879b-b775-373d-b8a9-845ac461dbad | -10.6681 | -49.4246 | 2025-06-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 35.7 |
| 6c957782-68f7-3c45-b649-e61e806476d1 | -7.4575 | -45.5116 | 2025-06-11 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 98.9 |
| 9f37674e-b001-3d97-8b07-c489d2b3a939 | -10.6492 | -49.4267 | 2025-06-11 02:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 40.5 |
| b9897079-27d5-3d6e-bb0f-7c95a2e1d32d | -7.4763 | -45.5099 | 2025-06-11 02:10:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 514e584c-be54-3098-b874-ed57f13ba92f | -7.4763 | -45.5099 | 2025-06-11 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 63f92360-06ce-3b71-9e03-cc16b671b290 | -10.6492 | -49.4267 | 2025-06-11 02:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 43.3 |
| 656638cf-8d6e-3e0c-8146-fb9b6785aee9 | -7.4575 | -45.5116 | 2025-06-11 02:20:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e0ec164f-af20-3428-8cf2-bf62fde6c36b | -10.6681 | -49.4246 | 2025-06-11 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 39.5 |
| c609d784-b163-3d75-a539-e80e725ae964 | -7.4763 | -45.5099 | 2025-06-11 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 51.6 |
| a7e4bd0f-c5f5-3843-96d6-91050f8d35c3 | -10.6492 | -49.4267 | 2025-06-11 02:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 42.5 |
| ae0fd01e-f96f-3c2f-b69c-d278928f34ac | -7.4575 | -45.5116 | 2025-06-11 02:30:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| a28e561f-7343-3537-b769-17ec5daa718a | -7.4575 | -45.5116 | 2025-06-11 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 8ef095c5-8390-375f-8f12-2e2c866d04ab | -7.4763 | -45.5099 | 2025-06-11 02:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 52.4 |


[Clique aqui para ver as próximas entradas](README4.md)
