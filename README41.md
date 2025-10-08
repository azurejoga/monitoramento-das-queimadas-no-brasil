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

## Dados Diários - Página 41

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 05d73935-de40-3b06-bf79-220df35e555c | -13.06214 | -47.88414 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91bc0372-3110-34bd-8fbb-a7cdb1e732f2 | -11.16593 | -54.89046 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e418251a-84c0-3570-9487-58e9455c4027 | -2.888 | -50.72683 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 71e991f8-72f0-3bcd-a7c2-785168e9781d | -4.1331 | -47.64976 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddf2d1ce-7599-38fb-a3be-b671e73b2652 | -11.29146 | -54.88913 | 2025-10-08 04:17:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 87ce74b4-ca56-3a56-9dad-0bb030e9d106 | -11.05873 | -47.92733 | 2025-10-08 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| efa37ff7-fcd9-3b1c-9ac7-00d243a1194b | -13.25274 | -46.47187 | 2025-10-08 04:17:00 | NPP-375D | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 80d3da62-9508-3dca-a0b0-38ebd92fdd03 | -11.99585 | -46.77192 | 2025-10-08 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 65c0a1a2-9bd0-31df-9ce8-0ab0bce8d24b | -5.71669 | -44.82333 | 2025-10-08 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 920b7ed3-8d9d-3023-a18b-fa792aa87272 | -4.05272 | -42.5138 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d7276af9-fe34-34b9-95e3-a533682586a7 | -11.72121 | -50.94445 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| aad97021-2837-3fba-a80f-5f8a363c19c3 | -5.91489 | -44.19638 | 2025-10-08 04:17:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6ec99f0e-04f9-3d14-9d56-4007e11da0ff | -13.93924 | -43.74009 | 2025-10-08 04:17:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0c8cdca1-034f-3970-aa17-7ffde473eb80 | -11.24498 | -47.38285 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cbe77de-4913-3e8a-a413-4d8ab137ad70 | -11.16507 | -54.88795 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 40a22bbf-2912-3ec6-8c9e-0c152af77462 | -7.4453 | -43.13712 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 80b6fd24-ac27-339e-928b-205b1569ed3b | -7.43978 | -43.15052 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| b1daad54-57ed-3e33-a7b6-62bf3d2fc73c | -6.12941 | -44.60275 | 2025-10-08 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55a03b18-c879-3534-a857-895032a3a024 | -9.6373 | -55.13116 | 2025-10-08 04:17:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6a10081-8784-3bfb-98ea-7d11f40ab688 | -5.83146 | -39.08718 | 2025-10-08 04:17:00 | NPP-375D | SOLONÓPOLE | CEARÁ | Brasil | 2313005 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5416296d-f4c3-3e9d-8b16-a2f6c688c47c | -12.2463 | -47.86582 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| b54fe6da-9f09-37df-ad3d-a17d05e19c20 | -3.43985 | -45.59554 | 2025-10-08 04:17:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53ca0698-17b5-3270-945c-d050f7011d7a | -5.83778 | -41.5002 | 2025-10-08 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 168d4bab-9475-3615-a08f-007d302f9097 | -3.89533 | -42.54877 | 2025-10-08 04:17:00 | NPP-375D | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c65b1c18-80dd-3637-a89b-93168687d712 | -6.7571 | -43.76327 | 2025-10-08 04:17:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 19f7b419-52de-3d4c-95c2-c50ba51d6e75 | -5.70337 | -44.21389 | 2025-10-08 04:17:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9492a785-0914-3e18-be44-ad8270e669bc | -5.70601 | -45.68217 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 50fc71a3-857d-3334-80fe-a142c20e2054 | -5.1436 | -44.96135 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 395fffce-3ec9-3ae2-9c25-0bfc4e3e35e0 | -11.2235 | -40.46752 | 2025-10-08 04:17:00 | NPP-375D | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fdd4410d-0eaa-3a7a-af33-3008980e0037 | -11.17256 | -54.88068 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c7c7a5fa-0743-3b37-90ce-a6477ba47450 | -13.02549 | -47.90204 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 51ba9969-ee17-314c-91b4-697b4d5a4515 | -10.41745 | -50.22598 | 2025-10-08 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc4e6471-7dcd-301a-b162-2207125c064c | -12.12162 | -45.1317 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4aba7049-46a7-39a0-bd90-c3e61f968b1d | -3.50124 | -51.11153 | 2025-10-08 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1503697-d1fa-36d1-a9c3-1519f74b2238 | -12.94122 | -46.85939 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| bcf05385-d7e7-3b1d-9c77-f99d7d31744d | -11.17007 | -54.90036 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c1d6bb65-f2b3-399c-9131-25290420252f | -11.69786 | -50.9599 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9623a636-0640-3d3d-a058-1c0e3e39513d | -11.86227 | -44.92873 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7cb1f844-743b-3a43-9a87-2b6061a7a1b1 | -11.87446 | -44.93802 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f64bc1c6-70d2-32ad-966a-c433527e2f3f | 0.92557 | -51.12872 | 2025-10-08 04:17:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 484c36a4-4ba1-3cbe-945f-9c3040ba1371 | -3.98237 | -40.3981 | 2025-10-08 04:17:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0c07cd13-2c4b-3329-9d6c-8733af944600 | -12.94377 | -46.84391 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1330a47b-9b13-3f3f-b3b2-85ee22b0805e | -4.6838 | -49.49372 | 2025-10-08 04:17:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d13a47a2-99db-3d45-bb8a-fac6e9cd845c | -7.44698 | -43.14809 | 2025-10-08 04:17:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 52d51a31-00bc-37d2-8bb6-d1443cd60507 | -11.79683 | -45.11156 | 2025-10-08 04:17:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38f794a2-b550-3a36-b8b8-6ac28d70acf0 | -13.04572 | -47.89287 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5043ba25-5d4f-365c-9c70-0167308a7f19 | -12.24774 | -47.86311 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5027e785-f260-35cf-8228-53d9535b85e4 | -11.11274 | -54.04107 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b5c3966f-217e-38e3-a6ff-50734a6dfffb | -5.14185 | -44.96017 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7fa96eea-f085-3305-813c-9802c8b8f23a | -11.68959 | -50.96611 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0961c9fc-a275-3dbd-8cc4-045d55736b0a | -12.92144 | -46.82806 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52ac3575-18b9-35cc-93f2-bcc4b4e71fe6 | -11.16509 | -54.89484 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fb112181-f9fc-3eed-81a9-3c171c52edf9 | -4.50107 | -46.35896 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f787ff67-b2a0-3329-bbd1-12783e518f35 | -11.46403 | -43.48645 | 2025-10-08 04:17:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5eee18e1-7f18-3bc7-9ce3-173305e45be6 | -13.08453 | -47.99185 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31c112a7-fcb7-318e-821f-a4833cd30f4c | -10.24304 | -52.70065 | 2025-10-08 04:17:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 252119a9-f29d-321b-aa23-cf20de1e8305 | -3.09091 | -50.57743 | 2025-10-08 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b88a8ed4-c3d5-31c2-bc70-6ed580719111 | -5.36364 | -41.00101 | 2025-10-08 04:17:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ff2065f9-578c-3cdd-bc93-0adfd8c2f7b5 | -4.69173 | -46.46812 | 2025-10-08 04:17:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e45b300a-cdd8-3e2c-aeb0-2b18e145e8e7 | -11.1453 | -47.755 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 13d1ce41-1509-3baf-b0db-a6b0d8d5c84e | -12.38751 | -51.12804 | 2025-10-08 04:17:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ad8c5f70-600d-34c1-ad52-e1bd466b1839 | -11.1427 | -54.88577 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e34a6b73-f015-32b5-b180-110b44d907d8 | -10.941 | -49.48119 | 2025-10-08 04:17:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 95bb4aa5-9d3d-3dde-8dd4-dfe49f084569 | -11.45772 | -50.20736 | 2025-10-08 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e598b4b9-8c42-3dab-bcea-a0af823a4396 | -9.5464 | -47.76602 | 2025-10-08 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a94dfab9-3fe6-32b8-806f-b7cc415343dd | -13.06889 | -47.93224 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6c41d3dd-00f3-36cc-843c-f7724812d3ab | -13.26581 | -47.78672 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a483ee4f-7712-38dd-84d0-e55a4ac4d89c | -11.18494 | -54.87911 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b68b002e-c580-35cd-8f62-69767294d9f4 | -11.1535 | -54.89232 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d5ce99a-de94-3a8c-85b5-575b33370451 | -12.74226 | -44.72016 | 2025-10-08 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ee05cbb-a779-321e-a30f-f804bd81df26 | -3.09792 | -47.02215 | 2025-10-08 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50459113-773f-3311-8e9c-908ddd1c19ab | -10.3735 | -48.13074 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9c40be0-40f7-3da1-bf54-0d21a869b362 | -4.01773 | -48.96288 | 2025-10-08 04:17:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd6a79b2-11b0-3d34-8d7a-ced43d5780e9 | -13.05953 | -47.94338 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 831b6284-a699-388b-86eb-2ced08f90381 | -10.18211 | -45.55053 | 2025-10-08 04:17:00 | NPP-375D | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 68ee268d-05b3-32f2-8d59-bb6f421d9448 | -6.74366 | -34.96259 | 2025-10-08 04:17:00 | NPP-375D | MARCAÇÃO | PARAÍBA | Brasil | 2509057 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ae978d9e-7333-30e3-ac83-7e28eff52b38 | -10.61708 | -48.64368 | 2025-10-08 04:17:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c9432430-f401-32b2-9536-a91989231c98 | -13.02914 | -47.90253 | 2025-10-08 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| abe61496-833d-3e47-b992-5d89bf309d41 | -5.4069 | -46.23076 | 2025-10-08 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c937082-e264-342b-b4a0-f0cbb5a6270a | -4.2091 | -44.66967 | 2025-10-08 04:17:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c5123c81-4bdb-3abc-b7c7-ba2d179e65ce | -11.94348 | -46.41805 | 2025-10-08 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7f136d2-3bc9-3715-9a9e-dae680d679bf | -4.08153 | -48.04526 | 2025-10-08 04:17:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 66d2cf0c-b0ca-3015-b902-1d4de3bf9b93 | -13.28968 | -48.04104 | 2025-10-08 04:17:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6dfca1ab-60c4-36c7-b9d7-afef5700d71b | -4.04994 | -42.50982 | 2025-10-08 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6117c1b4-bd7d-3e66-b484-c92a06897837 | -10.22052 | -48.17179 | 2025-10-08 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 387f9ad7-e38a-3495-8591-77b4e790cf85 | -10.74814 | -47.88635 | 2025-10-08 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4dc199bf-c487-38f0-83d5-31c25dff46d1 | -11.17 | -54.89348 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 35c17734-5c40-3622-8b23-b6c63ecb9c60 | -11.11143 | -54.04133 | 2025-10-08 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 60c10ccf-eec9-33cd-9306-b3375723c742 | -7.0095 | -42.87195 | 2025-10-08 04:17:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 610b0468-b2e9-39e6-85b8-d1edd9c7bc1c | -10.40055 | -45.36899 | 2025-10-08 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 79a44d9b-dbcb-346b-8e39-c12e4eee00cb | -11.17173 | -54.89169 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| dbfcc3d8-1217-38d9-9f78-a1fd77380ac7 | -11.22051 | -47.77031 | 2025-10-08 04:17:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 97171009-6ff1-35b3-91d0-10abaadbebe7 | -11.73291 | -50.95586 | 2025-10-08 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d4c3ab06-d363-3e7f-b13b-a173fba4e8eb | -12.93775 | -46.85878 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d52e6241-85c5-39e6-af6c-f8d738b2bfff | -12.91861 | -46.82359 | 2025-10-08 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 90d65365-fc59-34bd-879a-80b070d42666 | -5.17434 | -45.13301 | 2025-10-08 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 56aeb0cd-df61-3dad-ba06-e1a31fc772f8 | -11.16839 | -54.87131 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 830a7595-e36c-35a4-8ac2-28559e251aeb | -2.78913 | -49.59409 | 2025-10-08 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a760109f-5db3-364e-89eb-74e8a0e967b2 | -11.16425 | -54.8992 | 2025-10-08 04:17:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e4bf3c1-6be9-3f53-a2bb-1ff04875890d | -3.11335 | -48.78415 | 2025-10-08 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README42.md)
