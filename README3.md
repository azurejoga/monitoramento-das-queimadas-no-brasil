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
| c0ed8778-3075-32f0-816e-fb7a8c067bc8 | -15.21873 | -57.65561 | 2026-04-29 05:25:00 | NOAA-21 | LAMBARI D'OESTE | MATO GROSSO | Brasil | 5105234 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2fd4e0a6-860c-3470-b22f-aa317bb33903 | -18.29044 | -54.60716 | 2026-04-29 05:27:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82ca1a4b-1c13-3ea7-a894-91398ef485ef | -21.24743 | -49.16934 | 2026-04-29 05:27:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b9e14f72-d287-3d5a-bec9-5d776fca0945 | -21.25239 | -49.16962 | 2026-04-29 05:27:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 556f4e60-cf40-3b23-a370-c7bf74dd40e0 | -18.03446 | -53.02472 | 2026-04-29 05:27:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2b7e6434-f4aa-30d3-b8f9-f6e7beee995e | -21.24693 | -49.17693 | 2026-04-29 05:27:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| caec0aac-a94e-3e9f-9cad-ad2bb9c86be0 | -21.25463 | -49.17016 | 2026-04-29 05:27:00 | NOAA-21 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 268d8a0a-256a-353f-97c1-fe4c5fa645a0 | -21.25187 | -49.17688 | 2026-04-29 05:27:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| fd119df2-f2db-3120-b19a-aabf038f9c59 | -11.37724 | -56.49634 | 2026-04-29 06:50:00 | AQUA_M-M | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 34fe5e2b-fe8a-3b2e-ba60-192d6619f98e | -12.0178 | -45.34054 | 2026-04-29 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 8a60b33e-80d1-315f-8129-3165ea6ab6ba | -9.47313 | -46.11804 | 2026-04-29 11:42:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 58c12181-6a17-3cd4-b4bf-c83de11f8814 | -9.47146 | -46.12898 | 2026-04-29 11:42:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| d9db6afa-22d1-3103-86e3-0338676a9d1c | -12.01922 | -45.33097 | 2026-04-29 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| eff3cf12-dfcb-34d9-a47d-1e41dc31a3ef | -8.94486 | -45.66445 | 2026-04-29 11:42:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| f410f517-3e85-3427-ab09-0134cac852f3 | -12.01638 | -45.35012 | 2026-04-29 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| df6d9208-b85e-385e-9970-367e54ae9fe8 | -12.36969 | -50.01646 | 2026-04-29 11:42:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 43.0 |
| caeac0ad-03b8-3e81-989e-c621782a6106 | -12.36655 | -50.03531 | 2026-04-29 11:42:00 | TERRA_M-M | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 36.8 |
| 98acb0cd-f875-35fe-a642-217fc14d584b | -12.02691 | -45.34191 | 2026-04-29 11:42:00 | TERRA_M-M | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7d91f083-3d6a-3a67-879e-a0e4855b636d | -8.54196 | -44.32413 | 2026-04-29 11:42:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| adbc8d1e-9451-3ae8-8619-7aa47e0eb77a | -9.46338 | -46.11653 | 2026-04-29 11:42:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 72.5 |
| bf9eed6b-2d3a-3001-bc7c-336ab27f3aa9 | -13.18637 | -41.10242 | 2026-04-29 11:42:00 | TERRA_M-M | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 948a88bb-62d6-3999-89bd-47488404aef3 | -9.46172 | -46.12743 | 2026-04-29 11:42:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 120d80ce-a0fd-3eed-b276-af89a21849e3 | -17.2643 | -47.07796 | 2026-04-29 11:45:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0185951e-c3f4-39a4-ab6e-065f69000b54 | -18.72312 | -46.90183 | 2026-04-29 11:45:00 | TERRA_M-M | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 006d2934-4d60-3ad4-ae8a-088932fb2043 | -16.23123 | -45.48203 | 2026-04-29 11:45:00 | TERRA_M-M | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 63c2f33d-06b1-3efe-971b-9d45c5246c08 | -17.67686 | -46.73516 | 2026-04-29 11:45:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| ebc2496e-9459-3c62-977f-46bc476df75a | -20.21925 | -46.461 | 2026-04-29 11:45:00 | TERRA_M-M | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 27dd10bc-4aa7-3c54-b4b3-aedae70b2dcb | -18.72462 | -46.89191 | 2026-04-29 11:45:00 | TERRA_M-M | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 64dfb849-64e9-3aed-8969-8cf526562f52 | -17.26271 | -47.08828 | 2026-04-29 11:45:00 | TERRA_M-M | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| ca397043-1732-3d8f-add1-7e1bc894c3aa | -17.67534 | -46.74512 | 2026-04-29 11:45:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1d4f0613-caf0-3830-88a9-71ab7b4b262c | -17.75594 | -43.42663 | 2026-04-29 11:45:00 | TERRA_M-M | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 19957777-a81f-3693-97f8-bb0b35cdb512 | -16.22986 | -45.49134 | 2026-04-29 11:45:00 | TERRA_M-M | URUCUIA | MINAS GERAIS | Brasil | 3170529 | 31 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 17dfef55-30d8-3ea7-81fe-0d9489567c58 | -31.39274 | -53.70566 | 2026-04-29 11:47:00 | TERRA_M-M | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 12.0 |
| 8b9d4710-23a7-3203-bd8b-b6f80772bc55 | -31.38991 | -53.71649 | 2026-04-29 11:47:00 | TERRA_M-M | CANDIOTA | RIO GRANDE DO SUL | Brasil | 4304358 | 43 | 33 | nan | nan | nan | Pampa | 11.7 |
| c6f1a4c5-5069-3fb2-ad1b-fd0e99784ade | -12.37 | -50.0242 | 2026-04-29 12:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 93f09b8e-06ef-309f-9cb8-f5e6e1eae78d | -9.4658 | -46.119 | 2026-04-29 12:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 115.7 |
| af45c5a4-ae3a-3052-b1af-dd729030716c | -9.4658 | -46.119 | 2026-04-29 13:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.3 |
| 657c6d9a-5fcf-3615-b016-fddc407d2ff4 | -12.37 | -50.0242 | 2026-04-29 13:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 25716640-0afc-35bf-b3a5-05fd8f4763f6 | -9.4658 | -46.119 | 2026-04-29 13:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 82295744-2c66-3d48-8777-26dea83eedd6 | -12.37 | -50.0242 | 2026-04-29 13:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 106.7 |
| 6517d94d-2524-305a-854b-af5202d9ee1a | 1.10551 | -60.53436 | 2026-04-29 13:16:00 | TERRA_M-T | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f27dad06-3eb9-3b13-8245-914fcea9b61d | -4.64286 | -59.57352 | 2026-04-29 13:18:00 | TERRA_M-T | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 6beac610-3448-3765-8401-0ed464764522 | -12.0097 | -45.3315 | 2026-04-29 13:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 72.6 |
| d8e98f19-0006-3abb-8c45-684898c0c421 | -9.4658 | -46.119 | 2026-04-29 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 84719f28-47ae-3e95-a71c-a7ddd4144352 | -14.24693 | -59.14324 | 2026-04-29 13:23:00 | TERRA_M-T | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 27.2 |
| fa3d035d-6bc1-384f-8c36-1df32146025a | -9.4658 | -46.119 | 2026-04-29 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| b1e4c29c-82a9-3a35-8c7b-627732bf102d | -12.37 | -50.0242 | 2026-04-29 13:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 88.5 |
| c88ec14a-05d9-37a2-9a4d-354ee848a988 | -12.37 | -50.0242 | 2026-04-29 13:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 535b2dbc-9ee6-3c31-8a3d-29289d63e39d | -17.2677 | -47.0785 | 2026-04-29 13:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 72.4 |
| cee66cae-c6b5-3790-b0a8-b17c022c200d | -9.4658 | -46.119 | 2026-04-29 13:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 131.0 |
| de0a26be-33b5-383b-8462-dd2627b46bf2 | -9.4658 | -46.119 | 2026-04-29 13:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 2fcb55ae-e5f1-3b7d-a63e-238eda080e03 | -12.37 | -50.0242 | 2026-04-29 13:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 9b7d3310-0d08-3479-8cea-ddccbaf46b33 | -9.4658 | -46.119 | 2026-04-29 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.7 |
| e2a84a0a-2cd1-3dce-a257-818ffc3eddd2 | -12.37 | -50.0242 | 2026-04-29 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 72.0 |
| d790a1e1-6bd6-3b9a-b840-1e2218880a2e | -9.4658 | -46.119 | 2026-04-29 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 124.9 |
| 57377d96-27ff-3efd-ba04-bb5b59413ed1 | -12.0097 | -45.3315 | 2026-04-29 14:10:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 1ba00ca2-b9c1-36d6-afe8-7548ba385ae7 | -12.37 | -50.0242 | 2026-04-29 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 6fba90ee-73e8-37fa-ba84-ae8ee9b029b2 | -9.4658 | -46.119 | 2026-04-29 14:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 8e2b0653-870d-321c-b63a-773e2cc290b8 | -17.2677 | -47.0785 | 2026-04-29 14:20:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 1489c992-6d1c-3e47-b64d-1c6b1fdaf1cf | -17.2677 | -47.0785 | 2026-04-29 14:30:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 977b70d5-2570-3fec-b55a-26ec856df296 | -9.4658 | -46.119 | 2026-04-29 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 102.7 |
| faa5e538-ccff-3926-9503-5477a721c6e3 | -17.2677 | -47.0785 | 2026-04-29 14:40:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 87.0 |
| c332fad9-51ec-3eeb-83c3-46a84e51eff5 | -17.2677 | -47.0785 | 2026-04-29 14:50:00 | GOES-19 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 82.6 |
| fa09e2e0-84e6-3b0f-8c99-980fc76e28d0 | -9.4658 | -46.119 | 2026-04-29 14:50:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| c8d38ea4-3a57-3282-b1cf-8d48ef7ea472 | -10.6302 | -46.8348 | 2026-04-29 15:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 93.1 |
| 6bc9ac5e-21c3-390f-915e-5ad0a50e8324 | -9.4658 | -46.119 | 2026-04-29 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 1cca4bf7-8b26-3212-a14c-a047aa174645 | -10.6302 | -46.8348 | 2026-04-29 15:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 143.3 |
| 99b2cc40-06e0-3f4c-9771-490da6d0770b | -10.6112 | -46.8372 | 2026-04-29 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 118.6 |
| 6b80825e-e842-3b72-8bdf-e1da7d751945 | -12.37 | -50.0242 | 2026-04-29 15:30:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| b57e5622-a966-3543-badd-f6ffb1f9b46d | -10.6302 | -46.8348 | 2026-04-29 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| c1d9dd02-34c5-3d97-a2a4-b74f826afda5 | -12.37 | -50.0242 | 2026-04-29 15:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |


