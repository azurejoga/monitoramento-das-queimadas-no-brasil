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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c389c043-b70d-3767-81d6-160440289c20 | -8.9137 | -47.349998 | 2025-07-14 00:31:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 371dfecf-09df-3348-86b1-c0c690e253e7 | -9.4887 | -47.5555 | 2025-07-14 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e6d20790-44ef-333b-8a49-b9759129d035 | -8.498 | -43.286999 | 2025-07-14 00:31:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e2317f18-7951-3a1a-a80c-155a66ad9165 | -10.5825 | -49.136902 | 2025-07-14 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| be9725a7-c025-3aa7-8b68-cf43a15acbb3 | -3.5814 | -47.533001 | 2025-07-14 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d6e6f0df-8a01-38c5-a917-85446e031ee2 | -3.9807 | -48.41 | 2025-07-14 00:31:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 242ea4ca-7638-3de0-aabb-9e9ba1c62cce | -10.5671 | -49.115299 | 2025-07-14 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 56416d51-4225-326d-bbfb-83b37dea53f6 | -7.2668 | -45.3004 | 2025-07-14 00:31:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6bc039ca-e919-3ac4-b8ee-27101945c86b | -8.503 | -43.306702 | 2025-07-14 00:31:00 | METOP-B | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 70aa9f80-afeb-3e7f-8113-cfc3cb1296b4 | -7.2607 | -45.317699 | 2025-07-14 00:31:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbdb57a5-cd36-3777-a83a-1f24fea1b7a7 | -3.5786 | -47.520901 | 2025-07-14 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0680a8f-ac1b-3448-9b66-19654cbed8ba | -4.2999 | -48.101101 | 2025-07-14 00:31:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29b567ff-68e2-3b30-be7e-86cc798afd96 | -21.493299 | -54.2617 | 2025-07-14 00:31:00 | METOP-B | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 30b215fb-059e-36b2-a503-97c81bbe9555 | -10.2766 | -47.613701 | 2025-07-14 00:31:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9a236224-0846-3839-b184-e579440df587 | -8.9039 | -47.352402 | 2025-07-14 00:31:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c35b485e-5030-30d5-a4b2-bc33b3a4ce5f | -8.9087 | -47.329102 | 2025-07-14 00:31:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e3a9a585-04c8-3f4a-a38a-2a7ae9ffb762 | -8.9014 | -47.3419 | 2025-07-14 00:31:00 | METOP-B | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4e079da8-a393-36d4-ade4-5a34c6067c87 | -3.5856 | -47.506599 | 2025-07-14 00:31:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2d9ca27-8d7c-3ffd-85c1-2ec2fbcf761a | -21.499901 | -47.263599 | 2025-07-14 00:31:00 | METOP-B | TAMBAÚ | SÃO PAULO | Brasil | 3553302 | 35 | 33 | nan | nan | nan | Cerrado | nan |
| 74c09b9a-1585-3c37-a1e8-e8846be202f7 | -4.2422 | -46.624599 | 2025-07-14 00:31:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b427633f-c17c-3c1f-a38f-cbdc04890bbd | -10.2863 | -47.611301 | 2025-07-14 00:31:00 | METOP-B | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9fcea122-fb86-3b0f-a0e8-2397e194262e | -9.4911 | -47.565399 | 2025-07-14 00:31:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| cf22fac8-5a09-3b94-a415-085e63c1a47e | -7.2465 | -46.9725 | 2025-07-14 00:31:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e95731a5-72eb-3bc7-a365-b3be0266f163 | -7.2437 | -46.960899 | 2025-07-14 00:31:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 73b460fd-8b54-37ad-b24f-6a0268593225 | -10.569 | -49.123299 | 2025-07-14 00:31:00 | METOP-B | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d049c56-72f9-3b4a-a412-6f222d6fa5d7 | -5.2753 | -44.882401 | 2025-07-14 00:31:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2b6d610c-cc55-3a26-b1dc-b736ed376221 | -14.5098 | -58.580101 | 2025-07-14 00:31:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 46f1dccf-54e2-380d-82bb-7bc28cde41ea | -3.5809 | -47.5367 | 2025-07-14 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 50.2 |
| a18649b8-0ca6-36e7-81aa-81a00917bd3b | -8.5211 | -43.3063 | 2025-07-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 84.6 |
| 6b57b03a-3bd2-3908-b71e-8d393b513f43 | -10.2773 | -47.611 | 2025-07-14 00:40:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 486f44b3-3e81-3d91-a838-d023c84bbda1 | -3.581 | -47.5149 | 2025-07-14 00:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 0435f813-f68e-3bf7-8904-6e75577f837a | -8.5022 | -43.3085 | 2025-07-14 00:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.6 |
| 7312ed31-ff62-31de-b3e4-4cbf2cfc5cae | -3.5809 | -47.5367 | 2025-07-14 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 3139f354-08e6-35f4-9415-bc21eeddc6ae | -4.301 | -48.1133 | 2025-07-14 00:50:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 7489d886-448f-323f-a48b-ec850b3ba673 | -8.5211 | -43.3063 | 2025-07-14 00:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1d1da6b4-d504-3c7f-9481-40f41e2fa3e6 | -3.581 | -47.5149 | 2025-07-14 00:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| babbe170-a3a5-3cb3-9ba0-33737f116a0c | -10.2773 | -47.611 | 2025-07-14 00:50:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 2dd45070-0c8f-3ba4-a2e3-7374420221a8 | -8.5211 | -43.3063 | 2025-07-14 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 52dd87de-a6e1-3ffc-b37e-28d0b84fa469 | -9.361 | -40.4273 | 2025-07-14 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.3 |
| 15d8f9d4-9704-3666-81f8-c6b422531a78 | -3.581 | -47.5149 | 2025-07-14 01:00:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 53.9 |
| fe27cb05-9768-369b-a695-230877835d17 | -9.3614 | -40.4025 | 2025-07-14 01:00:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 65.1 |
| 0df3796b-8e3a-3d2c-9cb2-6b6fef95c7c2 | -10.2773 | -47.611 | 2025-07-14 01:00:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| cf940409-8aa7-3695-bcb9-b42752f1a73f | -3.581 | -47.5149 | 2025-07-14 01:10:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e8e9384e-5544-36d6-b7e5-8ab82d4e80bc | -8.5211 | -43.3063 | 2025-07-14 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 34a3665f-d623-3443-9f69-87e80ec3a450 | -10.2773 | -47.611 | 2025-07-14 01:10:00 | GOES-19 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 50.9 |
| 3d9f334c-44ee-37e4-81a1-53fa895bd6e8 | -8.5211 | -43.3063 | 2025-07-14 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 52577e32-b644-3ca8-bad1-c52506398805 | -3.581 | -47.5149 | 2025-07-14 01:20:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 174637c8-bf4a-3b87-aedb-c0ef8fb0932d | -20.146999 | -50.717899 | 2025-07-14 01:21:00 | METOP-C | ASPÁSIA | SÃO PAULO | Brasil | 3503950 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 32154f33-937f-315a-a196-d63d01e5e233 | -3.5915 | -47.512699 | 2025-07-14 01:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e2bed57-c714-35c3-8236-ae3a01d6d1d5 | -3.5819 | -47.515099 | 2025-07-14 01:21:00 | METOP-C | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1b0ea56-7f57-3bab-939a-1af5379d3561 | -10.2748 | -60.546398 | 2025-07-14 01:21:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e0ef9e96-6349-371e-b302-d2da1d5753f2 | -14.5026 | -58.592999 | 2025-07-14 01:21:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8a59300b-40cc-3639-b9da-b0e4b927fc44 | -9.0236 | -59.544899 | 2025-07-14 01:21:00 | METOP-C | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 017ab44f-5918-38f7-ab29-574fe4627d6c | -21.495701 | -54.273201 | 2025-07-14 01:21:00 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ff9f545f-ac21-3b5b-a450-898767748a64 | -11.8726 | -58.7034 | 2025-07-14 01:21:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a1556d44-af3b-37e6-a517-f037306881bb | -7.6326 | -56.758999 | 2025-07-14 01:21:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22fca2f5-5d51-3e92-ac45-cd3079ef2ccd | -9.4768 | -57.323002 | 2025-07-14 01:21:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7b2da7-61c1-34ce-844e-de2a3ef2eea0 | -10.2799 | -47.608501 | 2025-07-14 01:21:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1453a760-5639-3f56-a9eb-7fc3401e6da6 | -21.493999 | -54.265701 | 2025-07-14 01:21:00 | METOP-C | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 993095de-8744-386a-b50d-92d15c50f9ba | -14.5042 | -58.6003 | 2025-07-14 01:21:00 | METOP-C | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| fe23161a-7a5f-3342-9da4-3ebb5e5c5674 | -10.0576 | -59.105301 | 2025-07-14 01:21:00 | METOP-C | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bb65e4e4-575e-307a-8d96-bee348f21383 | -9.3585 | -58.836899 | 2025-07-14 01:21:00 | METOP-C | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93b05c4e-c007-3801-9ea5-c30958e626ea | -8.9163 | -47.3512 | 2025-07-14 01:21:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ac9d88bf-9e47-3fdb-abeb-c143335931b7 | -10.2895 | -47.6059 | 2025-07-14 01:21:00 | METOP-C | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1e0df190-ad92-3915-8ec0-ecb3f36ab1c3 | -8.5211 | -43.3063 | 2025-07-14 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 0c389405-d972-371e-97d5-a495921a1641 | -8.5211 | -43.3063 | 2025-07-14 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 90.3 |
| 32c22923-773f-3844-b7ae-103695a13f70 | -14.49647 | -58.60448 | 2025-07-14 01:41:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b98cc9e0-a8e1-39c7-bc2b-e3fce5568066 | -8.5022 | -43.3085 | 2025-07-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| e2e4d9b5-c96a-3ae3-9230-315526e04626 | -9.3805 | -40.3998 | 2025-07-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 205.8 |
| 083901ed-6c66-3090-b7a4-df0604dbfb67 | -6.1112 | -47.2897 | 2025-07-14 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 100.9 |
| 37cd5c6a-2bdb-3952-9737-54d8e3e1b892 | -6.1299 | -47.2884 | 2025-07-14 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 02d926b5-e194-3616-b2c5-b82984a7977f | -9.3614 | -40.4025 | 2025-07-14 01:50:00 | GOES-19 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 192.8 |
| da0f5d0e-91cd-3038-887d-8dbe9cf0e2b0 | -6.111 | -47.3116 | 2025-07-14 01:50:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 50.5 |
| a088b5a2-ba2f-3e6c-bf29-1e772b2be412 | -8.5211 | -43.3063 | 2025-07-14 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.6 |
| 9d2b85ca-261d-3c1d-b97e-98788a6305a4 | -9.3801 | -40.4246 | 2025-07-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 188.6 |
| e027e93c-8148-365c-bb81-3e2b9df5272b | -7.272 | -45.3019 | 2025-07-14 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 91b766f5-7862-3d88-bea9-096e87a818e2 | -7.2718 | -45.3246 | 2025-07-14 01:50:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f71b0694-2087-3e56-a52b-17a41970f7a6 | -9.361 | -40.4273 | 2025-07-14 01:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 172.7 |
| 38308ede-9dea-3ea0-a7fd-2e3d49de5734 | -8.5211 | -43.3063 | 2025-07-14 02:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 71.4 |
| f4d58c6f-bfff-38ea-95c3-897c223e3284 | -8.5211 | -43.3063 | 2025-07-14 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 72.1 |
| 13e65c77-e7fc-3dd7-9972-5563f17b107d | -8.5211 | -43.3063 | 2025-07-14 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 1f165b0d-1ca3-3d55-8358-2e21d78cca48 | -8.5211 | -43.3063 | 2025-07-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 71.7 |
| 98071f38-d8ec-3064-b100-eee72f4fefd7 | -8.5022 | -43.3085 | 2025-07-14 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 7d05b08e-51ea-394a-928c-6194b903bc11 | -4.301 | -48.1133 | 2025-07-14 02:30:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 2898c192-1d83-3a36-9389-fb6ebfb31cf8 | -8.5211 | -43.3063 | 2025-07-14 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 7a997fa9-81cc-32b1-8faf-4afe845485d2 | -8.5211 | -43.3063 | 2025-07-14 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 67.3 |
| ba07df08-3d39-3b99-b324-55b966b12ba7 | -8.5022 | -43.3085 | 2025-07-14 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 54.5 |
| 7f27f4d3-f32e-30d5-b739-8108e439b021 | -8.5022 | -43.3085 | 2025-07-14 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 49.5 |
| 1231a86f-b2d6-382c-8998-5afb53109391 | -8.5211 | -43.3063 | 2025-07-14 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 015c8c5e-9d0a-38cf-956e-4c942f3045fd | -8.5022 | -43.3085 | 2025-07-14 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 51.1 |
| 5aeff22c-4e27-311a-832e-68acf0de0124 | -8.5211 | -43.3063 | 2025-07-14 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 76.6 |
| ec79a267-6370-3694-ab57-5016c05f9e76 | -4.51792 | -38.54954 | 2025-07-14 03:10:00 | NOAA-20 | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 5.9 |
| a145c639-3f03-3b92-a362-5563124b248a | -5.15339 | -37.68623 | 2025-07-14 03:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f9cb6f07-9ce3-3d7b-84ad-98a36940dc2b | -9.45153 | -40.37987 | 2025-07-14 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 6df7cde6-eeb1-3abe-9db1-e5b7362f31c2 | -5.15266 | -37.68419 | 2025-07-14 03:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 467e8128-5d04-3d8f-9b8f-ff6e75ed648a | -5.1585 | -37.68522 | 2025-07-14 03:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6297f61c-ff4b-3676-a21d-bfd334d9242a | -9.45794 | -40.38118 | 2025-07-14 03:10:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 586485da-81a5-3723-9a90-39f437c01320 | -5.15775 | -37.68939 | 2025-07-14 03:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 748faa79-756c-3e56-8857-0be593e33d67 | -5.15191 | -37.68837 | 2025-07-14 03:10:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.7 |
| b1e96505-9395-31c7-bc61-c9ce274f4c80 | -8.24641 | -41.93401 | 2025-07-14 03:10:00 | NOAA-20 | NOVA SANTA RITA | PIAUÍ | Brasil | 2207959 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |


[Clique aqui para ver as próximas entradas](README3.md)
