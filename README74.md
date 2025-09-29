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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4043426-b5e0-3bc2-9ca9-e08284c9f491 | -3.10623 | -47.00377 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 06ef86b0-4b66-36ab-9397-123186f3ee85 | -2.58045 | -48.4046 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 3c1ea195-5e0e-39ea-8614-9d03b05edcfe | -0.09691 | -51.27906 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 76f0d741-fdca-3d49-a928-b682aa924466 | -2.57987 | -48.40095 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 84df0ec0-8beb-3119-94a5-d8108517c941 | -2.57973 | -48.40929 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| f20c2a05-756b-3c86-88b3-4f1fe9a326b0 | -3.10438 | -47.016 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 8b411e86-006b-3fc6-906c-9e0f9c8e528a | -2.58536 | -48.40664 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| d56ffb6e-8623-3af9-a080-9a8a4d6ad2c5 | -0.09708 | -51.27249 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 84c5b47a-8ef5-3ce4-b726-cd5376c0d7a0 | -2.58118 | -48.39989 | 2025-09-29 05:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dda6ad8-73c3-38c6-ad01-c3fb43cef0f7 | -3.09668 | -47.02097 | 2025-09-29 05:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 3adf6301-9468-3f6b-9f9b-6a8a316bfb52 | -0.09619 | -51.27802 | 2025-09-29 05:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 21.9 |
| 96603321-2566-3e2a-b6ee-aea4bf2d9546 | 0.35728 | -51.04787 | 2025-09-29 05:23:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6330e5c0-f206-37a7-83a4-e4d06c63cafc | -3.30697 | -51.66891 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6371300a-1c68-3d12-aeb0-dec1dc2f49ce | -3.10024 | -47.00264 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| ad227029-c561-3253-89be-6c125efaf155 | -3.31156 | -51.67269 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c72533d4-71b2-306d-8e4d-6bd270791cbd | -3.48148 | -51.60138 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0217ca58-627c-33a1-af60-0c40405229c4 | -4.31147 | -48.08257 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 756f3b97-015b-3e63-ba2e-56a236113e63 | -3.30654 | -51.67178 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b9d03861-84db-336c-9fff-5f711fec5352 | -3.0849 | -52.92649 | 2025-09-29 05:25:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfe9e7b8-b4ba-3699-973c-03ffbb39bb6f | -9.41782 | -54.69225 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8fc1e921-09f1-343f-a5d8-3f63b049c0c3 | -10.39784 | -48.15941 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 27a22dc4-b4c7-382b-8a24-1be59d36f92e | -3.09171 | -47.01371 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef4de0ce-34d7-3f5d-920b-864e869b9af4 | -4.25192 | -46.94936 | 2025-09-29 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 389bad5e-298c-3875-b052-bd1a98e98234 | -9.41334 | -54.69155 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 414d48e1-671f-3481-b858-d866bcf62aa4 | 2.2596 | -50.73531 | 2025-09-29 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0971b75f-22d7-3afc-814b-3287d749252e | -3.49844 | -52.4738 | 2025-09-29 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a1e36d3-016c-3bb8-b7ee-c8e1eed46e75 | -9.41272 | -54.696 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 747cf43d-42e7-31e4-b445-cc11daa2689c | -9.41596 | -54.70556 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd932460-1694-3586-9922-1d59b2993f32 | -2.30377 | -52.90762 | 2025-09-29 05:25:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 73cb66eb-6476-382d-b287-06cfaa2d87ae | -8.66323 | -49.43184 | 2025-09-29 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c978be3b-2d74-329e-805f-fdf179dbdc6a | -9.39863 | -54.69859 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5419b8d4-7c75-3cb2-a4af-949dccf3cb77 | -8.7148 | -50.05544 | 2025-09-29 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f7b3de3f-9ada-38fc-ab94-4c1ef0dcd6d2 | -3.36727 | -49.75026 | 2025-09-29 05:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2277979-223f-3063-aaa5-5454bf52522e | -4.2613 | -48.55441 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78d1a394-5071-366e-a58f-b4d2b77c761f | -7.81273 | -46.89451 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d6a83983-73eb-37d7-ac6e-7482a42fdf98 | -8.71601 | -50.04644 | 2025-09-29 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cdc2d58c-5bbf-3286-a79d-399710c4eae8 | -9.4121 | -54.70044 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| bbb20787-15c7-3b0b-8199-c0566d1ac386 | -7.81695 | -46.99421 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 85059e5b-fcb2-3753-b7f3-3f4fc6a652cc | -10.3991 | -48.14896 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b04c2890-e503-3afe-917e-14c4a5c67080 | -4.26479 | -48.55595 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf4d58d7-0bc5-3735-9034-9556218ac11f | -9.40188 | -54.70813 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33245599-eb5d-37fd-b1ee-d39007fdf09d | -4.31032 | -48.09399 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8bba6e52-0b81-360f-a889-a2150fc81f12 | -7.81493 | -46.99162 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7398f02c-ecb4-3919-9d20-13c348509ae1 | -9.35713 | -51.49065 | 2025-09-29 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 6babbefe-b299-330d-9f69-7dc4ac1e796b | -7.80547 | -46.89361 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8316f960-a700-3ac7-b3d3-6775fb10ca06 | -7.81609 | -47.00117 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3a849da2-e788-376e-a26a-edf961756e97 | -3.48612 | -51.60501 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3b23ec30-39e0-3b7b-8306-aa17f393f3ba | -4.3099 | -48.09325 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 42555eaf-5548-358c-8c10-5df4c6e71aac | -4.31716 | -48.08881 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b39c5b9e-16f8-3bdf-a86c-4122c2e77086 | -7.81178 | -46.90194 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2b35cf8f-5046-372b-96b9-a07a132ba8ab | -9.6404 | -48.12989 | 2025-09-29 05:25:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f450735-692c-3cc1-976c-edc2c33bc362 | -3.31199 | -51.66978 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 857a0c51-bcd4-3ecf-a83b-3c4f62d74618 | -10.40415 | -48.15991 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9a76cb70-bd95-3868-a891-8b433c231e11 | -10.39728 | -48.15824 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |
| dc0f41a5-5497-3a9c-b92c-022855d89a8b | -10.40995 | -48.11762 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 748beaa1-a7df-3247-9003-2e03c254d399 | -4.25203 | -46.9502 | 2025-09-29 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 02a89592-2715-3032-8dfc-f79314a91999 | -4.31069 | -48.08792 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bb831942-9938-34a4-a2d5-5dda3c7e0b04 | -9.40823 | -54.69535 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69d8f927-d7f3-3c30-9f2b-b99e353909dc | -3.36668 | -49.75424 | 2025-09-29 05:25:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 939e014f-2b61-3f85-b35b-d03912a46bae | -4.29178 | -48.27308 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| c01b44ed-a284-3999-a621-b512b264772a | -3.48657 | -51.60205 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6dbc0f57-7c61-33c8-996d-b314a8f99b71 | -9.41658 | -54.70112 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 19de6b3e-84f1-3ba7-9fc1-2e41b77ab072 | -9.40886 | -54.69086 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f04a752-980d-37f0-ba53-e2e9103c9648 | -10.39161 | -48.15254 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 247103cc-78bc-31e8-b59c-5a544ab36226 | -4.31181 | -48.0833 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7f70fbd8-d800-303c-8ff7-221dbe218e57 | -4.31106 | -48.08866 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| bf74e0a8-506e-3750-8f83-68f7e497d43e | -3.50398 | -52.46947 | 2025-09-29 05:25:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 83f5575b-ff8b-3d5a-bc52-4f5f3d8868ae | -3.48403 | -51.60345 | 2025-09-29 05:25:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c0c9ca8d-9a13-3e68-87c8-01a227365b4f | -3.09847 | -47.01493 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| b4e6829b-e5c2-35eb-a884-cd161930b7d5 | -4.29093 | -48.26687 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5ab4a096-a664-3616-bad7-06b369eadeca | -8.7154 | -50.05094 | 2025-09-29 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4c821e38-692d-3498-946c-aa9532f66073 | -4.26058 | -48.55921 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d23bb3ea-a0e4-3d75-8b29-9929ad1e7392 | -9.39739 | -54.70755 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6ef3b5a4-920b-3bda-a278-d91af2683a72 | -9.35765 | -51.48651 | 2025-09-29 05:25:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 50b5ba95-14f3-36fb-a430-2570ddedeb30 | -7.81402 | -46.9986 | 2025-09-29 05:25:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| c0a50ef1-7922-37eb-b367-90163b09d95e | -9.39801 | -54.70309 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9befc12d-19bd-35a6-81c7-108ccfd990eb | -6.85944 | -47.35564 | 2025-09-29 05:25:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fc34c293-f360-39b9-8cc4-4a7b8706e42d | -9.40637 | -54.70872 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 113beb5f-6eaa-36fc-a0f0-a8e909f559cc | -10.39781 | -48.15361 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18116263-f373-34e2-9c46-c8cade300a9b | 2.26682 | -50.73824 | 2025-09-29 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8bd89a0f-f99d-3f22-b179-4a3e1f992153 | 2.26452 | -50.73448 | 2025-09-29 05:25:00 | NPP-375D | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b536140-dfad-323c-858d-1bec0fd34446 | -4.24497 | -46.94852 | 2025-09-29 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8858b32e-45c7-30fc-aa37-a56589a868aa | -4.24509 | -46.94935 | 2025-09-29 05:25:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ee6a3f0-991e-3bba-be18-caf0a0c8d4c4 | -9.40312 | -54.6992 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 54c7260c-daba-3a63-92ae-a007be5a3994 | -3.0926 | -47.00748 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0b4c350-5d27-3138-ab9c-89f42ab7d25b | -3.10437 | -47.02208 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6e9078be-e11c-384f-9482-3a73b64ac73b | -3.60232 | -51.94619 | 2025-09-29 05:25:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76b93cba-932a-3503-a0eb-5f6efe0314f8 | -4.25848 | -48.55527 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8176a40f-2b8d-3e9e-b6c5-0fcf29af36b4 | -4.31829 | -48.08418 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| afdd6861-4e08-34f4-997e-9e4eff50839d | -3.10525 | -47.01601 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| cd093440-4460-3a02-abd4-9ab96513cbfa | -3.09759 | -47.02099 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 03cbf123-ebbf-36b6-885b-7d994057d144 | -10.39836 | -48.15515 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 951eccef-4d96-3d9d-8191-444c08cdd46b | -9.4172 | -54.69669 | 2025-09-29 05:25:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 17cdb32d-39d1-3b44-a8c0-1799f0e26310 | -8.71692 | -50.048 | 2025-09-29 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ce7422b8-7402-32bb-9505-08faf7ef350b | -3.10613 | -47.00992 | 2025-09-29 05:25:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 68204a40-e33e-3247-b419-5c6614d79156 | -8.71634 | -50.05251 | 2025-09-29 05:25:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fbf470d4-381b-3cd9-9e02-fd9e1adcfeda | -4.29017 | -48.272 | 2025-09-29 05:25:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 7bcc008e-8231-3b24-86a3-641fe9c7d7d7 | -3.34434 | -49.2272 | 2025-09-29 05:25:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 078fb043-1227-3557-8512-addf1423ce56 | -8.66715 | -49.43222 | 2025-09-29 05:25:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f0db6e95-4143-387c-9135-706bcd6e4749 | -10.39045 | -48.15632 | 2025-09-29 05:25:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README75.md)
