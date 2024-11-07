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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7637bda6-161b-33eb-96d1-b93d0050e684 | -5.34129 | -46.19535 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 55392898-eff6-3e52-81c9-94dd2b73a076 | -2.42956 | -53.66405 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 7e1845cd-e9c0-38bd-809f-f5d77100a4bb | -6.08511 | -44.71445 | 2024-11-07 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| c3c87f9e-7171-3c53-805e-4f8d86acf003 | -3.95706 | -48.16405 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| a3351330-8a74-3b25-8705-487399fa07e6 | -3.29309 | -50.07693 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| cdafc5da-8ffc-3e88-a134-aa4b1207466f | -5.97594 | -45.36377 | 2024-11-07 00:56:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 24.4 |
| 61481f69-b69d-37c7-b490-981df948281b | -3.59157 | -50.23489 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 21.8 |
| d1a50f5a-50e5-3110-b730-46f88f8d5bf1 | -2.43153 | -48.58725 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e15df38e-4dd0-3082-bb1c-8719e56907fc | -3.51419 | -50.47274 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| e6a35543-d008-358c-8547-34d446e1f766 | -1.94693 | -47.02536 | 2024-11-07 00:56:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4ace4d34-dc92-3b34-a475-cf4e3122f552 | -2.82903 | -48.46336 | 2024-11-07 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e7d86d12-c109-33fb-89bb-efb407e9d0d1 | -3.66821 | -50.2548 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 33.1 |
| 522ec849-bb05-32ce-9032-f5415ad79828 | -2.43279 | -48.59633 | 2024-11-07 00:56:00 | TERRA_M-M | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ea493dd5-5ef1-39ab-bd51-fbe5b00b7db1 | -4.49104 | -48.48452 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a29101f8-1449-365e-b443-71c2540e070b | -8.11702 | -44.42549 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 310494de-a6f2-3998-bec5-5885ee20af42 | -3.97721 | -48.17352 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| ca332411-f150-3110-ae0d-77c9f05f31d3 | -3.96692 | -48.16568 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8c5a2793-ea60-3277-9859-30881360fd11 | -3.48375 | -50.38475 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 68e0c4d4-5e2a-3a3b-941a-7bffd5c793e5 | -2.17326 | -46.44832 | 2024-11-07 00:56:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 3cda155c-5ff4-3f53-ace8-08a147b135d6 | -3.03162 | -53.27956 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 39.9 |
| db0fd9b0-34aa-3f41-821b-f28e93c69802 | -3.29512 | -53.11246 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 3fab6417-ab62-3f92-8d72-cede8ae1458a | -6.23534 | -45.31968 | 2024-11-07 00:56:00 | TERRA_M-M | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a260603a-233e-3e22-9861-52d0d034dfb9 | -5.0436 | -44.74531 | 2024-11-07 00:56:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 772f175c-c957-3a18-9d5b-e3c6bb8423a3 | -4.10765 | -48.5088 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f910a047-b8e5-3337-97ee-d46fb32eea2a | -3.56539 | -52.69361 | 2024-11-07 00:56:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| d1349887-ee4e-3207-b501-dd15a15e855d | -3.6251 | -50.20603 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5fb2b104-fbc1-3040-baf4-af99fa3de02d | -7.41866 | -44.79617 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 03ebc81a-3064-3c6e-83ba-7450f4c49f27 | -2.13209 | -48.74979 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 43463c85-e103-36be-9bc5-b4c188c06285 | -3.5741 | -52.16615 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 2266fa2c-1433-369e-ae2f-d531844a0b00 | -6.07439 | -44.71595 | 2024-11-07 00:56:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| ad05cd24-ea78-36be-9bd9-a3cab04f50f7 | -5.01949 | -44.35738 | 2024-11-07 00:56:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 129d2f21-f2db-38aa-ab5a-71e5a9144452 | -5.51518 | -49.1536 | 2024-11-07 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 811d7b86-85a9-3728-892b-9a14b4988ef5 | -8.09129 | -44.43444 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 9b672eb7-7272-3240-9720-d73305b5407a | -2.73681 | -54.82932 | 2024-11-07 00:56:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 00e51e57-ded2-392f-b2ee-f4821211b6df | -2.1922 | -48.32492 | 2024-11-07 00:56:00 | TERRA_M-M | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3b938898-2c41-3ac7-98a9-1e3dcbe205ae | -4.93591 | -43.63335 | 2024-11-07 00:56:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| ff4e8302-5a2d-3153-a2f8-5f6f64e5cd1a | -2.07336 | -52.03655 | 2024-11-07 00:56:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 88975783-ac13-36f4-8820-4f99928b1dce | -4.40203 | -50.6967 | 2024-11-07 00:56:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ede8151d-fcfc-3d5d-9078-6a91c4a882bf | -2.22753 | -46.8952 | 2024-11-07 00:56:00 | TERRA_M-M | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f39d05ac-f6eb-3957-a6b6-6291b1e3a704 | -2.4628 | -48.87668 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 576fa936-a1c6-3309-a372-98d70066a421 | -6.25624 | -43.56021 | 2024-11-07 00:56:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| dae27e26-a513-3411-af35-5be363858bed | -5.00005 | -49.89366 | 2024-11-07 00:56:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 68ae0d46-20a3-3299-a614-bf7f60daf2f1 | -3.10131 | -53.71584 | 2024-11-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| e61bada1-7ec6-3ec5-8861-145ebe056a0b | -4.51074 | -42.88574 | 2024-11-07 00:56:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 25.8 |
| b54ea8eb-fa89-3a0a-baf4-57eaa7809ba1 | -3.01337 | -53.42937 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 21fb4f7c-5a41-3030-b06a-97c1347e8bde | -4.1845 | -48.79776 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 586f83c4-4832-382c-b889-fd07dd1ae26d | -4.2973 | -48.62127 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 559df694-5ede-31e1-b757-8aaac7180d47 | -2.40896 | -53.63348 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 32fc2a8e-548b-3b3c-ab25-58e0cce3ead5 | -2.82939 | -52.91526 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| ceecbcd5-2f9c-39bb-a5d1-594ea1b5a74b | -3.71512 | -48.99409 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| cf91d0a4-9009-3a4e-8c30-e65e3a73ed87 | -2.03344 | -46.98481 | 2024-11-07 00:56:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 645e6caa-bb71-34b2-915c-3f26997115d1 | -2.76908 | -53.22176 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 507920a8-52af-3edd-b6da-59399f81097a | -4.88419 | -47.42389 | 2024-11-07 00:56:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca302f19-4436-3a4f-a2de-0956c63dd622 | -7.11171 | -47.85714 | 2024-11-07 00:56:00 | TERRA_M-M | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 5978ba56-72a5-34f6-a450-b1c87bcb6341 | -2.67172 | -48.65495 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d1e63437-fc05-3604-8078-6dc1bd6d7567 | -2.44015 | -53.66248 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| acdb5082-ecba-3171-88c1-0bfd828f3f53 | -4.38021 | -47.23697 | 2024-11-07 00:56:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f4aac72a-e764-3c15-91e6-cd96f059de84 | -6.96683 | -39.81608 | 2024-11-07 00:56:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 26.3 |
| dab3369f-cae7-3840-aa51-c52ed6968dd0 | -5.50634 | -49.15486 | 2024-11-07 00:56:00 | TERRA_M-M | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 38e638fd-65f5-3a30-81e2-5bce67e4031a | -4.60425 | -48.69824 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| a0541e28-2c4d-36b1-a629-ce32929fdc08 | -5.40197 | -46.91392 | 2024-11-07 00:56:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 804ca253-5148-3b1f-86c3-12077fb9c87a | -7.256 | -48.42233 | 2024-11-07 00:56:00 | TERRA_M-M | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1b59b892-0070-3f8d-8aec-418ae1aaed22 | -3.57019 | -50.54209 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| e3c2f5aa-c8d9-3d2b-9056-bc811762c42c | -2.93179 | -52.54143 | 2024-11-07 00:56:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 06bade99-eef5-3203-9fcf-dd4a511b9196 | -3.97979 | -48.39238 | 2024-11-07 00:56:00 | TERRA_M-M | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a8b8fc12-afd4-38a8-bff9-11d6bf0b02cc | -2.92299 | -49.59836 | 2024-11-07 00:56:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 3fa26710-0570-3d10-8272-4f7d0da5d0e1 | -6.17809 | -46.33866 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 600f114a-04d1-3719-bd17-b2d75986591e | -3.65805 | -50.24707 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0bb49f38-bfd5-3c6b-908c-418299af348d | -2.87769 | -51.46917 | 2024-11-07 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 859237df-1ee3-3124-964f-790a1afe3ab0 | -5.37186 | -46.2683 | 2024-11-07 00:56:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 28.4 |
| 06c5e0a4-082d-3e94-ad67-d0ad2afb7b05 | -3.18028 | -50.59017 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0522bad0-f535-3954-bd64-afec0a804e0b | -3.62262 | -50.18809 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b783abcc-5f25-3f78-9c3e-14fb2805509e | -2.88626 | -48.74065 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a38d776f-f219-3377-888f-bd697a48b37f | -3.65971 | -52.33609 | 2024-11-07 00:56:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| fa8daec2-e967-3427-b741-84a2a0db3fb9 | -5.55312 | -43.6982 | 2024-11-07 00:56:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| ccf76ff1-4d75-3eb7-bcca-eef040cd60fb | -2.53588 | -47.28762 | 2024-11-07 00:56:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 27d8627b-e4ff-3197-b95f-0481892b00d1 | -4.66553 | -46.34396 | 2024-11-07 00:56:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 672a2fe3-8122-3d45-8bb1-73d947d9b1f1 | -2.8013 | -49.78909 | 2024-11-07 00:56:00 | TERRA_M-M | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f9520e9e-97d4-3b5c-8db3-a248149aa7ce | -3.33212 | -49.03399 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| b4be60e2-7663-38cf-8eb1-70c7e005b84d | -8.11503 | -44.41259 | 2024-11-07 00:56:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e898c123-0085-3032-ae95-4ac6f5d51172 | -8.49651 | -42.08387 | 2024-11-07 00:56:00 | TERRA_M-M | CAPITÃO GERVÁSIO OLIVEIRA | PIAUÍ | Brasil | 2202455 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| ad164cec-9dd6-39ba-afd0-9803765a5861 | -3.58141 | -50.22719 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d349a5a2-3567-3224-b9e9-bb589d00a0a2 | -3.78266 | -50.14435 | 2024-11-07 00:56:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 38550986-f163-3db6-abfb-0e46a80b1745 | -2.93716 | -54.12248 | 2024-11-07 00:56:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a03a9326-f412-3950-932b-f81a05dc064b | -4.59073 | -48.47317 | 2024-11-07 00:56:00 | TERRA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| f3a0974c-bc8d-3478-8472-48eb00d19b18 | -3.97072 | -48.12779 | 2024-11-07 00:56:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 231dbf9f-e8fa-3ffe-b28b-a1d6d64910aa | -2.89795 | -48.62899 | 2024-11-07 00:56:00 | TERRA_M-M | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 06e0bc58-68c9-36a7-bc42-d2ec8a0fb3a4 | -2.6082 | -51.77176 | 2024-11-07 00:56:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| ee87acf5-e08d-3f3b-a4a8-eeefc9663a14 | -4.70957 | -43.80416 | 2024-11-07 00:56:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 8ffdbb58-ffb6-3848-8e15-e65470fb0d4d | -3.00424 | -51.44511 | 2024-11-07 00:56:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b744261a-7c21-343d-8c3c-e1329732c7f0 | -3.80427 | -52.19259 | 2024-11-07 00:56:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8be71e3c-9e7b-31e9-aed4-9e683ba209aa | -3.20532 | -49.23788 | 2024-11-07 00:56:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 94136158-5ab0-39b7-b610-ce3eab53c793 | -6.96684 | -39.84028 | 2024-11-07 00:56:00 | TERRA_M-M | ASSARÉ | CEARÁ | Brasil | 2301604 | 23 | 33 | nan | nan | nan | Caatinga | 36.6 |
| a7359413-6b65-3a4a-9dad-0716cb1ba50f | -5.4443 | -43.58768 | 2024-11-07 00:56:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 71.0 |
| 7661bf78-2a65-3a05-8d7f-4e7a377567f4 | -3.24832 | -53.36576 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 9d905741-9ffc-3917-bba3-e5ae784a8c6a | -3.08848 | -53.89029 | 2024-11-07 00:56:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 90f0db48-a56d-3fe9-9f37-5db73ac99c72 | -2.43133 | -53.67719 | 2024-11-07 00:56:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| fd3199ee-551b-323e-b21a-f2b35c7ab21b | -6.72758 | -46.96455 | 2024-11-07 00:56:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 350e80ea-5b3e-3b52-9f2e-dbf0b1548c16 | -3.00592 | -53.24555 | 2024-11-07 00:56:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 193fff90-83f4-3445-abaa-b10037c9286b | -4.42735 | -47.25384 | 2024-11-07 00:56:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |


[Clique aqui para ver as próximas entradas](README12.md)
