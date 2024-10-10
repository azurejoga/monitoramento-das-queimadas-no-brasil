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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1273949b-3fa2-36a2-9b87-808a2e16a6b6 | -11.60233 | -54.69527 | 2024-10-10 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 22cfd69c-6f2c-3620-be3f-c762452e0b47 | -11.59775 | -54.69086 | 2024-10-10 04:19:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbaed309-a89d-3d41-a0af-5b7da17a1038 | -11.18955 | -54.88039 | 2024-10-10 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d85014f-a6fd-3a39-992c-4ce653f8a8d3 | -11.1889 | -54.88376 | 2024-10-10 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 65fc9ecd-3897-3c45-8782-f8b7c71ea656 | -11.17189 | -54.78 | 2024-10-10 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 827c0e83-bdff-3803-a9c6-610aa47be6f1 | -11.17126 | -54.78338 | 2024-10-10 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af148925-9285-369a-91b2-6254a967c7bd | -11.16661 | -54.77896 | 2024-10-10 04:19:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a926898-a746-3f22-baa3-0a50bef4e49a | -11.13854 | -54.01385 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d36fce26-7a1b-315e-98c7-8381331cb145 | -11.13797 | -54.01685 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5221fb69-4584-3365-b20c-954ec2d15c83 | -11.1374 | -54.01986 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d6cc886-1eb0-39f6-86c3-bf3732d160b7 | -11.13351 | -54.01289 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 053895ea-0758-3c32-b616-a96c114e144f | -11.13295 | -54.01588 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 11bdc06c-f503-399f-9760-ac01ba8157fd | -11.13238 | -54.0189 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fa7c1666-9cf6-3cf9-8940-d23346035c8e | -11.1123 | -54.29296 | 2024-10-10 04:19:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a11b7cfa-e2a8-3c2b-9b83-0ee0e0cb2302 | -11.35724 | -55.42245 | 2024-10-10 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fe3dddb1-257f-300f-b671-6d05330f4363 | -11.35654 | -55.42614 | 2024-10-10 04:19:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b557d240-4172-3be5-9151-e4627c1af82f | -12.6726 | -54.71258 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 15d23768-a04e-3877-9728-5f80189871ac | -12.67201 | -54.71568 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2247e537-5fa7-3055-b91e-56ccfc19363a | -12.67142 | -54.71878 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 06cdd107-86d9-349f-ad0b-295ea35b8b82 | -12.67082 | -54.72192 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f379df42-21b2-387c-a6d9-eeb254c7da00 | -12.66865 | -54.70543 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fede930-f433-3557-a7d9-e0d6d32a5723 | -12.66807 | -54.70848 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83ca8a1a-fc2d-3d74-a512-4e81deda129c | -12.66748 | -54.71155 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 696346fd-ab58-379e-a996-ddef1ef4882a | -12.66689 | -54.71466 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4b56c454-5e83-3970-ac5a-3e8947bbd855 | -12.66629 | -54.71779 | 2024-10-10 04:19:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9dadafc6-d20f-3d18-bbab-5c7589a7fe48 | -12.43205 | -54.565 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cfe1a681-ef1b-3586-9bc8-3b9ccf6b91f0 | -12.43147 | -54.56799 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3813eeed-75c0-345b-a334-90fc3c0a309f | -12.41329 | -54.56924 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 407cedf8-d064-326c-b188-da6e589c5339 | -12.41168 | -54.56102 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 77845a73-e2b1-366e-8828-7a23c283b6f3 | -12.41109 | -54.56406 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 25ec8dfc-d6bf-3eb8-95d1-1c2965451382 | -12.41049 | -54.56716 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 22a4c5f7-fd7a-3ca3-b282-550eaae3fd49 | -12.40989 | -54.57024 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d0a33ab5-b9cf-3fb5-b5f7-cce9f49c901f | -12.40934 | -54.56208 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1e3400b7-ac18-3dab-954a-8a8985925172 | -12.40929 | -54.5733 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d8e75746-b42e-36c7-a3d3-c125b0414f24 | -12.40877 | -54.56517 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 22af29d3-0950-3ad3-b5fc-b72e102a3077 | -12.4087 | -54.57634 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1acdb49e-3275-33e1-a51e-972218602067 | -12.40819 | -54.56827 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8649c113-4da6-356a-be98-9bb4a5114857 | -12.40811 | -54.57938 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 498b1e45-5d28-38fe-b942-5c5c9808d576 | -12.40761 | -54.57137 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9d3fadb9-7c3f-38c9-82e9-c1dee8fb4c67 | -12.40703 | -54.57443 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8e96f133-bb90-3f52-b942-5eda192ec805 | -12.40646 | -54.57747 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 239a1647-f8ff-363b-a28b-feae4d3ae88d | -12.4059 | -54.58051 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 679c5870-c087-3087-ab2c-6eb61b66ed57 | -12.60292 | -55.22055 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc878a2e-dcc3-368f-96f3-41df71234bf0 | -12.59762 | -55.21951 | 2024-10-10 04:19:00 | NPP-375D | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 59b44724-8bc5-3e4a-9706-78be6301bcb4 | -12.59698 | -55.22288 | 2024-10-10 04:19:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c08bdfc-02ed-3ef4-bcea-d0e546a851e5 | -12.5917 | -55.22172 | 2024-10-10 04:19:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5e0572b3-1830-3ff7-8a5e-d7b60314a69e | -12.59106 | -55.22507 | 2024-10-10 04:19:00 | NPP-375D | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f60d639c-20a4-3874-a34d-78a260a6b252 | -1.19845 | -54.12104 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 54b34f1a-211a-31d1-b257-e2e4848e8874 | -1.19481 | -54.10557 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 202f2f9f-c7a5-34bb-a613-b4dc3fb80d72 | -1.19402 | -54.1105 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 951f8f07-5205-30d6-b2e6-eed44dafb6c5 | -1.18889 | -54.10434 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e587493a-19eb-322d-b299-ee462ca1c355 | -1.18817 | -54.10882 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 519ca416-d904-3469-b4a5-a4f16775ffe0 | -1.16088 | -54.20144 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1e264305-a45a-3f4d-8606-9f88c2dbd279 | -1.16018 | -54.20575 | 2024-10-10 04:19:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93a24bdd-b64e-3f26-ae71-2dd3c982cf86 | -1.15803 | -53.78454 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3d8e6e16-982f-31dd-b757-1478f70f2a04 | -1.13183 | -53.65053 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9fa51f4b-d971-3498-bb15-556aa50f8d57 | -1.12817 | -53.44799 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 162b7845-8856-3243-8a7d-0d63c7a1d846 | -1.12395 | -53.44631 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28f1fb36-8a63-3e6e-9881-ac5aa19d777f | -1.12331 | -53.45019 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 58d185ba-6902-3ac2-815b-decd8a866498 | -1.12245 | -53.44704 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| dfd710ec-f0d6-3cb8-ab81-043db5deae69 | -1.12184 | -53.45094 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c2af7090-e6df-31c7-a4f6-0fd02788bfc2 | -1.11374 | -53.6149 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 810946fa-ba0e-3a21-8586-f0ff7beff87d | -1.11346 | -53.61739 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f5fae67-bec7-302a-a71f-911e47ecbcb7 | -1.11316 | -53.61852 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d204e1d2-ebfc-3843-b4be-4479ddf7d117 | -1.11286 | -53.62107 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 78446508-d364-334c-b91f-8c374027818b | -1.11258 | -53.62225 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6107100-47cb-3ff7-b82f-3efed47a2c9e | -1.10762 | -53.6168 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7fff1248-75ee-3271-ad2b-0c4bdefc0870 | -1.10731 | -53.618 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf47ac4b-db8c-37c3-b7e6-f72ddf604de9 | -1.10698 | -53.62068 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c34b7513-27e3-3d95-a7fd-2bcd29a84f9a | -1.10669 | -53.62194 | 2024-10-10 04:19:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b58be736-2a5c-36de-aeca-3fe242d1981a | -1.02955 | -53.73178 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27586c13-43b6-307a-b169-40d473c8354b | -1.02903 | -53.73503 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8619cf0c-d076-3806-a620-7fa2faa76620 | -1.0238 | -53.73031 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9d5a82b3-7a74-36d6-8d70-204d46aa8cdd | -1.0232 | -53.73403 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f999ab11-bb86-3324-80bc-d01f84a18c95 | -1.01737 | -53.73299 | 2024-10-10 04:19:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 51611d74-af7f-3e17-ad19-d552a954fab5 | -6.1712 | -55.48424 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b3be8a40-d359-3d3d-842c-4dd6a88ab2ca | -6.16596 | -55.47882 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 234eb6a3-aa7e-35e1-8260-95990fedef27 | -6.15995 | -55.47773 | 2024-10-10 04:19:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 82332ea3-738c-3ec3-a94c-b141a3910c17 | -6.8742 | -55.11604 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b5a6ef55-61e7-31d0-b7a2-d0200e24f625 | -6.86322 | -55.14347 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 0728698f-e51f-33a0-8d3a-d6390ac4eacf | -6.6485 | -54.94724 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab2d859d-afb2-37b8-9f2c-c10123b1287a | -6.64263 | -54.94553 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ac48739a-58d2-3704-abca-b2a5d5e5a84e | -7.96355 | -54.78276 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 46f04410-5cf2-3665-a80f-d5eb5879508a | -7.96164 | -54.78176 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f3d90e8c-89eb-3df2-a23a-bd4b7a77f1a0 | -7.95929 | -54.77436 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 016511a4-1eb2-383b-aa19-e4b06ca9f54c | -7.95863 | -54.77805 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 57f9249e-b9b9-3b25-a2dc-55ab8b38c04f | -7.95797 | -54.78174 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2c568453-9175-38c2-9abe-913dd45139af | -7.95674 | -54.77705 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b0aa0dc4-79ea-3c9d-91f2-67a46b546a69 | -7.95605 | -54.78074 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b20cc35f-8d55-3d19-ad8d-2d011be3b7c4 | -7.95185 | -54.77229 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| baab981c-59bd-3aed-88fe-0e596cc1d14e | -7.86232 | -54.89332 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bae16e43-aee5-3fae-8f0c-bcd231503fda | -7.68732 | -54.83511 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 261419fb-6939-3419-9d71-5393f461cbcb | -7.68664 | -54.83886 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 607cd0ff-9cf3-3725-9301-4901edc5d879 | -7.68167 | -54.83417 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 74e2e677-7cc9-38f6-989f-7ad88dfad396 | -7.68098 | -54.83796 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 903e39c9-3be6-3d2d-a356-0110d514febc | -7.96232 | -54.7781 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c0d16cc-9900-3b25-81e0-402d9e88f428 | -7.95743 | -54.77335 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 91465c4d-5506-364f-8054-dd980a149b6c | -7.95372 | -54.77325 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f00ab26c-03e8-3ac5-82b1-0816d73a9996 | -7.95305 | -54.77698 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e12f6eb0-a341-3d91-87b7-9e43c45b87be | -7.94813 | -54.77225 | 2024-10-10 04:19:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README82.md)
