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

## Dados Diários - Página 196

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2fcddea2-1ac8-3809-8b98-b2d6ccd98876 | -6.406 | -54.7637 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 305c6cf3-c30b-3ddb-80b4-c5a0028e1028 | -7.5526 | -60.4651 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 809da88f-5a0d-3dd2-8d98-71647092f6f8 | -11.0933 | -51.5345 | 2026-08-31 19:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 128.7 |
| 1a900362-d494-368c-be70-4eb96f939e82 | -3.4185 | -61.3461 | 2026-08-31 19:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ea82898e-a10b-3916-ad78-f8b6cd82f32d | -3.1267 | -61.1811 | 2026-08-31 19:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 162.9 |
| eb252b7e-9d84-3e0e-96da-98714aefd585 | -8.6674 | -62.8179 | 2026-08-31 19:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 67.0 |
| 903963a8-3649-391c-bf0d-8b7fba3e54ce | -4.1516 | -60.6878 | 2026-08-31 19:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 85db2e78-f553-3723-b8a6-f9e7c620b4fe | -16.0352 | -54.3933 | 2026-08-31 19:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 115.8 |
| fd28fed2-b095-3922-a168-ccdc5de4e309 | -6.8019 | -59.4008 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 169.3 |
| 96e334fa-5ea2-364b-afb3-a9685bfd7e19 | -6.8593 | -59.0318 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 71fa861b-4b68-3d5e-a84e-9709027bd3c2 | -6.1294 | -57.6833 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 4f06e644-789e-3594-a7e5-878ed2a56e13 | -13.4519 | -57.039 | 2026-08-31 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 11331bb0-9dd6-3c50-8b7f-bc0bcc5d3bcf | -10.8444 | -45.3126 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.5 |
| c9906017-61dc-38e0-bfb7-5c1de8451171 | -2.7303 | -47.0644 | 2026-08-31 19:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 9e6bdbe0-46ef-3d8c-9a01-2cb5f8ddeff8 | -5.5831 | -60.2307 | 2026-08-31 19:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| d63f9419-4693-39e9-a632-0db898df59e1 | -8.8816 | -46.0253 | 2026-08-31 19:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 271189b2-1aa4-3d18-a81e-db4f45fba88a | -6.6233 | -58.383 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.9 |
| b22f8e96-0b22-31b9-b4aa-6cbae9779f8e | -14.4641 | -52.1964 | 2026-08-31 19:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 3079bf2b-ea06-3b35-acc2-4e8278d26e7b | -6.7832 | -59.4401 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 7737c5df-a34d-3704-b607-6ef4f56cc046 | -9.9898 | -53.9199 | 2026-08-31 19:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 824a5ddc-c68c-3106-a977-424cd8f909aa | -10.1324 | -45.8598 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 76e88c7b-cb55-3872-8406-b7a2e82b2e88 | -9.862 | -64.9771 | 2026-08-31 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.0 |
| 582cd522-9aa5-31bd-96d8-0908fdf0fc83 | -11.0936 | -51.5134 | 2026-08-31 19:20:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 199.9 |
| 9483780e-5bc3-3d48-9844-a689786d0582 | -13.5341 | -59.7589 | 2026-08-31 19:20:00 | GOES-19 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 14edc9db-7edb-34fd-b966-712a9fc7b8a8 | -6.5669 | -58.56 | 2026-08-31 19:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 116.1 |
| 3a8583e2-5414-3410-842c-5c3ce6091a45 | -8.5555 | -66.9574 | 2026-08-31 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.5 |
| dd39b408-ae3c-3523-9f8f-6b4c09ebe193 | -3.4185 | -61.3273 | 2026-08-31 19:20:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 9c2eb995-70ea-3be6-980b-5b7b1cce7668 | -14.1263 | -52.8106 | 2026-08-31 19:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 720b80cd-d111-36d3-abea-e0139339af48 | -9.173 | -59.3659 | 2026-08-31 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 22135172-6129-3d81-bafc-2cfae8e62c27 | -8.6012 | -70.2192 | 2026-08-31 19:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 64.7 |
| b1bca75f-08e9-367f-ad92-2b3b433a94a5 | -11.2317 | -46.1041 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 86af332e-c032-3b82-88ae-1cf96156851d | -8.8705 | -66.7822 | 2026-08-31 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 385.0 |
| f6b1aa58-f147-357d-8613-e97a835f0582 | -15.0053 | -48.1496 | 2026-08-31 19:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 72176f21-d2b2-3c9a-9617-48da4cdeedb5 | -16.0348 | -54.4143 | 2026-08-31 19:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 841601c6-3d41-36ef-abfe-fb14490243a3 | -19.094 | -57.4057 | 2026-08-31 19:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 104.6 |
| 94e1c890-7048-34da-b12e-b6f6d5836d9e | -7.9355 | -61.3473 | 2026-08-31 19:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 5f6dfce5-70dc-37fe-84fc-564fbd0bf97c | -9.6679 | -46.5455 | 2026-08-31 19:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 168.4 |
| 583016c5-0b5a-3a0f-8c03-62b73e3538de | -3.1449 | -61.1808 | 2026-08-31 19:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 1c585ec2-66da-3521-bbd8-a9e2def9870f | -6.8201 | -59.4386 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| b519496e-4d01-328d-bcc3-3ce4890b8809 | -7.6804 | -55.3555 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 60.7 |
| 97dab79c-114b-3a1c-aa93-22a40158c173 | -3.1083 | -61.2191 | 2026-08-31 19:20:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 4ff41adb-0740-390e-b60c-24474ad22c9b | -3.1839 | -60.1559 | 2026-08-31 19:20:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b11b2388-0010-3991-93eb-bf01bc6f21e9 | -5.9816 | -51.9155 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| 42c44787-283c-3e49-baff-96369c9eb649 | -10.0677 | -59.412 | 2026-08-31 19:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 5ec0b1cb-fa3e-39c0-b15f-277a60e27332 | -6.1556 | -53.5047 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 301effb8-1139-34df-967b-8c2198da41ed | -7.1822 | -60.6713 | 2026-08-31 19:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 897c6af4-a8d8-3a97-b966-4d6c4822b36f | -11.6786 | -54.5484 | 2026-08-31 19:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 2b191a86-5140-3965-a8a4-231e67f38c4b | -15.7349 | -56.1093 | 2026-08-31 19:20:00 | GOES-19 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Pantanal | 121.4 |
| 8406727d-37b0-33d9-a1ee-a9f1b4a9e786 | -9.908 | -67.0131 | 2026-08-31 19:20:00 | GOES-19 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 70.1 |
| 12a83316-706f-3acc-821b-93a285848a7d | -6.9368 | -55.6161 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| d7190602-ba43-391e-8557-2b7aa643bfae | -8.5924 | -66.975 | 2026-08-31 19:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 116.0 |
| 50d27c1b-d210-3ce6-b712-d53eface4f3b | -9.1895 | -59.6364 | 2026-08-31 19:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 797bcbea-9e67-3868-8910-0d2c1bef50fb | -6.7463 | -59.4416 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 846557f2-4e31-36fc-99ef-738ba00ac866 | -8.4528 | -70.5881 | 2026-08-31 19:20:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 580c744c-6e7e-31fa-879f-9d25341c90ae | -2.7304 | -47.0424 | 2026-08-31 19:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| 1cb3cd61-6280-340d-b1a8-4fd90ae5cd98 | -6.8009 | -59.5742 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 90903993-08e4-388c-a495-48dd2da295df | -5.9635 | -57.6899 | 2026-08-31 19:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| ec3e978a-9045-3bc7-bf0a-4345d2137d90 | -9.8434 | -64.9777 | 2026-08-31 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 1d60b41b-440d-3fa4-9aa7-168d5b4df85c | -5.8866 | -52.2507 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 6102772d-6279-304c-a615-2e7a27a2110f | -3.6076 | -59.0769 | 2026-08-31 19:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 71892e94-2562-3ce5-a5f1-af6010e77f17 | -14.5948 | -53.6134 | 2026-08-31 19:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.5 |
| 1384bc35-8cd5-3795-8391-100cbf9a09d3 | -9.2144 | -47.99 | 2026-08-31 19:20:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 69004bd7-b073-3b8e-a821-df7eed2f7681 | -6.3875 | -54.7646 | 2026-08-31 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| 8544eb1e-4a40-3b72-ab9a-8d3c44997353 | -10.8448 | -45.2897 | 2026-08-31 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 9e56bea5-72ab-357c-ae42-6677ba25c759 | -2.7119 | -47.043 | 2026-08-31 19:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| de0d7712-e210-3ef9-9fe7-15fe79a04167 | -5.8879 | -52.0652 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.2 |
| f41b4b28-b586-38f5-a355-8bd7763c46a1 | -7.3453 | -72.9539 | 2026-08-31 19:20:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 9777d689-4465-3fcd-a6fa-8e766923f992 | -5.9814 | -51.9362 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 71.4 |
| d151b043-d745-3011-8826-feee977e6f81 | -4.9788 | -55.8417 | 2026-08-31 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 95.5 |
| 30f0ac8d-9228-3523-9781-9652834185f5 | -10.1538 | -45.6982 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 127.9 |
| cbe06ffe-853c-3be8-8b21-473521f2ca0e | -10.9672 | -48.4111 | 2026-08-31 19:20:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 238.9 |
| d3792ffa-3fc3-366f-b35b-36d3dd5e876e | -3.6215 | -60.566 | 2026-08-31 19:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 233.1 |
| 70d12f17-50fa-3c02-aee8-d296bc71d4a0 | -7.6149 | -44.8833 | 2026-08-31 19:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 84.8 |
| 3a1b18be-79b9-39a0-bcd1-8af990134f21 | -11.1809 | -55.0821 | 2026-08-31 19:20:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| ac09e14b-673d-3f05-9c17-d270d9bf4746 | -12.0925 | -44.996 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 185.0 |
| ac23b4ad-3517-35ea-aa64-92de8c8df0af | -12.0912 | -45.0656 | 2026-08-31 19:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 107.0 |
| aed07100-c919-329e-b9dd-c19ef52d52fe | -14.5028 | -52.1913 | 2026-08-31 19:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 79291004-5a9f-395f-a91c-2fff60f2d9c1 | -9.9673 | -46.7797 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 96926f1d-e904-37b5-b090-7eb51bf77246 | -10.7407 | -54.0401 | 2026-08-31 19:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 163.0 |
| 87ae6173-6f80-3246-8fce-eb82069e500b | -11.6978 | -54.5262 | 2026-08-31 19:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a66dd8a0-72aa-36fe-a6a1-bbc1cc7626fa | -15.2278 | -56.3512 | 2026-08-31 19:20:00 | GOES-19 | ACORIZAL | MATO GROSSO | Brasil | 5100102 | 51 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 365e1f07-6351-3dfd-85b5-42860f1cc059 | -6.7813 | -59.7864 | 2026-08-31 19:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.4 |
| f83fa096-df1a-3865-9158-225393701579 | -6.1431 | -52.6481 | 2026-08-31 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 70fd3851-24ff-33af-aef7-c4e7e4d22016 | -8.2605 | -62.758 | 2026-08-31 19:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 79.8 |
| c6127072-2428-3228-b8d4-a69b4619b0b2 | -7.4802 | -63.7454 | 2026-08-31 19:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.9 |
| a74785f8-9886-3a29-b15e-24a8a41988dd | -11.5475 | -45.4906 | 2026-08-31 19:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 154.2 |
| dfcb8341-6018-3a81-a082-e3c9a9aa2530 | -3.6216 | -60.547 | 2026-08-31 19:20:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 132.7 |
| 96c7f71a-ddfa-3e1a-9081-cc7205f93cbc | -9.9896 | -53.9404 | 2026-08-31 19:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 105.2 |
| 4fda60d7-c751-3f23-8d3d-1e9d511d711c | -3.6259 | -59.0765 | 2026-08-31 19:20:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| c90f4520-9f06-34ca-9c4c-0b427a040a46 | -13.4707 | -57.0574 | 2026-08-31 19:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Cerrado | 80.8 |
| f7e0d8dd-de70-3745-8335-1b8e7a604dbc | -17.3027 | -42.6926 | 2026-08-31 19:20:00 | GOES-19 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 88.3 |
| 9f0a336e-1a69-3d3f-b579-e86266d72050 | -7.6253 | -55.2787 | 2026-08-31 19:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 6be83275-ef97-3e3e-88ed-44d9541702f6 | -15.4601 | -52.806 | 2026-08-31 19:30:00 | GOES-19 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 32bdf396-ae74-33aa-8d2a-1cd7bb53e4b0 | -12.9032 | -45.8382 | 2026-08-31 19:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 114.3 |
| ea410a7c-5b68-319a-90fd-4b6142bfa03a | -12.0925 | -44.996 | 2026-08-31 19:30:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 280.9 |
| 6e56a718-0552-3c70-a878-3d33e0617628 | -12.9589 | -45.944 | 2026-08-31 19:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 18d8ecaf-513f-3ae8-b047-10ed3870e0e8 | -10.1273 | -50.2971 | 2026-08-31 19:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.5 |
| 9ba9b261-6a78-38d5-a668-e639fa95b033 | -8.499 | -55.3051 | 2026-08-31 19:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 96.5 |
| a457b7d7-ab34-3722-a275-86c697e9dd69 | -11.4968 | -45.1071 | 2026-08-31 19:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 75ace9e7-76b4-3800-90ea-8571adc3468e | -9.4908 | -57.0144 | 2026-08-31 19:30:00 | GOES-19 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |


[Clique aqui para ver as próximas entradas](README197.md)
