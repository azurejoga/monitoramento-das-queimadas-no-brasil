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

## Dados Diários - Página 156

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 978517be-0167-3300-82ec-6af6189928f4 | 1.93728 | -55.71214 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 745e7700-0b98-3613-85a3-211c54910cf4 | -9.56557 | -64.33973 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 79a22e00-6641-35ed-8d59-8a3906ffa6e7 | -9.20053 | -65.78223 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 217bf982-48b4-3cc3-a01d-7d5ce9a1f925 | 3.07133 | -60.65253 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 72193fd2-ba6c-3aeb-ac90-5f0267672041 | 0.31424 | -51.00046 | 2026-10-05 17:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1c80a078-89a8-3b32-b444-82ad49b173a6 | -2.48236 | -57.78755 | 2026-10-05 17:37:00 | NOAA-20 | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| da0710c3-8e65-3e4c-9da3-9c7a41b25c93 | -7.21098 | -55.19456 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| f93e6619-f29e-3f41-b38b-cb6761bafd42 | -10.64567 | -68.61086 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c2331183-8b1e-3e10-aafb-b45216bba4d9 | -8.59407 | -70.0798 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 32.0 |
| 04e32ef8-d416-3c2e-9720-f3743b2be71d | -9.93965 | -67.89151 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 48484d75-9f7b-39d1-9f1d-315d25bc3c80 | -7.3348 | -55.73883 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 354d6e31-4364-3871-b017-ee0068cd5b45 | -2.34607 | -57.11828 | 2026-10-05 17:37:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4471cf4b-2f29-3874-94db-4e9bb2655a5d | -9.73859 | -65.0829 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| c9a7f10b-3c19-33e0-aff3-99aa7ed11f5b | 0.31315 | -60.44092 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 361789a6-f543-3b07-b5bf-021921f85826 | -3.03507 | -59.21988 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e8ff1c14-caad-369f-b0e7-d87e70353e8a | -8.63558 | -70.03762 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| e4d6c79c-37b6-3461-95af-317bdc5df193 | -1.36034 | -55.98269 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| f54839d5-4051-331a-a132-765ec80f82a8 | -8.62716 | -69.50765 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 6b790cc9-0c64-30ca-b00f-8ad035c90fff | -9.11002 | -64.37209 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9f44cd80-0595-3d92-aeb1-5e95d8dd14c5 | -8.92346 | -66.84585 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 14.9 |
| 0ff52c25-92b7-34cf-ab60-5e7f8acf8913 | -2.74307 | -64.49523 | 2026-10-05 17:37:00 | NOAA-20 | COARI | AMAZONAS | Brasil | 1301209 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8d310325-898d-3705-990b-d568bdb63710 | 3.07189 | -60.64889 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7e4a0713-fdd5-3ed5-87fb-b418d131af3f | -8.3198 | -67.58721 | 2026-10-05 17:37:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 802022cd-f683-36dc-962f-6921fe2084a0 | 1.61566 | -55.78504 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| 00a2a3c8-8cd6-34ff-8279-2416595b34b0 | -9.35931 | -67.44004 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| aacb63d6-b0ac-34f9-bb37-7709bbcbf540 | -9.50385 | -67.13818 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 0dfd559c-0076-3ce7-8afb-d74ca4d26bfa | -8.6361 | -70.04163 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 819338fa-7796-3244-babb-a8d18408aa63 | -9.32495 | -72.6861 | 2026-10-05 17:37:00 | NOAA-20 | MARECHAL THAUMATURGO | ACRE | Brasil | 1200351 | 12 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 314a0659-7a0b-3ef1-aecb-72976cd0dd8f | -9.92042 | -65.03316 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| b9d7e26c-c8e0-3644-ab04-069f5642e9ed | -9.4998 | -66.78541 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b971b01a-6772-3248-92ff-4f7f3cd1e192 | -9.23058 | -67.89026 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 9f123805-a5b1-3d8a-a197-0804b3da1445 | -9.4046 | -65.89886 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 0ec8e34a-8fc6-3f47-a687-480078e23065 | -3.18442 | -60.0552 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f9d42d01-0291-39d3-a81d-4fe47014cd15 | -1.63317 | -55.1317 | 2026-10-05 17:37:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 974e3fad-316d-3533-96d4-e0e2ea0d27b9 | -8.30958 | -54.66885 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d0eae75-d3cb-3f53-9865-f72289d91e28 | -9.99816 | -68.5516 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a7da4859-3fc0-397c-abf1-a6d50130765b | 4.20818 | -60.70954 | 2026-10-05 17:37:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 585027e9-7ebc-3acb-81cc-676518209800 | -9.32782 | -66.58786 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 30.7 |
| 2d092039-c9aa-32dd-95ae-c4276e329699 | -9.01554 | -68.42878 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d9a24fa5-71fd-3b7d-9f54-ba808d18cf05 | -2.32645 | -56.84749 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9eb0f783-dd0c-34ca-b901-30fd316b634d | -9.20713 | -71.86001 | 2026-10-05 17:37:00 | NOAA-20 | JORDÃO | ACRE | Brasil | 1200328 | 12 | 33 | nan | nan | nan | Amazônia | 14.4 |
| a6643214-249e-3a53-87a0-8134be45ceb7 | -7.86847 | -54.70096 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| b9c106c5-f954-3d80-abf2-027434c3ce5b | -10.63161 | -70.08459 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 40166c4e-12e3-30a0-a031-e98085805cf7 | -8.90322 | -69.3885 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 9e005e4e-9455-340b-885e-bb594235c467 | 1.92607 | -50.93583 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 92c2d8f4-9645-3b74-b0f5-fa692f45821b | -8.59663 | -66.81278 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| fab4dd48-d7db-3f0d-8220-b81bbb6b0f02 | 0.44525 | -60.53391 | 2026-10-05 17:37:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 6bd4d176-b152-3b4d-96dc-c57c4d309815 | -9.40476 | -68.87682 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 821ed6eb-79c7-3226-a360-2e7bb86a04ae | 1.74222 | -55.60442 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3707d1e4-16e8-3f88-90a4-4966fab05c3f | -2.59919 | -57.5517 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7aa1ae31-3f36-3021-be8e-8c1aaf451b54 | -2.77983 | -57.63174 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7811dd40-a573-3d92-9e18-1bafbefe9fdb | -9.17718 | -68.26984 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 73.5 |
| 530f5331-25e8-31dd-8014-0cd8288cf638 | -9.23617 | -67.89034 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 284c9bb1-8120-3722-ad2d-1f0ebdc9bebb | -6.37604 | -55.21114 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 31758e15-6f1c-32b7-a442-4bcb4be81890 | -2.09446 | -56.62567 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 10c19a56-2377-3dea-900b-4202a0b2c9d5 | -9.19997 | -65.77804 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| a9868cd8-73e4-3a37-af7e-11d998712488 | 3.57443 | -61.33544 | 2026-10-05 17:37:00 | NOAA-20 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 331421b9-85af-3722-838e-768cb6adfa50 | -9.38794 | -68.32985 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 74b4aa81-d886-3322-a710-6667e3263309 | -9.02794 | -67.55264 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 9cd91f9f-03fd-3e16-bad1-d682f1d16157 | -8.63273 | -69.5069 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 16.8 |
| 4282a0fb-3ce5-3b75-8e21-baa4e8f8d39d | -9.09902 | -65.73086 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8bf6a706-78dc-3236-82b7-089f52dc260f | -3.66078 | -69.43225 | 2026-10-05 17:37:00 | NOAA-20 | SÃO PAULO DE OLIVENÇA | AMAZONAS | Brasil | 1303908 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 506a8235-6bb6-3904-b973-b84a7a532d06 | -2.76857 | -57.65529 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 468d218d-4a21-3c29-aad3-2f8560383048 | -8.67865 | -67.2401 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| ff42226b-c32e-3614-9638-c19afe30cd07 | -9.14466 | -67.9355 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 93d526ee-d8d3-310c-827b-89f8ca91f5f8 | -9.13923 | -67.93324 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a3f60d0d-3869-32bd-900f-c92003d21176 | -2.78356 | -57.67915 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 7d57aa64-8f0f-3059-a4dd-1e2e0cabdfcb | -2.54221 | -58.00493 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 486323e4-c7d6-3dd7-a66e-7c0cce03c28d | -2.53822 | -58.02662 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3df0d6c1-574f-335f-95ba-8f3e2dcec184 | -9.13961 | -67.93619 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 93ddceab-b8cd-32d5-83a5-552cb9d63556 | -9.13187 | -67.75838 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.1 |
| d1880cef-c1bd-3cb1-ad63-f56946c3b0da | -3.18389 | -60.0517 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 2649ca9b-f84a-3cae-83a9-eca810db63b9 | -9.21977 | -67.38322 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 79b7be27-c292-3b91-b27e-bb1dd3baea20 | -2.13728 | -56.6949 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| cf10014d-76b7-346c-a9f1-a1ff24c32605 | -10.0855 | -69.15553 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 55d7c2bc-1deb-30a8-a80e-49988d592219 | -8.64586 | -69.26445 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b3cf53de-04bc-3bd2-b38e-a995dbf9947a | 3.41808 | -51.31987 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d93d7416-a560-3591-8559-1c7ffc206e38 | -3.03733 | -59.21203 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a94801a7-bba4-3961-a266-a42dbe3a205f | -9.4232 | -68.84966 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 1769a0ef-f60f-3612-926c-649e81894439 | -8.61985 | -66.98437 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9648a305-6c1c-3699-be80-921bfe2a1809 | -1.46052 | -55.26724 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 88d9a8a0-40d0-3a77-b272-adb11f3a604d | -8.53164 | -67.01904 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| f0218f0c-ae33-37a4-a128-0648c7c7014a | -2.1889 | -56.6382 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a07bd7e9-52be-348e-b471-2269cb20ab72 | -6.38192 | -54.97134 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| b449e55f-3935-333b-858b-9e7ca7e90d80 | 1.61439 | -55.7934 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 91c2cb21-92b7-3647-81ea-e085d0c9ea18 | -8.79735 | -66.92025 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4297a166-a053-35ea-9aee-c555f8c6b508 | -9.40843 | -65.89397 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 3b92b55e-9719-36eb-9a6c-d6dd0e5512f2 | -1.28022 | -55.41267 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| 90355f3b-7807-32fb-ba86-17344c4403ca | -9.47861 | -64.34391 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 905660d8-8073-35ac-9aaf-b7f880cd85e9 | -2.01575 | -66.31956 | 2026-10-05 17:37:00 | NOAA-20 | JAPURÁ | AMAZONAS | Brasil | 1302108 | 13 | 33 | nan | nan | nan | Amazônia | 11.5 |
| c61caf2d-ce61-3dc0-a8cc-74ec92bc63f4 | 3.53385 | -51.51169 | 2026-10-05 17:37:00 | NOAA-20 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3f2bad9e-655e-324f-a3c1-fc6e9bbe1915 | -8.57106 | -67.13146 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6665e3ae-cecb-3e6b-bc54-1f8db2b85752 | -8.52915 | -54.60934 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 4129800c-9519-3d5c-bff8-2b9ef4814cff | -9.1439 | -68.23004 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 17.7 |
| f81c490e-e84f-355f-8258-e721ed7470f0 | -9.10748 | -65.35444 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 26.6 |
| 8662ecfd-b6d7-358b-a58f-44d55c8f3031 | -9.43939 | -67.42229 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 0bf3d099-acb3-3ac7-8a62-e8d45b707da3 | -2.55405 | -57.98622 | 2026-10-05 17:37:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 60fbe87d-7506-335c-a27a-c90cdd948b4a | -8.76046 | -68.97409 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 52fa8462-e7a4-317b-afc3-dbbba2a62a9c | -10.38033 | -68.95927 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 7bd0aa0b-46b6-3c07-b635-632aff26658c | 2.09622 | -50.72736 | 2026-10-05 17:37:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 10.4 |


[Clique aqui para ver as próximas entradas](README157.md)
