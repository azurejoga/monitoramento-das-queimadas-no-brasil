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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0b3e22bc-447a-3691-b1dc-854d1862ea2a | -4.3402 | -47.7645 | 2026-07-06 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 97.0 |
| b3e0a995-ec08-3c76-a03d-b99c1e45b505 | -8.6727 | -54.6492 | 2026-07-06 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e903aa24-5f84-37ef-8e82-a1deaf8c2207 | -8.6725 | -54.6695 | 2026-07-06 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 958396f9-ba72-34cb-9669-ea47b5ac6632 | -4.3588 | -47.7636 | 2026-07-06 00:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 908b44b8-d0a3-357f-877a-826fc097007c | -21.0705 | -47.2568 | 2026-07-06 00:00:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 251052da-11c7-314f-a131-02a0526868b9 | -4.3402 | -47.7645 | 2026-07-06 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 92.5 |
| a889f9e4-e9d5-348b-8d7c-62be190f903a | -8.6725 | -54.6695 | 2026-07-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 128.8 |
| 1b14ec3e-3f66-308a-ad9e-b744e6686fb5 | -8.7294 | -54.5645 | 2026-07-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 674d0260-49bd-3812-ab34-d48fe27d5c86 | -8.6538 | -54.6707 | 2026-07-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.7 |
| bc98b496-b1a9-3114-b5cf-59de66359905 | -4.3588 | -47.7636 | 2026-07-06 00:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 4e979972-e7d5-3fa7-b378-ee158ccbfab8 | -8.6727 | -54.6492 | 2026-07-06 00:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 1c72f9b5-8e0b-3cce-9327-1eae3d4a95e9 | -4.3402 | -47.7645 | 2026-07-06 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| eaf9e5cc-e63b-371f-916c-40b2413001fe | -8.7294 | -54.5645 | 2026-07-06 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| f6da71c4-532c-3591-a73e-1a1b733afea4 | -8.6725 | -54.6695 | 2026-07-06 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 184.6 |
| 4769ea8f-e791-3a33-8304-5fbfb26c313f | -8.6538 | -54.6707 | 2026-07-06 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| c097acd1-991f-3f4e-93fd-447f25912087 | -21.0705 | -47.2568 | 2026-07-06 00:20:00 | GOES-19 | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 61.7 |
| fc3ae4fb-567d-3ce3-ac44-76bad22612f0 | -4.3588 | -47.7636 | 2026-07-06 00:20:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 8c3fcef3-5242-3507-b002-0152e7ae5dd2 | -8.6727 | -54.6492 | 2026-07-06 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 137.1 |
| bafc468c-a361-3429-b678-f4f0562971dc | -8.654 | -54.6505 | 2026-07-06 00:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| eb0b1738-739d-3cf6-9300-c858c3851209 | -8.654 | -54.6505 | 2026-07-06 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 09c8e351-600e-38a4-8f84-8687cff5366c | -4.3588 | -47.7636 | 2026-07-06 00:30:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.4 |
| 5aea81c5-05a6-359a-8fba-c58b42ded9ab | -8.6725 | -54.6695 | 2026-07-06 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 132.4 |
| 352ca285-3289-3206-9c17-f682c972567f | -8.7294 | -54.5645 | 2026-07-06 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| de19ecca-b38d-392f-aa17-abae2b1abb4f | -6.0925 | -47.291 | 2026-07-06 00:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 87.7 |
| e65f582c-9765-3801-a45f-cb838e330410 | -8.6538 | -54.6707 | 2026-07-06 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.4 |
| a56215da-ed12-3050-b9bf-3817536c55a3 | -8.6727 | -54.6492 | 2026-07-06 00:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 2b2ea946-ab6e-30a4-8eca-eaa0e17432f3 | -15.0959 | -49.4458 | 2026-07-06 00:30:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 72.6 |
| c06f8a07-5436-3984-ad82-10cb8e0ccd8b | -15.0764 | -49.4488 | 2026-07-06 00:30:00 | GOES-19 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 3dea4fb8-33e9-3227-8af8-e94fa88d06e7 | -8.6725 | -54.6695 | 2026-07-06 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 111.6 |
| bf08785d-e280-3bf1-ac3f-621c8c7906ec | -4.3588 | -47.7636 | 2026-07-06 00:40:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 9eabef94-e8d0-3712-abc4-4fa661fc2b90 | -8.6727 | -54.6492 | 2026-07-06 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.9 |
| a12f7ac9-6229-32d5-b82c-cc1431f8b834 | -8.7294 | -54.5645 | 2026-07-06 00:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 00b58c27-b4e8-350c-ab9a-24e1e9accff9 | -8.6725 | -54.6695 | 2026-07-06 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.9 |
| c5707b9b-ac4d-3b17-8544-dc727724801d | -4.3402 | -47.7645 | 2026-07-06 00:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| 0e20e76b-9a74-30b0-964a-3858be354b51 | -8.6727 | -54.6492 | 2026-07-06 00:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| b6027246-cc1c-3dab-aa02-a64b4bb0e1a4 | -13.25011 | -54.31129 | 2026-07-06 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 577d6406-919f-333d-a4ad-a36410815536 | -13.30356 | -54.38938 | 2026-07-06 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 17856688-8f10-38bd-9792-28c489b8eb52 | -13.30012 | -54.36858 | 2026-07-06 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 30.0 |
| 5bd1fc17-a489-323c-b238-aa4627ec074d | -13.26915 | -54.26342 | 2026-07-06 00:58:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 64ebc9c3-5ce5-3e73-ba4d-48072bf62446 | -8.6538 | -54.6707 | 2026-07-06 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.9 |
| fc026262-fe4f-3b30-ac40-e9b51162be35 | -8.7294 | -54.5645 | 2026-07-06 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 258cfea2-588f-3dbf-a596-6f08941ad010 | -8.6725 | -54.6695 | 2026-07-06 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 116.4 |
| b5aa59cb-9b16-3c1f-9fc6-1a687f90e445 | -8.6727 | -54.6492 | 2026-07-06 01:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 754eeb31-39b2-3721-b74e-fe737342fa37 | -8.73466 | -54.54965 | 2026-07-06 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.7 |
| 5dc44aad-21d0-3c07-b574-3aff41121e47 | -8.73859 | -54.57439 | 2026-07-06 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 505540f3-303e-3f5b-bac1-e0e3ac58b18c | -8.67569 | -54.66545 | 2026-07-06 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.4 |
| 2a9c47ce-5166-36a9-b9b9-56d61bffff3f | -8.66655 | -54.66132 | 2026-07-06 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 291.6 |
| 957fea3d-0e48-3e63-bec7-a030953c5656 | -8.67058 | -54.68566 | 2026-07-06 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| c2bff719-f01c-30cc-8c90-ff84fc662e5f | -8.66174 | -54.6677 | 2026-07-06 01:00:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 171.0 |
| 8fa9dd64-7de9-33df-9df7-5adfb919c866 | -10.39196 | -56.77769 | 2026-07-06 01:00:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.5 |
| f8c15cdb-44af-3122-9991-616b60e40c62 | -10.39178 | -56.76833 | 2026-07-06 01:00:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| f58e74bc-328f-3d35-9d0e-03172a62cf25 | -6.21814 | -57.77301 | 2026-07-06 01:02:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 579d52ca-eac5-3a88-8b18-9934cdc3a20c | -8.6535 | -54.631901 | 2026-07-06 01:05:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 987c8fe4-764e-3bc5-9da1-1732bbfcbf3d | -9.9312 | -59.924 | 2026-07-06 01:05:00 | METOP-B | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9881f1a1-f1bf-380d-8927-7aaca98c09e3 | -13.2581 | -54.241901 | 2026-07-06 01:05:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ae7faeb5-260e-32b0-9619-bdc1246f44a8 | -13.2926 | -54.375702 | 2026-07-06 01:05:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ace5c4f2-161e-3dc7-8a1f-737868d01464 | -8.6583 | -54.650799 | 2026-07-06 01:05:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6dc82ae-902c-32fd-8f43-36ec39ab0cd5 | -13.2678 | -54.2393 | 2026-07-06 01:05:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cb8987a0-5283-3396-9138-4101fc1e0f86 | -10.3912 | -56.7663 | 2026-07-06 01:05:00 | METOP-B | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5c477057-7bb3-34f1-bacf-7e01cb3a57ad | -13.298 | -54.356499 | 2026-07-06 01:05:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1c4bad7-da8a-3331-a571-8b1cd6baf047 | -8.6727 | -54.667198 | 2026-07-06 01:05:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ed52ba7b-aabb-3458-b65d-741a751223d3 | -13.2883 | -54.3591 | 2026-07-06 01:05:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ed523adb-6578-368b-9d66-a859abe790e2 | -8.663 | -54.669601 | 2026-07-06 01:05:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1756605b-c365-3d88-bc2f-327d716dd9b1 | -8.7262 | -54.552502 | 2026-07-06 01:05:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e52cde26-b2db-3cbe-bc04-7332f9821cb2 | -8.668 | -54.6483 | 2026-07-06 01:05:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c210271f-d2e1-3588-be0f-ba91eaa352b7 | -8.6725 | -54.6695 | 2026-07-06 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 126.1 |
| c3c3cf1f-f43d-308e-ad5d-1467d21ed1e5 | -8.6727 | -54.6492 | 2026-07-06 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 166a7c88-6cb3-3105-9dd1-6a4ce66a0c8e | -8.7294 | -54.5645 | 2026-07-06 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| dd5289ae-18ec-3f50-b59c-79b2e3eeb1f1 | -8.6725 | -54.6695 | 2026-07-06 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.3 |
| 33911f33-ab0a-3973-88d1-d98dded012d2 | -10.9205 | -43.0622 | 2026-07-06 01:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 1f5e0756-e99c-3dfc-b1f8-a0f0aac5e36a | -8.6727 | -54.6492 | 2026-07-06 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| 8b0ac3f5-ca6b-3cc4-99cb-80c7760e19b0 | -8.7294 | -54.5645 | 2026-07-06 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 3b4f8e5a-f415-3cc6-8288-3688fc9daea0 | -10.9205 | -43.0622 | 2026-07-06 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 311bcaf5-3e19-3cdf-bb87-0a9552bc0f3c | -8.6725 | -54.6695 | 2026-07-06 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 114.0 |
| cca9bcc8-1135-39ea-861e-3bd0237883a3 | -8.6727 | -54.6492 | 2026-07-06 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 7f7270ca-3e1a-3752-99ff-c7d2110f1570 | -8.6538 | -54.6707 | 2026-07-06 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 863484ca-4946-3e6e-9950-00cc1a27798a | -8.6672 | -54.648399 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96b53cd9-a33d-312d-9a51-6f6303505008 | -8.6746 | -54.677799 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b19c7db-8c9f-3385-9b5f-cbe9699dd73b | -8.6709 | -54.663101 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f65b3f9-9d06-32c0-8af1-6bf08d4195eb | -10.3977 | -56.773998 | 2026-07-06 01:34:00 | METOP-C | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9540309d-b58b-3f01-a833-607eccc6fddd | -13.2527 | -54.316399 | 2026-07-06 01:34:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5fc2c32c-7a10-3f6d-8787-519c1a1fe6a4 | -8.7398 | -54.567299 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09150cd3-6351-3441-9723-89248749c839 | -8.6806 | -54.660702 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c5657fbd-c25c-3d89-97e7-e64523993bbe | -8.6612 | -54.665501 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 07cdcf87-05f0-3b3e-9b29-6b1158cdb657 | -8.7361 | -54.552399 | 2026-07-06 01:34:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35438aca-8cb8-3817-a7ec-13d9615d4813 | -8.7294 | -54.5645 | 2026-07-06 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 1b22a339-f488-386a-90c0-8bde59aeaf6a | -8.6727 | -54.6492 | 2026-07-06 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 76.8 |
| 0c8f8b4b-c324-328d-8b07-047ebe1311eb | -8.654 | -54.6505 | 2026-07-06 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| bb1b1741-342a-37c2-8086-1a6a073d3917 | -8.6538 | -54.6707 | 2026-07-06 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 77.3 |
| 0108d7e5-f240-3a90-a2da-b6a59c74d3f7 | -8.6725 | -54.6695 | 2026-07-06 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| 8d89a7d2-b477-38af-9474-c5ad71e31b22 | -8.6725 | -54.6695 | 2026-07-06 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| b0a4518d-fa7e-3d4e-9829-ec2ae4be2b73 | -8.7294 | -54.5645 | 2026-07-06 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 81d6a1fd-2712-3c05-9c7e-f772bddfff8d | -8.6727 | -54.6492 | 2026-07-06 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 7bb5cea3-dcc6-304c-a672-6a02c8937894 | -10.9205 | -43.0622 | 2026-07-06 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8a297403-8a3f-3926-8c90-adad84489959 | -8.6727 | -54.6492 | 2026-07-06 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 3e4cbca4-a33b-3c29-bef1-7c507fd90931 | -8.6725 | -54.6695 | 2026-07-06 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| b7844e01-1183-3cbb-adf4-653a05befcf6 | -8.6727 | -54.6492 | 2026-07-06 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 88c6218a-e847-3924-93ea-040836875672 | -10.9205 | -43.0622 | 2026-07-06 02:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 4e22354e-8d6c-3697-9fb6-1e2ff86b204e | -8.6725 | -54.6695 | 2026-07-06 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.4 |
| d785ba12-cfd5-3e46-b676-beb37bd0bb90 | -8.6538 | -54.6707 | 2026-07-06 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 49.1 |


[Clique aqui para ver as próximas entradas](README2.md)
