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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4efbd61-f1ea-37e1-9d33-939ce6f52509 | -2.43033 | -46.50161 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 203cf1c2-1081-382a-b23c-992d00293938 | -2.67412 | -46.61269 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 96efd5a4-4f45-3152-8e87-786ea8135cfa | -1.4001 | -53.65741 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 8744115a-cc87-3b76-a1a5-e6d887def1a2 | -1.53581 | -45.84426 | 2024-12-02 04:23:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 174803ea-b3e5-3a30-88f0-289d7f7d3798 | -3.25869 | -46.44669 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1f915be4-4d85-3659-9a78-187628295a3a | -1.45065 | -54.52243 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10f49689-747f-37a7-a805-e559842226cf | -2.96033 | -49.57884 | 2024-12-02 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbca269e-7cb8-3194-8ec4-80705597690a | -3.13262 | -45.9803 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b4e4c425-fe18-3413-ac34-60783fe3301d | -2.55983 | -46.56214 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 545b15f6-b091-3fd4-a5ea-59db89ef2d24 | -3.26835 | -45.37585 | 2024-12-02 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 97169194-ff1f-338e-bddd-e28ff622a56e | -2.58166 | -46.42422 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b31c4fc-17d2-30af-9d98-b988d8ac7d89 | -2.12208 | -46.41751 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 63c9361d-7563-3f14-ab84-1114d3632897 | -2.89839 | -48.58754 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c4ef1bf9-5df2-3798-96df-34104c56f44c | -1.14711 | -53.66514 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e046dcc3-6f0e-3fd0-a9a8-d404f54b8106 | -3.26149 | -46.45073 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7bb407c0-5783-339e-9134-ab219ad681c1 | -2.21123 | -48.3814 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d630940b-80cb-3761-95a3-04c6b3f08c9e | -1.07896 | -54.11155 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3176a6c-b0cb-3e78-83c3-9fcfe52958e8 | -2.48414 | -46.57555 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 38b7f969-64e6-3dd7-ba80-92d17e900712 | -1.29503 | -51.36983 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a4ca370a-72e1-345f-afe2-3ddfe49b1be6 | -2.71805 | -46.20452 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fdde92bd-9c92-3103-86b4-7889fcb03f4b | -2.92425 | -48.01619 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59e6ab24-9f78-32bf-805d-bdc1e728000b | -1.89123 | -44.77529 | 2024-12-02 04:23:00 | NPP-375D | CURURUPU | MARANHÃO | Brasil | 2103703 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9d077f6-f8cb-3476-8fc9-2623d690b60b | -2.97335 | -48.04815 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3c8ba467-b049-39b8-931c-351f9894f55c | -1.56234 | -46.77565 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 102b596d-9878-3c54-a384-1793a61dda31 | -1.99356 | -46.459 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7fd5c5f0-78c4-34ce-9cbd-c4155a74d7d9 | -1.49834 | -54.95293 | 2024-12-02 04:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ba9e4dfc-fb93-307f-adb1-93e33c8a3f14 | -1.62907 | -45.81603 | 2024-12-02 04:23:00 | NPP-375D | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dee352e9-ea11-3e67-9426-90b8a9036f32 | -2.50683 | -46.23563 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cd03f428-b122-31d1-8a15-3cca92229203 | -2.81887 | -46.84725 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1e264c2-ac7e-373d-b43d-81b4d580aa90 | -2.20063 | -53.77494 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 318291da-6cc3-31ff-a4a8-bdcb41697a11 | -1.73339 | -52.63237 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1334f005-02f3-3e70-9b4c-66cfbb56cf02 | -2.56322 | -46.34552 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6ac7285-34a6-3f01-8ad1-47147f53bed8 | -2.67861 | -46.60611 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e67bd45d-5b37-36fb-8f51-d953d13d1b1e | -2.77885 | -46.01419 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6da84be2-06be-3985-90a9-29c56a5105f8 | -2.45834 | -46.52055 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 605ef23d-1f9d-3323-9e4d-913ac0c4307c | -1.69827 | -52.63719 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 22bddbbf-53c5-3065-87ce-dd839f9a07e2 | -3.13508 | -48.5289 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6241484b-079f-3393-832e-b56fd435063d | -2.44844 | -50.52111 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0b847eae-89e3-3e96-8fd3-2c28776b7926 | -3.16803 | -46.29284 | 2024-12-02 04:23:00 | NPP-375D | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 653f8cab-9c1e-30ff-90c6-988930b7617c | -2.70138 | -47.74055 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7c8320d5-53d9-3c71-a1bd-35e54eccbc8d | -2.47572 | -46.56329 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41ce524e-2e70-3e9c-8d83-a89242f8122e | -1.73168 | -52.63869 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 275912df-7bcb-3863-8399-cfaf97ffda21 | -2.6083 | -46.21243 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 33ae6ea8-28fe-32ed-a4a6-6a11e39804dd | -2.51406 | -46.23319 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e0e7851-fd0d-3550-9d58-7f3705711202 | -1.90683 | -52.86133 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2c9fb1f6-33eb-335c-b8a6-bbb9411b1f8b | -2.41556 | -48.87953 | 2024-12-02 04:23:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a916c34-3632-3ba1-8460-b2f334df08cf | -2.91361 | -45.34848 | 2024-12-02 04:23:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf7a3ac9-a43a-360c-8868-a7e6c738c9ba | -2.26514 | -53.6171 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 8a3f18b8-a36b-3aa1-81c0-3cec7689bb40 | -2.74742 | -46.12687 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7c34302f-e883-371d-8fd7-32d1b5f484cd | -2.97392 | -46.94476 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d32ded9-fe2a-3fd3-8b77-7556e3abfd25 | -2.5518 | -47.97698 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5438d3ef-08f8-3ec8-ac6e-6eae36d635b1 | -2.47124 | -46.56986 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bc35c0a9-7283-3f0a-9012-969fceb600d2 | -3.30489 | -46.40716 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ffff869a-d99b-3e3d-9f4e-7ee349ad32ae | -1.88055 | -45.52926 | 2024-12-02 04:23:00 | NPP-375D | TURIAÇU | MARANHÃO | Brasil | 2112407 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96d5c3f7-9be1-3d3a-9714-19a1f22c5509 | -1.07644 | -54.11142 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b9338202-12dd-33ae-aa41-8be9f7a8de30 | -2.44152 | -48.64569 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aecd2326-7fe0-3bc5-8121-100eb636dcd6 | -1.27136 | -54.55152 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65946e42-06f7-3b52-abff-995c60c1b0c1 | -2.86617 | -48.55686 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8303d13c-db70-3575-a786-9d0b9feb53d4 | -2.79799 | -48.68074 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7a6bc20-a0b3-3a98-80bd-1cb1207a9134 | -2.42977 | -46.50515 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 34fd1e45-d1b4-34dd-96b2-07615fd01b4e | -2.0602 | -47.73522 | 2024-12-02 04:23:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1e9e98b3-98a2-3926-9cf2-1efe59ca5084 | 1.13765 | -55.97596 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 935bbb8b-c314-3ca0-9b45-afb2c470034b | -2.76743 | -48.56838 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 73f7a16e-f4c6-36bc-a2de-1e426e3ab587 | -2.72701 | -46.25609 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a31405d7-b88a-3ffb-8c7e-3b692f11eb9f | -2.18987 | -53.77634 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 462433a5-cc62-34da-af5b-25d1f6b6e52b | -2.28594 | -45.74863 | 2024-12-02 04:23:00 | NPP-375D | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2ff54df-110e-3b78-be2a-4ddbd85a5b2b | -3.37111 | -46.66991 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 48d6ad88-8969-3ace-b7e9-fc3dec72fddb | 1.11818 | -55.99295 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80666c23-c556-3324-9a7b-0b7387a2ac2d | -3.86517 | -43.06941 | 2024-12-02 04:23:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef738757-74f8-3288-bc29-2e4b44b79526 | -2.86189 | -48.56042 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a0f1446a-e58d-3964-b196-832c8b421430 | -1.25729 | -51.58819 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b246ae11-1e95-3f2c-be53-bd7912e48357 | -2.60582 | -46.57665 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c17a2699-a758-3088-9b64-a44f0aafa04a | -1.40096 | -53.65213 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 15587cc4-6bce-3e4a-aca5-883cfd3a4d6c | -1.23658 | -51.60297 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4bc3fbc2-58cc-38d8-9021-1e34bcd43286 | -2.49592 | -47.27223 | 2024-12-02 04:23:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a3e8909c-dcf1-3131-af79-79d5e091d910 | -2.05099 | -51.19278 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 400034b8-898b-3736-905d-eca8687fad65 | -3.19341 | -46.5772 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ef54ed25-bf27-393b-82af-02ecca928dab | -2.60772 | -45.25106 | 2024-12-02 04:23:00 | NPP-375D | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 141eabb3-c9c7-3c29-9ca1-1f67406a9484 | -2.02115 | -54.31512 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 80186846-ddfc-3ac8-a0bb-5fd247c0d4d4 | -3.16427 | -46.63062 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f66ab7a-3ef0-33e5-9342-6734897d9ea2 | -1.24333 | -54.55066 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf05c5f0-d797-3814-a87b-6f4c9199dc88 | -2.92552 | -48.00836 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 618b96dc-ddcf-3f39-9c4f-aa5d50e6f874 | -3.16379 | -46.54724 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8fcb01e6-463d-30cd-892e-b470d4701888 | -3.13317 | -45.97683 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 803a13dc-20da-3b22-98f3-2efcebd3e768 | -2.83465 | -46.85709 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 154f0a9b-7014-3813-b948-c2517dfa06b3 | -3.05381 | -48.52861 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 187cefd1-c7d4-33c8-9ca4-ec0d03f4b2b9 | -2.74408 | -46.12635 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2e3e64e-1c0a-3298-84c9-ca5fdced636d | -2.47741 | -46.57449 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 388deeb8-c54e-3a3e-a3e2-29d059bafd3b | -2.46955 | -46.58055 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 71428e72-0aea-3ae6-a27c-1c24460437c9 | -1.53914 | -45.84478 | 2024-12-02 04:23:00 | NPP-375D | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 78f235ba-96e9-3728-9b23-7412650fb610 | -2.56713 | -46.40747 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2d6baa9d-7e13-3fb0-b07e-8e7359180bd4 | -0.59641 | -51.68738 | 2024-12-02 04:23:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66a4d8ed-cf68-3f6b-8682-1c2a1a193934 | -2.77106 | -48.56895 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0a219e3-6db5-3721-bbfa-8a9b4e0a2672 | -1.03029 | -53.55288 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7944a8b6-1e17-3bec-9f3a-89476a5e26be | -2.09211 | -46.31486 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d1ead12-9503-3b6a-8288-e9d35f6a7dec | -1.3561 | -55.20202 | 2024-12-02 04:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c43bc4ce-0106-3e81-8135-0593ce44c562 | -2.36457 | -48.28981 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 00f38855-bc69-31fc-af3f-22182c581737 | -1.73821 | -52.77819 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8c4b2003-2dbe-329f-b65c-01b899028e3f | 1.12369 | -55.98705 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ed097eaa-56a8-3f24-84d9-6b7c7004390e | -2.95628 | -39.96083 | 2024-12-02 04:23:00 | NPP-375D | ITAREMA | CEARÁ | Brasil | 2306553 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |


[Clique aqui para ver as próximas entradas](README30.md)
