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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3834f46e-1907-33c3-b8f6-34f11c1ebf30 | -2.2479 | -53.7829 | 2024-11-09 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 30afa627-809e-3f30-8766-67fc74b18ee6 | -4.2487 | -47.5511 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 68.9 |
| be35083d-9a1f-3118-9d66-a1990c4e7554 | -1.5163 | -52.1901 | 2024-11-09 00:50:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 5741b3b7-694e-32d8-b12c-6aa66249d885 | -2.2479 | -53.7627 | 2024-11-09 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| d61d6f2e-3cc3-3bdc-b517-fb5e5a7882b3 | -3.1326 | -52.9939 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 093f9c0e-9ede-3a30-8900-af7b2a7e9e35 | -1.5078 | -47.1813 | 2024-11-09 00:50:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 283.3 |
| 9ceb0cda-34c9-3da8-bc4c-ccd5ac94f774 | -1.1467 | -53.6573 | 2024-11-09 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.7 |
| a6846217-41d9-3692-8a84-8c815625ca83 | -3.967 | -48.15 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| 330a8137-2c79-335e-bbb5-6589f21bc491 | -3.068 | -50.5631 | 2024-11-09 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 69.3 |
| 99603126-01d6-38d9-bcdf-48451d411412 | -3.1512 | -52.9527 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 117.8 |
| 3cba30c3-5b2f-306b-ab9a-e65d31a791ba | -3.9854 | -48.1708 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d07e8579-138e-3054-beae-4fa3e69aa469 | -3.1511 | -52.9731 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 368.1 |
| 990182d9-0c92-37fc-bc86-24b8f16abb69 | -2.6764 | -51.8189 | 2024-11-09 00:50:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 4ddb7475-55e8-3e1d-b6fd-8d9a411391cb | -3.1641 | -54.4854 | 2024-11-09 00:50:00 | GOES-16 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| bc1f16d1-919c-3f91-bcdb-d03a8ae83c41 | -3.151 | -52.9934 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 126.3 |
| e2313d66-67c1-3808-9183-5b310f505012 | -4.2058 | -48.5491 | 2024-11-09 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 144.5 |
| 44dc2fcb-c5cc-3831-bf25-65419ab1dfad | -3.9669 | -48.1716 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 237.1 |
| 39baff83-6d3a-37a6-84d0-2b55e4efb35f | -2.5448 | -47.1137 | 2024-11-09 00:50:00 | GOES-16 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 46.1 |
| a524bd4b-a29d-3394-90c7-6467a8566929 | -4.1872 | -48.5499 | 2024-11-09 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| f3d5c119-6228-3959-aa76-22933dd4bf14 | -2.4104 | -48.5265 | 2024-11-09 00:50:00 | GOES-16 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 226d2b01-dc5f-3811-8192-1e396bf1eb3b | -3.2808 | -52.7455 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| bceaedc4-446c-3b7f-b468-beea4f57b99d | -3.1327 | -52.9736 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 136.3 |
| f405793c-c712-31ef-b176-6d715d1d2097 | -3.9668 | -48.1932 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 106.6 |
| 8670c212-8ac8-3cc4-98e5-44dc889c96a3 | -4.2484 | -47.5947 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| 60bd8c21-110a-3ab3-ac1b-9e3b99474c09 | -2.2295 | -53.7631 | 2024-11-09 00:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| e923d2ac-092a-38ed-be2f-69b77a08951b | -4.2486 | -47.5729 | 2024-11-09 00:50:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 259.6 |
| db13077e-7e01-3139-86f2-a00ca64bad77 | -5.4701 | -43.6371 | 2024-11-09 00:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 314.3 |
| 0eff8fac-9f8e-3372-a7c0-9083c6294bbe | -4.2243 | -48.5482 | 2024-11-09 00:50:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 4633fa5a-8558-3fd3-acc1-c3310a0cce2f | -3.5649 | -43.5654 | 2024-11-09 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 7da10a88-5f03-36c6-8fef-0d71bb3b6971 | -5.4889 | -43.6357 | 2024-11-09 00:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.4 |
| e67af5b3-b734-3ba1-b156-64db985d34ec | -3.4466 | -52.7202 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 162.7 |
| ab9610cc-0a77-3b5a-aff2-5cfae19f4169 | -3.5462 | -43.5663 | 2024-11-09 00:50:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 92.2 |
| a8273ecc-f3b3-3b5f-b0b1-4066c62914e6 | -5.4699 | -43.6603 | 2024-11-09 00:50:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 486.8 |
| 43db8178-ca1e-3f74-803b-36e44a806bf6 | -3.0947 | -53.3196 | 2024-11-09 00:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 70.2 |
| c0fcf1a9-5277-388d-84f1-f49584e6f52b | -3.9853 | -48.1924 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 4372cb32-517f-3481-95ee-8926062d19cf | -4.2484 | -47.5947 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 64.4 |
| cfc83399-2408-3089-ad7f-ffceb92078f9 | -5.4512 | -43.6616 | 2024-11-09 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 652e6064-7d21-3361-8414-f6d62ad2a7c3 | -2.2479 | -53.7627 | 2024-11-09 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| aa2596d5-89c4-3954-988e-1e2b8f46be26 | -1.5164 | -52.1696 | 2024-11-09 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 82.4 |
| 6c386f04-6017-3831-8ad0-eb916ce8c57b | -3.151 | -52.9934 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| a27b9ec5-d2ae-34b7-ac75-af1c572b2c39 | -5.4701 | -43.6371 | 2024-11-09 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 442.2 |
| dd316610-bb7a-38ba-8374-4327cb8ce13a | -3.0947 | -53.3196 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 90d9def3-7aa6-3e03-a248-7bb675175998 | -4.2033 | -45.8538 | 2024-11-09 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 4a84b19f-35fa-3287-b0d8-4106d2f29b39 | -3.068 | -50.5631 | 2024-11-09 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| befb1f03-06cb-31c9-8834-bc63b00915e0 | -3.9483 | -48.1724 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| a9519980-296b-326a-a259-7ee670c4e906 | -3.1511 | -52.9731 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 478.4 |
| 43949e36-d116-3e28-842c-fc5ec106f319 | -4.2032 | -45.8762 | 2024-11-09 01:00:00 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 120.1 |
| 2e564616-61cd-3883-bd82-c864a02e764e | -1.5078 | -47.1595 | 2024-11-09 01:00:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 167.4 |
| 8b721761-c9b7-3688-ba55-df7665012d1b | -3.5462 | -43.5663 | 2024-11-09 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| b484ca1f-99ee-3603-b15f-cabb964e2574 | -5.4699 | -43.6603 | 2024-11-09 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 493.6 |
| 03ef7972-70ea-31d3-a750-bf1d17d4a063 | -3.4466 | -52.7202 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 159.4 |
| 82a747cb-6b42-36d6-ac6a-f4be13b60e2e | -4.4417 | -43.6348 | 2024-11-09 01:00:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 75.6 |
| add62c0c-3045-3e79-af45-3666966c3b2e | -1.5163 | -52.1901 | 2024-11-09 01:00:00 | GOES-16 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 49.4 |
| bfd12e3f-f228-39bc-a7ed-4286720debb6 | -3.2808 | -52.7455 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 199831a3-5ea2-3847-840e-6afc97810be4 | -23.9095 | -54.0606 | 2024-11-09 01:00:00 | GOES-16 | ALTÔNIA | PARANÁ | Brasil | 4100509 | 41 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 74e05241-cc84-3be6-853f-fecdaca798b8 | -3.1512 | -52.9527 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 101.0 |
| 278e9f33-f2cc-3fd0-9376-038ab549b0cf | -4.2058 | -48.5491 | 2024-11-09 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 717fb5c0-2be9-34d8-9602-93bc9285f516 | -3.5649 | -43.5654 | 2024-11-09 01:00:00 | GOES-16 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 0ffa826d-c757-32d6-99d2-f5ee6fd77e95 | -4.2671 | -47.572 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.1 |
| c1925322-86cd-3ab8-8d2e-bedf819cc690 | -2.2479 | -53.7829 | 2024-11-09 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 67.1 |
| 09fe7056-2440-3a72-b70d-3ddaea427738 | -5.4887 | -43.6589 | 2024-11-09 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 313ea639-ba4e-38be-8eb1-1cb74b9e7998 | -3.9854 | -48.1708 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| e767f073-bf20-377c-87ab-8fad4e116237 | -4.2486 | -47.5729 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 250.3 |
| 3c4269a2-1202-35d8-bb63-965c96f24842 | -3.9668 | -48.1932 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 128.5 |
| 2f8e8427-4528-3490-a4ac-bbacd3560768 | -2.2295 | -53.7832 | 2024-11-09 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 9cae5590-d924-3cb6-b363-2ad00b857b7c | -2.6764 | -51.8189 | 2024-11-09 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 55d801ab-32f8-396c-820e-875db72e8605 | -5.4889 | -43.6357 | 2024-11-09 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 73.3 |
| 1f4e808c-b939-3ed5-9b0a-0177fe30c795 | -3.2353 | -50.2645 | 2024-11-09 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 64d9bab7-6023-315a-9dd9-1af7c89c226e | -3.967 | -48.15 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 615c77cf-d961-30d6-b3d3-484076b84d3e | -2.5747 | -49.1421 | 2024-11-09 01:00:00 | GOES-16 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 1319ca78-7b94-3185-9ed7-92a695a947c3 | -5.4514 | -43.6384 | 2024-11-09 01:00:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 5e978aec-f147-3922-8f55-6e569cc8e630 | -3.9669 | -48.1716 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 218.4 |
| 60e167c5-55eb-3636-8a0e-465bad7a3826 | -4.1872 | -48.5499 | 2024-11-09 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 0d15c75f-9ef1-3d24-a944-e4a11b3b80b3 | -4.2487 | -47.5511 | 2024-11-09 01:00:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2664d4af-ddd2-3c5a-ae4c-c41653e8c1bb | -1.1467 | -53.6573 | 2024-11-09 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 40.8 |
| 6b588160-438d-3ba6-a402-fc6dd3802854 | -1.5078 | -47.1813 | 2024-11-09 01:00:00 | GOES-16 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 337.3 |
| 65657b41-dd4f-3eeb-8911-8515ad969e1d | -3.0865 | -50.5625 | 2024-11-09 01:00:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.4 |
| e4e7bbf6-97a5-3bc5-ac14-da6e6c94b22b | -4.2059 | -48.5275 | 2024-11-09 01:00:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 36339d6f-beb4-361b-ae24-418720d1763c | -2.2295 | -53.7631 | 2024-11-09 01:00:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 268230d0-8802-34de-895d-2a97c96724a2 | -3.1327 | -52.9736 | 2024-11-09 01:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 163.6 |
| c8e4120a-1b5a-3adc-8a6a-42ccf30022b2 | -3.61 | -47.35 | 2024-11-09 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d15cf01d-dfd5-34f2-9963-ff045774b597 | -5.45 | -43.69 | 2024-11-09 01:00:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c962b05-9281-3e95-8ada-a513572ed477 | -5.45 | -43.64 | 2024-11-09 01:00:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a47abe0a-6ac3-3346-a183-e92398d730d6 | -3.13 | -52.97 | 2024-11-09 01:00:00 | MSG-03 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 232ba3a2-5566-35c3-876e-4c5207104231 | -3.58 | -47.35 | 2024-11-09 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0bd4d73-fa1f-33c6-85da-bae098e5093c | -3.61 | -47.3 | 2024-11-09 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6eb514d-cec0-3d33-94a7-33b704f98690 | -5.48 | -43.64 | 2024-11-09 01:00:00 | MSG-03 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a15c062d-27ea-3ab5-b117-e0e890707e53 | -4.25 | -47.56 | 2024-11-09 01:00:00 | MSG-03 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 739fb54e-cfaf-31d9-a309-7a6c9f0fa7e1 | -3.58 | -47.3 | 2024-11-09 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dd89df2a-8d28-33f1-bf04-49c10c4c7e1e | -3.58 | -47.4 | 2024-11-09 01:00:00 | MSG-03 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 361aebb8-d7b9-3e5f-a69e-19df8e781f71 | -1.5 | -47.17 | 2024-11-09 01:00:00 | MSG-03 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 336d36af-cb52-3918-8e63-d996ee62e51b | -4.2671 | -47.572 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 77.9 |
| c64449d9-7e3c-3205-8c32-27e0286f45ce | -3.0865 | -50.5625 | 2024-11-09 01:10:00 | GOES-16 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 8e2898ea-fce2-33f0-b7e6-01e5a11c5504 | -3.4466 | -52.7202 | 2024-11-09 01:10:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 114.8 |
| ad95db23-b263-3b2f-9745-0b17a208b05d | -5.4512 | -43.6616 | 2024-11-09 01:10:00 | GOES-16 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 108.0 |
| 44cacc82-eedb-3d16-9f62-b0531f304d30 | -1.1467 | -53.6573 | 2024-11-09 01:10:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| 6a7ded05-622a-317e-9ab0-37e23811b96f | -4.4417 | -43.6348 | 2024-11-09 01:10:00 | GOES-16 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| e14b9355-0573-3b8d-b593-3a8ae23cbd2e | -4.2243 | -48.5482 | 2024-11-09 01:10:00 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 50.1 |
| c8e2869a-9214-32d6-97e8-18415579c43b | -3.9669 | -48.1716 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 208.6 |
| a003bb35-63c0-342e-bc3c-c5f6f222438c | -3.9668 | -48.1932 | 2024-11-09 01:10:00 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 98.0 |


[Clique aqui para ver as próximas entradas](README12.md)
