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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 92bafda3-8abe-3cbf-a986-5a9c8ebfba2d | -10.20329 | -68.69215 | 2026-09-30 06:33:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9003f99c-1eab-3e07-8fc7-c75f624879d0 | -8.77353 | -69.53585 | 2026-09-30 06:33:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f024d2de-db22-3bcf-ad31-0b6ef566acc9 | 1.86212 | -55.61907 | 2026-09-30 07:46:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 257f18ed-ade1-3e64-aa85-bf3f3120b052 | 1.85057 | -55.62045 | 2026-09-30 07:46:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 0d7c7c72-f37b-3d90-9fab-9bfd206fb218 | -2.89832 | -54.08142 | 2026-09-30 07:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 3801d6d6-dc31-3994-ba29-38fc6ef6532c | -2.89465 | -54.10665 | 2026-09-30 07:46:00 | AQUA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 2e3b5cbb-2099-3f75-b0d9-3a23ab6b231f | 1.807 | -55.64267 | 2026-09-30 07:46:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| ce0dca08-27e8-3618-ad32-438adefd64ed | 1.86447 | -55.63441 | 2026-09-30 07:46:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b781bbc9-0615-3cf1-bcaf-598316d6e80c | 1.853 | -55.6362 | 2026-09-30 07:46:00 | AQUA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| c1974d30-0619-333f-9c02-4c0ac7f62ad0 | 4.09411 | -59.93768 | 2026-09-30 07:46:00 | AQUA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9e87dfa5-2f0b-39cc-b474-7b32872d27c1 | 4.34578 | -59.71162 | 2026-09-30 07:46:00 | AQUA_M-M | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 25b22eef-7048-3930-8fe2-8c7469536b25 | -2.90251 | -54.08715 | 2026-09-30 07:46:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 75.9 |
| 2f2269b7-6e44-34d0-8bca-f215c3ce6ae9 | -6.06409 | -57.60393 | 2026-09-30 07:48:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 066ea092-2e52-3916-882f-8bcc9c44b684 | -11.7729 | -50.44 | 2026-09-30 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 261c09d4-11e2-3682-b5e4-92df6170bf92 | -11.7919 | -50.4378 | 2026-09-30 07:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 88238822-8b66-300c-9f6b-f7ef629740d3 | -16.02799 | -59.19158 | 2026-09-30 07:52:00 | AQUA_M-M | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7927d62c-6d92-3c78-ac7c-5cc943519f52 | -11.32 | -51.02 | 2026-09-30 08:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8179c829-a4dc-3cae-bdaf-0bc4272190a9 | -11.35 | -51.03 | 2026-09-30 08:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e045dd8f-29c4-30d2-a694-e00204f93ce1 | -12.2327 | -50.2566 | 2026-09-30 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 2e8094d8-ee9f-39d9-be11-b913b5276eef | -10.7101 | -50.4932 | 2026-09-30 08:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 76.7 |
| f04d70be-fe20-3d94-bab7-1f46f6835945 | -12.2324 | -50.2781 | 2026-09-30 08:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| d21ae052-b6a9-3010-ab4f-08ddaa9eb162 | -10.7101 | -50.4932 | 2026-09-30 08:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 3bedb945-0932-3503-af64-a64f1a207b58 | -12.8847 | -44.8015 | 2026-09-30 10:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 103.8 |
| e5dc485e-d4aa-333f-9d65-fc89891aa6da | -17.5063 | -45.4903 | 2026-09-30 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 134.9 |
| e5892983-b990-37b3-92ed-482a46827351 | -17.4869 | -45.471 | 2026-09-30 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 215.5 |
| c74e2e72-7745-3c66-877f-d318cf568363 | -17.5069 | -45.4666 | 2026-09-30 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 567.6 |
| 90e90193-13c5-341b-ad3f-4d43128b72a9 | -17.5269 | -45.4622 | 2026-09-30 10:20:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 159.4 |
| eb8257c3-9cad-3bba-97a3-70e84862472a | -17.5269 | -45.4622 | 2026-09-30 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 145.3 |
| 7629c5ce-87e9-31d3-8341-a21fca99e2ae | -17.5069 | -45.4666 | 2026-09-30 10:30:00 | GOES-19 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 497.2 |
| f7f47b99-2979-3433-a97e-17425cff3188 | -14.1314 | -46.2571 | 2026-09-30 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 129.9 |
| a834a655-2ae9-3f1d-a526-76505dc9ef5e | -14.1119 | -46.2604 | 2026-09-30 10:40:00 | GOES-19 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 98.9 |
| a8a61685-98d2-3660-8852-7c7a97f0ffc1 | -17.5739 | -43.7041 | 2026-09-30 11:20:00 | GOES-19 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 4f2198f9-6a88-335d-b2b6-e26b1ae3ae38 | -8.2482 | -45.4356 | 2026-09-30 11:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 95133755-dcce-3935-b638-d7ca8b7ced2f | -17.9144 | -44.3976 | 2026-09-30 11:40:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 103.5 |
| b1e04485-0eb3-3f9f-8060-bc4f091feec1 | -12.6082 | -47.2429 | 2026-09-30 11:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 84.8 |
| beacf07b-2ecc-3f4c-837e-f91d81b1540c | -14.3153 | -44.9052 | 2026-09-30 11:50:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.2 |
| e81963f3-5208-3084-94a4-8b419715d942 | -8.2482 | -45.4356 | 2026-09-30 11:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 212eebea-af50-35f2-8aae-cdabc6008604 | -8.2479 | -45.4583 | 2026-09-30 11:50:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 90.4 |
| a8583510-6a4d-3524-89ea-521418204ae6 | -17.9144 | -44.3976 | 2026-09-30 11:50:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 139.9 |
| 529501b2-4f45-362f-8c71-eeb5673e76b8 | -12.8847 | -44.8015 | 2026-09-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 3698e226-e3a8-3f1e-aa14-14c15a694291 | -11.2095 | -45.1478 | 2026-09-30 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 88.7 |
| efc7988e-47e3-33d1-911f-9a1a8ee9ce7a | -10.5201 | -45.3554 | 2026-09-30 12:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 8ce6ea63-92b3-3143-810a-567fd33edc54 | -9.8613 | -44.9577 | 2026-09-30 12:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 79.8 |
| 48e467db-50d8-3fb2-b02f-18e8ae56d737 | -12.8842 | -44.8249 | 2026-09-30 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 285a8c7d-db29-3f7c-982a-05185b80fd08 | -10.5197 | -45.3784 | 2026-09-30 12:00:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 224.0 |
| 3ecc2572-c4b6-352c-b72c-4c6b57531be0 | -17.9144 | -44.3976 | 2026-09-30 12:00:00 | GOES-19 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 6581f4af-0a8b-3e62-88c0-e174183cd08c | -1.79237 | -47.94775 | 2026-09-30 12:00:00 | TERRA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 20.1 |
| fad1889f-189b-3bf4-9c0b-78785c416b6c | 1.86347 | -55.56843 | 2026-09-30 12:00:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 73b0ad3c-2d35-3325-9888-986501a4e102 | 1.80187 | -55.64417 | 2026-09-30 12:00:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| 5b48ba7b-c4c1-3514-9bfe-7a29adfa8603 | -0.84589 | -48.71667 | 2026-09-30 12:00:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 76a5fefe-c582-335f-83a5-dc47685a4db7 | 1.70592 | -55.92866 | 2026-09-30 12:00:00 | TERRA_M-T | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 3f25a606-4cb2-39ed-ad64-78062141e3a7 | -1.18329 | -48.82171 | 2026-09-30 12:00:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d2d4b2d0-5f00-3ce9-8116-1058b9ca48f4 | 0.31659 | -51.05469 | 2026-09-30 12:00:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 60b3b2d9-768d-3aa5-8cad-2df0a8d9ec36 | 2.54997 | -50.85271 | 2026-09-30 12:00:00 | TERRA_M-T | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 60fec6e5-6f7b-3ebc-8548-21122a9f261a | 1.86093 | -55.63583 | 2026-09-30 12:00:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| ada9df60-e0c1-3fe2-b604-1eaf2c80d9a9 | -0.67958 | -49.24266 | 2026-09-30 12:00:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 1bc27b0a-cc25-3f5f-a034-8f76cea4f532 | -0.48362 | -49.13025 | 2026-09-30 12:00:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 66.0 |
| 5bec434b-6a74-36cf-8285-5edc796bfe07 | -0.48228 | -49.1396 | 2026-09-30 12:00:00 | TERRA_M-T | CHAVES | PARÁ | Brasil | 1502509 | 15 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 89c4eda0-06a5-31ba-905c-c3ec5ff0a948 | 0.30777 | -51.0559 | 2026-09-30 12:00:00 | TERRA_M-T | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 160c27f4-ca77-32c6-944c-921c82c63aad | -0.66921 | -49.25072 | 2026-09-30 12:00:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 106e5b9a-f8d0-3819-ad18-58620e00b387 | -1.15036 | -48.98516 | 2026-09-30 12:00:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 3ffc9b41-144d-3670-a37c-a1e84b8b2108 | -1.42664 | -48.92319 | 2026-09-30 12:00:00 | TERRA_M-T | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e992401c-805a-301e-9b7d-5e9dec90e545 | 3.38636 | -51.28696 | 2026-09-30 12:00:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 3951cf24-d1d3-3259-aca0-6ca8f17538bf | -0.49271 | -49.1315 | 2026-09-30 12:00:00 | TERRA_M-T | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 1a745370-7d97-36b5-8191-cb0e9519a409 | -0.67827 | -49.25196 | 2026-09-30 12:00:00 | TERRA_M-T | SANTA CRUZ DO ARARI | PARÁ | Brasil | 1506401 | 15 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 31dfeb00-cdee-3ea8-acbb-a6ec48a0925a | -1.79391 | -47.93664 | 2026-09-30 12:00:00 | TERRA_M-T | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 57c80991-fc11-3b14-a8cc-466845c36308 | 3.38504 | -51.27774 | 2026-09-30 12:00:00 | TERRA_M-T | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 66d2571b-a01c-3321-a1af-9a2da994793d | 1.81144 | -55.62598 | 2026-09-30 12:00:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 862f2b21-ddae-3b51-95a8-43723dffed7b | -7.8309 | -45.81622 | 2026-09-30 12:02:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| e3588077-4556-3504-957d-8e22a5c4fd18 | -8.25383 | -45.44982 | 2026-09-30 12:02:00 | TERRA_M-T | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 38.6 |
| 9bbdb134-add8-31e2-83ca-17cf971f8047 | -7.61918 | -44.5449 | 2026-09-30 12:02:00 | TERRA_M-T | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 45.4 |
| 863e5d30-b6bb-39a2-b059-987b01b7cc87 | -2.92248 | -51.30852 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 37f0056b-7df3-304d-a447-c60d836a1558 | -2.58237 | -50.79071 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c220aa20-b740-30fe-a279-d93ff886fb55 | -2.90175 | -54.0917 | 2026-09-30 12:02:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| 12dd1f26-20a7-32ca-9214-e3d4ab9d4e55 | -7.03443 | -45.29915 | 2026-09-30 12:02:00 | TERRA_M-T | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 2802e192-d11d-3835-b76a-1680a393b6a2 | -3.57159 | -50.25515 | 2026-09-30 12:02:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 19875e53-33ce-3b3c-af4d-6ce00c89e7e5 | -3.24039 | -46.94506 | 2026-09-30 12:02:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 90b19f2a-057e-3747-881e-dddb237d91f8 | -9.22481 | -45.84711 | 2026-09-30 12:02:00 | TERRA_M-T | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 4176ba51-fe5a-3e9e-9407-787519c89da7 | -7.00249 | -43.73767 | 2026-09-30 12:02:00 | TERRA_M-T | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 791daf58-2d70-3d44-8374-21f014ce1b19 | -3.10562 | -50.28903 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 4ef2bc75-15a2-31fd-8443-2ac20a83596e | -3.25014 | -50.11233 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| da3314d9-4ab9-35a5-b40b-c3fb2ece888b | -6.33094 | -51.15715 | 2026-09-30 12:02:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 41.4 |
| aa918c4d-8202-31d6-ad1a-35ebe9cef988 | -3.22759 | -54.32007 | 2026-09-30 12:02:00 | TERRA_M-T | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| ad78a813-1bdf-3aab-8a99-f91b1e222d7c | -5.86218 | -51.79668 | 2026-09-30 12:02:00 | TERRA_M-T | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| f7d27e1b-e314-3f2c-9d6a-5300c18edc7f | -7.83129 | -45.81085 | 2026-09-30 12:02:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 31.6 |
| 98719ea9-adf2-318c-a5f1-0fb9c472c2d1 | -3.71168 | -54.22937 | 2026-09-30 12:02:00 | TERRA_M-T | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b011ef34-34f0-3bc7-b996-f651c6c34795 | -4.14667 | -48.90518 | 2026-09-30 12:02:00 | TERRA_M-T | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 2b3c0bd3-9e6e-3130-ab3f-8615cb6f8bbf | -3.38017 | -50.95692 | 2026-09-30 12:02:00 | TERRA_M-T | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 23.8 |
| edd2996f-21d1-3002-83c9-81eacdf5ecc2 | -7.56062 | -42.64987 | 2026-09-30 12:02:00 | TERRA_M-T | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 24.1 |
| d270a4e8-1c98-324a-a24d-3f1b6a368b08 | -3.41619 | -48.33585 | 2026-09-30 12:02:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| a3e0e019-747d-38eb-afed-20a68a465c61 | -6.90112 | -43.69644 | 2026-09-30 12:02:00 | TERRA_M-T | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 2296b4d7-0132-3551-a2c3-f4faaeb11ba3 | -8.99055 | -51.25999 | 2026-09-30 12:02:00 | TERRA_M-T | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 424a331d-059c-34c9-9db9-d080030eb02c | -3.65324 | -47.87921 | 2026-09-30 12:02:00 | TERRA_M-T | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| bc973245-9b54-3a1a-826e-c6d9cd8692c0 | -9.87409 | -44.96967 | 2026-09-30 12:02:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 46.1 |
| 31d476e6-768c-3bee-a835-e8015877f52d | -3.27314 | -50.14326 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| f9320066-4707-3ec8-b8a7-ecbc9a353d86 | -5.98672 | -53.54927 | 2026-09-30 12:02:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 87539231-1103-37e3-9583-c32b38f4439e | -3.11579 | -50.28127 | 2026-09-30 12:02:00 | TERRA_M-T | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| a321e213-c878-3a59-be2e-62f94a34cee3 | -6.32968 | -51.16606 | 2026-09-30 12:02:00 | TERRA_M-T | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7d3a5efa-35c7-3083-8a2a-c63ab4bafe0f | -8.83456 | -49.70507 | 2026-09-30 12:02:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 31.5 |
| c412d182-8181-3f29-813f-ac0df6b78e3a | -2.85153 | -49.53624 | 2026-09-30 12:02:00 | TERRA_M-T | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |


[Clique aqui para ver as próximas entradas](README64.md)
