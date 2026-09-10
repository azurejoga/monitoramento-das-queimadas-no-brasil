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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fe078cd8-3d8d-329b-9c77-86ebb46c2bd8 | -10.7769 | -45.96 | 2026-09-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 139d0448-366d-34cd-8ea1-25b846260b16 | -13.2297 | -61.6384 | 2026-09-10 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 42.2 |
| c080d35e-92a2-36b3-86fb-692993dd2043 | 0.2667 | -51.4597 | 2026-09-10 01:10:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 58.6 |
| e5f194a5-2066-32d2-9c04-24dc1fe03c53 | -10.7578 | -45.9624 | 2026-09-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 164.4 |
| fe04072d-3f95-3ea3-a321-0523243e4f73 | -5.7569 | -45.084 | 2026-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 339.2 |
| 80499a31-d6fb-3e18-a24d-580c3f4efd72 | -20.558 | -57.4771 | 2026-09-10 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 57.5 |
| bedb597a-ba94-3a72-8cb1-7c015b66679b | -20.5381 | -57.459 | 2026-09-10 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 71.2 |
| 32654afa-2505-32bd-b93e-af0f30326dce | -7.9834 | -43.9951 | 2026-09-10 01:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 51024197-154a-33bc-b592-a8703f55b836 | -20.5584 | -57.4561 | 2026-09-10 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 58.0 |
| 8a500f7a-7a6a-34f3-b84e-e81c5a709ff5 | -10.7772 | -45.9372 | 2026-09-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 61.5 |
| e1e43358-86f7-38a6-9270-53949363f2c4 | -6.5637 | -62.8908 | 2026-09-10 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 2b311c9d-6033-3733-93b9-10e984408299 | -5.7756 | -45.0826 | 2026-09-10 01:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 397.7 |
| 15ac933a-8bb4-3b3f-88fe-fdbc819b0859 | -13.2295 | -61.6578 | 2026-09-10 01:10:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 133.0 |
| b9c55029-2039-3a63-9f77-86fc968dafee | -10.7582 | -45.9397 | 2026-09-10 01:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 7bb2c1e3-7a02-3255-ad7c-c443d06f8078 | -12.83 | -44.3 | 2026-09-10 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 81ebaaa8-9572-31d9-ad11-55dfac527976 | -5.76 | -45.05 | 2026-09-10 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7c6aea0-383c-3db5-9508-1a751270dded | -12.83 | -44.4 | 2026-09-10 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 957715ea-3d1c-3109-91ce-b2e763c84a14 | -12.86 | -44.31 | 2026-09-10 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d55ae73f-7457-364e-928c-1eba2e998ce4 | -12.86 | -44.36 | 2026-09-10 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f6788fd0-113b-3375-bf6b-51f69d728323 | -5.76 | -45.09 | 2026-09-10 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6cefa843-3b2d-33a9-984f-acb3d0b2891e | -12.86 | -44.41 | 2026-09-10 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2dfa496c-faf0-331c-b3bc-8796f4d10db3 | -12.83 | -44.35 | 2026-09-10 01:15:00 | MSG-03 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0dc84df7-34dd-3fc9-812d-7a2f5d7bcd53 | -5.79 | -45.05 | 2026-09-10 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9d0b36c9-4564-3766-a55f-42e63a67357d | -5.79 | -45.1 | 2026-09-10 01:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1b7cd8ee-e251-305d-8b08-4161b3dead57 | -10.77 | -45.94 | 2026-09-10 01:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f49b84d0-a3c5-38d0-ab52-d491a15efd8a | -13.2295 | -61.6578 | 2026-09-10 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 812450c0-6fb9-3b1b-b710-67a42a5f7dc7 | -10.7769 | -45.96 | 2026-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 3acf89c9-8819-3406-9379-bdc0a9dda414 | 0.2483 | -51.4597 | 2026-09-10 01:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 8a6c71db-e3f9-3e38-85da-21dfe7e7ca92 | -4.3587 | -47.7853 | 2026-09-10 01:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| aaf53dad-903f-3f40-92ec-c655d0307fdf | -2.9391 | -50.4832 | 2026-09-10 01:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 0ea05924-99a3-3df2-af5a-3c23d07e4753 | -10.7578 | -45.9624 | 2026-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 037b792b-9e80-39fa-a720-62ae0bb59ff2 | -6.5453 | -62.8914 | 2026-09-10 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 127.4 |
| 552aef5c-a1f0-35ea-8ad3-b564d7cb0d27 | -6.5636 | -62.9096 | 2026-09-10 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| a087156b-cf7f-3b31-a474-a6bc684c2053 | 0.2667 | -51.4597 | 2026-09-10 01:20:00 | GOES-19 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 3004a643-9c25-354c-93b2-c1ed458bd006 | -5.7569 | -45.084 | 2026-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 389.8 |
| 5ba934f1-e2e4-3c6f-ba3a-464958b816d5 | -13.4453 | -43.8366 | 2026-09-10 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1a92405a-1eee-3a91-bb82-9ef48cb0c258 | -2.7331 | -57.6271 | 2026-09-10 01:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 7c3c7b38-39fa-3077-9d2b-493694a633ed | -5.7754 | -45.1053 | 2026-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| b8175426-6de3-38e1-a6ba-ee632632ead4 | -13.2487 | -61.6371 | 2026-09-10 01:20:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 46.7 |
| adbd14b8-4642-351b-95a6-9a552d5ed113 | -5.7567 | -45.1067 | 2026-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 112.6 |
| 7e17fb2e-4bd9-3cbc-a57b-f20a6d5c51f4 | -6.5452 | -62.9102 | 2026-09-10 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| e73c5323-5605-3df0-bc2f-00b86f1f7434 | -7.9837 | -43.9719 | 2026-09-10 01:20:00 | GOES-19 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 45f911f6-69f7-3af4-835a-78ed9463b0ca | -5.7756 | -45.0826 | 2026-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 283.1 |
| 4ce504d7-c0f7-31a8-ac1c-4181931f1971 | -10.7772 | -45.9372 | 2026-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 25f405c3-970a-3a0b-92be-fb9e85288eca | -5.7758 | -45.0599 | 2026-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 7ea20b0f-182d-3f29-a587-7ed762777d4c | -5.7571 | -45.0613 | 2026-09-10 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 4f1ccd54-008f-3fb8-930f-f8349a6da6b1 | -6.5637 | -62.8908 | 2026-09-10 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 153.5 |
| a5300e70-b141-349e-8110-ceb713f5a077 | -7.9834 | -43.9951 | 2026-09-10 01:20:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 4d035b48-61a4-3213-b3f6-1be668883785 | -10.7582 | -45.9397 | 2026-09-10 01:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 119.7 |
| c269a981-4de3-3c15-9718-c6ec60b195f8 | -20.54623 | -57.49331 | 2026-09-10 01:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 34.1 |
| f631ece0-786b-345f-b965-e59b554e3ccf | -20.53995 | -57.4612 | 2026-09-10 01:20:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| f2b96579-d5e7-31d9-9bfd-06dbafdf8b75 | -13.23256 | -61.66637 | 2026-09-10 01:22:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 119.8 |
| c059eb8a-5fd6-3917-9b79-98d9e3357c9e | -9.04606 | -65.40747 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d5e15109-d72e-30a5-bd4a-26f3eddf9ab1 | -9.92491 | -67.88229 | 2026-09-10 01:22:00 | TERRA_M-M | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 5.5 |
| ebab836c-34da-3f16-bbc9-8ac1e7bc3bce | -13.21859 | -61.65273 | 2026-09-10 01:22:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 15.3 |
| d0dbf484-64f6-35ce-ba1c-02663b2bc945 | -8.99678 | -65.40774 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| 50e9b3b6-5989-3810-8eb7-498de2dac174 | -8.98908 | -60.59035 | 2026-09-10 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 47d60b2e-b4e5-3b7a-a1b5-34ef26fe4d24 | -9.22467 | -63.64984 | 2026-09-10 01:22:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d753499e-0197-3a49-a5ec-5dbbfd34361a | -13.22898 | -61.64529 | 2026-09-10 01:22:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| e00d5d62-bee0-38cf-b53b-2f19cf68c5fe | -9.20349 | -65.77187 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 48f569f3-7280-3816-9a56-089eeb9a12e7 | -8.62762 | -66.51596 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3ea9332d-bc2a-32f3-873a-d38f5ad1fa8c | -9.04799 | -65.42033 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 3c2801e0-9d6f-33ce-b802-ffd9fa252899 | -9.16958 | -68.21205 | 2026-09-10 01:22:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 3322da39-2f45-372d-9e71-2f72d51ab4dc | -13.2316 | -61.65039 | 2026-09-10 01:22:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 9b46c8b4-dbfe-35f4-a807-4d64e5d43cc1 | -8.98522 | -60.58552 | 2026-09-10 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 30.7 |
| a8386f6f-859f-31bf-94e1-c93e88384a79 | -8.73318 | -62.38929 | 2026-09-10 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 2bea354c-0407-3f0e-ae99-47ae75ffb1a4 | -10.61764 | -68.6099 | 2026-09-10 01:22:00 | TERRA_M-M | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.7 |
| f0586d56-611e-328e-971e-abbedaf2c282 | -9.03628 | -65.7478 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 592d7a56-cc02-3ac2-85ab-055f049e0b5c | -8.88541 | -70.84415 | 2026-09-10 01:22:00 | TERRA_M-M | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5e869527-f0a0-3be1-a0d2-9fdcb80c12f3 | -13.22202 | -61.67384 | 2026-09-10 01:22:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a06f3f54-f018-36c3-b803-125bde7b782a | -8.73831 | -62.39419 | 2026-09-10 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 15a83a08-219b-3a05-8883-06c1f5082799 | -9.21687 | -63.63988 | 2026-09-10 01:22:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 2d6dbc57-95fd-3f1e-8980-f81255bc9dcc | -9.03754 | -65.42197 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e2321453-f211-3803-a314-91e436387433 | -10.62338 | -67.9285 | 2026-09-10 01:22:00 | TERRA_M-M | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 808f719e-427b-34fe-b235-e4bc213515bd | -8.82641 | -63.8151 | 2026-09-10 01:22:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ca95872e-cf56-367f-bfff-e808666f3614 | -8.62453 | -66.51113 | 2026-09-10 01:22:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| ef073330-3f8e-3d59-9808-b632efbcf3e9 | -9.21947 | -63.65716 | 2026-09-10 01:22:00 | TERRA_M-M | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 104cd3ab-dcab-30eb-b2a1-c92d7749b1bb | -9.08417 | -67.87067 | 2026-09-10 01:22:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 43826ecd-ce8e-3615-9003-b0bb9aa7aeed | -12.16019 | -64.13551 | 2026-09-10 01:22:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 08411d93-b652-3803-8b8c-79b12c63b35e | -8.89591 | -61.42986 | 2026-09-10 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 2eea9fba-eef6-365c-a87b-555ba50abe0a | -9.16828 | -68.2029 | 2026-09-10 01:22:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 5004aebf-edc4-39da-9376-ce400f6ed5eb | -10.85242 | -60.84418 | 2026-09-10 01:22:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 478cd7a6-a28d-32f2-995b-3e632029348e | -10.85119 | -60.84997 | 2026-09-10 01:22:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 15.2 |
| a71c8788-9d2c-3781-89df-f6b31d5f9a02 | -13.23501 | -61.6715 | 2026-09-10 01:22:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 68d2d66b-8396-388a-a2fa-4f9e64c0da43 | -8.90016 | -61.45602 | 2026-09-10 01:22:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 1eb3979f-77c3-34c6-a16c-38c80f4ef11b | -6.4603 | -62.86953 | 2026-09-10 01:24:00 | TERRA_M-M | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 33.2 |
| 2cb24f92-2c0c-393c-ad82-0cbdf6a1331a | -7.84962 | -72.9265 | 2026-09-10 01:24:00 | TERRA_M-M | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d94ab7fe-42cf-3545-a42b-e61c8123101c | -5.7756 | -45.0826 | 2026-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 318.1 |
| 79da76aa-89c2-3f22-839b-27d3b95efe6b | -2.7331 | -57.6271 | 2026-09-10 01:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| bbca9c2e-6918-357f-9c00-716d0fa634b4 | -10.7578 | -45.9624 | 2026-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 246.8 |
| d583287f-f74d-3444-a09e-d5b28e3d4fdb | -5.7567 | -45.1067 | 2026-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 3f021862-04ba-39dc-9931-b6d37d93c7af | -20.5381 | -57.459 | 2026-09-10 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 55.8 |
| 476e50a7-3f22-3448-9997-aeb0bae9d50f | -5.7758 | -45.0599 | 2026-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 25154d3e-15df-3446-9cb9-4d0ab1d52fb3 | -6.5452 | -62.9102 | 2026-09-10 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 71.8 |
| b20f0470-d062-3c49-967d-f3514f315788 | -6.3487 | -35.3238 | 2026-09-10 01:30:00 | GOES-19 | ESPÍRITO SANTO | RIO GRANDE DO NORTE | Brasil | 2403509 | 24 | 33 | nan | nan | nan | Mata Atlântica | 126.1 |
| e4f63979-2188-3fdd-abf8-5ab11d1ec14c | -6.7695 | -58.6097 | 2026-09-10 01:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| 3b1eeb2d-02c0-3106-89e2-0f49c8acbcab | -6.3484 | -35.3511 | 2026-09-10 01:30:00 | GOES-19 | VÁRZEA | RIO GRANDE DO NORTE | Brasil | 2414704 | 24 | 33 | nan | nan | nan | Mata Atlântica | 79.6 |
| 1bfa1f5a-8a74-3018-bdd3-feef79393844 | -10.7582 | -45.9397 | 2026-09-10 01:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 263.7 |
| 36ba5125-6ba4-3dda-924c-66503d7121db | -6.5637 | -62.8908 | 2026-09-10 01:30:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 98.4 |
| 69b7ce9b-6093-3c9c-96cd-82e46309e93f | -5.7754 | -45.1053 | 2026-09-10 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |


[Clique aqui para ver as próximas entradas](README10.md)
