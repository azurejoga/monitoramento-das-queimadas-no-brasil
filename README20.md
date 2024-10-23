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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39fda955-0173-35f3-89fa-144bc24538b1 | -3.11507 | -45.30453 | 2024-10-23 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a9d8e178-94b1-396d-9c41-eb49e6fed5e5 | -3.11442 | -45.30865 | 2024-10-23 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a38f12a8-d6b5-35ef-84bd-fc90d9e86b3c | -3.11251 | -45.30329 | 2024-10-23 03:57:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 45851fcb-5e93-39cd-8783-43fa1c7f94cb | -3.11183 | -45.3074 | 2024-10-23 03:57:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bcab8e53-3226-3f45-87ba-470b123db77d | -2.78644 | -45.19112 | 2024-10-23 03:57:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8fbabeb-97d0-34f1-923a-3bebe78aeafd | -4.96222 | -45.8787 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 54661166-c283-379d-acf7-ae8b50319781 | -4.96212 | -45.87546 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6237622d-2d31-3932-918c-97b85b1b280e | -4.96145 | -45.8796 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1531b5db-168d-37f0-868f-31feb46e9edb | -4.90313 | -45.85215 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e48da95a-b51a-3d44-a551-5e4b19d0ece6 | -4.89802 | -45.85584 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c9640c69-d75e-33aa-ba12-10b5024c4122 | -4.89008 | -45.33379 | 2024-10-23 03:57:00 | NOAA-20 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 33b6823c-8df2-33f8-88e3-6e6f5a61fa05 | -4.86535 | -45.86076 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| eca97cef-d064-39a4-a5b9-433117bbb7ac | -4.86528 | -45.86344 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86ffd1f5-a980-31d2-ab1b-2bfc57531a99 | -4.86466 | -45.86503 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 296623bc-5707-35e7-abcf-e0873f16e252 | -4.86169 | -45.85561 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bd40f09-a3f8-30cc-8c35-4d16e20682af | -4.86166 | -45.85831 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5250103f-2a2d-3347-b465-ff4597fee2f3 | -4.861 | -45.85986 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0bf070ce-356c-3144-adbc-a2a4494309c8 | -4.86094 | -45.86257 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5a568f90-5ec0-3e8b-9d09-c711519dc168 | -4.84556 | -45.52246 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 535f5a5b-86f3-3cfb-93ca-31eaf4a19a63 | -4.8449 | -45.52644 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce254391-6e57-3b36-a8d5-1cd306e8fa61 | -4.83553 | -45.85078 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aadde75b-515f-3825-bdf9-f602a81b1050 | -4.79486 | -45.90609 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf488cfb-de4f-3bba-bad8-6a38ea3d8dd5 | -4.77565 | -45.77335 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a4c99550-59f5-31e7-b0db-7b9afeb643bf | -4.75897 | -45.76592 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 03161015-8137-33cd-be67-cc70d01ab77a | -4.75829 | -45.77011 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b143db71-e110-38c3-a78e-b519dd906ed9 | -4.75392 | -45.76949 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7e31cdd2-6761-3468-92d1-199489022296 | -4.75323 | -45.77369 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0172b993-3004-3c3d-b5aa-63f42bf6798f | -4.7252 | -45.72684 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e782251b-3227-3d53-8937-3b0f768b98a3 | -4.72451 | -45.73103 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 519f6685-cc73-3840-a0db-b9e6c7686a5c | -4.7238 | -45.73534 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c86c7b7d-4574-3b2a-9f92-18ea84c186a7 | -4.72308 | -45.73964 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 644bed84-1183-3ede-99c9-cf3caf422c06 | -4.72084 | -45.72623 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 57325570-ff96-39a8-ba00-255e0ccb1f6c | -4.72016 | -45.73035 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bea2733e-ce68-3069-8860-9daee95a6a40 | -4.71946 | -45.73457 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| b722cea5-dcb4-307b-b781-ad7c54c11e5c | -4.71874 | -45.73888 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| aba69e8b-e059-3c42-8cba-e54b68814adf | -4.71801 | -45.74332 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 61c29111-58f7-3cd1-bf8d-f03aa9c4b9aa | -4.71508 | -45.73403 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| d35e1aa3-cb15-32cd-8711-804a19c737e9 | -4.71439 | -45.73821 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 12c021d7-2a98-3c47-818c-a05764a770b0 | -4.71367 | -45.74255 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e41c29d-9ff9-3afc-aeb2-bf6fbcfcd271 | -4.70304 | -45.64628 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5b64c1c5-e3d4-3faf-9ac7-2ab018f8a0f8 | -4.68817 | -45.86862 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aed390d3-3199-3945-b093-07481d0b825b | -4.68748 | -45.87276 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8d664574-4832-3bfc-bb6d-518ecbe05878 | -4.68677 | -45.877 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c050902-ba87-32df-be6f-494da4556584 | -4.68376 | -45.868 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c121bdf8-f9c6-3ba0-9272-698dcb236f8b | -4.68306 | -45.87221 | 2024-10-23 03:57:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 340559e9-a3ed-38d0-8587-bf888aa5e5e0 | -4.58512 | -45.78358 | 2024-10-23 03:57:00 | NOAA-20 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e0b121d9-d775-3b0b-9079-9dbf465d2864 | -4.47595 | -45.48233 | 2024-10-23 03:57:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 6e0bec12-6883-3f62-9a9c-61f6685a3d3e | -4.14723 | -45.5965 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3723c42a-7fc5-37dd-9c5d-17e632d72f9a | -4.14653 | -45.60067 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f9e42fd-d548-3dc2-aa75-2fe0c8f10d96 | -4.14583 | -45.59717 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd2b1281-0461-39bc-b8f2-a2f2921d786d | -4.14582 | -45.60485 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6c9b002-971b-38d6-ad7a-e68a4ab6ecd8 | -4.14516 | -45.60135 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8978098e-dfa1-3b4e-bcc1-073ebfa44043 | -4.14448 | -45.60554 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 135d376c-1331-3167-ad1f-32dc6394da0b | -4.14359 | -45.59164 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e63d488-02c0-3788-aa07-ce56e6bffb58 | -4.14289 | -45.59578 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 62efb937-6fb9-3f24-bf4e-ca41954413f9 | -4.14218 | -45.59996 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bc09c4f-afe9-3a88-b66e-4bb5c6343ff1 | -4.14215 | -45.5923 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ece3b35-6c4e-3697-badd-3e69a49277a0 | -4.14148 | -45.59646 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1251373-f84d-3f37-bed4-d68ee96f4457 | -4.14147 | -45.60413 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ab90ad5a-3192-3e00-90b4-a70bc832bfcd | -4.14081 | -45.60064 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc51f3e1-ce26-3e53-9724-a337739526e8 | -4.14076 | -45.60833 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d15d935a-6427-3894-a1c9-88b2c88a078f | -4.14013 | -45.60482 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edd6eb83-b4bb-35db-9ac7-9a3d9282369e | -4.13945 | -45.60905 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 78c24009-4ed5-3f3b-a9b4-bdd30f475bc5 | -4.13848 | -45.58742 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| aca59b5d-533b-370f-ae8e-51d3b786d60e | -4.13781 | -45.59159 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 62880afb-0f59-32e6-8042-6dbbb8845c3c | -4.13713 | -45.59575 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| a4318e34-b610-3f0c-9254-d81d17949751 | -4.13646 | -45.59993 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 99eecd07-aeb4-3a02-b367-b2e016c53faf | -4.13578 | -45.60412 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 7677ec67-f93a-3f57-b94d-29ae3a8a8e3e | -4.1351 | -45.60833 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 0527da77-1dd3-3544-a003-4d6d8bcc7b7d | -4.13442 | -45.61253 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 36a37332-bc13-35a7-baf8-70bbddaa73f7 | -4.13414 | -45.5867 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 0e6fba53-3411-3474-8e58-0ce4f5b31aa7 | -4.13346 | -45.59088 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 8.1 |
| dfc11c8b-c100-361f-ad3b-82db11ff6450 | -4.13278 | -45.59507 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 6d94cefd-6975-3e60-845d-90be8ef72e80 | -4.13211 | -45.59924 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 7912c766-c558-31ce-9ea3-ce294b5317c4 | -4.13143 | -45.60341 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| b0c27d96-4648-3e30-a023-44516d5d1b40 | -4.13075 | -45.6076 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 16.9 |
| dbaa5dd1-78bb-379b-8b3e-bf8932224c34 | -4.13007 | -45.61179 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 967e1efe-d8a4-3108-928f-f5acbf821c30 | -4.1298 | -45.58597 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1c701ede-5343-3184-93f4-592feb755576 | -4.12911 | -45.59018 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 158614a4-a1c4-3755-83bc-cbea68be1b36 | -4.12843 | -45.59436 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 60dcb383-d81f-3917-8f1f-ca93aa6e9771 | -4.12776 | -45.59854 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| e3fdc48e-5e43-3937-83d7-1dae08052b73 | -4.12708 | -45.60271 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 55188262-e1d0-37c6-ad98-83a2d31ecc38 | -4.1264 | -45.6069 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 584aeb86-1a1a-3d19-bcd7-f5c716ea5188 | -4.12572 | -45.61109 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b01de82f-9ff0-3f05-8870-121dd784d975 | -4.12546 | -45.58523 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 719694cd-d429-3e1c-8d18-8a35ac2bee63 | -4.12477 | -45.58943 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 56637d09-463d-3fa0-9148-a94249b23b4b | -4.12409 | -45.59361 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 5588a0b0-4c14-361d-8a20-94955cc1f4d7 | -4.12341 | -45.59781 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 77.3 |
| d80e94da-4860-3c1a-9892-93518c999fa1 | -4.12273 | -45.60201 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| edd162f2-4a60-3c05-88cb-85b8ba7eafd3 | -4.12205 | -45.6062 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 9647d003-288d-3b95-b72b-bc7e4b2acf16 | -4.12136 | -45.61039 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ccbdad3a-1df4-3a9a-9611-c4d82eab73bf | -4.12112 | -45.58449 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b2da51e5-ccaf-32f0-80f9-05c10ed9f63e | -4.12043 | -45.58867 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b56dfd99-19a2-38a6-a5e9-ea6d3ac1cf15 | -4.11975 | -45.59288 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1b3a835c-17ae-3bb3-9c07-73b79e2333ad | -4.11907 | -45.59708 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| cdffda27-ddd1-32a5-b749-7cdb49f57560 | -4.11838 | -45.60129 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a81f2e82-f562-3ab0-a830-602147ac9214 | -4.11769 | -45.6055 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1e1a4030-68d7-3fe7-a237-3a549d8e049f | -4.11609 | -45.58796 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ca64c4db-b983-313c-8e4b-e806c4159eae | -4.1154 | -45.59217 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5f394cba-dc79-3458-8ee2-30a4225215b7 | -4.11471 | -45.59637 | 2024-10-23 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README21.md)
