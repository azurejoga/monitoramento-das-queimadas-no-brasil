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

## Dados Diários - Página 36

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 98276c18-138a-361c-8f63-5def85f39796 | -9.03463 | -59.76414 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6729ab71-c55d-3cb6-86b1-7a998fd1dd20 | -7.48056 | -68.33682 | 2025-08-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ee2027ac-8326-3abe-a071-efea21d146df | -8.92468 | -60.76556 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d195ddd-86a2-36b4-bc6d-98b55b739125 | -8.93377 | -60.73395 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4999699d-3c0a-3f4d-a5e8-f6eecc50d322 | -9.37877 | -61.52965 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 292ec415-e395-3da3-814c-d3111a30a304 | -7.1434 | -60.13107 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 78bd2d59-d952-3329-b2d5-c66ac94dd39e | -9.88853 | -58.56863 | 2025-08-12 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34ea16fa-aa97-3b80-b411-b65d29977345 | -8.5675 | -54.71896 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 49d6bc0d-6e1a-3aa6-94c8-142b8196d00d | -8.93898 | -60.72992 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| d5f8be0b-4ebf-31f7-9d3e-4f6fe913a20a | -9.92244 | -60.48096 | 2025-08-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69ffd060-f47e-327e-863f-8ca67c61946f | -6.97511 | -59.28104 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 475de8bc-43f5-36f2-ba38-1efa72833911 | -8.93443 | -60.72932 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 26.7 |
| 95f9c3e9-2302-33da-a1a4-e1a282ddd91e | -8.56817 | -54.69069 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd71c08a-bab6-38f2-9766-a9fb2f41711b | -9.93184 | -60.48215 | 2025-08-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60bbe3d-9313-328d-bda1-cb8355257cdc | -8.92014 | -60.76498 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8aaabe3-a2aa-3506-b3a1-f1cce95c5a22 | -8.57412 | -54.6975 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a93d629f-ad46-3d67-a289-d9f698f31e55 | -7.1263 | -60.11861 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6775c0ae-8c68-3219-93a5-65de50aab6f2 | -8.92922 | -60.73334 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bdb58d41-9bf7-393f-84a9-ce4508cb9456 | -6.96456 | -59.28514 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 19a28d8c-188a-3b42-8723-58acc82dbef0 | -8.56227 | -54.70589 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1df1b88b-7e6d-3b42-8d1f-a02fc36af9b4 | -7.07888 | -59.20145 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48aaf2ca-d710-3e06-81c3-ce323a69f6a8 | -8.55922 | -54.67467 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 26d762e9-4b36-3880-8368-3203b0329f96 | -6.96534 | -59.27968 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| aff46acf-09fe-36eb-8a2d-3762d519f374 | -8.56662 | -54.70275 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 78d6b10f-77d0-3824-8b5b-a68af93b5a2b | -9.38197 | -61.53862 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c1b1ec1b-cd28-36db-8026-663f1b05f8a6 | -7.07318 | -59.20631 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3edcd560-d681-3f88-af61-59b680b90f53 | -9.89051 | -58.568 | 2025-08-12 05:48:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 56707b30-7889-317c-9d5f-cb81039413cf | -8.5712 | -54.68863 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7dc2a646-e024-30ee-b243-f5bdec7b3479 | -9.47543 | -57.84111 | 2025-08-12 05:48:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 416a71df-2865-3221-bca4-40dbfa763043 | -8.92988 | -60.76153 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d7037f5-0da3-3c43-a049-d1a45ebe30fd | -8.56428 | -54.72092 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bc210d2c-3628-38af-bcfd-c6216b7db66d | -9.19061 | -59.66416 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a6c08723-488f-3bc1-8641-b56e14429461 | -7.07395 | -59.20086 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b3019cd9-1d64-39b9-9d1c-edb065b4e3c4 | -9.38634 | -61.52809 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 81aecc33-6d22-35b7-9a4c-9bf8d709d355 | -7.06409 | -59.19965 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 77451135-ba96-3ffc-8701-de95b4c92d86 | -8.56145 | -54.68982 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4f8d4cf4-5289-303b-962c-16fab5c9fd19 | -8.57772 | -54.72251 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 5054d3cc-ac8d-3440-9331-0a55be9e5cda | -9.37216 | -61.53454 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e9e91737-8658-3551-8102-8a2dcb826867 | -8.5638 | -54.67141 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| deb2f6b2-814e-3c9f-b9cc-352ec6c8b1c0 | -5.89055 | -57.74638 | 2025-08-12 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b69f6adb-ebdc-375a-a5a2-c284b9c543ae | -8.571 | -54.72178 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ef16734d-88c5-3d7b-ad90-51605f99fdcf | -9.37764 | -61.538 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db41f098-45b1-3953-b7fe-78aaa3d5b697 | -8.96211 | -68.79781 | 2025-08-12 05:48:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 097a1357-554a-32cd-9b36-6bb763174d13 | -9.37708 | -61.53099 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f577d582-dc5a-3f9b-b398-13aa20c9d594 | -8.57334 | -54.70356 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5642a370-6af0-3795-b0b9-f0f59639d289 | -8.55996 | -54.66852 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cf9af491-a656-3ec1-a996-1eb4902878a7 | -8.56677 | -54.72497 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 4d1686bd-fa36-3018-8888-18264fc096b6 | -8.56584 | -54.70879 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c401c900-68c2-381a-8480-bc6628647b70 | -9.92714 | -60.48155 | 2025-08-12 05:48:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1b02f307-ae45-3f1b-b3d8-dfb6c7104bf6 | -9.19554 | -59.66471 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 26eacf13-ea2c-319e-a5a6-be01af44c30f | -7.13809 | -60.13532 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 5b0f5d8f-4cc2-34bb-ac83-fd456bc05c96 | -6.97432 | -59.28654 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 96a7dcd6-0c1f-31dc-a550-f561b8397b70 | -9.38201 | -61.52746 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cba4deb5-73bf-3190-8f57-6e7ec8b4af82 | -8.72331 | -63.14144 | 2025-08-12 05:48:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 607663d8-822c-3551-878d-48767335879d | -5.88521 | -57.74563 | 2025-08-12 05:48:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c3821e6-34a6-386a-92cf-baef78ffde08 | -7.14477 | -60.12135 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 30b7e6ac-890c-383a-8e86-f2e4d44e192f | -8.95263 | -68.50069 | 2025-08-12 05:48:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b58d595-5806-3b00-8e83-39f81d0c0cb6 | -7.48334 | -68.34091 | 2025-08-12 05:48:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50e865aa-6940-3022-a5f8-65e3e839cbb1 | -6.69308 | -59.14089 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| af8ffbd5-e4ab-319f-a7e9-abbbdf50b261 | -9.39067 | -61.52873 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fcdd5c5d-4c3f-318b-8c56-aabff12dc0d8 | -9.38311 | -61.53028 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 437741b7-1ccf-3f8d-b286-05a15e426484 | -8.56895 | -54.68455 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 49a510eb-3649-37c9-be1c-73645b2767d3 | -8.57571 | -54.70758 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9c34fa98-1a70-36e3-b564-9707ce6b236b | -7.13024 | -60.12418 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7ccabebe-d77a-3936-bd3b-a2037811ce0d | -6.97921 | -59.2872 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 97cc1f6f-983e-3906-85d8-405404bcb335 | -6.96867 | -59.2913 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| caa38423-416a-3505-9800-0d7d5e3fd570 | -8.92533 | -60.76094 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26b99768-dadd-35b7-8989-95af68051c94 | -8.5785 | -54.71649 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 40b8b799-d47e-3889-a8c3-e1b91f793961 | -8.56068 | -54.69581 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 202b5f1c-4ec3-3cb7-a31b-e4a9aff372e0 | -9.37649 | -61.53516 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 17ca554e-075c-35e7-b25b-d28b9cc62912 | -7.12889 | -60.13385 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| fda36d20-c833-31be-a710-ad5070381992 | -8.57646 | -54.70147 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8960e285-1a30-3563-ba36-f8253bd45647 | -6.96944 | -59.28585 | 2025-08-12 05:48:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bc91eb35-51b7-383c-82d4-7088923666ad | -10.35054 | -57.60672 | 2025-08-12 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 96b97701-8115-31cc-9fc4-6737fe11ac85 | -8.5608 | -54.71799 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bb046501-3940-3ba8-8c50-72066d65346f | -9.38367 | -61.52611 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cf38860-f8db-3b80-a566-c8033a9237b2 | -8.56739 | -54.69676 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| db2720b0-491a-3602-8f0e-8ab433d5e14f | -8.57177 | -54.71579 | 2025-08-12 05:48:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e021c766-0c09-3735-aafc-62d54ca6b1b2 | -9.37768 | -61.52684 | 2025-08-12 05:48:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 478e165a-2bab-3d5e-b545-0a02c10f721e | -10.35102 | -57.60277 | 2025-08-12 05:48:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a6437ce-05ea-3ee8-b517-8ba60dd16e84 | -16.3153 | -52.9201 | 2025-08-12 05:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| 8a5bb8ea-d550-3344-be03-0fac771bda84 | -6.5856 | -44.564 | 2025-08-12 05:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 8df52887-f49e-3787-8446-bea679ac6b4a | -8.9401 | -60.7288 | 2025-08-12 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 4cff79f5-ba4e-3662-bbb0-2b31d8801c72 | -17.6549 | -46.6757 | 2025-08-12 05:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 115.1 |
| d25a2eae-7a89-3fa6-8c4b-272daa0f818f | -9.723 | -49.4806 | 2025-08-12 05:50:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 97e53717-72cb-32c2-acb5-f772fcbeb2c1 | -13.3619 | -50.2423 | 2025-08-12 05:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 52.4 |
| dead845c-e0b6-3e27-a9bf-d4d4556e2464 | -12.5742 | -47.0006 | 2025-08-12 05:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 73.7 |
| 894d56a9-95ac-391c-98f6-fed58a83cabd | -17.6544 | -46.699 | 2025-08-12 05:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 56.1 |
| 53992450-43e0-31bc-aca7-6c306e319f47 | -16.2957 | -52.923 | 2025-08-12 05:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| f7d3cc6f-9fa3-321a-994b-254843d85ab1 | -16.2961 | -52.9016 | 2025-08-12 05:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 48.8 |
| 91370abb-b0bf-3dcf-8246-1bcebfcbe298 | -13.3427 | -50.2448 | 2025-08-12 05:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 0ee676dc-70d0-3f9c-85e1-6ad0babb14a2 | -3.9684 | -47.8901 | 2025-08-12 05:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 65c64742-7e37-3e6a-a72a-99cb4f53a188 | -10.62918 | -65.00707 | 2025-08-12 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ca9e9b4-f096-38fd-ac8c-08183b2718bf | -9.32088 | -68.32185 | 2025-08-12 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7ab4e128-0f9e-3a43-974e-395714d26599 | -9.32144 | -68.31833 | 2025-08-12 05:50:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 14e6f751-2208-36d6-a992-5687d3777012 | -13.07103 | -56.84925 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f67d9c36-f979-3b42-9669-81c1cc6ec449 | -13.05913 | -56.84293 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a933fd5f-8c3d-3f65-be27-2422530cbce0 | -13.06383 | -56.84367 | 2025-08-12 05:50:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d25cd263-99eb-36fb-acde-50c1c1aa5ebe | -10.62562 | -65.00651 | 2025-08-12 05:50:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d41403-5009-3d7a-bd77-6dcbb65b360e | -10.99523 | -68.77412 | 2025-08-12 05:50:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |


[Clique aqui para ver as próximas entradas](README37.md)
