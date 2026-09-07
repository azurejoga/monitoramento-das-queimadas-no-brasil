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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d3576c54-6408-389b-8122-5463655b963e | -5.89125 | -45.54764 | 2026-09-07 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0f4cc4f6-3f0e-3a07-84f2-cd2791107aaa | -5.36678 | -49.19823 | 2026-09-07 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a4e31564-f518-30bc-8a69-7bb2060f6208 | -2.8738 | -50.45653 | 2026-09-07 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 014cf8a0-22b2-3ade-a49c-f9ec2edf8bfc | -7.10753 | -56.51594 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e662407-7faf-39b8-aade-4d1cc8817bc5 | -9.57512 | -40.35679 | 2026-09-07 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 82537aa6-a709-30cc-a158-67c362fae3c8 | -12.75883 | -52.85235 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e34cba-bd58-35c6-9f60-da804412776e | -7.69813 | -55.3817 | 2026-09-07 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e0d19db6-dde5-3500-81a4-3ec84d4aeeea | -9.73883 | -43.40442 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e0372438-2106-3b49-94af-26af0461b339 | -11.32091 | -45.05318 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 83727c41-d3a7-3dff-a6e0-328ddc6ebdfb | -7.11516 | -56.50535 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c92a6486-1ace-3141-8b6c-1485088fb3fe | -9.24732 | -46.68795 | 2026-09-07 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0dc97a81-2d25-3db6-8a80-5090665364dd | -14.53994 | -40.32401 | 2026-09-07 04:27:00 | NOAA-21 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 5afd60ed-07a7-3cc7-831f-5fd48cc95553 | -11.31973 | -45.06107 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8d51e2ef-70f4-34c9-ad7e-afcf1c91cbc0 | -7.11449 | -56.50911 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| aa525cc3-0338-3df3-8516-edbfd27efa50 | -11.31557 | -45.09917 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c5dc80db-11ba-3ac0-9739-eb3ad986d61c | -5.36624 | -56.02878 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 32242a11-fce5-3a79-b9f6-acd9d38864a8 | -11.33169 | -45.06202 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b54d294b-0b40-3ccc-85e7-e8fc8312e3d6 | -9.93493 | -48.05053 | 2026-09-07 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3e8b7793-fcfc-3623-b815-3696cbe60c2b | -11.32936 | -45.0534 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d9948ee-c431-34a8-b719-f96823644dc0 | -9.93882 | -48.04753 | 2026-09-07 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e7970d81-5a86-3e3d-88b9-961a2eddcd4f | -7.10195 | -56.51496 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e421361d-b45f-3279-99c9-a2c458314df7 | -5.35384 | -56.03421 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 253d1447-14d1-37a3-aca9-6a819f109df5 | -11.27847 | -45.09858 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93e0b3f9-5a6d-320a-99d0-8153c83d66bc | -11.18723 | -45.02964 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59db3ddc-bae2-34b5-8e11-a11604f47d21 | -7.16448 | -46.45766 | 2026-09-07 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a02df245-5364-3eeb-8125-f0f5e82c75fa | -11.51659 | -49.61677 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5147f78b-1381-3679-a05f-8196cb9e8f24 | -5.36259 | -56.01671 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0c56e12-5e3e-3bcd-9b41-c5db1e6625df | -13.31256 | -45.23455 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| fb494335-f6f5-3378-be42-ae445db58351 | -7.6919 | -55.38694 | 2026-09-07 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1b104a87-5e47-3e63-bb64-43cb3e87fab4 | -5.36369 | -56.04359 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e3ef9f-555b-3b27-a887-15f9a5dd1ae5 | -10.73788 | -45.08346 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d788d8b-baf8-368f-ae45-76b51f036235 | -11.31331 | -45.10394 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 52c7e500-4718-3b37-8b5a-a3d0be43c083 | -9.74632 | -43.40526 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 9a078e28-0ffd-3f1f-974e-9760b2914f99 | -5.31861 | -55.87675 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a208213-d778-3867-b599-78dc2f79f18f | -11.31963 | -45.09579 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ffcc77b-e9e2-3536-8001-0209a9ef8002 | -9.73073 | -43.4079 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7f78b942-d87b-3c5f-9a3f-d74c100fbea4 | -10.66633 | -47.57521 | 2026-09-07 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9775566a-0813-3ae9-9515-9228cf587a49 | -10.73904 | -45.0757 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 936b783e-6193-3996-b304-4eface581a3b | -13.3049 | -45.23752 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91569485-44b6-36df-a0f1-da6a9bb99914 | -9.93826 | -48.05106 | 2026-09-07 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3683d19b-571f-3d6b-b5aa-64993f527821 | -10.74193 | -45.08015 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 08f8fb84-b655-3e85-8754-2573d1b8d564 | -11.94668 | -44.85892 | 2026-09-07 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 437af5dc-50dd-38c4-bc95-f26b6358ade4 | -12.75607 | -52.84461 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a2549ef7-263d-3b8c-ab83-d7a338478171 | -11.33064 | -45.09369 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 880e1e6d-b90a-3293-8813-c3553d896666 | -5.83253 | -60.25459 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 479f378c-bbc8-3c14-a2c4-6db8bf1180da | -6.05603 | -57.80065 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2cd3d904-5ad5-37c9-9732-1923eb826131 | -9.73446 | -43.40839 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| a3c5b949-01ad-3ec8-9158-c95f2a62658c | -7.12015 | -56.50963 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c9a759a2-23eb-3b7b-aa84-aab4a6b51ae2 | -10.66707 | -45.17907 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 81152e7c-7624-345a-bebf-9b0413ad3a18 | -11.31842 | -45.07959 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1baef09f-0572-346a-95d5-49e0baf7261f | -9.74387 | -43.39575 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 23b881cb-2dbf-3653-9abb-16f67c293273 | -7.10821 | -56.5121 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46d22318-e599-3c47-97cb-7919e71e4542 | -8.37488 | -46.61375 | 2026-09-07 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f146f24d-1b89-3a23-8665-0158895d861f | -5.99925 | -57.69277 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 48570adf-3f0a-3a95-870f-039f8608e2a8 | -11.94609 | -44.86298 | 2026-09-07 04:27:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 093cf0c9-f83f-386e-af51-570b83021e5a | -10.03794 | -48.21614 | 2026-09-07 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7c33e3e-c9e0-3173-9c8e-2278adbfe52b | -9.73195 | -43.42604 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| d736fe61-18bc-36ce-b812-7109870ed7be | -11.33576 | -45.05852 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 344b927f-7e13-3475-a950-82e85165396f | -5.32411 | -55.87777 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 892c167e-3e65-30a3-9ed9-880e78f6d2a7 | -13.29902 | -45.22828 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1bace2f0-2828-3612-8771-e0bfe333e6c0 | -13.29549 | -45.22771 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93d0fcc2-2b29-3720-bf65-f86765580330 | -11.33758 | -45.09502 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 3349e384-fc0c-3264-a18a-571998a408e8 | -13.44782 | -41.88745 | 2026-09-07 04:27:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c846b0a7-3f8c-39ca-9b69-2281cc056498 | -9.51256 | -41.99305 | 2026-09-07 04:27:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b229debe-51ec-378b-aef0-2577b18181a0 | -7.41548 | -46.55064 | 2026-09-07 04:27:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f196037b-798e-35ac-806f-54b9c9619b42 | -11.52907 | -49.62663 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 25eeed4e-5f9a-36a4-a556-e1e89113616d | -9.72949 | -43.41659 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 65f70f93-5441-3f47-a913-4a5baecd043e | -12.76738 | -52.85032 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3bcc258b-2346-3cad-8048-538d63d764f2 | -6.05684 | -57.79329 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 652ae4d7-6dc3-3665-b0b8-6815fe3e683d | -9.75069 | -43.40129 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 30.3 |
| d15af8ab-2637-31cd-a9a3-508e29b1e527 | -6.11027 | -57.63855 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| dddf6c3b-be2f-3c79-91d2-a3d8d6111c65 | -9.73509 | -43.40398 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0b5305d4-479c-326c-8b38-2087e262404e | -9.51661 | -41.99365 | 2026-09-07 04:27:00 | NOAA-21 | REMANSO | BAHIA | Brasil | 2926004 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ae2d10d9-6885-311a-b84a-6590699ed391 | -9.73258 | -43.42159 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 89e057d5-29dc-3166-9076-deea35fd314b | -11.32659 | -45.09695 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 54149b7d-7b5b-3392-b2e1-d2b099a62179 | -9.75249 | -43.41531 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| eb12b830-8906-3e1b-873f-5d2686cafd38 | -5.36751 | -56.02137 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7ee29a72-8219-33ff-b6ba-820ad6a1127c | -11.33411 | -45.09435 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| 69fd0d84-beb7-3be4-92ea-cdcfc1bdf312 | -8.57105 | -45.98202 | 2026-09-07 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 96bb1a9c-7335-3e8c-8ea5-029dae09feab | -10.37295 | -45.01407 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d91bfb11-75ef-37fb-89e0-86b5ecc12171 | -9.5706 | -40.35614 | 2026-09-07 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 32813489-6d40-3a9b-9671-63e95ee312e2 | -11.32878 | -45.05744 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 34f61965-b158-3b94-9dfb-f6d91a206e8e | -10.88671 | -44.17513 | 2026-09-07 04:27:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 07e30f32-ac9f-3bd1-94b8-b19c41c7173b | -11.33177 | -45.08595 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f663cf09-9fc1-377f-a9c9-e650891b81c2 | -5.99315 | -57.6916 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7433c319-9635-3497-984f-13c74336d424 | -11.32368 | -45.09249 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54528045-3a57-305f-a36c-303cbc5ce726 | -11.33467 | -45.09046 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| fb6de64e-2b27-3727-8854-af4dea363c98 | -11.3093 | -45.05923 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 416ddb60-cb61-3030-bd2e-00d0405ebec1 | -5.99151 | -57.70066 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 034bc3ed-c4d3-3128-a7ef-cd7b1bd7286c | -9.73757 | -43.41331 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3440feb4-45c9-385a-95f2-8563759db080 | -5.3718 | -56.02976 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 87cd60a4-60ec-337b-807e-9237668c8c01 | -9.73136 | -43.40352 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f5e8e4c3-ed83-3251-970d-272f5f96ccf8 | -6.06131 | -57.80356 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 87d031ec-ec20-346e-bb13-d18bafeeeacc | -13.30549 | -45.23347 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| c71afa7b-90b8-3b20-8e08-a4f9bfaf42c7 | -6.06225 | -57.8014 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3099f079-61a5-36a6-aff1-02c25ff5c41e | -13.3102 | -45.22589 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80fbc922-c4a5-3b3a-9de7-227ee49de07d | -11.18665 | -45.03353 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9655e622-1cd1-3e17-9dc1-49ced0681425 | -7.11313 | -56.5168 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7f9b64e8-6a94-31dc-a7a9-776231aba372 | -9.73384 | -43.41276 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 99c015c5-7690-35f2-96bf-5b9fb6b027f3 | -11.34101 | -45.07154 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README15.md)
