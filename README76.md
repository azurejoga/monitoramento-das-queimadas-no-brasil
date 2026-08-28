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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1105fbfe-728e-30d1-80d2-cce9c7ce935f | -13.4194 | -51.3945 | 2026-08-28 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 133.9 |
| b37d85ce-9b75-32fe-9087-f55ce81a7c40 | -14.3182 | -51.7046 | 2026-08-28 13:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 178.7 |
| c2b7f4db-e74f-3050-b9bf-4048999bdaf2 | -11.2493 | -45.0501 | 2026-08-28 13:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 73.3 |
| d8fd3d94-1c3f-337b-8a38-e0948e4cd2da | -13.4132 | -51.7784 | 2026-08-28 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |
| fd62c16b-2653-380d-819d-b227a8942f3c | -11.3476 | -48.3872 | 2026-08-28 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 7e78e6df-7c38-3bf6-ad43-b21a8bc132b1 | -13.4191 | -51.4159 | 2026-08-28 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 193.9 |
| 8769513c-9af6-3014-84d5-22b29918c96a | -10.7596 | -54.0384 | 2026-08-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 93.5 |
| f9131f8f-0e23-3856-8924-dee67423741a | -11.2314 | -54.0164 | 2026-08-28 13:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 8d2100e7-e698-34d7-8e61-81e8541c2196 | -13.3792 | -51.5061 | 2026-08-28 13:40:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 32d53e95-8d9c-38f0-a8ca-fd106d2da176 | -10.7839 | -50.6346 | 2026-08-28 13:40:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 9ddd4ea3-628a-31a5-b437-59fcd1840a0f | -7.603 | -61.3415 | 2026-08-28 13:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 99.0 |
| 3e45ba93-ec12-3c9c-9ccf-4a37e43d28e3 | -14.3182 | -51.7046 | 2026-08-28 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 119.3 |
| 40b1b144-2ebd-3d4d-abbd-2f1b92c7d225 | -10.9556 | -50.5311 | 2026-08-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 168.8 |
| 661f14e7-5a20-33e0-b11e-691544e25380 | -7.6214 | -61.3408 | 2026-08-28 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 149.5 |
| a0b5996b-7280-32fc-8504-5b68cd81ec6f | -10.7596 | -54.0384 | 2026-08-28 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 86.0 |
| c303d195-1d6f-3c15-a1ce-04c19d480604 | -12.2277 | -50.5792 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 99.2 |
| b32915eb-874a-3257-88ab-e2e57ca28621 | -13.432 | -51.7973 | 2026-08-28 13:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.4 |
| f0243d45-332d-38f8-9118-8e3f297452d9 | -13.3258 | -46.9107 | 2026-08-28 13:50:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 94.4 |
| 9a1a1568-0214-349f-b38e-fc6dc87688a1 | -10.937 | -50.5118 | 2026-08-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 2ab329be-b605-3a7d-851c-2f04ebd336ae | -14.5839 | -51.9677 | 2026-08-28 13:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| fcb1a56e-7d1d-32a0-8e2b-a5d8d0738491 | -12.3038 | -50.5915 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 119.9 |
| 49f42553-f590-3ee0-a602-d9b0129e974e | -6.6048 | -55.4536 | 2026-08-28 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 221.6 |
| a599e046-9cac-3d9e-828a-75413bd16715 | -14.9791 | -52.5951 | 2026-08-28 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 96.6 |
| 61038118-567e-34fe-8a24-e8993af6b38f | -10.4981 | -64.5005 | 2026-08-28 13:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 3919c266-750a-3dd9-8707-41786cdd7b66 | -11.6773 | -50.4724 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 404bc141-1c38-31ee-813a-1c6e9e35c0b5 | -10.7598 | -54.0179 | 2026-08-28 13:50:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.9 |
| 68977b53-fd17-38ed-8f29-e15328e00e76 | -14.1784 | -48.7703 | 2026-08-28 13:50:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.5 |
| 51562309-8819-30f9-bf7d-1f6379830964 | -12.2281 | -50.5578 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 186.3 |
| 831d2cd2-1f6e-3306-86f6-dcf9c3973596 | -7.5846 | -61.3232 | 2026-08-28 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 54.8 |
| 4e392248-0841-351e-bba3-1a9c2ed8c470 | -6.605 | -55.4337 | 2026-08-28 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f17fe0f9-4fdd-342c-910e-351e40653fa4 | -13.4194 | -51.3945 | 2026-08-28 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 363.6 |
| 9de4364d-0fdf-324c-9b84-ce7088bb8787 | -6.5863 | -55.4546 | 2026-08-28 13:50:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| dc4143b4-b2e7-36c8-a68d-ab0e09900ffb | -7.603 | -61.3415 | 2026-08-28 13:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 128771f0-d7e9-3350-a5a9-6940a4d41277 | -14.9985 | -52.5925 | 2026-08-28 13:50:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 125.5 |
| daca2377-c6f3-32d5-b623-5b92a1d05061 | -12.209 | -50.5601 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 3b3f5fba-3b00-30e5-845b-2cc996afa745 | -11.8239 | -47.2178 | 2026-08-28 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 129.2 |
| 16d2f7e6-cddf-3dea-bce3-1e135aa2dbd2 | -10.498 | -64.5193 | 2026-08-28 13:50:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 09463cc4-7242-33c1-9484-2c3c3a8b64ea | -8.9478 | -62.4084 | 2026-08-28 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 82.5 |
| a0716189-084f-3103-929b-f815c3832be5 | -11.6586 | -50.4532 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 115.3 |
| 787e30f6-fee1-37bc-8b8e-8406101f0155 | -11.843 | -47.2152 | 2026-08-28 13:50:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 683173a5-fa69-3e6c-8752-df84a68a29ed | -6.1472 | -57.7995 | 2026-08-28 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| f39bd463-9469-30e3-a40a-535894282e53 | -6.2693 | -53.1322 | 2026-08-28 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 146.7 |
| 5ec8f6a4-dcc6-3be3-942d-6581d2238871 | -9.9708 | -53.9419 | 2026-08-28 13:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 176.5 |
| 439014bc-ae9d-3553-8070-c4437f8b6f6f | -7.3663 | -55.1734 | 2026-08-28 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| d3366807-b1d0-3c4c-bde1-1cf5815ca433 | -13.4191 | -51.4159 | 2026-08-28 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 415.8 |
| c8f8f8ef-60ce-3c9c-a8d0-ea37e6168ece | -13.4128 | -51.7997 | 2026-08-28 13:50:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 20fd4313-8aee-34e4-8564-6f647cd253d3 | -6.2692 | -53.1526 | 2026-08-28 13:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 129.3 |
| cbee118d-2257-3294-b4f1-83801c2fee12 | -6.1656 | -57.7988 | 2026-08-28 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 173.6 |
| 160dbaf0-9f74-3e3e-a129-ea4aaa771c35 | -11.006 | -49.6461 | 2026-08-28 13:50:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| b2ecee4c-f595-3c5b-baf2-03a033ad6cc3 | -8.948 | -62.3894 | 2026-08-28 13:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 20e2c510-6aad-3d26-bf2e-7d46d59b4a55 | -12.2854 | -50.5509 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| e3d4de44-525a-3673-a9fe-24f15cb7e240 | -12.0733 | -47.1614 | 2026-08-28 13:50:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 17eaf081-1e67-3298-95e2-cc7b9ee5a758 | -8.5969 | -54.7755 | 2026-08-28 13:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 101.8 |
| c11eb84b-030d-3bd8-9658-a4bb0c9889f0 | -10.8028 | -50.6326 | 2026-08-28 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 162.4 |
| bb0d8354-1ea8-3479-86e2-782ff55df3fd | -12.285 | -50.5724 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 91.4 |
| 8b5d5afa-ed8e-3869-8510-37740a602e71 | -10.9367 | -50.5332 | 2026-08-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 60586c30-797a-369b-8622-e7b17edad509 | -11.2493 | -45.0501 | 2026-08-28 13:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 75.0 |
| c9e9ce2f-b7ff-3854-8c29-1845e62b30e5 | -6.1657 | -57.7793 | 2026-08-28 13:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 152.7 |
| 705903ce-ab72-39dc-9e74-dd8e5c698efd | -10.7839 | -50.6346 | 2026-08-28 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 154.9 |
| af98e3ef-1190-3401-be8b-4c9eb8e0f1e7 | -11.3476 | -48.3872 | 2026-08-28 13:50:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 1a4b397b-fb52-303d-a2af-3825a658b6bb | -10.8025 | -50.6539 | 2026-08-28 13:50:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 10cfe342-47c4-3fc4-b2ee-39ebce22c84a | -10.9589 | -50.2958 | 2026-08-28 13:50:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 201505d5-1aab-3767-921d-e5c2d2060789 | -12.3041 | -50.5701 | 2026-08-28 13:50:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 201.3 |
| 6741d5b2-d375-3597-b23a-48d48814085d | -13.3597 | -51.5299 | 2026-08-28 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| cd172ad9-c18b-3acd-9c7c-a7dd6ccb276d | -11.2493 | -45.0501 | 2026-08-28 14:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 80.7 |
| 4a106aed-1e23-3846-86fc-f195d483e673 | -6.605 | -55.4337 | 2026-08-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 165.9 |
| ba2ad9be-ed9b-300d-b829-3b5e5a1fc8fa | -7.5846 | -61.3232 | 2026-08-28 14:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 0d9b18ea-e3ca-3551-86cc-f784d1483dfe | -14.2302 | -45.2472 | 2026-08-28 14:00:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 6dd83b1b-2a3b-35e4-bc0e-b211dbeab12c | -13.3258 | -46.9107 | 2026-08-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 15c870b3-2b03-3837-922f-8e9804a00ee4 | -7.0289 | -55.6909 | 2026-08-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| f49de809-4a2c-3f7e-b779-09158bcf4f49 | -6.5322 | -55.2577 | 2026-08-28 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.5 |
| 91c5c03c-f072-37e8-adc9-fcf1795e7523 | -6.857 | -59.4371 | 2026-08-28 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 77b0b131-aa2d-39a3-9e73-b57e9a120bc9 | -12.2277 | -50.5792 | 2026-08-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 21fc7ffb-25b0-32ce-ae7c-93bf4c832d86 | -13.4194 | -51.3945 | 2026-08-28 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 434.0 |
| 1688444a-2833-30c2-98df-3af7687b8b3f | -14.1784 | -48.7703 | 2026-08-28 14:00:00 | GOES-19 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| e0f47aec-f0b3-391d-aa37-6709aa439daf | -14.3182 | -51.7046 | 2026-08-28 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.5 |
| ec2c4853-6a01-3865-9a55-721bb19fd337 | -13.3254 | -46.9333 | 2026-08-28 14:00:00 | GOES-19 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 857877c1-f35d-3a78-ba2b-4123d9efda41 | -6.2692 | -53.1526 | 2026-08-28 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| 6a29b9cf-321c-3409-889c-1e2ae5bc867b | -6.5865 | -55.4346 | 2026-08-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 104.3 |
| eee4912a-5327-3806-a0ea-8d250ac01d71 | -14.5839 | -51.9677 | 2026-08-28 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 123.0 |
| fc2fff45-2978-3bb4-a0fb-7271bb36888e | -11.2109 | -51.2476 | 2026-08-28 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 79.2 |
| d1761425-bc94-3922-95fc-7a9675ffc14e | -13.3988 | -51.4824 | 2026-08-28 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 80.2 |
| fa27b6e6-a23f-3879-ab50-0e378099818b | -7.0287 | -55.7109 | 2026-08-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 111.2 |
| 7f127420-1371-389f-97d6-155132cef821 | -13.3985 | -51.5037 | 2026-08-28 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 5d6bb2bb-a548-3399-8a70-b1bb7feb2c01 | -13.8378 | -54.0573 | 2026-08-28 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 87b11958-dab6-3f0f-91e2-62b69ad930c2 | -14.9209 | -52.6029 | 2026-08-28 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 105.0 |
| bcd8b142-1f4c-37cd-b3b9-c78d632d14d0 | -10.7596 | -54.0384 | 2026-08-28 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 95b92e9b-bdaa-3437-8e4f-8f93feb41c3b | -8.9478 | -62.4084 | 2026-08-28 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 117.2 |
| 2d410d7d-c167-3be6-b7a4-16baa938e6a3 | -14.9985 | -52.5925 | 2026-08-28 14:00:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 062946b9-cf08-33fe-a412-35d6be8cb2de | -9.2282 | -51.5428 | 2026-08-28 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 08d279ca-dcdf-3279-8232-c6c7e8555b41 | -10.937 | -50.5118 | 2026-08-28 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 0e580430-939e-3a9f-a200-3d9cdb08c639 | -11.843 | -47.2152 | 2026-08-28 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| a9e1298a-b055-3f5e-bd4f-de670903a536 | -12.209 | -50.5601 | 2026-08-28 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 317381e0-9300-3dba-9892-cd1820a7ae16 | -10.559 | -50.4876 | 2026-08-28 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 5abd200b-805e-3438-9a27-0f807fdb3817 | -6.5863 | -55.4546 | 2026-08-28 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 207.0 |
| c3c6bdcf-26e2-30af-8c69-2386aee8c4a2 | -14.9981 | -52.6138 | 2026-08-28 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 3887a922-7312-3ee3-a497-54b875dc9a41 | -12.0733 | -47.1614 | 2026-08-28 14:00:00 | GOES-19 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| c558cab3-0493-3a94-9f03-2b99a8051b0a | -11.3476 | -48.3872 | 2026-08-28 14:00:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 7f3190b7-7885-3a09-9e48-0921aa20ee65 | -10.8028 | -50.6326 | 2026-08-28 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 8f02e31b-69d0-3cce-a5e8-cf997f3fe943 | -10.498 | -64.5193 | 2026-08-28 14:00:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 68.5 |


[Clique aqui para ver as próximas entradas](README77.md)
