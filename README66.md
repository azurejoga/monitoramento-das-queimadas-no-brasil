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

## Dados Diários - Página 66

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61063c57-c6ee-3086-bce0-abed3bf1b524 | -7.05373 | -59.84747 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e8ef370a-2a13-3089-9e71-a6c427dc1eca | -6.80793 | -59.44862 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| abd38a5a-3923-3b10-9a5d-f35790028ef1 | -6.00828 | -57.85371 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ec8cdcf-00ae-3049-a4f1-46d1f04c8b4c | -8.57591 | -54.68954 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a2276abe-9e72-32ff-9087-f0d93a58a2ae | -9.40092 | -60.57327 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ec668e99-4de6-34f1-9434-34d5f8bde911 | -6.10998 | -57.73783 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b33206e2-19d7-3ae6-a659-cede59cab674 | -8.54206 | -54.77385 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 23c020fe-8152-3582-a461-02c169059148 | -8.56021 | -54.76155 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4900300f-c337-34ef-b706-c87f52b202a3 | -8.55179 | -54.75142 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 84afdd97-24a7-35dc-a153-1306085857e6 | -6.00637 | -57.86697 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8fa5f70e-d418-34c7-9858-16181e0d3460 | -7.60541 | -60.94638 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a1f85cae-f15b-3957-acc1-9e6977ec1807 | -6.13795 | -57.84847 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9bcc0a63-0203-37bc-8379-5515db80c33b | -8.57897 | -54.77589 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cb9f3f19-6eb5-32ce-9392-30046560ab26 | -9.17563 | -60.82818 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3abd73e-a64f-382c-97e6-e59db147427c | -8.95693 | -60.5864 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f1cf02d-7408-349f-ad62-8960751fcab1 | -6.75788 | -59.46688 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ea8d9b61-abc9-32e9-970b-880e99a1f13a | -7.60478 | -60.9507 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ee639db-add6-3b93-9a72-135470c57252 | -9.42125 | -60.41383 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ab0b0e0-ed98-361a-babc-e3051f5cab7e | -8.58117 | -54.75819 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6916fdf2-4ce8-38a6-93f1-abf24cf6b70e | -8.56243 | -54.74347 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6f37cffc-e225-39e0-9bd4-2aff20cb65b1 | -8.21443 | -55.02506 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fec26f6-820b-3d64-9e38-b869bd4bd668 | -9.40143 | -60.58695 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3b46989-c5e8-311d-994d-7d35e7b4b9a1 | -8.56518 | -54.75385 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 63e4e023-d3f7-3be2-b296-5495e7c388cb | -6.1462 | -57.86685 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e4af1f4-89dc-3b71-bb3f-d54ab30467ad | -8.58421 | -54.7336 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 01f14ba9-8ac4-33d8-aed0-1df1e479e473 | -8.08194 | -61.36013 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 876a2370-46ec-3aa1-932e-c0179e0ea505 | -6.85606 | -59.03446 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 500e62c0-67ed-35de-91fb-ad0a95a62f3e | -7.61297 | -60.95636 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df5e0f1a-27b3-3622-91eb-4f0d2ef34980 | -8.56088 | -54.73409 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4df1ee2b-1a65-3202-a8ec-ab255fcefbc2 | -8.56839 | -54.69486 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dde04c03-a31e-30ed-95ac-82e02050a25b | -6.79899 | -59.44189 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f9be684-8f4a-34bd-a646-fe3ddc136791 | -7.04496 | -59.84116 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 660109e6-c3d9-3098-a498-1a0eb75bfcc1 | -6.70051 | -58.9472 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 781ab6ed-4b46-3ae4-932d-166d708f31b4 | -6.75103 | -59.16777 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ae40ca8-521b-3132-b6f8-ab4ef0ee1344 | -6.70133 | -58.94144 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 2db7013c-fdd4-3328-a481-6ece3d0822e3 | -6.14379 | -57.84587 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b9bfa85c-ff53-39ff-b22d-52c87d5a43ad | -6.89103 | -59.03915 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b8878bd-fcc7-3c68-9880-42ad995714a1 | -6.14132 | -57.86285 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 61e44dc6-fb49-3c96-a79e-59baf1aaf975 | -7.6111 | -60.96916 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9c619d2-62d1-3690-86e9-6e3e6d85e6b3 | -6.84566 | -59.00341 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6e2cd2ba-8921-3f50-89de-fc0d10caf36e | -6.02134 | -57.80101 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c88a4468-8230-312d-ae66-7c5f4d363d9a | -9.39225 | -60.56705 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 44a9aae3-551f-3dae-b22f-73a2035fbe97 | -8.56624 | -54.76824 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 2efa5f9d-25b4-3df5-b73e-9afe6c5afda7 | -5.49752 | -60.1416 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b3de5152-c07d-3866-ad54-2212def35b80 | -6.7975 | -59.45249 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f808739a-e02d-3dbc-96d0-dd95bb56c659 | -8.54587 | -54.74413 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e9c1ceae-0756-375c-b689-ccde53b73901 | -6.14085 | -57.86607 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5e9e7933-eef9-3c70-b7db-197d08e439f7 | -6.14573 | -57.87006 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3869a2c9-ac08-3e13-8169-4bb00dbd88b4 | -9.42032 | -60.45424 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8caad4c-d3ac-3b49-95ed-2408847f353a | -6.70555 | -58.94772 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0b23739-4b0b-3276-b02c-fa1ab0ba5f4c | -8.57069 | -54.73203 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b7950cf-4536-320c-b2e7-00c7112a95f9 | -6.88442 | -59.04982 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6833329a-c9b4-3f5e-b2a6-6c10c3301d25 | -8.57215 | -54.72019 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 993a6e98-f426-3793-8595-755d4fb7ddbe | -8.55551 | -54.77565 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 866a0e0c-4c2c-303b-9f34-daa13b2b4ea8 | -6.08519 | -57.91238 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a5ad33b-b7bd-32c3-b849-147fdc50d6da | -6.84067 | -59.00261 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e74f2728-99b1-3792-9ece-c9fe46364704 | -6.0891 | -57.92307 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 06b982a5-5e91-3f48-a314-f54b69d12592 | -6.76906 | -59.45791 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3c152b87-1b55-3ae9-bf0e-cbd6bb35a122 | -8.55866 | -54.71827 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c7028853-dacd-37e2-a80b-e3969166d919 | -8.53543 | -54.71857 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fff75774-04d0-3b2a-b542-b9c4c6dfadc7 | -6.99182 | -59.04877 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caf836f7-695d-377a-b2f6-083c3389e5c6 | -8.58551 | -54.7556 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 394dc393-cbaf-399c-ac44-b1a7cab79672 | -6.87944 | -59.04912 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 877e6596-42d6-3bef-be7f-d49ab6400877 | -6.8492 | -59.01056 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ac5fb4e3-72aa-3482-8087-5b7e64e4eaa5 | -6.04047 | -57.80352 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3c0edeb4-40b9-37fa-aa71-55a06fa07fd6 | -6.09762 | -57.86326 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 987d3399-ed5d-3e90-8207-9ce6c9fb2633 | -6.80867 | -59.44333 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f76363a9-95ba-390b-89c0-b7ce49ed9814 | -8.54898 | -54.74139 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 640d911c-53d3-3e7b-9876-11b05ce3306a | -9.39626 | -60.57261 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e33219c2-e923-3b87-87d5-866b3c62375d | -8.53164 | -54.74827 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ffd546ac-ddb3-3e91-acfe-df0f48274be3 | -4.28103 | -60.85239 | 2026-08-19 05:59:00 | NPP-375D | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e50c7c61-5549-3dbd-a571-16ffa3794bff | -8.56245 | -54.72197 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| b2eedaaf-2d53-345d-9897-504b90e24e83 | -9.39885 | -60.57172 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b5087ed8-6dc1-3942-a16a-7991ea7b3a2b | -6.75262 | -59.15655 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| da0f0408-9a61-3997-82f8-c854ab230bd5 | -8.55042 | -54.72955 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 04c488d6-c12c-3a2f-a685-33e0e208b46f | -8.58274 | -54.7243 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2f24a6c1-4c88-3e0a-b4c0-15df77e165ab | -7.47309 | -60.04852 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f91efe4b-2b4d-3a86-bd19-d2170c6354fd | -8.58496 | -54.72752 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3ada6f4f-77b2-3bbc-8086-fe3be56078f7 | -5.49673 | -60.13816 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d36452bd-7c8f-376a-a5be-7868b45e5755 | -8.55645 | -54.73637 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1b73ee5c-b1df-333b-8e5b-90123d5a1843 | -6.08471 | -57.91575 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 676f4395-154a-3455-845f-add4766731ee | -8.53992 | -54.73708 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 3984fd89-2e6a-3b41-b745-1f1376ed9055 | -9.10965 | -60.39037 | 2026-08-19 05:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fb696dcf-1531-3dc3-9cc6-9fea7bcd36a8 | -6.00731 | -57.86048 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 1ea174cc-d1bd-3d67-bba0-71db2dcb3c34 | -6.79825 | -59.44715 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a61811ad-a5ce-3c6a-aa77-40af4199ae98 | -6.12519 | -57.70832 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3a7f7777-7156-334e-b623-078f202ca4eb | -6.63158 | -59.075 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2b390c6-4a9f-3c2f-8bf9-1ae1293f59c2 | -8.5684 | -54.7507 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4a9f5a06-6b77-380a-bdeb-db8ca0fa92de | -8.57674 | -54.71759 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e72d3e94-4ee6-3057-a348-1bbf1833f197 | -6.88103 | -59.03787 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5089a0d0-b541-303e-943d-b90a5f93300c | -6.88664 | -56.43907 | 2026-08-19 05:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8340068b-719c-366d-8dd1-49750ed2e00b | -5.4922 | -60.13747 | 2026-08-19 05:59:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5c280136-2431-3bcf-9a00-d2606b3b587c | -6.79267 | -59.45171 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 37773f11-de36-3cbb-83f1-6ff0d03e47ee | -6.84399 | -59.01481 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a6fd75a7-bd0a-307e-aed2-8bc8578c6c0a | -6.10459 | -57.73706 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 229a701b-dbcd-3c59-97d2-ac591f6b378c | -9.42196 | -60.40883 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df0617d8-6338-3adb-aea6-a24f75329649 | -9.40289 | -60.55857 | 2026-08-19 05:59:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6920eee2-b894-312c-ab77-9c0920eb2a39 | -6.84581 | -58.99824 | 2026-08-19 05:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a2adc276-c61b-3f04-99ff-2ff3659d995c | -6.02576 | -57.80827 | 2026-08-19 05:59:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbe56d08-195f-308a-a2fd-c554f744ef15 | -8.56765 | -54.7348 | 2026-08-19 05:59:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |


[Clique aqui para ver as próximas entradas](README67.md)
