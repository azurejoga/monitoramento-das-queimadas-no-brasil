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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1486c3de-5c86-321b-bb35-98e8eae9788f | -6.56577 | -44.03732 | 2025-11-26 04:21:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9e5ce20a-8f07-3e25-8325-38cd7678da85 | -5.60739 | -35.63665 | 2025-11-26 04:21:00 | NOAA-20 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 2ede73f7-8604-3258-af29-d05135fa39a9 | -4.25281 | -45.12951 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35968ee5-667e-3a17-a289-1ffdaa03d9ce | -3.89879 | -45.72432 | 2025-11-26 04:21:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e7390a8-f78f-3777-8a71-d124540b7b58 | -4.90882 | -43.79563 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e4261b8c-025f-3a12-b1a5-cfe070b16b41 | -4.5622 | -43.29844 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3c9980ac-d575-338a-acf0-d2031e054d96 | -4.71664 | -47.15953 | 2025-11-26 04:21:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0bb0f7cd-a1f4-3134-b368-e94fd7d39ff2 | -4.60106 | -44.412 | 2025-11-26 04:21:00 | NOAA-20 | LIMA CAMPOS | MARANHÃO | Brasil | 2106003 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2c7f64df-319a-362f-88b5-ec4264ff54a0 | -3.36786 | -49.25533 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5afaea46-b3d9-30e9-88c7-56353cd87e4f | -7.50899 | -45.72306 | 2025-11-26 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de117306-4e2a-35a2-9fbc-9afb4992ca0e | -2.50383 | -47.82469 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 6ac11580-7980-36b6-b997-84161d1e6b14 | -5.35219 | -44.88404 | 2025-11-26 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e67a97cb-0886-3e48-81e7-194cbd4bc4d6 | -3.34775 | -49.77361 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7dafc0a2-a5e7-3d88-ad37-37cce80d676b | -7.01585 | -45.16983 | 2025-11-26 04:21:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f20e713c-51ec-3ce2-87f2-24ec3eebba59 | -2.89652 | -49.53764 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5cbec121-4fe2-353a-8a48-58a2fa24f01d | -3.67358 | -43.5706 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1493fc16-5e20-36d5-aa37-037b13814c72 | -2.47914 | -47.83192 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 69f27b75-eb3a-3b6c-a44e-a61ae82636dd | -7.47809 | -42.75159 | 2025-11-26 04:21:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0ca313bc-e113-3ff8-a57c-d55e30572ab6 | -6.04042 | -45.83473 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c7073625-7e1d-3380-9a24-8e51ff009e0e | -10.20857 | -36.367 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| c35963a3-e387-3553-90f2-2299ac8227e8 | -4.0536 | -48.82364 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 00e3189f-98ce-3725-a5c0-00b02f3dc5d3 | -2.88678 | -51.81773 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 399aadbb-97f7-3f2f-b6b4-33db8d25ff19 | -4.65571 | -43.97952 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2cd4ca92-78b8-34cd-8bc9-9585f5874621 | -2.86774 | -48.65458 | 2025-11-26 04:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a71a1295-1533-34ba-ae00-e259666b1301 | -3.24162 | -50.59543 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 99f74f84-b61b-3c7c-b08e-f743d8f606e3 | -8.0547 | -43.12366 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.6 |
| a49eb88f-ecfe-3469-82fb-3ba42ee671fe | -2.72772 | -45.21063 | 2025-11-26 04:21:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 93c02b3c-b441-3cf9-a959-d8d6449968f4 | -4.27 | -45.12864 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e05544ad-cac6-3f83-aab4-953836f958a3 | -8.04556 | -43.11457 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 8e194039-af63-3232-a9b0-2e1f22137c45 | -5.64208 | -47.8579 | 2025-11-26 04:21:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7b2aeb2b-e62a-3516-98a1-f41092eaadb6 | -3.44008 | -50.18754 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d2091f1-7cd0-3364-8d05-2fd88b85f71a | -2.90851 | -45.48463 | 2025-11-26 04:21:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d6b8e6c7-0480-3949-b72d-b9281129b8c7 | -10.21437 | -36.3643 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 69.8 |
| f35f72c2-4811-34c2-a341-e3f5fe7783c3 | -3.67082 | -43.56663 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 54ca12b9-1228-304e-8de0-3895e7e2d571 | -4.16531 | -41.61561 | 2025-11-26 04:21:00 | NOAA-20 | BRASILEIRA | PIAUÍ | Brasil | 2201960 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 7ce2f67a-3c86-3fcf-b3ef-28a638e4848e | -8.04956 | -43.13435 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 06b5999d-0800-335b-8c40-28552171bcd7 | -5.08402 | -44.81673 | 2025-11-26 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bc5ee67c-ca2e-3459-88fa-07adb218f8ca | -8.05298 | -43.13488 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 9a36ebf5-a705-388c-b748-ab73256011a8 | -5.45593 | -44.82967 | 2025-11-26 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2f239c16-30a4-3370-9325-f00f075c435d | -6.29791 | -43.79482 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8b5bda7-3078-339b-af37-8ea1464c4495 | -3.67027 | -43.57008 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 769bada5-f3b8-3628-a7fa-66fea46a8205 | -2.73575 | -49.06522 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 158631f1-67ef-3c0f-8915-166d1c105605 | -6.27872 | -39.68801 | 2025-11-26 04:21:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cef0bda9-15c3-38f5-b1e5-d7d69469f348 | -5.41432 | -41.08071 | 2025-11-26 04:21:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c76d6c4b-dbc7-3920-ae64-1bb4531cbaf9 | -5.25544 | -44.14128 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7a0cbf85-9561-3509-865c-bf1897b3e616 | -5.50245 | -45.28498 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2f9a8535-0785-3240-b9ba-ce8915aa5ea4 | -2.40615 | -49.35171 | 2025-11-26 04:21:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27a2d464-935b-3773-a5f4-70bb8483588b | -3.7032 | -45.89069 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| f7dcf72d-7ab2-32b9-858a-861c55e63943 | -6.58293 | -43.86387 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 06e28d23-17cc-3ef4-b300-208e30c2d4ee | -4.56406 | -43.80558 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2ceac639-ee82-349a-9b54-f3118cf41428 | -6.08364 | -47.04821 | 2025-11-26 04:21:00 | NOAA-20 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 525dd70d-0171-3a94-b846-b2c07f79b177 | -6.51927 | -37.79977 | 2025-11-26 04:21:00 | NOAA-20 | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4a16039f-7a98-32b4-90ba-dbd356e30b48 | -2.94189 | -49.36319 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3332f23c-5ab4-3cc3-9303-87c5515c14f0 | -6.83757 | -39.05412 | 2025-11-26 04:21:00 | NOAA-20 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3c8c384e-33f6-3bd9-a14e-7dc722944c7b | -3.70602 | -45.89488 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 28ba6baa-db0c-3c22-aa7e-c9b54ef60e72 | -4.16997 | -43.71904 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 0f555bd5-d697-3953-a975-57d16fe6caf0 | -3.48834 | -44.5078 | 2025-11-26 04:21:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 24072ff2-c762-35dc-a75b-74ddd841e274 | -4.93932 | -49.9255 | 2025-11-26 04:21:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6254a522-5a12-3a76-a260-6b48fc4578f2 | -8.06327 | -43.13644 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 73b5df53-4049-3035-b6bd-8e1b1b6e269b | -6.67314 | -42.47787 | 2025-11-26 04:21:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 06881276-75a3-37a4-9cd8-dabf59ee1cf6 | -9.1363 | -44.40641 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8800167d-72a1-3d14-b6fb-f71e1a75d923 | -6.72782 | -42.52731 | 2025-11-26 04:21:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c24df21c-0909-3860-9dfe-521db701c645 | -8.07415 | -43.11128 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 07e76ba7-adc9-3258-9b6b-7a1a498ec4f5 | -6.31232 | -43.78991 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 84d5101a-6276-3a48-aa6b-9b6af5bd95b7 | -4.65348 | -43.9721 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 944d794b-9ac5-360b-bbe9-a33d4fb9d81a | -6.76367 | -46.51368 | 2025-11-26 04:21:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 97410749-512f-38c1-93a0-fda4be67a446 | -4.82642 | -43.82208 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2772dd32-e0e0-3259-b008-799b6e5864e8 | -5.57262 | -44.9724 | 2025-11-26 04:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 47f4bf9a-84f7-3085-9fb7-0729034ec8cb | -8.06157 | -43.10167 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| dd65eef2-ff95-361a-8eb6-918168b45f87 | -4.16943 | -43.72249 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 54542e4d-2a33-3cfb-a16a-e02d5c2c4a8e | -6.76706 | -46.51423 | 2025-11-26 04:21:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7add8b5b-3fab-34b7-a050-967388836287 | -6.05906 | -43.25615 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 4dffeff5-2fbc-3e68-9e0e-7f84c29efea0 | -4.69132 | -43.88248 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d441891e-7d0d-3e71-8402-a3e20fa84809 | -6.58524 | -47.9064 | 2025-11-26 04:21:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 19cce7ba-8fa2-3d6d-897c-ced3beb6d0c0 | -6.04335 | -42.99118 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 60db6c0b-6d6a-36f2-9ac8-d87dc13517a6 | -3.98079 | -49.28427 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0f97b442-6006-3d59-bbea-b33bbab53aef | -4.23341 | -40.39112 | 2025-11-26 04:21:00 | NOAA-20 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7f0e8379-303c-3780-9de8-b4451e0b7a88 | -4.2431 | -40.67446 | 2025-11-26 04:21:00 | NOAA-20 | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c76c5897-6bf7-32d4-a4d8-1e8239e9b5ed | -4.2224 | -48.37236 | 2025-11-26 04:21:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 557db724-79d4-33e9-ba79-4cbc9709cf86 | -4.65901 | -43.98004 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34545393-ea81-31f5-9775-06b9b1ea2635 | -5.22092 | -44.78922 | 2025-11-26 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ea9d7c7b-848e-32a9-88af-4dd825ada093 | -4.72655 | -43.33133 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17ba9c17-9153-306c-9cdd-4ae7fd3f7925 | -2.71385 | -45.69552 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 634f3b53-e896-36f4-b880-1578b0c5e49e | -5.64137 | -47.86216 | 2025-11-26 04:21:00 | NOAA-20 | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc53e81d-8452-329e-957a-f1c4ca045f6b | -2.7876 | -45.51718 | 2025-11-26 04:21:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 08824717-81fd-3336-b958-859cb2269a65 | -8.04327 | -43.10654 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 491a55ad-76f5-3800-934c-d0c4c0941cb7 | -7.7468 | -44.19338 | 2025-11-26 04:21:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 8cbb7800-c523-384a-baa0-0eb1f1922f64 | -5.03057 | -43.25871 | 2025-11-26 04:21:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f321b636-e655-36f8-8e4f-fe23d892b99a | -4.05725 | -48.82584 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4e74f337-2578-37f5-ab25-049c387b93fe | -3.46945 | -43.4214 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 20816a43-8998-323e-bed7-5ae135caec1f | -8.06213 | -43.14389 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0d7f6584-131f-30ed-bebb-012c490df159 | -2.71503 | -45.68821 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d409f0fa-c6eb-3807-8882-68fa1361579a | -3.70941 | -45.89543 | 2025-11-26 04:21:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c95de872-d65b-3d03-8a55-d7b4422a37b7 | -4.96903 | -50.87245 | 2025-11-26 04:21:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d25099d0-0f8c-3800-9cbd-6a00f9d3a627 | -8.04384 | -43.10278 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 57cc796a-8e6c-30ae-a48c-6aa424bbd18b | -4.91416 | -44.66582 | 2025-11-26 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 51befee4-9fb4-3ca0-acbc-9b6117b3b4ba | -7.56305 | -45.87548 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5d09b646-6e18-3f1b-91fb-4917727d3286 | -2.15735 | -46.08399 | 2025-11-26 04:21:00 | NOAA-20 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ff24415a-4c63-34d4-a93e-f7c09a47f71c | -4.26113 | -45.12009 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8cc3f428-3e85-378c-93fa-6f0f24b64d1e | -4.49549 | -43.50674 | 2025-11-26 04:21:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
