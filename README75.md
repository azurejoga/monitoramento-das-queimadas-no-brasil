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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 519a0399-776c-308f-a7a7-1af8ffb5c7b1 | -11.85724 | -52.42789 | 2025-09-04 04:55:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3f68c19f-23c6-3ec4-b0d3-7c87b331057b | -10.06712 | -54.79069 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5db2720a-9860-34e3-8817-bfa6b4c33eb3 | -12.6273 | -56.9892 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27a77e12-a09a-3b2b-8f97-dceae1572e91 | -17.04495 | -47.14221 | 2025-09-04 04:55:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5295498a-f629-3320-b874-15255a827959 | -11.59055 | -52.16499 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f5e8d99a-97fe-3825-bc5d-a2fe66899b94 | -11.67915 | -57.35271 | 2025-09-04 04:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d47e64b5-b361-3c90-a9ae-8e49bde3b005 | -12.89012 | -48.08401 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e6e276b-755b-30b7-ba8c-fef5356f2c4d | -12.91537 | -57.00277 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6f431682-709f-32e5-bc22-aacceb9f0a1a | -15.56481 | -48.39954 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 38fd0fbd-52a3-3de7-8f66-4880a7b6a435 | -15.04078 | -48.10665 | 2025-09-04 04:55:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a78e5d5-1f0f-3c0b-89e3-70102f8dc5e3 | -12.49616 | -53.84145 | 2025-09-04 04:55:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3eae588e-2d7e-3fde-8db0-731f74bfe319 | -12.97192 | -54.78249 | 2025-09-04 04:55:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32d19830-7b1d-3a64-838c-ce315ef3a221 | -10.48495 | -53.64242 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fd305b3f-9fcd-308c-9a05-22935968d686 | -14.38994 | -53.07589 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f7e8841-18d4-30d0-b2b0-42cb895ae6f2 | -12.50459 | -48.05558 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 91519024-6268-3880-a341-713c5c9336ef | -11.85105 | -51.49492 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f4ba7ab-59ff-3566-be90-3e87177c9495 | -16.53684 | -55.08966 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9f8fd55d-9e00-319b-a5e7-f2403ee62b5d | -15.19761 | -52.35781 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dc3a617-8c59-3e3c-a464-891ca22ec084 | -12.86778 | -48.02125 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c96d430c-32ca-3dc5-a2da-bc6fb003eeff | -14.55191 | -53.06725 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1e45a04-2e7d-38f4-b259-e5d18a2c9b9c | -11.85512 | -51.49153 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0dfda0ef-6909-3f19-af91-3f3d1d7ba8d7 | -12.90362 | -56.94091 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| a11c1736-38ff-3ce7-95bb-e5464a713013 | -15.03381 | -50.076 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6e35aa4b-cda5-3a8f-9b86-31a5333037cc | -11.63425 | -52.19767 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| be2b85d0-80d4-3aa0-80a0-a8c19ea27101 | -10.87527 | -55.76251 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 25225439-1e6f-3246-923f-b5ef8113c793 | -10.49049 | -53.65051 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 994f03ac-052b-3bc5-821f-71779c79065b | -11.58086 | -52.11423 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 55f23b8b-a4a0-3231-9954-8f011c3ecb72 | -14.82243 | -48.21039 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| aa7b9234-703c-330f-bc70-7823a361e865 | -13.7112 | -46.91612 | 2025-09-04 04:55:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82f9a1c1-04dc-3388-b7cc-704d519de04a | -17.17641 | -46.25278 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 63849ba8-a217-302d-ad92-945c55f4ba0c | -10.58207 | -55.42123 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a13f5f32-8ffa-30de-bee2-9969486668d2 | -12.905 | -56.93262 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 95198162-5c15-385c-844d-bc9066730d34 | -15.00339 | -50.06664 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e82cacf5-5ae9-371a-bed2-c50f2ecbd05e | -12.91589 | -57.01055 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7206bb10-7d55-395e-a18e-e27a578fb597 | -15.0299 | -50.07563 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 07e68f42-523a-32ca-af35-90613d6f3a60 | -15.00353 | -50.03672 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 08faed4e-1514-3cc9-b7c9-dcf5625f9e88 | -17.73182 | -46.17071 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 45e9a015-c257-3d29-abf7-79039c814b32 | -10.09156 | -54.76852 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df646171-9fde-36bf-bf3f-7dbca02706b9 | -14.55982 | -48.04075 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 58d5d6a8-2b19-3117-a00e-a84fdec1fae5 | -15.16827 | -52.35407 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 268f716b-1c61-3fee-be19-73fd9980f204 | -11.87952 | -51.5432 | 2025-09-04 04:55:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba905330-9637-3aed-911a-e34b7d5022df | -17.61278 | -46.6459 | 2025-09-04 04:55:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 1e42b9af-e8f8-3719-9847-726723efd6b3 | -17.15583 | -46.25017 | 2025-09-04 04:55:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4275fd51-505f-31cc-b91a-f1aaf85de5f1 | -8.70263 | -62.39852 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c636056d-9774-3068-bad7-5955218f7f12 | -13.10256 | -57.11454 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 811816c9-f7c9-30c5-861b-bbe2d401f55e | -13.44489 | -46.9416 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0baae083-9818-3c06-8e29-0affa4d055e1 | -15.98492 | -55.9565 | 2025-09-04 04:55:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 49b58965-62cc-3a80-912c-2772f00e33ec | -10.47388 | -53.62622 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a43b6ab-da8a-3880-ab26-421f78f561e6 | -15.30351 | -52.74958 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6fdd7749-d1f3-3fbf-9deb-68b29fd507fa | -12.94956 | -48.06446 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7ff7b316-d349-3ef1-b19b-0d1c52e36e32 | -10.52623 | -57.77512 | 2025-09-04 04:55:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 62f489bd-9fc2-318d-8dd5-f5056d7afd69 | -10.09891 | -54.76602 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c02828d-9cbf-36f5-b5c6-6cbbad6cc04b | -14.5928 | -52.19133 | 2025-09-04 04:55:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1070e706-a964-3ddc-8ae4-412dc3062241 | -15.02689 | -50.04012 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 17e0be83-5a78-34ea-9232-ae70b8203006 | -11.60378 | -47.77807 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f4762877-7ef0-3f92-a1dc-d2950bb6dcf8 | -11.07856 | -52.00005 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b6909e1-b7e6-3320-858d-45de929f0eda | -12.5035 | -48.06359 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 58e46d50-6aec-3e1e-921d-3110e1bc8d9e | -11.2078 | -55.05866 | 2025-09-04 04:55:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb893cd7-5c7c-30e8-8c36-5ef1f592e205 | -12.23621 | -50.15571 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b9160e1d-17c5-3af1-9ef9-906bbe959c32 | -10.50211 | -50.44806 | 2025-09-04 04:55:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bdbaadcc-2f0b-3438-974f-cbd8f54041f7 | -11.88716 | -50.60755 | 2025-09-04 04:55:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e400b9b0-46dc-39f6-9e65-7f5998ad8b4c | -11.20143 | -55.01257 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eea2ef86-e107-37f2-9a9c-5ba1c9d67011 | -11.73422 | -47.75117 | 2025-09-04 04:55:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8fdb3af4-e9f2-3532-983e-db5db16fd76a | -14.58934 | -48.02102 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c7460771-6081-322f-a946-b67db8f229b1 | -12.88507 | -48.02304 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f3afceb4-07b7-3712-be97-5d23c6779b0b | -10.10068 | -54.75512 | 2025-09-04 04:55:00 | NPP-375D | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b71eca73-429a-30e4-8c58-52c84a1dcedf | -15.53663 | -48.34232 | 2025-09-04 04:55:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 57f98efb-ccea-3623-aa03-be1d4b05cec0 | -10.99082 | -49.75092 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0d6bb37f-591a-3dce-9960-39c8d4201643 | -11.08876 | -52.04719 | 2025-09-04 04:55:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 68452849-aa4d-3a62-b113-59addc6a2c5a | -14.56416 | -48.04182 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e880c4ed-c6ba-3b4d-a649-cf9947623242 | -15.03855 | -50.04198 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79544748-1233-39c9-b894-f2fff03027d2 | -10.61265 | -55.40706 | 2025-09-04 04:55:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd84741a-25f7-3bd9-a9aa-34e4c69b6511 | -10.98596 | -49.73151 | 2025-09-04 04:55:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dab51e9b-ad78-31cf-b8da-2b29babf98e2 | -12.88655 | -56.95501 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 66385147-b387-33f9-a26d-7c1f4d30eefe | -11.58401 | -47.76275 | 2025-09-04 04:55:00 | NPP-375D | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78626796-c145-39f7-911e-7ca25d2cc13d | -13.44029 | -46.94049 | 2025-09-04 04:55:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 80aa220d-aae6-36a1-9b1a-60a000f7b9de | -11.59508 | -52.15814 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07dfebf1-4bf2-324a-a0ca-0758406845ea | -10.78785 | -52.76303 | 2025-09-04 04:55:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86550b45-e6da-3da2-8a6d-601380ff2d4d | -11.85622 | -51.4357 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3a7200e-30cc-3937-ac19-b52a293e183d | -16.30984 | -52.9601 | 2025-09-04 04:55:00 | NPP-375D | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 47e82c46-fd77-3fd9-83da-f1077145ccf8 | -10.44838 | -53.61492 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 870b9d86-6d32-396e-9506-4cfcf58fbdc7 | -12.48974 | -48.06883 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7b055d3d-a135-3f53-8aad-df7d954b2c9c | -15.15377 | -52.3797 | 2025-09-04 04:55:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d022e807-7f15-3b0f-90cc-c64b6c2e7e98 | -11.58823 | -52.1116 | 2025-09-04 04:55:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d6db3e2-87ba-388f-8c51-57853dd297da | -13.49179 | -51.80235 | 2025-09-04 04:55:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bbfb386e-2b8a-3140-bf3c-651ab464311a | -14.37866 | -53.12696 | 2025-09-04 04:55:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dbc2296-9afc-3810-a25f-c38e85b46f51 | -12.47099 | -48.07899 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 10f9a4de-736a-3cfa-97b8-85f221e1b509 | -15.01371 | -50.07804 | 2025-09-04 04:55:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc5b617e-3eb4-34de-b241-24ea07789586 | -11.19288 | -55.02237 | 2025-09-04 04:55:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| abed0399-922d-384b-9e2f-000e97b0bb83 | -11.78224 | -47.3272 | 2025-09-04 04:55:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| abe621b4-7c20-3355-aa15-2bcce10d8479 | -15.87815 | -56.89246 | 2025-09-04 04:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6878ae6a-4333-3f8f-9f29-427c99279ac9 | -10.87217 | -55.73827 | 2025-09-04 04:55:00 | NPP-375D | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d72ab954-e14b-3807-a39a-3eca1cb87c24 | -10.44727 | -53.62193 | 2025-09-04 04:55:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 495bb77a-437b-3f03-8ccc-c03d8760db51 | -8.70665 | -62.39531 | 2025-09-04 04:55:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 88144b01-8041-3d20-9202-14f2b94efc47 | -10.06851 | -58.3903 | 2025-09-04 04:55:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9b4ce71-fbe6-3505-97b1-4ecec5e444ae | -14.59858 | -48.01052 | 2025-09-04 04:55:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ba8f4ad5-8cff-3794-a120-43f2d49678d4 | -12.95386 | -48.06502 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e04ebefd-c16b-364d-a7fe-905022877ab2 | -13.10186 | -57.11872 | 2025-09-04 04:55:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c42b83af-8895-3559-84de-ab1bfade7f32 | -11.86961 | -51.46601 | 2025-09-04 04:55:00 | NPP-375D | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 554837fe-d7cf-35d1-8094-216e9054e864 | -12.88076 | -48.02246 | 2025-09-04 04:55:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |


[Clique aqui para ver as próximas entradas](README76.md)
