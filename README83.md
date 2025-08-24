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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 91897882-c0d3-3217-9aae-9ad204d122d1 | -22.04857 | -53.82534 | 2025-08-24 05:25:00 | NOAA-20 | ANGÉLICA | MATO GROSSO DO SUL | Brasil | 5000856 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f52b0cef-3819-33c5-9268-6100db313ede | -8.67978 | -62.87896 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bc7c821-505d-38df-88b4-2efbe0dd0e1c | -8.86837 | -62.42433 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee9a8364-0ea6-3470-ad22-36b4aaf544dc | -9.23183 | -60.92488 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c93750e0-1ff9-3db4-a9ef-912aa239933e | -11.32763 | -47.86586 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 40a8ac0e-92cf-31f2-befa-7a5aefac1a8d | -9.05037 | -65.72131 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c71cc8d3-d44a-3a4f-ad6c-f05948c0c0c1 | -9.21482 | -59.7826 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ee0e69d-b2d1-3c51-9f05-5fa2a8c8498c | -9.20508 | -59.4775 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2bccf3ff-df12-3f29-be27-a53231530d6a | -8.9024 | -62.41838 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e67c884-f837-32c1-87af-9cdb373528b1 | -9.0307 | -59.01307 | 2025-08-24 05:25:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5df34cc4-77eb-3786-8517-aaca2b1ac9ea | -9.018 | -65.3856 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 400c9648-43ed-3892-8a56-67c07a6ddb3f | -11.18152 | -55.02997 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 92628a8b-0607-3dc6-94d4-8e974e9b3884 | -9.00586 | -65.69584 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 898491b7-00c2-3c99-81b9-791f3d296e84 | -18.02497 | -51.08519 | 2025-08-24 05:25:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 68fac882-2464-306f-8371-937ef1bb337c | -9.20127 | -60.79481 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 02a67897-9fec-32eb-901c-7b629704809c | -8.24026 | -61.46214 | 2025-08-24 05:25:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 38be70b9-d6c7-3bbe-8285-0ebff841f09e | -9.00634 | -65.69839 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| a13b6880-676e-35e7-9e36-dc7c8e79e65c | -8.91304 | -62.41643 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6a8ecae5-8c15-3e5a-b31e-aa00648082be | -9.01847 | -65.72083 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87009f59-3ad7-3269-9dd8-09961edd145e | -8.89788 | -62.425 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b65041e5-052d-3b64-9026-564a3294ff33 | -9.20237 | -60.78782 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| e28fc02b-2977-36df-95fc-2a319920b416 | -8.90505 | -62.44457 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5e7716b-a862-3a9c-8d29-9d113eda6994 | -11.31837 | -47.85394 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 872160f1-edc3-3ea8-a839-a190687dc2a8 | -9.15964 | -59.45531 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 02dd6399-7b0b-3462-bc18-6f222ef94a80 | -9.37268 | -63.44714 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d36cd2f3-36f5-32cd-b9b0-90f3d5d056b0 | -8.89614 | -62.43575 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ec4511aa-4e24-3230-b34e-018285df52f8 | -9.21752 | -59.62272 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9c08ad5-2b32-3a4b-8fa5-521c905ff32a | -9.19847 | -60.76929 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 339fa1ae-0bde-368b-9102-dc6f101e35c9 | -9.16477 | -59.46749 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a063c06-d078-3272-9f13-7e43977e869f | -9.95842 | -60.18149 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3917a9bc-349c-3b89-b943-13457b2f4fda | -9.15234 | -59.50341 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95bc6d4b-4d6f-3fbe-9649-50101865fc66 | -8.61336 | -62.59396 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 75804e70-db72-30c5-a165-294aa427d407 | -9.52363 | -60.55461 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f48c73ce-e822-34cb-949f-d0befe105bc2 | -9.16871 | -60.80756 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 9bf38edc-47ff-3eca-8217-eeaa156b21bb | -8.884 | -62.43425 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 022be95d-8a82-3f89-b798-8db6018da6d8 | -9.51686 | -60.51018 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de097325-0c24-33c5-a89c-d7440eb181d1 | -9.0119 | -65.68931 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| adf9c953-033c-356c-85eb-4ab77128d607 | -8.90841 | -62.44512 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7c8ff5b8-f0d2-3977-b348-3297c0cf95a2 | -11.31416 | -47.85741 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 8395ca4b-f859-3107-a4ec-a7e6a2efc855 | -11.51206 | -51.88225 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 965c8de8-445b-333a-8baf-f0c3a11b568c | -8.61161 | -62.60484 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d66d9345-ed13-33cb-b554-d7a523f05857 | -9.00116 | -65.7001 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c2d21ba-ffef-3f3c-ad91-f4b47997da3e | -8.9645 | -61.67155 | 2025-08-24 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| eab8513c-0666-337d-a5de-d2044d13c18b | -20.3385 | -51.70579 | 2025-08-24 05:25:00 | NOAA-20 | SELVÍRIA | MATO GROSSO DO SUL | Brasil | 5007802 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0ebe86c-4f25-3826-946f-ffaa7fe9bf55 | -11.17887 | -55.03185 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c0f1eb6d-3aa2-327b-b0a1-c2d9b47c18df | -9.51302 | -60.51692 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5a764500-ca4c-3dd7-87f2-cafd73f74c15 | -8.60914 | -62.64178 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 13487efe-6644-3ec1-8a2e-57b27c76fa9c | -9.19356 | -64.55539 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| daa02fc0-c2aa-3474-bf74-a6c9604b0e13 | -11.54273 | -51.90928 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5d7afee6-b4a6-3c5d-8d98-1ec19b88610e | -10.29669 | -60.53774 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6723cae4-829e-30fb-94e5-6da25f5f87be | -11.31776 | -47.85952 | 2025-08-24 05:25:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9fbf7bb8-7f17-39c6-a6ae-bb11b9d0b762 | -8.99493 | -63.64033 | 2025-08-24 05:25:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 443faf39-33cf-3f0b-ba4c-8dd49ad7f880 | -8.673 | -68.6898 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4769930-afd4-3dcd-8000-ad7009624ece | -9.16816 | -60.81106 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 632e526b-7e20-3ba6-890d-776b436fd166 | -7.72991 | -67.06944 | 2025-08-24 05:25:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c04dfeb9-df45-3795-b5e2-72bedec0681a | -9.93988 | -60.50037 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| de8f001b-f71b-3f6a-bfa8-e77f29ba6e70 | -9.01498 | -65.38023 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c2cbdb58-f59e-36f1-9a6c-8c83e8260e27 | -8.58343 | -62.6077 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9b17b06-65d5-3f4a-b1ec-b8bc0c5ed3dc | -8.8795 | -62.44089 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9ab3e440-328b-34e5-ab60-83e718fa6730 | -11.51296 | -51.87484 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0c3a2ecd-0dbc-3d79-86cb-211200066b2e | -9.95676 | -60.19229 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0a1c136e-701f-36ef-bcee-26e39e6c8847 | -8.60719 | -62.58922 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 55154207-9961-3fcf-a50c-6ec6f951b0c6 | -9.25174 | -59.63131 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b181aaa-6702-3b16-9f59-bdb0b798369e | -9.15768 | -60.81297 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea8ce6ce-7953-3084-92ca-972c01c3037a | -9.40351 | -61.96529 | 2025-08-24 05:25:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8227040-6b0e-33d9-8d7f-55b53d681873 | -9.1495 | -59.49918 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f46a14bf-39a2-30f9-b41b-33db8fd4a133 | -15.67736 | -53.87903 | 2025-08-24 05:25:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 916fadf4-8b8d-3026-867e-185a846b71b6 | -11.52683 | -51.85441 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 7f3362df-ff44-3a00-b4c6-7c01b44dcd3c | -9.94266 | -60.50444 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 09aa8cac-eaba-39a8-8f50-f3f41c919c17 | -9.20404 | -60.79883 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 24e6252f-caa0-3e17-8988-ecda90e4381f | -9.45552 | -63.50403 | 2025-08-24 05:25:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b353e205-874c-38fd-b6d3-a1bf2a991448 | -8.43993 | -63.86465 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d13c7774-b4f3-3b97-b518-963f5794f3a4 | -11.53291 | -51.85123 | 2025-08-24 05:25:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| e74dd89c-7dc5-39de-a661-21fc628d5478 | -9.51412 | -60.50986 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16b89104-31cb-3bf6-9823-c6950552eaf3 | -9.19656 | -59.46482 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec37b93a-f30b-3cd4-acc2-fa3bca281ca1 | -9.0016 | -65.70266 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e2f15952-eb5c-3820-9c65-2c5739472e02 | -9.50969 | -60.5164 | 2025-08-24 05:25:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 08b1b290-63fd-336a-9ce5-0ad45dd83a66 | -8.90957 | -62.43793 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d208cc1d-6ad1-3747-afc7-091923b81204 | -9.15915 | -59.50446 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c9c1a791-a9cf-339a-ba75-05eb343a715f | -15.3196 | -56.15693 | 2025-08-24 05:25:00 | NOAA-20 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c4d2e47-63df-3f98-a674-b29239bd7012 | -9.01458 | -65.72015 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5ba47188-fed1-399e-8902-3f3d8d93ac17 | -9.02436 | -65.68646 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b5413991-e753-3910-83a6-20e21b457a8c | -8.24357 | -61.46267 | 2025-08-24 05:25:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72005161-7e83-39ec-a5b3-eb48d0cc9457 | -9.22263 | -59.75403 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35948146-b404-377a-b670-4198a10f3026 | -9.15799 | -59.48914 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 79be6ca4-d341-359e-a6c6-b4c71397ecfc | -9.02748 | -59.76887 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a31bfee3-e07a-372f-9632-9bc08d79e335 | -8.44414 | -63.86124 | 2025-08-24 05:25:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c602a9b-7fe0-38ba-8bd8-1dddc668a694 | -11.17703 | -55.02932 | 2025-08-24 05:25:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d757a20f-1819-35f2-9268-bcfaa9476724 | -9.0134 | -65.38965 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 0562d51c-3616-3bf5-a028-f4dea5a9aff2 | -9.20292 | -60.78432 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1dee7093-3f6c-393f-816b-d34b50ee7da5 | -9.24723 | -59.63813 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eefcb9a9-6291-3118-abb5-768e2b6192cc | -8.58793 | -68.15114 | 2025-08-24 05:25:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4553dd9b-f54c-3cdb-b6f5-38745c384a35 | -9.00737 | -65.37891 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 48bf2f8d-4c24-334e-b499-957877e5132f | -8.87671 | -62.43675 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 631731b8-6182-34f4-bf51-a009a3978a71 | -9.15856 | -59.48544 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c9b54c86-653c-3c15-a7c0-fe66e34b29b7 | -8.88179 | -62.42652 | 2025-08-24 05:25:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aada1fc2-3dfd-33a1-a4d4-54cec542cb8b | -11.73546 | -51.69989 | 2025-08-24 05:25:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a86f4948-ab91-36a2-99d6-a00b395207ed | -9.20736 | -60.79935 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 557db682-7e9c-324b-98b7-0eee7b0a5d8e | -9.16989 | -59.47966 | 2025-08-24 05:25:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 92aa5c91-4b3b-3966-aac4-282034cb4989 | -9.02102 | -65.39098 | 2025-08-24 05:25:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |


[Clique aqui para ver as próximas entradas](README84.md)
