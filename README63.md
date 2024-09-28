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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 51beab57-3d78-3910-ab9b-208ba00f6546 | -19.61131 | -43.88223 | 2024-09-28 04:23:00 | NOAA-21 | LAGOA SANTA | MINAS GERAIS | Brasil | 3137601 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e3278340-705f-3310-8918-28e75d216f82 | -19.53948 | -44.07746 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3211ce48-79b5-3abd-87b8-deb5f181c324 | -19.52171 | -44.09821 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bc499b6f-bad0-3634-88fd-a793e7434570 | -19.51805 | -44.09766 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86545ba4-bd38-37bb-9f17-728ea2ef1513 | -19.51743 | -44.10222 | 2024-09-28 04:23:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e96693ff-1543-3b49-8e39-f3ebea5dda2c | -20.32288 | -43.73521 | 2024-09-28 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ba8d4747-29df-3185-8e6f-fd1a8bcc8059 | -20.1778 | -43.51989 | 2024-09-28 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 8fef9ac2-d133-31a9-a66f-437fc7f85510 | -20.15173 | -43.51152 | 2024-09-28 04:23:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 1f7d7080-2e33-3fc9-9756-610c109c6aff | -19.98488 | -43.52042 | 2024-09-28 04:23:00 | NOAA-21 | BARÃO DE COCAIS | MINAS GERAIS | Brasil | 3105400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 58e0804d-01d4-3cda-ae2d-3fd3b25f554f | -19.95764 | -44.12879 | 2024-09-28 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 96797ab4-7e78-3d46-ba3c-0007f7922ee1 | -19.92321 | -43.77884 | 2024-09-28 04:23:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 391ec3c7-72db-36ea-81c6-a5f571d6099a | -20.50255 | -43.63036 | 2024-09-28 04:23:00 | NOAA-21 | OURO BRANCO | MINAS GERAIS | Brasil | 3145901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 9593ae4d-f2d2-3657-aed5-b0b97885ea97 | -22.11581 | -44.71574 | 2024-09-28 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| b0809597-d82e-3bac-91a1-9823dc510e2a | -22.11519 | -44.72053 | 2024-09-28 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| e4d82fd9-a099-3f18-9c05-ad90b3d9c573 | -22.11153 | -44.71998 | 2024-09-28 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4b04b5ce-ec05-3ce9-8fd5-f4d70badfb68 | -22.09959 | -44.72491 | 2024-09-28 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| da398ae7-b6ed-3d0b-8e70-487226a0d130 | -22.09945 | -44.72672 | 2024-09-28 04:23:00 | NOAA-21 | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 583766ab-6627-385f-8a31-9740087082b6 | -21.89875 | -45.23727 | 2024-09-28 04:23:00 | NOAA-21 | CAMBUQUIRA | MINAS GERAIS | Brasil | 3110707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7d5897b4-ae28-351f-9399-fd7524c35aac | -21.19671 | -44.93951 | 2024-09-28 04:23:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 216dec20-aca0-378f-8130-59f5d2b4d1a7 | -22.39903 | -45.53239 | 2024-09-28 04:23:00 | NOAA-21 | PIRANGUINHO | MINAS GERAIS | Brasil | 3151008 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c4655c47-69c4-3a44-9d8c-7d980a41ab5a | -17.84934 | -45.8987 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 77d2adf5-5f24-3d91-96d2-2347b7952c12 | -17.84654 | -45.89442 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 6c2d48c2-8d3b-3f2e-b61c-adf692a7c80c | -17.84598 | -45.89814 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 33.3 |
| b5473e37-8fbb-3814-b263-20268b8a66b9 | -17.84318 | -45.89387 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 53417ce3-f66d-366d-92e7-36d76697e58a | -17.84262 | -45.89759 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c553e227-e751-3a83-b75e-bf48c3af6641 | -17.83982 | -45.89331 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 73e0e0c8-b806-343d-90d3-826db9326d2a | -17.83926 | -45.89703 | 2024-09-28 04:23:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2373fcb2-188f-36e9-a270-1c9918fcd4ce | -17.77516 | -44.58821 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9a3ca79a-8d09-39d3-a58f-5e00990a232c | -17.77164 | -44.58768 | 2024-09-28 04:23:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a56e971-4599-3cd5-8840-49663797eaa5 | -17.04347 | -45.70544 | 2024-09-28 04:23:00 | NOAA-21 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da31f6a0-28bc-3476-ab94-54b6fb7debac | -19.28766 | -45.99997 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GOTARDO | MINAS GERAIS | Brasil | 3162104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44005549-bf71-31fa-b343-0763998069b3 | -19.04099 | -45.91804 | 2024-09-28 04:23:00 | NOAA-21 | TIROS | MINAS GERAIS | Brasil | 3168903 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d459c1e3-2dc6-3612-b219-f6137d7cc84e | -18.34165 | -45.07258 | 2024-09-28 04:23:00 | NOAA-21 | TRÊS MARIAS | MINAS GERAIS | Brasil | 3169356 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 890def1c-2f28-3ef9-8255-89f09547e8c3 | -20.56928 | -46.26247 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63713305-680b-3f1a-b097-41ce266310df | -20.56649 | -46.2579 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec934e56-c2ad-3299-b264-8adc54ee5dac | -20.56591 | -46.26183 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7249c891-84a2-3c8f-9ab2-8fcec1e54b2e | -20.56311 | -46.2573 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a90f8f8d-959a-349c-bba5-98a263ffaed9 | -20.56254 | -46.2612 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1fc71365-b831-3bde-83bb-b3f075058179 | -20.56196 | -46.26511 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2cc6df61-8a2a-398c-8ce6-baded56cd5e8 | -20.56032 | -46.25274 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0a60ed06-dc32-3181-8129-e2e7305a6f92 | -20.55974 | -46.25665 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 5de12135-00e8-385d-9576-2961ea54fff2 | -20.55917 | -46.26054 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b4c8b34e-647e-38d6-8c68-dc8728bd7468 | -20.55637 | -46.25599 | 2024-09-28 04:23:00 | NOAA-21 | CAPITÓLIO | MINAS GERAIS | Brasil | 3112802 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4cc19a48-319e-3e61-a293-e282edc75c25 | -20.32051 | -46.19454 | 2024-09-28 04:23:00 | NOAA-21 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c62857a5-11b4-3c7f-a605-0d051931ccc9 | -19.63717 | -46.12948 | 2024-09-28 04:23:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 38cfda07-f1f2-3776-bb4d-68c890d737aa | -19.57843 | -46.12012 | 2024-09-28 04:23:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 73891ae2-ce8e-3b89-8dd2-4d80efb13c7d | -19.57506 | -46.11955 | 2024-09-28 04:23:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 23a8ce13-54ae-37bf-9e8e-91d8003ea70c | -19.57449 | -46.12337 | 2024-09-28 04:23:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0ee5cf5-02f2-3c82-afa0-bbf3b9816f4c | -20.89449 | -45.41886 | 2024-09-28 04:23:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.3 |
| a92b68d1-5027-3765-ad6f-6922458342b2 | -20.8939 | -45.42298 | 2024-09-28 04:23:00 | NOAA-21 | AGUANIL | MINAS GERAIS | Brasil | 3100807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| c834ec48-9a32-3877-ad85-2369020340a1 | -20.51998 | -45.88322 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f8b9199-203b-37c7-8afa-d212327d7052 | -20.51656 | -45.88263 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 82992bd5-7edb-34b8-8ff3-ed52a5e8dc51 | -20.51315 | -45.88202 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e18432c-ce8f-35c5-ae29-5b879bc56f6e | -20.50969 | -45.90575 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6e861537-c9f3-335f-b075-bee87ea294c0 | -20.50631 | -45.88082 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c0af3258-343a-3c97-9861-6259420d72d8 | -20.50626 | -45.9052 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2046f087-1278-33ba-9d6f-ce8f6e1c0e7f | -20.50397 | -45.89693 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 9.1 |
| ef1e2ef4-26e7-3b55-95df-cfc5262826ab | -20.50341 | -45.90078 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 92c2fa6d-b46a-3996-845c-fc2edc675187 | -20.50285 | -45.90462 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 6cab63e5-8927-3796-8b45-fcaaa051468a | -20.49948 | -45.87962 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6105aa1f-fd9e-3e17-a22e-02358d32ee71 | -20.49944 | -45.90398 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 80c925c3-e55a-3e73-bc2c-9ed68e62b277 | -20.49886 | -45.88389 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4406741-b931-366a-8f26-916651094d84 | -20.49603 | -45.90334 | 2024-09-28 04:23:00 | NOAA-21 | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a150c7a2-33f8-385f-af48-21e20045a527 | -20.49544 | -45.88327 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baffe261-c548-371a-b6ca-ce49afb5b8fe | -20.49483 | -45.88746 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c273965-2a84-38ca-8991-b01d80713eec | -20.49202 | -45.88266 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 63371175-bf3e-3009-8e89-aeea5e1c0b04 | -20.49141 | -45.88689 | 2024-09-28 04:23:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 135e3a6f-4250-36db-b1e5-b10a9cbab6a6 | -20.44875 | -45.47874 | 2024-09-28 04:23:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1ef081b9-7e1f-36fa-b8ae-98110097e9fb | -20.44818 | -45.48275 | 2024-09-28 04:23:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d6ba9ddd-e135-3d34-8afc-71931727c33b | -20.4447 | -45.48221 | 2024-09-28 04:23:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92f17ee1-8de0-3dda-86ae-88546b3c021a | -20.28513 | -45.83724 | 2024-09-28 04:23:00 | NOAA-21 | DORESÓPOLIS | MINAS GERAIS | Brasil | 3123403 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 42528934-dbbf-371c-a961-b14ff39c22e0 | -19.80184 | -45.718 | 2024-09-28 04:23:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| cc137fc7-60f6-36f9-8b29-c32d7e51ad28 | -19.79842 | -45.71741 | 2024-09-28 04:23:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 18296692-faa6-3ad6-889b-b16a9d737326 | -19.7983 | -45.71868 | 2024-09-28 04:23:00 | NOAA-21 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7586baa2-67c4-3c90-9760-d213138a3cfb | -19.647 | -45.89061 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ff1d58f-7a81-3b38-946c-3b4ba51570fa | -19.64644 | -45.89444 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6878cf36-a0e1-32f8-935b-4108fd24b95e | -19.64587 | -45.89826 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4fc81fb8-3888-3d0a-8eb6-96243da3814c | -19.64248 | -45.89767 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d6c3ed31-2b2e-3a24-96c9-87b0275e744a | -19.63909 | -45.89708 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| dbb4b9b7-3b66-3b34-80c1-a875060c40e5 | -19.63569 | -45.89649 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 1dd6deaf-a6fa-3653-8488-ba131d596d48 | -19.60567 | -45.86362 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0af13a4c-4db6-3f0e-a3df-5c6125fc8cbb | -19.60227 | -45.86305 | 2024-09-28 04:23:00 | NOAA-21 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2442b93a-14e3-3de9-bbb0-3e107b4891ca | -20.44645 | -45.46999 | 2024-09-28 04:23:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7139df57-910a-30e7-bc2a-ec1e76699978 | -22.16669 | -45.82041 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 3085565e-0122-3ab1-96a3-501e0b5fd41f | -22.1661 | -45.82452 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 6893b784-99b0-3605-9cf7-d18c2fdb9880 | -22.16379 | -45.81573 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| f9ab0784-292d-334b-8b0c-699d8cc38ba4 | -22.16321 | -45.81984 | 2024-09-28 04:23:00 | NOAA-21 | SÃO SEBASTIÃO DA BELA VISTA | MINAS GERAIS | Brasil | 3164407 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 77cad561-1f44-34c0-9a24-cab5b164522c | -22.02097 | -46.48994 | 2024-09-28 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0f7e2a02-4442-389e-9ea3-0bf6e7c528ec | -21.99211 | -46.49709 | 2024-09-28 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 0c5a6a9a-8597-3f8a-b6a4-36fe5e4b70ff | -21.98815 | -46.50042 | 2024-09-28 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2963db71-6458-3a4a-bb6f-4a159540a63d | -21.98758 | -46.50434 | 2024-09-28 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| c775f32c-72da-31b4-9d1f-240acab12fb3 | -21.98475 | -46.49986 | 2024-09-28 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1fea927c-ff1a-37a3-86c9-d2394c6a74d0 | -21.98419 | -46.50378 | 2024-09-28 04:23:00 | NOAA-21 | CALDAS | MINAS GERAIS | Brasil | 3110301 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9cd0a203-b2e2-3705-8f0b-770ad4de774e | -21.9598 | -45.81294 | 2024-09-28 04:23:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ef8e3091-9051-312b-8a49-86b959c942ed | -21.95922 | -45.8171 | 2024-09-28 04:23:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| b0b7f501-1126-3a18-a5f1-4161b2fd6580 | -21.95633 | -45.81234 | 2024-09-28 04:23:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 32d0e54d-3475-3205-8907-5f306aaee1df | -21.95575 | -45.81649 | 2024-09-28 04:23:00 | NOAA-21 | TURVOLÂNDIA | MINAS GERAIS | Brasil | 3169802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 829998a1-7bb5-3e02-ac1b-94a4f2eeeac1 | -21.89352 | -45.61262 | 2024-09-28 04:23:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| e763a12c-8dcd-3710-b7bc-76f99b73f36c | -21.83814 | -46.13193 | 2024-09-28 04:23:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b718e381-49b3-3f0e-8f29-766c26a1a932 | -21.83472 | -46.13134 | 2024-09-28 04:23:00 | NOAA-21 | CAMPESTRE | MINAS GERAIS | Brasil | 3111002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |


[Clique aqui para ver as próximas entradas](README64.md)
