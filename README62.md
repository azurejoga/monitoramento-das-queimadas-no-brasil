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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c3f728ee-5c80-33e5-afcc-5ff1af851e1d | -6.93704 | -58.96051 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b409fb0-3435-3cab-a609-67bba09b8977 | -6.40812 | -51.67606 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 944f3df2-5ffd-34a9-b410-a7f882a83e10 | -6.09351 | -57.71957 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f12ffe4a-c483-3f86-9e6e-08eb585c5fd3 | -5.22321 | -52.02108 | 2026-08-29 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0cec07bc-33e0-3c3c-8a06-275560fde1c3 | -7.36655 | -55.17682 | 2026-08-29 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 108bd2d6-5fa7-3b2a-9ecb-949eb026ed91 | -5.99071 | -57.68388 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1a7ab812-cf11-3a03-9625-fd0f463a3792 | -5.7796 | -57.58881 | 2026-08-29 05:36:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c513fca1-9dad-32ab-bb70-eed3b5f5fef8 | -6.94716 | -58.94767 | 2026-08-29 05:36:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4ec4fb2f-d5b3-3af3-8005-91f5d4e9b2de | -4.1523 | -60.68785 | 2026-08-29 05:36:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad465d63-9227-305d-9d2e-e4dd70fb88cb | -6.77493 | -55.67789 | 2026-08-29 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3140fb74-6c7b-367e-9c5c-4cee0836e16e | -6.77029 | -63.0472 | 2026-08-29 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b839ed46-772f-346b-9d52-603add8328e4 | -11.27279 | -54.04273 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9f6262f0-460d-3bed-8e5f-a5eb487064f6 | -11.22731 | -53.99092 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a9da5c1b-8353-36d9-b3d2-91c9b4b73e84 | -11.71744 | -54.52873 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c464ec5-830e-3527-a02f-d933df6644f0 | -8.59103 | -54.79451 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41434043-c0a9-3ce4-8cc5-b83118d19d81 | -11.26685 | -54.0418 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b1a1e56f-a2f4-3791-92b6-0c9eb6ed7512 | -11.26426 | -54.03575 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ef488453-f2ee-32c2-8827-f626e934ba3f | -8.99894 | -65.43343 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85e90ca3-f78a-306b-b98d-56d7817129e7 | -8.63278 | -66.53828 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6e0a0df5-b75c-39ea-9e4e-96febe64f6d4 | -14.89882 | -56.33377 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d208e339-6859-3d52-9f66-cba5921b5ad5 | -15.12205 | -53.57525 | 2026-08-29 05:38:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 22.3 |
| 0af17184-7f7b-3b05-a299-3321d8cd1fb9 | -9.21109 | -51.5392 | 2026-08-29 05:38:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 38126cd1-01ac-32ab-89fa-2325936630bb | -9.06503 | -65.42221 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0d596cc6-8f0e-3bcb-b065-b6937d6da57d | -14.92572 | -56.33712 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c94a0e6a-3cae-36f3-b96d-b0a9dea951a9 | -12.78535 | -60.48747 | 2026-08-29 05:38:00 | NOAA-21 | CHUPINGUAIA | RONDÔNIA | Brasil | 1100924 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4d3d5bd4-479f-30ff-bc2b-d54ee287fd67 | -10.46327 | -64.48752 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1256272b-a885-312b-9879-b9239f919d89 | -9.25762 | -57.08134 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6c6954e8-5292-3461-b335-71b50857dca9 | -8.95718 | -63.27674 | 2026-08-29 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b4fdc898-1f63-3d24-adbb-28ce3e477a3d | -11.26396 | -54.01455 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e2033291-6b87-3e57-b3d5-45c8fbfdc8a6 | -8.9967 | -65.44762 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e6df2e9-b4e8-3c3f-b970-ca214df1703e | -14.2024 | -52.85847 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2c4eea6a-327b-317e-bf6d-ffa6b00addbb | -9.93818 | -60.43366 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 27db2581-b0cc-3e7f-843f-fd1913f5f0d4 | -7.61578 | -61.36379 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38d97cb0-24ba-3f9b-a6d9-3a0982020ce9 | -9.50664 | -65.57745 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3f8fb6d2-4e4e-3d29-bb7d-64e32aeb06d9 | -8.59117 | -54.80058 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 83e7d3e2-044c-3074-8535-a086fe808f0f | -11.23928 | -53.99228 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4bc3572-94af-342c-8a73-1b8a369512cf | -11.26242 | -54.02786 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7eccb5e9-cccc-36a9-9ce7-b236d5361678 | -8.65447 | -62.84019 | 2026-08-29 05:38:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daff47c7-0568-3694-be6b-7cfd4963d5a8 | -10.4069 | -61.19996 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1995cbdd-3ad2-3c25-b792-0d8e94eaa138 | -11.72274 | -54.53361 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e6b6393-2766-32e8-aa5e-48631aef4a70 | -10.46604 | -64.49153 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4ce379e7-a69d-3684-af81-6ef94b302830 | -10.47892 | -64.49722 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd50570c-ffec-386b-b715-3082173e3127 | -9.13761 | -61.0098 | 2026-08-29 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc74064b-935c-3b9c-b3db-32c068da266a | -9.38854 | -66.51517 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0df16eb4-b193-3876-8fb7-6319377bd879 | -8.50376 | -55.32373 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d7c3e2ff-f0f8-3153-b8e9-0d325967a53d | -8.37927 | -70.85172 | 2026-08-29 05:38:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b79ba7e9-ac85-310d-bf3b-b9dd0f366aa8 | -11.23874 | -53.99672 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 7af4ec76-9130-30a5-958f-962013496cfb | -8.98837 | -65.43537 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7718c573-dabc-3d90-b205-986bd02daf35 | -8.87709 | -71.27046 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9fbff76-096d-3f8d-a625-3438ae9a6aab | -8.53775 | -55.26397 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c6ddcc50-4df1-31a9-b827-5a61f99c95dd | -8.59657 | -54.80198 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1805c731-4276-3b31-affd-e5965f2c1dd8 | -8.95283 | -62.3776 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 063d15e4-3298-3d35-b564-809540107d77 | -8.24839 | -70.10051 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 123cc870-66d7-3f0c-b941-57467d50a23c | -10.50865 | -59.63364 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25e74448-403b-3faa-baf5-6f24b8e095ae | -11.22517 | -54.0087 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb2d0a79-cb71-3d35-b5e7-baabb069d962 | -11.04144 | -57.2081 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| d21e89a4-2a81-36f2-91a8-8ecdf026c0e5 | -8.99838 | -65.43697 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 616f4071-2b9a-3d35-8986-71f8a1e53784 | -10.47561 | -64.49669 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7c657dbf-17e9-366f-9824-ca3a0832c633 | -11.72249 | -54.53876 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c33ad9f6-00ec-39a1-a2b6-8463f2298378 | -8.59938 | -54.7738 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 815dc0da-1666-308d-9c9a-76645499b9c9 | -10.41123 | -61.19612 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b866ba7-8a5e-353a-b0fd-38ad04693c71 | -10.48277 | -64.49424 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e4e5e4f3-fb7f-3828-90fd-f356a42b519b | -9.86932 | -65.02593 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 963de876-f5d5-3e7c-af77-6ff5e95be4a6 | -9.42985 | -67.40971 | 2026-08-29 05:38:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5118e8c-8900-3775-b4f6-9b03b15d24b4 | -10.50968 | -59.62638 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 00d0b51a-5b00-3adf-b440-ea0828e972c1 | -8.24905 | -70.09656 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a56bfa00-3c91-3311-90f1-a0cde78997ef | -7.92927 | -61.37107 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3b8fb17-7dd2-3079-9286-1c214cd12de5 | -8.53246 | -55.26316 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7d95bc7e-914f-3c5b-be42-66b0957ff3dc | -14.21026 | -52.84748 | 2026-08-29 05:38:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bd38e438-9737-3eea-ab9a-811a85b1f6a3 | -14.91247 | -52.61684 | 2026-08-29 05:38:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7ffea8a4-45cf-3898-bb6d-2c43a26e40d7 | -9.88634 | -66.99465 | 2026-08-29 05:38:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d338ecb0-104e-3126-825b-65dbaedd2226 | -11.27018 | -54.03678 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfe65773-4d28-3e8b-aa75-0f0ad3269bf1 | -7.58748 | -61.33491 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2a813f0-6bfc-394d-8ab9-7f6002be5b0e | -8.53861 | -55.26496 | 2026-08-29 05:38:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3281ee6d-0598-3501-80c7-ed437920d3ca | -9.9222 | -60.43624 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e1f406c9-e83b-3f6a-bb7b-8b027e107606 | -11.62802 | -54.58806 | 2026-08-29 05:38:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ea417728-9d9e-3ff2-be15-bf659dadf2f1 | -9.30919 | -56.79739 | 2026-08-29 05:38:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c5e2bb96-207a-31c0-9148-3f1c7accafcc | -7.00563 | -71.66306 | 2026-08-29 05:38:00 | NOAA-21 | IPIXUNA | AMAZONAS | Brasil | 1301803 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c5d26dd8-442c-3c16-b6f4-e219ad93c294 | -8.59754 | -54.79424 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7dc45acc-3d50-3481-95d3-6160df0d48fe | -8.98724 | -65.44247 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06aad459-5882-3671-8399-496a2fb39fd9 | -10.48554 | -64.49826 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 8629db8a-5378-3cbf-bc69-416b72053d66 | -9.9375 | -60.43842 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 04135c3b-01e0-3c8a-b901-72cd56823646 | -8.9917 | -65.43591 | 2026-08-29 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 890c5b83-57a9-3fe8-b361-7757f508610f | -8.95921 | -62.40556 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11df7768-ef5f-350b-8cfe-d258b4f16d6f | -8.6003 | -54.77239 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3888ca94-3ead-3533-a5d5-04948738ebbf | -11.19366 | -55.09143 | 2026-08-29 05:38:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8fdaf9c-69f9-355b-a52b-c84f5113a3ae | -7.59279 | -61.348 | 2026-08-29 05:38:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a6022df-63ff-307f-8f83-3aac7ad768a5 | -10.55729 | -59.61413 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bcbd0c81-350d-341c-ab9f-7b05a4bb9284 | -10.39312 | -61.24274 | 2026-08-29 05:38:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51a34ea7-05cd-3aca-97fd-0779ff4402a7 | -10.75449 | -54.0387 | 2026-08-29 05:38:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3e2f79af-a803-3bf4-836a-de577cc8c8c2 | -8.58938 | -54.76514 | 2026-08-29 05:38:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9c52bac7-b157-3020-847a-61879209f88e | -8.60722 | -70.21268 | 2026-08-29 05:38:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ff8b9316-7731-3e3d-afb3-4bf99d677c35 | -10.05691 | -68.83864 | 2026-08-29 05:38:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb6a512b-e8da-32b2-9a78-10365015ff3d | -14.90339 | -56.34145 | 2026-08-29 05:38:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 890b67a1-f508-3063-aa02-9419df0570a8 | -10.55273 | -59.61724 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5c48211a-e932-3f2f-9340-c1b38b0b5785 | -9.88531 | -60.26664 | 2026-08-29 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 32583b7d-311c-3370-a76a-433c555ccc14 | -10.48223 | -64.49773 | 2026-08-29 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 9511c341-3fde-36d6-8ae3-1b3fca6cc73e | -9.51609 | -65.58262 | 2026-08-29 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 051e8b76-5b59-37c7-b2af-3c01ba7ddb21 | -11.03107 | -57.24989 | 2026-08-29 05:38:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 91d4363f-7f9c-3267-b68a-39d9b1bbe5a7 | -8.95171 | -62.38514 | 2026-08-29 05:38:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README63.md)
