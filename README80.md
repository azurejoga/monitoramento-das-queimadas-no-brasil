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

## Dados Diários - Página 80

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b47c7b4-9409-351e-a2ea-4f2652bd1b43 | -9.16761 | -59.47172 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f21811a8-a59e-3827-bede-a0753b270846 | -8.66825 | -68.68896 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbc767d4-a56c-35ef-8e14-f839214cd70b | -9.1693 | -58.3082 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 034eee6d-9b0e-3963-8df4-2f3fb312c0a9 | -9.01965 | -65.69065 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e51d9e05-a41d-39ff-95e0-0c7d52d4d841 | -8.61278 | -62.59759 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 3389d9dd-97e4-3cb2-a6b6-8ca6bda507e9 | -15.32424 | -56.15972 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc11ef69-ee36-3224-a478-42d6240fd7fa | -8.61219 | -62.60122 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26a52e87-57e4-39ac-a1cb-8188321bb9f9 | -9.21893 | -59.61876 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a08c8c79-1958-3e02-829a-540c0c94a93b | -8.97789 | -63.39585 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c9fbb69-b696-3595-a47c-e91652079073 | -9.00728 | -63.63039 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f8f6836-dfd2-3cc9-b414-e504352cf806 | -8.67775 | -68.69067 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ce1e3c6b-df3f-3c82-a857-6c017f30b379 | -9.15395 | -59.44684 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| db1b5a2b-8eb2-3674-9f60-3bec8d977bf9 | -8.88607 | -62.43411 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 106f6d61-d3f3-3ef6-b00b-72d892e1fecd | -9.16946 | -59.59649 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28fe4091-1cda-3129-9760-5dcd91abd1eb | -9.52581 | -60.5405 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75c36fcb-ab90-3005-b524-3d143713f3ff | -8.61836 | -62.60596 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e4d4eaf-290f-3327-82c0-27c51707db84 | -9.14722 | -59.49126 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0ee6e9be-6b0c-3851-9e6a-1c5126e110df | -9.0107 | -65.71948 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8a656961-1c45-3ada-b377-4f5a9b1070d3 | -8.9164 | -62.41697 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b4b5259a-56a2-3c4c-9364-b75d1501c20c | -9.02319 | -65.71659 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 61f742c2-d43d-3a64-9862-dcb4ab4df01a | -9.16653 | -60.82154 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 4041021e-6398-31d4-99fa-21337a8f02fd | -9.03095 | -65.71799 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 62ce845e-a7a0-3c86-8042-76d346c4d545 | -9.1517 | -59.46168 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 746c6162-04ed-3080-adb1-4c7366d1e344 | -9.1614 | -59.48966 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c318fc71-029d-33b2-98f2-4846caf7d3b4 | -11.31492 | -47.85084 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e247845-4026-3ebc-b202-2c8ee05998a3 | -9.18926 | -59.62587 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42cefad7-cb0c-31ad-8cc2-0c0196dcf0d6 | -8.91408 | -62.4313 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9139e9ce-040d-310a-ac21-fb2517fc99d0 | -9.51631 | -60.51371 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8beb16b4-6fd9-3712-a48f-59de33dd275b | -9.20681 | -60.80285 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8eccb29d-2d2c-34cb-b4bd-47eeef72a80f | -22.60789 | -52.49482 | 2025-08-24 05:25:00 | NOAA-20 | EUCLIDES DA CUNHA PAULISTA | SÃO PAULO | Brasil | 3515350 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 0bfd4006-bd0e-3489-aaee-f00bc32674d3 | -9.93376 | -60.49577 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 41502232-e8ad-3e3a-8977-ffbf95d7f4ac | -9.19628 | -60.78327 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 449b022d-be15-3ee2-9ec5-fdb96a30183e | -9.15175 | -59.48439 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 38ce40a4-9237-3d1d-a6df-67ec45b1d725 | -9.13923 | -60.7352 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0f37987-7699-3925-9d69-e980c249781b | -8.13224 | -62.85939 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| adae1605-52e0-367a-a5c7-4be6796b6fd4 | -7.96753 | -63.07528 | 2025-08-24 05:25:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bb840572-36af-3392-b5f5-bcf5923dbbfc | -16.79827 | -51.35777 | 2025-08-24 05:25:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1cde905f-fb8c-3695-a2a7-be583b49dc60 | -9.51855 | -60.52129 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d0f84832-e826-3a0e-ae8a-72163e9a8fa3 | -9.03872 | -65.71932 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2a005ca6-8bde-30e5-b801-7813460de710 | -11.53669 | -51.91227 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94c6d413-b97f-35d2-8cea-e482c5574fb9 | -8.68378 | -62.87582 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2beaf362-5147-3db1-a552-c2ab6dace576 | -8.60031 | -62.61046 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3c91f79-4d82-382f-9d0b-a5617ca77be2 | -8.93699 | -62.43871 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2cc603e9-9d06-37dc-b61e-e0e3374d0248 | -9.2079 | -60.79586 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 584a5fd6-3400-3c75-b7ca-81c1895d78bb | -8.91343 | -60.72431 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5abdfdb8-ecdf-32b4-bae4-b080e1b88d46 | -8.14469 | -62.86905 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0e488b53-9f68-33cf-b26b-7f0c6f36ba31 | -9.1382 | -60.78514 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a98077cf-23e9-358f-9a57-11c23d6cb191 | -9.14773 | -59.46485 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7894efc8-3d18-39bd-acdd-db7afec7d71b | -8.61557 | -62.60177 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9936fd92-6776-3fb8-a107-b3dfc7d87595 | -9.14834 | -59.48386 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 171e6e8c-44be-321f-ab8e-51e2703411f0 | -9.02666 | -59.01636 | 2025-08-24 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 43394f22-ef43-32e8-9b02-7dd76b15e158 | -11.5242 | -51.92166 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 732da469-9e20-3028-883a-abbf8f1bfa57 | -8.90621 | -62.4374 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 513d2536-fd5e-3752-9afb-c1cb34d26108 | -8.90227 | -62.44043 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a4146b5-c625-3895-b897-7bb5efed3258 | -9.15342 | -59.47333 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5f63b504-5f4c-3c03-ad86-968e41a275df | -14.79354 | -59.63051 | 2025-08-24 05:25:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 055648b3-6103-379f-9cc6-14ff4a908fac | -9.15398 | -59.46962 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| d2a94355-76f9-33c7-869c-c59b39a58ff5 | -9.95898 | -60.17789 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8478aeb-58ce-3005-bc2f-12eadfaee23a | -9.94441 | -60.16086 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e79e2dc-89c1-39fc-9bf6-1de1b5918851 | -9.01628 | -65.71028 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 0e7584e0-b20e-3ba6-9b30-6873324ccbff | -20.33897 | -51.70055 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 015309c1-b4fb-3e89-bf12-ffed319a9d92 | -8.61499 | -62.6054 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e7034a41-06aa-3ff4-94e2-2038763ff597 | -8.89892 | -62.43989 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b46593ab-9ff8-37b0-a2a1-976c6e41dba2 | -9.96123 | -60.18561 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 17d0b923-a7ff-3ba1-b6a7-dbcedb344208 | -8.66359 | -63.85006 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c596cb53-ff71-32a5-9133-39570b34eaca | -9.6493 | -59.6424 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6530bcd6-05f7-3623-9567-13a581aa77a7 | -9.25513 | -59.63185 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b25dd874-8d85-364d-93c9-49eb0952ef48 | -9.26671 | -61.02687 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3d0a016f-70cd-32d9-b660-88ca4c9d38e4 | -10.34559 | -58.60117 | 2025-08-24 05:25:00 | NOAA-20 | JURUENA | MATO GROSSO | Brasil | 5105176 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ae0339f0-0d91-3618-a1f2-2a6569b21a5e | -9.15002 | -59.47279 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c63bb99c-d87e-38a5-8db6-650f85f54c2b | -8.98795 | -63.63916 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 285b4259-90b5-3b37-89cf-f1c8925c1fe5 | -9.13321 | -60.77364 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d932d6ab-ec17-38f1-aef5-6b63859414f7 | -9.14894 | -59.50288 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 81f9db1b-50ef-3da6-a858-2a43ec84bd74 | -8.62895 | -62.62635 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26a86cf1-b9e4-3be1-b474-ae00f401adca | -9.1907 | -64.5537 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e5d6fbd7-12cd-36b5-98bb-c72bf21aa825 | -8.63107 | -63.65065 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 11886c8b-c689-3f47-bcd0-bf557739a7be | -11.18214 | -55.02545 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8faa3053-7734-396e-93d2-2f506460dc4b | -9.0124 | -65.70961 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| d9884bc7-9011-33b4-aac3-4d9c1464593c | -9.16992 | -58.30409 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dcedb054-4af1-3176-981c-c660a0841b96 | -9.20015 | -60.7803 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a1aa85bc-f303-31d8-bafe-df2ebb6d7891 | -10.10472 | -57.76967 | 2025-08-24 05:25:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6496b6f0-68b9-3aec-94f8-4b5a6d488058 | -8.96781 | -61.67208 | 2025-08-24 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57bfa9cd-9e91-36d6-808f-f2aa6cafc777 | -9.19259 | -59.46801 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b477aec-2b89-3a4a-810a-c0f4ce899ab5 | -11.53715 | -51.90861 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 451176d6-7e29-3540-b12f-85b697bf6bec | -9.15515 | -59.48492 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| af144f96-18e6-3566-88d2-fef22c9bb02b | -9.50977 | -60.55603 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| aa6c9cbe-f6db-3329-b2f2-5911c5cbe9d1 | -8.89453 | -62.42445 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cab213-d31e-390f-affe-38814fe59dc8 | -9.18293 | -59.46273 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f5e3992-e845-3eef-81cb-7923b447df33 | -22.04819 | -53.8294 | 2025-08-24 05:25:00 | NOAA-20 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| a6723aaa-9ff6-386d-a8bb-59d00f5b5b61 | -8.91628 | -62.43902 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47bf2114-de3d-304c-9ccb-bae2886e295b | -9.0033 | -65.69286 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| dd6ca7cc-6633-3ec3-a095-7ac10d4c5fd9 | -9.21926 | -59.75351 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bdb6f71d-35b9-395b-b302-b2a91ea857bb | -9.19905 | -60.78729 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 708274c1-0f0b-3761-996e-c62fec97689e | -9.00937 | -65.70396 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| bf34e41f-aa92-3168-8c53-7f394aa762ac | -8.63233 | -62.6269 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48801760-9b10-31bf-b977-7631b142cfce | -9.15631 | -59.50024 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b492cb7-bfb2-3b50-95be-238b01be0af8 | -9.15575 | -59.50393 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d77f16-6457-32fd-940c-315ea19ea90c | -9.15623 | -59.45478 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8dcb89a5-15e5-3cff-822a-8600040a4856 | -9.00198 | -65.69518 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fe0f7669-f865-3d98-a5c8-412bff6b13b3 | -9.07992 | -66.06567 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |


[Clique aqui para ver as próximas entradas](README81.md)
