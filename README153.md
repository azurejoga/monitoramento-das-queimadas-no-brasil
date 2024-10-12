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

## Dados Diários - Página 153

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9d8394b-3fd0-38cc-9f56-3e71088fb471 | -12.6983 | -45.4797 | 2024-10-12 14:26:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 121.8 |
| d038bfb9-56bf-3222-b75c-bf938501067d | -13.7348 | -60.5883 | 2024-10-12 14:26:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 216.5 |
| 9b3bfe44-d73c-3da6-a75a-7e5556d71564 | -13.7342 | -60.6471 | 2024-10-12 14:26:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 53.9 |
| d938f79f-9410-3e73-aa43-73cc7319e446 | -13.7153 | -60.6289 | 2024-10-12 14:26:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 5cdf8085-6b91-38c9-81a9-15ece4f2f713 | -0.803 | -48.6611 | 2024-10-12 14:35:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| e230c718-4dd7-3888-a7c9-3f7b23893f9d | -0.8215 | -48.6609 | 2024-10-12 14:35:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| e11e2a1e-2061-3a88-978d-005c08addedd | -1.0428 | -48.8085 | 2024-10-12 14:35:12 | GOES-16 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| ddd0ef0f-3f4f-30d2-b830-607b0d8c3f79 | -6.8294 | -42.8233 | 2024-10-12 14:35:45 | GOES-16 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 54.0 |
| db6ee7df-0ac3-3215-b0c9-72b0afaea604 | -7.6592 | -61.1869 | 2024-10-12 14:35:51 | GOES-16 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 812acd5c-81fa-30aa-901f-4620035e87cc | -8.9376 | -64.2406 | 2024-10-12 14:35:58 | GOES-16 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 82.0 |
| fb9dfbd7-0ebd-33e0-952b-39ae779843f5 | -8.911 | -62.372 | 2024-10-12 14:35:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 57.0 |
| e3dd5cc0-1acc-3172-8b2d-a5129bbcc59c | -8.9667 | -62.3506 | 2024-10-12 14:35:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 484f3965-7494-3353-8260-d5f423972410 | -8.9666 | -62.3696 | 2024-10-12 14:35:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 5d35d1e5-3045-3567-9356-78e5388a9a3a | -9.8554 | -60.2772 | 2024-10-12 14:36:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 73cc1e5f-3d26-3ddc-a229-c56193ccca54 | -10.1865 | -42.4291 | 2024-10-12 14:36:04 | GOES-16 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 67.7 |
| c186c8fd-b0ff-31a7-9783-a7c7df6b322e | -10.4032 | -49.4318 | 2024-10-12 14:36:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 103c952c-dcbc-3cb9-a0c0-c2a9a013e5a6 | -10.6883 | -50.7084 | 2024-10-12 14:36:07 | GOES-16 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 138.8 |
| 31b86ab0-0957-3c6b-b8b6-1ec8b20ed31b | -11.2637 | -44.213 | 2024-10-12 14:36:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 159.8 |
| f6f8180e-4651-33c0-9eaa-4f2c4065209a | -11.2446 | -44.2158 | 2024-10-12 14:36:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.0 |
| ac2c549c-70ad-3328-81c1-3f9bc2ef56db | -12.1142 | -50.5285 | 2024-10-12 14:36:15 | GOES-16 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 154.3 |
| b1e3b784-2e8a-3306-9806-18e0e728de3e | -12.3374 | -59.8682 | 2024-10-12 14:36:17 | GOES-16 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 9782d65d-5b95-38a5-b1b2-c67af9f5c623 | -12.3246 | -59.2611 | 2024-10-12 14:36:17 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 60.0 |
| 2a9ae767-c086-3165-b1df-8e1958d55608 | -12.679 | -45.4827 | 2024-10-12 14:36:18 | GOES-16 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 127.2 |
| 0fa674fe-3662-33d4-893c-a70fb16ab23c | -13.7342 | -60.6471 | 2024-10-12 14:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| ddc7bdf1-b795-382f-8640-67b50e6e831d | -13.7348 | -60.5883 | 2024-10-12 14:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 200.2 |
| ae3c9c92-ea97-35ad-9af0-a1fa3f4a396a | -13.7153 | -60.6289 | 2024-10-12 14:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 8214d84a-150a-3e8b-ab2e-e65a9289880d | 3.2863 | -51.3476 | 2024-10-12 14:44:48 | GOES-16 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 63.6 |
| b5a42f03-bc0a-3eb4-912b-728d99ba0f85 | -0.84 | -48.6394 | 2024-10-12 14:45:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 20ed0e1c-8024-32b3-91e3-15bab1e42cdc | -0.8215 | -48.6609 | 2024-10-12 14:45:11 | GOES-16 | SALVATERRA | PARÁ | Brasil | 1506302 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| b2670556-3bb9-39ba-86ee-89a79c530e89 | -3.1389 | -43.003 | 2024-10-12 14:45:24 | GOES-16 | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| b3061e7d-25fe-3702-a36d-5b3a40239935 | -5.2485 | -48.0641 | 2024-10-12 14:45:36 | GOES-16 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b8b77ef7-cc12-3063-ac6e-086d06ec5d2e | -5.2869 | -47.8882 | 2024-10-12 14:45:36 | GOES-16 | SAMPAIO | TOCANTINS | Brasil | 1718808 | 17 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 1af81168-8f2c-3e82-88f5-f3e18334a863 | -5.2674 | -48.0196 | 2024-10-12 14:45:36 | GOES-16 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 7ec496bd-bcd3-3a3c-80e9-e4faf48944d5 | -5.3813 | -47.7085 | 2024-10-12 14:45:37 | GOES-16 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 56.0 |
| e12730ef-a2c5-31d0-872d-7f277b7440bf | -5.3821 | -47.5994 | 2024-10-12 14:45:37 | GOES-16 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 57.5 |
| fe5ea98b-c49d-334d-aeef-04e17c03a2ae | -8.3217 | -44.0983 | 2024-10-12 14:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 59.4 |
| d6d599c4-300a-3be1-8405-eb872e9c7808 | -8.2839 | -44.1024 | 2024-10-12 14:45:53 | GOES-16 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 90.7 |
| b6530593-21e3-381a-92da-7008bdbb1840 | -8.776 | -63.2673 | 2024-10-12 14:45:57 | GOES-16 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 50.0 |
| a9067f38-be31-3f32-bbfd-ecaadf1eebe5 | -8.9667 | -62.3506 | 2024-10-12 14:45:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 49.0 |
| fb31c339-2603-39d0-94fb-2e7389f8763e | -8.911 | -62.372 | 2024-10-12 14:45:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 58.8 |
| a358817f-0a84-3d41-a445-33bc90ab44a1 | -8.9666 | -62.3696 | 2024-10-12 14:45:58 | GOES-16 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 550902c1-e1d1-3dd0-9853-828c68b1bf3b | -10.4032 | -49.4318 | 2024-10-12 14:46:05 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ad819ff3-a807-3478-9347-8c0329575ce9 | -10.4427 | -50.7123 | 2024-10-12 14:46:06 | GOES-16 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 42aff72a-1dcd-3bce-935a-62513a634cb0 | -10.5094 | -49.9584 | 2024-10-12 14:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 65cf9080-c835-3946-bcba-fd9e24b947b0 | -10.4713 | -49.9838 | 2024-10-12 14:46:06 | GOES-16 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 106.0 |
| b1c29a93-7346-3d81-ac37-892be93cd122 | -11.2633 | -44.2364 | 2024-10-12 14:46:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 159.2 |
| 974217cc-b07f-3971-b67e-30296c1cd498 | -11.2446 | -44.2158 | 2024-10-12 14:46:10 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 157.5 |
| 68185fc0-ba66-3725-aee9-64ced9fa9640 | -12.3246 | -59.2611 | 2024-10-12 14:46:17 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 71.9 |
| 303989a2-30fa-305c-ade7-325fbc009d8a | -13.7348 | -60.5883 | 2024-10-12 14:46:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 187.4 |
| db6e22ad-0d04-3019-bc14-373ed7159102 | -13.7153 | -60.6289 | 2024-10-12 14:46:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 104.9 |


