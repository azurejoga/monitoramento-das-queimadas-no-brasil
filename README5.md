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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eede89ff-fa84-3a33-a7cb-510802030413 | -3.9653 | -48.120399 | 2026-09-27 01:15:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 977a56f7-3997-3631-b8cf-2027687178de | -17.791901 | -47.159199 | 2026-09-27 01:15:00 | METOP-C | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| c92f0d75-d799-3038-81e7-ba9ddba5f0e9 | -6.074 | -57.809399 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65f71189-e4ed-3864-b484-bd6f39e927ab | -10.8075 | -60.711399 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 90dc61f9-aaec-3381-85b0-4a9d771a6b30 | -3.2201 | -54.326199 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e897037-f74e-3bc7-aa46-e12bd5e2aca8 | -21.632999 | -50.061298 | 2026-09-27 01:15:00 | METOP-C | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a479a61c-0728-3b7a-a0a7-18a525269f60 | -2.9459 | -57.709801 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| cec25147-7199-32ec-a557-e8426214157d | -4.5482 | -54.9758 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfa51259-7d20-3c13-baad-623b56c95d59 | -12.285 | -50.382301 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8b5d750e-997e-3c9a-85a1-0035819edd7c | -7.9678 | -54.901299 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ad543a5-7bc2-3b84-ad31-1050d7411f86 | -2.6565 | -56.548698 | 2026-09-27 01:15:00 | METOP-C | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a3e0480b-abc6-3d7e-99a1-c1f310dd8d23 | -1.0465 | -53.571098 | 2026-09-27 01:15:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fd383645-9aec-3adb-bbcc-e09dd9805bfd | -4.5384 | -54.978001 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6f1c8d6-ee12-3c19-87cd-6239bd4cb6d7 | -11.9605 | -50.573002 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14077811-4942-3df0-abc3-a8010fe70ac0 | -6.0674 | -57.825298 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d9a8d32-f9a3-3f22-828b-8ec354afce72 | -10.4152 | -53.808701 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f38fb283-829f-346d-80cc-099fbb55f027 | -1.6802 | -55.8965 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9cf31b4-70f2-334a-806e-82eeb2bec4bc | -4.5638 | -54.954102 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e9db3bca-2d8c-3eec-96fb-39baa03a61e7 | -3.2322 | -54.333599 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| de240c28-0f8b-36a0-9246-57511a49b2e3 | -7.6836 | -54.747299 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8dd6984-9acb-3f4e-a6a3-52e9ae8a8f6e | -11.9157 | -50.518002 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0b53492b-b7eb-3d86-ab28-3011a33f89a1 | -14.122 | -46.328701 | 2026-09-27 01:15:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| c158c210-be79-314e-a88a-e81ae53e64a9 | -2.6763 | -56.4561 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e04e2c17-6a72-3a7f-adc5-eacf4ac847ec | -5.162 | -56.009899 | 2026-09-27 01:15:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c868c95-66fa-30a9-aee7-7f326262b224 | -1.6043 | -54.816601 | 2026-09-27 01:15:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab076998-205b-3b90-ad95-cb6509e26a69 | -8.0265 | -54.887501 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3de537be-5031-34b2-9a2c-4034da9eb638 | -11.9285 | -50.528 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 24c7c21b-6ead-320f-ae83-781871f0bcd3 | -6.7271 | -52.987301 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eb8144e-7dda-3bb8-bcef-34fb9eb26201 | -3.4232 | -50.4286 | 2026-09-27 01:15:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0cca4731-3ef9-35d9-a619-aca73f1c27f1 | -2.9305 | -56.5741 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cd32ecb1-2964-3911-9d33-f4399dffe1da | -11.9667 | -50.597801 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88890940-a07b-38c9-b650-8f602a06b38e | -4.5716 | -54.943298 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66be8eba-6014-31ee-b4a3-fff79f447d1b | -6.0756 | -57.816299 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e02c6d70-1952-3956-91bc-078c04b626cb | -6.0658 | -57.818501 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85b23030-a841-3322-891f-6ecbbfa0fadf | -12.1264 | -50.245701 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2e899da6-4a9e-3bfd-957a-57b383ca46e8 | -2.6781 | -56.463699 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 588c8426-91ad-35f2-90a0-f3ff61bd9fe7 | -3.0751 | -54.410198 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c6307c7-8617-3664-a6eb-1a5506fbd16f | 2.636 | -60.169998 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| b22b9940-8c90-3f53-9908-ec5f31f3ab72 | -12.311 | -50.321301 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9beaedd6-8931-3529-b6cb-c8d5977bf8b9 | -3.8543 | -52.007801 | 2026-09-27 01:15:00 | METOP-C | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08344968-4dcf-317c-bb91-5704f7060967 | -17.0495 | -56.584301 | 2026-09-27 01:15:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c311226f-4931-34a1-9563-b4103b27d2d5 | 1.6626 | -55.9589 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d436c81f-4cf8-3c75-b751-a5515503b712 | -11.922 | -50.543098 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d80178fa-dba7-32f1-bdb1-af20d36cdd40 | -12.1231 | -50.2327 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b35dba2-c40a-32b0-acd9-c562845fdfff | 2.6427 | -60.185799 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9282abcd-7a22-3681-8005-bf85b32e12d4 | -10.4229 | -53.797901 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ae0a100-43b6-3b20-a9b7-dd2d1c5d0eef | -11.9853 | -57.6045 | 2026-09-27 01:15:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d25432a2-482e-355e-8d6b-72d74e8593a9 | -4.5287 | -54.980301 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 821ba04a-5630-33c8-b982-821016668b8c | -8.0498 | -54.8988 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85ec07f4-e739-3666-b868-0acd3ab93ff9 | -11.0491 | -51.314201 | 2026-09-27 01:15:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a9fcaf0b-2cba-35f5-a8a3-ed8d2a7fe4d2 | -4.4893 | -54.944099 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5d2949c9-9025-3293-af20-26da700b7167 | -11.9734 | -50.582901 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 90e64c87-b289-39a2-ab0c-e12c744fd5b2 | -12.0546 | -51.406399 | 2026-09-27 01:15:00 | METOP-C | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 05374d22-fd03-396c-b3d7-51eddd689d53 | -11.9862 | -50.5928 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3e7da900-b67d-3184-af49-a6de9dafceea | -2.5747 | -54.034401 | 2026-09-27 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce9c1b3-51b3-36b9-ad67-7a423156f074 | -14.116 | -46.306801 | 2026-09-27 01:15:00 | METOP-C | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| acd0c158-7004-302a-967c-6c508920ebb3 | -12.1686 | -50.331001 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d4ce9b4-1c39-3e56-b0f9-88a9767f69a9 | 1.6492 | -55.927502 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 023affef-a123-3616-9f11-91ea04a8f4e2 | -10.6726 | -57.629902 | 2026-09-27 01:15:00 | METOP-C | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| dbdb3735-9ae2-34a2-b783-ea9176602d56 | -12.2851 | -50.3008 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ddf4f3b2-5f5a-3751-90d6-d3f263a9e250 | -11.0365 | -51.305199 | 2026-09-27 01:15:00 | METOP-C | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6880349e-f50e-3869-8d4c-a89c166dd82d | -12.7306 | -50.672798 | 2026-09-27 01:15:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 574e3b3a-0417-3ece-bd71-ebbf92bc3769 | -12.8912 | -61.7146 | 2026-09-27 01:15:00 | METOP-C | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 86959174-7968-3b75-8bd5-fe96bd85d2d8 | 2.6443 | -60.179001 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 15b1a65f-b3e1-3495-8c4a-ce32dd4de94c | -15.9905 | -54.9375 | 2026-09-27 01:15:00 | METOP-C | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| eec858a5-0b3f-3e63-9678-c968f5b7c21a | -10.4074 | -53.8195 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a9a44b8b-68c4-35a5-aa66-aab784ef9c50 | -10.4054 | -53.8111 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 71f43f2f-3561-3c3d-84ec-8caeaf6ed803 | -11.8153 | -50.530399 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6879cd6f-8637-34c5-9fc8-ddf2670f4306 | -2.511 | -56.233101 | 2026-09-27 01:15:00 | METOP-C | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a652f79a-5052-3e65-8cb3-66201e60d7ed | -6.0576 | -57.827499 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85bdc94-c3e6-3446-a749-2df251c618ff | -3.963 | -50.709099 | 2026-09-27 01:15:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1cdaf42-e3a6-3fbe-9c2f-d5e830b46246 | -8.0479 | -54.8909 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 39e1900d-086d-3964-99f4-ae55dcaaf826 | -17.047899 | -56.577 | 2026-09-27 01:15:00 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d6dee5d9-5cac-321f-8ca1-ec3c7f0a462e | 2.6897 | -60.1605 | 2026-09-27 01:15:00 | METOP-C | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3664d5-e0fb-3511-9d17-06f13c5afb5c | -3.2277 | -54.314301 | 2026-09-27 01:15:00 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b6a19414-71c7-3d70-aae5-9a0988c0c115 | -5.17 | -56.0 | 2026-09-27 01:15:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aced923c-ba6e-3fa1-88a6-a9c8bedb3901 | -11.0279 | -54.038101 | 2026-09-27 01:15:00 | METOP-C | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce50c311-9e09-3809-9265-afebab6e364a | -10.4192 | -53.8256 | 2026-09-27 01:15:00 | METOP-C | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1a80442e-8854-3321-b210-161c05ccf940 | -2.7875 | -57.693901 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9d9ddddf-2c95-3058-acaa-7b0341184f9c | -7.6874 | -54.7635 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3da2f7-4f00-39cb-a915-fd19b83a0e00 | -4.5618 | -54.945499 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a7d7056a-c8e4-309b-8436-0e8520d51557 | -10.8211 | -60.727001 | 2026-09-27 01:15:00 | METOP-C | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 62b82700-7103-38f3-8119-108b6c36a057 | -8.0382 | -54.8932 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1055c169-657a-3a4e-942b-e3c3dc3bf174 | -1.1483 | -54.096298 | 2026-09-27 01:15:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11e024d3-d4bc-30f4-bc3e-be861234788d | -2.0613 | -56.8731 | 2026-09-27 01:15:00 | METOP-C | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 82aae1cc-72cb-3028-89f8-760e268d3e46 | -14.4129 | -52.798599 | 2026-09-27 01:15:00 | METOP-C | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e03c18c-3eb9-30d5-9899-7e2acefafd13 | -4.4991 | -54.941898 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7f1cfec-4ba8-3ec3-84ed-a82c6fe9c99a | -11.9476 | -50.563 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a31f980d-fee2-3095-b811-797d59b3ea1f | -9.6179 | -55.110901 | 2026-09-27 01:15:00 | METOP-C | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 5630a3f8-457e-38b6-bc48-c52a43352f58 | -3.9669 | -50.7253 | 2026-09-27 01:15:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e19011e-bde7-3c8c-b2f0-cc5a30523a32 | -6.069 | -57.832199 | 2026-09-27 01:15:00 | METOP-C | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a029662-3c94-38d0-8d7a-e8092d373f16 | -4.5442 | -54.958698 | 2026-09-27 01:15:00 | METOP-C | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1152c6e0-aa03-3383-bcc2-3c12e3d95e57 | -6.1337 | -53.0508 | 2026-09-27 01:15:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9915e88-0766-3e5c-86da-85f305bc0652 | -11.906 | -50.5205 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c87fab4e-78fb-313d-b343-d4afdb76a098 | -8.0363 | -54.885201 | 2026-09-27 01:15:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20fc6cfc-bb85-31ca-8464-3d096908d499 | -12.0313 | -50.607498 | 2026-09-27 01:15:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 30569af4-5e10-3016-9db2-a349a4384ad7 | -2.7989 | -57.6987 | 2026-09-27 01:15:00 | METOP-C | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 53cf1ac1-7360-3c42-9cfc-6c7bbb03a29e | -1.122 | -57.2714 | 2026-09-27 01:15:00 | METOP-C | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2aee2681-2de6-3b1e-9293-ee47dce67539 | -1.0438 | -53.559502 | 2026-09-27 01:15:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8966ab9c-0509-39c5-8788-efcaea754f46 | -13.379 | -51.3214 | 2026-09-27 01:15:00 | METOP-C | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
