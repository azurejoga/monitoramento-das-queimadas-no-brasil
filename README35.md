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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2e139062-575c-383e-97b8-41e9a53608eb | -6.914 | -59.1455 | 2025-08-13 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.3 |
| 50f0ec1b-cd7a-3a7e-92e9-bc1f67dc3054 | -6.9141 | -59.1261 | 2025-08-13 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 220bf274-57ce-336e-b994-2a00a0a8c7d9 | -6.8771 | -59.147 | 2025-08-13 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.8 |
| adc0d8d3-f634-35ff-a2b6-ee74dd008fdd | -6.8957 | -59.1269 | 2025-08-13 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| e366316a-18fd-3ae3-838a-22e098bcc83d | -6.8772 | -59.1277 | 2025-08-13 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 5e089c40-4e5e-3f7d-a4fa-981102f1a8c2 | -6.8956 | -59.1462 | 2025-08-13 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 198.4 |
| af0a868c-4db6-3b7d-9f6d-a9c0c2059d2e | -6.9141 | -59.1261 | 2025-08-13 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 65386ff6-9619-3750-b16a-64d0a2908162 | -6.8957 | -59.1269 | 2025-08-13 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 111.3 |
| a311022f-ff97-3fe6-98a7-0c5357fda3cd | -6.914 | -59.1455 | 2025-08-13 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.4 |
| e0862056-50db-372b-a0b8-1a6c00970557 | -6.8771 | -59.147 | 2025-08-13 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 150.1 |
| ea82027d-9135-3d2c-ae33-9fab035f4352 | -6.8772 | -59.1277 | 2025-08-13 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| c186c6f0-bd81-308c-a0da-1f42ab5943e0 | -6.8957 | -59.1269 | 2025-08-13 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 107.2 |
| c068df5a-4850-3004-a3c4-447be0b498c8 | -6.8772 | -59.1277 | 2025-08-13 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| faca3d3e-bd31-3f11-a7e9-17e4c11b0d57 | -6.8956 | -59.1462 | 2025-08-13 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 174.3 |
| 92587e40-6642-3800-ab05-654e11eaea95 | -6.9141 | -59.1261 | 2025-08-13 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 76582e06-4e1c-3739-8b52-4c6cf2129ea5 | -6.8771 | -59.147 | 2025-08-13 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 145.3 |
| dc2c0e7d-aafb-31bb-81f9-0afb305e81f3 | -6.914 | -59.1455 | 2025-08-13 08:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 744df7bd-f325-31a7-a724-85e4043efe60 | -6.8957 | -59.1269 | 2025-08-13 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.6 |
| f7862ea5-bfbb-374b-9ae1-61fee9b4fee5 | -6.8772 | -59.1277 | 2025-08-13 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 23be3b42-3cbd-39aa-8702-f16c860a8568 | -6.8771 | -59.147 | 2025-08-13 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.6 |
| 039864d4-75e5-3817-be63-629a8d932948 | -6.914 | -59.1455 | 2025-08-13 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 07a41b3c-ac67-3ead-8669-1bae2bc4c099 | -6.9141 | -59.1261 | 2025-08-13 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ed73c7c4-4e0c-326d-86f4-e7888e9aba31 | -6.8956 | -59.1462 | 2025-08-13 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 151.5 |
| 5feb5232-f5bd-3cb1-90b0-729970af7226 | -6.8957 | -59.1269 | 2025-08-13 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 86.6 |
| 76a424af-1a08-3bba-8f8d-f16015861d15 | -6.8956 | -59.1462 | 2025-08-13 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.0 |
| 367c765b-dd52-3fd7-914b-a7434195f124 | -6.914 | -59.1455 | 2025-08-13 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 17a13d6c-f460-32bb-8383-f1318450e832 | -6.8772 | -59.1277 | 2025-08-13 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 555cccf7-a1bb-3842-becb-993b20f6043e | -6.8771 | -59.147 | 2025-08-13 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 110.4 |
| a19a0af0-4eb4-3e5b-b4c9-9240c63ba0e3 | -6.9141 | -59.1261 | 2025-08-13 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 80df83f1-f15e-3396-9d99-5e73d649ae3c | -12.5361 | -46.9837 | 2025-08-13 09:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c1c5b61b-5aa1-30bd-9f4f-9114a12a7954 | -6.8956 | -59.1462 | 2025-08-13 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 127.7 |
| 0163bccd-5ec4-3514-8272-dd6685cb70f5 | -6.8771 | -59.147 | 2025-08-13 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 32997c17-0ffa-3322-9c33-35711cce6afd | -6.8957 | -59.1269 | 2025-08-13 10:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| b8a93146-8d53-37a6-a3ca-b79300afdaa9 | -6.8957 | -59.1269 | 2025-08-13 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.8 |
| 9d46911d-cd2e-3655-b967-1eb038f5c263 | -6.8956 | -59.1462 | 2025-08-13 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.3 |
| a85c5740-3e7a-38f7-989e-889522d50030 | -6.8771 | -59.147 | 2025-08-13 10:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.5 |
| 1629a6e6-5d7c-392a-8e43-7a9905ce6448 | -6.8957 | -59.1269 | 2025-08-13 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5533f81c-baef-3d08-8f3d-084010f539db | -6.8771 | -59.147 | 2025-08-13 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 96.6 |
| e8e014a7-9c53-3cea-85e3-fbc915cc263f | -6.8956 | -59.1462 | 2025-08-13 10:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 143.4 |
| a0849288-1c7d-3655-a36d-1f4beb3db905 | -6.8956 | -59.1462 | 2025-08-13 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 131.5 |
| 74257f07-1879-3e13-9471-b7cc61b4cf37 | -6.8771 | -59.147 | 2025-08-13 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| fccb280e-899b-3f58-82f4-da1ca3c1be80 | -6.8957 | -59.1269 | 2025-08-13 10:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.5 |
| 28da5343-85b4-38a3-931d-0b688fbf7295 | -6.8771 | -59.147 | 2025-08-13 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.3 |
| 8f173568-c1e2-35e4-85b0-ae80702e0599 | -6.8957 | -59.1269 | 2025-08-13 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| dddf1113-d023-3525-af44-07d3bc1b76ff | -6.8956 | -59.1462 | 2025-08-13 10:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 4ec82b26-7cf1-3380-87fa-8d00132797de | -6.8771 | -59.147 | 2025-08-13 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 90.1 |
| e96e48ea-edaf-3451-a7d4-ab891f08f22c | -6.8957 | -59.1269 | 2025-08-13 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 75.6 |
| e7b41085-ef9d-3c8d-a2c1-53ac79163264 | -6.8956 | -59.1462 | 2025-08-13 11:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 2da1115a-25db-36ad-bbd3-b10661a7476d | -6.8957 | -59.1269 | 2025-08-13 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| a7e3ae90-9985-3d11-b738-307163eef8d6 | -6.8956 | -59.1462 | 2025-08-13 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 122.6 |
| 01ded0b3-f73f-3a5c-8c51-68a6d476c5ec | -6.8771 | -59.147 | 2025-08-13 11:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 605566b0-c1e5-3845-8321-855359832b65 | -6.8771 | -59.147 | 2025-08-13 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 94.4 |
| ae0cb403-32d4-3f00-82e6-2f454ce0976e | -6.8957 | -59.1269 | 2025-08-13 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 8dfb828c-5c51-398a-bbd5-92a1a35c1ae5 | -6.8956 | -59.1462 | 2025-08-13 11:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 68e20779-f24d-3afd-aecf-601e7c71a1fb | -6.8957 | -59.1269 | 2025-08-13 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.4 |
| ef8e2b4c-d9a6-3d70-85b3-af97ff965b06 | -6.8771 | -59.147 | 2025-08-13 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.3 |
| 734c2947-5fe8-3fcb-8d43-c6b44104c1dc | -6.8956 | -59.1462 | 2025-08-13 11:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 124.2 |
| 66a2ba20-66f1-3c4d-a44f-fa5d10c1e505 | -6.8957 | -59.1269 | 2025-08-13 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| 254db3d7-fbc6-31de-8545-072a8fb14351 | -6.8956 | -59.1462 | 2025-08-13 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.7 |
| 1c1f3696-148a-3f0a-a137-41170e0c20b0 | -6.8771 | -59.147 | 2025-08-13 11:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 97.6 |
| e6196f07-e94b-345c-8350-2d80b8ea9c14 | -6.8771 | -59.147 | 2025-08-13 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 3a21bd0d-a235-384b-bfc9-acd299c3e2c3 | -6.8957 | -59.1269 | 2025-08-13 11:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.1 |
| e82dd4d6-32c5-3adc-9211-69b21c68270e | -6.8956 | -59.1462 | 2025-08-13 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 123.4 |
| 3c7e59ed-e824-3f9c-943a-40e23110c7c9 | -6.8957 | -59.1269 | 2025-08-13 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 49f8b395-bed8-3302-84b4-8dc9bef19c49 | -6.8771 | -59.147 | 2025-08-13 12:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 24a2ad30-29d5-3c2b-a920-33f667c905a0 | -6.8957 | -59.1269 | 2025-08-13 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| d0536d70-8d74-3fa9-8490-cdf5384a27b3 | -6.8956 | -59.1462 | 2025-08-13 12:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.6 |
| 0e76a975-e58a-3240-905e-36c61ab27c58 | -6.8957 | -59.1269 | 2025-08-13 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 240ff1f0-ce4a-38f7-91eb-e774ba969179 | -8.106 | -55.5701 | 2025-08-13 12:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 130.1 |
| 9e591795-f6df-3edd-bb67-0f7ad64d29fe | -6.8956 | -59.1462 | 2025-08-13 12:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 128.0 |
| 584c76eb-210a-32bf-abd1-13c2d97a7cd9 | -6.8957 | -59.1269 | 2025-08-13 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.9 |
| 577bc16b-7cab-376f-841d-293f84bc9151 | -8.106 | -55.5701 | 2025-08-13 12:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 70.4 |
| d456f26c-10c5-335b-a415-7bd03602d340 | -6.8956 | -59.1462 | 2025-08-13 12:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 136.9 |
| 751ddc2d-0198-32fd-9a11-eaef5574890a | -2.90343 | -48.25362 | 2025-08-13 12:32:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 3af27081-0011-31ba-a686-586c790f1b07 | -6.61582 | -43.87395 | 2025-08-13 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7091b280-2a0f-349f-aa5f-d5482973cf87 | -0.74958 | -47.75483 | 2025-08-13 12:32:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9a7baf2b-56a1-3d54-ac30-3da6696df906 | -7.48544 | -43.93344 | 2025-08-13 12:32:00 | TERRA_M-T | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 6c00092e-ab1b-3309-b8b7-6858ee4719eb | -0.75088 | -47.74587 | 2025-08-13 12:32:00 | TERRA_M-T | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| ecf6af1d-b486-3916-8052-dbcf5207e387 | -3.5879 | -47.52226 | 2025-08-13 12:32:00 | TERRA_M-T | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 05279bb1-f89e-3b4e-aa10-c492bc4acea0 | -2.91359 | -48.24592 | 2025-08-13 12:32:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ab7c910e-e8d6-3a63-bb9e-83be382a1bb5 | -2.9047 | -48.24469 | 2025-08-13 12:32:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 38cd5f90-3b62-3384-b8ac-052c2ece885a | -6.6182 | -43.88004 | 2025-08-13 12:32:00 | TERRA_M-T | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| af44406e-fd8e-3980-9388-0c3d302e8cda | -4.08596 | -47.32552 | 2025-08-13 12:32:00 | TERRA_M-T | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 959971a6-f414-35e0-872e-f416937c3fd7 | -3.11924 | -42.92736 | 2025-08-13 12:32:00 | TERRA_M-T | BARREIRINHAS | MARANHÃO | Brasil | 2101707 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d54fb462-f5c2-3024-bb6d-27e05a1f0d85 | -2.91232 | -48.25486 | 2025-08-13 12:32:00 | TERRA_M-T | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 742204ab-91d3-39e0-8260-e473ec5c178f | -10.09038 | -50.31516 | 2025-08-13 12:34:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 97ebf500-9842-3343-822a-524a83a742db | -12.57453 | -47.04259 | 2025-08-13 12:34:00 | TERRA_M-T | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 612086a9-a1dd-3e7a-ab81-dfbffa6836b7 | -9.71138 | -49.46979 | 2025-08-13 12:34:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b0aa40ff-4775-3891-922b-7d58fdbc55eb | -7.07299 | -59.18729 | 2025-08-13 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.0 |
| d86cd41e-e849-332a-80ff-ccda060004f1 | -9.71008 | -49.47896 | 2025-08-13 12:34:00 | TERRA_M-T | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| a38b8f7d-2780-399e-900b-6bc74f18160d | -9.30843 | -48.92702 | 2025-08-13 12:34:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| a379eaa7-a1da-32b5-869c-0bbbff06fdbc | -7.06551 | -59.1933 | 2025-08-13 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.7 |
| 52203032-f31a-35da-bf99-3b16a363be64 | -11.18468 | -50.59152 | 2025-08-13 12:34:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 21.2 |
| dc36bc4e-712b-30c6-a91a-17bd3d5a06b6 | -9.31752 | -48.92828 | 2025-08-13 12:34:00 | TERRA_M-T | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 78334251-79f8-3fbe-939d-148f2df3a762 | -8.11453 | -55.56534 | 2025-08-13 12:34:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| a7954e9a-3085-3628-af7e-39a12f296726 | -12.32064 | -50.05312 | 2025-08-13 12:34:00 | TERRA_M-T | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 15d6c141-ee6a-3ae0-b466-3d6aec5f8e19 | -7.08135 | -59.19614 | 2025-08-13 12:34:00 | TERRA_M-T | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 33.4 |
| 1df48694-9b08-3f6a-876e-fe797d6cf0c2 | -10.31242 | -48.11152 | 2025-08-13 12:34:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0c2aa038-f5b8-3fe6-aa4b-0ab9f76351cf | -8.57281 | -54.6931 | 2025-08-13 12:34:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 14e127d6-5eef-3a68-aafb-ed7eb24484c5 | -8.11194 | -55.58173 | 2025-08-13 12:34:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 66.9 |


[Clique aqui para ver as próximas entradas](README36.md)
