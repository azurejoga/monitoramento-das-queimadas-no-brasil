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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ff0c7fe7-e328-39db-9c74-c08e8e1a9be9 | -2.6764 | -51.8189 | 2024-11-09 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| cf6929c7-f0a1-3440-a329-99d846a0d053 | -3.9853 | -48.1924 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| d1674479-ce06-3c82-8d49-062eb4d30d4e | -2.2479 | -53.7829 | 2024-11-09 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 7f07b3e9-7860-336d-8c3f-807f2a5eb5d3 | -3.2808 | -52.7455 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 3964ceb8-87ad-34db-89cf-aad417521746 | -3.1511 | -52.9731 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 544.4 |
| 14f70ecc-a7fc-3d48-aac7-01b5f32bc92c | -1.5078 | -47.1595 | 2024-11-09 01:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 129.1 |
| 8b444e7d-7493-3d16-9ba5-3eb594a7c5f6 | -4.2058 | -48.5491 | 2024-11-09 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 33b038b2-3186-3bdc-a5da-ca30099baf51 | -23.9095 | -54.0606 | 2024-11-09 01:10:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 102.5 |
| 57f34b1f-a708-3148-b7ee-4da28ab0b2ad | -3.1327 | -52.9736 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 232.3 |
| 7279d302-228b-3bef-9e5e-b91d57d79dd9 | -3.1328 | -52.9532 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| 6296052a-726c-3b9f-80cc-0ca4c3f66f94 | -4.2486 | -47.5729 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 261.4 |
| a7af98ac-fdaf-37a1-ad52-9872e9aec387 | -3.967 | -48.15 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| f57c96a8-07da-34f7-9227-94ac91b2d65d | -3.1326 | -52.9939 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 41f124a2-ebb1-3b6f-97e7-7e61c25eb5bb | -5.4701 | -43.6371 | 2024-11-09 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 373.1 |
| 6b2de2ac-ad6a-39e1-b3ee-324d91ff3a24 | -3.151 | -52.9934 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 181.4 |
| 7716da77-ccb1-3d61-8efa-ad44037c0a5f | -4.2487 | -47.5511 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| da02f4f7-060d-3ed0-abb2-728eb2c4b9b7 | -3.0947 | -53.3196 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 833ea070-67f0-37f0-9253-16ecbac34cb0 | -3.9854 | -48.1708 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 1ee42269-1b94-3dd6-983c-5e50e60236de | -1.5164 | -52.1696 | 2024-11-09 01:10:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| f8b9a1fc-db31-343e-a98c-30e7b464bd1e | -3.2353 | -50.2645 | 2024-11-09 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 2ddb594f-3453-3c83-89bb-5b54aeefbf55 | -1.5078 | -47.1813 | 2024-11-09 01:10:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 287.5 |
| c820f68b-cf99-3747-8b2c-7befdea6c06f | -4.1872 | -48.5499 | 2024-11-09 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| e0aed27f-0315-375c-b8db-29eac2a37c2f | -3.8277 | -46.4944 | 2024-11-09 01:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b326c758-7de6-34a5-96e9-68ea8e07f3de | -5.4889 | -43.6357 | 2024-11-09 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 90.4 |
| 1ddc40d4-e383-3637-b2f5-bd6fb82d2829 | -3.5649 | -43.5654 | 2024-11-09 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| fa6af0a0-94a2-31b4-ae96-f77fb5ac6bf6 | -3.8463 | -46.4935 | 2024-11-09 01:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 67.2 |
| 78bdc537-d1fa-397f-9f76-acac81284255 | -4.4415 | -43.658 | 2024-11-09 01:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 527c57ed-224c-37b3-b78c-1b340b492dc7 | -3.068 | -50.5631 | 2024-11-09 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f2088837-fb63-3189-9a57-ad7107b752aa | -3.1512 | -52.9527 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 133.8 |
| 10d70bbd-3d2c-34e7-8cb1-866d01ae5d3b | -3.5462 | -43.5663 | 2024-11-09 01:10:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 9c2d6354-8ba8-3aa9-afba-0e6b588ccfc2 | -4.2032 | -45.8762 | 2024-11-09 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 5e562e52-3297-3703-9323-66383bc26b45 | -4.2219 | -45.8529 | 2024-11-09 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 1016f057-81d1-33a6-994d-aa2dc1752248 | -5.4699 | -43.6603 | 2024-11-09 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 562.2 |
| 1eb21ec8-c1fb-3eb1-aaeb-7e7abf47d6f9 | -3.8278 | -46.4722 | 2024-11-09 01:10:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 56.9 |
| 6e3fe0be-0aaf-310b-a765-6c0536d86e2c | -2.2479 | -53.7627 | 2024-11-09 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 3eefad80-8f76-3357-ab31-c5f1d80bcc92 | -5.4887 | -43.6589 | 2024-11-09 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 116.3 |
| e73321ab-b02d-3552-82e5-ba4fae0136db | -2.2295 | -53.7832 | 2024-11-09 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1f43c233-aaa0-348a-a28d-ca62f4e60ae9 | -4.2484 | -47.5947 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.8 |
| c99394b4-e3b3-3895-9837-d75fe5ea0ab0 | -4.2033 | -45.8538 | 2024-11-09 01:10:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 183.4 |
| 65066545-9d62-3c02-aba8-21f788d77667 | -2.2295 | -53.7631 | 2024-11-09 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 2abff112-ed45-325c-98c2-65642aee52ce | -3.9483 | -48.1724 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| b7268048-f08a-35e4-958f-8992ca514974 | -5.4514 | -43.6384 | 2024-11-09 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| a40a18f4-ea2e-358b-81e8-85a6c3c8bbb9 | -3.151 | -52.9934 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| 22d0c23c-5fb4-32a3-b8a7-af385122de64 | -5.4514 | -43.6384 | 2024-11-09 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| f14fcebd-bc9e-361b-9e67-091dd1efcdba | -2.2479 | -53.7829 | 2024-11-09 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| cc4b16b7-9b67-3a1d-a97f-ee1b52a58737 | -4.2487 | -47.5511 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 76.5 |
| f58efee4-6bfd-318a-9710-3a71819f5edc | -1.1467 | -53.6573 | 2024-11-09 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 9cb5fb5a-5c9e-3143-95a0-814dd692eb44 | -3.1511 | -52.9731 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 440.1 |
| 52fe9c7e-4e85-3c07-aec3-4441b62a45ba | -4.2484 | -47.5947 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.2 |
| e508b50e-1ef6-3f8a-b8f6-7cdac1ed1698 | -5.4512 | -43.6616 | 2024-11-09 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| e96ff8cf-c2ba-321e-aa51-671d4f14c233 | -4.2058 | -48.5491 | 2024-11-09 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 107.6 |
| 4d0a2c42-6ff7-3b52-ba12-3ee368c45dcc | -2.2479 | -53.7627 | 2024-11-09 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.5 |
| f7d414af-a424-33a1-888d-c7f08973fa08 | -3.9483 | -48.1724 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.7 |
| ba253773-1b3e-34f2-a00f-63b6bb5b9be6 | -3.1326 | -52.9939 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 2190a343-3e6a-325c-af3c-f59c67c1acd9 | -3.5649 | -43.5654 | 2024-11-09 01:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 680b357b-b2e9-3843-be06-1d5641133388 | -3.0865 | -50.5625 | 2024-11-09 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.6 |
| bff4243d-e9d4-3140-bd4d-c4711729aa0d | -5.4699 | -43.6603 | 2024-11-09 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 264.5 |
| 80531ea8-b27d-3652-b467-d25b5cbc4cdc | -1.5078 | -47.1595 | 2024-11-09 01:20:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 84be9bed-0303-3f28-b4e0-4a16e7938853 | -3.4466 | -52.7202 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 3d3476e3-7314-3a3b-b1e6-4c59a32ef223 | -2.2295 | -53.7631 | 2024-11-09 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 4dc3ad26-cb63-316a-9fa5-6222f9e9338f | -3.1506 | -44.3883 | 2024-11-09 01:20:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 115.4 |
| 9706b473-a814-3ca0-8b16-d5665ee32ece | -3.0947 | -53.3196 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 74768e01-74dc-349b-81a3-03052c84811c | -4.2219 | -45.8529 | 2024-11-09 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 74.6 |
| 14dc7623-10c9-39cb-a283-119661fc2824 | -4.2243 | -48.5482 | 2024-11-09 01:20:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| a421951f-72f0-34ed-8e01-a2ec41f7763f | -2.2295 | -53.7832 | 2024-11-09 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 5940f258-44a8-37a4-b210-ec80153afeab | -5.4887 | -43.6589 | 2024-11-09 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 0d177392-ea69-3352-937f-ad2004cd7738 | -1.5164 | -52.1696 | 2024-11-09 01:20:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| bf4132f6-dbf1-32f0-b182-67843994a6a2 | -4.4415 | -43.658 | 2024-11-09 01:20:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 118.3 |
| e965176c-3860-3574-bcad-c7e498919004 | -3.1505 | -44.4111 | 2024-11-09 01:20:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 160.1 |
| 0e6a5dcc-0518-37b7-b8d7-5702800d3495 | -3.9668 | -48.1932 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 5b4af191-7648-3445-a7fb-d1dde37781be | -3.8464 | -46.4714 | 2024-11-09 01:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 9acee736-5710-3e27-94b6-2491ee1f86b8 | -23.9095 | -54.0606 | 2024-11-09 01:20:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 70.8 |
| 14355a2a-d719-3d4f-824d-5f0e2312ef53 | -5.4701 | -43.6371 | 2024-11-09 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 239.4 |
| 6008e457-7637-388d-ace6-520ee0992a34 | -5.4889 | -43.6357 | 2024-11-09 01:20:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| d47bf8de-7492-35f6-a9c6-43a0e7daa16a | -3.1691 | -44.4104 | 2024-11-09 01:20:00 | GOES-16 | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 7932d665-a21d-36d5-887b-5a27e2f218c7 | -3.1328 | -52.9532 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 6b5b6602-7b8f-393e-b2f8-7e4fb5d0aa26 | -3.967 | -48.15 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 72bad337-6f62-35c9-82d5-282f55ce9d25 | -3.068 | -50.5631 | 2024-11-09 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 176fea71-166e-3f64-b550-ca37ec02b02e | -3.735 | -54.2091 | 2024-11-09 01:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 3cc79220-d794-31a8-9c3c-004d49e43bd9 | -1.5078 | -47.1813 | 2024-11-09 01:20:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 154.8 |
| 9343c67f-a762-3315-9dfd-e8170f57cc19 | -4.2301 | -47.552 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 8067851c-d37e-3ba9-84c8-53040d87e4bc | -3.9853 | -48.1924 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 66.7 |
| c7cdf7a9-490e-3fc6-96ba-defb0fad4682 | -3.5462 | -43.5663 | 2024-11-09 01:20:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 2d5cf092-3005-3f5a-9409-b259afab6c80 | -2.6764 | -51.8189 | 2024-11-09 01:20:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| 1d17603d-4769-38aa-9c7a-a64793a858bd | -4.2032 | -45.8762 | 2024-11-09 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 100.7 |
| 244d7665-be12-3d44-861f-48a15751c042 | -4.2671 | -47.572 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 939fdb6e-54db-3817-816d-4d48437f6212 | -3.9669 | -48.1716 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 202.2 |
| 11aecb88-b044-3470-9a70-f35a8e102046 | -4.2486 | -47.5729 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 241.3 |
| d26fc8b8-9048-32ab-b28d-7722edf80240 | -3.8463 | -46.4935 | 2024-11-09 01:20:00 | GOES-16 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 7b192987-12f7-3f92-9f42-e889aa721cfd | -3.735 | -54.2292 | 2024-11-09 01:20:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| dcd66208-8abc-3c2d-9dd8-667499207086 | -3.1512 | -52.9527 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 121.9 |
| 41074962-3fa1-3bf9-8f92-46aa75f68b11 | -4.4417 | -43.6348 | 2024-11-09 01:20:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| e6dbce68-eccc-399b-a99e-04a446622fa8 | -3.9854 | -48.1708 | 2024-11-09 01:20:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 860e3634-0ee0-3795-8323-233e042e5f31 | -4.2033 | -45.8538 | 2024-11-09 01:20:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 132.6 |
| 86bb59a0-ce0e-320b-9ebe-c0a00db51599 | -3.1327 | -52.9736 | 2024-11-09 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 263.6 |
| aa5140f5-d7f9-3001-9449-422b1e2024d7 | -3.735 | -54.2091 | 2024-11-09 01:30:00 | GOES-16 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 0639a607-eccb-3c18-97ae-9652c4c91d6c | -2.3605 | -46.8557 | 2024-11-09 01:30:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| d9947534-ffee-3bdd-bef4-5e0d3e28ad49 | -3.0865 | -50.5625 | 2024-11-09 01:30:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 5933ec46-de73-3a7f-8f08-9540a450df98 | -3.5462 | -43.5663 | 2024-11-09 01:30:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 75.8 |
| efa892a8-ca5f-3494-9ef6-0d54601c9370 | -4.2671 | -47.572 | 2024-11-09 01:30:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 95.7 |


[Clique aqui para ver as próximas entradas](README13.md)
