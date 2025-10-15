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
| b6b01906-271b-3141-b8cc-2e6f234f0e01 | -3.0572 | -44.4605 | 2025-10-15 14:00:00 | GOES-19 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 15a54537-8005-3808-8539-66f70d04e7b9 | 1.3348 | -50.7461 | 2025-10-15 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 65.5 |
| df1d80b7-ffb4-301a-9bc0-bd8ff7588a2e | -4.6698 | -43.1092 | 2025-10-15 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 143.2 |
| 7b4981ba-025f-3b62-a32b-06971b1612d1 | -4.6696 | -43.1326 | 2025-10-15 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 199.0 |
| a498a066-8277-3a16-bb4b-eb6acf336fce | -10.8289 | -43.9482 | 2025-10-15 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 190.1 |
| 0097cb3f-8da6-31dd-bbf5-2d3b5981a61c | -11.4572 | -44.0909 | 2025-10-15 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 158.1 |
| faef7fa3-1390-34ee-9c3d-131a9ffdf24f | -5.2496 | -40.9731 | 2025-10-15 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 165.3 |
| e6244a08-5d57-304f-97c2-f4c79d1cd459 | -10.8285 | -43.9717 | 2025-10-15 14:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 137.1 |
| 6e489361-eadd-378a-b9aa-3ce1635e1e23 | -11.438 | -44.0938 | 2025-10-15 14:00:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| 2653cb1b-0889-33a5-9be9-508f78b2c43e | 1.3349 | -50.7253 | 2025-10-15 14:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 153a266b-18fb-3690-b09e-8f4096ad67d2 | -13.7305 | -42.3185 | 2025-10-15 14:00:00 | GOES-19 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 3550aeb2-4b52-36cc-afb6-4c58c8049d79 | -15.316 | -43.8377 | 2025-10-15 14:00:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 82aeeec9-82ab-3799-9a6e-b1119d59e13b | -13.8768 | -43.6157 | 2025-10-15 14:00:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 12484b86-d7de-3e5f-94ef-a4b44a29d80d | -10.7753 | -47.2857 | 2025-10-15 14:00:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 129.7 |
| 0a17dd0f-5fe7-3597-ba88-0e67d5eb1a3d | -4.6511 | -43.1104 | 2025-10-15 14:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 249.0 |
| 262b572a-58f5-3167-826a-44f3ff7b5d82 | -9.3221 | -46.9631 | 2025-10-15 14:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 981f230a-2fcc-38fe-8d73-ea880d709431 | -5.2866 | -41.043 | 2025-10-15 14:00:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 223.7 |
| 39fb0759-9703-3e52-bb78-633cc5a1723d | -5.4278 | -44.2172 | 2025-10-15 14:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 154.6 |
| ee49f2c4-9269-383c-9f91-4bd46c803819 | -4.6698 | -43.1092 | 2025-10-15 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 128.2 |
| 4d4de552-4566-3b14-94c2-d16dba831897 | -10.1333 | -44.5545 | 2025-10-15 14:10:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 66.3 |
| d43d91dd-f322-37a4-9c40-a799eeb51f5b | -4.6696 | -43.1326 | 2025-10-15 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 178.4 |
| f8ac3b48-d05d-3bf7-bc1c-977780dd93e9 | -11.5729 | -44.0501 | 2025-10-15 14:10:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 281.0 |
| 7670a490-339f-3eb9-8a93-90a60cd16f71 | -5.3655 | -42.7333 | 2025-10-15 14:10:00 | GOES-19 | DEMERVAL LOBÃO | PIAUÍ | Brasil | 2203305 | 22 | 33 | nan | nan | nan | Caatinga | 80.6 |
| c5c091fa-ca8e-3e67-8c8a-7054123f43fe | 1.0766 | -51.0403 | 2025-10-15 14:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 92b2e083-b8bd-36a2-acfe-af3d44a85782 | -5.8714 | -42.7886 | 2025-10-15 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 156.3 |
| a277eb05-88aa-3591-b187-d4ffe12f188c | -10.6734 | -45.2896 | 2025-10-15 14:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 2680a982-e730-3745-8ab5-994f695d6cda | -19.0319 | -57.5382 | 2025-10-15 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 81.4 |
| 6fe1148b-2baf-33c8-9957-bee7d5ad8820 | -10.8285 | -43.9717 | 2025-10-15 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 149.1 |
| 75727dac-d8f4-3274-a5b5-596d4e2cac8a | -5.2866 | -41.043 | 2025-10-15 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 216.8 |
| 44eec898-7306-36d9-8c04-033e5501217d | -5.2496 | -40.9731 | 2025-10-15 14:10:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 161.1 |
| 8094786e-4d0c-3636-9d22-d4aaa4d654ef | -10.8289 | -43.9482 | 2025-10-15 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 232.4 |
| 4aa818f1-c874-3147-9827-3c14105c576a | -2.8644 | -50.7361 | 2025-10-15 14:10:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| 7f899681-7ad9-32e5-9e6e-2b09b227727c | -5.3535 | -44.1534 | 2025-10-15 14:10:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 062289e3-3c35-3275-909b-2fe503c1c595 | -5.8902 | -42.7871 | 2025-10-15 14:10:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 7c92fb54-c8f4-3e46-a786-5c65b25a48d0 | -15.316 | -43.8377 | 2025-10-15 14:10:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 95.2 |
| c934aaec-60a3-32fa-a217-a19e577897b9 | -10.8097 | -43.951 | 2025-10-15 14:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 62174617-7c9d-39a3-8fa7-467ed6367bbd | -10.7753 | -47.2857 | 2025-10-15 14:10:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 114.1 |
| fa87daf2-d3bc-3e57-83cf-f2d258f6e14b | -4.7313 | -44.9015 | 2025-10-15 14:10:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 92.1 |
| 2eb7f8ba-7ccb-34a4-87ca-8c99fe6683c4 | -6.3733 | -41.4828 | 2025-10-15 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 103.7 |
| a9cd6b0f-fc9e-3523-aab8-d7c07e81557d | -4.6509 | -43.1337 | 2025-10-15 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 526.6 |
| de63fcb7-adf9-39a5-8845-0ffc672adc43 | -15.6538 | -44.4838 | 2025-10-15 14:10:00 | GOES-19 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 89f4e0df-8b2a-37b9-86c4-18abad8da96d | -4.6511 | -43.1104 | 2025-10-15 14:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 245.4 |
| 5d38400f-52a4-3ad8-a23d-a741190c3097 | -6.3921 | -41.4811 | 2025-10-15 14:10:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 89.4 |
| ff152dde-2214-3adf-95e6-5a5eb874ff55 | -19.0323 | -57.5174 | 2025-10-15 14:10:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 70.1 |
| e2e62afd-eeb1-3a5c-96ed-c188822df913 | -4.7313 | -44.9015 | 2025-10-15 14:20:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 108.5 |
| 51ed4030-5913-304a-bb17-98e144f3968e | -5.2496 | -40.9731 | 2025-10-15 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 260.7 |
| 8aa75abf-31d5-3d18-9025-90946fd095ad | -3.6908 | -44.3647 | 2025-10-15 14:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 174.7 |
| 4265c6e7-205c-3e0a-848b-f60db7d3db8f | -5.2682 | -40.9959 | 2025-10-15 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 137.1 |
| b41e8f5f-f20d-35f0-bdd6-b9d5d4f6f004 | -6.3733 | -41.4828 | 2025-10-15 14:20:00 | GOES-19 | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 113.4 |
| 259ede0a-dd4e-3fa5-9e3f-07be3e833d22 | -11.4384 | -44.0703 | 2025-10-15 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 126.2 |
| 5ed7a46b-860b-31ce-bc64-d7949e09bf60 | -19.0323 | -57.5174 | 2025-10-15 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 76.5 |
| 016b9b15-51eb-3e23-b95c-629b652edbe1 | -4.7312 | -44.9242 | 2025-10-15 14:20:00 | GOES-19 | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 90.1 |
| e86b39b3-2cb6-34e6-ae92-b71607e22d90 | -4.6509 | -43.1337 | 2025-10-15 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 535.6 |
| e6df95d6-5456-33d5-8dcc-aa188030d575 | -4.856 | -43.214 | 2025-10-15 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 118.5 |
| 5ae93685-9c8f-3cc7-b125-ca661f9d6cc0 | -11.5537 | -44.053 | 2025-10-15 14:20:00 | GOES-19 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 2db14439-c467-30c0-87a3-808c8c270ca8 | -6.2334 | -44.1565 | 2025-10-15 14:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 162.5 |
| ea767d48-a883-36f6-8018-62aeeee49a12 | -5.2684 | -40.9716 | 2025-10-15 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 801e40ea-372d-396a-b1b5-184205094bd8 | -5.3535 | -44.1534 | 2025-10-15 14:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 55a03adb-f2ee-330b-b1b2-b0e712064d41 | -10.8097 | -43.951 | 2025-10-15 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 160.1 |
| 9b02871a-c11c-3007-a87b-d0d4e103baec | -4.4722 | -41.9894 | 2025-10-15 14:20:00 | GOES-19 | CAPITÃO DE CAMPOS | PIAUÍ | Brasil | 2202406 | 22 | 33 | nan | nan | nan | Caatinga | 112.5 |
| f7497e57-ee21-3ccb-8512-a7224efa9f45 | -5.8614 | -43.8627 | 2025-10-15 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| d6e8dd18-cf9d-372b-b901-d34dea2ab6f7 | 1.0951 | -51.0194 | 2025-10-15 14:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 7370bfe8-18fd-339b-a23d-bfdc73e675bd | -5.8616 | -43.8395 | 2025-10-15 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.6 |
| 36cea081-5d23-3000-b060-5e6705bd13c8 | -10.8285 | -43.9717 | 2025-10-15 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 196.2 |
| ce2792e3-ddf0-3585-9725-22ff7d6e9bc5 | -6.0633 | -44.308 | 2025-10-15 14:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| b24b36f4-790e-3d8c-bc63-0ab53860080d | -10.7753 | -47.2857 | 2025-10-15 14:20:00 | GOES-19 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 112.1 |
| beca7246-ca47-3576-8603-a3944eb972ce | -5.8714 | -42.7886 | 2025-10-15 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 118.3 |
| e5dbf7df-de6f-3f5b-ad30-8d3a957f25e1 | -3.6674 | -45.2285 | 2025-10-15 14:20:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 94.6 |
| b9888dee-3401-370c-87ad-1994ded7ea97 | -5.8802 | -43.8613 | 2025-10-15 14:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 4497fd26-4ee9-359f-ba59-744e14e19508 | -4.6511 | -43.1104 | 2025-10-15 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 197.0 |
| 054a5d43-7ac6-39d1-bb4e-8293d7050be4 | -19.0319 | -57.5382 | 2025-10-15 14:20:00 | GOES-19 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 81.8 |
| 408771df-ef16-3436-b613-a0752917bb41 | -3.0386 | -44.4612 | 2025-10-15 14:20:00 | GOES-19 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 95.1 |
| f3fd8d03-26d9-3e79-ae1e-4590e39391f3 | -4.5917 | -43.5563 | 2025-10-15 14:20:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 94.1 |
| c36b51ed-0b9c-3957-902e-365554ee9d19 | -11.438 | -44.0938 | 2025-10-15 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 168.5 |
| 06d3f720-3b5c-317b-a95a-3c6911e99a00 | -10.8289 | -43.9482 | 2025-10-15 14:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 317.4 |
| 1ac9f7ea-3b82-3375-851a-c996a267c1d8 | -5.5696 | -42.9766 | 2025-10-15 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 78.4 |
| 3b4c11e0-bd24-3faa-b4b1-f6b65085a75c | -5.2866 | -41.043 | 2025-10-15 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 240.4 |
| b9bc7bea-d966-3094-913d-478fdd3abaad | -4.6696 | -43.1326 | 2025-10-15 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 180.1 |
| f5365906-de7b-350e-8b48-9334cf9a387a | -6.0492 | -41.8959 | 2025-10-15 14:20:00 | GOES-19 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 187.7 |
| d998ef13-906b-36a2-9bf9-32f2bbde5ba7 | -6.4637 | -41.8351 | 2025-10-15 14:20:00 | GOES-19 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 110.4 |
| e1ccde91-e86c-32c4-98db-70acd9d4a07b | -5.4278 | -44.2172 | 2025-10-15 14:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 232.2 |
| 72b3ecca-0e33-3193-86cd-0060969f7e8e | -4.6698 | -43.1092 | 2025-10-15 14:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 131.4 |
| 573678dd-6ab6-3134-9451-93cdfcfe7f62 | -5.4463 | -44.2388 | 2025-10-15 14:20:00 | GOES-19 | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 138.2 |
| 97afb6c0-f74d-3842-a813-86ad0201e5eb | -3.6722 | -44.3656 | 2025-10-15 14:20:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 102.9 |
| e7899bfc-bd7e-3193-b4aa-7a0d00554b5e | -5.5694 | -43.0001 | 2025-10-15 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 126.3 |
| c666de7f-f76f-350c-92b5-9c5aa2a289fe | -5.4465 | -44.2159 | 2025-10-15 14:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 128.4 |
| fd0da934-63ad-341e-aece-0aab696d7fe0 | -5.9085 | -42.8327 | 2025-10-15 14:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 70.6 |
| a213988c-9423-3407-b069-4815e8a53765 | -11.4572 | -44.0909 | 2025-10-15 14:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 226.2 |
| dca6ab77-3180-336e-bc59-dd81ad73995b | -5.2494 | -40.9974 | 2025-10-15 14:20:00 | GOES-19 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 149.9 |
| b7ed3623-f504-37c6-9bcc-5ecd4d044d72 | -5.4278 | -44.2172 | 2025-10-15 14:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 275.8 |
| acc3d79f-bcb3-3a5b-af7c-a9e4aedc1fd0 | -4.1336 | -42.2237 | 2025-10-15 14:30:00 | GOES-19 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 6686348a-cb56-3db2-9b70-80f8d0a4993e | -7.7575 | -42.4458 | 2025-10-15 14:30:00 | GOES-19 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| 80decb74-d800-3112-995c-36bb4bbc4712 | -3.6675 | -45.2059 | 2025-10-15 14:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 4b1d5be7-c8d2-3ff6-80d9-15b9d17adb0a | -10.1333 | -44.5545 | 2025-10-15 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 53e17486-fd52-3f63-95ed-0a3dc93498da | -5.4465 | -44.2159 | 2025-10-15 14:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 167.0 |
| 5a122caa-a861-32f5-aa2a-17eba59f6908 | -10.1524 | -44.552 | 2025-10-15 14:30:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 85.1 |
| 9cfdb8e6-1dfe-3c8c-9a7f-b0c5c0bfc03d | -9.3336 | -46.1113 | 2025-10-15 14:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 85.6 |
| 7b353d7a-eecc-35a1-bf57-da8494487ba6 | -3.6908 | -44.3647 | 2025-10-15 14:30:00 | GOES-19 | CANTANHEDE | MARANHÃO | Brasil | 2102705 | 21 | 33 | nan | nan | nan | Cerrado | 445.9 |
| f055b624-692e-35ea-817f-3c06182100cb | -11.4572 | -44.0909 | 2025-10-15 14:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 182.1 |
| 6cf593d3-a4cc-3f63-a683-25a969feb2ca | -3.6674 | -45.2285 | 2025-10-15 14:30:00 | GOES-19 | IGARAPÉ DO MEIO | MARANHÃO | Brasil | 2105153 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |


[Clique aqui para ver as próximas entradas](README54.md)
