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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0cdc9aa6-1749-3dd9-8c1a-25bb1815e83d | -10.90169 | -48.18627 | 2025-09-15 04:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 35894a3a-8602-3c7d-b0cb-2c9ca2ebb2ce | -15.78145 | -53.47517 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 013843b6-c39c-3317-a138-72a5191f2de3 | -14.82664 | -51.63683 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c4c33047-44d1-3590-9ef5-4bbc5f426762 | -11.48027 | -43.60596 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 528fffd6-b5a4-3e81-a170-c93b17f4c3f5 | -11.29129 | -50.84108 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2829fb50-bf6f-32a5-857b-b0c05b2755ae | -15.41563 | -52.98702 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ce3a592-7d7f-34fa-8498-6b34f759bc3c | -15.1023 | -52.47897 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b63f9b84-788d-3647-ac43-bccca073cc42 | -13.90264 | -48.31797 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 24d17779-e34b-3864-b400-849cec936c58 | -12.05047 | -46.54376 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d77d77de-cce4-3f48-a9d3-e2cb46a553a7 | -11.15737 | -57.19001 | 2025-09-15 04:51:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1605f5cd-ef35-3b67-bf81-9a339ccd43b5 | -13.74735 | -48.77304 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2d64372-2464-3e95-a161-e900d0418ed1 | -15.18202 | -52.3183 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c745bc6c-c8c0-3155-b786-b11c1c57a099 | -15.86732 | -47.32869 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 67fa202d-2049-32fd-9b98-87c4eb46ea4f | -12.00373 | -46.66409 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fc85f9e3-24d2-38ab-bda4-0aa2816a051a | -11.62742 | -46.59192 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 691d80c8-03b3-31f7-a209-17dba1889141 | -11.08525 | -49.7333 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 052357c7-378c-3127-a60d-d13ea6f596a9 | -14.20176 | -48.76698 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05717808-75b4-31ca-81ae-ca5a73a5c37c | -14.4663 | -55.95972 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76a62ebe-6567-3cb7-ba26-86edd191233e | -11.85431 | -50.53064 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 01bad5b6-bf6e-33b4-a147-35384abf4cfd | -12.08841 | -44.87176 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1607c02e-828d-35f0-889c-115fc2760132 | -17.73604 | -49.08646 | 2025-09-15 04:51:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| cc1877bf-96a6-3db2-938f-5bb606f0ad12 | -13.89937 | -48.313 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 83c76d85-eb17-3569-a863-4895d415b23a | -11.70574 | -59.31129 | 2025-09-15 04:51:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763ef017-db82-3980-b6c8-53f85ec7db95 | -15.41287 | -52.98288 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59787722-04d1-393c-b6c1-54b81e9ec123 | -13.88008 | -48.1399 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8b813165-a500-3136-b236-9a0278964f32 | -16.27779 | -54.92076 | 2025-09-15 04:51:00 | NPP-375D | JUSCIMEIRA | MATO GROSSO | Brasil | 5105200 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8cc14dc8-1f31-3350-957b-9a947c5e93f0 | -11.62376 | -46.58749 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4e12ddfb-80c0-3e28-ad2d-83306786481c | -11.08233 | -49.72884 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e851dfc4-a733-377b-a01e-f35c77b892ec | -16.49262 | -55.10207 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 5fed14ce-c1d2-3cc5-a7d0-72b82ba84a2b | -11.50855 | -43.64328 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5480d36-d968-36e3-94b2-365bd882b9fc | -13.89546 | -48.31265 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| cc49e380-f648-3609-b247-aae61cd712ea | -11.80076 | -50.49618 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 519ca993-5d75-37c9-ac34-0317e9206ab2 | -13.88072 | -48.30456 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0558058c-0220-33de-8d79-efb9109459b0 | -10.3411 | -57.85534 | 2025-09-15 04:51:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 35ed5ea3-852f-3d94-ab99-a16de771b3c3 | -11.27269 | -50.82699 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3b77045d-8850-3d16-93b7-870caaf805fc | -15.09506 | -52.48149 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aebafff9-5774-377f-a158-5a873364c4a1 | -13.88146 | -48.13017 | 2025-09-15 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e6ba49c5-4b57-34b7-8a32-cc0ccc79adaa | -11.39904 | -51.36598 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 1866ad66-666c-3ffb-9266-9c052040b2ff | -14.79561 | -51.6129 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 989f5695-2263-3cd3-9ba1-4a5de9be58a8 | -12.43387 | -48.00289 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1515ed96-86c5-3083-8f2f-7d597cdd2aff | -11.86285 | -50.52048 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 71cdc180-4ebe-3370-ab54-d41318a3fd22 | -13.94502 | -44.79699 | 2025-09-15 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb7564c7-dc40-34bc-86ce-7567e642c6ca | -11.08118 | -49.73666 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d3bd960-19e7-39f0-832f-b6ebe53ea083 | -12.05102 | -46.53985 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6046d29-b593-3901-abb3-6249541378f1 | -11.36674 | -47.35495 | 2025-09-15 04:51:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1dfa6214-e4c0-3a69-a2f0-aa3979bf0f19 | -12.00267 | -46.67173 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 0c9bb8bb-eb1a-31c9-9711-d132dde46110 | -11.85943 | -50.51994 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 750962dc-c043-3bae-b446-95b492a35bc0 | -11.07476 | -49.73167 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d165ac5-5869-386f-9efc-bbe9baa07ee0 | -11.47632 | -43.59621 | 2025-09-15 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e6e5beef-aa1c-3f9c-86d9-a87a80f0d4df | -11.87311 | -50.52208 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3456c60c-1ae5-38e1-a950-e68e51d11932 | -17.37809 | -53.25307 | 2025-09-15 04:51:00 | NPP-375D | ALTO ARAGUAIA | MATO GROSSO | Brasil | 5100300 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a6455e1-a36a-36f7-b982-813c69ac0861 | -11.07419 | -49.73272 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dee0dcf9-1f2d-3c7a-b1bf-ff3b4e3f2081 | -18.61921 | -43.90604 | 2025-09-15 04:51:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| abdfc70c-5285-372c-b00f-4d6ffdcab977 | -11.07883 | -49.7283 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 37e7b91d-8f04-3929-80a7-d9607b198f68 | -10.92033 | -61.96452 | 2025-09-15 04:51:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3133bb16-4735-3b68-a91f-8525045bac36 | -15.78602 | -52.20663 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7d3282fa-7c67-37e9-831c-ad87e92f58f0 | -11.61956 | -46.58696 | 2025-09-15 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3c08562-d23f-3808-a59b-151359e06719 | -10.9385 | -45.50179 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4baa1626-e4f7-3e8a-a0ac-b7258c7cd33e | -15.08003 | -52.4757 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afb0e4b9-bbe7-33ad-ae4e-d2d82c3c6fef | -9.68931 | -62.00336 | 2025-09-15 04:51:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 11b182f1-9d0d-3f64-9fa6-06c2e7ce6683 | -16.58208 | -55.17245 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| cd87e797-d68a-354f-8920-2e93eb369a9d | -11.76723 | -50.7833 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5fb30b49-dcdf-3d4d-9165-4d6ea5623c55 | -11.66597 | -46.50088 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a94a7de2-19e3-33d8-9437-890052f506dc | -11.9928 | -47.19162 | 2025-09-15 04:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1b4b9cdc-7479-3d94-a2ff-aed4578f0e4b | -14.82044 | -51.63205 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| cd7c75ff-ea8c-3b4a-a2a6-256ad2898b57 | -15.69815 | -54.34499 | 2025-09-15 04:51:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0272c024-f58c-33a0-ae84-9f157ecbaf52 | -15.76264 | -52.23643 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b986174-5e2f-3ea7-b7f3-d7dd051116c2 | -10.93462 | -45.49672 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47c8f169-0f34-3f24-9d7d-5159087fd949 | -14.46918 | -55.96458 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 69136b6c-e946-30ea-9ce2-d849006ec102 | -12.00687 | -46.67236 | 2025-09-15 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| c636c16b-79d8-3dda-8332-0c7eec0615e2 | -11.12574 | -45.31305 | 2025-09-15 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 67a01071-e15d-3f91-a5b1-ce32f3abb901 | -12.00115 | -47.76468 | 2025-09-15 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 5f00fbec-8002-344e-8117-0a71c8dba419 | -17.73614 | -49.08806 | 2025-09-15 04:51:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f66566f2-951a-3ded-9778-6f8283ad768d | -13.7511 | -48.77378 | 2025-09-15 04:51:00 | NPP-375D | CAMPINORTE | GOIÁS | Brasil | 5204706 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d7d81b0-b3e6-3312-8f76-da719b1e8e70 | -11.26875 | -50.8301 | 2025-09-15 04:51:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53d2093f-c5c3-3e47-9fd7-3737296e01f9 | -11.76667 | -50.78697 | 2025-09-15 04:51:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfc1d9a5-613a-317d-b131-3561feba7cfe | -11.07999 | -49.72049 | 2025-09-15 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a57f122a-3658-3bce-9550-7454b9528d84 | -14.80293 | -51.61029 | 2025-09-15 04:51:00 | NPP-375D | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e5738269-3833-35e1-938e-b350f1046f61 | -12.05203 | -63.12242 | 2025-09-15 04:51:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ff53eef-6057-3903-82cb-92eb0dc50a64 | -14.45911 | -55.95839 | 2025-09-15 04:51:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b631d59f-8f7b-3083-bc03-91294a40a5b3 | -8.4578 | -64.14134 | 2025-09-15 04:51:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 98e92532-e583-30ea-b161-58973b65ad61 | -12.64603 | -47.93714 | 2025-09-15 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8eaee84e-0c31-325a-9f98-dce76ac35dd7 | -16.66915 | -49.77876 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 088cff74-d405-3bd9-9f7e-2a562510f4da | -16.62292 | -48.96635 | 2025-09-15 04:51:00 | NPP-375D | BONFINÓPOLIS | GOIÁS | Brasil | 5203559 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| adab2fc7-4d04-3dee-b561-be6c189b48f9 | -16.71702 | -54.94909 | 2025-09-15 04:51:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6101bf09-4564-39ea-b2a4-7a8df98c53c8 | -11.78876 | -50.43674 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| dca6265e-836f-3589-9e15-3c8b152cc902 | -15.80106 | -53.4746 | 2025-09-15 04:51:00 | NPP-375D | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aa31eec-c058-33b2-84c9-971597612ffb | -12.11247 | -44.84087 | 2025-09-15 04:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc336ba5-e6eb-3b9e-ba0f-68b3ba4e8823 | -16.67466 | -49.78189 | 2025-09-15 04:51:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c8dc5bfb-7750-3c18-8a3e-7a393c9c774c | -11.83334 | -50.44369 | 2025-09-15 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 226515ca-ea36-3111-b694-a2873cd5c0ea | -12.08368 | -44.87102 | 2025-09-15 04:51:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2d22ac8a-360d-312b-9b38-70c0f3a95d8b | -15.78882 | -52.21088 | 2025-09-15 04:51:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0ea6a1d2-8a42-30af-90ff-15ee7934785a | -14.20044 | -48.77628 | 2025-09-15 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ad010b2c-bc43-3f55-a4f8-00eeb03b2c86 | -11.66122 | -46.50419 | 2025-09-15 04:51:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47136d83-a4dc-3949-bc9d-7220af49c38d | -14.17799 | -46.14895 | 2025-09-15 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 699ff047-bb91-3540-93a4-161d2d8b96d9 | -13.17653 | -47.28731 | 2025-09-15 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a65f0885-fc49-3c01-9fda-fd9336a9ff7d | -18.78692 | -48.5403 | 2025-09-15 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae1bfff5-4c90-381b-b791-1d0e134615e4 | -18.791 | -48.54095 | 2025-09-15 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 581e339d-a7ae-3ad9-9016-5558a4fb1435 | -24.84122 | -50.35722 | 2025-09-15 04:53:00 | NPP-375D | CARAMBEÍ | PARANÁ | Brasil | 4104659 | 41 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2648a259-61e5-31a6-85bb-513e0cd5caa5 | -20.2386 | -46.1806 | 2025-09-15 04:53:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README54.md)
