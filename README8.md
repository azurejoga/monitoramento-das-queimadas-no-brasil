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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8342ae92-2e14-399b-8803-1eed2eb212f5 | -4.78042 | -46.1314 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 34631f41-81f1-39c9-8648-0009a1af0957 | -3.57019 | -47.18142 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fb24581-d1c3-3c62-8cbe-4185bd775db1 | -3.40889 | -47.08237 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90fe2ebc-d9b4-33b7-bf4a-2fb9fa723fc0 | -3.68375 | -41.69719 | 2025-12-04 04:21:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4807f46e-465d-3d47-a774-c01c073cd297 | -4.73716 | -44.43176 | 2025-12-04 04:21:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9e1c5e7a-1498-31dc-bde2-74f377855ada | -7.11194 | -39.156 | 2025-12-04 04:21:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 208c62db-a699-3fe8-97d6-3658eccd2011 | -2.33009 | -49.08435 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ed6bed6-1893-372f-87f0-7d7dfcd3dc30 | -4.69606 | -44.49944 | 2025-12-04 04:21:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43534f4e-141f-37d0-ab11-9927c1cc4128 | -6.42195 | -44.79394 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6a4af7e-29b7-3222-91e0-1a41659e3df4 | -4.47753 | -42.39553 | 2025-12-04 04:21:00 | NOAA-21 | CABECEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202059 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| cf84dc2b-3a82-3e16-b243-ecba1a7a65f1 | -2.42219 | -48.59302 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| f03a6190-5cbe-39ab-81ba-b8cd26d2a986 | -5.33996 | -42.12057 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9e82d007-3fa3-3e34-9c05-d905dbe8cc01 | -2.86314 | -45.24684 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3be2b5b6-09e2-3052-95f7-c5e9386bc6ec | -1.96923 | -46.05481 | 2025-12-04 04:21:00 | NOAA-21 | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 33d5b8c4-fdf2-3036-94f1-dcc4d17bf69a | -5.38892 | -40.51633 | 2025-12-04 04:21:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| be0e1cb8-45ee-3d0c-8d3b-8d29194834ef | -2.53615 | -47.31522 | 2025-12-04 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 91f9699d-0b99-32e1-83c2-8d11e88d5edc | -2.61121 | -49.25745 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f522203a-99d1-3035-9098-f293af0bb8cf | -5.99445 | -40.37456 | 2025-12-04 04:21:00 | NOAA-21 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 82e2e3e8-4288-36f3-9576-9838d9f20ddd | -4.28883 | -48.36116 | 2025-12-04 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbb08169-e885-34b3-b244-1fd986a3ab4b | -4.50439 | -45.77167 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 40453990-e327-378f-88ef-3cde3f913930 | -4.50159 | -45.76755 | 2025-12-04 04:21:00 | NOAA-21 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 055eaa5b-f2b7-3685-9a37-5f7398b2de2b | -4.11821 | -47.2929 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ded99dad-dd05-31bc-8b48-949d8fe5e143 | -2.79405 | -48.90071 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0e520bd5-8a01-368b-82a7-7c4c25a157aa | -4.83743 | -43.19938 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d6f4dc1c-1188-34c7-9f70-5c7d5f7912ac | -2.13811 | -47.88313 | 2025-12-04 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c6c9a7c0-90f1-3144-af7c-f6e885f4568a | -6.05782 | -43.74883 | 2025-12-04 04:21:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 73bb0965-bafc-3747-a4a3-89f4a2665968 | -4.26393 | -44.15219 | 2025-12-04 04:21:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d56b79b8-b417-377c-a11f-07bc49958403 | -4.12181 | -47.29343 | 2025-12-04 04:21:00 | NOAA-21 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19334476-5391-37ee-8d1f-2aac05a66ca4 | -2.4885 | -47.82757 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 93877431-f5c2-38b3-8435-577bb1657f4e | -3.49901 | -44.51844 | 2025-12-04 04:21:00 | NOAA-21 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4339ffbe-c8d4-3fc2-b910-d3530d6a2683 | -5.22138 | -43.96756 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b448361a-a7c9-37aa-b7f2-b7e555085809 | -2.14683 | -47.50688 | 2025-12-04 04:21:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2bf03fc0-92cc-3111-a541-2e24c8c86173 | -5.34343 | -42.12111 | 2025-12-04 04:21:00 | NOAA-21 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 91d74beb-9b16-399c-81e3-8f30d7b062bb | -2.41897 | -48.59572 | 2025-12-04 04:21:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 7f5ece60-4c84-32b0-b33c-984392950a22 | -4.70085 | -45.69907 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2826a5e4-8204-3bb9-add3-14409c6f6d46 | -5.67382 | -39.60194 | 2025-12-04 04:21:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cd7c4c74-d4e7-30f6-8688-830c908cc39c | -2.78711 | -47.43576 | 2025-12-04 04:21:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85d4b903-cc1f-3290-a822-819409efa774 | -4.77362 | -46.13026 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 69e5c153-3158-3d39-96db-2fa122fce209 | -7.30052 | -45.11105 | 2025-12-04 04:21:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f83ca3c3-a33b-3c00-9231-b9e5e58cc7d7 | -4.5544 | -45.80528 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 75bf487a-5fd8-34c3-be08-b02c75abe826 | -4.02525 | -47.34212 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e256c34-a98e-3b82-a898-5b8ee0309537 | -4.25172 | -49.25309 | 2025-12-04 04:21:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3c31823b-d415-35f6-9f9e-814c486495d1 | -3.60694 | -45.66824 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30bdb83d-6b3c-3090-a7c1-a7063c5cf834 | -5.35094 | -46.14206 | 2025-12-04 04:21:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f8de3d6-03ce-300e-8200-414a5cd80825 | -4.52792 | -45.62458 | 2025-12-04 04:21:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b16a2df-aac6-328e-b03c-7aa887d0fed9 | -3.91955 | -47.69254 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c0b7d27-d3b6-355d-9c0d-6cb8a1513a5b | -3.04932 | -48.42272 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 3def4a6b-9801-34c2-9872-d815d4f2ac06 | -4.52943 | -44.10604 | 2025-12-04 04:21:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db3966be-91fb-372e-8bed-8e9ec36dd250 | -3.32757 | -44.37501 | 2025-12-04 04:21:00 | NOAA-21 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd2f8fb7-e5a2-305e-9a04-d1344f287b23 | -4.92829 | -44.70882 | 2025-12-04 04:21:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3dfea789-376b-3e0a-92a4-7330396afb3a | -4.80014 | -41.81689 | 2025-12-04 04:21:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 8885f8cf-823b-3c7b-b1a4-adbb1c93b79d | -4.83019 | -43.2019 | 2025-12-04 04:21:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8ba3a709-165f-38c6-ad7f-7e25b6dfaf93 | -2.34762 | -46.9173 | 2025-12-04 04:21:00 | NOAA-21 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e1fa394-65da-3670-a448-aafe3a591a57 | -2.53962 | -45.71227 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a215dd5e-c55b-35e9-8d25-563c319a7326 | -6.49864 | -43.80014 | 2025-12-04 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bcc688e7-038c-3379-a70a-543523b7e9ad | -5.55915 | -45.45414 | 2025-12-04 04:21:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e18bcf1f-bdc8-3a13-96e2-ca405c573758 | -2.06626 | -45.35772 | 2025-12-04 04:21:00 | NOAA-21 | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 67b485f0-239f-3c16-9aed-91055621a834 | -3.6563 | -41.07716 | 2025-12-04 04:21:00 | NOAA-21 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dc096b94-b1bd-329d-b934-40ab5caf5a0f | -4.77761 | -46.12716 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f12e504-beb9-3706-bba3-93f31f6f658f | -6.43295 | -44.78858 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 396881f7-021e-32bc-bb59-0b8730df1d95 | -2.79282 | -48.90038 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86a7ecd0-ffb8-35ef-acc2-6aa750b41462 | -7.15068 | -38.86058 | 2025-12-04 04:21:00 | NOAA-21 | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| bdadf0f6-65ae-3ba8-b911-ea9eec6b90a0 | -2.53263 | -49.45464 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dd11bda-a57b-376e-9eb6-7eb60c60a1f0 | -4.02446 | -47.33887 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed679fb-6c30-3a54-93df-b8707c30b3f5 | -4.79955 | -41.82079 | 2025-12-04 04:21:00 | NOAA-21 | JATOBÁ DO PIAUÍ | PIAUÍ | Brasil | 2205276 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c2d32fee-2c9f-31f5-a0ba-5b7c6a36a537 | -2.85978 | -45.24632 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e54d82cb-9de2-35c7-a630-101ed2844973 | -2.14574 | -47.88426 | 2025-12-04 04:21:00 | NOAA-21 | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 77f36804-80a8-393a-9394-e9df8f0dd894 | -4.52051 | -44.66212 | 2025-12-04 04:21:00 | NOAA-21 | TRIZIDELA DO VALE | MARANHÃO | Brasil | 2112233 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ead5f10e-a53e-35f4-8472-1a1234c1c7ba | -4.70028 | -45.70267 | 2025-12-04 04:21:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22c79cf8-1311-3f11-b814-75c52901d3f5 | -3.21055 | -45.15939 | 2025-12-04 04:21:00 | NOAA-21 | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 31289aec-697c-3d6d-a88b-7c69698709ca | -2.79348 | -48.90421 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0c2e11d2-5b9d-31f0-96a5-c37226ae9500 | -5.29157 | -43.84359 | 2025-12-04 04:21:00 | NOAA-21 | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| afe537bd-d953-3f1d-a522-94a3b90f6a65 | -5.98325 | -44.59654 | 2025-12-04 04:21:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed267468-ed2b-3cae-a6a7-2c581ec65cd8 | -2.41601 | -49.34584 | 2025-12-04 04:21:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e0ee7df0-9376-3a25-99ca-db274782b4cc | -4.07698 | -43.69557 | 2025-12-04 04:21:00 | NOAA-21 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6edcbcd0-771c-303c-a42f-b33924aaab51 | -4.72638 | -44.71605 | 2025-12-04 04:21:00 | NOAA-21 | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36344756-0bde-387a-925c-d935e1efa3f4 | -3.78878 | -43.60151 | 2025-12-04 04:21:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 92c830fd-70fa-30b9-a98b-13165208fe0c | -4.04973 | -46.61171 | 2025-12-04 04:21:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.3 |
| d63d2418-fc68-3fe4-824d-bbf369dded36 | -3.33247 | -45.6104 | 2025-12-04 04:21:00 | NOAA-21 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb8d0e9-0a8b-3fb6-862d-e84bf80531c6 | -3.29167 | -50.20364 | 2025-12-04 04:21:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 57843789-c8ab-36d2-b615-41a05a003795 | -3.16813 | -48.63673 | 2025-12-04 04:21:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 77f7e015-310b-33db-8de4-5e7f18365e72 | -3.23484 | -46.85245 | 2025-12-04 04:21:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dceb5188-fdbd-3f3e-8048-89a9f9add0ea | -6.42141 | -44.79739 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8977d103-d63c-31c9-9a26-98ad0b0e2442 | -6.42525 | -44.79446 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af9f9beb-25d9-3d9e-b253-ec00a71efddb | -3.367 | -50.75592 | 2025-12-04 04:21:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| daa99aec-3569-3d71-bb68-4f08572ec65f | -6.43241 | -44.79204 | 2025-12-04 04:21:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89572ccd-8bba-376f-af3e-1164490e26c0 | -4.02742 | -47.34354 | 2025-12-04 04:21:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 664a3557-abfc-39b0-989f-f1fb1dc52c86 | -5.79501 | -42.99124 | 2025-12-04 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7e2af52c-98de-3d3a-af4e-bc523acd1c86 | -6.46564 | -43.72659 | 2025-12-04 04:21:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7f8e5d47-8e0a-3244-9832-85270cf85714 | -4.66844 | -46.30299 | 2025-12-04 04:21:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b18d06e2-de6f-3890-a5ac-4d27eb4dd25d | -4.34371 | -46.13847 | 2025-12-04 04:21:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e994c2a7-1e53-3257-bfd2-a80edb8db68f | -3.81462 | -40.94511 | 2025-12-04 04:21:00 | NOAA-21 | UBAJARA | CEARÁ | Brasil | 2313609 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2193c730-0870-383e-ad11-88fcfaf3ed30 | -2.46267 | -44.16448 | 2025-12-04 04:21:00 | NOAA-21 | RAPOSA | MARANHÃO | Brasil | 2109452 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea08f7b7-5619-3e65-aba4-da1007f2e7eb | -5.0191 | -41.00566 | 2025-12-04 04:21:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| d1764549-c495-3495-8405-4f1c57aa6752 | -2.88993 | -45.3829 | 2025-12-04 04:21:00 | NOAA-21 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0e89b7ef-d47d-3736-a747-9fe11f9d38ea | -5.82573 | -43.00308 | 2025-12-04 04:21:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 70eaa76e-ae64-349b-83cd-350ef96e4e0e | -4.85423 | -42.47523 | 2025-12-04 04:21:00 | NOAA-21 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1bbb3fe7-6a64-3281-a684-a023ee04cb9d | -2.49082 | -48.14782 | 2025-12-04 04:21:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb293804-670f-3ee8-a0ee-bf9c20038e8a | -2.60294 | -49.25615 | 2025-12-04 04:21:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7458c4cd-f6ef-3b50-acd2-9ae080c6ccb3 | -4.33345 | -48.76717 | 2025-12-04 04:21:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |


[Clique aqui para ver as próximas entradas](README9.md)
