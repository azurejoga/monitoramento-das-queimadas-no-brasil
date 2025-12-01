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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 26414bc1-0900-30d0-8b31-c3d958c89afb | -3.56968 | -47.17838 | 2025-12-01 04:25:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 95bdac30-7e2c-393c-ac9e-b3d091cda989 | -4.14423 | -43.72798 | 2025-12-01 04:25:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82a945e5-6e2c-35b6-b373-1adf042061af | -3.44839 | -50.15903 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ca7d31b6-7c8c-3960-9f4b-d7c2716f11a4 | -3.2623 | -48.57084 | 2025-12-01 04:25:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4016ef24-018b-3bed-befa-5a0c76806780 | -5.70749 | -45.63229 | 2025-12-01 04:25:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3a332055-d6fb-39bf-ba31-ec0833f81be7 | -2.04577 | -52.10835 | 2025-12-01 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 43a9e945-9f4d-3833-8dff-54e19b97c5b2 | -2.51089 | -49.09751 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b1ec965a-4997-337f-84ac-d6f0c660dea9 | -3.60375 | -47.26849 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 4190a558-10cd-3037-aff1-a66e4dd3c4b9 | -4.37866 | -43.33886 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| edb2f8a9-86e4-3c86-bda6-952af6113ccd | -3.28368 | -50.50723 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3f7e2df8-074a-38d8-90ef-48dd4fdad9b1 | -4.39097 | -43.3288 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 32.0 |
| a2f6d0bd-afdb-36a3-a6de-677d1f44cab0 | -2.44468 | -47.08005 | 2025-12-01 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 069559a3-0782-3b47-830f-cfc04ed3d3ba | -2.81391 | -48.25014 | 2025-12-01 04:25:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c50e3f7-f520-3fa5-b2a4-8743fc0bf506 | -3.70715 | -45.90733 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9145bc27-4efc-3c7b-92fc-ab97dac26aab | -3.59362 | -47.26686 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 82cfa701-ab5a-39c8-a893-aee87a590999 | -5.49625 | -42.16557 | 2025-12-01 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d0071515-120a-317c-8bd4-2a7950de37c7 | -3.25032 | -50.68774 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 67ff7d2c-8ce9-3773-ab35-36c9deef8362 | -7.7428 | -44.18663 | 2025-12-01 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 753d9c9a-a665-3258-ba8d-d3c7aad59875 | -3.29422 | -50.24323 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3ad65f4d-6c2f-3196-b1cf-a9a884f74488 | -4.37073 | -43.15349 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 3f1991ee-abe1-3d87-aaea-d7a0283ee846 | -5.7505 | -40.81695 | 2025-12-01 04:25:00 | NOAA-20 | NOVO ORIENTE | CEARÁ | Brasil | 2309409 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 892dc70f-59bd-3cad-8b6e-85859487abbf | -5.49555 | -42.17016 | 2025-12-01 04:25:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 02e9c15c-5752-364c-981b-02af1db68442 | -4.31061 | -45.37807 | 2025-12-01 04:25:00 | NOAA-20 | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| baa194da-919e-3934-a5a4-0a791669474c | -2.94005 | -40.09798 | 2025-12-01 04:25:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f729f15e-9455-3acb-8b57-3a6ad4d9d3bd | -2.79844 | -45.22921 | 2025-12-01 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| caeea472-e866-3e61-b862-39aa26bace95 | -4.38507 | -43.3439 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c4e065c-5998-3312-9254-ac4ccbbdd6e8 | -5.52019 | -42.5921 | 2025-12-01 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1f720f39-fe64-3fa6-945a-cb954123f2f5 | -3.70581 | -50.65519 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b024ebfb-36a8-304c-ba9e-ab7da9eb629a | -4.39448 | -43.32935 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| af67c3e7-5e7c-3458-9e5c-69724ad23479 | -3.47812 | -51.3652 | 2025-12-01 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 49673d13-5579-3a5f-af61-d1ae9fec2db5 | -4.22524 | -45.53058 | 2025-12-01 04:25:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9292126a-850f-3dac-8c79-4057b5a0f3d0 | -4.39508 | -43.32544 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99bab93c-c7dd-37bc-96f2-fffaebfec923 | -2.97445 | -49.63713 | 2025-12-01 04:25:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 91664b44-4aa1-3c3c-8ada-ca5a47e433b2 | -4.38978 | -43.33662 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3990a976-c4c8-3286-80dc-6372df619dfa | -3.57834 | -50.27554 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 334267e8-56d5-37b8-b911-8211aed5fb2f | -0.6487 | -52.36659 | 2025-12-01 04:25:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9f621751-10c1-392e-8d3f-6765602c4b42 | -3.93779 | -45.84531 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bc194605-e5fb-3590-9dd1-f45c6f62628c | -3.13184 | -50.2542 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d0971ac-d4d5-36a0-8c88-3d3d09ea5c26 | -5.33419 | -43.56982 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| c7f75d72-b8c3-3ade-965d-ebe6368891a2 | -3.70439 | -45.90338 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66236c3d-ad9e-3590-84f4-c95bab5e3d54 | -6.30972 | -43.8116 | 2025-12-01 04:25:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 37b5054f-21fd-3ca8-99ee-9dd0f9ce96f6 | -3.59999 | -50.31466 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 585fc696-28fc-392f-b6da-a0810691a4f4 | -2.26468 | -45.70491 | 2025-12-01 04:25:00 | NOAA-20 | PRESIDENTE MÉDICI | MARANHÃO | Brasil | 2109239 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df1b8880-cd98-338d-9200-43aa89521294 | -3.23138 | -52.85103 | 2025-12-01 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 572b4136-4da1-33bc-a075-1772ebf85819 | -4.60137 | -45.21422 | 2025-12-01 04:25:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8c0b9d89-7c38-3057-a682-7508a0ecd542 | -4.3672 | -43.15294 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c57fcd7-10db-3a40-9142-460b872c1da4 | -2.84869 | -45.62078 | 2025-12-01 04:25:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b9527bc-9259-340a-96a7-f847a4b4c054 | -3.5052 | -50.55445 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 904ac262-a62c-3861-89f0-b65c0c5d8edb | -3.47391 | -51.36454 | 2025-12-01 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 55a553eb-0737-3de8-94fb-e1639c49ec48 | -2.63374 | -48.54002 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3d399179-fe07-38bb-8b0b-7f0a4d5b5fcf | -7.74339 | -44.18273 | 2025-12-01 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 97d22e79-59e3-3024-b01b-d021ca3488a9 | -3.11142 | -54.17428 | 2025-12-01 04:25:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5fb25619-17c1-3cfb-91ec-b65022185676 | -2.04125 | -52.1076 | 2025-12-01 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ccf2a18-7605-3f85-9eeb-9ad486ee127b | -2.4291 | -45.73774 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60f03285-b99f-314e-8631-a8cbecb08dac | -3.20345 | -50.7713 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ea66b5af-4d1a-3e43-a94c-e16a44059f1b | -3.26652 | -51.46876 | 2025-12-01 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed5dea06-75a4-3481-aac7-3fd05aa179c6 | -2.84484 | -45.62369 | 2025-12-01 04:25:00 | NOAA-20 | SANTA HELENA | MARANHÃO | Brasil | 2109809 | 21 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b2e9af20-6c2d-3bb4-88b4-f96cebda4bc2 | -1.73764 | -46.87109 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f7264ebd-76d1-3a6e-92e3-31adb7b89ddc | -2.51272 | -46.00473 | 2025-12-01 04:25:00 | NOAA-20 | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de436140-3b6a-395e-bb5c-212b0576b288 | -2.35114 | -48.62504 | 2025-12-01 04:25:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9580deee-76f2-3f49-b6d6-e4da928c06f5 | -2.44411 | -47.08367 | 2025-12-01 04:25:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7e430c44-7634-3de8-9d90-7302b74b8c81 | -5.87022 | -44.50243 | 2025-12-01 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b5c8d5a-92ed-318d-b584-91cca2a8d531 | -3.711 | -45.90442 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.9 |
| df6f9eab-de65-3aa9-a37b-1bc0f29c7124 | -3.24916 | -50.69487 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3fa6f307-fb85-37c2-ad8a-28e232184999 | -3.1322 | -45.82735 | 2025-12-01 04:25:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6db26200-8475-3a11-94db-90c82cf29ab9 | -3.47328 | -51.36841 | 2025-12-01 04:25:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 506a497e-2a2d-3b36-914e-916c8d07e1c0 | -4.6283 | -43.26691 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bb2e361-99d8-37bd-81fe-aedd0f201137 | -2.3361 | -50.35659 | 2025-12-01 04:25:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9b26c8c9-b365-34ae-a1df-267a2b8e9c23 | -3.39253 | -50.256 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b0e0cc7-d2ab-3d88-8cfc-b985da79da6e | -3.03742 | -50.24171 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fba379d0-1fa2-3ee3-8683-699b6f34073a | -4.18976 | -44.76253 | 2025-12-01 04:25:00 | NOAA-20 | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9710260b-55d7-3b26-b6bc-f037301f4738 | -4.37365 | -43.15799 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eeb715ce-bd02-3ff0-8a1b-9795bdfecb4a | -3.85241 | -40.97647 | 2025-12-01 04:25:00 | NOAA-20 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 2163b416-3155-3c4c-bfa0-fda0c0bc138d | -3.9514 | -44.76567 | 2025-12-01 04:25:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4f67a50b-e308-3325-8e66-e0d46e696cb8 | -3.88666 | -46.51236 | 2025-12-01 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a7161385-5803-35d7-a613-f4c6b3c0de2c | -2.95527 | -49.15321 | 2025-12-01 04:25:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae972d0-654e-34cb-b236-2b91d32e8c35 | -4.36658 | -43.15691 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 971e64b8-e8ac-3f06-97ed-8f00ab3e51cd | -2.07192 | -44.79361 | 2025-12-01 04:25:00 | NOAA-20 | MIRINZAL | MARANHÃO | Brasil | 2106805 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ef9b58e6-f958-3f22-bb8d-bc6b7641d4fb | -3.7498 | -42.95836 | 2025-12-01 04:25:00 | NOAA-20 | BREJO | MARANHÃO | Brasil | 2102101 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7715c4cb-2216-30cd-81e7-fbd33e24530f | -2.24426 | -45.61683 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0c7d4454-095e-3050-80c8-301d7e5b6374 | -2.91941 | -45.2799 | 2025-12-01 04:25:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f215546d-667a-3e8b-ba8b-243a620503f7 | -3.94055 | -45.84926 | 2025-12-01 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0f900e83-d748-3f29-83dd-4b8188ac1f06 | -3.5998 | -47.27155 | 2025-12-01 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0c9e8587-b607-39d4-b05f-1f20d1d739e6 | -2.2579 | -46.4531 | 2025-12-01 04:25:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 574ff99e-c3f8-312a-af66-df61ea974d33 | -5.52623 | -42.60194 | 2025-12-01 04:25:00 | NOAA-20 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fa69558e-62f6-3210-90aa-b0a4c840a8be | -2.87112 | -48.70152 | 2025-12-01 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 548ad7dc-1925-389e-906c-ef5b4e09adc7 | -2.95119 | -41.74755 | 2025-12-01 04:25:00 | NOAA-20 | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| c2c66a8e-491d-3d7c-a344-4a3039084224 | -2.73582 | -45.21552 | 2025-12-01 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1b88961c-eb3d-376f-b5a8-6af8ad090d9e | -2.24481 | -45.6134 | 2025-12-01 04:25:00 | NOAA-20 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de7f0f45-47db-32c7-9659-dc107aef327a | -5.32777 | -43.56489 | 2025-12-01 04:25:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 4d246383-ceac-371d-9e0e-df5e272bfacf | -4.38134 | -43.1551 | 2025-12-01 04:25:00 | NOAA-20 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 155bd8e7-799d-30fc-8723-b2303478f6cb | -2.04199 | -52.103 | 2025-12-01 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 043c9022-0273-32bb-8e2c-2afd1a10fe51 | -3.38862 | -50.25535 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7de520eb-d767-3928-ac02-4c5040bf4f33 | -3.71046 | -45.90785 | 2025-12-01 04:25:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b588018e-eedf-30fa-b6f1-a2e3d1767ee8 | -3.23189 | -50.67389 | 2025-12-01 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e350be2-4556-356b-a365-114e71937d8c | -3.58431 | -40.43295 | 2025-12-01 04:25:00 | NOAA-20 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 274c3763-3abd-3894-b2c6-b41575c878e7 | -3.32802 | -45.63983 | 2025-12-01 04:25:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 27e0e4bd-06cf-320c-b5a2-beda877d64cd | -3.79606 | -51.20062 | 2025-12-01 04:25:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1b6dbc20-8876-3197-8dd0-f49aa9d1005b | -3.13165 | -45.83078 | 2025-12-01 04:25:00 | NOAA-20 | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7992661-46e9-39bc-8843-483a8457bd7f | -4.38277 | -43.33551 | 2025-12-01 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README14.md)
