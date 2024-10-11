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

## Dados Diários - Página 108

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 619503ed-d6cd-3cb4-bea0-bb9b7a9ea9a1 | -12.96824 | -53.51004 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c7de9dc9-89fd-3f48-b931-5d295333cb2d | -12.96821 | -53.50759 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 218501d7-654f-3a6b-aee3-bb724dfa0950 | -12.96206 | -53.50293 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c18b1c98-8ca8-3438-a7e7-1613969d6242 | -12.9614 | -53.50922 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebab37d9-7a86-3a9c-afab-0632e31642bc | -12.96138 | -53.50679 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b74690d4-883d-3169-a8dd-de8d070c9d3d | -12.88066 | -53.48431 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d97c2d16-667a-34d2-9650-1c13e6181efc | -12.87999 | -53.49065 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3b4d16eb-ff65-32a1-8ea2-0e0708f1fd1f | -12.87945 | -53.48467 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| a592cdcd-45fd-3e34-b839-b72df4b194a2 | -12.87874 | -53.49099 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5544f9f3-a60d-3a50-ba96-dd03b2890b91 | -12.87449 | -53.47719 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c751c7e9-bb7b-3117-ae87-78d22f195490 | -12.87381 | -53.48358 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 94f8a513-af40-33d2-bfeb-34cfcc07fabe | -12.87332 | -53.4776 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c0f36300-3fce-3d82-b8b1-82ed5fb47961 | -12.87314 | -53.48989 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 40b5ee71-0216-382c-81e0-0df736e622f2 | -12.8726 | -53.48396 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 2e1bc739-84bb-3570-bd3e-6770e103c7b2 | -12.87189 | -53.49026 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 5f853b8a-d61a-3893-a308-f5e2da841608 | -12.86763 | -53.47645 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 196be7ba-f12a-3530-89fb-15ca057b8f3c | -12.86696 | -53.48281 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a0b50fd9-b061-3b30-bbcb-9ed2c128acbb | -12.86646 | -53.47687 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 124d65ac-00ef-3f13-acb9-db2adc4907a4 | -12.86629 | -53.48911 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 6eb62edf-690c-3b41-a95b-53416e0f0d26 | -12.86575 | -53.48321 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 959319c3-0063-3990-95df-d4de6b2e5ce5 | -12.86504 | -53.48949 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| b8bc6f84-cb76-3d9f-80b6-07f1b143b5a7 | -12.86434 | -53.49575 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 89b628b1-5ac3-3e76-a763-43d617870c02 | -12.86078 | -53.47566 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| b9c4981c-1164-35f7-b24a-92b005470270 | -12.86012 | -53.48202 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 58bbac76-a3da-34da-bc43-a5dc1380c1cf | -12.85961 | -53.4761 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2b683abe-6946-3343-98b9-ef7ba859a4b4 | -12.85945 | -53.48829 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 45408f97-458f-3537-b8ff-34f3374daceb | -12.8589 | -53.48243 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 2d2bf2d8-8bb1-3c89-9f90-63fb285b20a7 | -12.8582 | -53.48869 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 8988eb46-0317-3de4-8188-c749c8182812 | -12.85394 | -53.47487 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| cf74a7f0-f71a-3a6d-9298-6c52c526157f | -12.85327 | -53.48118 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 21.5 |
| 780b06e4-d124-3741-acf6-2f0359d59be7 | -12.85277 | -53.47533 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 6f0ac85d-93aa-343b-b723-6139e305934b | -12.85262 | -53.48744 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 61eae1ba-f60c-304c-b987-d6e3b71f679c | -12.85207 | -53.48161 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 62d100c1-b390-33d8-b2c4-9c9a854e7064 | -12.85196 | -53.49373 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 1805de39-f3cc-3446-9176-c0c55928ada9 | -12.85137 | -53.48788 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 9b581782-16f7-3f1f-ace1-ed4bf68d9dab | -12.85067 | -53.49415 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| edc620ac-559c-3aae-b9ef-961f720492cf | -12.84709 | -53.47401 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 56a6a9ef-9e25-37a8-b328-624988bbe85a | -12.84643 | -53.4803 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 4a010631-031d-3a9d-88c0-3d531e41d7cc | -12.84592 | -53.47449 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 1a41fd4d-3f9d-3f93-8453-33d352df87e7 | -12.84578 | -53.48659 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| e5cddeb6-f0a1-3f4c-aed2-733e23288631 | -12.84523 | -53.48077 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 6092d69f-0c96-3053-8d48-c68509b14d65 | -12.84512 | -53.49287 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| 85b55b41-3075-34a9-b08b-eeda075a0518 | -12.84453 | -53.48704 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 4ae1d9cb-0d3c-37bd-a4f2-9e4db5c62f0f | -12.84446 | -53.49916 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 137d10f7-de28-3eff-afb8-d972f48e8578 | -12.84383 | -53.49332 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| e25c36ac-17a7-36d8-bd8a-e5f9d056a9d6 | -12.84313 | -53.49959 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 33b4baa9-323f-349c-a316-f6cfd71b0e46 | -12.84025 | -53.47313 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| ea0d760e-d11d-3ab8-8b0c-8a7fd8fa8757 | -12.8396 | -53.47943 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 27.8 |
| 73e25620-b14a-3809-a604-c7c7fbc01ea0 | -12.83908 | -53.47365 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 13b45110-0dab-3a03-a8b2-f87c66f13be4 | -12.83894 | -53.48571 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| c591eb2e-fafb-3378-a5bd-bd80f6bec39a | -12.83839 | -53.47993 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 03cfe135-45c9-3d18-aed5-92572be731b4 | -12.83829 | -53.49202 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d2d8a75e-79cd-34e4-8e79-cf7360238429 | -12.83769 | -53.4862 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 21ef884d-bd73-3c65-8743-aef1598120d6 | -12.83763 | -53.4983 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 84304013-4990-3c78-85fa-1a88d14c4c41 | -12.837 | -53.4925 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 95b8e890-07b5-39c9-be12-09a8e3bdfa39 | -12.8363 | -53.49876 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| cf91e06c-62a5-37be-96ae-48cc7f5decc3 | -12.83342 | -53.47223 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 5b6b0027-7aa8-3b45-abab-6addc5af5e65 | -12.83276 | -53.4785 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| d5d78d26-3b14-326e-8a90-861c6e366add | -12.83225 | -53.47275 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 47727ca1-256d-3375-bc79-3d8f5161087c | -12.83211 | -53.48482 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 9a4fc235-4e22-34e5-a57c-eced0e5c9f11 | -12.83156 | -53.47902 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 0d038e0b-a66e-31da-bc62-9a9bc11f52bc | -12.83145 | -53.49115 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 29.7 |
| fe02d9c4-d6c9-3cf0-8ac4-388b69eb028a | -12.83086 | -53.48533 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.1 |
| 911b293a-ce82-3356-8003-622a7797ea36 | -12.8308 | -53.49744 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 25.6 |
| 6ac4e4e7-4fb4-3fc6-a90f-53481fa2c1a4 | -12.83016 | -53.49165 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 831dfb22-01cd-36d5-8db9-8b9845fc6f3c | -12.87587 | -53.46419 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| e2f592ab-d5fc-3b81-8e5e-c18f468859b5 | -12.8755 | -53.45819 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3e4483ed-0210-3488-95b1-e784136aae31 | -12.87478 | -53.46462 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c8bdb71-5628-372b-b6c4-5d3826a343af | -12.87405 | -53.47112 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 9e512674-0b41-3089-bac4-62b64d0bdbfe | -12.87036 | -53.45067 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d9d4fb32-5794-35e6-aa23-b07aa2571731 | -12.86968 | -53.45713 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cbdc5679-1060-33c2-af76-6fd075d4684c | -12.86935 | -53.45116 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e87b49df-21c0-3734-bf8f-625274416db2 | -12.869 | -53.46354 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2e64c549-b0d7-36b5-ae9e-f0c0346b5098 | -12.86863 | -53.4576 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 0a7deb6c-37de-314a-beef-3f0d98eb998d | -12.86832 | -53.47 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4578f780-5a27-3dd2-b2e2-85695fe02cc8 | -12.86791 | -53.464 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2c43276f-7921-3c1f-a55c-ec8ddc9890f7 | -12.86719 | -53.47043 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 98cee10d-3165-3296-9cba-65cc00a71953 | -12.86347 | -53.45013 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 104d96cd-32f6-3309-b2b9-2f106b702701 | -12.86279 | -53.45657 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 5d72c636-106f-3ff0-9c06-06e51365038e | -12.86246 | -53.45063 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| e41d6fbc-5887-3fa2-a0a4-f2f168bb73aa | -12.86212 | -53.46293 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 328d368c-a25a-3566-9610-afeadec35c16 | -12.86174 | -53.45706 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 839cec4b-37ff-33f3-8dde-3bbed486d0cd | -12.86146 | -53.46928 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3dda4ceb-5095-395e-8ce1-0712b783a7a8 | -12.86103 | -53.4634 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 13221ba8-c53b-3c2e-8286-aef56403142d | -12.86032 | -53.46974 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 13.3 |
| f410964a-be15-3790-abd2-123e7c45b1a3 | -12.85593 | -53.45585 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 68fc284f-bc64-3992-b87b-51fabd227982 | -12.85526 | -53.46221 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| d10cd971-8afc-3321-ae81-6360016852a9 | -12.85488 | -53.45634 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 52665328-e189-3956-ac54-109d446dcab3 | -12.8546 | -53.46856 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 15.9 |
| f7a0172e-8ba7-3772-921c-1151be0ddd21 | -12.85417 | -53.4627 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 9f5ad320-5faa-392e-b104-ee90214a14a9 | -12.85347 | -53.46903 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 56947509-9644-34ec-bdea-f23d88ba53dd | -12.84842 | -53.46135 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ee8b50a0-1d48-3678-b590-ab1129fc974e | -12.84775 | -53.46769 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 5548d1ec-5d0d-3575-8aad-66c685e47a4e | -12.84733 | -53.46185 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 723d7d98-76d7-3136-a130-3c5dcc4b9507 | -12.84663 | -53.46818 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 23.7 |
| 2545498b-0ae2-37bf-b92d-f7e686fabe37 | -12.84091 | -53.46681 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 4a71d810-1e8a-39e1-ab94-7b8b7feeed13 | -12.83978 | -53.46733 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ebcd8fd1-5e43-331d-b77c-a773e2e9989a | -12.83294 | -53.46645 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| ab5e0406-951b-3b40-a439-3858f3af2244 | -12.64233 | -53.10469 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0d1f7a37-ee0a-383a-ab6d-304422f5ce27 | -12.46938 | -53.15609 | 2024-10-11 05:42:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README109.md)
