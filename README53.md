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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb03e8b5-81ab-33ae-980a-60d325336472 | -8.23105 | -45.43928 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d0d1695-e70a-38d8-af6f-f2ae21a6141e | -2.94533 | -57.80208 | 2026-09-28 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 143e9ed2-c0b9-3977-b911-2e302c2fd4b8 | -5.72671 | -53.46078 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 767dd0ed-d630-3cf6-b69c-fd40b13454ed | -5.73034 | -43.28209 | 2026-09-28 05:10:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b0ad9160-b528-3b23-a152-6da594b8891e | -7.82032 | -55.14367 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 020ed09d-eef4-3917-951c-085c9cfcf828 | -10.20012 | -49.99743 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cd2b1b9f-5739-3bc8-b75d-5a56c69f13bd | -7.28367 | -55.57363 | 2026-09-28 05:10:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2234fb5f-e23a-31d5-83fb-9741fa401d85 | -6.07573 | -57.81155 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3129fd5d-8ea4-3e01-913b-1d2aebd4a6a6 | -6.30825 | -56.03212 | 2026-09-28 05:10:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 99f8baa7-af4f-34c9-a80a-632e6ae55e1e | -8.03253 | -54.89426 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cb7216ee-b286-3d05-be97-646140d54d95 | -8.25399 | -45.4073 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 562a01a8-13e3-3252-aae1-d4c0ad88b952 | -7.67734 | -44.79262 | 2026-09-28 05:10:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 69f232b2-eb8c-3b66-89d8-3b5abf7b4ece | -8.65623 | -45.41696 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd90cf1c-a4cd-33e0-ada9-ed036f3fd53c | -8.35619 | -45.44106 | 2026-09-28 05:10:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5822f7c-832c-3ccc-832d-d4af7981ab6c | -2.55678 | -58.0502 | 2026-09-28 05:10:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c60bb31b-42ac-3096-9b78-93da699f1673 | -6.14526 | -44.13836 | 2026-09-28 05:10:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 222b4fd6-f3b9-3d3c-8fe2-3a6f9a3d0e28 | -2.95956 | -54.09436 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| eaf7ea2c-7419-3150-b849-3f46e2553714 | -8.65576 | -45.42056 | 2026-09-28 05:10:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 178079a1-f860-33d0-a74f-6438fbd2c35f | -8.43764 | -44.87007 | 2026-09-28 05:10:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db56e7d2-90ae-3f54-ae7d-06d16b4642f0 | -10.21733 | -49.99266 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10f8867d-1877-3b05-84cb-526bd17a293f | -2.55956 | -54.73484 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| beebd963-9bcf-3c9a-8652-c6499dac4439 | -2.94565 | -54.09574 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e916c3d9-2240-3768-a044-865e5ab30913 | -10.80033 | -48.7347 | 2026-09-28 05:10:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2262f009-4b75-3525-a701-0dc28e3c147f | -10.22189 | -49.9897 | 2026-09-28 05:10:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| afda20e7-c5b0-3538-b382-b05e40316a38 | -3.14573 | -54.09846 | 2026-09-28 05:10:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bbf17c58-3879-3416-8b06-2540a1944dee | -7.37707 | -42.11225 | 2026-09-28 05:10:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| b476cb99-ad39-335a-88e3-ed5ff9968983 | -10.15908 | -46.57582 | 2026-09-28 05:10:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ddcb2fb2-6b61-3694-a773-ac4d2f1f52be | -3.02028 | -54.2078 | 2026-09-28 05:10:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cd60c3f7-ab18-3b05-8ecd-a320942db76b | -6.09818 | -57.62982 | 2026-09-28 05:10:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf100104-e57e-3811-8169-e0d255224fb1 | -3.93767 | -59.65215 | 2026-09-28 05:10:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ec115384-a4b5-345c-990a-406fd7a6c1bb | -7.49743 | -55.02378 | 2026-09-28 05:10:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d2c9451f-478e-3ea8-ac5d-d21931a7091a | -2.98623 | -51.05338 | 2026-09-28 05:10:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee0abe81-150f-316c-8947-30a1f741a129 | -9.77383 | -44.83257 | 2026-09-28 05:10:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 36f30d16-2095-34bc-a568-b0d3a4721fe4 | -3.51244 | -50.3189 | 2026-09-28 05:10:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c4cee36-18be-3708-96f9-7c53ac401891 | -3.07609 | -51.1988 | 2026-09-28 05:10:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5a8ec84-9089-31a7-9999-e4f1901b9599 | -11.18322 | -44.80844 | 2026-09-28 05:10:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 45.1 |
| 4ab928ff-d57d-3adc-ae71-c3ea5ebbeeb8 | -16.36146 | -52.41134 | 2026-09-28 05:12:00 | NPP-375D | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d3557c2c-5112-3abb-85f6-74b297d35e28 | -12.68758 | -46.98468 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 331331be-05ce-3f6d-ac8e-f55a36fff1c4 | -12.74298 | -47.29824 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 0b90fcba-0dad-3be1-a7e4-5376efd63b6f | -15.46397 | -46.14954 | 2026-09-28 05:12:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b985c58-9686-3ca4-ab30-0bdc5341fe9d | -12.6799 | -45.01756 | 2026-09-28 05:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4375df87-886e-3efd-b8fa-25e1138539d1 | -15.1725 | -46.14706 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3692814b-fa1e-3a8a-bea8-cfa93291c384 | -15.05301 | -47.23002 | 2026-09-28 05:12:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f362e122-6032-3542-8797-dc78f0333950 | -14.73953 | -45.57158 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c4a8f1ba-6a65-3668-b49c-7c21a73e1238 | -11.4925 | -47.38447 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2a1384c5-b001-393c-8dcd-3402e58efc09 | -9.08351 | -61.44918 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3379a459-250a-3061-afe4-cc2db53b7b13 | -10.82405 | -60.74552 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7490e456-04ce-36da-b40e-d7142ed9f722 | -8.83839 | -62.39215 | 2026-09-28 05:12:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 210ed939-347a-3915-a7fe-cdd382736074 | -12.625 | -47.31098 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8429fdd0-329b-344b-80ef-c9c74600243a | -11.59878 | -44.13208 | 2026-09-28 05:12:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f684e548-7f5e-3501-a1eb-e3692b8a5696 | -12.13875 | -50.34652 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| e5dd2bae-13be-3937-8e9c-a011ac84a4e6 | -16.35385 | -42.57169 | 2026-09-28 05:12:00 | NPP-375D | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b9d612da-b1cc-32c4-a1ce-62e225474e34 | -9.93284 | -60.72295 | 2026-09-28 05:12:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49822244-5a55-3fc5-ab06-0bee30e6bf72 | -12.80079 | -54.00917 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b9cc56a-a4bb-399c-8a13-c9b24ee58468 | -12.59085 | -51.96107 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a79cce0-2506-3e93-852e-b1c6b27ea4a6 | -10.95126 | -49.60253 | 2026-09-28 05:12:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 634aa630-68ea-3ce7-9573-850fbc9ecdcd | -11.07452 | -51.40218 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8079465d-2a4d-3782-aa0a-efa081f489e3 | -9.17003 | -61.40503 | 2026-09-28 05:12:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 31eabc94-32c8-32b5-b476-660dd953193a | -10.40344 | -53.81686 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9ebd8dfb-c824-34d6-a95a-1b5a2136047f | -12.68877 | -46.97541 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dc003f4-a22a-37a1-ad9f-bb16860ec867 | -15.16484 | -46.16451 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d0f3d32-e1b9-34fb-aad3-cc51c60919ba | -13.45752 | -48.58858 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| dcfeb634-9fbb-3cb4-9f92-ada2346684ca | -13.10817 | -47.41896 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d62d575e-f474-39e4-889c-79c45f787ba6 | -12.6574 | -47.32779 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e867a100-7b8d-30c1-90f6-1ec80f1e0601 | -13.46526 | -48.58663 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 76337832-5a57-33f4-8079-0297228b0623 | -10.41976 | -53.82317 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9d8f397-8ab3-355f-9ce9-ffff5c70f059 | -12.59828 | -51.96224 | 2026-09-28 05:12:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6f8b4f4-27c6-38e1-8bb6-cdf9df913444 | -12.63503 | -47.31247 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6e36b3f8-cfcc-37bf-a9c7-dedfc1ced847 | -14.71552 | -45.57593 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b926c35b-1d06-30a1-8f66-abe7d7ef6238 | -11.11024 | -51.34192 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| de478bc1-06b1-32c1-8ed0-79b2c3df8632 | -14.41004 | -52.80867 | 2026-09-28 05:12:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 81dfc6d4-979b-3a1f-b635-81ca1202bde8 | -12.16501 | -50.39428 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.2 |
| e2cd605c-a78d-3935-bef0-adf767b00a1c | -10.42314 | -53.8237 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5dcdda98-f593-3cad-a9c0-188febc3f531 | -12.14916 | -50.35877 | 2026-09-28 05:12:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc2b0dbf-6d0d-3136-b92a-7c1c73dfbeb2 | -11.62689 | -46.79205 | 2026-09-28 05:12:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4be484e-d43f-385d-8f39-fd9f61393370 | -13.44948 | -46.31343 | 2026-09-28 05:12:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3ffbf3d3-1b32-36d4-9af9-cd505ef79b75 | -11.37993 | -47.44239 | 2026-09-28 05:12:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 0eefa84b-7803-324b-84a9-185fb5206f0b | -10.42371 | -53.82006 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9e5820b-42d6-3595-bdd9-95d34311183f | -14.12186 | -46.29213 | 2026-09-28 05:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59f967a9-55fa-3ab3-ae0a-9f81040cc833 | -11.04138 | -54.04225 | 2026-09-28 05:12:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| afc11a34-70cf-39f3-b51b-d301c3fb056c | -12.57203 | -43.50405 | 2026-09-28 05:12:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 65adb8ba-b987-33d0-9841-da18076bdeb2 | -15.1023 | -53.88651 | 2026-09-28 05:12:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3fac4d71-74c8-37f6-b721-b67d697c8408 | -11.1495 | -48.32311 | 2026-09-28 05:12:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| fd2f6d45-89c7-3be8-8717-0a01cd3e5518 | -14.60265 | -45.59069 | 2026-09-28 05:12:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d3962d7b-7cc0-3a83-9f2a-3e045c37d48b | -15.08967 | -54.71819 | 2026-09-28 05:12:00 | NPP-375D | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c7c4a036-7011-3496-8db9-e50fb4ccefb3 | -12.13755 | -57.17351 | 2026-09-28 05:12:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 560f555c-37b8-34ac-bb5b-a39523ac69d4 | -12.62372 | -47.28096 | 2026-09-28 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 471db856-dfb4-3ea3-8a56-45e5969755e4 | -14.52246 | -48.30208 | 2026-09-28 05:12:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 92b2313a-7b05-3805-928e-eae4d1b6aba7 | -11.38586 | -45.39879 | 2026-09-28 05:12:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 163a2872-0439-3198-9a27-3c3055d61664 | -12.25949 | -53.99366 | 2026-09-28 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| beca0416-8428-3c8a-8098-7710a72fffb9 | -15.19329 | -48.43546 | 2026-09-28 05:12:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5fa819e3-5a65-34d3-b8df-21733851bd5b | -11.07894 | -51.39817 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 359b7b4d-acff-3ad3-b643-ade3ec5b5aa5 | -12.73794 | -47.2976 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 23823070-9ff9-37c6-ac2b-55a93e3d3d18 | -13.45538 | -48.58973 | 2026-09-28 05:12:00 | NPP-375D | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0ffd34df-8b84-3d6e-b809-030da94aeff4 | -11.0701 | -51.40618 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56d7e837-e4ef-3a35-a5f8-cff7c9619dde | -12.74729 | -47.30453 | 2026-09-28 05:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 52.6 |
| d6d14f3a-da9b-34b2-97c4-bb017814877b | -10.89785 | -50.69334 | 2026-09-28 05:12:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa63de85-92a2-3e13-9673-8725e1971b9e | -10.404 | -53.81324 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bc44bee7-932f-30dc-a690-fd19cdfe7eb7 | -10.42427 | -53.83875 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1c7ab64f-065d-355f-bd0a-4ce938d58860 | -10.41582 | -53.82627 | 2026-09-28 05:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README54.md)
