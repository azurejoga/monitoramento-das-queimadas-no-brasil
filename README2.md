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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ea27d28-bbc7-3a08-bb93-e32b9c22105d | -10.93221 | -57.12206 | 2025-06-23 01:02:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 23.8 |
| a398691b-4cc5-37c0-956f-58c205dc9766 | -10.89079 | -56.4733 | 2025-06-23 01:02:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 9b2574bb-120f-3e46-83d9-d7badbc34800 | -10.89921 | -56.46069 | 2025-06-23 01:02:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| cb2f6efa-acec-374d-8e76-0d94f82aa98d | -9.41342 | -48.41689 | 2025-06-23 01:02:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 18.7 |
| b5c0baf4-5a49-3721-9724-2fe82c605408 | -10.88933 | -56.46199 | 2025-06-23 01:02:00 | TERRA_M-M | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 12.8 |
| a1ba6d64-32f2-398d-817d-1afc2f1aeb9f | -9.15388 | -48.98172 | 2025-06-23 01:02:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 681b151b-a785-3220-b247-b15b7e2c511c | -10.50409 | -53.5874 | 2025-06-23 01:02:00 | TERRA_M-M | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 32104db0-60bd-3714-9b70-8c3c9f1fa6d6 | -9.42361 | -48.42615 | 2025-06-23 01:02:00 | TERRA_M-M | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 77c2e5b7-a093-3ce8-844f-1e268efe4ee0 | -10.92554 | -57.12935 | 2025-06-23 01:02:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| af6af691-d77d-3dcc-b404-7428676e44f7 | -10.93379 | -57.13474 | 2025-06-23 01:02:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| bfe0812b-32d8-3461-8cfc-9678fb6f89d0 | -9.15162 | -48.96714 | 2025-06-23 01:02:00 | TERRA_M-M | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 799ff831-3c58-3e09-9893-db03aaddefef | 2.75002 | -60.3706 | 2025-06-23 01:05:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 258c2ff6-042b-398d-80df-9821dad104b4 | -8.07 | -43.1216 | 2025-06-23 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| 17b023d5-e285-380f-99f1-53abd6f83420 | -17.3837 | -42.6483 | 2025-06-23 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 55.7 |
| dc9ed5ef-64ba-3d69-9fd4-fd1e8b5a340c | -8.0703 | -43.0981 | 2025-06-23 01:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.4 |
| bbfd8b35-2b85-3e13-9a83-8952543a7484 | -11.6172 | -58.2693 | 2025-06-23 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| e587051c-de26-3dda-966d-fc68611bfbab | -17.4045 | -42.6186 | 2025-06-23 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 150.9 |
| e3dc8cb7-40d6-342f-889e-d2ac5d2c3243 | -11.617 | -58.289 | 2025-06-23 01:10:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 121.5 |
| 987bebfd-cfef-3646-993b-5a67ee467c95 | -17.3844 | -42.6235 | 2025-06-23 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 120.9 |
| db4aaab6-8f76-30f5-8bb3-209f16a115a4 | -17.4038 | -42.6435 | 2025-06-23 01:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 68.6 |
| 0206ca09-0c86-3ff3-b567-0bdc250e2021 | -11.6172 | -58.2693 | 2025-06-23 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| ce64320b-2112-3def-bace-50f857b98ce7 | -11.617 | -58.289 | 2025-06-23 01:20:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 129.0 |
| 044d7596-4769-3835-95c5-6d6fc46a3b9c | -8.0703 | -43.0981 | 2025-06-23 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 75.2 |
| fee30f6f-0fa8-38ac-974e-4b53ea60063a | -17.3844 | -42.6235 | 2025-06-23 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 82cd91e6-c8f1-3da5-8108-1e7e24d5b73f | -17.4045 | -42.6186 | 2025-06-23 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 200.4 |
| 781ed294-7255-328c-83c1-fbdbe1ef32f2 | -8.07 | -43.1216 | 2025-06-23 01:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 72.3 |
| bc6a72f2-ddea-35f5-a91b-51ff73366819 | -17.4038 | -42.6435 | 2025-06-23 01:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 76.3 |
| 30848118-5821-3798-910f-7650a9317a6c | -17.4045 | -42.6186 | 2025-06-23 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 137.3 |
| 3daec3dc-afe9-3021-96d4-e0a2e9b7de92 | -8.0703 | -43.0981 | 2025-06-23 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 85.9 |
| 972ddc9d-04ce-3fda-84df-d879fc11f6cd | -17.3844 | -42.6235 | 2025-06-23 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 139.7 |
| 9989f5a1-66f2-3d5a-823d-7ea7a639c583 | -17.4038 | -42.6435 | 2025-06-23 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.1 |
| 86ca464d-886a-3d40-b758-06c744222f1e | -17.3837 | -42.6483 | 2025-06-23 01:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 62.5 |
| d3372e10-afde-36c3-ab51-66a2f22b863d | -8.07 | -43.1216 | 2025-06-23 01:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 78.0 |
| 36aa5dd3-5485-3709-829d-e94dc44109f2 | -17.4045 | -42.6186 | 2025-06-23 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 186.2 |
| bd371695-a0c2-3d00-8cbc-cf0d69461972 | -17.3844 | -42.6235 | 2025-06-23 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 713d6026-9396-324a-bb6d-5b6e7809b4dc | -11.617 | -58.289 | 2025-06-23 01:40:00 | GOES-19 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 7cb0c5d4-44da-3894-a8ef-13cb8aebff26 | -8.07 | -43.1216 | 2025-06-23 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| 28e5079c-4ded-3bc4-a27c-d40bf96710c8 | -8.0703 | -43.0981 | 2025-06-23 01:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.9 |
| cbf9c85d-3cf4-3d3e-8cd1-88ed7e787d27 | -17.4038 | -42.6435 | 2025-06-23 01:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 79.5 |
| f4221bee-7d9f-3cf3-add4-3af6bbc7b13a | -8.0703 | -43.0981 | 2025-06-23 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.6 |
| aa0394d7-2f21-34e4-a31f-3ddd4e1e983b | -17.3844 | -42.6235 | 2025-06-23 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 48574456-bf48-3a5e-a874-d19dafd70abe | -17.4045 | -42.6186 | 2025-06-23 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 190.5 |
| 2cf53919-7b02-37ac-91e8-7d2419a6564b | -17.4038 | -42.6435 | 2025-06-23 01:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 7a4c80ef-617f-3f25-99ac-da593ecbd8b8 | -8.07 | -43.1216 | 2025-06-23 01:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 8ce012f2-8be1-3600-aa7d-f4db8be38239 | -17.4038 | -42.6435 | 2025-06-23 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 86.2 |
| b486312a-4f68-3136-a9b3-19f08213e779 | -17.3844 | -42.6235 | 2025-06-23 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 667f7d69-cc8f-34eb-aa1e-e7e4c7aba410 | -17.4045 | -42.6186 | 2025-06-23 02:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 158.4 |
| 757b4333-8926-36fc-b136-16c7cb72dcf7 | -17.3844 | -42.6235 | 2025-06-23 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 59e202b7-a72c-303c-a409-eb1721803cff | -17.4038 | -42.6435 | 2025-06-23 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 79.3 |
| f4f6e20f-ad5c-3499-a0d9-da6ffa57770b | -8.0703 | -43.0981 | 2025-06-23 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 59.9 |
| e67162e8-e3fa-3166-9fff-e5d68d85108d | -17.4045 | -42.6186 | 2025-06-23 02:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 139.8 |
| 0e74c19e-53b1-3ba4-96ef-c76aca4f1ae5 | -8.07 | -43.1216 | 2025-06-23 02:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 5eaf8032-f8b9-3381-8159-3e1edbf25331 | -17.3844 | -42.6235 | 2025-06-23 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fd249d8f-a32e-355d-85f2-2521f83d0a3a | -17.4045 | -42.6186 | 2025-06-23 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 123.8 |
| 18c95755-3c74-306b-84f1-a519f42be281 | -8.0703 | -43.0981 | 2025-06-23 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.8 |
| 34d808bf-53ef-3a1e-98fd-554e4f1e95e1 | -17.4038 | -42.6435 | 2025-06-23 02:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 50.0 |
| 191818b3-f85e-3bae-b20e-f7b741adfb1c | -8.07 | -43.1216 | 2025-06-23 02:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.8 |
| 5743f3d9-2b0a-3e00-aa93-48a99956c5e4 | -17.4045 | -42.6186 | 2025-06-23 02:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 7d247a0f-a70c-30ef-a0a7-a2ce704aba15 | -8.07 | -43.1216 | 2025-06-23 02:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 74.5 |
| e2d01dec-6fd4-3355-8330-a9b04fc0cf5a | -17.4038 | -42.6435 | 2025-06-23 02:30:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 1d805882-e1e5-3982-b3aa-96c39dda7f63 | -17.4038 | -42.6435 | 2025-06-23 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 54.7 |
| 06209422-fa19-3977-b794-e2e9482901df | -17.4045 | -42.6186 | 2025-06-23 02:40:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 104.5 |
| aea86c66-39f1-3d60-84da-0c13b695b04b | -8.07 | -43.1216 | 2025-06-23 02:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| bf4ec4f1-8cdb-3513-9c3f-636944cc2c62 | -17.4045 | -42.6186 | 2025-06-23 02:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 85.5 |
| c01e9b28-9275-3559-9b2e-45d15924c5f3 | -8.07 | -43.1216 | 2025-06-23 02:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 0df869db-82ab-3af8-910a-f69d1da7c37b | -17.3844 | -42.6235 | 2025-06-23 02:50:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 54.8 |
| 20984385-f329-3884-87f2-111b72598761 | -17.4045 | -42.6186 | 2025-06-23 03:00:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 7b6f529d-5e0c-355f-b502-7770d182138a | -8.07 | -43.1216 | 2025-06-23 03:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |
| 06848386-3dbf-3752-9cf9-3509548f38c8 | -17.38906 | -42.64005 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 32.7 |
| f4f608ec-d7ff-37f8-a708-5d1682586a80 | -17.38647 | -42.63029 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 3536b14f-488e-3f33-ad96-500d2e327cbe | -17.39075 | -42.63298 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 5edb76de-d760-3f46-8921-d0cda6bd513c | -17.39178 | -42.63917 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| df978ad0-b540-3f33-805f-fdce310aec41 | -17.39245 | -42.62585 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 28ff579f-c735-32b3-a4f4-e9753e06372b | -17.3951 | -42.62489 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 07668f44-214f-3497-9756-0779aa95e1b6 | -17.39344 | -42.63202 | 2025-06-23 03:06:00 | NOAA-20 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 25.8 |
| be365e36-0c36-3750-bd32-76a867416738 | -19.83117 | -40.11142 | 2025-06-23 03:08:00 | NOAA-20 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b2db6f3c-b8a7-3268-b9ea-9f25e301f688 | -8.07 | -43.1216 | 2025-06-23 03:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 93605209-d053-3963-a1d1-edc69e05180e | -17.4045 | -42.6186 | 2025-06-23 03:10:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 74.4 |
| dccc51c5-734a-3a4e-a3f4-8b5152164ee6 | -8.07 | -43.1216 | 2025-06-23 03:20:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 67fb32fb-81a8-38ff-97bf-b112c27b4c99 | -17.4045 | -42.6186 | 2025-06-23 03:20:00 | GOES-19 | TURMALINA | MINAS GERAIS | Brasil | 3169703 | 31 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 43624797-0c2c-30f0-a7dd-5c460fa1fa25 | -8.07 | -43.1216 | 2025-06-23 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.0 |
| 46002dbc-bdd1-3893-9787-7de54ee13c76 | -5.57347 | -45.20975 | 2025-06-23 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 59828889-9346-37fd-aa55-04c39372c604 | -5.41927 | -45.11576 | 2025-06-23 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6503ded4-df18-3653-abc5-2ec6298e5dfb | -5.11065 | -43.14703 | 2025-06-23 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| db5862fa-28ce-3761-b309-c28ee18e18ae | -4.66892 | -41.95819 | 2025-06-23 03:53:00 | NOAA-21 | COCAL DE TELHA | PIAUÍ | Brasil | 2202711 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2e7c666f-77f2-32a4-ad43-894555924004 | -5.42007 | -45.11095 | 2025-06-23 03:53:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7fda4655-e891-3590-a2bb-5f34908a32ba | -5.49307 | -43.98153 | 2025-06-23 03:53:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 65ebb18a-36d3-3a71-836f-1fcb699bacf2 | -5.1091 | -43.14322 | 2025-06-23 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 89b709b9-2d9a-308b-84a2-969a51c575e9 | -5.49791 | -43.97833 | 2025-06-23 03:53:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9a89ea0c-73f7-3810-8078-ad858f18e430 | -5.07171 | -37.71587 | 2025-06-23 03:53:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9005380e-79e9-38a8-be35-28ed4d4bae62 | -5.10721 | -43.14287 | 2025-06-23 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ef453998-5db4-3045-94e4-1adc1bfbb719 | -5.10852 | -43.14671 | 2025-06-23 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2479f114-9555-382f-9367-e21cd913fc7d | -5.7007 | -44.24594 | 2025-06-23 03:53:00 | NOAA-21 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 259e455c-0493-3d30-bd05-fe884bcf20b9 | -5.49727 | -43.98224 | 2025-06-23 03:53:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 62b347cd-73cb-32da-838e-4f5272faa1d9 | -5.10664 | -43.14638 | 2025-06-23 03:53:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fd955a72-e095-3d61-a29d-a6b3ff2142f5 | -14.17637 | -40.21717 | 2025-06-23 03:55:00 | NOAA-21 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| bfa9f241-4be1-39a6-a03c-e6354e0f02e0 | -7.35257 | -45.33528 | 2025-06-23 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c66e9950-ca5c-3860-a253-dfdfd7d78cfb | -11.57976 | -44.66115 | 2025-06-23 03:55:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3f666784-25a4-3d92-8739-bd8195a00024 | -8.06994 | -43.10812 | 2025-06-23 03:55:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 0e23d40a-d1d7-3cd5-b703-df825e9994d9 | -10.06958 | -49.66337 | 2025-06-23 03:55:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
