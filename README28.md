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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48de9575-aa86-3126-9a51-8b372be5ab70 | -3.25784 | -50.39415 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b10aa7c-1395-39e0-888e-76849a7fe54d | -4.06495 | -46.85095 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eb82fb28-09b3-3445-9ef9-c3c0447a40d7 | -2.60223 | -54.01902 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5c922d65-e0bd-332e-b82d-d395202dd000 | -2.26721 | -48.98817 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4b9bb664-6968-3c02-885e-3d10bb999bf5 | -1.50007 | -51.97707 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20997214-311c-3ffe-ab4c-b7483b353648 | -2.09584 | -46.39851 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6c4411f1-85fb-3023-a97e-e75411d96141 | -3.31196 | -50.87546 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63fb6451-4c13-316b-87ba-99ee7439d09b | -3.08276 | -45.97098 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5c85067a-0499-358f-a7d6-88590ccfb9bf | 0.45882 | -50.78851 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| de471644-85ce-3500-8baa-2092ba87c0a9 | -0.95511 | -51.64365 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1c2e45f3-d5da-33c4-b8a4-be2c352df006 | -2.72645 | -47.97146 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| acbb944a-565e-36ff-a66a-251d87651a6f | -3.06444 | -53.29026 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 143f22e3-49d5-3eb2-aad8-6d38902dbe62 | -2.23547 | -46.82253 | 2024-11-21 04:29:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 66ce6622-17ec-3740-ab43-3642c272d32c | -2.29905 | -46.05005 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| d85e0130-fc27-3f7a-9096-78b1b060c4b2 | -2.32862 | -45.66309 | 2024-11-21 04:29:00 | NPP-375D | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 13bd2244-b2af-3455-bb8f-5a0b29b1eeb9 | -2.69292 | -51.71347 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f3c9a4c-d01b-355d-bbf7-984597cb0b61 | -2.71562 | -46.08989 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0e4a5c10-8d12-3738-8ef1-224316d5e3c3 | -1.47068 | -53.48548 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d0fc98d-7132-36af-ac46-e4af2fec123a | -4.0649 | -46.82967 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3298293f-4a03-33f4-888f-c7b207d8a860 | -2.73828 | -47.5393 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 005b3e32-25ba-3ed5-ad07-5e6d5fd45c84 | -3.88075 | -46.66653 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| af03d41b-ffee-3ec4-bb47-fa897508a19f | -3.59466 | -43.63088 | 2024-11-21 04:29:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 651cba10-f491-3aa9-851a-f8b847137808 | -3.07273 | -53.28994 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0102276f-9035-3d2b-b851-ea83f08390c0 | -3.51487 | -44.92624 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c045db7c-2cd2-36ba-9589-75caf1ac517f | -2.38476 | -48.92894 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 2535a7b8-cd22-3aec-8082-103173cb96a6 | -3.95513 | -46.90478 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d8d38d2e-44f7-3d13-915b-65d685a497f9 | -1.51676 | -52.08751 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6966b5d3-ede1-316f-be5f-f6f2cf84b890 | -1.17494 | -46.72379 | 2024-11-21 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5161c7b3-fed2-3439-a450-b18b1c0c1f93 | -3.47019 | -47.68208 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0cf91329-ea03-3931-8727-9d42b38147de | -2.69608 | -46.23661 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6787fdd-5f41-3d1f-8c54-5353cc1335ea | -2.15853 | -50.91318 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 932ed7dc-9403-3472-b3be-c853212da508 | -1.42825 | -46.0149 | 2024-11-21 04:29:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28f2a28c-8b78-32de-b393-a56640529a33 | -3.96293 | -46.72533 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8415df09-f525-380f-85e9-a30e892ba152 | -1.32061 | -55.45683 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10eafcf0-40f5-360a-861f-858ce4e929dd | -2.09065 | -46.32341 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| fc35850f-e773-3750-b932-3856d43e2b8a | -2.62747 | -46.06912 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6782e33f-b48f-3626-895b-e8ad88c09952 | -0.95156 | -51.7175 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 949fca0a-6350-3623-9970-871c34d6fe67 | -1.23187 | -51.78799 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| daf21328-5f29-3bc7-9dea-e4aa6f00ba90 | -4.00737 | -47.97011 | 2024-11-21 04:29:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d13a9e9e-ce16-32b2-9280-5377b50f9ee7 | -2.18149 | -50.5791 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff8d5ee7-159f-31c9-803d-4a62b7f7323b | -2.55089 | -47.28931 | 2024-11-21 04:29:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c12aa269-ce26-3209-9c9f-1df110a86357 | -1.48993 | -51.13411 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| acbc8e9e-72e6-32f1-9e09-d8fcb22c2993 | -2.40453 | -48.61135 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 06b75852-193a-3dd6-b565-1a09d001c4aa | 0.61579 | -51.77531 | 2024-11-21 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d4577df-63f3-3c9e-a35f-06e6b559ada4 | -2.38652 | -49.09659 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fa4c8a07-f7da-30fa-a09e-08e0631b7f3b | -2.00414 | -46.6138 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 72db3914-87e4-3b57-918d-42f4cc5145e6 | -2.00883 | -54.52679 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| d277328b-5030-3e9b-ba36-389570b98c9e | 0.6152 | -51.77148 | 2024-11-21 04:29:00 | NPP-375D | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcdf9ca5-dae3-3dbc-8cae-0c4ef037e1b4 | -0.42098 | -51.56469 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0491d4b0-5762-3046-a9f3-e30e7375ef36 | -2.40635 | -51.99143 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d4f0882-408a-3d5b-a03d-8fabbf15463d | -3.2918 | -50.53694 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cdb4c3a2-3ea2-37c8-ac2e-cf1f0b484cec | -3.283 | -50.00739 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 319febd1-a57e-3176-a908-c8f60bbea1eb | -2.72253 | -47.97447 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3eb41ea2-f194-392e-8e11-0269c1ae92f1 | -1.25044 | -51.74984 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e22f5fb-a906-39fa-8cbe-87ea6d9c6ee7 | 0.40803 | -50.81898 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2bdc600-ac85-34ff-81c7-5c60e7effb5c | -2.14507 | -53.57077 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c47217b-575e-372d-8497-286e99b59b56 | -4.02966 | -43.74995 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50ff1e5d-6b21-3fc3-b973-ce0ef42d7852 | -1.98451 | -53.13825 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3f64cc0b-fd04-377c-8454-7691ff52198f | -0.93581 | -51.71908 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5f72ca6d-d394-330d-9076-25d3c6418c57 | -2.1019 | -48.88978 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4f376ad-ca78-380c-b10e-b3942ccc9c1b | -3.94551 | -46.34145 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e621b980-46b0-327f-9e83-463a5d25fd58 | -2.06345 | -53.43747 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 20e9057e-2c06-3172-a6f0-4b014917bb12 | 0.81599 | -50.25594 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e27cf626-3a9f-3963-b61b-7da149f1cefb | -2.93742 | -48.33235 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 603a6f1a-b83a-3d1d-ad25-e5e86510c49f | -0.88887 | -51.72286 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01223229-1719-328f-9e79-1158528f1a79 | -1.23241 | -46.74323 | 2024-11-21 04:29:00 | NPP-375D | BRAGANÇA | PARÁ | Brasil | 1501709 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2cfb27b1-1a5a-3b37-af1c-609df44e8051 | -1.19958 | -53.68526 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d719c14e-9b79-3651-8ead-9e1ace401f18 | -1.21839 | -51.79327 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e80ee94e-f504-3c42-89af-f382fbf985c6 | -2.41764 | -54.63742 | 2024-11-21 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3a3012ca-0b91-3c43-a14e-3bc9af8db800 | -3.94292 | -46.70094 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1ec611f-ff3c-3e10-ad6b-a052c200ce5c | -4.06822 | -46.83018 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4a24012-bef0-3876-960a-7affe7f1a082 | -2.82394 | -54.02051 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf771b1b-5057-36e5-ab9f-b9f5cf24966f | -2.93013 | -45.27095 | 2024-11-21 04:29:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8e5b25a8-a3ae-31ab-8487-e194215ca08a | -1.58227 | -52.92904 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 11d96ebb-9180-3b66-8997-e57d09b7f5b2 | -3.33379 | -50.50161 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 860e2ab4-f1ca-3f7e-947c-3118ed461be2 | -2.72309 | -47.97094 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 767588bd-7823-3673-bbe1-92e8caff3ebb | -2.85392 | -46.67624 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1921b023-4f02-3c00-a90d-6d754e0c56a6 | -1.59385 | -50.44001 | 2024-11-21 04:29:00 | NPP-375D | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2554f582-8954-3a49-a794-75f0f743c27f | -3.2699 | -50.62766 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc2cbfff-f290-3215-a4ea-e436314af00e | -2.65889 | -46.56057 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3195a4f3-1e38-3c5b-8c69-6ad0ecb6116f | -1.46332 | -52.69122 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b558a53d-debc-3ca3-bbef-6a4dc01e28e5 | -0.25375 | -48.51309 | 2024-11-21 04:29:00 | NPP-375D | SOURE | PARÁ | Brasil | 1507904 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3738fed7-7ee6-38c0-9ca7-964e89e0d08a | -3.22352 | -50.58416 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a135d445-a2b2-3642-beb0-eeb76e043c79 | -3.10937 | -53.17772 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6221f080-d942-33eb-9339-a08573f743b1 | -2.61151 | -54.53686 | 2024-11-21 04:29:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a084efa8-5057-341f-9113-4d7eeb6ea377 | -1.2525 | -51.77927 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b917b9b5-78e8-3b9a-93ac-5019786ae3b9 | -2.62801 | -46.06562 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c870f964-32d9-3f43-b71f-27a4b9c057c6 | -1.04716 | -51.7403 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 14171720-913d-3ace-893e-63781ebfe17a | -2.47573 | -49.17286 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| aa1edcca-3921-39a6-89e3-30337b3e34c4 | -3.35979 | -50.17933 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| bd272bf9-a2b1-3e15-80c2-db003bcee552 | -2.26267 | -48.40199 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d0b3589c-134c-3d1b-a7d0-30f80d017c4e | -3.2675 | -45.37003 | 2024-11-21 04:29:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7d05de5b-daa4-31bc-859d-af343ab5cd35 | -2.92007 | -46.83476 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b960c46f-6822-3aa4-b745-4247d7f2cad0 | -2.61383 | -48.21645 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db7a5b1d-86d6-353a-a8b0-dd7e05dd5361 | -2.75189 | -48.57823 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 656d28c5-d27e-3b03-b4b0-371ec7782735 | -0.044 | -51.23891 | 2024-11-21 04:29:00 | NPP-375D | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8004ca9f-afdd-37de-abc9-5770113108ff | -4.47531 | -42.95713 | 2024-11-21 04:29:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c9dbb55-6401-3929-ab8d-8d47f4ae4f7d | -3.27753 | -50.57933 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d0c3f4eb-e6c9-3dab-8764-5e5b1bb3d003 | -3.89291 | -46.65419 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2c378170-8295-374e-ba09-17716c463281 | -2.6651 | -46.2425 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README29.md)
