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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a7a228dc-3204-37f9-b89b-0b977842f164 | -2.94028 | -53.28305 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 82beb930-f139-30ee-8ecc-284dab84ddc8 | -2.19091 | -53.82983 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed96f8d8-d50c-3184-9df2-c1d887aff83e | -3.04881 | -48.41809 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d6a839f2-9ca2-320b-a44f-2ea8baae15ea | -2.70126 | -49.30879 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2540964-800a-32bd-95cc-b0109b865ef1 | -2.70549 | -49.30943 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f9300dab-8bd7-3c07-9503-93d3f1ac5e2c | -1.41186 | -55.26811 | 2025-12-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0dcd4dff-f3ca-342e-88f5-f40de6d7a697 | -2.84184 | -51.06277 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c598a179-28b0-3bb9-94eb-689040b6e5af | -2.62133 | -45.14197 | 2025-12-03 05:08:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9dd4eabc-cc60-3815-9929-1985de11cd49 | -3.24103 | -45.54598 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 3a140d60-f8cd-3078-8010-fdfaafe63843 | -2.35809 | -50.10623 | 2025-12-03 05:08:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 1c3c6228-145e-3aad-acb9-036ded442b4a | -2.57213 | -46.88589 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6472a569-7648-358c-9cc1-ae7d6e63065f | -3.77187 | -50.13665 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5bcd4891-fa70-3158-b0e3-74e771738b96 | -3.2225 | -46.86561 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4993300-0070-34a9-b827-9be7610510bb | -2.57303 | -49.09921 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 183d2868-80dc-383c-b875-ddb907ef7395 | -3.84651 | -47.05947 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 555543f7-3e25-32ad-9b36-b98d3c51abbb | -1.43776 | -55.19064 | 2025-12-03 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 19b79054-aa58-31f0-a475-5ce17aa16d12 | -3.24763 | -45.53959 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87448872-83ea-327e-855f-6f6581766341 | -1.98561 | -46.47694 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19f5feaa-ac58-3cce-850d-a0c878d4b4b0 | -1.05834 | -53.10114 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60d2e676-e534-3b4f-94f7-92370114cca2 | -2.83322 | -50.4677 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 105fc82b-7c97-34f8-8be8-d66433a68ba4 | -3.15045 | -50.56332 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 189307f5-e33d-3dbf-99dc-b7a27fb968bc | -3.85068 | -47.0661 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 858a0e06-cb71-3869-9101-20e35a5d0d5b | -3.24156 | -45.54238 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b7de68aa-ec56-3b6f-83c8-19905bd7d4ea | -2.60665 | -49.25052 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0e3ef3bc-a5f5-3281-b976-64cdcdff605d | -1.13623 | -53.80327 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fceb14c1-54ca-3e29-9450-c313561386be | -2.99113 | -49.52325 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| f379a5c2-65ff-3277-aacb-5ed773577971 | -2.93515 | -53.27111 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 86bc1855-a014-3b40-8d36-84d5c6015f0b | -1.06519 | -53.60914 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e7941b9-c00c-37fe-bb4e-4f3ae5e548c5 | -2.70488 | -49.31335 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 47344e36-a422-3fb1-8266-848e05e3ed50 | -2.41199 | -48.65034 | 2025-12-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0ccbc78-27ca-362c-80f5-6e2926be39d8 | -3.23602 | -45.5416 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 2acd615a-dc7b-3ee0-9b56-30a2ac3d25c5 | -3.19129 | -41.85345 | 2025-12-03 05:08:00 | NPP-375D | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 6add4a40-7924-3b69-b3db-eb5054d97e56 | -2.60604 | -49.25444 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 39487fac-984f-3d88-8630-ce3d15a7159a | -3.22364 | -46.86502 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 46e8b18a-6961-39b2-a857-00426d1db6e4 | -3.36188 | -46.85402 | 2025-12-03 05:08:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f7df902c-b5e8-3586-bfb7-fc4e2f8d08e7 | -5.9031 | -43.7198 | 2025-12-03 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fbe44a20-294b-31cb-bd46-f01a2dbab033 | -1.9107 | -46.28557 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca9798d0-466e-33e0-a10a-336fa1dbbf16 | -3.22318 | -46.86797 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3931fc19-8d73-3d3e-b308-339e0fa56c62 | -3.67723 | -47.61638 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 89875d1e-c946-386e-a45d-1feceae2c657 | -2.6012 | -49.25768 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 811ac5f8-c10f-35ce-abad-d751062a984b | -5.90334 | -43.71918 | 2025-12-03 05:08:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ff46e14a-412a-3670-ae73-0cc58f0766ff | -4.66688 | -46.30889 | 2025-12-03 05:08:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c2a36e44-543a-3aeb-9327-891ab9d2dbc4 | -1.49768 | -52.03768 | 2025-12-03 05:08:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcfc27e2-e2c3-3941-9df7-e1c08db6dc53 | -2.57298 | -46.88049 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 69130c23-751e-356b-93a8-da3e5d59b5ed | -3.2865 | -50.08217 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0cf68b8c-4ad4-3165-a92d-8d3c2db5bd83 | -3.22207 | -46.86856 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 23015336-001a-3963-b1b6-3cbb646ddfda | -3.96318 | -46.58664 | 2025-12-03 05:08:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b7a1fbd-1e9a-34ec-bd5c-cb09a0db8936 | -3.77594 | -50.13727 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 338b2c3f-0b7e-3e08-8d06-023fe0a6a978 | -2.38281 | -47.69687 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 753ce675-869f-30f2-a254-5951c16d6658 | -2.61843 | -45.13919 | 2025-12-03 05:08:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3656805b-44c7-34ad-b6c6-2b63f4a2141c | -2.83792 | -50.46335 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6f00d6f4-309e-37d5-8a92-da56e808fd79 | -1.90772 | -46.27903 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 160efa36-70a6-307b-911a-c01f7fbd678c | -2.92318 | -48.22795 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e4318271-2d61-3b25-a75a-bd0ad6af4312 | -5.38569 | -46.75723 | 2025-12-03 05:08:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 498ec424-d01f-3afb-8a3b-68273240cfd7 | -2.80117 | -52.90124 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 199ed06c-6d55-3259-88da-176c4554ab99 | -3.53316 | -49.98702 | 2025-12-03 05:08:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 08e13391-6e19-3d8b-b99a-35ca99e6547f | -3.31178 | -42.50704 | 2025-12-03 05:08:00 | NPP-375D | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6749b2d7-a4a1-34a4-86fe-bd07866bf491 | -3.22756 | -46.86639 | 2025-12-03 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 771e872c-1593-33e0-a4bc-e9afb5b17697 | -2.38266 | -49.38842 | 2025-12-03 05:08:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ec386bea-0dc1-3ed6-b620-9f50b71b15ac | -3.25316 | -45.54044 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 16f23803-2483-3c7a-8ddb-c27e2a03d452 | -1.11238 | -53.17962 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c071b541-c0b4-3488-b419-40adeede7531 | -3.60075 | -47.26582 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7588eb36-9096-3a20-a7aa-6f783bd1340f | -3.63499 | -48.89513 | 2025-12-03 05:08:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f5b8565a-c956-3619-9859-8fdf78125142 | -2.73998 | -49.33333 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 42f58fb6-90b9-3002-a449-db422162d33a | -2.93458 | -53.27475 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a036af1d-f36d-36f5-9553-b9d138f55902 | -1.98157 | -46.48192 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3691eb33-f48b-3035-b4c5-403ef4b074ae | -2.63918 | -48.03889 | 2025-12-03 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 482792a3-c4e4-3d03-a4fb-cf713b2e17a2 | -2.20647 | -47.99746 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| bfb61a1a-072e-3303-b5fa-16015ddf1a06 | -2.89245 | -53.29829 | 2025-12-03 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5205d031-939e-32ce-aa72-dba2f8bdd079 | -2.17311 | -48.36994 | 2025-12-03 05:08:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 92458d7d-643a-35a5-aa16-7a042fabbb4c | -2.46484 | -51.25571 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 50526c9d-2c11-37c4-90be-cbbd0808e604 | -2.98334 | -49.51809 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 59fd96fa-4970-35ea-ac97-b39832777961 | -1.8663 | -48.0224 | 2025-12-03 05:08:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff40272c-1d58-3661-8abb-f58feda15797 | -3.85739 | -47.05542 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 68563aac-9b88-3d4c-841a-c46b75f4ef7e | -2.35729 | -50.11136 | 2025-12-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6ce8da2c-853e-3a70-9088-f287deb508c4 | -3.85195 | -47.05743 | 2025-12-03 05:08:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| aeb34a05-df80-385f-b163-a3958a962e51 | -2.09106 | -53.41801 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec8aa25d-b25b-38d9-af4b-8807084338f2 | -1.91196 | -46.28597 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dbcc5996-7575-3f55-baf8-db21036e517d | -2.24629 | -48.31297 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0a8a2ba6-85bb-3764-9a22-01e830ad402e | -2.21036 | -48.00285 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 04c9afc3-076a-3aed-8090-dc9efa20f4ad | -2.60181 | -49.25377 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 71384e92-53fb-3686-a806-298bc3d47ce4 | -2.6006 | -49.26158 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 95d46e27-0c97-3e43-93d3-a3c81fe3af43 | -4.41479 | -47.60139 | 2025-12-03 05:08:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6f941f51-83c4-3c47-8283-359e5464ae83 | -1.06854 | -53.60966 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b73cd0bf-b6c5-3506-9299-d8e29ea6bc2b | -1.30998 | -55.46583 | 2025-12-03 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4c32db67-25fd-3124-a71b-00d205f240b2 | -3.43288 | -49.48079 | 2025-12-03 05:08:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d19da8fd-8975-32c3-b354-148eaa97cae4 | -1.93233 | -52.11737 | 2025-12-03 05:08:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a153add0-f424-3097-af86-b67e6b03fec9 | -2.62712 | -48.05629 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dfde4eb5-4483-3208-80ca-7c55f4a364bb | -3.2471 | -45.54319 | 2025-12-03 05:08:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e011360e-442a-3f32-9b76-eaa7a3d1a678 | -1.15409 | -53.88459 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 57d2c16b-4098-3c7f-93b0-94c3e534e4b0 | -3.2451 | -50.16298 | 2025-12-03 05:08:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| efe78c42-95ac-3a0c-b585-9f9b3819fe4d | -2.15261 | -53.53718 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 177f5101-54ea-3f11-83d4-4a01ddd7f31b | -2.98753 | -49.51877 | 2025-12-03 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3017163e-5be9-33a3-94e6-726bb993ae8e | -8.04632 | -43.09658 | 2025-12-03 05:08:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 50b26fd2-e100-3fed-bf55-480437e7fd22 | -1.29066 | -53.18076 | 2025-12-03 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f015e586-ca5e-38f1-8de3-8a345ec15b05 | -3.60189 | -47.26699 | 2025-12-03 05:08:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d3730cc2-7a77-378c-afca-a0817c119fd6 | -3.0436 | -48.42192 | 2025-12-03 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 86b3a047-9356-3c28-b893-d08b43c0e0a1 | -1.93932 | -50.33251 | 2025-12-03 05:08:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8954a899-af7a-37df-8ca1-8847f701d7fe | -2.66052 | -54.08955 | 2025-12-03 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acda09e6-1024-37bb-945c-f411a1f1c8d1 | -1.98204 | -46.47891 | 2025-12-03 05:08:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README18.md)
