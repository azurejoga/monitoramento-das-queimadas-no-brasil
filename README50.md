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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1557899e-2465-32ad-b156-322d3b4bbd74 | -2.51888 | -51.93036 | 2025-10-07 04:34:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 34b7d763-4df0-304d-885e-9348095572ae | -1.56387 | -55.43593 | 2025-10-07 04:34:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 03b88d84-cb3e-3c7e-abcd-07ba0a17c756 | -4.45295 | -43.22416 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c08abe2-3a34-39a4-880d-92ab52b850d2 | -3.09237 | -47.01452 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1920a178-66ae-3b7b-9eaf-66ff9469b3c8 | -3.1385 | -50.44672 | 2025-10-07 04:34:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c7c94b7-0171-32b9-a393-aa5f355ae8b2 | -3.09406 | -47.02541 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 71c18c54-3017-3a41-9123-23070a000f50 | -3.10234 | -47.01608 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b425d730-50c9-3dc9-9a42-a056aaae57fa | -4.45224 | -43.22894 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 88f2d67a-bbdc-3003-9743-62a73a011930 | -3.20472 | -51.01576 | 2025-10-07 04:34:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd2cc6fe-299f-36e1-b6b0-8378845421c2 | -3.0887 | -51.25142 | 2025-10-07 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 07d934cd-c551-3fc3-a026-ad0ba1fdd853 | -4.44382 | -43.23252 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 98ce9bbe-72c9-343e-9dbd-ea655431f7fd | -5.20924 | -37.62715 | 2025-10-07 04:34:00 | NPP-375D | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ac4362be-56e1-3da3-b2c5-426741845ae6 | -4.4498 | -43.21878 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8d090840-bbe1-3ebd-aa4d-aea7cd33ce84 | -3.69863 | -49.41713 | 2025-10-07 04:34:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31f364a7-688d-3d90-a5fb-cd98e1f78087 | -3.09515 | -47.0185 | 2025-10-07 04:34:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 46a969a4-4250-3064-8b73-7633bffd2043 | -1.61528 | -46.66276 | 2025-10-07 04:34:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4445dd2e-0f20-3104-a54e-64b28bcc8b6b | -2.80049 | -54.85867 | 2025-10-07 04:34:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 83dadca4-2005-3ce4-8e30-dbd9f5142d25 | -4.86566 | -42.78628 | 2025-10-07 04:34:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d680209c-2616-3c44-8c33-f2a672a2d266 | 0.74757 | -51.58167 | 2025-10-07 04:34:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6f0f784f-cf61-3d3e-bbe2-7a416b4e0c14 | -2.93531 | -54.17562 | 2025-10-07 04:34:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0b176a5c-9112-3726-8b9f-f96bb4769734 | -4.43999 | -43.2244 | 2025-10-07 04:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e6fe7b10-26bf-3864-a9fc-d56f805e7cd5 | -4.86168 | -42.78565 | 2025-10-07 04:34:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0440ce98-067c-3448-b3d2-1f6c721feb9d | -3.08681 | -51.24873 | 2025-10-07 04:34:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 888c1207-ee67-3c38-8dde-30b5aff4484a | -2.79877 | -54.85772 | 2025-10-07 04:34:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c6b9b782-8db6-368a-8a1e-b85015fa0fca | -3.87251 | -38.43067 | 2025-10-07 04:34:00 | NPP-375D | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 8cb4d71d-66f2-36b2-bf85-9089bfa82f64 | -5.77358 | -45.74598 | 2025-10-07 04:36:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3ececd12-806d-3d9e-ac98-31e1b540d0f7 | -10.38992 | -45.3826 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e2cbc2c7-c4a6-3f6e-8836-c50a4f3d6368 | -7.69688 | -48.05965 | 2025-10-07 04:36:00 | NPP-375D | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 15b11fca-5b61-386d-8fe1-0b4231f1287b | -5.40153 | -45.91459 | 2025-10-07 04:36:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 05f5b110-64da-356c-8b45-cf06888346f1 | -8.55106 | -46.24535 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c5a75c41-9325-3a9b-9e74-b44e40558d71 | -4.6855 | -49.49306 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a5210255-3afa-3a5c-9497-1c1c553a613f | -6.98429 | -42.87118 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 97b33b66-cdb1-3aa5-af7e-6db0ccfa1f86 | -4.27256 | -48.63267 | 2025-10-07 04:36:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| eef0c61c-138e-3aac-b331-2a6e88d60e23 | -7.77997 | -44.20145 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7b6cacff-1a5d-36c4-9198-086135bcf16c | -8.18071 | -43.34773 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 76ebd903-45b2-3ba5-9149-6e01aee55275 | -7.62663 | -43.06371 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 83f03056-c3ac-3893-8f63-4134b134ba6b | -8.6754 | -49.94187 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9c9d0fc3-95bf-33a0-bb54-bf44d0ff48e1 | -7.79019 | -42.6102 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d17060d9-c074-3f63-b64c-8733cf5605e9 | -7.67776 | -42.58712 | 2025-10-07 04:36:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8fd28206-183c-3442-93ec-a1985c7511ed | -10.32195 | -46.93393 | 2025-10-07 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 6ef3625d-d14c-31cf-a4f4-816cbd65df7b | -7.47152 | -42.61773 | 2025-10-07 04:36:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 27903ab1-09e4-3c60-b02e-112c60cc2484 | -5.59947 | -43.10749 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1f481a6b-dc6d-3f4b-b55e-0e9d88f4d17d | -6.71945 | -42.84391 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9883f58b-71a3-3eb8-8d10-80d5c507c7b3 | -6.01211 | -45.41821 | 2025-10-07 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b14b3465-c1bd-3ba1-99b3-1d1bc2cade53 | -7.62255 | -43.06314 | 2025-10-07 04:36:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39c21f3d-c197-3062-99d6-cb26baa8b024 | -5.5793 | -43.56884 | 2025-10-07 04:36:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 06e56aa5-687a-3798-b3cf-f2248861cc58 | -8.20542 | -44.18391 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c9ca38c-80a8-333b-ab69-e63ddd4160ab | -7.69245 | -42.39861 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| fec4bf66-f194-386f-9060-436c72e6af91 | -6.64923 | -41.97638 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e2b9180-de5c-3a37-ba2d-3466dedde023 | -5.38956 | -40.99427 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| c01c0de2-1146-327b-9a68-221c44fb915d | -10.1576 | -45.42095 | 2025-10-07 04:36:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8eb32fa4-8fe4-35a9-b003-5de885cb881d | -10.23233 | -48.19175 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a4d62a4-7102-3fb1-9a72-7700d5878f17 | -8.85507 | -46.08875 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6fddd6a8-7d53-3309-90a0-544e13176521 | -8.6173 | -54.96961 | 2025-10-07 04:36:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 51d5e30b-2ed0-3098-ae97-b249d37c1070 | -8.55049 | -46.2491 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b0f705b-b4c7-30fb-8069-23b61c1412aa | -8.5372 | -46.24311 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b55ab9d9-dd7b-34d3-a0df-f6b8fc17ccb7 | -8.69535 | -48.4398 | 2025-10-07 04:36:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26ec56ab-014c-303a-b544-9a4d9d8c2192 | -10.03883 | -48.28434 | 2025-10-07 04:36:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3150aa45-4c37-3d78-9fc3-b20c3f5bcc4f | -6.72408 | -42.84081 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d96a972e-6b8e-347e-9c3f-cc406c4ed832 | -8.62021 | -44.94015 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8c0ebbae-d94e-3fb0-a799-ed9c0aff0dae | -6.3178 | -41.61152 | 2025-10-07 04:36:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 11cd5e9e-19e3-3009-8903-ae8d7e4f4b62 | -8.85096 | -46.09218 | 2025-10-07 04:36:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 31d46368-9841-37f5-a5aa-4c407696a8ce | -6.65477 | -41.9687 | 2025-10-07 04:36:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e6f80829-77b8-3d72-82a0-0e64b422f80f | -6.32117 | -38.52302 | 2025-10-07 04:36:00 | NPP-375D | VENHA-VER | RIO GRANDE DO NORTE | Brasil | 2414753 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| b2761864-fc73-3887-9e4d-251f45d700cb | -6.98376 | -42.87483 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 35.2 |
| 1384f7c5-9ac3-3997-b35e-152dd6343bce | -6.69948 | -42.86644 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| c95c0733-2c2f-3157-98e6-30d6fa43dfea | -4.22873 | -47.21009 | 2025-10-07 04:36:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e2dca750-9477-386d-bcf2-078ad2a1e806 | -10.39843 | -45.37574 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bf89e94-ddf2-3389-89f3-3fae436d7e3d | -5.84893 | -42.85089 | 2025-10-07 04:36:00 | NPP-375D | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.3 |
| 42491481-0752-3150-a1e7-f2e4a497e677 | -9.95477 | -43.75294 | 2025-10-07 04:36:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a109b958-46c2-3d59-93dc-3a048ca3f021 | -8.34456 | -49.65778 | 2025-10-07 04:36:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 68cbaedc-f0b4-3de2-9042-20dad5d43b8c | -8.9377 | -49.85712 | 2025-10-07 04:36:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b0a4f3d-eb2e-337d-88ca-c4fb7bdc4bf2 | -10.33797 | -46.94415 | 2025-10-07 04:36:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7623410e-d35b-3e67-b588-ed6218f56193 | -5.59766 | -44.4241 | 2025-10-07 04:36:00 | NPP-375D | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f190c04b-6ab7-3c1e-adf2-2896e8d9190a | -4.48312 | -47.67567 | 2025-10-07 04:36:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b0a8dfc-337d-3fe7-b85c-28d092b617c3 | -8.20611 | -44.1792 | 2025-10-07 04:36:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b2e1ac3d-6e14-3161-9c80-7580c1cb42fb | -6.71537 | -42.84334 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0cd75716-0434-33a6-8c47-54129cf088dc | -6.75372 | -42.23471 | 2025-10-07 04:36:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| e16103d5-8a6c-32cd-9773-5f199f17e229 | -6.65752 | -39.29504 | 2025-10-07 04:36:00 | NPP-375D | CARIÚS | CEARÁ | Brasil | 2303303 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ae67d59f-90d4-3a39-8496-4feb7a433508 | -6.37167 | -46.43128 | 2025-10-07 04:36:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1ccd28c-e798-3549-aed4-fd266ad268a7 | -8.60944 | -44.91171 | 2025-10-07 04:36:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6d341ed0-b756-33ab-9ab7-b7b427664d01 | -8.54701 | -46.24865 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de6eac43-6788-3921-95f7-de327cf0e5e5 | -6.16038 | -44.0878 | 2025-10-07 04:36:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a311f2-3a73-311f-a4dd-4ef2a226e9e8 | -5.33389 | -43.38885 | 2025-10-07 04:36:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0791541c-a106-30bc-8aed-85aa8a85281f | -9.09199 | -47.96152 | 2025-10-07 04:36:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96e0a5dc-e56f-369a-95ab-7afadfe535da | -5.91754 | -44.97124 | 2025-10-07 04:36:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b20d5d9c-be7c-394b-ac46-0013a069fb5c | -7.72137 | -42.40162 | 2025-10-07 04:36:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| fc70e976-5464-31d1-90a3-840378a719f0 | -4.56796 | -55.9583 | 2025-10-07 04:36:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 7b04d673-b6bc-3d58-9aef-827094ac6271 | -10.35899 | -44.98311 | 2025-10-07 04:36:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a92552e9-c007-3a22-8bda-f6048078ab0c | -8.66102 | -46.28118 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b2f04ca1-54c8-3ee3-b78e-1b245f543d22 | -4.68489 | -49.49679 | 2025-10-07 04:36:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7ab2f490-dfec-329f-ab51-3434d658222e | -6.98481 | -42.86754 | 2025-10-07 04:36:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 60548d7c-c12c-3923-8bfa-e6879518f69c | -9.02878 | -50.66398 | 2025-10-07 04:36:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6f7c1e6f-5555-30b9-901a-97aa5fd5b0b2 | -8.48478 | -46.29856 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb6ba858-ad62-3fab-a004-7583fd89fcfc | -8.54815 | -46.2411 | 2025-10-07 04:36:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| f5b7b7a3-8a2d-3b3f-b019-fc486dd412b0 | -8.17913 | -43.35845 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 0d80d511-3d15-3440-9da9-3531785c8839 | -10.25544 | -44.3697 | 2025-10-07 04:36:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 003ad237-67e5-3570-908e-4aa74570c56c | -5.74324 | -44.98447 | 2025-10-07 04:36:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d9cff955-11a8-3521-ab52-6e75c83b8d48 | -7.00864 | -42.789 | 2025-10-07 04:36:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 46b1463c-6f16-3787-a68f-2a76c4b59f2d | -8.17772 | -43.34007 | 2025-10-07 04:36:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |


[Clique aqui para ver as próximas entradas](README51.md)
