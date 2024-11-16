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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 84ec09eb-6769-3beb-8b2d-6a731ca5c7ea | -19.766701 | -55.396 | 2024-11-16 00:47:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e02b9637-8bfa-3d61-8a71-95a5b62b4afc | -2.3456 | -47.471001 | 2024-11-16 00:47:00 | METOP-C | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 58beae35-8161-37b3-bf3f-ec08f4bb880f | -2.6661 | -46.196602 | 2024-11-16 00:47:00 | METOP-C | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61ccfd35-4927-3ff0-9fa1-34fce6c13585 | -3.3074 | -52.862 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8f73cc0-602d-313f-baf0-cef7d1c9abfb | -4.5538 | -48.006599 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97cad7ad-ec6a-3c7a-8a3d-73c8f3edf4f4 | -3.7256 | -45.6656 | 2024-11-16 00:47:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7a627cbf-6cad-3a1e-86de-cb67a7b74d48 | -2.3906 | -54.629299 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad641b24-93b6-3f5d-aecf-0c1b2031ab10 | -4.5519 | -45.7607 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa0e503-c489-341f-80b1-addc153af514 | -2.33 | -54.815601 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8e3b499-c5e9-3df6-b12c-65f95a922d0d | -2.2019 | -48.807701 | 2024-11-16 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c5d4a06-6658-3fad-9bbd-94235bfa2da9 | -0.8323 | -52.3172 | 2024-11-16 00:47:00 | METOP-C | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 88b00665-7e8f-3f92-a912-51b3d746c1e1 | -1.2805 | -52.472198 | 2024-11-16 00:47:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468f3b8f-8dfd-3c51-8702-c3ac2969b512 | -17.5469 | -57.506901 | 2024-11-16 00:47:00 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4bfa5146-f8c0-35dc-a8b0-a6fe8f6952f2 | -3.2401 | -53.5186 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c2f2be51-d9c7-3a0f-91f7-5f350e6c6c7f | -2.151 | -46.548 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cdc4b268-e42b-3369-894f-48cc69a97369 | -1.8569 | -54.2742 | 2024-11-16 00:47:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d4d17e2a-29f9-3a35-9b0d-6f3734bd6064 | -0.2984 | -51.5186 | 2024-11-16 00:47:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 1a42ddf0-f862-3722-af56-a1315f88a93b | -2.1473 | -53.695 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cfc98e0-7c70-34ce-b6bc-1ff1c2c2521c | -3.124 | -45.1675 | 2024-11-16 00:47:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7b9f88b2-63d9-3d73-b6d5-07061fbc316a | -4.6487 | -45.1269 | 2024-11-16 00:47:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dce2bd3c-47e7-3fad-a8b7-ba5bda85d83c | 0.1593 | -51.141701 | 2024-11-16 00:47:00 | METOP-C | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 7ec9f31f-2f4f-30a9-8cdb-642081fd4cbc | -3.4342 | -53.330002 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcdc21a4-a86f-318d-b52d-4e9f13827cc9 | -3.7478 | -54.7188 | 2024-11-16 00:47:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bd36e6e-b380-313c-acd1-693021c17a78 | -3.0334 | -45.088699 | 2024-11-16 00:47:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a3401192-b29b-39d6-9399-4dca1142378c | -3.0264 | -45.102901 | 2024-11-16 00:47:00 | METOP-C | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 76ed1cd6-5e48-329b-abb3-f34abe5f7b41 | -3.4949 | -47.2272 | 2024-11-16 00:47:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6938eed-f909-35a0-ae73-8a74cf65a52e | -3.6048 | -52.221199 | 2024-11-16 00:47:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2c81f63-8034-378d-8782-d01bc69bccd3 | -4.1356 | -49.362 | 2024-11-16 00:47:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e993443d-de8b-3711-9b40-672e410eb340 | -3.9075 | -49.044899 | 2024-11-16 00:47:00 | METOP-C | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e3f043a6-e880-32f4-8aa9-86b57a4ce22b | -2.0841 | -50.489201 | 2024-11-16 00:47:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0b0923b-2664-3ea3-9ee5-ced63a9fb7cf | -0.3052 | -51.502899 | 2024-11-16 00:47:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| d3a75f9f-4e68-303a-94e4-2f1451a1d339 | -1.2211 | -53.699902 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f69da9db-41ce-3d56-ac21-08bf947361bb | -0.2567 | -48.509899 | 2024-11-16 00:47:00 | METOP-C | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66888f0e-082a-34f0-8fdd-07db0b964f8f | -2.1508 | -53.710499 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08f1c437-c963-319e-be77-88d3c1cba5a1 | -4.366 | -45.628601 | 2024-11-16 00:47:00 | METOP-C | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 593f76c1-9abf-3dae-b829-e5a0d8b3ab32 | -5.7154 | -44.803902 | 2024-11-16 00:47:00 | METOP-C | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 20a05394-8c0f-3e67-8bb5-49d146b8b0ef | -4.2991 | -48.0648 | 2024-11-16 00:47:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66e336ef-7224-3128-834c-1ee1f58272f1 | -3.5819 | -50.541901 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 60f09170-a331-3b1a-a7db-505d5c00e706 | -2.4594 | -53.980301 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b3c8fff-ce31-3c71-a671-87a8092462e6 | -6.2954 | -39.492199 | 2024-11-16 00:47:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6a5f30dc-acec-35d3-a6c1-8d10d07dcabb | -3.3091 | -43.825401 | 2024-11-16 00:47:00 | METOP-C | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 42760fae-4610-31fe-ab7e-e3a5118272ca | -6.1326 | -42.5774 | 2024-11-16 00:47:00 | METOP-C | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d84611ff-9922-3d8e-b427-9708bfc6fad9 | -2.0993 | -46.591 | 2024-11-16 00:47:00 | METOP-C | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c01e28d-89f9-37ef-a6f2-247d6e56a0cc | -6.2889 | -39.466599 | 2024-11-16 00:47:00 | METOP-C | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| bd2cfacf-3763-3997-8178-30cf85210a69 | -3.5067 | -51.023899 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bdfab4c4-cc25-349f-8f22-80aa403a0a3d | -3.9658 | -45.809799 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 510311a0-7da1-37b7-92a7-4584d996a12a | -2.7688 | -48.583302 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 80ed83a4-5ae0-3aa6-8d62-f79a310f198f | -2.6083 | -54.545399 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c22127b8-ff52-30b5-a831-52d2e17bf916 | -4.3651 | -48.0825 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11bc680c-f28b-39ad-8e9e-fe685bfbc5b7 | -2.6539 | -46.188599 | 2024-11-16 00:47:00 | METOP-C | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bdc622a-405f-3895-9acd-1039c6375f41 | -2.5507 | -46.8923 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 47ee689f-119b-3f99-a48c-961a48341479 | -4.3829 | -48.070202 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2fae2eb7-257d-3660-a08c-596944d7c658 | -3.574 | -50.507702 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3ac26e8-b09d-3014-a961-f9474a38a677 | -3.7281 | -45.676201 | 2024-11-16 00:47:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 74598fea-6862-3116-b303-669fd44c1e6c | -1.6399 | -53.277901 | 2024-11-16 00:47:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3c7fd57-3f1e-3bf8-9964-3d68d9bfda07 | -2.6675 | -49.125999 | 2024-11-16 00:47:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7650bd7a-d825-37a9-94fb-dc433de266b3 | -3.2006 | -45.099998 | 2024-11-16 00:47:00 | METOP-C | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1bfd90ad-4649-30d7-a41a-3181b1c9ab0d | -9.3959 | -40.3256 | 2024-11-16 00:47:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 215ec90d-67da-3c33-8d80-f1fac2d00282 | -3.1314 | -54.5387 | 2024-11-16 00:47:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 823705aa-433b-3304-8cdd-96d8f82a8d25 | -0.2969 | -51.511799 | 2024-11-16 00:47:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9308e6b9-9287-3899-b435-30cc401b82a8 | -0.0987 | -51.2775 | 2024-11-16 00:47:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 71384fdb-0097-3c77-9666-e77735228406 | -3.3675 | -52.718201 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6928e7d6-393c-39e5-9272-dc9942641fd9 | -3.9811 | -43.712799 | 2024-11-16 00:47:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ad4729eb-3783-3176-a9bf-a236a8208cdf | -5.2347 | -44.905602 | 2024-11-16 00:47:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 40750b4c-b6e3-383d-8876-7134de1023e7 | -3.3675 | -45.413799 | 2024-11-16 00:47:00 | METOP-C | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4ddca68a-2836-3f37-9346-13fb62fc0cf1 | -3.4325 | -53.3223 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6989cfc1-d63e-3059-8cee-7bbff6af31ad | -1.2327 | -47.471401 | 2024-11-16 00:47:00 | METOP-C | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f5dbd9d7-a63e-3718-8aad-4b7349faf726 | -4.1565 | -45.440201 | 2024-11-16 00:47:00 | METOP-C | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 587dd9ff-09d5-32e9-af8e-79b4844c66c8 | -4.2983 | -48.1059 | 2024-11-16 00:47:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01d22f37-c2f9-3546-b242-db162085b617 | -2.7849 | -48.563599 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95bb2b1c-9e21-3871-afd9-fb140ae01026 | -2.1428 | -53.720402 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5846bc29-1979-388b-83a8-927090a46a75 | -3.978 | -45.818001 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 71d41640-2715-3e18-a271-0c68b5be1196 | -2.5814 | -54.426701 | 2024-11-16 00:47:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adec1420-5d8b-3e17-ab02-6baf9bb854f5 | -4.0242 | -49.192699 | 2024-11-16 00:47:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2895349b-2080-3f04-ae9c-fb50065eb77c | -4.0909 | -49.973701 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67dbd770-9748-35de-a1ea-d3e9c4380d58 | -3.9756 | -45.807598 | 2024-11-16 00:47:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a7412df2-3514-32ca-a78d-861de0715287 | -3.7379 | -45.674 | 2024-11-16 00:47:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0d669c2b-f333-3912-853a-8f0d56adbe58 | -3.3172 | -52.859901 | 2024-11-16 00:47:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3a0c486-82e5-3d90-bd37-805b4b624091 | -10.6577 | -44.491299 | 2024-11-16 00:47:00 | METOP-C | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aedbef73-f223-37e8-86e8-aec5cbb7bf82 | -0.9274 | -52.507 | 2024-11-16 00:47:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ee6620d-4844-352b-9417-501f8fa27702 | -3.5803 | -50.535 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2f06e6df-dafc-31b6-ac33-3d34a78e097d | -3.8825 | -52.263901 | 2024-11-16 00:47:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d72984c-6676-3d53-98b7-68ced8a35f3f | -3.9845 | -43.727001 | 2024-11-16 00:47:00 | METOP-C | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0f826b-8105-3268-8926-258065440e73 | -3.0306 | -47.977798 | 2024-11-16 00:47:00 | METOP-C | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26734d84-d7b6-313e-a669-7aa611719cbb | -2.1798 | -47.955601 | 2024-11-16 00:47:00 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6d00500-93a1-3f97-8e80-9f8bb95e4dfd | -2.6616 | -46.837399 | 2024-11-16 00:47:00 | METOP-C | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20ea8d8e-7b56-3424-9c9b-252bcfef44a2 | -2.0941 | -50.2188 | 2024-11-16 00:47:00 | METOP-C | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 057c5334-d189-3de2-b3d0-5b1c09ab24a4 | -5.9438 | -44.467499 | 2024-11-16 00:47:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f384e544-f4a9-3b35-af54-6fb650cb259c | -4.1506 | -50.772598 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b5084ee1-639f-3f05-bfce-109747c25e24 | -3.7368 | -50.183498 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc730575-8016-3d43-8b23-873b7d8202ae | -2.141 | -53.7127 | 2024-11-16 00:47:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed0bb653-af8f-3207-92a5-d0be079f0de2 | -4.2331 | -50.682499 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 45adc3eb-2db9-3503-8f1a-86bb6dd00124 | -4.7169 | -50.588402 | 2024-11-16 00:47:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e82b77b-154a-3e1e-bad4-633e97845c4f | -17.560499 | -57.527401 | 2024-11-16 00:47:00 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 86c53766-a6cc-36c9-97e3-5b3f1e81052b | -2.7804 | -48.588799 | 2024-11-16 00:47:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e272e6df-215c-3d2d-ae80-784a38527ace | -3.7466 | -50.181301 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 27b7e103-31bd-3e5c-b1a4-4a7ad4884d58 | -4.2165 | -47.225399 | 2024-11-16 00:47:00 | METOP-C | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| aa44cd84-1497-3bc9-b506-c12a78c20f9d | -0.9657 | -46.9412 | 2024-11-16 00:47:00 | METOP-C | TRACUATEUA | PARÁ | Brasil | 1508035 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a6bf300-45ee-3bd6-a023-43a257503e2c | -3.7605 | -50.781101 | 2024-11-16 00:47:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8fc08d0b-fab1-35a9-b56c-61a5ca0d81cd | -8.286 | -45.970501 | 2024-11-16 00:47:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README7.md)
