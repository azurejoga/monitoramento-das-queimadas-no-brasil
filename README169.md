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

## Dados Diários - Página 169

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f429819b-26d8-388c-a12c-d406449306c8 | 1.89989 | -55.57575 | 2026-09-28 17:13:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7d038d96-f4ca-3766-96d7-534dfc2c4ac2 | 1.86259 | -55.59262 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 2576d814-d097-3221-be48-ebbb23095391 | 2.4506 | -51.00718 | 2026-09-28 17:13:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 8d6f5aec-428f-380e-9a6b-4166cd3821a1 | 4.11018 | -60.91879 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 18.0 |
| cd2dd6f5-97a6-3466-9872-ba4ba9eee0ce | 4.05278 | -59.93423 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 52a74c0e-4756-3cc3-846c-fb2b0aeeec36 | 1.8648 | -55.57801 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 4ed49bb9-6dbf-3db8-b928-3e4599dd4ac0 | 4.47828 | -60.51377 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c1f53a1f-3f0c-35f3-8cea-4f92241dc0c0 | 3.93926 | -64.33386 | 2026-09-28 17:13:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 42b26e9e-f4f1-3ff5-a86b-f5152d975c49 | 4.3902 | -60.5413 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 67c1455a-b50c-3d17-8cbd-3d5aa606d3ba | 1.87783 | -55.58375 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 951df022-28ef-3aa5-a3df-35dfdea872b3 | 3.68521 | -51.72589 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.2 |
| b9c88efc-d4d4-3517-888f-3553842db69f | 4.40607 | -59.80551 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e0600c77-5c1e-3852-9072-a4ba70f9d2d2 | 1.71881 | -50.96111 | 2026-09-28 17:13:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 17.3 |
| b70ccb67-b0cc-3228-899d-54e5346ada1a | 4.0087 | -51.64331 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 41.7 |
| ca1198c5-b866-3c7f-96d7-54fb42d01a2c | 3.48198 | -51.49003 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4be3c2c3-0f89-3a1e-bd1b-94f1e51404a7 | 3.69408 | -60.18991 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 558437f4-1328-3821-8994-083ea6695dd5 | 3.81113 | -60.67493 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6f2248f5-e58e-3177-8e3c-8d63878032f6 | 3.86427 | -59.97416 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e0ace2c6-60df-3963-afdc-eae55dc7c799 | 1.84562 | -55.59001 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| c3ccec74-666a-35ec-907f-d6c2fb911dfa | 2.04225 | -50.90792 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 2838f6c0-cad2-3bc9-b571-de3ca4b2de56 | 1.87894 | -55.57641 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 62f2bde8-79de-3aaf-b2e6-0e09d56a6590 | 4.09841 | -60.90021 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 11.2 |
| d089258e-6e6a-3fd4-83c8-2552909e336c | 1.72256 | -50.96609 | 2026-09-28 17:13:00 | NOAA-21 | PRACUÚBA | AMAPÁ | Brasil | 1600550 | 16 | 33 | nan | nan | nan | Amazônia | 10.6 |
| e377c008-e52a-388a-bab4-b8b1f427a43f | 2.07536 | -50.74926 | 2026-09-28 17:13:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 77ce5da3-0b38-36ae-9dc9-694b276b1a1f | 1.67326 | -55.92122 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 9110063b-46a1-3bbc-99e7-dc6005bc72de | 1.89483 | -55.58621 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| caf6ed7f-e1ae-36fd-9af4-6d9f6f5a69a1 | 1.66761 | -55.91307 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 460a74c6-7640-3495-a65d-70587a8a3720 | 2.44995 | -51.01157 | 2026-09-28 17:13:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 5.8 |
| a7e386d1-d565-367e-9c41-7966f54356af | 4.4106 | -59.82138 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 940a751b-d410-37cd-80f1-78642582fdc0 | 3.70045 | -60.19481 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 8b258246-8169-327a-8345-940aba10ff6e | 2.45367 | -59.9433 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d89e4793-254b-3da3-9b84-f981a013d6d0 | 2.46881 | -59.93772 | 2026-09-28 17:13:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 1547bb76-74b3-36c1-96de-13f50fee0ead | 3.93994 | -64.32956 | 2026-09-28 17:13:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 344ec048-09c2-3831-bb95-578b21eb401e | 3.55432 | -60.11399 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 690b2c7c-91e9-3218-b5b0-773382558a95 | 1.83223 | -55.97489 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| f4164d82-f06c-3769-b890-c2416c30071c | 2.38447 | -50.99945 | 2026-09-28 17:13:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 5c800ee3-1b26-3a10-b444-0bf2d8fed6a3 | 1.84956 | -55.58687 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 6dc3abf0-5373-3076-a642-18dce8f105cd | 1.8795 | -55.57273 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 34c9e0ba-d69e-3033-95fd-675c5e12b929 | 4.03066 | -60.07726 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5dd4d9fb-b3bf-32c6-aa1f-f1208f6ee53d | 4.26511 | -59.83239 | 2026-09-28 17:13:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7a0f5b27-bbc4-3e14-8a0c-cecbb2a278ae | 3.85735 | -60.01939 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3c173db3-d366-30c3-b128-1e0406318915 | 3.67606 | -59.91841 | 2026-09-28 17:13:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 61f7ddce-cc1c-394b-affd-7846de6968d6 | 1.95231 | -55.69575 | 2026-09-28 17:13:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| dec349ca-af7a-3ba0-84e7-c6f3424ddf02 | 4.17808 | -60.69283 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 42b0b5bc-5895-39b5-8256-ea1fc14485fd | 4.01494 | -51.63135 | 2026-09-28 17:13:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 71d9696d-09f2-3a1a-aacd-a074e846f796 | 3.92026 | -60.62582 | 2026-09-28 17:13:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 6d4f9db0-cea4-3b94-bf38-874352924aff | 1.68521 | -55.95579 | 2026-09-28 17:13:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 96ab51d7-a2f6-310a-a38f-1f21341975dc | -10.22 | -49.98 | 2026-09-28 17:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 1fd7d46c-6ac3-3c4a-a2e3-a6b2bc1e2e37 | -10.27 | -44.63 | 2026-09-28 17:15:00 | MSG-03 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0588a956-afa3-31e0-9fcd-8c893415aa10 | -11.86 | -50.92 | 2026-09-28 17:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e89638d5-d377-33da-a4d4-96c062d4698d | -9.45 | -41.82 | 2026-09-28 17:15:00 | MSG-03 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 9261d9eb-c3e8-3c11-af58-e7f05dea4f22 | -10.25 | -49.98 | 2026-09-28 17:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 38aed274-7395-3419-a1c2-5eaf1267e779 | -10.3 | -44.64 | 2026-09-28 17:15:00 | MSG-03 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d826beb7-afef-3a0d-809b-798ec726dc2a | -8.24 | -45.43 | 2026-09-28 17:15:00 | MSG-03 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 4ed670d2-96ee-37fe-977c-6a8b0d6299ed | -11.86 | -50.86 | 2026-09-28 17:15:00 | MSG-03 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f7254e6b-196b-324e-8150-3cea68e93e1c | -11.12 | -51.18 | 2026-09-28 17:15:00 | MSG-03 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| bd59c6b7-40ab-31c2-864e-4205582b79f5 | -10.22 | -50.03 | 2026-09-28 17:15:00 | MSG-03 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 94b36a04-927a-3974-8e55-b4a9698d3508 | -13.4534 | -46.3 | 2026-09-28 17:20:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 162.6 |
| 9d4116c5-6c56-3458-b775-bde19f536a39 | -12.1547 | -50.3735 | 2026-09-28 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 23db18ef-b0a7-3cc4-9fbc-cb23efde9eea | -12.6459 | -47.2823 | 2026-09-28 17:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 0f92faee-0ba3-39cb-8579-e3aeaf702e6a | -11.7828 | -51.0578 | 2026-09-28 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 0e991fda-7481-336d-ba19-075ea6db227a | -11.2859 | -51.3031 | 2026-09-28 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 387e07a8-54c4-3533-82fd-8cf77663148c | 2.1266 | -50.8788 | 2026-09-28 17:20:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 950b61cf-35c7-38df-acff-3eaf162cd31c | -10.6928 | -60.7322 | 2026-09-28 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 98.2 |
| c2db8316-03d0-30e3-a5c5-9768e2c49f86 | -12.2445 | -50.7271 | 2026-09-28 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 034b928b-221c-38dd-bcb7-048ccc73a801 | -10.824 | -60.7246 | 2026-09-28 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 144.1 |
| 7e531f25-0f8c-3272-af3d-3ee20821af18 | -12.1678 | -50.7576 | 2026-09-28 17:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 789fb7ef-0128-3e48-a1ea-330e172b79ed | -12.155 | -50.352 | 2026-09-28 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 6e147b64-0fb9-3fc4-a896-a98d5cc105e4 | -11.7138 | -50.5752 | 2026-09-28 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.4 |
| 56a530b1-254a-39e2-b311-195249d68008 | -9.9784 | -50.1412 | 2026-09-28 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 153.5 |
| 302252e8-1823-387a-b46e-6ddd11cdcfe0 | -11.7329 | -50.573 | 2026-09-28 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 85.5 |
| afb07d94-2982-30a0-bdf4-c85c0df7c413 | -10.1095 | -50.2135 | 2026-09-28 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c0d4e7af-6b1c-33c1-b12e-beff05bca1f0 | -12.1362 | -50.3328 | 2026-09-28 17:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.8 |
| fca620f6-d77c-3960-b792-418ced99121c | -10.7115 | -60.7312 | 2026-09-28 17:20:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 115.1 |
| 16bd82a5-5626-324a-bd37-128d3bd5af7b | -9.9396 | -50.2304 | 2026-09-28 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 174.2 |
| 47189ce4-93fd-3730-bc02-c16a3a4b816f | -11.1966 | -44.7805 | 2026-09-28 17:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 295.0 |
| 0f756192-446f-33b2-bd34-9af8523a72e5 | -11.0764 | -51.3885 | 2026-09-28 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 93.7 |
| f77994f9-6af3-3461-9d7a-b48d65dd0106 | -1.4116 | -49.0384 | 2026-09-28 17:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| ba4566be-9e49-3e03-8d3c-1d7865fc72c2 | -11.7643 | -51.0173 | 2026-09-28 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 0ad98b98-b855-3eca-8c57-449f9463bd5c | -11.058 | -51.3482 | 2026-09-28 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 0e24dd5c-438c-33dd-a20b-c62eef806c12 | -11.8427 | -50.8594 | 2026-09-28 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 143.1 |
| 05723b67-233e-36ca-add6-83021d2ace68 | -9.9582 | -50.2499 | 2026-09-28 17:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 48b262df-2707-362f-90f4-de8b99a7de37 | -11.7659 | -50.9107 | 2026-09-28 17:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 75.7 |
| bbd919d0-0dc4-33df-97b0-d4a46c89ccb6 | -11.1901 | -51.3766 | 2026-09-28 17:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9e5c6e74-1ef4-3255-87f8-44d1d1cc8b4e | -12.1866 | -50.7767 | 2026-09-28 17:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.5 |
| 74772afb-1ece-3b5a-8a8c-0650a4512039 | -11.7325 | -50.5944 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 95.2 |
| 9f030f11-9a1c-30dd-8f19-a066c2eb101a | -9.9396 | -50.2304 | 2026-09-28 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 2fcf4523-dcb8-3885-85ab-3a5545447f4a | -11.1966 | -44.7805 | 2026-09-28 17:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 269.1 |
| 8a1529aa-4b8a-3022-9c38-c48fb488cb4e | -11.7138 | -50.5752 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| ddede877-af61-3ecf-b2a4-a39f3b86a862 | -12.1359 | -50.3543 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 606418dc-52da-3403-b373-4b404fce49a1 | -10.7104 | -50.4718 | 2026-09-28 17:30:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 70.0 |
| 3141e478-d72e-30d7-8df4-145b22488967 | -10.9349 | -50.6612 | 2026-09-28 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 6a9505e8-e418-3a1c-ad64-d9b35a385107 | -10.2257 | -49.9879 | 2026-09-28 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 13bc7c97-76a4-3d8c-b935-7f09f8a56109 | -11.1178 | -51.1304 | 2026-09-28 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 1869d974-28b3-34e5-b648-7154a7afdacd | -11.7329 | -50.573 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 97.2 |
| 54cabc32-1681-3219-b123-237ff520b05c | -11.8659 | -50.5791 | 2026-09-28 17:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 66.6 |
| cd99abea-fa31-3d55-9c1a-8262f5f6bec1 | -10.2067 | -49.9898 | 2026-09-28 17:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 177.9 |
| 43534e90-90a8-3135-8efb-66992bd273ca | -11.7831 | -51.0365 | 2026-09-28 17:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 34e50452-e627-3dc5-8c5e-3ea032a31626 | -10.9156 | -50.6845 | 2026-09-28 17:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| e829c435-56fa-368a-8cc9-77492dc822dd | -1.3008 | -49.0613 | 2026-09-28 17:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |


[Clique aqui para ver as próximas entradas](README170.md)
