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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2944520b-af8a-3f63-8d46-9b289795ca2c | -10.20194 | -50.00936 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6dd8aa21-5f33-346f-b30d-b2edb1c17e22 | -11.10811 | -51.33855 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2a7602e9-26c1-3c59-8eb8-d8850567aa5e | -10.42011 | -53.83367 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f409ca18-6633-38b3-a8cd-570074844dd7 | -10.79609 | -48.73909 | 2026-09-28 05:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| f697d4a5-0e3f-3a80-8623-7b7af23da402 | -9.9769 | -50.16295 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 9e422f41-4620-3f2a-9d9b-5b105c41769c | -8.93233 | -62.37095 | 2026-09-28 05:29:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 68ca8059-83d8-3fe0-847c-50bdfe12b4f6 | -6.16355 | -57.70214 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e28c9298-c9c1-3b24-a93f-a46aa81648c7 | -11.11391 | -51.33931 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2418d9ce-25fd-3a5f-a0c0-2d8c8826faaa | -6.63639 | -59.95066 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d45166f1-a8ef-3159-9790-60e340abe3ea | -6.16294 | -57.70625 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd21b3ad-b65a-3774-bb54-ddda37924c8d | -10.22877 | -49.99773 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5435b729-3684-345b-8e1f-3324fe1815be | -10.21191 | -49.98052 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4840394f-a576-3dbf-a7fb-f4516041fa11 | -6.88069 | -59.88766 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10009e29-8fde-3f18-9708-e94711a9077f | -4.98011 | -56.14981 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e843e33d-e359-330d-b19d-ac4e7d7c19dc | -7.55954 | -61.35363 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8a95d5b2-c22f-3ec8-89ef-e2b6883a55e4 | -10.89694 | -50.69382 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2466369-8889-33a5-a9d4-8eeb23b3973c | -9.9929 | -50.13578 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e3f5d202-61ad-3611-9382-cdf0925c1aa7 | -6.78822 | -59.38839 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c823e38-5eb1-376b-bffd-cb707ec71e88 | -10.00558 | -50.13068 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| a79df835-c87a-3dec-9079-eee5f307a809 | -6.69876 | -59.96366 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56763a57-b370-3077-bf01-a96148dcc2f9 | -11.11378 | -51.33774 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8a86b0eb-d557-3be5-9119-dcb3a359fb1b | -9.93597 | -50.23976 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0f972ae5-a1c0-335e-b43b-79eb11245dfd | -6.89122 | -59.84237 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4aec0f33-b591-3a44-b83f-ff415014d92d | -9.97626 | -50.1659 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 662f9479-9cd1-380e-bfd8-de25291f6766 | -10.21066 | -49.9904 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ab35885f-1f2f-37ec-b101-9d73df0e1b73 | -4.98779 | -56.15104 | 2026-09-28 05:29:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19e71d5d-4312-34ea-a09e-8f663f0a10d2 | -6.06498 | -57.82909 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4e99f856-c319-3f8e-a34d-01c8d566db3c | -7.27441 | -55.58207 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3daf38a-0fb4-38f6-98d7-cd4de3d2cd3c | -8.73254 | -47.98345 | 2026-09-28 05:29:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba45f6d2-d2db-3b3d-9cbe-b8e29a414428 | -9.98415 | -50.15228 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b62453ea-b535-3766-af03-3147065a4d3a | -7.68189 | -54.85075 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1c5676b6-9b7b-39c6-b007-d1fbbe425b45 | -6.78763 | -59.36988 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c617b541-6bfd-3535-a4e9-01afb8a74711 | -11.10903 | -51.32876 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2bb75dd0-9d0d-39bd-836f-9785f5a2e75e | -6.85292 | -59.91219 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e3b0e470-2864-3b95-8603-d79fcb678e5e | -9.98612 | -50.1398 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c667d0ed-0461-3b2a-b1c6-126da97dd149 | -10.92327 | -50.67872 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f73e2bbf-0f66-3289-8f31-a1ad54f3639b | -10.22189 | -49.98729 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 647ad9f7-d774-37c5-a54e-5140557eb541 | -10.79414 | -48.73705 | 2026-09-28 05:29:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| d130278e-a3e8-3003-861a-a1e90d571d0b | -11.1086 | -51.33442 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6e7b8f76-e498-3833-b4b1-fe6245661c57 | -6.77977 | -59.37603 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fb175538-cbf3-35a1-a2c4-9de94b9e530b | -10.21564 | -49.98644 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7a31d6f0-340d-328d-99d5-5852bbf1d57a | -10.21566 | -50.00106 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 251f5474-0c82-3abb-8a3c-606a5c4054b4 | -9.98673 | -50.13501 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 725199da-a4bc-392a-8d31-4ec9d6b7745a | -9.60146 | -62.3954 | 2026-09-28 05:29:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4e8adace-50bb-3e90-857f-afe8b252bde8 | -6.84849 | -59.91868 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3b8cadd-8631-31c4-ad40-23bd4e3ff736 | -10.25658 | -57.73969 | 2026-09-28 05:29:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 469611cb-914b-34ec-9b03-9aacd5327742 | -10.93645 | -50.67117 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b92359fb-cf67-3074-ba2c-61f2db38e07a | -7.05981 | -55.4862 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67d6119f-482e-3293-b710-b670679155c9 | -10.20705 | -50.00539 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff01f206-00f6-3602-82c5-10bb277ddced | -10.42425 | -53.8397 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e0c048c7-63fc-3291-bc6e-23ddaaf42f7d | -6.78314 | -59.37655 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 55a4cc48-a249-3c7b-9cb4-32e7857d83c8 | -6.78147 | -59.38736 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c767331-2d7a-3596-aed9-47a24a59ac4d | -8.03406 | -54.89653 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 63223e1f-94b5-3ab2-9e6c-323544401493 | -10.20318 | -49.99948 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4d7d6b2f-80b1-31a1-b0f7-129673340c5e | -7.71637 | -54.76528 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 11f4dbda-16b3-319c-85a8-5cfd94dca415 | -6.63694 | -59.94715 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a58d9b8f-b89c-3eea-b21a-4fb04523c36d | -6.16713 | -57.70271 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ae10e269-2e01-3d7b-ba8e-c169f974c017 | -10.21623 | -49.98149 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ec31980-2d30-3d1f-b98c-bb913fe57961 | -7.71575 | -54.76955 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bf832337-35ed-380a-b7a6-73b77c78e565 | -10.41527 | -53.83288 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0f6515ae-9985-34ff-90aa-7a6493252e23 | -10.01792 | -50.23405 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2eac47c1-7a50-3e6a-9aaf-89ba8591cac0 | -10.22378 | -49.98709 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 63af96f3-fe5b-3827-9c90-28317dbb4607 | -9.97629 | -50.16778 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 410cb211-3943-3988-96e6-f072154e6374 | -8.61126 | -64.0651 | 2026-09-28 05:29:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9bce79a3-6823-3181-838a-2deae684987b | -9.97751 | -50.15816 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| bf6f9987-c46f-3b8c-9293-e4e0136395dc | -6.07516 | -57.81007 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b2b165f9-6dc7-34b1-9b43-0f252fa63c2d | -3.93911 | -59.65276 | 2026-09-28 05:29:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0f4dfcb7-7247-3dcf-881d-60bd8e7555a2 | -6.00676 | -47.39674 | 2026-09-28 05:29:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c3dd9775-370a-3df1-8bab-798571c0e80e | -10.2088 | -50.0052 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 105ba17d-cff1-3e1b-a350-293893d0b9e6 | -6.64083 | -59.94416 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 376dfdc5-9084-3174-b5d6-d910f50c8e00 | -7.68131 | -54.85488 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 819bb2f4-40ef-3281-aa68-a51f10ae3d0d | -9.07117 | -61.44017 | 2026-09-28 05:29:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97f7b00-e206-34b5-991d-4a0464b0506e | -7.55568 | -61.33521 | 2026-09-28 05:29:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 985c5d93-f460-387c-919f-8a1f86020d2e | -7.8271 | -55.13879 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c60ef9a1-d6bb-3d33-a9ad-b0cc19e82422 | -7.4665 | -55.00365 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b0abb88-7fce-3ac0-a953-d552f55ce252 | -7.72895 | -61.24904 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 66ab740e-f9e7-3a36-a02d-734f158a070e | -6.07147 | -57.83421 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| af29fed1-277c-3be2-b23d-912cdca97c12 | -6.06266 | -57.82048 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b588d36-4323-3384-bc26-e4b87ccb529c | -7.71077 | -54.77314 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0bd77e27-cfbf-35d4-adcb-7e74f8719ab8 | -6.85237 | -59.9157 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a695e0a-5557-370f-a6ff-4cf566c16061 | -7.69386 | -54.76639 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b1d13111-4e8e-397b-a12c-43cd72cf54ed | -6.70209 | -59.96418 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 240e2bb7-2180-3655-ad12-5e02291515a9 | -11.12922 | -50.06092 | 2026-09-28 05:29:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 3ef66e92-1b98-3f30-b1c7-1518387e68c3 | -10.00648 | -50.12775 | 2026-09-28 05:29:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e5680b5c-55df-35c5-a044-9fa3325322ca | -7.2837 | -55.57605 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c93fea1-f87a-34b1-bbb3-5db87c4f47b7 | -10.89545 | -50.69147 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 60f5d34a-ce89-3cef-a548-fe7c7f1facd6 | -8.03781 | -54.90136 | 2026-09-28 05:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd5ae6b0-199f-3480-a98f-03b7d6e1b83f | -7.82342 | -55.13418 | 2026-09-28 05:29:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 201b6202-4851-3a3e-b48d-9536d582ae66 | -5.99983 | -47.39583 | 2026-09-28 05:29:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| e46388d7-749d-362a-9475-de7735c7f142 | -9.13934 | -47.98243 | 2026-09-28 05:29:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 02fd9a76-bc88-3eed-97ea-1f3d763ab4c4 | -6.87402 | -59.88663 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9a772a4b-9bc0-37ee-b44e-8d972cb5a8a0 | -6.17133 | -57.69916 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a41db781-5f4f-31b6-94d9-7fb45703bd5d | -11.11431 | -51.33362 | 2026-09-28 05:29:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 04e15a5a-def9-3f89-9422-7f94da70fe40 | -6.07871 | -57.81065 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6a16785-0379-3c57-bafd-0ce8cdc28652 | -6.69543 | -59.96314 | 2026-09-28 05:29:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b73bc51c-56ec-3c77-a121-e020f45924fb | -10.40771 | -53.81513 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 94880632-9fd6-3341-b5ea-bb79049fe0f7 | -6.15935 | -57.70572 | 2026-09-28 05:29:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c274e11f-fd1f-3da7-b04e-d0ed12c4cea8 | -10.41599 | -53.82745 | 2026-09-28 05:29:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ed2141b9-b951-3c7e-83f1-2511c7ba5105 | -6.77921 | -59.37962 | 2026-09-28 05:29:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c8f84990-ef4e-36a3-aa5e-6cc4e4791c9d | -9.60473 | -61.82288 | 2026-09-28 05:29:00 | NOAA-20 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README65.md)
