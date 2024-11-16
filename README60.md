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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5dba8c17-d177-30a8-ae3d-9cab30c9183b | -16.84272 | -57.00264 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| bc9e08ee-2686-39cd-a7d5-7b27f746b54f | -17.56472 | -57.43365 | 2024-11-16 05:46:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 4b5ea904-e4ae-3971-abfb-10bc30c95fae | -17.30935 | -57.50607 | 2024-11-16 05:46:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.9 |
| 88f5cbd6-cfa1-30a5-b23e-acaa465d5e0e | -12.02258 | -62.92848 | 2024-11-16 05:46:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 83904fa0-4eae-3dff-93be-e0dd05dfbac1 | -16.03689 | -59.40264 | 2024-11-16 05:46:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 61b04662-8f42-3bda-a07e-947b3302773f | -22.05809 | -56.00951 | 2024-11-16 05:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d95cd7f8-bcc4-3635-83b2-d7c7cbfb5043 | -22.05149 | -56.00895 | 2024-11-16 05:48:00 | NOAA-21 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e21c38a5-2335-3ee3-902f-b57ce1be2b4c | -6.1363 | -42.578 | 2024-11-16 05:50:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| 4022e678-9477-3aae-8752-1bdcfc602200 | -3.2753 | -45.5151 | 2024-11-16 05:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 140.1 |
| e0180302-4089-358f-9fb3-6096459597c2 | -4.4725 | -44.5752 | 2024-11-16 05:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 73320e5a-f3a8-389e-8156-1361c7924aba | -2.9044 | -45.3494 | 2024-11-16 05:50:00 | GOES-16 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.4 |
| d970e93a-9721-313d-a113-52bbbb3a9b8d | -2.78 | -48.5806 | 2024-11-16 05:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| ae2300d5-73b3-3aff-9cdb-302e95284daf | -2.2299 | -53.6018 | 2024-11-16 05:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 41cc4d30-530a-3dee-8037-1316c8ab1d67 | -3.294 | -45.4919 | 2024-11-16 05:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 101.9 |
| e65f341d-5206-3183-90b0-befe9f0534d3 | -3.2754 | -45.4927 | 2024-11-16 05:50:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 82cdf1e8-64a6-3c67-b646-7e5b295f0bef | -4.4726 | -44.5524 | 2024-11-16 05:50:00 | GOES-16 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 6b3bce9e-7015-3bf0-a8c9-5613e16a0778 | -3.2939 | -45.5144 | 2024-11-16 05:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 144.6 |
| ecf67fb9-901a-3ee0-9939-b684fe338993 | -3.2753 | -45.5151 | 2024-11-16 06:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 68d14cd6-5a8c-3281-beb2-aeaaed693726 | -2.78 | -48.5806 | 2024-11-16 06:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 66.4 |
| d4151f47-288c-3859-ba0f-35ac0eb61560 | -2.2299 | -53.6018 | 2024-11-16 06:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 1eeb8cda-ba73-3b1b-9c9f-85a9d0838cc5 | -6.1363 | -42.578 | 2024-11-16 06:00:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 95.4 |
| d5c696fd-075e-3e82-8680-c76b4ef72f6c | -3.2754 | -45.4927 | 2024-11-16 06:00:00 | GOES-16 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ba3b8a5f-251d-3886-b59a-901cd05e92a9 | -16.09462 | -60.09491 | 2024-11-16 06:07:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f9f1690b-e5b9-3155-ba14-64a26c59a5ba | -15.90015 | -59.24762 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 99b29581-d188-34f2-912e-6686c9d94fd0 | -9.06952 | -65.85088 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| eefd60e1-57e0-347e-ad69-dfadd87de714 | -9.52707 | -66.64808 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ebfc531-3b2d-3f1b-97c9-3fd170f4f5ba | -15.89987 | -59.2507 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| d5eb4040-ce15-3142-8e38-73b268c21b17 | -16.10159 | -60.09567 | 2024-11-16 06:07:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c5d47a1-b376-3210-98c4-25a345f2bc6e | -15.89854 | -59.2658 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a2fc35f4-0437-3184-af1b-e8efca92078f | -16.0155 | -59.36923 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8a68ab75-cd9e-3d80-9e4f-584cbba94820 | -10.12623 | -65.02368 | 2024-11-16 06:07:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f01d2319-c05b-3454-bec7-716f885e60e9 | -15.89903 | -59.2595 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5f97f42e-c7bc-3a34-a8a6-ad902d5597eb | -9.0774 | -65.85876 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 329d33e0-3cfa-3a50-93be-6b6e046897ff | -10.12082 | -65.02806 | 2024-11-16 06:07:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d8c9b816-002e-3124-99f5-fe1d6115e86e | -9.07769 | -65.85641 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1ece07ce-6f22-3c5f-9623-c4cbe26ad1f2 | -9.64492 | -67.25563 | 2024-11-16 06:07:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d25c0b21-b1ea-3f10-91ea-112e815f4f35 | -9.58308 | -66.39991 | 2024-11-16 06:07:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 314d0f93-dea2-346a-802b-df95e084e764 | -10.12554 | -65.02873 | 2024-11-16 06:07:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 52c474b4-d475-3f6a-be60-adb5e895d271 | -9.64895 | -67.2562 | 2024-11-16 06:07:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c7c7ea2c-5093-30f8-8a44-7bfb65f69df0 | -16.02267 | -59.37103 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 85a8d3a4-1e50-3cf5-87b3-dfe50876771f | -9.07391 | -65.85151 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df49dc54-2bac-3148-b3c7-98012a50efc8 | -9.0733 | -65.85578 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4d7c3c3b-7a49-3881-9505-415c894f32b0 | -15.8994 | -59.25606 | 2024-11-16 06:07:00 | NPP-375D | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 35a3fb8e-0215-3877-aacf-f0c925487b05 | -9.82072 | -63.36158 | 2024-11-16 06:07:00 | NPP-375D | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9ffbcfe0-cf09-3af8-843b-04918800bbd1 | -9.07799 | -65.85447 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 470ffb4e-3375-3abb-aa42-bb60b352a22a | -9.07831 | -65.85212 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fba5e94-9f51-332d-aebe-9c3d502c9fb7 | -10.03088 | -64.22276 | 2024-11-16 06:07:00 | NPP-375D | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7da3bfc7-e6b5-3e8e-a6a1-110a469c3f24 | -9.72498 | -66.83063 | 2024-11-16 06:07:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8df86b30-095e-37ce-b1b2-e4e25435414c | -16.1 | -60.10104 | 2024-11-16 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eb3d17a0-8267-3ce8-b976-49d37110d7dc | -16.1006 | -60.09438 | 2024-11-16 06:09:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 12bd553b-8bc4-33dc-a283-c0aed2031b82 | -2.78 | -48.5806 | 2024-11-16 06:10:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 4aa9dd40-04ed-3001-8d23-5645f4f0bae2 | -6.1363 | -42.578 | 2024-11-16 06:10:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 97.0 |
| 8f8e7361-9974-33c1-b8ea-20993de9f918 | -6.1363 | -42.578 | 2024-11-16 06:20:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 89.0 |
| 721c1d1d-35e3-3a48-b3ed-71d64de3da02 | -2.78 | -48.5806 | 2024-11-16 06:20:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 5dd8b478-2044-3ce5-a7cb-80a65ad04dec | -6.1363 | -42.578 | 2024-11-16 06:30:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| 8c80c273-f0c0-3433-8b62-3d68a1764563 | -2.78 | -48.5806 | 2024-11-16 06:30:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| f4696e44-c20a-337f-a600-3712e8e95f32 | -3.388 | -45.2857 | 2024-11-16 06:30:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 47.6 |
| 307e46b1-ca0d-3f63-a044-5b0e8838901b | -9.07153 | -65.85752 | 2024-11-16 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b2737e0-55a9-3de4-9e08-706e87d5aa31 | -9.07455 | -65.86288 | 2024-11-16 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64362b41-b7fb-334a-bb2c-dec421c169ad | -9.07821 | -65.85841 | 2024-11-16 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4a374d67-d56b-3ae3-a632-70ba4b0901c6 | -9.07526 | -65.85697 | 2024-11-16 06:31:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 84593cd6-8b12-3e5c-9927-57cdc8b1e72c | -10.12407 | -65.02858 | 2024-11-16 06:31:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 84cb47fb-fc2e-3253-a875-f9daefea8ca5 | -10.12329 | -65.0355 | 2024-11-16 06:31:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89d2a064-6482-3e6c-a728-381a6fc00f71 | -10.11989 | -65.03228 | 2024-11-16 06:31:00 | NOAA-20 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 99a8ac70-297f-32ed-8b30-33df06129858 | -4.0931 | -45.6131 | 2024-11-16 06:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 129.5 |
| 4f09f070-2188-31c1-8a10-7ec9252d59eb | -4.1117 | -45.6122 | 2024-11-16 06:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 84.6 |
| 0ab62a8f-dc2b-3749-b932-5664face5106 | -4.0933 | -45.5906 | 2024-11-16 06:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 95.0 |
| b44081bf-09c1-3518-9f64-748fb8b4d609 | -6.1363 | -42.578 | 2024-11-16 06:40:00 | GOES-16 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 54.8 |
| 2910e965-443b-3e79-924a-206726b23279 | -2.78 | -48.5806 | 2024-11-16 06:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 2733da9f-aca9-3220-804e-3155b5a14398 | -4.1119 | -45.5897 | 2024-11-16 06:40:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 70.7 |
| b39e8e18-affa-3cf6-b836-7a92ac80c492 | -3.388 | -45.2857 | 2024-11-16 06:50:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 368158e5-ac7a-324b-9c3e-25f7e0526b9d | -3.0535 | -45.2539 | 2024-11-16 06:50:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 2fdcd2a2-c9ac-329a-afdb-66391ad0c430 | -2.78 | -48.5806 | 2024-11-16 06:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| fab71c79-3f5f-3ffa-9b0d-a41331948116 | -9.82062 | -67.93994 | 2024-11-16 06:56:00 | AQUA_M-M | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5221f4bf-360e-397f-8d7e-f04f5257e8ac | -10.11982 | -65.0183 | 2024-11-16 06:56:00 | AQUA_M-M | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 2a244f83-2e66-3515-a562-02883b32a492 | -2.78 | -48.5806 | 2024-11-16 07:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| be78944b-d66d-30f1-ad39-37eda47a43ca | -3.0535 | -45.2539 | 2024-11-16 07:00:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 81.9 |
| f1b5d34d-a079-32d8-9bbc-2f1d2b66ab64 | -3.388 | -45.2857 | 2024-11-16 07:00:00 | GOES-16 | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 47.8 |
| e2f7c08f-a336-3d1b-8b8c-4dc032602790 | -3.0535 | -45.2539 | 2024-11-16 07:10:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 126.5 |
| 4f1c93a2-e223-3b86-9446-87cf118745bc | -3.0535 | -45.2539 | 2024-11-16 07:20:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 83.8 |
| c6cba54b-9b4d-3548-bd2e-d7168edc3745 | -2.78 | -48.5806 | 2024-11-16 07:40:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 7fc3b9a1-6acf-3960-9c00-e6d20cb3d4f9 | -3.0907 | -45.2525 | 2024-11-16 07:40:00 | GOES-16 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 0ee4d228-0923-3eb2-9036-02bb140cbb5f | -17.2547 | -57.4493 | 2024-11-16 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 81.6 |
| a8c46284-a498-367f-ae12-eab0923a1b25 | -16.958 | -57.6269 | 2024-11-16 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.7 |
| 79d039da-9c2c-382c-a3ef-9c6aaecd957d | -16.9577 | -57.6473 | 2024-11-16 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 77.1 |
| ff26d0d6-23e5-3e55-99c3-3cd2a7770740 | -17.235 | -57.4516 | 2024-11-16 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 97.8 |
| 3769c748-ad18-373b-9f31-fcbd29191598 | -16.9384 | -57.6291 | 2024-11-16 08:00:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 96.9 |
| a8e0091d-4d8f-34b9-bbe4-9b31177cd87b | -16.9384 | -57.6291 | 2024-11-16 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 93.4 |
| 1d13f072-4ef2-3376-8483-5a9a23f8d6d8 | -16.9577 | -57.6473 | 2024-11-16 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.5 |
| fed1e4e0-54e2-374d-9bd4-44dc748ec759 | -16.958 | -57.6269 | 2024-11-16 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 103.4 |
| c6b20a8e-d259-3f99-92d6-5ec095fc4332 | -17.235 | -57.4516 | 2024-11-16 08:10:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 71.3 |
| 762e7631-da1b-32e6-8bae-7aa42a50e12a | -16.9384 | -57.6291 | 2024-11-16 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 89.5 |
| 50f90661-d056-3b84-84fc-06b16dbac257 | -16.9577 | -57.6473 | 2024-11-16 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 80.5 |
| 418f9586-b35e-37d1-bb9f-c0c967e81a31 | -16.958 | -57.6269 | 2024-11-16 08:20:00 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 105.3 |
| a2311d41-f707-38c6-81f9-daa9166375e6 | -17.5865 | -57.5739 | 2024-11-16 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 125.6 |
| 6392000c-3a8b-301c-bf1a-e39b81735dce | -17.6063 | -57.5715 | 2024-11-16 09:20:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 142.2 |
| ea02b1a7-35e4-3a26-ab60-ce016e51dead | -17.6063 | -57.5715 | 2024-11-16 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 114.4 |
| e6034df0-1d52-3296-b7ba-88b96d8dd14c | -17.5865 | -57.5739 | 2024-11-16 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 139.4 |
| c8de1d37-95b2-31c7-9adb-17d6269cb50e | -17.5862 | -57.5944 | 2024-11-16 09:30:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 123.6 |
| 0fc9210c-fbcf-33f6-aff2-c5e58a09d734 | -17.5862 | -57.5944 | 2024-11-16 09:40:00 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 124.6 |


[Clique aqui para ver as próximas entradas](README61.md)
