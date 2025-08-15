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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c7140c5a-470d-35f6-a7e1-3fad46518181 | -5.762 | -46.6741 | 2025-08-15 01:30:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 290e8ff0-6071-3b8a-b902-be6a4c0658f4 | -9.4994 | -60.5278 | 2025-08-15 01:30:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 170.1 |
| f1f200c3-2a7a-36ae-ace8-cca42157eb28 | -11.3657 | -55.4107 | 2025-08-15 01:30:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| 24e388f8-853d-32c6-aaa1-1144371ac496 | -7.0797 | -59.2157 | 2025-08-15 01:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.8 |
| 3573895d-7013-3edb-bac3-09efbbb8848e | -6.0808 | -59.9274 | 2025-08-15 01:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| e2efbe11-9aef-32b2-bd16-3cea6df2a8b9 | -9.1706 | -59.6762 | 2025-08-15 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.4 |
| ffc63912-d678-3c5d-9b17-1f3106f30929 | -9.152 | -59.6772 | 2025-08-15 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 61812e35-477d-3d63-aced-2d9912280255 | -7.0797 | -59.2157 | 2025-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 92.7 |
| ecba6e2a-935b-3f51-be82-7ac3a5eb4ffb | -20.4101 | -45.3981 | 2025-08-15 01:40:00 | GOES-19 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.9 |
| 31fb40bc-957e-3f4e-9175-5c833d5bd19f | -6.9302 | -59.5497 | 2025-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 82004a25-674f-3885-89b6-0a5907d761cc | -7.5291 | -61.3444 | 2025-08-15 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 84.0 |
| d2618e0d-0da4-36b3-be66-774d986ed699 | -5.762 | -46.6741 | 2025-08-15 01:40:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4befee41-f4db-3975-95ff-8f424af23587 | -7.5919 | -63.4978 | 2025-08-15 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 51.3 |
| dfc36e64-cf9c-316d-9f9c-d2efc772022a | -9.208 | -59.6548 | 2025-08-15 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| fa02b695-9015-3bbd-b2f3-8b9c49e2aea4 | -9.5179 | -60.5461 | 2025-08-15 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.4 |
| fcc8310a-4547-3d65-a477-f379806ab9e2 | -11.3466 | -55.4326 | 2025-08-15 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 79.4 |
| d09912a6-ede1-3202-a850-31a607abcebf | -11.3657 | -55.4107 | 2025-08-15 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 109be393-2f49-3974-a542-82bb2971a978 | -9.518 | -60.5268 | 2025-08-15 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 113.7 |
| 169fe5fb-c0ae-3d7f-8ff9-a108295328cb | -9.4994 | -60.5278 | 2025-08-15 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 148.9 |
| 596ef28f-b62c-310e-ac59-6671c7ff7c17 | -3.4254 | -49.0517 | 2025-08-15 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 65319dda-43b0-3e38-91bc-643f90ab09d9 | -14.2444 | -44.5897 | 2025-08-15 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| a092c567-fd16-3036-89d9-39483707a525 | -7.6104 | -63.4972 | 2025-08-15 01:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| bec485f8-c232-388a-aaf2-e863cbd8c594 | -9.1708 | -59.6568 | 2025-08-15 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 21d090ee-5ce8-327f-ad78-73dda3a3ab43 | -11.3468 | -55.4124 | 2025-08-15 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 127.8 |
| e4030da6-5e81-36b8-b367-2c58f35cde0e | -9.1894 | -59.6558 | 2025-08-15 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 805f3155-10ed-30b1-97a6-572a7f882a0b | -18.7146 | -48.1836 | 2025-08-15 01:40:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 50.3 |
| a6016187-9007-374b-846a-08593f0bbc00 | -9.4992 | -60.547 | 2025-08-15 01:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 2fdcf7d8-05e0-3ff8-8a7a-05e77e78b773 | -14.2449 | -44.5661 | 2025-08-15 01:40:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 13ec470d-9423-359f-9895-1baab5d82bcb | -7.5292 | -61.3254 | 2025-08-15 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 107.9 |
| 37648912-fef5-3cbb-adbc-b1a04beeef09 | -9.1892 | -59.6752 | 2025-08-15 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| fe1ec76f-1ef4-3891-9d96-15183e868bb9 | -5.455 | -60.1391 | 2025-08-15 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 1f6a8e3c-ce3d-36f1-b688-7bb21ea2a809 | -6.9303 | -59.5305 | 2025-08-15 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 6199f12a-51b2-3e65-afcb-0d946f1a4671 | -11.3655 | -55.431 | 2025-08-15 01:40:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 52efe522-3dd5-302c-ab58-a920ad2c6b2f | -6.7129 | -58.8251 | 2025-08-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 104.6 |
| c58cb302-9eda-34f6-bf33-7450343077b9 | -9.1706 | -59.6762 | 2025-08-15 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 0d56db5f-a228-311e-8a01-fbef749bca6f | -7.6104 | -63.4972 | 2025-08-15 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| ee70d016-2521-3fa2-a163-8a0db3c5fe0c | -6.9302 | -59.5497 | 2025-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.5 |
| 89c6a373-578c-331d-bb52-eaaf6e6d54ef | -11.3468 | -55.4124 | 2025-08-15 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 215.2 |
| 80a79d1b-141e-3f31-9ff5-f5fc1b8e3c75 | -6.0623 | -59.9472 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 18ef5495-84d2-34f2-bb7b-3e9a4b8a1149 | -7.6103 | -63.516 | 2025-08-15 01:50:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 058d9fd0-e476-328d-96a7-c485391b8004 | -9.4994 | -60.5278 | 2025-08-15 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 201.3 |
| 31c80701-7dfd-3855-ac42-aa75f1b449b3 | -9.4992 | -60.547 | 2025-08-15 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 76e6ab62-0a18-34ae-9dc0-d3e1c0ca32e6 | -6.0807 | -59.9465 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 255.1 |
| 6b5e0310-532e-35ed-9c0e-b0e1d0da713d | -7.5291 | -61.3444 | 2025-08-15 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 2c30fb6a-1551-34b3-b9a9-0e499eae6aee | -11.3657 | -55.4107 | 2025-08-15 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 94.1 |
| 8ca73121-1831-3b5b-838c-78e49f75f091 | -6.0806 | -59.9657 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 128.5 |
| ac583cf6-6509-37cd-93d1-240565f98f73 | -5.762 | -46.6741 | 2025-08-15 01:50:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 58.2 |
| 2af0bfef-b684-3d6d-ac05-581e969e019a | -7.0797 | -59.2157 | 2025-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 07b8c1de-a88b-3d43-80cc-8834f9cc402b | -6.946 | -60.0104 | 2025-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 15a41da5-a30a-31cd-af1c-9237c95646ea | -6.676 | -58.8267 | 2025-08-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 84.5 |
| a7b7c64b-6f9c-3e9b-9149-c67fb00f57b3 | -6.9303 | -59.5305 | 2025-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.8 |
| dfebf942-b7f8-3aa1-af87-347178591202 | -6.6944 | -58.8453 | 2025-08-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 837a75b8-205e-3d1c-b61b-5e783ceac013 | -16.2957 | -52.923 | 2025-08-15 01:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| 690eebf7-52a4-3b26-b067-4e5ba7dc048c | -18.6944 | -48.1877 | 2025-08-15 01:50:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 49.9 |
| cbec0028-4beb-3820-bfa0-18f6e20343aa | -9.5147 | -40.3558 | 2025-08-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 268.1 |
| 8ab5b646-eb15-3191-b153-c0e43089d520 | -6.6576 | -58.8274 | 2025-08-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 1b7ac774-257b-3278-ba3d-3eb994d49087 | -9.1892 | -59.6752 | 2025-08-15 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 12c0374d-2595-3609-b435-6cf51ef79ab1 | -6.0991 | -59.9459 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 9a0d13c0-9baa-310e-93e4-b0bccf292b71 | -11.3655 | -55.431 | 2025-08-15 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 159.2 |
| 6ef86a36-566b-3443-a3e0-3a161ce99ee1 | -5.455 | -60.1391 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 114.6 |
| 4c19e1dc-d9d9-314e-b0d6-e88b47c743ec | -9.5152 | -40.331 | 2025-08-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 169.8 |
| 66d8a761-7709-380e-9eeb-d32ba92aab67 | -6.6945 | -58.8259 | 2025-08-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 130.9 |
| 5875e123-1305-3909-a51d-a94f0664b594 | -9.3875 | -60.5528 | 2025-08-15 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 98262421-1386-3cc4-91b3-21cdbd7fe428 | -7.5292 | -61.3254 | 2025-08-15 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 2e789d60-910d-3f2d-a788-a8f804826bdd | -9.5179 | -60.5461 | 2025-08-15 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 0a2341f2-ab27-3aea-b1c7-a5aa40372b92 | -9.4956 | -40.3586 | 2025-08-15 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 69.4 |
| 78957514-cf61-36d9-91e2-30002643f515 | -9.1894 | -59.6558 | 2025-08-15 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.6 |
| ac2ea726-d1eb-340e-9aed-4b6d3599ad36 | -6.6577 | -58.8081 | 2025-08-15 01:50:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 694cc0cb-4f3d-3254-9ab3-1623011b907e | -11.3466 | -55.4326 | 2025-08-15 01:50:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 7a28b097-6db6-3e81-a1af-26b040e564eb | -6.0622 | -59.9663 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 9d650972-9857-38d8-a4be-56dd4dd20efd | -9.1708 | -59.6568 | 2025-08-15 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 4762d6f8-8088-3c01-920b-4a934cb2ae7d | -9.152 | -59.6772 | 2025-08-15 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| c969c784-8b1a-391c-9c1d-a2f988cdb145 | -9.208 | -59.6548 | 2025-08-15 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.9 |
| b99da212-518c-3b9d-bd3d-4ac0898cf760 | -6.0808 | -59.9274 | 2025-08-15 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 59adc082-f8df-3734-ac22-9e10ebbb66d1 | -9.518 | -60.5268 | 2025-08-15 01:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 812fd03b-5f3c-353d-b1e2-1683bce219b3 | -15.6541 | -49.7757 | 2025-08-15 01:50:00 | GOES-19 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 6bf38074-be48-3050-b4ca-70b4e63169ff | -5.455 | -60.1391 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 101.1 |
| 4ab37f63-4553-32d7-8d8e-de22bd1aca1b | -9.5152 | -40.331 | 2025-08-15 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 136.9 |
| 070d1170-1446-3e2e-bf41-abc445c3fa39 | -11.3655 | -55.431 | 2025-08-15 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 242.8 |
| 7a88c8b2-6074-3cb0-9cd3-1118af401dd7 | -7.5292 | -61.3254 | 2025-08-15 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| 09c9d996-ca84-32fa-9a97-ede21daa0ae4 | -9.1706 | -59.6762 | 2025-08-15 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.2 |
| f2887247-e919-3a01-8012-90e1e4151e16 | -6.0622 | -59.9663 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1920c417-d08d-3aca-94e5-960723f762ec | -7.5291 | -61.3444 | 2025-08-15 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 4db805a3-a185-3729-b431-1fd3c30a649f | -7.5919 | -63.4978 | 2025-08-15 02:00:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 448f500d-8b31-3ff5-908d-bdce7676dc2d | -6.0808 | -59.9274 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.7 |
| e890e987-5f7a-36f3-92e4-2ad0ffa953ab | -9.4994 | -60.5278 | 2025-08-15 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 138.7 |
| d0d635f2-7e47-3a3c-b9b3-4151f570ab00 | -9.5147 | -40.3558 | 2025-08-15 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 223.5 |
| 7d520e86-e994-374a-b55d-bb470185fb36 | -11.3466 | -55.4326 | 2025-08-15 02:00:00 | GOES-19 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 193.3 |
| f82f7ec3-b406-33b4-887e-9dcb22752727 | -5.762 | -46.6741 | 2025-08-15 02:00:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 66.7 |
| d4f2c5bc-d77e-35ae-b251-88c0eadc142f | -9.1894 | -59.6558 | 2025-08-15 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.5 |
| 48ca4235-f090-31fd-b0fb-cda0bdfcde75 | -6.0991 | -59.9459 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| a9e0a622-2033-32ae-8f20-4921d02db0b5 | -9.1892 | -59.6752 | 2025-08-15 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 2d0804de-6f76-39da-8d03-a0b931cf4bc4 | -9.152 | -59.6772 | 2025-08-15 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.0 |
| abc524ef-920d-3c02-b33f-e3f3f7e690fc | -6.6944 | -58.8453 | 2025-08-15 02:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 19a44425-3bbe-3850-ae46-0f37e15f7909 | -6.0807 | -59.9465 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 154.1 |
| 1299cf51-b839-3656-978b-651b677b72ec | -14.2444 | -44.5897 | 2025-08-15 02:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 691cf1da-89fd-3ecc-9ac4-4b1ec9f3ca64 | -13.0696 | -57.1344 | 2025-08-15 02:00:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 668abb7f-e82a-383b-b1ea-1ed6e1ab5ee1 | -7.0797 | -59.2157 | 2025-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| e15e87f6-7905-3517-a204-1cbb49a84327 | -9.4992 | -60.547 | 2025-08-15 02:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 5f21b4fe-a5d9-31e4-a326-37e2c3f8203d | -6.0806 | -59.9657 | 2025-08-15 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |


[Clique aqui para ver as próximas entradas](README14.md)
