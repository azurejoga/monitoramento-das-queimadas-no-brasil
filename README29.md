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
| e4384917-c126-377b-b089-89ecdcc87bf8 | -2.09193 | -48.47398 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b191fe51-7d80-37cf-886b-bbb390e1e00a | -1.50662 | -52.14665 | 2024-11-11 04:18:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 247856d8-dd1c-3c64-935a-fda04e4f2691 | -3.5904 | -44.54723 | 2024-11-11 04:18:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 254633d8-1e0b-39f5-a99a-2f837502149f | -2.33202 | -46.56799 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e98ff068-deb8-3f4d-af03-3363c81e6dd8 | -2.60167 | -48.19001 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbd776dd-db2a-3ecf-ab95-7e8b65b0e9a9 | -2.05999 | -46.14404 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 821aae40-f318-3288-b9b2-2522b8dce6d0 | -2.59383 | -48.31595 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bf07f297-dd19-362d-a719-700aad860eee | -2.06689 | -46.34632 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 44a58d48-302d-3756-9dab-d4e3608f1f93 | -2.54919 | -47.45013 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d24f1f0-285f-3710-8971-52bebb648ff2 | -2.54847 | -47.45455 | 2024-11-11 04:18:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 930cc75f-4ec2-33cd-aa0e-693fb2389673 | -2.99694 | -46.94213 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 20c710a3-9518-330d-95ae-ea4ecf8a4d18 | -2.8416 | -46.65147 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8bcf3a18-cfa5-3523-ac6a-ebfa2400c13a | -1.20187 | -47.56324 | 2024-11-11 04:18:00 | NPP-375D | IGARAPÉ-AÇU | PARÁ | Brasil | 1503200 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a557c601-12fc-304f-97e7-f9af19b37650 | -2.25243 | -53.73636 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| e25ab9d4-edaf-3830-8394-9dc5bcb973df | -2.48441 | -46.35164 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f587137c-ce8d-34d8-91f4-8adccd9c9e4e | -2.65439 | -46.79883 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c028f0d-bfe0-3821-825c-e032bd95a553 | -2.192 | -48.36929 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87a5ad4a-10f9-337d-957f-e7b6916acfce | -2.83509 | -46.64629 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 396b8cb8-bebf-3cba-a992-1ec5df11331a | -2.99494 | -49.51632 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b9cc6806-52b2-34a0-89fc-704f6111609e | -3.24693 | -46.43777 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b78b3a0-ecf4-34c8-8b04-61b47c8c8554 | -2.37409 | -50.33632 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fe0a76f9-423e-318b-817f-66c7b31b819f | -3.00215 | -49.52547 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bb6bba11-ab67-3186-afc7-16e238216705 | -4.69458 | -46.43254 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c0da929d-0b63-32b4-a545-a2898764bab6 | -2.73205 | -54.13815 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e5195892-1526-3717-b8ad-061b6ae1e13e | -2.21106 | -48.37755 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0f369d6-626d-3064-bfc6-32d3fda581c1 | -2.54385 | -47.30976 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3c4c44bb-5721-3151-9e33-d513db793e43 | -3.99055 | -44.13433 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea3e7245-af75-3148-b77e-ce9559344899 | -3.53578 | -43.56129 | 2024-11-11 04:18:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7abfe18e-947c-30db-b289-f7d91a60c918 | -4.47875 | -45.6648 | 2024-11-11 04:18:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57a8d546-2635-30f7-9202-283e3ba3815c | -2.54549 | -47.32359 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5ff05fe4-4379-3ddf-b8c0-73d94ff44040 | -2.68093 | -48.66104 | 2024-11-11 04:18:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d726d752-66d0-3164-8543-925232626368 | -2.19313 | -46.81287 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 71867689-91c9-306d-92ec-5314719148f6 | -0.88529 | -52.93211 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7b9e85e2-976a-36d5-81c6-58cbec078eb5 | -2.22932 | -48.39096 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 22.0 |
| da2b9fc6-7481-3792-879e-5c2eaa0eb84c | -3.24463 | -45.38414 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 099d1d85-2513-3237-b49c-0064e241a43f | -4.46126 | -38.74929 | 2024-11-11 04:18:00 | NPP-375D | ARACOIABA | CEARÁ | Brasil | 2301208 | 23 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9ae1294e-c622-3881-875c-f3ad8670ccd9 | -2.59854 | -48.18453 | 2024-11-11 04:18:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d93d87f-847d-350c-818f-f4becdb45d6d | -2.84479 | -46.63129 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4fc52670-bdd1-35e5-86a8-ad6ea6d16190 | -1.62592 | -52.53234 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e008cc39-76f6-3f07-adc6-daa6440fd0a4 | -1.96696 | -46.40989 | 2024-11-11 04:18:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc66adb8-2994-3906-8c4e-aba73bf58cfe | -2.8016 | -46.60381 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 75ddb6c2-e48f-32f7-b0a0-4be1e8d752b3 | -1.7605 | -48.5206 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d65d271f-82a7-3658-8864-da233eccb8d0 | -4.31685 | -46.38572 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ed184018-4368-3228-b55c-54833c321650 | -2.24667 | -53.66357 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60e2294e-0b99-3e6b-9468-886b62ef3844 | -3.18549 | -46.18979 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fac8b5c3-9501-3bf9-adc9-d6cbc93527bf | -4.02098 | -46.96182 | 2024-11-11 04:18:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7484e66e-8033-3f88-b2eb-dafe7d20838c | -2.59822 | -51.7214 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2922e577-b940-3639-a23d-2e5e428bd71e | -1.32334 | -54.63991 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9b130cfb-c94e-3a58-a0de-b25fa7f6ef82 | -2.99367 | -49.52414 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e03f2103-1660-3396-9ada-847767d62649 | -2.30487 | -48.90172 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 357234ef-833f-3ec4-b9c6-7b2d55f76fad | -3.12827 | -45.23688 | 2024-11-11 04:18:00 | NPP-375D | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 87e8c1cc-ca78-348e-b73b-e73a62876a34 | -1.8266 | -50.97678 | 2024-11-11 04:18:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 16963c50-847b-37da-89f0-a5faeedb2580 | -2.82372 | -46.64863 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| df5369cd-bf05-3427-baed-d54ff8f53e5b | -4.69396 | -46.43639 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3992c976-8e32-3b63-bf0f-bee3fd9049e6 | -2.1202 | -47.89312 | 2024-11-11 04:18:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf80e79e-1d28-3ce8-8f1b-d627d6086c94 | -2.75112 | -49.36755 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 26b994a2-1425-3ef0-8994-83ab28e32142 | -2.69704 | -46.80977 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| df041a85-cfc2-3b73-8ea6-75fb740a3a5f | -3.48208 | -48.23935 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 81fe139b-5a09-3b9f-ae72-5dae420779f3 | -4.68007 | -46.36778 | 2024-11-11 04:18:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a2895e00-0951-3c72-9b95-ac43e94ee29f | -0.14752 | -51.55257 | 2024-11-11 04:18:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| aa8f83a5-09c0-30f3-91b2-aa3cb7754513 | -2.51901 | -47.34656 | 2024-11-11 04:18:00 | NPP-375D | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 63fce690-6295-3f6b-9a0f-34de69cc3d0e | -3.59373 | -44.54776 | 2024-11-11 04:18:00 | NPP-375D | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dadbd4f4-0767-3788-823a-40983f08a096 | -1.39055 | -52.36898 | 2024-11-11 04:18:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3456df94-89c8-3f34-810a-a801856ab9c2 | -2.4611 | -53.69546 | 2024-11-11 04:18:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27c633b5-13ff-335a-93e7-c25fbabb56a6 | -3.12661 | -51.10636 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60111726-d233-3c57-8b45-ada6cf5ced72 | -3.239 | -45.37583 | 2024-11-11 04:18:00 | NPP-375D | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4dc8a6d5-e886-3986-bb3d-492a98819358 | -3.48009 | -53.4906 | 2024-11-11 04:18:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9edf8b49-9912-3277-acc3-24c76df7a7c6 | -1.4021 | -54.50153 | 2024-11-11 04:18:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a34ffdca-20b3-346d-97a0-8b830b9c5c6e | -2.75454 | -49.34825 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 561297dd-0593-3ea6-8c24-983e050c3eb1 | -3.02693 | -50.97137 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 2544ad73-6ccd-316a-a0ed-05bd63b52ef7 | -3.10881 | -45.97169 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0069f5ff-526e-3ce0-ab06-fb2aad9a0a4a | -2.8733 | -46.64692 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cbdc8b84-59b6-3710-953b-a8372e5b1612 | -2.39516 | -46.76147 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1f845edc-20eb-3c04-bf06-31ad34bf60a6 | -4.0698 | -43.95294 | 2024-11-11 04:18:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 855c43e3-aa45-3990-982c-c0257380f258 | -2.8425 | -46.62268 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7de151c-f8f3-38a5-b5d7-7ccbd79b67bd | -2.75518 | -49.3444 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f4666a9-2588-3e39-b940-93aecb4a8281 | -2.9782 | -45.83299 | 2024-11-11 04:18:00 | NPP-375D | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8ff1bd61-6407-36ee-9f09-bd8c28211b28 | -2.30336 | -48.5538 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8db1b4a2-339d-3914-8613-4dfeb0f83f2c | -2.36646 | -48.88545 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37478f6a-9249-37a3-9aac-4b126f10ffba | -2.37789 | -50.33449 | 2024-11-11 04:18:00 | NPP-375D | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2f9c4de6-70f4-3d49-b65d-52fef9ebb336 | -2.17397 | -48.32987 | 2024-11-11 04:18:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1f114c1-b4a3-37d3-adab-c5baa47fd349 | -4.5838 | -47.07623 | 2024-11-11 04:18:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 85bbb512-a6d4-3af7-bab7-003370fc96af | -3.32597 | -46.10212 | 2024-11-11 04:18:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| c1d6c35d-9d1a-302a-a527-7d74204fd6d7 | -2.59916 | -51.71578 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 36a3a594-bd82-3931-abeb-ebda7b5c283b | -2.34339 | -46.56562 | 2024-11-11 04:18:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfc240e0-1c8b-33d2-9661-8bda89a413b9 | -2.69575 | -46.81788 | 2024-11-11 04:18:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4f5bc63c-08db-3d17-aafe-336e4d4a1099 | -1.51883 | -55.00331 | 2024-11-11 04:18:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 678d82b0-f98f-3965-b10c-def841660437 | -1.64473 | -52.05192 | 2024-11-11 04:18:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a5334fb-5ee1-37ed-aa37-206c1b76c676 | -3.08734 | -51.0722 | 2024-11-11 04:18:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d771c6ac-579b-3292-938c-9e25d27cd07d | -5.37599 | -42.75755 | 2024-11-11 04:18:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b65a4652-62e5-3f38-a957-6c346bac578d | -4.81876 | -44.35327 | 2024-11-11 04:18:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5edb9e27-0c75-3e74-bb4a-349f77ea6325 | -5.37543 | -42.76119 | 2024-11-11 04:18:00 | NPP-375D | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 810e86c6-1e3a-3dce-ad71-b4e0b0ed38c0 | -3.95069 | -49.0033 | 2024-11-11 04:18:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af1bfb72-d959-31e4-9a1f-a7d34976d184 | -3.08984 | -49.59487 | 2024-11-11 04:18:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d645682-de72-3fcb-b812-dbb88cd15d0b | -1.34768 | -47.20992 | 2024-11-11 04:18:00 | NPP-375D | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c274adcd-5c60-3846-bbd5-6c173bd4117b | -2.47858 | -46.34776 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d601545-8eba-38e7-a04a-6bed650a036d | -2.95591 | -51.97165 | 2024-11-11 04:18:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70f6307d-f777-358c-91ef-3357a997cf29 | -2.10516 | -46.19828 | 2024-11-11 04:18:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7d78d08e-4109-3dfb-ae77-52dcb8d8912f | -2.65569 | -49.39571 | 2024-11-11 04:18:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 84f4600d-e98d-3b02-a6ac-a9ece6f906f6 | -3.02378 | -53.25154 | 2024-11-11 04:18:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README30.md)
