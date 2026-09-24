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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 488a72d7-2e86-32b1-8ae1-783d435beb26 | -4.83418 | -42.89327 | 2026-09-24 04:44:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7108a229-98dd-3be0-a946-e5c14fcbcbcb | -7.39504 | -44.77235 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eca1082c-05b8-39e6-9b40-920d5e494eb6 | -3.68808 | -60.56593 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7f126027-4b0d-333b-bdcb-f71f0a807b72 | -7.52694 | -45.20667 | 2026-09-24 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1fd8125f-d0d5-3aab-a749-97da0c30b5dc | -1.27727 | -57.03888 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ec8e2ec-8ff3-3a0a-851a-ed270002bab4 | -7.50514 | -39.2736 | 2026-09-24 04:44:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 853daed7-9322-322e-a954-9ddb14b25415 | -3.44646 | -50.08126 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 11fa1664-5e7e-377c-8aaf-46b1ba410716 | -5.5754 | -42.30011 | 2026-09-24 04:44:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 0eab657e-db72-36bb-9aef-4cff049e3182 | -1.33097 | -47.78415 | 2026-09-24 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbba296b-1666-3687-9ef2-27201985f03e | -3.68342 | -60.55176 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e5c5ab88-ca20-3b18-ba5b-008a90ac38d8 | -3.68423 | -60.55487 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 09bcf9d4-6cdf-318f-9d39-a6f087e74e12 | -6.42216 | -43.48102 | 2026-09-24 04:44:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 31239a60-5425-3b11-a9cc-7a41dc3f45a6 | -3.44784 | -60.57394 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f436fe97-6632-3a6e-82bf-0a292032ffac | -3.83268 | -49.00106 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b8134e0-8f43-3716-98f0-04fd3d04db03 | -3.76096 | -47.50188 | 2026-09-24 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6dbc60fe-2a10-34cb-9e2e-eb0d00dab8e5 | -2.89891 | -54.09952 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 53fbda0a-da96-363c-8158-e71306da4ab0 | -1.78713 | -47.83396 | 2026-09-24 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8f2f8629-c8c9-3400-af7a-15e91ae934a3 | -1.78855 | -47.8339 | 2026-09-24 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e4e979c8-ab41-3dee-b449-ad7a236c5244 | -4.99674 | -45.55135 | 2026-09-24 04:44:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 367c3ffd-aed8-3f75-b64b-9a4d53bace1d | -5.84041 | -53.85275 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9df9f974-94f3-3758-9ac1-d3bc1672b710 | -3.70446 | -54.2076 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b832b380-cf97-3527-8a1f-b1bf3b4578c6 | -3.67647 | -60.59084 | 2026-09-24 04:44:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9786035e-8595-3cc1-9307-771f8617617a | -5.82087 | -47.75745 | 2026-09-24 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5856b4d0-9011-39f5-b836-c8fdbf86c95d | -7.8118 | -38.86269 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 010e941e-4f63-388b-bdfd-9bcb2e006375 | -3.91485 | -59.66771 | 2026-09-24 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| dc2c6942-12d2-3fb9-983b-04293d2fa41f | -3.06333 | -49.57112 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 15351a08-0c6c-3a7a-abde-f89aaa92d6e0 | -1.33433 | -47.78467 | 2026-09-24 04:44:00 | NPP-375D | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 306bc08a-98a2-3919-82ee-f3e96a666894 | -2.89505 | -54.09392 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8fabf228-c41e-33be-be5b-39aeecf9d55a | -2.16795 | -48.32029 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a2cd63af-ef40-336c-a42f-83491e660947 | -3.04648 | -46.92847 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc98caa7-b980-37be-bdf8-ef81d9f48168 | -1.27857 | -57.03077 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9d4b65cd-48ad-3a46-8809-4d7ea0de585b | -3.21804 | -53.40981 | 2026-09-24 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 37d3f20d-bedd-3f2d-96ee-937d0a1497a1 | -4.28325 | -48.61167 | 2026-09-24 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b9e6567f-16dd-3e46-b43f-837d976f8e65 | -5.23384 | -49.29968 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0c7cf28a-cd06-3d39-b912-0e1d7b4b4245 | -6.53406 | -51.50796 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8ed3d40-b07d-31b9-8fed-1fee32aaedbe | -5.93168 | -46.36076 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 27dba06b-29da-3425-8842-3a58ecdc2cb2 | -5.77714 | -46.57164 | 2026-09-24 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42d7ce49-e270-3c5b-9aea-3d13aaab66f7 | -6.53035 | -51.50734 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8740f279-d5f2-3b9d-b134-c17849ec3a08 | -3.9125 | -59.66719 | 2026-09-24 04:44:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 76af8f0d-be70-317a-8a2f-2a1cf206a359 | -6.31891 | -43.04516 | 2026-09-24 04:44:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| caeba3b4-0914-3771-9f49-7f2d56fc6e28 | -7.44595 | -44.68371 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 85165cf0-b5ab-36d1-9f8c-3646ae8ed9cf | -2.92588 | -48.73623 | 2026-09-24 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da8abe76-581e-39ff-b50b-83cd92986471 | -3.71837 | -54.20961 | 2026-09-24 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e8f41891-dced-3551-836f-8a091c06875f | -3.21065 | -53.39968 | 2026-09-24 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bb0aa8f-53a4-3f36-b8fc-443875a54b7d | -6.33996 | -49.86573 | 2026-09-24 04:44:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 727f17ef-6477-35c7-8620-5c9c256cd222 | 1.51108 | -56.01515 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fba9d97a-7fcf-3678-9e92-09b087b371d8 | -6.129 | -45.02499 | 2026-09-24 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9430bfcd-693d-378e-b2e4-77ad5d0d7df7 | -5.49822 | -49.02774 | 2026-09-24 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 664ccac5-2053-395a-a957-6631bcf42226 | -4.30147 | -49.12714 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 58e1ce46-bd4a-342a-b885-17d7a48d1fd2 | -3.2301 | -54.32385 | 2026-09-24 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 250c5b6d-2600-3414-97f8-d6e3f0d378f0 | -2.71527 | -57.51545 | 2026-09-24 04:44:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| b8a47a4a-c290-3bc4-82af-9b611de3175e | -5.81644 | -47.76387 | 2026-09-24 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de3b4c97-14f7-39d4-abef-c121ecd272e1 | -7.67514 | -45.48721 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 504757e3-d3b1-3465-ab5d-ad19a4879ca3 | -7.67282 | -45.47852 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ed75b949-96c3-3092-b356-52f33956a22c | -3.80911 | -58.89301 | 2026-09-24 04:44:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ebfd6d8e-cf16-3d0a-b561-0d6472714538 | -4.11281 | -51.07604 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 49bf7f16-56a7-3d4d-bf21-064a81d46fa4 | -3.0627 | -49.57502 | 2026-09-24 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3bd8f393-20bb-371d-a140-fbd0184b9def | -5.83899 | -53.86115 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a554446e-59fb-3ec8-b46e-b319461db14f | -7.49989 | -39.27289 | 2026-09-24 04:44:00 | NPP-375D | JARDIM | CEARÁ | Brasil | 2307106 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 5149b9e0-185b-3c02-b0b4-4af71346ddf7 | -6.20363 | -47.49744 | 2026-09-24 04:44:00 | NPP-375D | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e40344f3-8f21-3f36-9570-05bedada73d8 | -3.52442 | -49.3736 | 2026-09-24 04:44:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 909b5a59-872b-3d69-8476-e8e825df22ce | -7.67266 | -45.48318 | 2026-09-24 04:44:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2b7d34f3-3a8e-3526-97c0-de76fe641f02 | -4.20034 | -47.88406 | 2026-09-24 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e3b98706-c67a-3314-90ff-138bd81cae83 | -2.29557 | -47.88834 | 2026-09-24 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec17cd62-bc88-38ab-9adf-f4246b7ea4af | -6.17093 | -44.17864 | 2026-09-24 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4d5bad92-b60d-391b-91e4-e3e8bb213595 | -3.55493 | -43.46326 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5c9c0b04-ae15-3735-8b0e-ce80275e709b | -4.95175 | -45.14471 | 2026-09-24 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8a6154a9-69eb-3083-8287-258fb80e2d76 | -4.99264 | -45.13526 | 2026-09-24 04:44:00 | NPP-375D | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7a3e75dd-cd53-318d-8530-e72bf5c05873 | -2.88655 | -54.08759 | 2026-09-24 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1be2ac6f-cd7e-34de-909a-ce0dc2673c6d | -7.3987 | -44.7729 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b2afd68-448d-3d75-a305-723346b48415 | -2.8838 | -49.47662 | 2026-09-24 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 29a064e5-1507-300c-8b49-d3d582e0ae63 | -7.19497 | -47.45355 | 2026-09-24 04:44:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bce03855-ee9c-316c-8b28-e2df55422f1e | -6.63785 | -47.70507 | 2026-09-24 04:44:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3031a32-ee12-380f-bcf2-0e18a0fef42f | 1.50599 | -56.01984 | 2026-09-24 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94619ac7-abfc-3a14-9368-c810171d6a1f | -4.446 | -55.03244 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1ae9163-af47-31b0-b2ce-6f97861a2c31 | -7.76022 | -44.818 | 2026-09-24 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 90319c44-02bb-3635-925a-da0028087da0 | -3.82128 | -54.55599 | 2026-09-24 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1ee8cff9-0bab-3dde-b928-9b0c74cfe062 | -5.84906 | -46.10688 | 2026-09-24 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2bd4e8cb-28d6-315b-9617-5cfe7a6d80e6 | -3.7207 | -49.04745 | 2026-09-24 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a06289c5-5013-3467-b425-a3e821c23a4f | -6.65182 | -43.62343 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4ab24fba-1744-3ed0-baa3-663b4847af45 | -2.38657 | -48.52519 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c20f122-4356-3fd1-b1de-6ae5dce78970 | -2.17076 | -48.32442 | 2026-09-24 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fb96f276-ede6-3137-9dd5-1e8d50d699fa | -2.97879 | -54.15067 | 2026-09-24 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3ac35d2c-a039-3e88-83a9-61d3e89d29d6 | -3.00357 | -54.17467 | 2026-09-24 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d76ac97-1954-3649-90ad-f3e03a85bf05 | -3.18159 | -48.01336 | 2026-09-24 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a97884c5-3e6a-349f-a2ef-5ec83dac0caa | -4.47116 | -54.9715 | 2026-09-24 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fbcaee99-e3d7-3579-ad99-0fa2f013d3f7 | -0.93448 | -47.55227 | 2026-09-24 04:44:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 816143f7-bd84-3723-84ec-f57f8cb2de75 | -6.5213 | -52.82135 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b15e39ca-fc8f-3c6a-973a-d9917654f45d | -7.42585 | -42.63724 | 2026-09-24 04:44:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 81692d23-0442-3157-b3fa-9c7ca2028569 | -3.58834 | -50.03227 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79f5a7f5-1c6a-36c8-8354-ebc9b3f3502a | -5.83535 | -53.85619 | 2026-09-24 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5d554ba-5e00-3b29-a417-44c563a67465 | -5.25542 | -49.23167 | 2026-09-24 04:44:00 | NPP-375D | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bf3414a-8997-31e9-955a-976edd4eee8b | -3.55123 | -43.46489 | 2026-09-24 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 2fe14a20-44d4-33d0-9d08-b13b62b03100 | -1.61978 | -54.91726 | 2026-09-24 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3b99cc20-4802-3bcb-bcd5-346fbb249380 | -5.81422 | -47.7564 | 2026-09-24 04:44:00 | NPP-375D | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c7224f08-6b20-3ada-8b6d-730db0543cdb | -2.59755 | -47.35024 | 2026-09-24 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c836972e-9aac-3e43-81c2-a516add8ce4a | -6.42964 | -48.46409 | 2026-09-24 04:44:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3ceb6b98-7eb1-3359-a2e6-18ab72346ed8 | -4.10834 | -51.07983 | 2026-09-24 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d3cff2a-472f-3f89-b3f2-314ecc9b8d1c | -6.31396 | -52.67193 | 2026-09-24 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5442923b-6c1c-3ab5-ad10-07cbbe2f8f45 | -7.62962 | -46.79132 | 2026-09-24 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README47.md)
