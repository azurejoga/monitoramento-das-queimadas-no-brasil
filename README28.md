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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e334fdbd-1f00-3424-bcde-1be3ca2b8c9c | -6.17625 | -45.43429 | 2024-09-28 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 430a129a-60ab-3bdb-a24e-141076363ec5 | -6.17499 | -45.44099 | 2024-09-28 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 085f4d11-6d7e-3d86-990b-6fa75d6dc540 | -6.17003 | -45.44084 | 2024-09-28 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| fa814d72-2e2e-34ae-84f6-52527cd6325c | -6.1679 | -45.44013 | 2024-09-28 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 26ab9e21-99e9-3847-8dd0-e98eacb467a6 | -5.765 | -45.55003 | 2024-09-28 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 055122a9-36b0-3e69-9a9c-2e6c06aace13 | -5.76371 | -45.557 | 2024-09-28 03:28:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e29ff3a0-8629-3a17-979a-3a864bf0ff26 | -5.32836 | -45.43062 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 838d112b-e64a-33af-aa9d-2dba599f3723 | -5.32701 | -45.4382 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ad0f50cb-3ef0-3f21-a913-034794504907 | -5.1954 | -44.94244 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 821ba90a-552a-37d1-91bf-64e3f2183b13 | -5.19478 | -44.94215 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 0e8ddbf6-b287-3cd2-a9ad-456c6487575b | -5.19429 | -44.94867 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c79d0f29-1cda-3afd-b253-28c8d734206a | -5.19365 | -44.94831 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3da791ce-bb21-376b-b6f5-d9e60b7e5701 | -5.19317 | -44.95501 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 04d5da0c-8ebd-3139-9543-96627436267b | -5.19249 | -44.95458 | 2024-09-28 03:28:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 086b927b-d637-30ab-b00f-c1e03ab05b43 | -7.83128 | -45.48864 | 2024-09-28 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 2e1007c3-1545-3f4c-ad27-ae79db9f3da3 | -7.82064 | -45.54444 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2c2a74d3-4a78-366e-ba1a-0a87e74ff857 | -7.81953 | -45.55024 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c6df69c7-c6bf-35a4-a509-d6adf7b712d5 | -7.28737 | -46.14332 | 2024-09-28 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f5719ff5-5384-3433-9aae-5e84e39ab3ee | -7.28601 | -46.15049 | 2024-09-28 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3007ff65-478c-3f12-9e47-e6f035888bc2 | -7.28276 | -46.14176 | 2024-09-28 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| febea2e8-d7e5-3875-ae16-d330018958da | -7.28139 | -46.14868 | 2024-09-28 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cd4e506e-9390-399b-9074-85c628c8d4bf | -7.14243 | -45.44358 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 8395abcf-656f-3086-95fe-d36a42994709 | -7.14241 | -45.44193 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| afe605e3-aaf3-3e8f-a19c-a165b6b72648 | -7.14114 | -45.44855 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 87e05b16-e7e4-3302-9d1e-9b3a55a27f9d | -7.03231 | -45.34767 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2c36cb84-b4e6-3a45-b4d4-98e7516ce777 | -7.03218 | -45.34743 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d81cf569-a606-351a-b915-a698f1eadbfe | -7.03106 | -45.35437 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c2694d3-c5aa-3766-80b3-6e66e77fa1ce | -7.0309 | -45.35412 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| fd530106-bd58-3ac8-9d2a-fb9a40ec8b99 | -7.02548 | -45.34609 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8403b446-3226-3cc8-ba6e-4b16582cbf65 | -7.02536 | -45.34587 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 40662b72-9b8e-33f0-b41a-71f237545fdb | -7.02423 | -45.35284 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fa600c7b-f2e1-3392-821c-e3e0f36b2bfa | -7.02406 | -45.35262 | 2024-09-28 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 99332534-880b-3bb7-88eb-d4eefa6b1a7e | -6.57782 | -45.71931 | 2024-09-28 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| c6d02915-0e8f-3985-9338-59d9882e7513 | -8.88389 | -45.6465 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6beaaf3d-af78-3600-8586-9e574a1a4187 | -8.87814 | -45.64561 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a34c3057-9f58-32f1-908d-e1f27c2619f3 | -8.87695 | -45.65157 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1458a1a2-29d9-33a0-87b4-aa8ca2713a27 | -8.87589 | -45.6514 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 264dba65-3b85-3061-9636-212e1e509d6a | -8.8757 | -45.65776 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 40a2e498-c6bd-391b-9ec3-5b05502db353 | -8.87468 | -45.65762 | 2024-09-28 03:28:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3debe28-198d-3788-858e-7acaac2b81bf | -10.65005 | -46.06154 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c180b4bc-92b2-3333-b523-b7cb8b59e656 | -10.64662 | -46.05306 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| d3bcea24-e7ef-36dc-b04b-b19aa324dc00 | -10.64589 | -46.04718 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 4fe21a51-c793-340e-9160-db1cb1468e0f | -10.64529 | -46.05952 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 40.4 |
| b302567c-c322-3e48-9a64-3bc72fd9675c | -10.64459 | -46.05371 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fbcb0ebc-9d8e-3865-b392-e9dfd67be764 | -10.64396 | -46.06601 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 7c3543db-ede1-3a28-9e55-bb85e6ef25a9 | -10.64329 | -46.0602 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 43770271-0284-3cc9-99fb-835937dea2b9 | -10.64262 | -46.0725 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 0c468434-def2-3073-8741-487b9042a9c7 | -10.642 | -46.06672 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 01ef4b9a-b71a-353c-a3b6-026170d21057 | -10.6413 | -46.0789 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 37437cba-1a06-30d6-a360-77c6c3921c53 | -10.64124 | -46.04509 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| c9bc577c-b37d-3580-8e04-54182de20bb0 | -10.64071 | -46.0732 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e13597e-9e1f-3ac7-9480-f27890bfd8c1 | -10.64001 | -46.08517 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2d734d15-6af0-32d3-860c-8456febb1777 | -10.63988 | -46.05164 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| aaa7fda4-f474-3abf-92ac-91f3457431b7 | -10.63944 | -46.07957 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b26ae182-f9c1-3d85-9321-95a5b81ad7d1 | -10.63917 | -46.04564 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 2c9204bf-99ab-3635-b07c-59321b3693bc | -10.63853 | -46.05819 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a2fd0e76-227e-3845-b5de-8e0fc32fb693 | -10.63819 | -46.0858 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c88b32d7-2fd7-34c7-ab43-83883ec2f43f | -10.63785 | -46.05225 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 50d60acb-3b4e-3dd7-8831-53a4e989af38 | -10.63719 | -46.06469 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 45a5c981-176e-313f-8263-e103299f4426 | -10.63654 | -46.05882 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| 81e2eb8d-4d50-3ea4-885c-022cbeb62100 | -10.63587 | -46.07111 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 1faad822-b1e6-35fa-b192-363b5fb69bf2 | -10.63525 | -46.0653 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.5 |
| cca85f85-bf8b-3827-be4e-d1cde64c9290 | -10.63458 | -46.07732 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f3f2408f-53e8-39b4-b277-fd4bb6167238 | -10.63398 | -46.07167 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 0d41f7c5-d2e5-3923-9952-d7c00ea1f590 | -10.63331 | -46.08351 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1783f5d0-802e-385d-b4d0-231be68ba732 | -10.63274 | -46.07785 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3e9ac571-3060-34b2-9b13-47df488d3f5c | -10.63205 | -46.0896 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7aea1619-c909-31f1-a1cf-607c1baaee2c | -10.6315 | -46.08408 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2be86585-c821-3332-8843-24b1b34183de | -10.63028 | -46.09019 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a4c88bae-bb94-3a41-85eb-fa62d18ef411 | -10.6279 | -46.07558 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ab0e70f0-cf93-3045-946d-da7d13c35ebc | -10.62663 | -46.08172 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1e3f354d-6c6b-3efc-bce4-ce62f0b8c7f1 | -10.62605 | -46.07608 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1f453a92-f014-35f6-8bcc-08ad7b243c6b | -10.62534 | -46.08796 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c5608ada-5418-3be2-b0b8-c2230c4d666f | -10.62482 | -46.08226 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1979c133-47a0-31af-b98b-89eaa4b4e67a | -10.62248 | -46.06774 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| cdbc2e0a-a565-34a7-bd12-b4079411fad1 | -10.6212 | -46.07388 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 63144dc9-de92-369e-909c-eb14e678fb02 | -10.6206 | -46.06821 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 814386f3-0713-34f2-8658-0d92dd72f6a1 | -10.61995 | -46.07996 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c3f3bc58-4f59-36c6-955c-20bfa7478d3d | -10.61936 | -46.07436 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d06770dc-6e88-39cf-b6ab-cc5b545e8621 | -10.61813 | -46.08047 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9344d57b-ef0b-3996-b177-28469c2b5aa7 | -10.61582 | -46.06588 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 5f852b36-03a5-3372-bf8f-2846e8e160b6 | -10.61453 | -46.07209 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 3175db3b-48b5-3636-9392-2e9dd0196e63 | -10.61394 | -46.0663 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4423e17f-a2cc-3363-8aef-851e72b75e29 | -10.61325 | -46.07825 | 2024-09-28 03:28:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1a7a7055-dc99-30ed-85f0-98c9195b8d06 | -10.59385 | -46.06123 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 617ee8b4-c9d9-36ab-aa71-62e5dfa7954e | -10.59254 | -46.06771 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f2b8d976-d772-30b2-a64b-dc529bc28229 | -10.58963 | -46.04734 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 200d45d9-4041-3071-9d5d-0c0773970a96 | -10.58837 | -46.05351 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7cda8df6-f6d9-3fbb-a9ac-4e8d5dedecc4 | -10.58414 | -46.03973 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 76f34876-3ca4-3867-a563-92df1e1d4606 | -10.58289 | -46.04587 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 90070acd-d9b9-300b-b7b3-bf1c12480a36 | -10.57904 | -46.06484 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 28b486e2-cc8e-313d-b2b7-f3e0c07b9084 | -10.57771 | -46.0714 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 024864c1-9aee-3ba3-9fa6-3a28344720ac | -10.57638 | -46.07796 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 39b36127-bec7-327a-9a9a-544e15b322c4 | -10.57505 | -46.08447 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4ce1601d-846d-38ad-ba61-678fc8509401 | -10.57489 | -46.05061 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0d12c20d-3fcd-3d9c-86fc-0ff6c90f007a | -10.57375 | -46.09088 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2d4fdea5-6356-3118-943f-ae76689045b0 | -10.57361 | -46.05689 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| d8168f03-914b-33b5-b2c7-c4e6659a4517 | -10.57245 | -46.09728 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f91182b1-a713-3707-9175-b442350e5092 | -10.57231 | -46.06329 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 9e59a761-974e-388e-9646-b4c4fd92461a | -10.57112 | -46.10382 | 2024-09-28 03:28:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
