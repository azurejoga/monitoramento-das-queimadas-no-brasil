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

## Dados Diários - Página 88

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 529bcb18-d771-343e-8246-727bb35d55e3 | -8.11147 | -70.13422 | 2026-09-24 06:46:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 331b49f0-89af-3c42-afe7-0bbae1b9d7e6 | -8.31425 | -70.54074 | 2026-09-24 06:46:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c1e2fc1-422f-3dfa-9aa9-8e0a9c464204 | -8.11608 | -70.14266 | 2026-09-24 06:46:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dafb2635-d38e-347b-9df7-d1b9605b725a | -9.22251 | -67.3904 | 2026-09-24 06:46:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dbd7a33-b569-3266-bc43-dedc85408984 | -7.52449 | -70.39896 | 2026-09-24 06:46:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a8b0a57-4822-3f49-9190-c4494a334612 | -8.96423 | -72.59118 | 2026-09-24 06:46:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5530db57-0102-3f06-9064-823a0d771d22 | -8.65004 | -67.03288 | 2026-09-24 06:46:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5e4ad931-b883-3dd3-87d5-28079da96f88 | -9.22172 | -67.39655 | 2026-09-24 06:46:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 00a7de72-5c10-3f4c-8878-2ebc5da63ae7 | -7.51947 | -70.39463 | 2026-09-24 06:46:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d97c1aad-4754-367c-9004-5478bfddfefc | -7.51896 | -70.39829 | 2026-09-24 06:46:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 642c2c7e-54e4-3645-ba2f-55c8671c4fb3 | -12.1112 | -50.7215 | 2026-09-24 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| e970fef4-d246-32a9-b031-0a0b975102a3 | -12.13 | -50.7407 | 2026-09-24 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 77359926-ee0d-39c6-9dc4-9a8b2c33c066 | -12.1109 | -50.7429 | 2026-09-24 07:10:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 35d8eab0-11f5-3549-bfb3-738d600020aa | 1.60603 | -55.88329 | 2026-09-24 07:14:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 53f9441b-578f-3c8e-8060-7df862bc59ac | 1.60201 | -55.87994 | 2026-09-24 07:14:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| ad8d1757-26ea-3298-b124-d7fbe23df81b | -4.11887 | -51.08355 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 6c1caecb-0a05-3656-a30f-770a68a4dd88 | -6.6536 | -55.05547 | 2026-09-24 07:16:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 7a374d12-0897-37c5-9df7-bd3f37cc37cc | -3.72122 | -54.20264 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a23b6eca-7204-3f86-894c-d9c241502bf3 | -3.15505 | -54.59518 | 2026-09-24 07:16:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 0fcd1761-3bc9-35f8-a003-4aece058fe76 | -6.04522 | -57.76413 | 2026-09-24 07:16:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 5e0aa36c-434a-3277-b776-5f055d2a9764 | -1.83706 | -55.71401 | 2026-09-24 07:16:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| d3d3f056-ea50-3242-a52f-5d595dedd855 | -1.91786 | -58.25726 | 2026-09-24 07:16:00 | AQUA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| cbc6a310-f6b7-3e8b-8f58-8b9283899321 | -3.42042 | -54.0057 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| e01ff766-5fe9-337f-a07f-bff9e5065dfa | -6.60884 | -59.92252 | 2026-09-24 07:16:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 45.4 |
| 7f2460b0-882e-38b5-b021-81059786b4a2 | -2.89654 | -54.09603 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| 03688bd7-277a-386a-848e-30894c5a0a57 | -5.59322 | -60.20119 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 1c8a506e-b56b-3d8a-aba3-4b760cd580f8 | -4.56487 | -54.93901 | 2026-09-24 07:16:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6cb1b864-daff-3d54-ad36-a82c11ef2559 | -1.28102 | -57.03658 | 2026-09-24 07:16:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 805992bf-ca45-3eea-9593-2b3a8b05dbf6 | -5.59592 | -60.18469 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fe50f441-bf77-39e0-bef1-b8456c572fc8 | -6.62013 | -59.92434 | 2026-09-24 07:16:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 6c346e30-e0c7-377c-8796-50f43302e4d6 | -3.44633 | -50.06995 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 8b4e8b29-645f-3563-88c6-15348cad6f30 | -1.92015 | -58.2643 | 2026-09-24 07:16:00 | AQUA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f88009b1-914b-3704-8122-233a16207b22 | -1.19742 | -54.14313 | 2026-09-24 07:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ad3216f3-6663-3a61-9ade-dc642180fcf4 | -4.12053 | -51.07201 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 633322f6-ddcf-3050-ba60-3d79d018bef0 | -3.70504 | -54.19134 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 27e73536-966a-3510-8110-c52aa36f40a4 | -6.67714 | -58.57667 | 2026-09-24 07:16:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| d9d8a381-34f3-377a-811f-eb68dbacda45 | -5.8378 | -53.85506 | 2026-09-24 07:16:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 5d6c475b-d2c7-3053-a97b-7406d282bf57 | -1.62686 | -54.91093 | 2026-09-24 07:16:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3258afad-cb1d-3d0a-aaf8-6f97df50a846 | -3.16249 | -54.60521 | 2026-09-24 07:16:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bb9598d7-344d-3cb1-b708-674c21a465bc | -3.00501 | -51.5339 | 2026-09-24 07:16:00 | AQUA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3e1b8a14-3087-394f-987d-7d6d14b80b3f | -1.21775 | -54.55606 | 2026-09-24 07:16:00 | AQUA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| d0f61265-ada2-3ce8-9fef-21d83a74c55e | -5.77358 | -56.5197 | 2026-09-24 07:16:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| d4ffb6cc-6606-385e-9c9b-4b687b386444 | -3.45702 | -50.07145 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.1 |
| f68efb73-af65-3f52-ae35-89d1dfbca957 | -6.88353 | -55.56377 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| cb7ab485-fc26-3fc7-84fa-c752b8af87ed | -2.63988 | -54.68774 | 2026-09-24 07:16:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3ed2a4ea-2d25-3f14-88fa-479c0e85836b | -3.71247 | -54.20135 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 05d17502-70fa-3573-8168-8ff806071965 | -6.60639 | -59.93784 | 2026-09-24 07:16:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 7affb699-04f5-3efe-8af7-346947629d79 | -4.1089 | -51.08186 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 703c1be0-ba01-39a4-af39-027af3ebec4b | -1.82794 | -55.7126 | 2026-09-24 07:16:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| c11517f0-42f7-316a-99bb-0b030534eff8 | -6.32863 | -49.85356 | 2026-09-24 07:16:00 | AQUA_M-M | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 37e7d7cd-55e6-34de-b95b-415c205721a8 | -4.4768 | -54.96498 | 2026-09-24 07:16:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a28c966c-0bb1-342e-83c3-8b4166d82d55 | -2.93998 | -57.78824 | 2026-09-24 07:16:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7383bfc5-b6ef-37ed-bfb3-eea45dc841ac | -6.44365 | -59.94638 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| a0e21a75-1c65-30c4-b9f4-b4982da5752e | -5.32988 | -48.97874 | 2026-09-24 07:16:00 | AQUA_M-M | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c5dcc0fa-eb06-3da6-b5f4-2251ad116e77 | -6.44088 | -59.95287 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 17729049-3728-3cff-a383-49d2313fefc7 | -6.34485 | -57.7688 | 2026-09-24 07:16:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 7c87b5d0-5933-3686-bc8d-0efdc8c4884f | -3.17559 | -48.01094 | 2026-09-24 07:16:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b7d2b076-b275-3896-b49d-d238fdeadd18 | -6.89976 | -55.57523 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a5f3950f-4c95-31d6-9177-f244dd9bd3e5 | -3.16382 | -54.59648 | 2026-09-24 07:16:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 016759cf-6830-3940-8285-fcd3035db9f8 | -4.53954 | -54.96531 | 2026-09-24 07:16:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 576077b4-7853-3ea7-b38f-4d6efa2bb59e | -1.84123 | -54.71843 | 2026-09-24 07:16:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| bab88d4a-cd81-3dc2-ba47-5fb357d326f2 | -3.70372 | -54.20005 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ab2fa467-73ee-37b3-bf40-4654dca277b5 | -2.88911 | -54.08604 | 2026-09-24 07:16:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5884740d-a509-31ed-8017-ca246664e52a | -1.27109 | -57.03513 | 2026-09-24 07:16:00 | AQUA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 91985878-6367-3f11-8f40-10079e92f76d | -4.53821 | -54.97406 | 2026-09-24 07:16:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4474166-40c9-3664-b168-da94b818232b | -4.11009 | -51.07531 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| a930d6f2-9a6d-31e8-a8de-53261ffd82c9 | -6.44126 | -59.96154 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 3ca8f5a3-29fd-3149-911e-bbc19047e3fd | -2.94186 | -57.77618 | 2026-09-24 07:16:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 8.9 |
| af7fef6a-b4f2-3637-8f08-3fa1363b17fc | -1.83563 | -55.7235 | 2026-09-24 07:16:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| cf84e7a2-22e1-36e2-b1f4-1a7e0003180d | -3.15372 | -54.60392 | 2026-09-24 07:16:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 13.5 |
| eec29313-5a17-392a-95cd-70c4ce6adf71 | -6.10224 | -57.66869 | 2026-09-24 07:16:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4b9a45b4-bec5-36c1-a34f-bfcaa47df4d3 | -6.67012 | -58.56861 | 2026-09-24 07:16:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| a01fc72e-8209-3b59-8435-e945da59ecee | -6.68387 | -55.04879 | 2026-09-24 07:16:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2cb13ac8-922c-3379-b11b-da8a9598d310 | -6.68254 | -55.05754 | 2026-09-24 07:16:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a1db07f6-3b77-37de-ae4c-8133c4a5d255 | -4.71877 | -55.97921 | 2026-09-24 07:16:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a14a7aa4-f95b-3f6c-b6c9-7fd0ceda3075 | -1.6255 | -54.9199 | 2026-09-24 07:16:00 | AQUA_M-M | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| fbfc3a21-17e3-3e29-a86c-429385371c43 | -6.62912 | -59.93277 | 2026-09-24 07:16:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f9bbc73e-a6fa-3093-b375-e2a98cc3c56a | -4.55611 | -54.9377 | 2026-09-24 07:16:00 | AQUA_M-M | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d9042516-8d78-3b7d-b979-8dbb38adcb51 | -3.44441 | -50.08334 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 27.4 |
| 63a5505e-85a5-35cd-bad9-2cb79b2f918b | -6.64041 | -59.93459 | 2026-09-24 07:16:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| b69f8b10-43e7-3310-9366-fc21989b931b | -3.45508 | -50.08485 | 2026-09-24 07:16:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| a80bd4fc-24e9-3fed-bbc3-303feb95f40b | -12.1458 | -50.71982 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 52cf5666-8268-3c44-9dc4-bdabb69aab06 | -12.09664 | -50.73026 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 23.4 |
| 080be85b-e1b9-3174-a9f0-d1a34e44bb77 | -10.6195 | -53.99312 | 2026-09-24 07:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| dafc449d-9cd4-3346-a422-696bfbf2cb80 | -14.56531 | -54.11618 | 2026-09-24 07:18:00 | AQUA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a80e2495-f86b-361e-b7bf-4ed5f30bf1bd | -11.90205 | -50.72569 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 28.5 |
| a4903fbd-9ca0-33df-81cf-5a803dd87d6a | -9.25112 | -47.34999 | 2026-09-24 07:18:00 | AQUA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| e8706180-32aa-3d17-8bdb-c17ba5218fcd | -9.25908 | -46.22777 | 2026-09-24 07:18:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| cff36f9e-474d-34ac-927f-3a32ac110059 | -11.25815 | -51.35503 | 2026-09-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| fda92a34-49b1-3edb-ba22-f7c597fb4d3e | -11.22048 | -51.37228 | 2026-09-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 22.9 |
| 16fc461c-16a4-31c2-bac8-398f2aaec076 | -10.90284 | -53.94361 | 2026-09-24 07:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 5f5f9ed6-7565-3b57-9c3c-f85f9a31383f | -11.24642 | -51.34653 | 2026-09-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 926857f7-519c-3bd9-b629-313e5a9b7661 | -11.91375 | -50.72725 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.3 |
| f68bf892-a1e9-312e-9dcc-e6b363ff76fa | -9.26824 | -46.23367 | 2026-09-24 07:18:00 | AQUA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 80.0 |
| c70d007b-56a2-31ee-a94d-ea379f201cb3 | -11.95836 | -50.74991 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 26ea0cc5-1a26-3d02-9cd7-fcc99bebcde6 | -8.2678 | -54.7726 | 2026-09-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 8a33d22c-abe3-32f9-90a4-0d7b86ec985e | -10.6181 | -54.00283 | 2026-09-24 07:18:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 501c1571-7ad8-31e2-b278-24b93e93f2d1 | -11.23541 | -51.34503 | 2026-09-24 07:18:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 8b90d925-f5b7-3825-82aa-c79b886453d8 | -8.26914 | -54.76371 | 2026-09-24 07:18:00 | AQUA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| baf51a0d-1f95-3cac-8626-69a7d29bcaff | -12.14137 | -50.75305 | 2026-09-24 07:18:00 | AQUA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |


[Clique aqui para ver as próximas entradas](README89.md)
