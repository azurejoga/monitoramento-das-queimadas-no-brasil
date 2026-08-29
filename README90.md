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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6f3f7833-c7c5-3eec-bfe1-366b0df942b1 | -3.4002 | -61.3276 | 2026-08-29 17:10:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| f15c28e6-6a5a-387d-a2b7-231c7fe00ba2 | -6.8386 | -59.4379 | 2026-08-29 17:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.7 |
| 107f2832-ae1e-3e1c-ad5c-077cb6e203dc | -8.2227 | -54.9613 | 2026-08-29 17:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 9ab287ae-654a-39ec-8a06-2ff2662e2846 | -12.91 | -45.89 | 2026-08-29 17:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 798ed140-2d9c-3236-a41a-3ae30268e02b | -12.94 | -45.9 | 2026-08-29 17:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| dfe6581b-a4af-3b4c-a9ca-d391df66eb30 | -11.53 | -45.51 | 2026-08-29 17:15:00 | MSG-03 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 30929de4-80ba-308b-a555-30d83ad92907 | -11.54 | -46.09 | 2026-08-29 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1e64a26c-0d1e-3b55-bd16-0bc6145f0b04 | -11.26 | -45.34 | 2026-08-29 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab39a42d-8862-37b3-be79-ef363a249bc6 | -11.23 | -45.33 | 2026-08-29 17:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef4323f0-64c0-3ca5-a3fd-a3f2c654f2f0 | -6.8598 | -58.9545 | 2026-08-29 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| a1dba680-40e9-309b-b97b-d990ebca9002 | -7.0041 | -59.5275 | 2026-08-29 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| e8612464-3b0e-3c8f-b61d-9d3f195761a9 | -6.6765 | -58.7492 | 2026-08-29 17:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f5c7a91d-9ba5-3d31-bcd0-c2995ebc3042 | -15.3654 | -53.7887 | 2026-08-29 17:20:00 | GOES-19 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 81.5 |
| c45bc40b-910d-3527-9084-b1226344575e | -6.7094 | -59.443 | 2026-08-29 17:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 4a987173-ed38-3036-bba6-cebc9dea9ad7 | -11.245 | -45.3037 | 2026-08-29 17:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 280.1 |
| 22f471d5-f165-37a4-b5e6-93a463dc094d | -8.6487 | -62.8376 | 2026-08-29 17:20:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 150.6 |
| 2616bab1-fed3-3995-8bf9-bfc711e79fcd | -11.1916 | -51.2708 | 2026-08-29 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 124.6 |
| 63388017-5814-3eb1-bd5b-e5d01055d930 | -11.2106 | -51.2688 | 2026-08-29 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 203.1 |
| ecb2e268-b724-3cb9-8110-cb8e24a6130c | -10.7649 | -50.6366 | 2026-08-29 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| a7b3729e-74c0-3f41-b465-870638019adc | -11.1939 | -53.9993 | 2026-08-29 17:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.8 |
| 8809ea97-e13f-328b-9189-145c0031eddd | -8.631 | -66.5473 | 2026-08-29 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 107.4 |
| 5fea856a-b506-339e-9615-43c0e8c1c45d | -8.2227 | -54.9613 | 2026-08-29 17:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| b9c73515-3982-3bfe-9340-f726a8139c8f | -8.9478 | -62.4084 | 2026-08-29 17:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 139.9 |
| 1d34eb8b-2c3a-3a70-b0d8-283d1b70ba9d | -8.6311 | -66.5287 | 2026-08-29 17:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.1 |
| b7945461-42c0-3b7b-be2d-761f3a4e24cf | -12.1902 | -50.5409 | 2026-08-29 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 162052b1-cb7c-3896-8409-307ee8471232 | -11.006 | -49.6461 | 2026-08-29 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 79.7 |
| 91896200-2007-3d6f-9050-a38ccaceed00 | -8.3718 | -62.697 | 2026-08-29 17:30:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 32173aaf-ce5a-3dd4-8433-d5c278d985f9 | -8.6487 | -62.8376 | 2026-08-29 17:30:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 171.8 |
| 3e0bc99f-edf3-3eb8-92a6-bf02e33c63ea | -8.9478 | -62.4084 | 2026-08-29 17:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 92.1 |
| d1b145b6-7249-3631-ac3d-f1618bdd4e73 | -9.0061 | -65.3813 | 2026-08-29 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 05447fa1-bbc3-38dc-909d-6bb368e679d1 | -20.941 | -57.5694 | 2026-08-29 17:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 74.9 |
| 1aa61e5a-dba9-3ba7-89da-acea7eaadbe3 | -9.1709 | -59.6374 | 2026-08-29 17:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| ecea5128-cc15-39f8-8297-c7845a9686b9 | -6.6765 | -58.7492 | 2026-08-29 17:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b286b34f-c2bf-3993-a7b9-945cc73e13b8 | -7.0812 | -42.2063 | 2026-08-29 17:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 113.8 |
| c0a89426-ab5f-3ca8-a03d-fb3b33718f64 | -8.9873 | -65.4379 | 2026-08-29 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 84.9 |
| 21bafe61-1d17-3ec8-8617-2a081bc15c82 | -10.4981 | -64.5005 | 2026-08-29 17:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 44.6 |
| b81b7c56-0d9d-3e82-9391-997b2e9f81dc | -7.0041 | -59.5275 | 2026-08-29 17:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 5ee5bcba-0ce8-3a7a-9d11-e018473a4437 | -14.2989 | -51.7072 | 2026-08-29 17:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 153.2 |
| 34195973-1b92-35de-ab88-a82b0db52813 | -11.2106 | -51.2688 | 2026-08-29 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 0244ce14-d4d0-3430-868d-f7b29e02cbbe | -10.4794 | -64.5012 | 2026-08-29 17:30:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 97ac2834-744a-3c38-b97c-8a4b0d745f61 | -11.0057 | -49.6677 | 2026-08-29 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 4955c88e-ddde-3a42-8ec4-f72bce838270 | -11.245 | -45.3037 | 2026-08-29 17:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 2b6d7979-6e77-312a-94a0-a41e20c12e48 | -8.1432 | -64.0053 | 2026-08-29 17:30:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 46e863bd-6fd9-3c58-8a2e-9a81e54636b8 | -7.1001 | -42.2044 | 2026-08-29 17:30:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.1 |
| 1b77fd0e-5a46-3e44-b361-bcc76fc10900 | -11.0247 | -49.6656 | 2026-08-29 17:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 97.5 |
| da2743fb-53d2-3cea-9a74-4c3d868ddf77 | -8.2227 | -54.9613 | 2026-08-29 17:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.8 |
| 7c42cf3a-fce3-3e7f-8c88-d93dbcb2d621 | -8.574 | -66.9569 | 2026-08-29 17:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 90.2 |
| a3296a3d-e24f-3bb4-a175-e8d7af959b4d | -14.3182 | -51.7046 | 2026-08-29 17:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 110.5 |
| 8792d81b-76ae-3004-a39a-8fdd84fb1fe9 | -8.6694 | -49.5369 | 2026-08-29 17:30:00 | GOES-19 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 28d83c51-4ed5-3006-a7f4-9de7a2fa2886 | -10.7649 | -50.6366 | 2026-08-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 2202f6c8-9aac-3da4-8c05-b9b6fc4f25a7 | -12.3232 | -50.5678 | 2026-08-29 17:40:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 37.2 |
| 3592e841-d6ad-399a-a914-8fba1b2d6d8f | -6.8015 | -59.4586 | 2026-08-29 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 3259d170-4deb-30ce-b0e5-a725c96fd1e1 | -10.3391 | -49.9762 | 2026-08-29 17:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| b3d74c7b-6211-3729-9c8b-cc7b76abb89f | -13.8378 | -54.0573 | 2026-08-29 17:40:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 85.7 |
| 39811048-8d75-3d6e-b7bc-bb1e51ca4e73 | -11.9081 | -55.8891 | 2026-08-29 17:40:00 | GOES-19 | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| c687bb23-f5e2-33f3-bdc1-7261a6e70088 | -20.9207 | -57.5723 | 2026-08-29 17:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 75.0 |
| b888f543-8cbe-39b9-86f0-db92a1049376 | -6.9872 | -59.2582 | 2026-08-29 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 6c48dca6-1257-3f29-870c-5df26c105897 | -11.1939 | -53.9993 | 2026-08-29 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 120.7 |
| d1c346db-2960-35e4-a47f-52d3a4cf63cb | -14.5627 | -52.077 | 2026-08-29 17:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 80dc8a31-de72-3afd-a448-0f5513e4d792 | -6.641 | -58.4987 | 2026-08-29 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 2bd4d17a-fa91-32ad-b2e4-d455d6264ade | -11.1729 | -51.2516 | 2026-08-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 51.5 |
| 7e7ec677-4fa6-3be6-8288-403e0a491995 | -8.6158 | -54.7541 | 2026-08-29 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 159578fe-2f1c-32af-8dd4-e70f02af0ae5 | -11.006 | -49.6461 | 2026-08-29 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 3ddd8430-69da-3f02-aecb-203423d18972 | -8.2227 | -54.9613 | 2026-08-29 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 2231aa51-1a55-36b0-ad13-b873d5d926ef | -9.025 | -70.7268 | 2026-08-29 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 689554eb-2ef8-369c-bb85-dbdb1eecb0c3 | -6.6541 | -59.4452 | 2026-08-29 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.0 |
| b55e2948-ebca-3af0-9db7-28cead56aae5 | -20.941 | -57.5694 | 2026-08-29 17:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 69.2 |
| 41c77b52-3614-3549-8990-2d919df29dcd | -8.2147 | -69.8582 | 2026-08-29 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 0e4e2cfa-9ef8-36cb-9e8a-ab58166644f5 | -11.0247 | -49.6656 | 2026-08-29 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 97.1 |
| c50cb16c-87b1-322c-a62d-3e644b844479 | -10.7603 | -53.9769 | 2026-08-29 17:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e3f316d7-7538-3167-8a4c-6eed942e4524 | -6.695 | -58.7291 | 2026-08-29 17:40:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 82.3 |
| c66daf02-0372-36ff-8cda-5b159fb4f0f3 | -8.8219 | -70.638 | 2026-08-29 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 7b43bff5-3675-3efd-b07f-da95d876b8fa | -6.4909 | -55.8967 | 2026-08-29 17:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 6256da55-57e1-39f5-9740-fa434d1289be | -6.9521 | -58.9506 | 2026-08-29 17:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| f223acde-1172-3429-afa9-f9360c127edd | -11.1726 | -51.2728 | 2026-08-29 17:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 101.5 |
| 7a8fbd9c-e266-3a38-83ad-4f23bae04b25 | -8.3717 | -62.716 | 2026-08-29 17:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 60.6 |
| f00855ef-56fe-368c-8637-4843d56bf0c8 | -6.8357 | -59.9571 | 2026-08-29 17:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 870e2f28-448e-3aae-9969-992a1e8b32f6 | 0.1914 | -60.5067 | 2026-08-29 17:40:00 | GOES-19 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 174.9 |
| ef641482-6604-3552-9488-90cd748d1097 | -8.6311 | -66.5287 | 2026-08-29 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| bb3fb30c-9d08-3d59-93a5-a37ac8e05e1d | -20.9414 | -57.5484 | 2026-08-29 17:40:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 73.4 |
| 3fffff26-1e54-3cb0-877a-bb5a4a45aeb1 | -8.6487 | -62.8376 | 2026-08-29 17:40:00 | GOES-19 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 175.3 |
| ff8e489e-312f-333f-9615-d16c753719fa | -8.6734 | -71.0433 | 2026-08-29 17:40:00 | GOES-19 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 1091bd83-4ae9-3aa5-9010-27d05c452fd7 | -8.7845 | -70.8586 | 2026-08-29 17:40:00 | GOES-19 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 49.5 |
| 2c3823d8-13bc-3c48-ac7e-825fa3418dfe | -8.574 | -66.9569 | 2026-08-29 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 102.7 |
| e6c1c14c-1984-35e5-acb3-4061e3f394fc | -8.2414 | -54.9601 | 2026-08-29 17:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 96.0 |
| 11a3ca29-030a-3656-9da3-c8646f9aab89 | -11.0057 | -49.6677 | 2026-08-29 17:40:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 62.4 |
| a695353c-5c19-38f5-80d8-208ef0894d72 | -9.0057 | -65.456 | 2026-08-29 17:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 158.5 |
| 083f90a5-f381-3781-8059-6818888cda5e | -3.4002 | -61.3276 | 2026-08-29 17:40:00 | GOES-19 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| fa2d8fb8-e2b8-3c2a-93d8-c25b219f5d34 | -8.1432 | -64.0053 | 2026-08-29 17:40:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 53.3 |
| 02b9c715-41cf-3b5c-9434-89839a598d9b | -7.0812 | -42.2063 | 2026-08-29 17:40:00 | GOES-19 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 93.4 |


