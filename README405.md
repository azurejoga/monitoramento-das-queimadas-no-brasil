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

## Dados Diários - Página 405

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3f143558-c726-3b84-80a6-6b0cc062a6dd | -10.7666 | -46.616 | 2026-10-08 19:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 79.4 |
| 02ccff45-583e-33a6-8c52-00aec7ad83b8 | -3.2956 | -53.6984 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.4 |
| fc3fc46d-5748-37a2-9d9f-803f36e5ddf4 | -11.619 | -43.6196 | 2026-10-08 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 206.7 |
| 3d3e48b3-c66e-3337-a87f-6d5eb9e12789 | -2.5675 | -58.037 | 2026-10-08 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 9c62deff-9f57-3415-9d9f-707ca87f5ab4 | -3.8383 | -55.9774 | 2026-10-08 19:20:00 | GOES-19 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| b0b09437-1b07-3acc-96a3-3a568a67bfa7 | -6.1429 | -47.9432 | 2026-10-08 19:20:00 | GOES-19 | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 41cb9f41-ac58-3e85-a38b-d25cff42ec27 | -6.4905 | -55.9563 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 317.2 |
| ecaf7de8-c8c6-36eb-b0d5-98facbcca41e | -1.8233 | -54.9307 | 2026-10-08 19:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 49.2 |
| e072c92b-1c7f-3c01-bbaa-f997d9995a8e | 1.7672 | -55.5463 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 73.5 |
| fb526c94-399e-319d-853a-afbd712f2988 | -6.0386 | -51.7261 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 86.2 |
| 38868791-45f3-330e-88f3-2f19be2225ec | -3.5234 | -44.3267 | 2026-10-08 19:20:00 | GOES-19 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 89.3 |
| c9d4407c-37c0-3b20-a130-be91ce104362 | -5.9835 | -40.9367 | 2026-10-08 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 158.8 |
| c0665a24-241e-3220-a027-e70e021e34d3 | -5.2352 | -56.109 | 2026-10-08 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 3b1daae7-f453-344d-9b35-376fc44ed233 | -14.4345 | -43.9157 | 2026-10-08 19:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 3d354272-1114-3cc5-b014-87028d207fc5 | -6.4764 | -55.3004 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 157.5 |
| 496f72c2-93e6-312b-ac65-b63001176566 | -9.9007 | -44.8608 | 2026-10-08 19:20:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 688.9 |
| 9e37678b-9198-39b3-9991-a921172f53f6 | -15.1248 | -43.6369 | 2026-10-08 19:20:00 | GOES-19 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 95.9 |
| 5bdfa386-0486-39e9-9965-53d5f42ada95 | -6.498 | -43.9501 | 2026-10-08 19:20:00 | GOES-19 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 139.8 |
| aafad835-5dbe-3ba5-8869-c30bcd230dc5 | -1.3264 | -56.4176 | 2026-10-08 19:20:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 8ac6ea30-9e6b-3739-83cb-e821531fe906 | -6.1615 | -52.6676 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |
| 6ab054af-8c42-3c19-a2c5-547dede363d4 | -5.9267 | -51.8151 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| 6ee2ef5d-a14c-3d76-87e8-fcb3ed8bab27 | -11.2478 | -46.2831 | 2026-10-08 19:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 280.5 |
| 66622fa0-2f21-302b-980d-00abfb3cd3bb | -4.7404 | -55.6522 | 2026-10-08 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 127.8 |
| f7a48a28-cc22-3ada-bcd0-08e4ff62abc5 | -5.3763 | -45.943 | 2026-10-08 19:20:00 | GOES-19 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 75cdc4e3-c2d0-3e48-939e-abbc81edbb84 | -14.0873 | -43.7671 | 2026-10-08 19:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 136.8 |
| 5a3872fc-9654-3873-92df-c532ff400527 | -3.195 | -42.9772 | 2026-10-08 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 43407139-7065-35b7-a33d-f12caab0fa58 | -3.2081 | -58.0057 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 202.3 |
| 4a62203e-ac0a-3518-b503-61e8f3d98aa3 | -8.2178 | -46.3844 | 2026-10-08 19:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 111.1 |
| 5488357c-9df5-3158-8a35-35611782551d | -5.9833 | -40.961 | 2026-10-08 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 282.9 |
| d1e8b0b5-3d62-37e6-a3c3-66c785c26786 | -6.3133 | -54.8084 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.9 |
| 3f4aa32b-4ddf-3dac-858f-b8af1f2935b9 | -5.9647 | -40.9383 | 2026-10-08 19:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 66be56ba-d1a7-39e9-91d2-f4496eaee5d5 | -4.6641 | -56.2281 | 2026-10-08 19:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 10a8ab10-4983-350c-82aa-fad5ea27b1de | -6.8762 | -43.7083 | 2026-10-08 19:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| bf814a00-54a2-347b-8431-043346e50769 | -3.314 | -53.6979 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| 1b2cc1c9-ce6c-3322-bca1-582feac5672c | -9.0173 | -44.3676 | 2026-10-08 19:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 127.8 |
| b18b1417-fe41-3ca9-b006-6a078316ab65 | 1.6937 | -55.6263 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 210.9 |
| ad648102-f693-381d-a084-db5d01a92f81 | -1.091 | -54.1803 | 2026-10-08 19:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| abb6f7c4-dad5-33b6-8ea3-73cc98b0753e | -11.7742 | -43.5245 | 2026-10-08 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 155.7 |
| aefca740-a50f-3774-8d43-4546f62350b5 | -3.1787 | -50.5807 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 158.7 |
| 59648a60-6613-35e5-8af2-922ad93efe4c | -5.0946 | -46.206 | 2026-10-08 19:20:00 | GOES-19 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 141.3 |
| c06fdae0-e058-3d95-8109-25a32785bc5a | -8.9772 | -45.9249 | 2026-10-08 19:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 195.0 |
| 0afbdc2b-e1fe-3b81-8803-832add5f9ae6 | -6.2541 | -52.683 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| f1dac857-b778-370b-94e2-56b697cb91d8 | -2.8712 | -54.1719 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 35a6205a-16cc-315f-b633-f50d4db0df96 | -2.8895 | -54.1915 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 98801455-d456-35c2-a4d6-a176b47f74f1 | -3.1879 | -58.6433 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 133.3 |
| d78e56e8-0335-36af-a541-93a7113743f5 | -2.853 | -54.1322 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 256e7f42-9b83-3d46-ae6a-bec4c4d9edf5 | -11.0754 | -44.0534 | 2026-10-08 19:20:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 189.5 |
| 896d537e-6a73-3a83-9512-3798d99415f3 | -6.2348 | -52.7866 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 183.0 |
| e89822ee-5d58-32f0-86f9-870475877569 | -3.0073 | -57.7772 | 2026-10-08 19:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 4a22c97d-ec0f-3014-8cb7-bddeee8e745f | -3.095 | -59.1832 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 5d01d001-4a46-3197-9ce6-03d75e4508d7 | -14.4339 | -43.9396 | 2026-10-08 19:20:00 | GOES-19 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 200.6 |
| da45752c-3413-389c-8fd9-73cff7f0bfda | 1.7488 | -55.5861 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 94622a50-0e4f-382b-a739-a1bd0794817e | -11.755 | -43.5275 | 2026-10-08 19:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 134.3 |
| 6099637f-918e-3439-92a8-f2e8a5f084ef | -4.1025 | -44.1149 | 2026-10-08 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 104.2 |
| 808f896e-c567-332c-8275-c2b551f47480 | -2.5903 | -56.1642 | 2026-10-08 19:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 79.5 |
| 2e13f003-cd98-3a32-85fc-2e84132a5024 | -2.8571 | -59.2641 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| 26531d35-4e7d-3514-a32a-a1c265a37dad | -2.0576 | -56.8786 | 2026-10-08 19:20:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| cab288ff-2e95-3673-85ae-4f69017c7f15 | -2.7428 | -54.1347 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 142.9 |
| bc5e7913-012a-33d9-b67f-71b589b21b8a | -3.2031 | -53.8621 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 2ac55d97-194e-3c2c-b6b9-dabd3ab2c7ea | -3.1697 | -58.6244 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 97.4 |
| 0fb203f0-94d6-3700-b24b-a9e378968605 | -7.0706 | -52.6764 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 131.4 |
| 0434a3a9-06af-3ba2-903b-c20071520552 | -9.0362 | -44.3654 | 2026-10-08 19:20:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 64.1 |
| e12c10cb-38f6-3c83-bd79-cf6a8a47c47e | -2.5492 | -58.0373 | 2026-10-08 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 197.1 |
| c6f49fab-2308-3c99-afac-bc1787a903b8 | -6.2355 | -52.6841 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 99.8 |
| e65f90b5-074f-3c64-bc55-fc8b90ce0499 | -6.3134 | -54.7884 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 0d3f06ae-4482-3a5e-892e-90eea5b683fc | -2.8163 | -54.133 | 2026-10-08 19:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 6b06be3f-a82f-36b5-b5db-369f3b3f09c6 | -3.2137 | -42.953 | 2026-10-08 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 307.9 |
| 6c688518-3b7a-3db4-abfd-86ee40ebe33f | -3.93 | -56.0143 | 2026-10-08 19:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 134.8 |
| 50c17f84-8aa8-3f81-81bd-a25496e110a9 | -4.1192 | -44.4119 | 2026-10-08 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1cf17c1f-7444-3cba-aa48-a788dfd7a8b7 | -2.9451 | -54.0497 | 2026-10-08 19:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 9c2b3e80-c3fe-32e0-b2f6-dd1340b1ce4f | -3.2136 | -42.9764 | 2026-10-08 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 255.3 |
| d3b3bd60-8fda-348f-a498-ce5f4fc80dee | -6.1371 | -53.5056 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| cf614135-5836-3c8b-b8bf-f60177df7ca4 | -5.9266 | -51.8358 | 2026-10-08 19:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 185.6 |
| 1eacee69-3da2-3632-b9c1-1c33ff2a7133 | -5.5146 | -42.8399 | 2026-10-08 19:20:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 88.5 |
| 33c96287-7951-370a-9049-e6f610cff1c5 | -12.1549 | -44.7314 | 2026-10-08 19:20:00 | GOES-19 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 141.4 |
| d6d59dcc-809d-3f3a-883f-fa3fb95e6f64 | -3.095 | -59.2024 | 2026-10-08 19:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 3a4727fb-0754-3d94-9e72-8af4fd40d1eb | -3.7817 | -41.6718 | 2026-10-08 19:20:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 129.3 |
| ae2c2483-3c04-37e4-9f69-d2c454153c71 | -15.4026 | -44.3207 | 2026-10-08 19:20:00 | GOES-19 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Caatinga | 285.6 |
| 83ca4882-c5ce-3a93-95c1-d0062fd31c75 | -3.8413 | -44.1283 | 2026-10-08 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 96.4 |
| 1bbabee8-c460-3cf1-a629-825f1a404b52 | -8.9775 | -45.9023 | 2026-10-08 19:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 184.2 |
| b979406c-0b9c-38e1-8b77-9cbf4692cdc8 | -3.1951 | -42.9538 | 2026-10-08 19:20:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 78.4 |
| 23ec9e15-183e-32ca-b7bc-26194ec04a18 | -2.5309 | -58.0376 | 2026-10-08 19:20:00 | GOES-19 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| f1603e73-6ee9-340f-b92d-c8d58b614622 | -14.4591 | -41.1854 | 2026-10-08 19:20:00 | GOES-19 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 139.1 |
| e11fb3fe-57db-34ab-bdfd-51d0706e996e | -2.572 | -56.1646 | 2026-10-08 19:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 132.1 |
| c07810cd-758b-337f-a015-f0d788875cbf | -3.4095 | -58.0013 | 2026-10-08 19:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.6 |
| ddb73bb1-479a-3129-bf3a-17f4128b74df | -4.1023 | -44.1379 | 2026-10-08 19:20:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 7ee30e4d-a9b8-3d89-b4b4-7fa70ae4021f | -5.7119 | -53.4658 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 395.7 |
| 765b218d-19bd-3223-9d7b-f81bae087f19 | -3.3912 | -58.0017 | 2026-10-08 19:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 4a302d0d-b58e-3036-a1cf-0e60a5a97272 | -3.1972 | -50.5592 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| a8e4d690-7840-33ca-bbfe-0e0e868c2cf9 | -9.7377 | -46.9621 | 2026-10-08 19:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 80.0 |
| b9e25df5-98d8-3b72-9532-bae920c354f6 | -7.1627 | -55.1247 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.8 |
| b3ef6ebb-c471-3ccf-8aa7-c70bb1f62923 | -6.4596 | -55.0415 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 5135cc2a-129b-373f-a562-8d5428911edc | -3.3637 | -50.4701 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 088a1974-a10a-3e88-8e27-36c837a974e5 | 1.7671 | -55.5661 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 96.7 |
| 9e3f5628-b3db-3c49-af39-bd4605a66979 | 1.6754 | -55.6266 | 2026-10-08 19:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 63.7 |
| b7f14bb8-7702-358e-b456-3b3cf30c5db4 | -6.4031 | -55.2042 | 2026-10-08 19:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 112.5 |
| c4a34f4a-45a0-3be6-a97e-5ee18288a28d | -5.7909 | -43.3806 | 2026-10-08 19:20:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 259eaa89-f6d9-396c-91dc-58b27e911659 | -3.2533 | -50.3899 | 2026-10-08 19:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 138.6 |
| f54f6082-1987-33ea-8786-88844380dfe0 | -14.0472 | -43.8222 | 2026-10-08 19:20:00 | GOES-19 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 113.0 |
| 08bd06f0-7575-3567-86ba-a713223f57d7 | -5.3716 | -44.2211 | 2026-10-08 19:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 165.1 |


[Clique aqui para ver as próximas entradas](README406.md)
