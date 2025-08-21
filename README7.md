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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b327982d-bc2d-380a-bdae-68e7fd67c16c | -8.8736 | -62.4115 | 2025-08-21 01:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 4a9403cc-1d58-3a8b-a56d-b09b9fb473a2 | -15.8849 | -49.0076 | 2025-08-21 01:10:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 53.0 |
| e1c12003-7cb4-397a-b8c5-2b6edba061d1 | -8.6344 | -62.1177 | 2025-08-21 01:10:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 8da3798a-855b-3216-8829-60c43fe4bdf8 | -9.6254 | -40.5875 | 2025-08-21 01:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 148.5 |
| 055e75ea-fc73-3698-9693-f83934d09e3e | -12.9537 | -46.219 | 2025-08-21 01:10:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 7868cee6-9a02-355f-bd48-71e7aececf1d | -8.6343 | -62.1367 | 2025-08-21 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| 755624ea-c057-3d16-9848-da8976734bf9 | -8.8737 | -62.3925 | 2025-08-21 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.1 |
| a97906d9-8f52-31b7-8c32-ce695b57466b | -12.9533 | -46.2419 | 2025-08-21 01:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 73.4 |
| 5c48b5ac-ae25-371f-8321-24ed7df56059 | -8.6158 | -62.1184 | 2025-08-21 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 29f9343f-42dc-344b-bcde-dec33038cb1c | -8.6344 | -62.1177 | 2025-08-21 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 52.1 |
| 4dc7479f-5d2d-334e-b688-c47d4cd7cd18 | -8.8922 | -62.4107 | 2025-08-21 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| de9f68f9-b57b-3de4-8a25-d124bf67f85e | -12.9537 | -46.219 | 2025-08-21 01:20:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d98cd322-ef40-3ac7-b29f-faeaba0d4f45 | -15.8849 | -49.0076 | 2025-08-21 01:20:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4c761581-3383-34d9-8fda-2c2e8f0e550d | -7.0354 | -44.6167 | 2025-08-21 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 132.1 |
| bece9af4-7352-3809-99db-50f95baf15c3 | -9.6446 | -40.5847 | 2025-08-21 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.6 |
| bd64e561-60c0-3d59-a9e1-2a73b932a6a9 | -23.1209 | -49.3052 | 2025-08-21 01:20:00 | GOES-19 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.5 |
| 8ad4cc6b-07de-3eee-b515-3955a2fca35b | -9.6254 | -40.5875 | 2025-08-21 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 162.5 |
| d39f0da4-4d9d-3fc5-b680-da538290d384 | -8.8736 | -62.4115 | 2025-08-21 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 90.6 |
| 7e95df81-2e99-323c-abac-dc592e928fa1 | -9.625 | -40.6122 | 2025-08-21 01:20:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 62.3 |
| 00de6198-f371-39f4-a43a-69563a587fc2 | -7.0166 | -44.6184 | 2025-08-21 01:20:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 230.8 |
| 6ae01038-31ef-35b7-bffe-334b555f97ed | -18.3038 | -45.5257 | 2025-08-21 01:20:00 | GOES-19 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 40.4 |
| 9199a9dc-3891-3c3d-9c39-554b3755486a | -13.1367 | -54.9171 | 2025-08-21 01:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 63.8 |
| 328c62fd-adff-3a0e-bf08-dd2ae5cba85c | -23.1216 | -49.2817 | 2025-08-21 01:20:00 | GOES-19 | MANDURI | SÃO PAULO | Brasil | 3528601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 71.8 |
| 21b00643-5bab-34ee-8409-a35ba322b183 | -8.6157 | -62.1374 | 2025-08-21 01:20:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 5186354a-e3e8-3b13-98b9-4f74eec9e125 | -8.8551 | -62.4123 | 2025-08-21 01:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 43.5 |
| 0f74b681-2bf8-38ae-8507-dc3f338c5e2b | -8.8735 | -62.4305 | 2025-08-21 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 44.0 |
| fa36ba8e-5561-34d7-a720-8d849f46652e | -12.9537 | -46.219 | 2025-08-21 01:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 61728b00-82ed-33e2-8a96-3274d9d5aff5 | -7.0354 | -44.6167 | 2025-08-21 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 162.3 |
| ae53e1fb-d1e8-3f10-95b2-5960f4fc6b05 | -9.6446 | -40.5847 | 2025-08-21 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| e10d6935-0f09-34b3-9343-1086fbabb7b3 | -13.1367 | -54.9171 | 2025-08-21 01:30:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 79f007a1-a9ee-32a0-a607-32dccf21ad21 | -8.8922 | -62.4107 | 2025-08-21 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 2d57d1b6-2245-3578-b94c-9b5e773ace5d | -14.8538 | -47.9504 | 2025-08-21 01:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 7e48db4b-4a40-36bd-9490-713fd832f684 | -15.8849 | -49.0076 | 2025-08-21 01:30:00 | GOES-19 | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 444e45d3-967e-308f-a65a-17e55810ae5e | -8.8737 | -62.3925 | 2025-08-21 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.7 |
| 1387911a-7cb7-37fd-82ea-5734b9830a6b | -9.6254 | -40.5875 | 2025-08-21 01:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 74.7 |
| 3aa36f5e-636f-342e-8689-c0e9f4252f16 | -12.9533 | -46.2419 | 2025-08-21 01:30:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| 31b2ed74-924b-35a3-8476-0ce000bd1be2 | -15.0193 | -54.832 | 2025-08-21 01:30:00 | GOES-19 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 46.3 |
| a5b1d1aa-5e70-3183-882a-19270cc0a247 | -8.8736 | -62.4115 | 2025-08-21 01:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 105.8 |
| 988da9d6-ba34-3652-bacf-0fb7e6237208 | -7.0166 | -44.6184 | 2025-08-21 01:30:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 232.6 |
| 895d8cea-6c33-3780-99fd-f3111ebdf309 | -14.8543 | -47.9279 | 2025-08-21 01:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 99e2c5b4-3d8d-34b7-8e8f-192c2d711927 | -8.8667 | -62.4025 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 98a036b6-f280-3313-953b-00f82c2951e3 | -8.878 | -62.4072 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| ae9a3407-9fbf-3609-af78-836ecda219a1 | -13.1457 | -54.916901 | 2025-08-21 01:36:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 107a384a-0eef-3a19-93cb-461d75867e85 | -13.1584 | -54.926498 | 2025-08-21 01:36:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a83f1d3c-f628-376c-843c-1afb469275bc | -8.8796 | -62.4142 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 2e69fc50-e8f1-3255-a814-d73359da0605 | -8.8878 | -62.404999 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 0ca71a94-a808-3dfd-8598-5dcf42862846 | -8.8863 | -62.398102 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 1efc3836-8cca-394b-843c-4c4966cf61d3 | -7.0576 | -59.837299 | 2025-08-21 01:36:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb899ad7-7702-3bdf-be4f-4b16c258602e | -7.054 | -59.821899 | 2025-08-21 01:36:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 16a5f40f-a605-3eea-887f-7a5b42cee115 | -14.8655 | -47.947899 | 2025-08-21 01:36:00 | METOP-C | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 629e68ec-b06a-3cef-b030-9e87d748182c | -8.6213 | -62.138802 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 07570eab-fc31-3976-8811-45743ab69fe4 | -23.688499 | -51.830601 | 2025-08-21 01:36:00 | METOP-C | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c7ef395-09a9-3ff9-9c03-3a599bfa8cd4 | -8.3829 | -55.008598 | 2025-08-21 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9928708-432d-3df2-90fd-6981d07b2004 | -7.7794 | -66.959297 | 2025-08-21 01:36:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 74db1131-ae11-3542-9b04-d2e73cc15f29 | -23.685101 | -51.8176 | 2025-08-21 01:36:00 | METOP-C | BOM SUCESSO | PARANÁ | Brasil | 4103206 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c13c1608-ea8b-30d1-ad3c-068e79029796 | -13.1554 | -54.914398 | 2025-08-21 01:36:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 14df71b4-b2bd-3f53-9cad-3c9a14a31c09 | -13.3364 | -54.401199 | 2025-08-21 01:36:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a0045642-4876-3d90-b63e-b77a998958c8 | -8.6311 | -62.1366 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f7e7683d-9554-3e6b-9b90-32cc645f66d8 | -8.6393 | -62.127399 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 65a0391c-b84c-325a-9e3b-25447c19a1ec | -8.8682 | -62.409401 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a01c72d1-98ac-377d-b943-ecabecf5911d | -13.3397 | -54.414101 | 2025-08-21 01:36:00 | METOP-C | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cc9dbfef-377c-35b4-a684-4dc6ec05f63f | -6.9357 | -62.887199 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 24c7cd86-2deb-3813-9aa3-380548d9c689 | -7.7771 | -66.948997 | 2025-08-21 01:36:00 | METOP-C | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| af5099a2-1f2f-36e7-9c2e-70b30b8477dd | -13.1487 | -54.929001 | 2025-08-21 01:36:00 | METOP-C | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 21851c6f-ced5-3308-86c6-e87f17f1dbeb | -7.5096 | -63.831001 | 2025-08-21 01:36:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 00b370e4-7e0f-32bb-ad10-05eb5d84109f | -12.5902 | -60.3657 | 2025-08-21 01:36:00 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b7903b0c-63c9-3fdf-b5e3-6bb3fe834e7d | -14.6254 | -54.869301 | 2025-08-21 01:36:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9dba699e-e53f-32b5-ba50-04ebfbdfc359 | -7.5553 | -63.851299 | 2025-08-21 01:36:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a1e0ae59-4326-3264-9f75-49b5288ee2ff | -6.9455 | -62.884998 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| f9c8550e-609c-346e-9bab-6bfab89d844e | -10.9937 | -55.2486 | 2025-08-21 01:36:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| df6d42a8-fa52-3563-8033-256493f1b4a1 | -8.8812 | -62.421101 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| a0d82afd-4fa5-3081-a8eb-c5b71773ab81 | -7.5537 | -63.844101 | 2025-08-21 01:36:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3d694c9f-d82f-3e76-8403-cef3485304d8 | -14.638 | -54.878201 | 2025-08-21 01:36:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7692728e-6ad6-3202-8dea-16d3b5e572d3 | -8.8765 | -62.400299 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 17225b47-367a-306f-ae33-83750fc3211f | -14.6351 | -54.866699 | 2025-08-21 01:36:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eb2cba96-a206-324b-9dfb-7d8927e1953c | -8.8698 | -62.416401 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| f84e8301-aeda-35e7-a650-1fe9747d9b6a | -8.8894 | -62.4119 | 2025-08-21 01:36:00 | METOP-C | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 11084724-f68e-3f33-913a-107152e7b5bf | -8.6295 | -62.1297 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3814b0a3-e92b-34f4-8c00-9056cfee50a1 | -7.0558 | -59.829601 | 2025-08-21 01:36:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 35a2827d-bf8f-3675-a626-2546435cc401 | -14.7569 | -56.023998 | 2025-08-21 01:36:00 | METOP-C | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 60732664-9882-3e02-82b1-285d644e7be8 | -8.6244 | -62.152599 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 629cf9c3-8c3d-3d57-bf73-3e96fef205ad | -7.5651 | -63.849098 | 2025-08-21 01:36:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 62292c3a-7e1c-379a-9a02-ae2ce478bdbb | -8.6197 | -62.131901 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| c5054920-2d6e-3f12-86b6-df423821c1c6 | -7.0656 | -59.827301 | 2025-08-21 01:36:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 87a136d1-6a99-35ba-af86-ef396d41945e | -14.6283 | -54.880798 | 2025-08-21 01:36:00 | METOP-C | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5f1ff1ca-a259-3241-901e-3e15eb69c1dc | -8.628 | -62.122799 | 2025-08-21 01:36:00 | METOP-C | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5453606b-ec78-3143-acd8-b2005388d5fc | -8.3794 | -54.994499 | 2025-08-21 01:36:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d4e49f-bbb6-38d8-bc12-363481d62cc1 | -12.5886 | -60.3587 | 2025-08-21 01:36:00 | METOP-C | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| caeb4629-99f2-34e7-827c-761572f0c6eb | -10.9906 | -55.236301 | 2025-08-21 01:36:00 | METOP-C | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| e2b793e3-d6f4-3cd6-a511-9759e0283e2b | -9.6446 | -40.5847 | 2025-08-21 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 147.2 |
| 4282056e-0ffe-344a-8ff0-4b5bf76d050b | -12.9533 | -46.2419 | 2025-08-21 01:40:00 | GOES-19 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 5da714c8-d0aa-3fac-8e5f-fbaa07f0793f | -9.625 | -40.6122 | 2025-08-21 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.1 |
| f496f46e-fd91-322d-9745-d0ef14736d37 | -9.6258 | -40.5627 | 2025-08-21 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 15b94cc0-caa7-30d2-a413-1e460ad8c835 | -8.6157 | -62.1374 | 2025-08-21 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| 43f50c57-24c5-3b5c-9edc-09d240fe234a | -7.0352 | -44.6396 | 2025-08-21 01:40:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d0247407-cadf-38c1-9f6a-0e0721b1ca6a | -8.8737 | -62.3925 | 2025-08-21 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 8ba13c21-9712-3cf8-9e27-e04f993175f0 | -10.9905 | -55.2403 | 2025-08-21 01:40:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 82e1770e-64b9-3b3a-8e9f-9b77a702947b | -8.6343 | -62.1367 | 2025-08-21 01:40:00 | GOES-19 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 1a517d8c-4125-3968-874a-303f5dde16bd | -14.8543 | -47.9279 | 2025-08-21 01:40:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 41.2 |
| ed942276-b7a4-3b98-9515-67d50c9443da | -8.8736 | -62.4115 | 2025-08-21 01:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 102.1 |


[Clique aqui para ver as próximas entradas](README8.md)
