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
| 1a0d97f5-d0ea-3cc8-866f-0ccbafdff5d6 | -5.06269 | -56.07282 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f50823d-a0ab-3130-828c-2e7c91610642 | -5.51037 | -60.13203 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 706a494a-1022-323a-8ccd-67f2e686e520 | -5.48958 | -60.13475 | 2025-09-06 05:55:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c35ca84c-523b-30a5-9d77-261ec8fb2bc9 | -5.00781 | -56.03767 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f40f2c3-b1e9-3988-900b-05cd16c95552 | -5.78655 | -57.55838 | 2025-09-06 05:55:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6185c913-efad-3029-9a82-41d34a162387 | -5.10564 | -56.14408 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4dee1f43-679f-33d4-b1fd-126bc7d13634 | -5.00837 | -56.03793 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d364576e-12c9-3cb6-8ff9-fbde0c5d25f8 | -5.06894 | -56.07299 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 170aecf7-266b-3967-8942-d37f8a73beaa | -5.06987 | -56.06857 | 2025-09-06 05:55:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb9b5a3c-42fd-347e-8a12-25e12d9ec269 | -9.24703 | -57.07301 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5cd058e-287b-3ee9-9950-db45b06b1af0 | -10.16669 | -61.14075 | 2025-09-06 05:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c9855c95-f37c-3127-8fc4-3681d204a2da | -8.49154 | -62.70423 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1d6aa619-1e12-3397-8841-0f09b27ca5e9 | -8.47806 | -62.64179 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bcc55759-662f-349e-adbf-53e4e282f308 | -6.86988 | -58.93179 | 2025-09-06 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e2f9f801-e1b3-3d24-b91f-2f84263a7c35 | -9.23998 | -57.07712 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7053c657-cdb3-30e4-a3ad-b4cd2b015dc6 | -12.35552 | -63.64643 | 2025-09-06 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d891f76-fce1-342a-af0b-df0589de0613 | -12.35401 | -63.64801 | 2025-09-06 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f86098b4-7e73-3f0e-8890-bbeb4f685d64 | -8.48778 | -62.69933 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f9da5480-4330-376f-a7c4-6f4da6c6fd7c | -9.20522 | -57.0939 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f82deb0-dca5-3323-8405-632f130cce4e | -9.06827 | -62.35285 | 2025-09-06 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1305d124-c51b-33de-bc1c-e39248615399 | -10.14139 | -55.15879 | 2025-09-06 05:57:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 9fdbc324-1309-3eaf-a132-eee733302498 | -13.04548 | -56.86023 | 2025-09-06 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53c99047-b806-3dee-afd6-c579aba406d7 | -11.48018 | -55.55378 | 2025-09-06 05:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7affbfa5-92a0-38f6-a9e7-279ad7f00437 | -6.86938 | -58.9354 | 2025-09-06 05:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4397e07-ef42-34a2-8fe7-531431facc65 | -9.99326 | -60.01763 | 2025-09-06 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cb9bd1b1-6466-3631-ad4e-3e7316a078e6 | -9.07279 | -62.35351 | 2025-09-06 05:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0fc27fe9-6097-3c69-91c6-38ea42eedef1 | -13.03869 | -56.8592 | 2025-09-06 05:57:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 38bbce38-3940-3fb0-b5a2-d6594793bc4e | -9.21937 | -57.08514 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 90e8a375-4875-37b0-92b8-d6b6c8021e06 | -9.24638 | -57.07814 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| aa5e04b9-ab10-3489-9fb6-e24c2a90054f | -9.25278 | -57.08163 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e2c3c12-c959-3d86-8f65-077c3c0ed0fb | -8.47722 | -62.71076 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5cf1c77a-2377-3f3c-a499-d31058380569 | -9.9937 | -60.01424 | 2025-09-06 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dc593c67-4efb-3501-ad3d-3c06200d325e | -8.47746 | -62.64604 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51f1d722-b544-3686-96b2-5d0acd99973b | -8.48159 | -62.7114 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c27df2e-2873-3ed8-b4ef-17e43df279f8 | -9.2528 | -57.07912 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ef79512-d642-3923-adae-237632e273fe | -8.48717 | -62.70359 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5527734c-6c34-3a05-9a69-b7d0307c6468 | -9.99907 | -60.01498 | 2025-09-06 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| de97a287-09c5-3604-bf77-ab9ca29e9fa7 | -9.21873 | -57.09027 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6287bfce-2ec7-3407-85fe-899105728fbf | -10.41572 | -60.74621 | 2025-09-06 05:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cc691032-0247-3e3e-b94a-44912ab907be | -8.47307 | -62.6454 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3433b1f1-e2ee-3039-b716-d2edb3cd515c | -8.47782 | -62.70654 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12c00a73-4117-37b6-a1da-68dad4186bdd | -11.48101 | -55.54665 | 2025-09-06 05:57:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65a0b62e-ed69-3551-97de-b6366d101dec | -9.24062 | -57.07201 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a030152f-b8d5-377e-941c-1d788fb73040 | -9.23353 | -57.07643 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64077010-e6aa-39fc-9277-27a9784ac5fd | -8.48219 | -62.70718 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2693779-4108-309f-9c73-b2a60337da5b | -8.47842 | -62.70231 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0fa206be-d7ef-3655-83cc-e47c9dfe5522 | -9.24767 | -57.068 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 049b38c7-5d08-3fa0-9e00-2c3cc902dd60 | -9.23225 | -57.08656 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f2f2a29a-9a8c-35f7-aa37-dc004115abf6 | -9.21164 | -57.09476 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be55cd99-e9ae-3e3b-9381-4dc1b652c819 | -8.4828 | -62.70295 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 75cbb20d-b1cf-3ed0-9dd2-f44a6ea8b930 | -8.48656 | -62.70782 | 2025-09-06 05:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1e14dc4c-909e-337b-9259-ca8d1df072e5 | -12.35458 | -63.64383 | 2025-09-06 05:57:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b44f1e4-a2d4-345b-b53a-0c7c1d936f4a | -9.23289 | -57.08152 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70112be0-86ea-3e21-9e44-ad59e6a2fc24 | -9.21227 | -57.08976 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b004bbd0-8d54-3261-95e0-393b9aa2b137 | -9.25337 | -57.07668 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6fb9787a-2718-3cef-89f0-01845ad69ba5 | -9.25396 | -57.07183 | 2025-09-06 05:57:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3f3f3712-6543-3dc0-9d4f-197af8586536 | -10.42081 | -60.74735 | 2025-09-06 05:57:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eb511465-6b0b-3d4a-82a7-86879966b7ce | -9.99413 | -60.01085 | 2025-09-06 05:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64db6ba6-57e0-3569-a54a-69e0a1d036a1 | -19.89713 | -57.92705 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 750a6913-1eb2-359f-8426-37060b8abc5c | -14.33799 | -60.32726 | 2025-09-06 05:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e55c36ac-1d9e-3320-9150-9c73c8c2576b | -19.88451 | -57.9178 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ebc39f23-8bdd-3965-ac6c-d9ecbeaf0ddd | -14.34394 | -60.32489 | 2025-09-06 05:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e44a2af9-207e-30da-98eb-99dc30ffdcb4 | -19.80615 | -57.94334 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 58c8b639-7452-3840-9849-e5746c6a243b | -19.91036 | -57.93492 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 60817b46-6b46-36a3-8803-f1ab29239119 | -19.89139 | -57.91843 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 777ca1bc-57c7-33fe-9621-b4bbe8c531dd | -19.90401 | -57.92772 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 1e529bcb-e71b-32d1-9334-2d4b98597a19 | -19.81248 | -57.95052 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 60f74888-faff-3117-b3b3-edd3f397393d | -14.33852 | -60.32275 | 2025-09-06 05:59:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fcd24c39-9a72-3f1c-805b-c1a3646c39b7 | -19.89766 | -57.92049 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bc764d7b-0feb-3765-afcc-01f49dab5cd2 | -19.89078 | -57.91983 | 2025-09-06 05:59:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8cae165a-fa8c-355f-877a-3b8b17e8e556 | -10.6128 | -44.3284 | 2025-09-06 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 168.8 |
| b3ca2cf9-baa8-3db8-b702-3d5136d7c449 | -10.5937 | -44.331 | 2025-09-06 06:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| bf6fe803-39a2-3a73-a682-6321a1c96659 | -10.6128 | -44.3284 | 2025-09-06 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 156.7 |
| aeca6427-333f-303d-9837-44a4b1fbd1bc | -10.5937 | -44.331 | 2025-09-06 06:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 85.1 |
| ee48a41a-cec1-3308-8886-c0ec96f256f3 | -12.41921 | -63.90324 | 2025-09-06 06:20:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2639aff6-b020-3490-a1b7-11e5401c12ff | -10.6131 | -44.3051 | 2025-09-06 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 3b51d1e3-dd9f-3bfb-a8d1-4f143af39dd8 | -10.5937 | -44.331 | 2025-09-06 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| eaa06ce0-408d-367c-b716-a7d87cbc2869 | -10.6128 | -44.3284 | 2025-09-06 06:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 144.8 |
| c81396c4-eb4a-3d7e-8bfa-af86e97bd071 | -9.0951 | -47.0093 | 2025-09-06 06:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| b3ce51f2-073e-3a9b-9acc-ef45c676a5f8 | -10.6128 | -44.3284 | 2025-09-06 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 177.6 |
| a0764f59-9a95-3266-8da5-6dcb5f056827 | -10.5937 | -44.331 | 2025-09-06 06:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 0b0288cb-9177-314c-8167-d24111410e90 | -10.6131 | -44.3051 | 2025-09-06 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| dc8fc23d-018a-399b-bc39-ef13e1a90752 | -10.6128 | -44.3284 | 2025-09-06 06:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.4 |
| 0774b588-1b8f-3801-9dea-727de9077075 | -9.0951 | -47.0093 | 2025-09-06 06:50:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f618bf8c-f957-357f-8ec2-ed8a2dc87759 | -10.6128 | -44.3284 | 2025-09-06 07:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 141.8 |
| 2e8743da-c974-3422-baa3-409d5f6879de | -9.0951 | -47.0093 | 2025-09-06 07:00:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 67223de5-c2b8-3bbb-9bb6-fce1577e6990 | -10.6131 | -44.3051 | 2025-09-06 07:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 49.6 |
| ea52df60-6eec-3205-ba6a-7bc05028a2ff | -10.6131 | -44.3051 | 2025-09-06 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.8 |
| d49b6165-bd4a-3ae5-b2b6-9868d3210997 | -9.0951 | -47.0093 | 2025-09-06 07:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 68.1 |
| e588c1ec-baed-3960-a69a-86b38f63efbe | -10.5937 | -44.331 | 2025-09-06 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 53.5 |
| a942b089-a084-377e-8ce5-544062bb1410 | -10.6128 | -44.3284 | 2025-09-06 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 42f967bd-ed2b-3f4d-acc8-7441732d3f3a | -10.5937 | -44.331 | 2025-09-06 07:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 3f025345-ea24-389e-b66c-96d16ca7aea9 | -10.6128 | -44.3284 | 2025-09-06 07:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 621d82d8-f506-3cf0-8b64-0cdf2c18db4d | -10.6128 | -44.3284 | 2025-09-06 07:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 94d6a06b-4eeb-39e2-90cf-ab413471dc37 | -10.6131 | -44.3051 | 2025-09-06 07:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 51.2 |
| 5a8216a9-9608-3584-bd2d-0f43e852a0d5 | -10.3327 | -46.4225 | 2025-09-06 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| ed413fe9-639f-3595-933f-059142441887 | -9.0951 | -47.0093 | 2025-09-06 07:40:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.9 |
| b5cff529-defc-393d-964f-fa6aba74cedf | -10.5937 | -44.331 | 2025-09-06 07:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 73.0 |
| a4374904-fb9f-397f-8851-b34e0fe88592 | -10.6128 | -44.3284 | 2025-09-06 07:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 100.3 |
| b2381a50-3847-3631-b729-044dd7231ffa | -10.3137 | -46.4248 | 2025-09-06 07:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |


[Clique aqui para ver as próximas entradas](README87.md)
