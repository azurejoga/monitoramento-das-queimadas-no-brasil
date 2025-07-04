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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b67d045d-9e27-3f79-a963-aaceeae83e4a | -9.51264 | -65.58743 | 2025-07-04 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c4a0904f-a54d-3a8f-8720-5ddaf8ad56ce | -10.30546 | -57.13441 | 2025-07-04 05:57:00 | NPP-375D | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 429d6b95-af38-30d4-9776-c5d2b7ece574 | -9.63797 | -63.50618 | 2025-07-04 05:57:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 31e82039-7942-3f95-8bb5-1e3544437d06 | -9.84389 | -68.34473 | 2025-07-04 05:57:00 | NPP-375D | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1fe9dfb2-b086-3a21-9c9a-31b5e699da61 | -6.6112 | -43.8941 | 2025-07-04 06:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 52.0 |
| c3e1848c-60e6-351e-87e9-849d3ddaa154 | -6.6112 | -43.8941 | 2025-07-04 06:10:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| ea461d5e-703c-3745-ae43-aadbd5bfc003 | -6.6112 | -43.8941 | 2025-07-04 06:20:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 6882ed6d-9c3e-3e07-8647-7de3eaa1f05f | -9.51037 | -65.58672 | 2025-07-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0bc66d9-acd9-3fa1-a4f3-312f75688588 | -9.51603 | -65.58741 | 2025-07-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2adfc89f-3818-397a-89f1-ae8491ac0c2b | -9.58352 | -68.56837 | 2025-07-04 06:20:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0612bb7f-7009-3a22-92fb-97e1e697d2d9 | -9.52727 | -63.57253 | 2025-07-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e78b45c2-b18b-36a7-854e-e1e45b3c6381 | -9.5266 | -63.57794 | 2025-07-04 06:20:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9438de36-3391-3291-9fcb-8b4b46234973 | -6.6112 | -43.8941 | 2025-07-04 06:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 48.6 |
| 3ccd4c00-dd38-327d-bbe5-0641a2e76afa | -9.63284 | -61.46489 | 2025-07-04 06:44:00 | AQUA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| adf6a34c-51de-3408-9b05-d61f00ddb098 | -8.52745 | -54.76604 | 2025-07-04 06:44:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8394bc8a-af9d-3e5c-aec5-1a2bd82d7891 | -9.52286 | -63.56689 | 2025-07-04 06:44:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6b684b03-180f-354a-9074-45cb0c5e9fce | -6.6112 | -43.8941 | 2025-07-04 06:50:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 0d790e2d-b88a-314e-b761-6bba1a8f4f75 | -19.129 | -46.9385 | 2025-07-04 07:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 138.0 |
| 975c12b9-57c6-32b1-9f17-6c6645482841 | -19.1284 | -46.962 | 2025-07-04 07:40:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 5cc2317a-e462-3c6a-b041-5e9c59211db0 | -19.129 | -46.9385 | 2025-07-04 07:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 110.1 |
| d95e7768-55ef-3288-8cec-9a65b40ef70d | -19.1284 | -46.962 | 2025-07-04 07:50:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 844a3c99-dbe6-36a2-91c8-8ac8a2465ad6 | -19.129 | -46.9385 | 2025-07-04 08:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 62.4 |
| f4539546-a837-38dc-b6ab-050e83ad0161 | -19.1284 | -46.962 | 2025-07-04 08:00:00 | GOES-19 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 55.0 |
| f577c815-e204-3ff1-b7ae-f6b6b1aafb78 | -12.427 | -50.0387 | 2025-07-04 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 136.6 |
| 32b2e9c0-a069-3b01-856f-00822314f2a4 | -12.4274 | -50.0171 | 2025-07-04 11:40:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 4c876133-e6fe-3dd2-a4c4-8bef6309ffc7 | -12.427 | -50.0387 | 2025-07-04 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 238.2 |
| b0129356-a3c1-3c8a-920d-3a47e8cdbc95 | -12.4274 | -50.0171 | 2025-07-04 11:50:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 3ba7cf32-3361-3fe1-83b5-efad3c338047 | -12.4274 | -50.0171 | 2025-07-04 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 282.7 |
| e48189ac-f0fa-3b32-9777-534e06886bc0 | -12.427 | -50.0387 | 2025-07-04 12:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 342.1 |
| 0790c4b3-38c5-3158-9160-7c8da7f51420 | -12.427 | -50.0387 | 2025-07-04 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 299.2 |
| 7c5dd7dd-c703-3b0a-9c46-0699c53ded33 | -12.4274 | -50.0171 | 2025-07-04 12:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 235.5 |
| 83b875ed-1889-3c6c-b7a2-2b5d49411a8f | -12.427 | -50.0387 | 2025-07-04 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 419.9 |
| f6d56fa1-aafc-333a-8235-b03ace2d6afa | -12.4274 | -50.0171 | 2025-07-04 12:20:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 332.1 |
| 2f8af74b-21af-3e14-9f86-11ef5c478939 | -5.75237 | -46.07816 | 2025-07-04 12:27:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| dd11a859-a165-302b-9953-b7be0e91bb02 | -6.88517 | -43.2393 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 25.8 |
| 3d4fc2af-750b-38a9-b08c-6438bbde3264 | -5.14197 | -45.1685 | 2025-07-04 12:27:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 47cb0079-885f-3abe-b44a-965aa74ae35f | -6.00727 | -44.52551 | 2025-07-04 12:27:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 32.8 |
| 855f7b26-7a14-3f12-ba1b-b32375c24e81 | -5.89886 | -45.16356 | 2025-07-04 12:27:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 6dcd6a1d-3881-3558-9f20-b0de3bdbea7a | -6.74362 | -43.1785 | 2025-07-04 12:27:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 10.8 |
| f73aa732-930e-3897-bdfc-6e2d23855bd5 | -5.97728 | -43.76764 | 2025-07-04 12:27:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 18.7 |
| fec502f3-fa72-374a-9752-4569009c9f9f | -5.69461 | -43.65944 | 2025-07-04 12:27:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 27.1 |
| 468f0068-5728-343f-9549-315cc191d72c | -5.75104 | -46.08762 | 2025-07-04 12:27:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.3 |
| 4aa78727-1dbe-3907-bab8-e7702313eca6 | -5.9003 | -45.15318 | 2025-07-04 12:27:00 | TERRA_M-T | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 16f34097-49d4-3ca3-8ac7-4da20c670e87 | -7.41086 | -45.40967 | 2025-07-04 12:27:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f4e9e126-3b6b-3830-b08e-2b0596ad2a4a | -6.82943 | -47.83958 | 2025-07-04 12:27:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 7b6e8a6d-ed07-3cd6-8fd5-d088cb8be1f2 | -7.00249 | -43.54708 | 2025-07-04 12:27:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 2f75eabc-c010-3be9-a4c4-28d0d5f1bfd5 | -7.39028 | -45.41758 | 2025-07-04 12:27:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 7587580a-dc28-372f-80c6-6fe8cd7f6dd3 | -5.14339 | -45.15826 | 2025-07-04 12:27:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1c616e21-29ea-337a-82d7-ed4029d81d49 | -7.00499 | -43.55387 | 2025-07-04 12:27:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7205b6be-7187-310d-898c-e2fa71ba778a | -6.6157 | -43.88314 | 2025-07-04 12:27:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 1a2caccd-e900-3aee-9d3c-51ba033f2093 | -6.01721 | -44.52686 | 2025-07-04 12:27:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 198.2 |
| 129e3f1e-15dd-35af-8fac-a5dc935d8a28 | -5.69833 | -43.66659 | 2025-07-04 12:27:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 54611e64-fa4a-3972-9db0-dae6245b4de3 | -5.29816 | -42.66407 | 2025-07-04 12:27:00 | TERRA_M-T | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b935e3bb-37e4-3bae-898a-7425ff27902a | -6.01878 | -44.51562 | 2025-07-04 12:27:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 17.3 |
| f6dc23b6-5f3c-38e7-8242-1fb9128c5356 | -6.99756 | -47.50005 | 2025-07-04 12:27:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 69d8e3c3-88aa-3d01-b7a6-2eb8157f9a37 | -4.54392 | -48.0161 | 2025-07-04 12:27:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| f3404c99-2093-3add-ae6d-4a8bce03a792 | -6.12143 | -42.52365 | 2025-07-04 12:27:00 | TERRA_M-T | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 18.0 |
| ee584b3e-d4d6-3950-bc36-dc11e616cad2 | -6.88708 | -43.22486 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 57.6 |
| 22962c20-2ca7-3186-9ce0-b3753c30e86c | -5.97902 | -43.75471 | 2025-07-04 12:27:00 | TERRA_M-T | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9b4b0c3c-c0b9-344e-b1d9-69696a20b5b2 | -3.01554 | -41.74769 | 2025-07-04 12:27:00 | TERRA_M-T | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 8acae5bc-118e-3d1d-93ff-981a7df4231f | -7.22573 | -43.09275 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 12.4 |
| 7f8aa4eb-e388-38b1-aad7-b62c44666d87 | -7.11462 | -47.84429 | 2025-07-04 12:27:00 | TERRA_M-T | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 69b79095-2b04-3fb8-b5d9-8062b77203d6 | -7.00679 | -43.54012 | 2025-07-04 12:27:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8ccd8db2-0ce5-3fcd-b956-dcc138f683b1 | -7.34547 | -44.83258 | 2025-07-04 12:27:00 | TERRA_M-T | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 24608024-7e47-3843-9878-14c08cffa60a | -6.37379 | -48.06508 | 2025-07-04 12:27:00 | TERRA_M-T | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab73e26c-c0b5-3bbe-9da0-2a30cf87e1b7 | -6.66181 | -47.59684 | 2025-07-04 12:27:00 | TERRA_M-T | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| a5751a13-514f-37d1-b738-cb8f7fe3b80a | -6.79149 | -45.05943 | 2025-07-04 12:27:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.2 |
| eba3d3bc-79c7-3b32-a92e-ed48e9686c31 | -4.81985 | -47.32231 | 2025-07-04 12:27:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a4cd2184-22bc-3b85-bc17-13f8c4b308f9 | -6.28742 | -43.67122 | 2025-07-04 12:27:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| f6c517e4-feb6-3590-a9f8-8b9b743dcf44 | -6.77665 | -45.54459 | 2025-07-04 12:27:00 | TERRA_M-T | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bbd3aed2-4d9d-3eb6-a127-27150ae58381 | -7.08278 | -43.21855 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| bab44d81-05fe-3556-aa14-8995cdd71f9d | -4.82111 | -47.31354 | 2025-07-04 12:27:00 | TERRA_M-T | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| edb42266-a7a8-33f3-b67a-007fffaf18db | -5.33018 | -44.96827 | 2025-07-04 12:27:00 | TERRA_M-T | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 29.0 |
| e19572c0-dd6f-3b91-ba14-d7da3ed399ad | -6.10446 | -49.587 | 2025-07-04 12:27:00 | TERRA_M-T | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 3658f71d-cdbe-38c7-a566-796ee17764ad | -6.88899 | -43.21036 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| a4386b15-6dde-3369-9b50-a75887984f00 | -6.61399 | -43.89588 | 2025-07-04 12:27:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3e4820c2-9af4-349e-8770-a68b2bf5dc12 | -6.27684 | -43.66945 | 2025-07-04 12:27:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| b4cfb2ac-c3ae-350c-9c97-782cc53b1779 | -5.91735 | -43.4472 | 2025-07-04 12:27:00 | TERRA_M-T | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| d590ca51-8862-3a1e-86d5-d6576cf85cbd | -6.8307 | -47.83077 | 2025-07-04 12:27:00 | TERRA_M-T | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 15.8 |
| 3c2bcdf9-9ba9-3931-a893-afbcb79ca426 | -6.27504 | -43.68282 | 2025-07-04 12:27:00 | TERRA_M-T | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 785927e6-ad39-3aa7-a4de-83579cc92d6b | -6.96131 | -42.83851 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 405c1139-825c-3a3e-86d5-9f5ae09b4cb4 | -4.54263 | -48.02497 | 2025-07-04 12:27:00 | TERRA_M-T | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 27a1c6f3-fea5-3cd5-9866-916bd22c951d | -6.60519 | -43.88173 | 2025-07-04 12:27:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 2255eb40-ad39-308f-a18c-852be1e7ed30 | -6.85109 | -42.80196 | 2025-07-04 12:27:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 17.9 |
| 324335f9-76d8-337a-8897-4fc213d81d54 | -7.0895 | -44.16984 | 2025-07-04 12:27:00 | TERRA_M-T | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 5a4600cd-678a-385b-9213-52e24af22c7c | -16.63268 | -47.79474 | 2025-07-04 12:29:00 | TERRA_M-T | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 68d7dada-40f1-3e37-ab41-dd1a51be1721 | -7.70987 | -50.58565 | 2025-07-04 12:29:00 | TERRA_M-T | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| b704c85a-2c73-3e93-9bd3-7816f3cdc4e7 | -7.73294 | -45.88606 | 2025-07-04 12:29:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 196724b3-3b27-3530-8530-4e1ed8ff04ec | -10.5569 | -49.12859 | 2025-07-04 12:29:00 | TERRA_M-T | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 7ec5701f-9646-3333-9fee-c3e45a15c53a | -13.43524 | -47.81224 | 2025-07-04 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7cfa75d9-b810-332b-bc5b-477f209f86c5 | -10.82428 | -54.02445 | 2025-07-04 12:29:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 07910d76-9422-3a88-a5d3-28ea19f734c5 | -8.3824 | -44.04862 | 2025-07-04 12:29:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 26.5 |
| 7f4cd314-96ee-33ce-8b86-918adf7c49ee | -16.94447 | -46.09336 | 2025-07-04 12:29:00 | TERRA_M-T | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 0a38a27f-ff1d-3ac7-8f0e-bfa77231495a | -13.40017 | -47.80099 | 2025-07-04 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 02ac9afb-8ae7-3055-a44b-4364dddcfd57 | -9.23498 | -47.01035 | 2025-07-04 12:29:00 | TERRA_M-T | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 8b938d30-d8dc-36f4-b6a6-c825c05f168d | -13.38714 | -47.82826 | 2025-07-04 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| c11af800-3eac-38ff-a191-03eab0513876 | -14.25193 | -47.03241 | 2025-07-04 12:29:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| cecc89a7-00b0-3156-b618-ae82dca3d4da | -8.38061 | -44.06187 | 2025-07-04 12:29:00 | TERRA_M-T | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 1615bd1b-cf78-33fe-9fd1-76f46dc9881d | -8.42994 | -46.96624 | 2025-07-04 12:29:00 | TERRA_M-T | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 21daf1a5-996a-305b-a879-41605266d233 | -13.40398 | -47.83994 | 2025-07-04 12:29:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README23.md)
