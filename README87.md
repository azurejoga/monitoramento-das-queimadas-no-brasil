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

## Dados Diários - Página 87

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a809e8f7-a28b-310b-af72-577fa6e19fdb | -9.02548 | -65.71076 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| aeb798ae-f99a-38dd-9dd9-939f51f22db6 | -9.02429 | -65.71944 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6f22cac2-e881-335c-a912-a52f89668c52 | -9.01863 | -65.68591 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b005fd03-3255-3a76-ad23-dba281fd2523 | -8.13615 | -62.86405 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 14aa73dc-b072-35bd-bedd-2b32369c22ad | -5.62088 | -60.23654 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4ae5b24b-4959-3060-859e-3ab61c116d94 | -9.01706 | -65.38962 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6d7206c0-2497-35d5-be3e-c89303c991db | -9.02595 | -65.70521 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 98da4307-9d95-3975-8267-c0f8ff2a79c3 | -8.91182 | -62.41439 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1d7665dd-1d06-3774-9194-c06eb36c3405 | -9.20845 | -60.78961 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 75a5e93a-c5c5-3e7e-9d36-43e54eb450eb | -8.99642 | -63.63667 | 2025-08-24 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 66317886-d21d-3f74-ab60-4aec77c77f5b | -7.54805 | -63.8535 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f6cca0e-8d58-35fe-9f41-6bf02dcb323e | -9.04878 | -65.72626 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 249697ce-2ec5-3536-b896-430b2ed5e986 | -9.33115 | -63.1931 | 2025-08-24 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| bf41a21f-1622-36c0-ba00-5cee9c712bc0 | -9.14021 | -60.7732 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 970713a5-3472-32ac-a1d2-873a4823eeef | -9.01041 | -65.70869 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f0b8377b-dd45-3767-87b6-22241e95f266 | -8.13502 | -62.87292 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 508b0772-fba7-3e35-8af4-a2710a3e18d1 | -9.01701 | -65.69781 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a605852f-8af9-3474-b67d-4f529003e89f | -9.63136 | -63.09914 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eba62d69-ff96-31fe-b477-39057fba5a1b | -9.20685 | -60.80083 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 4f9a763a-af4d-3db8-931c-066ae1cf35c9 | -7.80555 | -63.55439 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b06231f-e41e-31d9-94fc-79f1c4500719 | -9.2077 | -60.79607 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 67c2d252-a94d-3fd2-b2f3-f64010e9259b | -9.02084 | -65.70727 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f49438e7-519d-3e48-9809-52d40f415ef3 | -9.03061 | -65.70875 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 48cd2b5b-3312-3990-a92c-eb7ce904ce25 | -8.67812 | -62.8796 | 2025-08-24 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1e2e000c-1484-3629-b0ae-119592d59350 | -7.81125 | -63.55518 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4ed9768-61b4-3355-8477-4759503b4994 | -7.7266 | -67.0697 | 2025-08-24 06:14:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f42a350b-d0dd-3100-aed9-ca87c7392c0f | -9.02018 | -65.71031 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e3792c2-5538-3d2d-8604-3ca7c98ca32d | -8.62853 | -62.62593 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ec5fd680-3d9c-3100-9460-2826b3273a57 | -9.02892 | -65.72296 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75dda253-7fad-38a3-9086-a437cbbb5fc9 | -7.96895 | -63.07117 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0fee1997-8b72-3fa5-9f2f-4475dd641fe3 | -9.19621 | -60.77325 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5deb04cd-94f4-3d92-bd7a-cc16252f4d7d | -9.14096 | -60.76685 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8813446-c06f-3143-99e6-beda25a21e01 | -8.89622 | -62.42703 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7720c14-775c-3fa1-b14e-aa6de804cf7c | -8.68414 | -62.88046 | 2025-08-24 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69460a90-3e0b-3456-82c9-14fad062a4f1 | -8.61431 | -62.59046 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b2cd14c0-0295-3efb-92af-10112e4fafa3 | -9.47824 | -63.13378 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 599a2544-b190-3099-ad09-c7203705ad2b | -9.02508 | -65.71364 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 33ef1301-2082-3d63-afbb-9a11bb8ef109 | -8.61866 | -62.60543 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e389c449-4799-309a-a810-261c1e26c6e8 | -8.89936 | -62.41277 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e9f971c0-833b-3c08-8e81-5b014eca7717 | -9.19691 | -60.7683 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3a0a38f1-e441-34e1-990f-e931bb2e7415 | -9.00463 | -65.71365 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b487ead6-5f5c-3218-98f4-c0726d8ce4cd | -8.90743 | -62.44855 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 00fcf97f-ace1-32b6-a6e1-5d9c5eeb3068 | -9.02986 | -65.71453 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1312435a-336b-353c-8613-e60dc775bca9 | -7.4303 | -60.62269 | 2025-08-24 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c0e3e3d-c215-3dd2-aa8e-0d3b12d2f29e | -9.02301 | -65.38416 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e40563e1-d278-30b2-a7ae-b0a4f533d384 | -8.91426 | -62.44459 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25721ded-98d1-3ce5-917c-be3a8305bcd5 | -5.42268 | -60.1772 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 522f6b6a-6452-3d99-88b1-e32698ba8445 | -7.97427 | -63.0763 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9a48fef3-2aad-3a53-a0e4-7b3cb779388e | -7.55478 | -63.85447 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0726a1ce-c9ec-3ba2-af51-17161c301e12 | -9.02558 | -65.70808 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 5a3f5413-8524-32f1-a8ac-7a802e43cc07 | -9.13327 | -60.77269 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e7d71f6f-9544-3144-9780-20dd49f1b409 | -8.60818 | -62.58961 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f4688dde-ac9d-3ef2-b825-bceaeac4e060 | -8.92171 | -62.43582 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 358aaa33-4afa-356c-b237-4d16b05ec77b | -9.20763 | -60.79446 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c4c9f934-1d05-316c-adfd-1096c2072887 | -9.13253 | -60.77466 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 695e49f4-581c-37d5-8d4a-7b66277fcb55 | -9.02587 | -65.70789 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4cea3697-9479-3598-8fb8-a25ea9f871cb | -5.44971 | -60.19505 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 5d3dc6a8-dec7-3858-8cc0-535f59d1cd87 | -8.90628 | -62.44835 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 31e256e7-1298-362c-a431-415718ba5432 | -7.55934 | -63.86264 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e5eb977-c1cf-3e56-834f-8553198043b4 | -9.00761 | -65.382 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f27e2eef-84dc-3415-8298-83e5febf9bec | -8.91119 | -62.4193 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8d5b60ce-d649-3e96-9b81-d8a0b543312d | -9.02971 | -65.71719 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b3c0996-8e3b-3ef6-b98e-161fe1349a44 | -7.94762 | -63.0507 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 76480f07-eaa7-3d98-891e-1d3192b8a210 | -9.02219 | -65.39032 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3158f2f3-a6e6-3a82-9ae6-f278f4a5e729 | -9.0054 | -65.70796 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cd545cc0-53ec-34be-b165-d1d6f3209dbc | -9.01868 | -65.72193 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 288c8a0f-0264-3bb8-9d6f-e2c439b69430 | -7.73172 | -67.06586 | 2025-08-24 06:14:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 95c3c599-d98a-343c-a93b-57bd1882e72e | -8.66776 | -68.68625 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c673772-827a-39cf-9392-8b486aa0a46c | -9.02446 | -65.71677 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 895d7cd3-b729-3d75-8e74-c1820d0f90d2 | -7.55266 | -63.86172 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 47249450-7751-394b-923c-1940767f79cd | -9.01425 | -65.7181 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| da44800f-d321-3a21-8071-876c67b1b861 | -7.5482 | -63.8611 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 610a890d-b9a4-3626-a5ca-29d649c09058 | -9.01823 | -65.68888 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0de7d971-7493-3372-ad0d-74a6141ea79c | -9.01782 | -65.69186 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 3a15401e-3643-3e0e-b3e4-dabaab539cc7 | -7.57085 | -63.43728 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1d9d984-ef54-38f2-b1c4-447a19111e07 | -9.03024 | -65.71163 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| bed63e6a-b6f8-3266-86c4-791b3f6be1c7 | -7.56036 | -63.85525 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1123f384-68c8-3bb6-a9b4-5721f4f888db | -8.141 | -62.87377 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| de481168-af9d-3651-9d91-a78ad34ea6c5 | -6.7471 | -62.86751 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 40f7256c-42c7-3682-aab2-2ac64432fbe1 | -7.97305 | -63.07446 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c23e3d33-e046-3dec-975e-2d52a9d2b7af | -7.43516 | -60.62474 | 2025-08-24 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 43e3ec29-342f-38d1-84f3-2753f97a3eb8 | -9.02521 | -65.71097 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9648f02-df46-387b-ab62-34188aeb6048 | -8.92046 | -62.43563 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e470171f-97bb-3906-92fc-641ca9e938c5 | -8.91043 | -62.41413 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 0d651850-50a9-3572-9e8f-87b5e25c02a8 | -8.6078 | -62.64219 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fbae1a3-4518-3502-96fa-eaa626c3e097 | -8.82244 | -69.39716 | 2025-08-24 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d97baffa-d88f-380b-907f-e82188a67523 | -9.04916 | -65.72333 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 67a3d758-6546-3016-b2cc-d45af4caccdd | -9.01661 | -65.70076 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a1843a0a-0a5e-315e-af9b-9199e591e73f | -9.07538 | -65.71837 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f28acbb8-ccda-3fc7-99cf-2ba51dcdf328 | -9.23396 | -60.92871 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c6bf9bb8-924f-3498-8dcf-a44ba68de438 | -8.87701 | -62.43938 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7fa1d65c-7e91-3c38-a4b7-f3934ad93794 | -7.55314 | -63.85801 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe4ab591-78fa-3fe7-8224-7778a8e58ddb | -7.54757 | -63.85723 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5d02b055-bdfe-3877-87fc-f1a80ab34ac8 | -10.42353 | -64.43076 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54023c3d-98c2-395a-b749-e6733167c92e | -9.82166 | -64.26368 | 2025-08-24 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fead5e6-c896-3c18-8c0f-92b96e345601 | -10.41749 | -64.43369 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d76d2436-f678-3d3a-9c5c-9a36381c5cf8 | -9.82117 | -64.26746 | 2025-08-24 06:16:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee615697-3578-3628-b686-be2a68e704ce | -10.41376 | -64.41803 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 13d3d5b5-1e1f-3755-a19b-a9c10f3940ce | -11.9925 | -61.0275 | 2025-08-24 06:16:00 | NOAA-21 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 62bca687-3ebe-3339-a243-9cf4ef831a46 | -10.41889 | -64.42244 | 2025-08-24 06:16:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README88.md)
