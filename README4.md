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
| 062ad098-c982-3b8c-be9b-9abd6e3c374d | -6.5326 | -55.157001 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 437f713b-c479-34a8-9d38-db0d82efd3a8 | -11.1992 | -54.896599 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eeee0478-f708-3775-bde3-98b0da0f70e9 | -6.5407 | -55.1474 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ddb19e41-f092-397b-93e5-6619f6e4bcb0 | -12.5929 | -46.929798 | 2026-08-05 01:13:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f2643c24-8b12-3dfa-b75c-16726aa8a97e | -2.8753 | -50.479099 | 2026-08-05 01:13:00 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba8d6682-a75e-3f8d-9ef8-b6716bd60a3a | -15.0876 | -49.505901 | 2026-08-05 01:13:00 | METOP-C | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 34637191-8b3e-37a7-9368-1dacaa0ad4da | -11.2317 | -54.858898 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 84bf3376-6d9b-356d-ad9c-16eb8a62f560 | -14.1841 | -54.413399 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00752196-3400-30c4-9261-2f9df4e969fe | -6.5493 | -55.184399 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6fba380c-82e3-3360-b755-6961e621bcb3 | -11.1714 | -54.9105 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b1533e28-a96b-39d5-bce5-aa6341fc1b88 | -11.2138 | -54.915699 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a481886b-a776-3698-9feb-6aeb1fc13142 | -6.5638 | -55.1577 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3e4b5dd-cf97-3865-89d1-72f7c4104f4a | -14.1373 | -55.252201 | 2026-08-05 01:13:00 | METOP-C | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f9fdf552-eafb-3abd-871f-7ca232eff28b | -11.1746 | -54.8797 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dc30cc82-b6d5-38cc-a420-003b5cfc57ee | -6.5557 | -55.167301 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa604c23-046e-39a6-bc77-c54d98433ddc | -11.2333 | -54.866001 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 61edbe2a-b3b2-3157-bbff-99643b78fefa | -11.9254 | -55.910599 | 2026-08-05 01:13:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a820f27d-4528-3af1-874a-247537e45fe5 | -12.5978 | -46.948502 | 2026-08-05 01:13:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| da91c32c-9094-369b-b0af-86f8fe5c54bf | -11.1861 | -54.929699 | 2026-08-05 01:13:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ac9051ce-18fb-39ad-bb51-14bfe251c896 | -11.1779 | -54.894001 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8dbdbe88-99e5-3f24-b0b4-41e534f98b86 | -6.5522 | -55.1525 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dbbdc46a-cf9d-308c-a020-672d72255219 | -11.1894 | -54.898899 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fea104bd-f8d0-37f1-980a-6c2f4d2bb510 | -11.2203 | -54.899101 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc37611e-655a-3dc1-8e12-6dd555ad759e | -12.5881 | -46.951099 | 2026-08-05 01:13:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 80cdb3e8-1efd-3da1-a816-0322394894c0 | -11.222 | -54.9063 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65d193c2-99c9-322b-bf66-cb4eec9ba292 | -11.1943 | -54.9203 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0067fcb3-212e-3cd1-9ab5-99c4709e5d92 | -11.1975 | -54.8894 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c7470e84-a131-3845-9911-2375ed429d12 | -11.2252 | -54.920502 | 2026-08-05 01:13:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8246c9fc-62ff-3c71-b0df-fc200374398b | -14.2021 | -54.4468 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 862dcf2a-c88e-319b-9dde-d447d9978eed | -11.1747 | -54.924801 | 2026-08-05 01:13:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 89561c66-1d3e-35a3-be0c-92fb56ac4bed | -11.1828 | -54.8703 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 8946edc9-756a-32fe-8ef6-150fa741e0f0 | -11.1763 | -54.886902 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 87cebd06-f36e-3979-8c8e-046b376f5ff5 | -11.2122 | -54.9086 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9092c159-6ad6-3fce-9f2d-948ee98ccc11 | -14.171 | -54.401402 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 21a86e05-3ebc-3f3f-85c0-da84461b5427 | -6.5718 | -55.147999 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 339dd85e-1503-379c-bd76-0eef77d90e30 | -11.1681 | -54.896198 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 03005317-4fe2-3f1a-bdc8-8d455a5c11b3 | -6.5574 | -55.174702 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f40a083d-2d68-3717-b327-a67dfdbf8efc | -11.2071 | -54.8419 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ee61be0c-1461-3b0c-b210-c43e62bb15f1 | -3.6719 | -49.477798 | 2026-08-05 01:13:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7bf79dfc-97da-3fc1-acd0-1bfe2b80aacb | -14.1612 | -54.403702 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b0a94092-c3d8-3e40-9cd9-3dd429c286d7 | -11.1877 | -54.891701 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0a5167f4-5f52-3b82-90e5-1bf0818941f4 | -12.6074 | -46.9459 | 2026-08-05 01:13:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 39d4b472-2266-3d68-9dd5-82fe65a3694f | -6.722 | -58.927399 | 2026-08-05 01:13:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a4518aa7-78b0-3ab9-9b59-39d4e1d5f877 | -11.2236 | -54.913399 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb260f82-57d4-30cc-b282-ff1cca34a1a1 | -9.6133 | -47.779202 | 2026-08-05 01:13:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e58be0a5-161b-3c15-8444-26c4fa26a4c2 | -9.1521 | -49.673698 | 2026-08-05 01:13:00 | METOP-C | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b3c779c-3354-307c-a4e2-633c972abe29 | -12.2128 | -52.8689 | 2026-08-05 01:13:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 99a9090f-fae9-36de-a522-a31b9a6ad703 | -11.2089 | -54.894299 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82130a8d-0f1d-37c4-9cb7-db722e2e8898 | -14.1743 | -54.415699 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6fa300d5-1b48-3870-b52c-a7751e0a8b81 | -14.1988 | -54.432499 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 4d2c3ada-6aec-3f12-a5fd-2ef61fa2f642 | -6.6486 | -56.420399 | 2026-08-05 01:13:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52b9dc43-ac61-3d41-880f-2c77b324ce4a | -6.554 | -55.159901 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65c43ea0-994d-387b-988e-220efd93d1f9 | -8.3508 | -45.993999 | 2026-08-05 01:13:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 36c7a195-e49a-300e-a3b6-f4d5940fbd1d | -11.1796 | -54.901199 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2f6bb1fb-3a89-38be-b92d-86c951df4e5f | -8.3604 | -45.991501 | 2026-08-05 01:13:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f8d615a3-9b6a-32d1-8805-e6d916d58d22 | -12.2147 | -52.877102 | 2026-08-05 01:13:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 65f810dc-def1-34d2-89d7-cc6dfb91776a | -11.2057 | -54.925098 | 2026-08-05 01:13:00 | METOP-C | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2257c4eb-328c-33f7-99ce-e7317541e903 | -11.1927 | -54.9132 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 112fd5d6-8ac2-391d-ac6f-ec71ed14d612 | -14.1857 | -54.420502 | 2026-08-05 01:13:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d182fec9-2673-37a2-af14-4e6f6e6c4705 | -12.203 | -52.8713 | 2026-08-05 01:13:00 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 85cc1edf-501e-30f6-bba8-271335d61d59 | -20.392 | -49.313202 | 2026-08-05 01:13:00 | METOP-C | NOVA GRANADA | SÃO PAULO | Brasil | 3533007 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d6f8d13b-0dca-345f-af17-c60293b6659a | -11.1829 | -54.915501 | 2026-08-05 01:13:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a1eddcfd-18b2-3897-b5d0-9fe72e211a39 | -6.5505 | -55.1451 | 2026-08-05 01:13:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb2247dd-c5cc-3066-84cc-8f7ab77ec6bd | -12.6025 | -46.9272 | 2026-08-05 01:13:00 | METOP-C | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 493b433f-a17c-3c24-a815-a33f77e35e24 | -11.19 | -54.89 | 2026-08-05 01:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 39a140db-dcd3-3336-a314-1d1e8f297071 | -11.16 | -54.94 | 2026-08-05 01:15:00 | MSG-03 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4d25f6ad-a82e-3d95-a2af-64865060de2f | -11.16 | -54.88 | 2026-08-05 01:15:00 | MSG-03 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1f80ad80-b5ec-395d-a68a-52e0fbaec3ac | -11.19 | -54.95 | 2026-08-05 01:15:00 | MSG-03 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 33c5a01a-4078-3682-98b8-f4e1e5ab853b | -12.5947 | -46.9301 | 2026-08-05 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.8 |
| be697b6f-568b-37b4-aa08-f8f1e355a0e7 | -6.5514 | -55.1569 | 2026-08-05 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 4056be8a-31f0-3b9e-9a1b-9dbdd7ec9694 | -12.4386 | -50.5109 | 2026-08-05 01:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 817b0e77-7098-33be-9c58-c537fabf0514 | -12.5754 | -46.9329 | 2026-08-05 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 4517670f-d503-37af-964d-50fe1b4a379c | -12.5942 | -46.9527 | 2026-08-05 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 888abb8c-f67d-33bd-82c3-074e2d180704 | -12.575 | -46.9555 | 2026-08-05 01:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 07d722ef-38cf-3dfa-987a-5983d39d4714 | -6.5514 | -55.1569 | 2026-08-05 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 4f9fd3fb-96ab-3c59-83e5-4e8d512991c1 | -12.5947 | -46.9301 | 2026-08-05 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 136.8 |
| d461cec8-2179-36b3-a6ac-d5b6d2d1e79e | -12.4386 | -50.5109 | 2026-08-05 01:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| d0f2ba2e-70c2-39f1-ac76-f3faa5f9708d | -12.5942 | -46.9527 | 2026-08-05 01:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 137.4 |
| 53887fec-9861-3486-990b-d96e64ecd4a9 | -12.4386 | -50.5109 | 2026-08-05 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 979acff2-a25f-39ad-a8f6-03d732ef6623 | -12.5754 | -46.9329 | 2026-08-05 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 4b639d30-e046-31a1-a984-7eda4bc10494 | -6.5514 | -55.1569 | 2026-08-05 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 88d3d646-8777-316a-9369-f1323d1a3aed | -12.5942 | -46.9527 | 2026-08-05 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| cadc0544-aca3-352b-a572-06865fab0bae | -12.5947 | -46.9301 | 2026-08-05 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 145.6 |
| 2da81bfd-60bf-3502-a12f-caae271072bf | -12.4383 | -50.5324 | 2026-08-05 01:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 9fa3543a-bfb6-35fb-8173-291174359419 | -12.575 | -46.9555 | 2026-08-05 01:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 255f69a8-7dca-3155-a2e0-eb8ba8fd2b0d | -12.4386 | -50.5109 | 2026-08-05 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 131.2 |
| 6c1ae200-c474-3500-8eeb-6a91e5b8ab5f | -12.5947 | -46.9301 | 2026-08-05 01:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 91b74591-14c8-37be-8bd9-f8f02e20ecac | -6.5514 | -55.1569 | 2026-08-05 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 5a18b51b-86db-3e1e-a86c-51bfe1e8eb3f | -12.4383 | -50.5324 | 2026-08-05 01:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| aa210229-ab74-3e1a-816f-4abdc3188189 | -12.4386 | -50.5109 | 2026-08-05 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.3 |
| 6e677b95-5ee9-30f3-bb0f-0e8a71895639 | -12.5942 | -46.9527 | 2026-08-05 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 44ad5af9-15c8-3dba-a865-25f105589c78 | -12.5947 | -46.9301 | 2026-08-05 02:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 131c15f2-c0e2-3d31-a995-9d5359077f30 | -12.4383 | -50.5324 | 2026-08-05 02:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 27d2d0ef-f6b6-3ff1-ab58-fee8ca794283 | -6.5514 | -55.1569 | 2026-08-05 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 95f00862-4030-3fce-9c9c-aae3d9faa2ae | -12.4386 | -50.5109 | 2026-08-05 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 7c151eba-3063-3a29-a995-4fb2413fe8fd | -6.5514 | -55.1569 | 2026-08-05 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 140e2129-9d6c-3f6b-bb95-f05695e811b9 | -7.5068 | -49.7394 | 2026-08-05 02:10:00 | GOES-19 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 43.3 |
| a417a776-0ef3-3246-9a18-9d928638d4f6 | -12.5947 | -46.9301 | 2026-08-05 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 155bda6d-87c5-3022-b194-b286be593038 | -12.4383 | -50.5324 | 2026-08-05 02:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 3384d933-4c91-39b8-96ee-9fc349fbc0eb | -12.5942 | -46.9527 | 2026-08-05 02:10:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |


[Clique aqui para ver as próximas entradas](README5.md)
