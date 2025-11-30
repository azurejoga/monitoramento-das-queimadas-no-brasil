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
| ba1f272c-3827-33ab-b22a-997b670f79ce | -8.0318 | -43.1493 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 60.1 |
| 3822da3b-e1db-39f0-aa31-8823478f27bd | -23.6454 | -52.932 | 2025-11-30 01:00:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 75.3 |
| 87b04062-933a-3d66-912c-58d3c4afe2f4 | -5.7309 | -39.8286 | 2025-11-30 01:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 467.9 |
| 53b7e082-a53a-383b-8c0f-0c2b897edea3 | -5.7498 | -39.8269 | 2025-11-30 01:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 92.5 |
| 5c28423e-1c29-3ae5-be81-dd2cab19f198 | -5.7306 | -39.8534 | 2025-11-30 01:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 200.3 |
| d71759e2-798c-3919-bef2-97f92cb885a8 | -7.5014 | -37.4242 | 2025-11-30 01:00:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 62.7 |
| edf04dcd-073a-32da-ace8-c5fa28d822d0 | -8.0507 | -43.1472 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| f3d1c52f-4e18-308e-95d1-e6fd0b05ab76 | -12.0195 | -49.2659 | 2025-11-30 01:00:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 99.4 |
| 811cf096-c133-3460-9264-e3118a2c78d8 | -8.1633 | -43.2055 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.8 |
| 660b50c1-ca7e-3b80-becb-0437435fec6a | -4.4358 | -44.486 | 2025-11-30 01:00:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 5b3bdd50-035d-3739-b06c-211fbe74b394 | -2.6507 | -48.5629 | 2025-11-30 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 65.7 |
| 1666aa8a-36f2-3666-9d6c-b7f7262a0fe5 | -5.7311 | -39.8037 | 2025-11-30 01:00:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 104.0 |
| 726b9aaa-d652-3f55-84e9-e9a863448052 | -8.1822 | -43.2034 | 2025-11-30 01:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.8 |
| 724edda1-52e2-3246-8a69-c0c4426ec470 | -23.63304 | -52.95542 | 2025-11-30 01:06:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 44.8 |
| cc0519dd-29d0-3a12-8420-3673395e2431 | -23.62967 | -52.93752 | 2025-11-30 01:06:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 42c41b7d-eefc-3f45-8e5e-d3b1dafb7bf1 | -22.49701 | -46.95964 | 2025-11-30 01:06:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 30.3 |
| 6ea30a46-3766-3346-b7bb-5f67ea3abce0 | -23.63172 | -52.94992 | 2025-11-30 01:06:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 149.0 |
| 4f5203b6-3291-31ac-9275-9df4ca0e4227 | -22.49015 | -46.92591 | 2025-11-30 01:06:00 | TERRA_M-M | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 61029766-dc94-37ad-8808-8bc4d4fe227f | -23.62303 | -52.95725 | 2025-11-30 01:06:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| ab0a2b8d-c58d-3564-9a81-889232225437 | -23.64171 | -52.94798 | 2025-11-30 01:06:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.2 |
| ba4afd22-98a1-3d9b-b33d-b8c83e492a82 | -23.63106 | -52.94302 | 2025-11-30 01:06:00 | TERRA_M-M | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 113.1 |
| 7b16df03-9c56-3a2f-8b47-4a2b67ff4663 | -19.98271 | -47.86613 | 2025-11-30 01:09:00 | TERRA_M-M | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 44.2 |
| ac65a673-6994-3b4f-a74b-67681d17f775 | -19.92768 | -57.44421 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.7 |
| b23b9b36-f141-3c61-b67a-f8f5e018cb8f | -19.9763 | -47.83356 | 2025-11-30 01:09:00 | TERRA_M-M | DELTA | MINAS GERAIS | Brasil | 3121258 | 31 | 33 | nan | nan | nan | Cerrado | 45.0 |
| e13ea8df-95c7-32dd-bb0c-c89fe53a65de | -19.84411 | -57.77024 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 22.0 |
| 25ba478d-c9fa-316e-b66e-b032366f81b0 | -19.85683 | -57.79711 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 10f3b5b3-d652-380d-a920-246a25749c26 | -17.48189 | -57.1396 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| d58a4e14-d5f0-309e-acf8-1543f3de6866 | -17.48813 | -57.11945 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| cc0fe832-ec63-3b6f-b899-72547ab535c0 | -17.50995 | -57.14472 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 6f92110a-2359-3ce0-9bff-25d3bd775a2d | -20.91847 | -56.37072 | 2025-11-30 01:09:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7b4d7d67-506a-38cd-b5ce-2ec1889d7dea | -21.00043 | -49.31493 | 2025-11-30 01:09:00 | TERRA_M-M | CEDRAL | SÃO PAULO | Brasil | 3511300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 36.0 |
| 205cca15-0ec9-3021-aaf9-ad5464714d4c | -19.85556 | -57.78769 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 25.2 |
| ba6323b6-52ce-328c-8482-fd8f12b125bc | -19.92011 | -57.45499 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.7 |
| 7acc44dc-4c23-3ce0-93fd-f0fb991c2e06 | -19.91882 | -57.44561 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 1e25141f-fd46-3734-8e53-1ed17839769a | -17.47922 | -57.12086 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 8bdcc89b-9de9-32f9-820e-b1c695e2f181 | -19.93396 | -57.42405 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 3562650a-ac96-3f83-8517-bd88e67fb4ba | -19.85428 | -57.77827 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 31.1 |
| a497ae2e-b2d3-392d-96ad-35fcdda4802d | -17.49213 | -57.14754 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 042fab3d-0caf-3320-b76b-47499e6ac090 | -19.33415 | -54.17943 | 2025-11-30 01:09:00 | TERRA_M-M | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 4fb05735-06bd-3694-a691-90a2320ddc36 | -17.48055 | -57.13023 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| 8389a9a2-4f1b-389c-9598-73135efe2e64 | -21.14604 | -48.62154 | 2025-11-30 01:09:00 | TERRA_M-M | VISTA ALEGRE DO ALTO | SÃO PAULO | Brasil | 3556909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 69.3 |
| 5725739c-8bf9-3adc-8674-00d0a71b1854 | -20.18286 | -52.38316 | 2025-11-30 01:09:00 | TERRA_M-M | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | 19.2 |
| e572de9a-27b9-3008-82e4-a971b8f9853f | -20.91983 | -56.38029 | 2025-11-30 01:09:00 | TERRA_M-M | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8fe0c82e-dfc3-3e92-b168-3722272ea3a8 | -19.86316 | -57.77689 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.6 |
| de528c42-7328-3080-b075-c05b52173abb | -19.84667 | -57.78907 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 15.8 |
| cc488a4f-ec71-3ec8-8169-df3edfc99eb0 | -19.84539 | -57.77965 | 2025-11-30 01:09:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 60.2 |
| 7c778e94-206b-375e-a616-bcb7c24bcc29 | -17.50104 | -57.14613 | 2025-11-30 01:09:00 | TERRA_M-M | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 19.2 |
| b4557c9e-724f-3e73-b04e-d453799c066a | -12.01086 | -49.28326 | 2025-11-30 01:09:00 | TERRA_M-M | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 86b0175f-b8c5-35c0-a7ff-9bf1d32e29ab | -14.99468 | -56.82244 | 2025-11-30 01:09:00 | TERRA_M-M | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 898c2b90-92b3-33cd-a9cd-4faa70f32df9 | -12.0004 | -49.2683 | 2025-11-30 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 01e811ef-3268-36b5-a10b-5d2c4675fa7d | -8.0321 | -43.1257 | 2025-11-30 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 103.2 |
| 0117ef9d-cc94-3d7a-8c7a-b0b905036550 | -5.7309 | -39.8286 | 2025-11-30 01:10:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 260.2 |
| c9b8faee-c2f1-3170-9217-0fab00224e8b | -8.1633 | -43.2055 | 2025-11-30 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 84.5 |
| a00176e5-5e3b-3706-976e-41f10fa86d09 | -8.0507 | -43.1472 | 2025-11-30 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.7 |
| dadaf3bd-3aa1-3635-b4e1-6135b7790f54 | -19.8477 | -57.7627 | 2025-11-30 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 44.7 |
| 89803a27-8614-3236-9adb-031f06467fd1 | -12.0195 | -49.2659 | 2025-11-30 01:10:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 91.8 |
| d030a155-a24c-39eb-b84d-704d8dedc0e6 | -2.7565 | -45.1744 | 2025-11-30 01:10:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 1a298ffe-662e-3cbd-b31e-4b3ae19c0d8a | -8.051 | -43.1237 | 2025-11-30 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 79e22f26-a297-378b-a6ef-b92fee3e602c | -9.9864 | -36.3848 | 2025-11-30 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 88.0 |
| 42dccd31-6df4-3312-b130-0b1aa44d2f28 | -9.9859 | -36.4118 | 2025-11-30 01:10:00 | GOES-19 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| 7e492cd9-2f91-3a18-b752-55448e52dc5c | -4.4358 | -44.486 | 2025-11-30 01:10:00 | GOES-19 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 311b3075-30bc-3f60-9901-28379071f387 | -5.7306 | -39.8534 | 2025-11-30 01:10:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 9a033504-fedf-34b2-bfee-884afe3f19eb | -8.0513 | -43.1001 | 2025-11-30 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.8 |
| f71553f5-ceb7-3559-b3d3-7636ec443012 | -8.1822 | -43.2034 | 2025-11-30 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.7 |
| 1a5f5e01-c7fa-3072-8033-8ccc5b2720b7 | -5.7311 | -39.8037 | 2025-11-30 01:10:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 58.4 |
| d099247d-f518-3a70-9432-5dbdf28fff44 | -19.8276 | -57.7654 | 2025-11-30 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 37.1 |
| 2d19e1e4-30e2-38b7-a51f-ca35eb235b0f | -2.3464 | -45.5469 | 2025-11-30 01:10:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 7252aa58-9d7f-3d43-8b0c-240e03ac1b49 | -5.7498 | -39.8269 | 2025-11-30 01:10:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 63.4 |
| 230af91a-eb28-3005-8b6d-704f028b4e55 | -19.8473 | -57.7835 | 2025-11-30 01:10:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 43.8 |
| 8905e658-8d67-3d23-85cb-d8b050d05043 | -2.6507 | -48.5414 | 2025-11-30 01:10:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 53d5f337-2db3-377e-be76-308f970abf24 | -11.07699 | -54.77516 | 2025-11-30 01:11:00 | TERRA_M-M | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 22523643-ad65-3bdb-b134-2b2b0919d194 | 1.985 | -55.73388 | 2025-11-30 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.9 |
| 7e281a82-9a2e-31bb-abbf-f9ac0b874006 | 1.15437 | -60.50166 | 2025-11-30 01:13:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 08aabb27-94ef-3f85-aed8-c66f88bd8763 | 1.98222 | -55.74654 | 2025-11-30 01:13:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 011179c7-d7a3-3a79-ab4c-7f977b2a646d | -23.6237 | -52.959 | 2025-11-30 01:20:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 71.6 |
| a7a7b07a-497c-30f4-a9b4-6851f73c5c1d | -23.6448 | -52.9546 | 2025-11-30 01:20:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 76.4 |
| e91f095a-fa89-30c7-9155-dedc0dfb2e90 | -2.7565 | -45.1744 | 2025-11-30 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 115.0 |
| 06997dff-522e-30c8-a9b5-25e95bf5c947 | -23.6243 | -52.9365 | 2025-11-30 01:20:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 121.4 |
| 29702683-4f85-3916-9e47-aa19fc570f64 | -2.7564 | -45.197 | 2025-11-30 01:20:00 | GOES-19 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 408450f0-3871-39ae-857a-0f086a82dfad | -8.051 | -43.1237 | 2025-11-30 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 128.1 |
| 1c7240f9-87a7-3470-a072-66757d61901c | -8.0321 | -43.1257 | 2025-11-30 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 120.7 |
| 115dbfa2-f906-32a6-bd84-81441f957488 | -2.6507 | -48.5414 | 2025-11-30 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| d0dfa974-ddb6-3678-9af4-2dd8541a0474 | -2.3464 | -45.5469 | 2025-11-30 01:20:00 | GOES-19 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 151.2 |
| efbe7b7a-7c3b-35a3-917c-4a69abe2ec7e | -2.6322 | -48.542 | 2025-11-30 01:20:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| 4efd118e-e2ec-3d13-9145-145387b8bb5c | -23.6454 | -52.932 | 2025-11-30 01:20:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 136.0 |
| c6e066fb-1489-3545-b0f2-8b26c464fa30 | -5.7309 | -39.8286 | 2025-11-30 01:20:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 132.6 |
| d456cdec-3ac9-34d7-98f9-9acd8b6df2b8 | -19.8675 | -57.7808 | 2025-11-30 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 40.7 |
| 7de68047-2045-3ec3-9310-dd413f87be72 | -12.0195 | -49.2659 | 2025-11-30 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 82.6 |
| bd9663f6-040a-3575-ae67-450ca375dc32 | -5.7498 | -39.8269 | 2025-11-30 01:20:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 61.6 |
| d777e983-960a-3d59-85fb-97ec9677a357 | -8.1633 | -43.2055 | 2025-11-30 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 100.0 |
| 98531155-19d4-3698-b026-d93cbac7a509 | -19.8477 | -57.7627 | 2025-11-30 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 64.1 |
| 00944daf-f7a6-3f4a-82a8-f417340682cf | -12.0004 | -49.2683 | 2025-11-30 01:20:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 6eb7f6d6-63a0-3325-8e20-bff415107ab4 | -19.8473 | -57.7835 | 2025-11-30 01:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 88.6 |
| 9ca62719-1d15-3db1-8fae-9e423cf8624e | -12.0004 | -49.2683 | 2025-11-30 01:30:00 | GOES-19 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| 09322a82-d733-367e-a409-241de2311aea | -7.5014 | -37.4242 | 2025-11-30 01:30:00 | GOES-19 | SANTA TEREZINHA | PERNAMBUCO | Brasil | 2612802 | 26 | 33 | nan | nan | nan | Caatinga | 60.6 |
| dc084fb4-79b5-360d-9137-4a2e4379bf71 | -23.6454 | -52.932 | 2025-11-30 01:30:00 | GOES-19 | TAPEJARA | PARANÁ | Brasil | 4126801 | 41 | 33 | nan | nan | nan | Mata Atlântica | 96.6 |
| 252eb0be-3478-3c7e-b0e6-5e03021c7cc7 | -8.1633 | -43.2055 | 2025-11-30 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 98.3 |
| f2227b08-39ac-369c-bfb6-91106ba9db87 | -2.6322 | -48.542 | 2025-11-30 01:30:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.7 |
| ea77fd77-67fd-34a2-90bb-601c216c2d9c | -19.8477 | -57.7627 | 2025-11-30 01:30:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 81.7 |
| 6ae3a854-4156-33e1-bce8-319a5a896975 | -5.7309 | -39.8286 | 2025-11-30 01:30:00 | GOES-19 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 95.5 |


[Clique aqui para ver as próximas entradas](README5.md)
