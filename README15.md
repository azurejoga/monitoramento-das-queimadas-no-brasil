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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c756aeb-9412-3341-9add-fcc3ca3b471f | -22.77786 | -49.32133 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1c7a4a83-e204-3460-b78f-fdd07fff40e1 | -11.91633 | -54.82376 | 2025-06-18 04:19:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 81bf50f6-4b9a-3311-9e35-a2e33d6e1428 | -14.19659 | -45.51816 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5012684a-7014-3c76-a72e-7b621a1377bb | -15.67041 | -43.59235 | 2025-06-18 04:19:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a04fdd05-6ae3-3343-be92-ae197e631a4c | -22.7774 | -49.31859 | 2025-06-18 04:19:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 18ab841f-c04f-38c8-b3c2-ec35f0ba558a | -12.65345 | -54.12884 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c08759d9-0f7b-33f6-9858-4fa4d7d8c65e | -20.37782 | -45.60347 | 2025-06-18 04:19:00 | NPP-375D | PAINS | MINAS GERAIS | Brasil | 3146503 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7df7bc96-0093-3ea4-a8ac-1f0741cfce95 | -14.4347 | -48.9133 | 2025-06-18 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 1e482e77-905f-37e7-b5ed-faa7ce559aeb | -12.57933 | -56.98629 | 2025-06-18 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a797626e-6136-3793-9700-dbe49de0e0d1 | -13.17927 | -48.36388 | 2025-06-18 04:19:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 099bcb19-0064-3c48-b589-194658f64c7b | -21.19534 | -44.9388 | 2025-06-18 04:19:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 22411a48-1645-3093-9da2-fa3f534c3c31 | -12.52815 | -57.77806 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e0bd0dc3-36d9-34eb-b7d5-2299befa8299 | -22.67468 | -42.85791 | 2025-06-18 04:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 0800155d-0dac-3e3f-bc8b-5bb8e7d37c8f | -22.67588 | -42.85556 | 2025-06-18 04:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 360a7b34-f251-32cf-ad43-a1ec14f90691 | -14.02833 | -55.12926 | 2025-06-18 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb287e97-5469-3dde-bc17-091aceaf3e3f | -12.71926 | -54.97096 | 2025-06-18 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64a8c202-5563-3513-a862-115b384531ec | -20.92399 | -49.09554 | 2025-06-18 04:19:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 9bab0802-9df6-38cb-9c41-de011e95e216 | -15.40242 | -47.82845 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69e37a1f-8531-35fa-a6b2-216179cf6a5f | -22.67909 | -42.85357 | 2025-06-18 04:19:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fa4ed69b-5196-3ea2-8709-b7736391b4be | -12.64339 | -54.12288 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b8b61fa-0cf5-384b-82eb-5c259a828783 | -14.19499 | -45.50686 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 13ed284b-77ea-3b5b-a265-1e143575c581 | -20.99568 | -47.39288 | 2025-06-18 04:19:00 | NPP-375D | ALTINÓPOLIS | SÃO PAULO | Brasil | 3501004 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 97ecff28-c80e-3daf-b4b9-475ed25b051b | -21.02452 | -42.83527 | 2025-06-18 04:19:00 | NPP-375D | VISCONDE DO RIO BRANCO | MINAS GERAIS | Brasil | 3172004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| eb2e54a4-2d81-3327-8ed2-f675bb8453c7 | -12.49818 | -55.74155 | 2025-06-18 04:19:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 8cfc0cbb-d7b1-3698-a88f-449ffd3ea5be | -11.95792 | -58.73867 | 2025-06-18 04:19:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7094e040-7ac6-3851-a710-5fb28439385f | -15.40593 | -47.82912 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fedb3aff-f301-3d67-9980-39d3d5711ca0 | -19.89929 | -49.35077 | 2025-06-18 04:19:00 | NPP-375D | ITAPAGIPE | MINAS GERAIS | Brasil | 3133402 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 7caed336-84b5-3e5c-9be7-d32367221c04 | -14.19384 | -45.51402 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f786042d-ccf0-3add-8fae-4d475be22f92 | -21.64488 | -44.22989 | 2025-06-18 04:19:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2a6bc165-05d7-3463-81a7-a5085c1e18c1 | -12.64877 | -54.12407 | 2025-06-18 04:19:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 873f4798-b0c8-3bfa-9273-f50f16b9326c | -12.5248 | -57.21657 | 2025-06-18 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 66d31284-40b2-3123-b87b-e370c569c0a4 | -12.52941 | -57.77208 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5f812c2e-e9ab-3a98-a381-88de12e84d4b | -11.6164 | -58.29353 | 2025-06-18 04:19:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9adfd4c9-f2fb-3c8d-b5c8-d33166407946 | -14.02347 | -55.12438 | 2025-06-18 04:19:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 93b6c5ed-ac76-3f25-9b47-a75e64f3d31d | -20.23055 | -46.74232 | 2025-06-18 04:19:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f079973-dff7-33aa-9634-1773e78fc2ce | -21.66725 | -41.94636 | 2025-06-18 04:19:00 | NPP-375D | ITAOCARA | RIO DE JANEIRO | Brasil | 3302106 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 2aa6b8a2-a3db-32fd-b168-07a784236afc | -15.40808 | -47.83788 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 916a4a00-a53b-3e48-839d-1f8734f3ea76 | -15.40173 | -47.83255 | 2025-06-18 04:19:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b1b16e6a-2c5b-3da4-b172-8e5540dc0649 | -14.19717 | -45.51457 | 2025-06-18 04:19:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5b806fa6-d11b-3ecd-b78d-3f24a6d78191 | -14.64717 | -48.05588 | 2025-06-18 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 836037e4-3b17-3d3d-bb8e-41dea48a55a1 | -15.62471 | -46.46685 | 2025-06-18 04:19:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f84c5a01-1f22-337a-acc4-44f23a2859ff | -11.1382 | -53.9223 | 2025-06-18 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 109.2 |
| 8bab100c-c18f-353b-a6b7-c605c6c95474 | -11.1379 | -53.9429 | 2025-06-18 04:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 136.8 |
| 0f467ea5-fed1-30af-b8f2-399f110bfae2 | -11.1379 | -53.9429 | 2025-06-18 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| 913d860c-e44c-3374-9e0b-b1ab034e58ad | -11.1382 | -53.9223 | 2025-06-18 04:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 30a4b132-f453-3de3-ba9b-0300c127450f | -4.54959 | -48.00889 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cbfa5ef8-4433-32db-a5ee-c4458692be47 | -3.54148 | -42.43816 | 2025-06-18 04:36:00 | NOAA-20 | JOCA MARQUES | PIAUÍ | Brasil | 2205458 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 89928aa6-392d-30ce-a970-7c33b103a62c | -4.5485 | -48.01591 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 34b8c4ad-d5d3-3a1b-83c8-cda59c70e9ca | -4.24868 | -47.58541 | 2025-06-18 04:36:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0e0fdac6-5c5a-3ec6-8443-9bbd747e89e8 | -4.38379 | -48.06929 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98ac2023-a92a-3052-a497-f79b761e20d5 | -3.22299 | -54.86774 | 2025-06-18 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb633a29-ec82-33fb-b705-8be8ee159e3d | -4.55293 | -48.00941 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e83bdae-c7b3-3e08-ae7d-22a5bce39145 | -5.061 | -43.24866 | 2025-06-18 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2de49383-91b2-39e4-8599-b9e6eb9335e4 | -4.82064 | -44.35688 | 2025-06-18 04:36:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 687ae248-20ca-3213-951c-19ae645c6005 | -2.90273 | -54.48964 | 2025-06-18 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1049e166-dcad-38e8-8572-aa2cfc49037d | -4.37937 | -48.07576 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b4513514-2bbb-38a1-a39f-82b878f76ff2 | -3.2193 | -54.86302 | 2025-06-18 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49e5bc70-1875-3fc2-ac87-5c056953190d | -4.82185 | -44.35516 | 2025-06-18 04:36:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 12903fe9-aada-38e0-ad94-111c8a1c8ac1 | -4.38325 | -48.07279 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eec29fdc-d4d0-32f5-b0a3-5cefd9b983d0 | -4.54795 | -48.01942 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 39759d8d-5761-3571-a2f3-ab3bca3055ea | -4.54904 | -48.01241 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 36ec486f-f79a-3da0-9666-7a12c1ff0504 | -4.55626 | -48.00993 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4e1b1e33-55c3-30ae-a0b4-caf107783900 | -3.22364 | -54.86372 | 2025-06-18 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5e69c77-b169-3372-b500-dc95dba2f852 | -4.55348 | -48.0059 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 8a571934-b4fc-33d2-ac7a-2aeb3ea7869e | -4.2813 | -48.18166 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ca2ad43-5ee8-31a2-af03-cd5317fca40a | -4.81791 | -44.35455 | 2025-06-18 04:36:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 18db6a0d-cff9-378c-a4b9-38be10db3d4e | -5.05733 | -43.24408 | 2025-06-18 04:36:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 64525bbf-4fca-3544-b5cf-80948990b00a | -5.07185 | -43.72646 | 2025-06-18 04:36:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38ecfff7-a9d4-3de8-b021-26e78443e589 | -4.37992 | -48.07227 | 2025-06-18 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb629354-c64a-372b-8ddc-0ad1fb6da35a | -3.21864 | -54.86703 | 2025-06-18 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 73877fdb-864f-34a7-896f-5d73c7c0e377 | -8.3079 | -55.10667 | 2025-06-18 04:38:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1680ef51-9af9-38fc-a437-5a5b71357b72 | -9.25536 | -50.03288 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 826a2b5f-3d05-3bfe-b54f-4bdf68bf73cb | -11.13076 | -53.93137 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 35.1 |
| 3728e310-86a4-3755-b126-410fed2eafb6 | -6.03786 | -44.05156 | 2025-06-18 04:38:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d77d00f9-6ade-33d4-8b41-0461b7fef6ee | -6.61008 | -41.7762 | 2025-06-18 04:38:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a9610172-d557-3a14-81f3-e797872c7acc | -5.41492 | -47.56742 | 2025-06-18 04:38:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 751e629d-fb2d-3c94-ab93-29ce9ae9246e | -8.23897 | -46.38692 | 2025-06-18 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cc6cece7-a7be-3136-8933-48126c188bdc | -6.68013 | -43.21834 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 4.1 |
| c33d8c19-fa4d-370a-b345-cb3ac19c2548 | -7.28034 | -49.99796 | 2025-06-18 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 687200fa-2326-32a0-98a7-0220fb5aac2f | -11.33883 | -45.21202 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 740e0d2b-2c26-3d8e-8111-0c899a2da20a | -7.25107 | -44.64086 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d3211774-5d53-3a6f-9e63-f7a2a94f39f1 | -8.70661 | -50.04507 | 2025-06-18 04:38:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bc5ae84d-fccd-3362-a879-55db6ed1916e | -6.66249 | -43.18577 | 2025-06-18 04:38:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7a41c409-1d08-3a7c-98d5-e2914ab9d647 | -8.60023 | -48.05456 | 2025-06-18 04:38:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5fd685a-627f-350c-b8dc-9a51e8898a98 | -10.35628 | -57.24488 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 95ec18fb-9309-33fc-ba79-35e60b936f38 | -7.60849 | -45.55345 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c17ed7f5-8d52-34b3-b53a-84c85556181f | -9.84146 | -44.70066 | 2025-06-18 04:38:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e465e652-36cc-341f-848c-70960a01d810 | -9.26838 | -50.03824 | 2025-06-18 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5393f398-da4c-33ff-a98e-b2a039674b4b | -8.45459 | -46.90105 | 2025-06-18 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1dd8c554-b8ef-3b41-943c-530ec8371584 | -11.14245 | -53.92887 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c0fc22dc-3d49-33a3-b519-bce141eaf464 | -9.49057 | -56.08822 | 2025-06-18 04:38:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 92569995-38b0-3ec5-a322-fbc517835f9b | -10.98933 | -45.09686 | 2025-06-18 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 86c673ac-fb29-330f-8314-1fd69d25b838 | -10.35966 | -57.22626 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69122ebd-674a-3912-9b9e-1656cf69c9a2 | -7.28365 | -49.99849 | 2025-06-18 04:38:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 34ca7cae-9060-37e2-8362-10b03518fa2d | -10.92258 | -56.84113 | 2025-06-18 04:38:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 7fa45b2d-5e3e-3726-993d-6fbd10189a45 | -7.25506 | -44.64159 | 2025-06-18 04:38:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b6be289-9567-374f-8470-13b235154605 | -11.1417 | -53.93322 | 2025-06-18 04:38:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 0333402e-7d52-3a7d-a188-b2f04d1293c5 | -4.71109 | -48.43008 | 2025-06-18 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b55ba9e1-17d9-3972-a456-802dede65e5a | -10.34808 | -44.30425 | 2025-06-18 04:38:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ee84fab-a345-3db2-a831-f1f47888ef52 | -7.5486 | -45.6444 | 2025-06-18 04:38:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |


[Clique aqui para ver as próximas entradas](README16.md)
