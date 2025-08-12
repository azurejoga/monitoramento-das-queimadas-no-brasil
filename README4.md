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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39061a7b-da21-3880-af82-0b2c542f0d3a | -7.64432 | -56.72668 | 2025-08-12 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b5f123f6-fafd-3192-88b9-4ca9b6dd3c49 | -9.19091 | -59.66941 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| bb63eb19-43b7-3219-be95-7f3a29a287ba | -7.64555 | -56.73554 | 2025-08-12 01:09:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 391eda0c-4bc4-3544-a198-fc89525a8f0c | -9.38159 | -61.5332 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 43d2ca74-e0d4-3c02-acaa-618a6fd7681e | -9.19942 | -59.65647 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 42950272-3be0-3a8c-a6a0-24ba69bf9d7d | -7.07752 | -59.19226 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 8eb80be7-87f5-3e62-a3f3-26f5ecffecf0 | -7.13936 | -60.13203 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 76.5 |
| 64056105-1b36-36b3-84ad-dc502c4c2a2f | -7.91458 | -55.42701 | 2025-08-12 01:09:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fd5e8d4b-9c90-3e7f-b05f-03a4a6c17c02 | -7.06516 | -59.21073 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8e6e286a-4bc1-326a-9ddf-f2d8801e87f4 | -6.10126 | -59.92626 | 2025-08-12 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 21.4 |
| f7399414-c382-3a29-904b-61b16417180d | -6.11103 | -59.92485 | 2025-08-12 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b3a3285e-5d54-3edb-945c-4dafde7504aa | -6.97319 | -59.28144 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.8 |
| 37356355-5673-32ce-b315-d1e25db0ad8e | -6.96368 | -59.28273 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 3d54e2e6-65aa-32cb-bc0d-ba70a5eed1e6 | -7.07075 | -59.21413 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 07285eb9-c787-3465-ac57-1a07c0e5ee8d | -7.06939 | -59.20381 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| c3966d72-49a1-3fb2-9a57-91fb793db553 | -7.12931 | -60.13343 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 36.4 |
| 92eb6b4f-2c45-3ab0-885e-3a5c6c98cb94 | -7.06375 | -59.20042 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 55c57b5f-1338-3342-b896-7f6ead1442db | -8.92857 | -60.73608 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| f4e90657-29a0-3375-8865-421fab91c22f | -7.88145 | -63.26438 | 2025-08-12 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 88f395ee-0687-3711-96b9-fc97abcd6a95 | -7.08023 | -59.21283 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 716946b5-13cc-3104-879e-0100e2265eb5 | -7.14789 | -60.11924 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b013ca1d-fd9e-34a5-b9d8-42249a036ff2 | -8.92117 | -60.76486 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.9 |
| c3c2db5e-3c4d-34b9-87a5-2a85729774ee | -8.56072 | -54.66656 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c6f9d739-0a3f-3fa6-846b-2cf67ddf62b6 | -5.84358 | -59.91347 | 2025-08-12 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ca4948be-78d0-3706-b504-9bc23d68dcac | -9.20095 | -59.66815 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 86e4390e-fe35-393f-bbf2-10a41be3e164 | -7.8705 | -63.27125 | 2025-08-12 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 12.7 |
| a3c63365-72ca-35fe-8fa9-6d4140233937 | -9.38501 | -61.53914 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| dedd76cc-7ede-3246-a464-6c319ac60adc | -7.1278 | -60.12191 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.0 |
| 6640ba3d-fc36-323f-84b5-59d176b3197e | -6.10272 | -59.93716 | 2025-08-12 01:09:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 9c2eaafb-0914-389c-9747-9433812524ff | -6.97459 | -59.29175 | 2025-08-12 01:09:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 1726ad22-f181-32bc-87ee-544c33ffa64d | -8.56641 | -54.7056 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 6e3bbca7-c746-3617-bf88-809d9c6f694b | -8.56006 | -54.71247 | 2025-08-12 01:09:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 0aad22f6-efe4-31e5-9e53-b93d4194c089 | -7.88396 | -63.28495 | 2025-08-12 01:09:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 26275e01-3120-3df4-8c5f-941c56e48810 | -8.93937 | -60.73468 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 967c3df6-325f-338b-967a-ad59118eb298 | -6.30956 | -51.40082 | 2025-08-12 01:09:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| d183b973-58cb-3cf8-a661-ab1f4f6c6e72 | -8.94109 | -60.74835 | 2025-08-12 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cc402788-3e3a-3488-9799-83ab4f28a2a7 | -12.5746 | -46.9781 | 2025-08-12 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 7da8a8ea-bdb7-3395-9bfe-9ffeb4099445 | -7.1483 | -60.1174 | 2025-08-12 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| b4d34885-2fc7-3675-9d4e-b2a1a39e3e31 | -12.7759 | -45.4445 | 2025-08-12 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 45.8 |
| 7ff691a0-2cfe-311c-98be-24444933ec73 | -9.3806 | -61.5315 | 2025-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.0 |
| ac758376-3bf6-33ac-b9f3-686dd8ce23e2 | -8.9215 | -60.7297 | 2025-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ec9ac459-eed6-3f21-a49c-5865eecde31b | -12.555 | -47.0034 | 2025-08-12 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 96804260-19b4-3e63-b619-8d41ea41115b | -22.6353 | -54.9867 | 2025-08-12 01:10:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 113.6 |
| 60b559d3-561c-32f5-affd-ea03cc15ab72 | -9.5152 | -40.331 | 2025-08-12 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 93.4 |
| c77b8362-8bf9-3ea6-9fe4-0830ac35e74b | -7.1482 | -60.1366 | 2025-08-12 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.1 |
| 3c51b78e-420e-3f9a-aeca-fb909ae81c63 | -7.1299 | -60.1182 | 2025-08-12 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 160.3 |
| 4b810307-2b0c-3d83-84e4-97f430ab8d9f | -7.0799 | -59.1964 | 2025-08-12 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e8cf35e2-b03b-3fd5-af4f-8908e494bbcb | -8.5788 | -54.7162 | 2025-08-12 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 0dd9e3d7-a633-3ced-beb3-ec214fd89869 | -9.5147 | -40.3558 | 2025-08-12 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 87.0 |
| 1a2a1f3a-c278-39fe-8b39-53ce55e9b76c | -22.614 | -55.0123 | 2025-08-12 01:10:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 152.2 |
| 6b78b3e2-a459-3cf1-b419-f32c44ab0b57 | -8.5602 | -54.7175 | 2025-08-12 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |
| b1fe4091-30b2-3789-bdf6-e29dbc4d0d40 | -19.3109 | -48.4248 | 2025-08-12 01:10:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b267e312-f11a-321c-9328-2b656031b3f7 | -8.9401 | -60.7288 | 2025-08-12 01:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| bc1b4349-9062-383d-bb3d-66a2c095ca3e | -22.6348 | -55.0086 | 2025-08-12 01:10:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 138.8 |
| 526681f6-5d70-3ebe-aa05-ae94aab19faa | -12.5742 | -47.0006 | 2025-08-12 01:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 285.8 |
| e4b1b413-9765-3ecd-b34a-e389aea78f68 | -9.723 | -49.4806 | 2025-08-12 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 85.8 |
| e8470801-425e-3bb7-bad5-ef2e5ca7cabb | -16.2961 | -52.9016 | 2025-08-12 01:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| b83529a7-3797-3595-86c8-1c6899db4dc5 | -22.9828 | -49.0361 | 2025-08-12 01:10:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 83.2 |
| f6bededc-2943-3558-98d5-54d0f589a0d3 | -22.6145 | -54.9905 | 2025-08-12 01:10:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 123.5 |
| 527f30c1-274a-3db4-b78e-9b75d8608bca | -16.2957 | -52.923 | 2025-08-12 01:10:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 1fa0121d-47de-34cc-991f-7c775bf466e4 | -8.5211 | -43.3063 | 2025-08-12 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 79.6 |
| 697b51f3-0e87-3ba6-be4d-0c51bbf48e63 | -7.1298 | -60.1374 | 2025-08-12 01:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.7 |
| b27aa81c-0cef-3f77-900b-7fc0e8688686 | -9.7041 | -49.4825 | 2025-08-12 01:10:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 2fc404e9-5c81-366b-8264-7f1729987cc4 | -21.7801 | -48.3036 | 2025-08-12 01:10:00 | GOES-19 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 83.6 |
| 225e5bf9-f7e0-3f29-9cae-1ec93a67652e | -22.614 | -55.0123 | 2025-08-12 01:20:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 82.2 |
| be6597d2-4485-330b-97ec-d462c18371ee | -23.0038 | -49.0309 | 2025-08-12 01:20:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 58.7 |
| 003008ff-8f59-3484-a1fb-f7a2829fc8ef | -8.9401 | -60.7288 | 2025-08-12 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| f3babb2e-5246-342f-83e2-ef3f3a04e873 | -12.555 | -47.0034 | 2025-08-12 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 296.1 |
| 669ec0cd-7ab1-3dc9-984c-972368823e3a | -16.2957 | -52.923 | 2025-08-12 01:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 83.5 |
| 6ad5efa8-bc6c-3309-840a-32b10b7712c3 | -7.1482 | -60.1366 | 2025-08-12 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| d58dc1e4-e711-3fc3-b779-a1d8f77d2e6d | -12.5554 | -46.9809 | 2025-08-12 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 192.4 |
| 3600fdc7-820c-3f07-8dff-296dcee1c015 | -16.2961 | -52.9016 | 2025-08-12 01:20:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 6ef5a951-c9ab-3e2b-a85e-80b4f3ec91af | -14.6894 | -53.7272 | 2025-08-12 01:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 41290295-33c4-3ce5-a0a3-d687b102cc8c | -12.5746 | -46.9781 | 2025-08-12 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 259.5 |
| dd1fcb1d-3d59-307f-8f76-4aa27a65d5e9 | -22.6348 | -55.0086 | 2025-08-12 01:20:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 65.1 |
| 3bddc572-d047-3579-a6b7-79d5060ced2e | -12.5934 | -46.9978 | 2025-08-12 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d56a99bf-d615-3abe-8b0e-df3f3259c8b1 | -22.9828 | -49.0361 | 2025-08-12 01:20:00 | GOES-19 | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 38ba5209-12b3-3819-8ac3-5d97ec6e7b35 | -19.3109 | -48.4248 | 2025-08-12 01:20:00 | GOES-19 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 64ef749d-e33c-3fe6-a2b2-b944449f810c | -9.723 | -49.4806 | 2025-08-12 01:20:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 7d93c66e-858e-30b4-bc7d-43cfed8e12d7 | -9.3806 | -61.5315 | 2025-08-12 01:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| c0b90740-0d9f-300b-9eca-382f290306ec | -22.6145 | -54.9905 | 2025-08-12 01:20:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 54.9 |
| be4e8585-8f10-3bcc-b5a1-53353647f5aa | -8.5211 | -43.3063 | 2025-08-12 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 1f31dbb9-d99c-38f8-8693-06326c1d73e0 | -7.1298 | -60.1374 | 2025-08-12 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 32d020a3-af48-3595-a715-a1a89d06d2e0 | -7.1483 | -60.1174 | 2025-08-12 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 690f9a71-a676-3b85-abe6-823311ce9872 | -12.7759 | -45.4445 | 2025-08-12 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 13cf842b-18b1-3ec7-af55-64174f58751b | -8.5788 | -54.7162 | 2025-08-12 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 9fe1096b-b68b-3639-89d2-6ff6a2de9a8e | -12.5742 | -47.0006 | 2025-08-12 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 420.3 |
| 4e55fd90-21fe-3f9b-a1a0-88cfda4e0687 | -22.6353 | -54.9867 | 2025-08-12 01:20:00 | GOES-19 | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| 37b1e52f-e1de-3632-88b0-63ea6c7e3511 | -6.5856 | -44.564 | 2025-08-12 01:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 65.4 |
| cedb4d2c-91aa-3c07-9d6c-1e9c816511e8 | -14.6898 | -53.7063 | 2025-08-12 01:20:00 | GOES-19 | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 131c94e2-e74b-3f9c-af75-f1e56915ee96 | -7.1299 | -60.1182 | 2025-08-12 01:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 114.3 |
| d349582e-607b-3cbe-9d63-b347a93d8351 | -12.5554 | -46.9809 | 2025-08-12 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| f0c5407c-afaf-30bd-9bb3-7b7f4813d195 | -7.1483 | -60.1174 | 2025-08-12 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 5878ac49-6382-326b-a0b9-2a29a3e57656 | -8.5788 | -54.7162 | 2025-08-12 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.9 |
| 7a994c09-c724-3545-8901-1540d881b67d | -12.5746 | -46.9781 | 2025-08-12 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 159.1 |
| 77e9ad0f-997b-39a1-b7a8-0ac1d860faaa | -8.5211 | -43.3063 | 2025-08-12 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 4df11bdc-0332-33ed-a119-e697977fb817 | -7.1298 | -60.1374 | 2025-08-12 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e232865a-6de0-3a97-a34c-2eff8db52226 | -9.723 | -49.4806 | 2025-08-12 01:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| cc907aa8-848c-3f75-90e3-d3524d38a47b | -12.7759 | -45.4445 | 2025-08-12 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.4 |
| ef41d71d-0d6e-3359-b8c2-e32659b267da | -7.1482 | -60.1366 | 2025-08-12 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |


[Clique aqui para ver as próximas entradas](README5.md)
