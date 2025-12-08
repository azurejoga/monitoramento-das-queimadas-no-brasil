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
| 920a5872-9c15-3dde-aafa-234a532ed846 | -2.6437 | -45.493 | 2025-12-08 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 95.7 |
| 4d1065d9-e532-36e4-a8e8-d1e5a7b16d29 | -2.6623 | -45.4924 | 2025-12-08 00:00:00 | GOES-19 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 0f8bbe15-23ee-397d-8e63-7597e8eb9a9c | -2.253 | -45.7285 | 2025-12-08 00:00:00 | GOES-19 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 88c5ef13-d355-3dfb-a839-ea8d0a62f476 | -2.7243 | -43.9921 | 2025-12-08 00:00:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 3859685c-d508-34f4-9497-d043b83ac16c | -2.7429 | -43.9915 | 2025-12-08 00:00:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 129.2 |
| 86b0a8c5-1f29-3034-bbab-5585b4539d96 | -3.7394 | -45.6523 | 2025-12-08 00:00:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 76.7 |
| cd602725-5632-32a3-b57f-6a1df6ee0af9 | -2.7242 | -44.0151 | 2025-12-08 00:00:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 6bf55996-4c75-399d-93fc-6c92c7e2346f | -2.7428 | -44.0145 | 2025-12-08 00:00:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 162.9 |
| b6982f83-5099-34ec-957e-ffe66fe59a29 | -2.6381 | -46.9575 | 2025-12-08 00:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| f044656b-0889-327d-b6d9-49a74a1b17b7 | -1.714 | -46.12 | 2025-12-08 00:00:00 | GOES-19 | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 48a91606-45c9-3181-9210-fc923780fcc4 | -2.7242 | -44.0151 | 2025-12-08 00:10:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 107.0 |
| ce52c343-fd52-3bd3-baec-d9af58f69e5b | -2.7428 | -44.0145 | 2025-12-08 00:10:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 113.9 |
| e1fbd6a9-b59f-3cf5-8c38-7913fc12c895 | -6.5631 | -51.1126 | 2025-12-08 00:10:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 32e07d50-c20b-317f-9d26-9b562f6fa350 | -2.4449 | -49.2731 | 2025-12-08 00:20:00 | GOES-19 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 34acc748-7ecb-35ef-9d86-a8fe902e6283 | -2.7428 | -44.0145 | 2025-12-08 00:20:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 29b17f93-c5dc-3e66-89d1-f02e90594e06 | -2.6381 | -46.9575 | 2025-12-08 00:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| c9f35e3f-6cbb-35a7-a67d-ef8bf21d49f3 | -2.7242 | -44.0151 | 2025-12-08 00:20:00 | GOES-19 | ICATU | MARANHÃO | Brasil | 2105104 | 21 | 33 | nan | nan | nan | Amazônia | 95.8 |
| 2ac83a13-37f4-3002-adf3-989df10e8360 | -2.6381 | -46.9575 | 2025-12-08 00:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 53a05597-8db6-3b27-8c58-d043f4e6c067 | -3.7394 | -45.6523 | 2025-12-08 00:40:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 56.4 |
| df857d68-e465-3643-b339-a6cfa98f5b4b | -2.6381 | -46.9575 | 2025-12-08 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| fbe237fb-1155-31ad-8bfc-da9df919291d | -2.6381 | -46.9575 | 2025-12-08 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.3 |
| e802a1b5-1cb7-33b5-bd36-691041e708ef | -2.6381 | -46.9575 | 2025-12-08 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 6b61c642-b9fc-3c29-8dfe-662a6051d268 | -2.6381 | -46.9575 | 2025-12-08 01:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 81.1 |
| 7372199d-18c6-3bee-9336-f78999be76d9 | -9.9696 | -36.2531 | 2025-12-08 01:20:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 84.0 |
| d3bd8de8-c4a3-3c2a-9203-370a710e316f | -2.6381 | -46.9575 | 2025-12-08 01:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 85.5 |
| f1cf8999-2d1f-39d2-8713-c8f49a9d2abb | -9.9696 | -36.2531 | 2025-12-08 01:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 110.2 |
| 54edecbc-e94a-3ced-9f27-6f9ad392efbe | -2.6381 | -46.9575 | 2025-12-08 01:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| d2a3429d-a79f-391a-b28c-74d3f1292143 | -3.7394 | -45.6523 | 2025-12-08 01:30:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| fec74695-b80a-32dd-bf6f-8b506b4ee797 | 3.31139 | -60.83103 | 2025-12-08 01:34:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3310f5db-05b6-33e0-b9ba-dad6f1015655 | -2.6381 | -46.9575 | 2025-12-08 01:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 75.6 |
| d7b51797-4138-3367-a654-384625fe3e53 | -3.7394 | -45.6523 | 2025-12-08 01:40:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9c450a2f-85c7-39dd-a708-9dbed82e13c7 | -3.7394 | -45.6523 | 2025-12-08 01:50:00 | GOES-19 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 59.0 |
| 67567626-b605-33ef-a476-a035289ac84f | -2.6381 | -46.9575 | 2025-12-08 01:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| fdac01fe-5ffd-3b3d-96bd-af5ad8d08eb9 | -2.6381 | -46.9575 | 2025-12-08 02:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 33325f94-8db8-3ee8-b52b-6111d7dd5ed3 | -2.6381 | -46.9575 | 2025-12-08 02:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 30009a5b-b268-3fb4-8a58-fdfbee73ef6a | -2.6381 | -46.9575 | 2025-12-08 02:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| f3c14056-174f-3a6d-8785-4b95a8088936 | -7.80909 | -35.29567 | 2025-12-08 03:04:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| fd368235-bc47-3cd4-a99e-c29a37549809 | -7.81119 | -35.29559 | 2025-12-08 03:04:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| db984f30-40de-3587-aba0-8762480b0e52 | -7.41313 | -35.18574 | 2025-12-08 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 26e35653-50fe-3166-a2de-c5155f12c5e0 | -7.43429 | -35.22131 | 2025-12-08 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 1a7310af-c4af-3fd5-a99e-aeddbeb5ef8a | -8.08379 | -35.24643 | 2025-12-08 03:04:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| eb568f1f-1699-3bb4-af80-09a8447fd53c | -7.80586 | -35.29456 | 2025-12-08 03:04:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| d0a00bc7-cf26-3bc0-b5cc-6a6f9ad507f1 | -7.41374 | -35.18241 | 2025-12-08 03:04:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 1afc65ac-b646-36d8-be59-ca8a1643f06a | -7.80376 | -35.29462 | 2025-12-08 03:04:00 | NOAA-21 | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 97348f09-dad3-31f9-b9d2-272b33c3ff6e | -10.14689 | -36.3729 | 2025-12-08 03:06:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 354ce8cf-c1fd-309f-afaa-5fb580907f79 | -10.14619 | -36.37663 | 2025-12-08 03:06:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 82d4241f-19d0-3f32-9466-268c2ae9af62 | -10.1821 | -36.215 | 2025-12-08 03:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.5 |
| e1daebf7-5d16-3347-b34d-85cd98d42f34 | -6.73488 | -34.97828 | 2025-12-08 03:34:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 4bc22962-9bf2-3b46-85c2-86cb345a3639 | -3.97665 | -42.51076 | 2025-12-08 03:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d86da7c9-93ab-3482-bde2-5773ec5ed539 | -10.17856 | -36.21793 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 10152d4e-8b3a-36e5-acfd-f7b2f61e0cdf | -10.14848 | -36.37657 | 2025-12-08 03:34:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| c22cdbb2-4c18-34d1-9eca-39d5db696015 | -7.4204 | -35.18486 | 2025-12-08 03:34:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| dc5afc1d-0b35-396e-bd00-dfd745e690d6 | -7.41261 | -35.18771 | 2025-12-08 03:34:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| dbc0ac0e-345e-3fdb-a78d-31a753e0d627 | -6.2677 | -37.67765 | 2025-12-08 03:34:00 | NPP-375D | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b9f8759a-f138-3072-a729-3fda7129e276 | -10.18443 | -36.22771 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 9fab7a63-f17b-3f37-a3ee-b7315f5292e8 | -5.64488 | -40.68062 | 2025-12-08 03:34:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 0cef5866-7d82-373c-87de-9a7a7939cdef | -10.18513 | -36.22344 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6022a6c5-7b9c-355e-8966-93d6b9c2427a | -10.18583 | -36.21919 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| dd9e5bdd-d590-3dd4-9995-b92cd9d9069f | -10.18506 | -36.22157 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1c742df1-33e4-3c5c-a1b8-ec98da9cc447 | -10.1822 | -36.21856 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5522f11d-6b35-342a-ad26-5599e7daa506 | -10.17422 | -36.22155 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 132.4 |
| 4a3d867d-1b25-377f-95e0-413214d86633 | -6.63808 | -39.11948 | 2025-12-08 03:34:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 303e9d49-cfa4-3673-9519-09daff63e7b5 | -5.08738 | -43.66147 | 2025-12-08 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9756bf73-6be4-3706-a8cb-e15d69396a5f | -6.60183 | -39.53255 | 2025-12-08 03:34:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 2fc4cca3-14c0-344a-8e08-ef8e1599b02b | -10.17785 | -36.22218 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 9e0f44fd-4c14-38c6-9b74-873abf1dc42e | -10.1829 | -36.2143 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 6535693e-3399-33a4-9ff4-c717045a2b0f | -7.41617 | -35.18834 | 2025-12-08 03:34:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 3e1c88bf-2118-36d5-9f7d-5a6229b6ff0a | -7.80976 | -35.29521 | 2025-12-08 03:34:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bef8102c-d6c6-312c-8948-4525421b46f5 | -10.17129 | -36.21666 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 132.4 |
| 6b41a240-651f-3b29-b9f5-8b80419bab02 | -3.97061 | -42.50976 | 2025-12-08 03:34:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| fe11c223-04fa-3aca-8427-96227e1caed1 | -10.18579 | -36.21732 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 053e9ca4-e3b0-3ee1-80c8-8c08c404bac5 | -10.16765 | -36.21603 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 50a0a093-32d9-3317-b959-8c6c2f84bbda | -10.18288 | -36.21244 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 456e673b-b594-3400-b331-4da9c9b89036 | -5.08828 | -43.65639 | 2025-12-08 03:34:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f028a6f5-1db4-3832-9e65-6a939c2bff20 | -10.17563 | -36.21304 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 61b9d362-6400-3d0f-829a-2c9bff614aa3 | -6.66383 | -35.10992 | 2025-12-08 03:34:00 | NPP-375D | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 71d04a71-5e89-30ca-86b0-123044d64714 | -10.17926 | -36.21367 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 0b495959-9364-3b1b-8ed5-31176a606634 | -10.18215 | -36.21669 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1ff7817f-e3d1-3e21-8c93-7d7f3e09e0e9 | -10.18142 | -36.22094 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67ca3329-32d7-32bf-bdea-2582c4fa24aa | -5.26933 | -37.90422 | 2025-12-08 03:34:00 | NPP-375D | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 02dc808e-c6f5-3db1-b21a-aaf0e8480fc6 | -10.14482 | -36.37591 | 2025-12-08 03:34:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 14ffd2a7-16fe-387c-83a8-1a728720d82e | -6.63347 | -39.11869 | 2025-12-08 03:34:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 1ea92579-1532-3db0-9e08-ec35113aac6d | -10.14555 | -36.37151 | 2025-12-08 03:34:00 | NPP-375D | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| d40c248e-e0be-361b-a2e5-0614ca4dc795 | -5.64428 | -40.68399 | 2025-12-08 03:34:00 | NPP-375D | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| e4389925-1a7f-38b1-a97a-71523bac09bf | -7.41684 | -35.18426 | 2025-12-08 03:34:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 455f4bae-ac66-35c8-808b-5601e0b10544 | -10.18361 | -36.21004 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 289e0826-624f-3a40-88dc-85df5abaede8 | -7.80618 | -35.2946 | 2025-12-08 03:34:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| ff190f40-05d0-396a-99c9-b9301d1c26a7 | -10.17058 | -36.22092 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 132.4 |
| 2795bcfb-b295-3ec7-a2f4-8b8b039e77ca | -7.80261 | -35.29399 | 2025-12-08 03:34:00 | NPP-375D | CARPINA | PERNAMBUCO | Brasil | 2604007 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8ce77b1a-83c3-3c83-8ca5-cba84c68a580 | -10.18149 | -36.22281 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| b8cd6ed0-8025-3df6-a0f4-630f6cf0ab66 | -10.17634 | -36.20878 | 2025-12-08 03:34:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 6dd456ca-6c79-3f05-bfb0-32728c64e6c2 | -11.48815 | -37.94236 | 2025-12-08 03:36:00 | NPP-375D | RIO REAL | BAHIA | Brasil | 2927002 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| fc887086-4bf7-3b45-b6c9-2a2c67737672 | -2.63636 | -46.96897 | 2025-12-08 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 1ad3bb51-5ff0-39e4-88b7-9fe237c8df48 | -4.44825 | -44.14045 | 2025-12-08 03:53:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b4fbeff1-6cd6-341b-abc2-fa2d9f617084 | -3.4708 | -44.8881 | 2025-12-08 03:53:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 924090d6-d7a8-36e5-b9b0-cbe0fd6ac2bb | -2.63754 | -46.96183 | 2025-12-08 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e5b457fa-f791-3842-b0c0-e75d2217139a | -1.76189 | -45.86293 | 2025-12-08 03:53:00 | NOAA-20 | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| c9f001cf-1b36-370f-8aa0-192b3aec68de | -5.14279 | -38.07141 | 2025-12-08 03:53:00 | NOAA-20 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 0ce0d29e-cee2-36ee-b6ab-228d20ce127f | -5.08681 | -43.65669 | 2025-12-08 03:53:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1730929e-fc46-3280-bf03-5b56174eace9 | -3.39407 | -44.16184 | 2025-12-08 03:53:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README2.md)
