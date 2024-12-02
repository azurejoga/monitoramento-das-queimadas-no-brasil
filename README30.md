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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 603d7152-ed32-3be4-aee2-4cd01b75fe5a | -2.60526 | -46.5802 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00201e2c-6504-3eb4-a5fb-6b764a44dd9d | -2.94213 | -47.99493 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57d17ebd-787b-3f6a-a105-60a94edc025c | -2.67356 | -46.61625 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e6049d53-22e9-3654-b319-f9b6d8684bd0 | -2.65506 | -46.58059 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6bee32bf-7982-3035-bb55-65df32131598 | 1.11499 | -55.99454 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3612ef46-ef0e-3225-90bc-29c7f8ae4374 | -2.79733 | -48.68497 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e67dce0-1e70-31c0-8831-9d949414e04e | -3.0565 | -48.53056 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 107e2c37-95c1-3018-8c2d-f5f4c81fe9c2 | -1.07552 | -53.4501 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| bf80d262-9764-3b6f-8e0d-0dae4c5866f2 | -3.12766 | -45.99017 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5522a19c-13f1-396d-8109-16b1de64240e | -1.23376 | -51.62079 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 950443fb-fcd0-323d-afe8-610fc322db0f | -2.50293 | -46.23862 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fabd7001-e28e-3e11-81d1-544ebac4504b | -3.22412 | -46.44844 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c84492a9-3ee7-374d-a28d-f4b1210f00cf | -2.87699 | -47.8621 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1f969df9-6b07-3bd0-8e54-ae83f287c223 | -2.7546 | -46.10301 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34a02c44-7300-3ef0-9dc6-a170b5aeb717 | -2.9717 | -48.03579 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd58fe6e-e8dd-39c0-a814-c71e99bd0110 | 1.0985 | -56.01198 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bbbf4ca0-9387-3ca6-88bd-359eb6e8fcfa | -3.03042 | -47.80227 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e06af094-68e2-3187-a253-09237a91e8e2 | -3.13738 | -48.53772 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bb2ab42b-3ba9-34d5-a0f8-a2666bfef80c | -2.04538 | -51.20021 | 2024-12-02 04:23:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acafc945-2e50-36af-adbf-cec53bcf8d50 | -2.46955 | -46.55868 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 72364470-40df-3805-9a09-d0c25fa98b8c | -1.59531 | -51.26336 | 2024-12-02 04:23:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 90e0f43f-984a-3f6e-bf04-77fe2c1f6a01 | -2.11481 | -46.39826 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8340d7c8-016a-3528-ad74-2f75bf0bc55a | -2.4819 | -46.56791 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5382277-b4b0-3c12-bc9b-42f0e85ae18f | -2.6444 | -46.58256 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 86fa196b-b26f-36c8-b4e6-e3dd4ce1dc57 | -1.81404 | -46.64014 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 29d4764c-813e-35fb-94d6-e9409e81fdbd | -2.72084 | -46.20853 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21edca5f-4092-38bf-942f-18a65ec5ed24 | -2.71637 | -46.19352 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| adebacae-da0d-3853-9ab6-6aca4a21b160 | -2.71414 | -46.186 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 136ae877-6b1c-3f68-bd5b-83d00a2260e3 | -2.67917 | -46.60255 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f492de8d-4f92-3eff-8566-89a8f7df09fb | -2.99745 | -46.91177 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f2cec87b-ae3a-391d-9ecb-6e8240c091d4 | -3.1962 | -46.58126 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 74b37c29-681e-3e8c-b6b4-d720a17ae9a3 | -2.58619 | -46.56993 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 48b4967e-4af1-3bb6-ae31-beb5943023e2 | -1.49772 | -54.95669 | 2024-12-02 04:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea567b68-513b-359d-8548-376dbd6758ac | -2.80144 | -46.82612 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e446d0fa-1040-3827-b6a7-6b85c630b9ad | -2.50334 | -46.10624 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 73cdf4c8-2c2e-362b-a605-27777568efa2 | -1.0795 | -54.10832 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0c935032-54e6-38fd-87a1-a83bfe97036d | -2.92136 | -48.01171 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3eac0d4c-ba83-36a3-87eb-c24d602c75f0 | -2.86256 | -48.55627 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 127d2d53-b35c-36bd-bf51-29f6e77ec46d | -2.15831 | -46.08111 | 2024-12-02 04:23:00 | NPP-375D | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe80ee73-412a-3a43-aada-a11a653ec8e3 | -2.4847 | -46.572 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2489ad2e-71f9-39f2-b6a1-0d171fe1b059 | -3.28865 | -46.04052 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60fdc416-2d79-3dab-8d83-de0a2032549d | -3.18226 | -46.49598 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a2f648fd-d882-30f1-b498-fa5ecd007b6d | -3.1293 | -45.97978 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1cc3ff03-3142-3368-ba67-8cf619437845 | -1.7345 | -52.78181 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| df54156c-de76-3650-97e5-f9492e7fe5a4 | -1.07765 | -53.45267 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| fdb549ff-80fe-3252-a0f8-e6877a86ff38 | -2.9565 | -49.57822 | 2024-12-02 04:23:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7db52544-c992-330e-b71c-e1a9c35fef64 | -2.46675 | -46.57645 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5e8aca96-e199-3a36-9fa3-ba74a91d5943 | -2.15549 | -49.76004 | 2024-12-02 04:23:00 | NPP-375D | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 848c6018-eb06-3ed1-81bc-1c8ae865bc44 | -1.2336 | -53.3612 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e13a33e-4420-3568-aacb-2fa579f55d12 | -2.60245 | -46.57612 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f274e813-7172-314a-820f-2271d126bc4b | -2.55871 | -46.56925 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e6c3dac-38d7-3f63-b55b-7a55c66f62b0 | -2.56992 | -46.41153 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f78d39b5-50e2-37bc-9b6b-89db099236ab | -1.26177 | -51.58891 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be55ffbb-0ab1-3e8a-a6c1-eadcb1897ca0 | -2.93861 | -47.99437 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 49df2b2c-e708-37ee-a1b8-c8d0e1608b52 | 1.14644 | -55.96836 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| decb0f99-3943-3a85-a740-93e24442a20d | -1.44257 | -53.39639 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 98e8c333-700b-3be2-8ab6-b0e2ed5e8193 | -2.26703 | -53.60564 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a18acc41-ee84-37c9-bd26-a18b37b41b42 | -1.43705 | -53.39836 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b84f26d9-6df8-32f9-ad79-2875e2fc9512 | -1.35101 | -55.19724 | 2024-12-02 04:23:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7b55cf3-201b-3b9b-b785-343b1481d950 | -2.23528 | -46.38804 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a92e14ec-f198-3734-b91c-df25441141d3 | -3.2628 | -45.36792 | 2024-12-02 04:23:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c03fe4fa-732e-3f89-bba3-a74dd3b6b1db | -3.13593 | -45.97776 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2797dd65-7e01-32ec-b75e-d3dbf61f562a | -2.20623 | -48.34249 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2b8fbfab-f3d9-3809-88cb-dd7c075c806a | -2.80862 | -48.61348 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 980e7201-d3a5-3e4c-91b3-81fb4a46f0ed | -3.08844 | -46.55741 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b30bd3d2-18c5-30a4-af7a-818dfc92ebe8 | -1.23939 | -48.32601 | 2024-12-02 04:23:00 | NPP-375D | SANTA BÁRBARA DO PARÁ | PARÁ | Brasil | 1506351 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0624e4c-a54d-3148-8971-91225a69f40e | -2.47068 | -46.57342 | 2024-12-02 04:23:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62ec84d7-1e76-3fb8-a3ba-8644315ece6d | -1.07695 | -54.1082 | 2024-12-02 04:23:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 80da026d-b290-3308-9909-45aef4f5ddf8 | -2.67061 | -48.80103 | 2024-12-02 04:23:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b9005a62-320c-3a0f-a3db-17607d5448d8 | -1.29515 | -51.37531 | 2024-12-02 04:23:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 840122e0-881b-3a47-886f-181cf2d28d01 | 1.09302 | -56.01792 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d743927-5ebf-35ab-b1c5-a5a8dd1d5e8e | 1.12443 | -55.99193 | 2024-12-02 04:23:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ffb8b150-b9e5-35b2-b606-3d236a28b09c | -2.66268 | -46.12794 | 2024-12-02 04:23:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e51d197b-f320-3d58-97c4-ab79c3a99e68 | -2.70801 | -46.18147 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f1a29381-c3f3-3b65-aabb-d529b3c10266 | -2.11928 | -46.41346 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f924ebb1-7a95-3a9f-bc72-ea056a6300c9 | -2.14392 | -46.38832 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1da5794a-c970-3955-b20b-684032c35f73 | -3.27487 | -46.45286 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 5650fdf6-03f9-3db4-a20f-fbd93b218dca | -2.72067 | -47.5521 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7b6717d5-4353-3474-9a66-d4847a52ff28 | -1.9101 | -46.40973 | 2024-12-02 04:23:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e336d1e9-2367-3ba1-9a7f-782f74200526 | -2.91028 | -48.3285 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22cde5fa-fac3-39f4-b394-4479884430a5 | -1.72288 | -46.22509 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61dac1fa-9c0a-37a5-8fe4-fb5b8ea1dd4f | -2.63385 | -46.95559 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed2b7426-9a08-360a-9764-76fc75aa3673 | -2.93509 | -47.99381 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 80aa4ed6-77a7-3b46-9913-c128c3b841cc | -2.9303 | -48.00109 | 2024-12-02 04:23:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c74f5459-317b-3f29-a159-b1965cb06e40 | -2.56154 | -46.39937 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 16fc6311-2cc1-3d09-bc36-301e4070bfe6 | -2.63045 | -46.95506 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f34c062b-6b09-385c-936e-6415c6d6cdd2 | -1.07719 | -53.45565 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 6942e2b8-8058-3f6d-8635-af091187e77c | -2.84701 | -46.88855 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ee0c36bc-2092-385d-a921-c2a4e9fb07ff | -1.68664 | -46.20531 | 2024-12-02 04:23:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c350bad-fa31-3b2d-977e-2195998870bf | -1.07455 | -53.45603 | 2024-12-02 04:23:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| df8f19ac-75d3-3d13-9358-8eb1b2ce1596 | -3.12542 | -45.98272 | 2024-12-02 04:23:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f490971b-922b-3245-ae34-19136d67d8ac | -2.4349 | -48.64029 | 2024-12-02 04:23:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9dbbed72-4bb5-36ad-96e6-9a66cfc95fa1 | -2.5865 | -46.0122 | 2024-12-02 04:23:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 457c9af5-a70a-3357-8666-14d4ce5f15d6 | -2.19902 | -48.34135 | 2024-12-02 04:23:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6143a8c7-2eb3-3186-9e11-b3f746e1381d | -1.78671 | -52.75387 | 2024-12-02 04:23:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d316eeb0-f33c-3dc8-8953-f5d549e1c983 | -2.62308 | -46.95763 | 2024-12-02 04:23:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a866116d-b03e-3ac7-a84f-f526b72cf8ce | -2.55596 | -46.34799 | 2024-12-02 04:23:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c1cd515b-95d0-3b97-9b04-df36916660a4 | -4.1097 | -39.99591 | 2024-12-02 04:23:00 | NPP-375D | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e520d9f9-0baa-34bc-ab00-94d19d66dcf7 | 0.89197 | -50.95729 | 2024-12-02 04:23:00 | NPP-375D | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 87823e50-09e7-3376-a491-9986535bab45 | -1.13943 | -53.67644 | 2024-12-02 04:23:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
