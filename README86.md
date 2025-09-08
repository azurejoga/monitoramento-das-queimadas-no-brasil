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

## Dados Diários - Página 86

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c536bfc8-598a-35e2-9a40-3e570817c310 | -7.82986 | -45.42099 | 2025-09-08 05:21:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 15c36a57-a092-3a9f-8cf7-1a30d89e4989 | -9.34672 | -63.8176 | 2025-09-08 05:21:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10c1a68c-b937-38a7-88b0-d42972bed9d0 | -12.94642 | -54.764 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8034f217-79da-3bac-a3e2-d23ae5dce34e | -9.20599 | -46.0513 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a369c31-71cd-3dda-9ef0-98fe8d3a0580 | -10.14634 | -46.20367 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 137fd071-ac5e-38b3-9768-a5ebe85f65cb | -6.2798 | -53.42628 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc3570c0-5a46-3e9d-9671-efdfa055132d | -6.95172 | -62.93975 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 273ba954-241e-30a2-9ea4-b049e3ade4d5 | -9.17056 | -59.38377 | 2025-09-08 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 893fb726-4132-375c-a5df-54203efd813d | -7.93934 | -61.79923 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 55cb5832-b7e3-309b-aa2d-1063fe984674 | -9.08364 | -65.4277 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e7a3135f-71c9-30b8-a413-afa1b48cdd91 | -13.04195 | -47.14584 | 2025-09-08 05:21:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6241504-bee4-3861-ba0a-9653706a2fdd | -6.28454 | -53.42311 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 52b2359c-32ce-391b-a28b-84c9e659a7da | -12.81252 | -56.52007 | 2025-09-08 05:21:00 | NPP-375D | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c16d519-19b1-314b-923e-2c7da3772869 | -9.70683 | -57.79662 | 2025-09-08 05:21:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f439694e-23b8-3173-911c-c187ac62ef0e | -11.19933 | -55.00439 | 2025-09-08 05:21:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7354363c-0645-3b96-87b3-2e032e888f58 | -8.09561 | -54.75728 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e7f3ea3-8bca-3c99-9cc2-0c3a6600c006 | -11.35615 | -50.38442 | 2025-09-08 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 040513f9-b173-3bf2-8058-4f9c3f6e24e3 | -6.92001 | -62.94385 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 734e2523-aae4-38ca-9ee3-d3f6d0b09540 | -12.61877 | -56.98461 | 2025-09-08 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46fb5764-a9d0-351d-a52b-57516e2867f7 | -9.47459 | -60.48775 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4b333a41-79a6-3c3a-a697-42dcf103e9f4 | -6.54131 | -54.99251 | 2025-09-08 05:21:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae0d1737-5715-3f29-977e-e7e500253312 | -6.96454 | -62.93251 | 2025-09-08 05:21:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e5132ef-6728-310f-a3b4-5120ffca1fa3 | -7.39919 | -61.63818 | 2025-09-08 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81e45e71-c3cf-3f18-ad38-42aee0da3e7d | -9.48186 | -60.48529 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e6fe2abc-304b-3e86-856a-5e80e0a6fa55 | -9.12119 | -65.95877 | 2025-09-08 05:21:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| add74ca9-64a5-3378-bff2-6f019786c20d | -12.94535 | -54.77184 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a54d09c8-6f7c-3307-95f6-e2a29aff2fa1 | -11.19898 | -55.06479 | 2025-09-08 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffd1abdb-4084-3670-877e-7e81e240e6fb | -10.14926 | -46.21261 | 2025-09-08 05:21:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c81a02bc-6cce-3464-85f1-9e5214e7b81a | -12.19914 | -53.91785 | 2025-09-08 05:21:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3efdb897-9a35-3067-a7f1-9fe8a33fa8a1 | -8.18319 | -50.14515 | 2025-09-08 05:21:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eca0aa03-d3ef-3e23-9964-5e8752c0465a | -10.05045 | -59.35881 | 2025-09-08 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 391294b9-b974-3c45-aac2-80abaf259a6d | -6.83822 | -52.80123 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 51e97ba8-4a05-3a01-8d13-a8fa74bca40d | -6.82427 | -52.80482 | 2025-09-08 05:21:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6586482f-73c0-3f4f-925c-5c76ddda06a9 | -12.89023 | -47.99063 | 2025-09-08 05:21:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e35dee43-f9dc-3956-922c-376ff6bc42c6 | -13.81153 | -46.28792 | 2025-09-08 05:21:00 | NPP-375D | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6760be24-eb8f-3ea0-b60f-fe18e5a0b14e | -15.68458 | -53.55667 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddb12ed8-7db3-3eb8-9953-b81e49dae1bb | -16.34315 | -52.94024 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5581dfdd-e109-3847-a048-c0f220b682e8 | -15.25086 | -53.79794 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b1348810-6ee0-3222-8f47-c40aad637155 | -16.29296 | -49.55387 | 2025-09-08 05:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df336728-77b1-3ea9-a54b-e8c3a4069781 | -15.17936 | -47.95876 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7333a78a-5622-3996-844b-92d0737962b6 | -14.93176 | -55.88245 | 2025-09-08 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a98b660a-0e1b-3b19-abf8-b0f05d373fd2 | -15.76656 | -53.5635 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| da7d0861-dc3d-351c-8926-f454852a93c9 | -19.52098 | -47.88475 | 2025-09-08 05:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6f356b4-085c-30a3-a2c3-cdbda9e8b4f0 | -15.24722 | -52.36296 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9c502a63-e983-3fbc-b55d-0339223fc3a0 | -12.42053 | -63.89726 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3fe2d6ab-ea01-3eee-9d4b-68c7e9cd9e10 | -15.0778 | -50.11064 | 2025-09-08 05:23:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f388dc87-79f2-3e45-8617-24db666213d9 | -15.25217 | -53.81589 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b5ca37b-3c49-3273-ba83-23c0c3f47d3f | -12.41759 | -63.89216 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ff0598ef-8d59-31fb-81df-a18d3c5fdc79 | -11.89666 | -64.9843 | 2025-09-08 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 248c85f3-ab6c-32e2-b8d3-74742f2c6ba2 | -15.83366 | -52.28878 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 806006c7-78cc-328b-838f-b4a91109dca7 | -14.87747 | -55.82637 | 2025-09-08 05:23:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ec89487-7957-34fe-9017-d934af261a1f | -16.33389 | -52.93292 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f1bfc68-c143-39f4-b764-630143941f1f | -14.52235 | -48.7746 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a66fc9c2-316b-3f2c-923b-692ab9fb3daf | -15.84079 | -52.27288 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a95aa1bb-7a20-3bc9-a7b2-e27b9b6b4ad9 | -12.86901 | -62.10901 | 2025-09-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48509ef-8aca-304e-b54e-ddc2c3022f55 | -16.34384 | -52.93431 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ae9b37f1-4171-32d8-8107-58eb86c83609 | -16.30834 | -58.11749 | 2025-09-08 05:23:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 21be9ef2-46a4-3a65-b190-9785aa0ff959 | -15.25761 | -53.8186 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2210447-2e6c-389c-bb30-460993b35a22 | -14.51433 | -48.78932 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| abf34a98-5187-3632-b833-0d5efe365b45 | -16.33325 | -52.93847 | 2025-09-08 05:23:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a284b0e0-ff72-3b40-8f42-cc3d33951116 | -14.71391 | -60.25107 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33cba7c0-bd5c-393b-a39b-c2fa1a55608c | -15.66756 | -53.86888 | 2025-09-08 05:23:00 | NPP-375D | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 44518a28-45ad-3c1d-9cef-306b6c51358c | -14.50658 | -56.49099 | 2025-09-08 05:23:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 266f24a1-45d0-3802-9e93-f99aee34fbc4 | -14.71058 | -60.25051 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e9c5cc6-a0d9-3256-8abb-b0bd8b465f05 | -11.91123 | -64.97105 | 2025-09-08 05:23:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09a9b613-df4b-3de9-b62c-affa3ba7683e | -15.25549 | -53.79853 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2a0a952-82a2-3bf2-9372-7a1e4845fd33 | -15.25681 | -53.81643 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bf0a9c6e-cf07-3335-864d-6d98ebbab2ec | -13.39839 | -58.98454 | 2025-09-08 05:23:00 | NPP-375D | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 106ccb51-e104-3ebc-85c2-fdfacd72a435 | -15.25234 | -53.82295 | 2025-09-08 05:23:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0e00acf7-9ec2-3520-9f40-89190571de91 | -18.02813 | -47.11486 | 2025-09-08 05:23:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 6.7 |
| bac71c70-b105-38a9-b06c-9b6ac68aaf10 | -12.8718 | -62.11332 | 2025-09-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2f0cd241-1345-3ba0-bed2-57046e1eaee2 | -14.52124 | -48.78496 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed8101a6-9000-33bd-8dff-a7efb49081cc | -15.18806 | -47.95854 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 71e075b2-a66a-3c25-8fae-e3f035cbe0ec | -15.53239 | -56.32081 | 2025-09-08 05:23:00 | NPP-375D | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4423e2a6-7ca7-3066-a987-150207e8477c | -15.18622 | -47.97735 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bb09b4c4-f778-30e3-b455-a2b43a67031e | -14.52392 | -48.75996 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6d718483-121f-3a56-a1b0-fadc1f993773 | -14.5207 | -48.78992 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f44ebbde-f851-3405-a4b8-77e3b0ab23d4 | -14.68248 | -48.19324 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d6fcdcca-8cff-3cb2-85ae-1ba8ad5da108 | -15.83119 | -52.26525 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae9a70f8-1452-3481-8c52-0ba98176c60c | -15.83222 | -52.30092 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2587ccb-16c0-3ca5-b864-48f2d140147e | -19.53183 | -47.88408 | 2025-09-08 05:23:00 | NPP-375D | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c242cd36-c04b-39f3-8d25-c06d48e7138b | -14.79569 | -48.23502 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e3d66d5-13c3-3b4c-96f5-9eee9c6daf1e | -15.84699 | -52.30896 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fce014ab-a989-304f-abe4-1512f9db7a1c | -15.73564 | -53.58039 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0bff6668-08d4-3a01-924d-9c70dee73f8d | -16.28904 | -49.55006 | 2025-09-08 05:23:00 | NPP-375D | INHUMAS | GOIÁS | Brasil | 5210000 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7235d7f-cc84-3ceb-9584-ab073174102d | -12.87243 | -62.10959 | 2025-09-08 05:23:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13528a1f-e06f-3125-89f6-aa92cb8ffe6c | -17.58499 | -49.79778 | 2025-09-08 05:23:00 | NPP-375D | EDEALINA | GOIÁS | Brasil | 5207352 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaa226c6-e51e-3efe-8ff9-9ed1c597ee12 | -14.52443 | -48.75523 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 97cef387-5d82-378d-9c33-574adee878e1 | -15.68524 | -53.55138 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7cef84f8-4bf0-35df-b530-99be088c6672 | -12.41314 | -63.89594 | 2025-09-08 05:23:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 315656be-41ea-3828-912f-1d5971b45d26 | -15.74321 | -53.59717 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20da642c-dd1e-308a-ae6a-df70fa92692d | -15.74793 | -53.59787 | 2025-09-08 05:23:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7eb7c861-4bb2-34bc-a63f-9305b79386b4 | -15.82509 | -52.27248 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 766d893f-5c2a-3141-b80f-d7ce67d7f6bd | -15.24503 | -52.38169 | 2025-09-08 05:23:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 91eccfa3-bc4f-3a9a-8306-dcb51d4485a9 | -14.50641 | -48.80315 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| de3b4d1e-4a5f-35e3-96ba-70b077f912c2 | -14.35252 | -60.3143 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| adc8b9b1-15f7-38d2-962c-2d66b5528ad9 | -15.18608 | -47.95954 | 2025-09-08 05:23:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a762a705-ccf3-3935-bb1d-d7b096dbf730 | -14.80699 | -48.19082 | 2025-09-08 05:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0fd45b5a-72c6-3af4-9818-54b10c78adc0 | -13.89359 | -53.98542 | 2025-09-08 05:23:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f003461e-81d4-3d17-9219-c078166ab8d4 | -14.70724 | -60.24995 | 2025-09-08 05:23:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |


[Clique aqui para ver as próximas entradas](README87.md)
