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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b8127fe0-1c33-3cac-bec0-836fdeeea382 | -16.35115 | -47.09647 | 2025-10-03 04:34:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b82c54c-2248-3250-8cd7-b8d8a0322466 | -14.71938 | -48.08626 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1358b832-b6b0-3c91-a554-af55d9b70c73 | -14.23036 | -46.09778 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d33d860b-1fea-313f-aca2-5582f74a8dc9 | -12.62853 | -46.96042 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf76c125-6079-30d0-a97f-35aa4e90bde8 | -13.51193 | -47.25418 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b01e3cc7-9c2d-3569-8bfd-a8906df4bac9 | -15.75915 | -47.77455 | 2025-10-03 04:34:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d3edcb03-31b3-3c55-aced-7aac1a0a6679 | -15.92176 | -43.3073 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2b59df1f-09e3-3967-8d57-d056978f475f | -13.14722 | -44.53727 | 2025-10-03 04:34:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4a8c9422-8bae-3214-94c4-45876abdf869 | -13.7559 | -47.97841 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30202110-db9f-3ce0-9295-80515bf9fbf3 | -13.14584 | -47.83138 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2252e364-83b2-3878-bbcf-5bfeb5c203e1 | -14.73478 | -48.13013 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eae56850-d99a-3e6b-b648-c8047e8bcbbe | -15.23931 | -48.72084 | 2025-10-03 04:34:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3aea31a8-433f-3813-bca7-b69e6004e577 | -13.31714 | -47.20126 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b5b18a8a-7f7b-3d7f-8f4e-a9dfeba073b2 | -12.61689 | -46.97584 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 2af191d8-285a-3ee6-9dc5-fa96cf80303a | -15.91772 | -43.33857 | 2025-10-03 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0fb561ee-1300-32c9-b9fd-5d589770acf1 | -13.34879 | -48.08336 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9894cfcd-0b20-34dd-8cbf-c0ba8363ed2f | -14.2924 | -45.89201 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5265c8d-2de7-31c3-8e68-07b81d109d6e | -19.72777 | -45.88196 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 01b665ca-2aed-39b1-9ca1-ce9881cf03d1 | -13.54244 | -47.28568 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c7cd3378-95a7-3257-b6fe-f22cd39558d4 | -12.92806 | -48.44117 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 553f0af0-9039-3296-83b3-ed2970f4f862 | -15.24583 | -49.3167 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 310d8ee9-4211-3f4f-a171-5928a379de18 | -13.19591 | -47.88821 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a6fc546-efb1-30ac-a2a2-13e3ba8d182a | -13.77779 | -47.58141 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 75437618-1823-3449-a99a-712e4ea6ca0a | -13.2015 | -47.806 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 702f4c83-3370-3af0-91a3-79ab097397ad | -13.75085 | -48.0791 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 40bf8c5d-96ce-3b92-99f7-243559831f17 | -15.78321 | -43.69609 | 2025-10-03 04:34:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b67e4d41-39f8-3ca9-a634-71fb20dd72bc | -14.82996 | -51.74234 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 40905cbe-6344-3449-96bd-65d90da8603c | -13.97577 | -48.17379 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 230d313d-93c9-3306-9f0a-4370b92577e8 | -12.62613 | -46.96149 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb4837aa-6b71-3710-aac0-07fc7ca6cbfc | -15.27684 | -47.91764 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7ce6770f-f437-35e6-90aa-aa1a14fafdcf | -13.13586 | -47.89768 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b307cb4c-e7ca-3e44-965c-0f0241fa0051 | -19.14259 | -41.49949 | 2025-10-03 04:34:00 | NOAA-20 | CONSELHEIRO PENA | MINAS GERAIS | Brasil | 3118403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7bd6bfca-f81f-3dd9-a2c8-25381d798c2b | -14.92281 | -47.21629 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 117b8fec-2045-318c-a0a0-c836da7df983 | -16.29381 | -45.24398 | 2025-10-03 04:34:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| aa280101-c009-3f84-8bf4-5a7a0777e94a | -14.9427 | -46.90687 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82c1b7bf-86c6-382d-ab70-9b5f4b94664f | -14.59747 | -46.72728 | 2025-10-03 04:34:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 393a655d-9bc8-3b29-b66f-5a075abcc9f4 | -15.25136 | -50.12254 | 2025-10-03 04:34:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 24564062-d782-3092-8e47-2b913ede83fc | -12.36903 | -46.51417 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 451e3bca-2f76-3885-8a6e-930f35143373 | -12.91199 | -46.91646 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ca505c4c-dced-37b3-8f7c-17dee5c1db5b | -13.14308 | -50.02691 | 2025-10-03 04:34:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 125c2216-0376-33b4-a65a-17be5381f6af | -13.55296 | -47.30526 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e89d62f4-315e-3959-83d9-078ba8c752ca | -14.67938 | -48.09888 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6538cda-6bf4-3841-88a9-dddbf1a1a2eb | -12.93002 | -45.09192 | 2025-10-03 04:34:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b58fe7ac-1fea-31d9-8eb6-75c7166e5cf7 | -13.96167 | -48.09734 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3815ad0b-4870-3e9e-b1b7-606beb36fa66 | -17.33014 | -52.81248 | 2025-10-03 04:34:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfaceec9-986c-3be0-b82a-c7cad0c43cbc | -14.95119 | -47.51831 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 83cb7a90-9a6f-3bfe-84e0-05e3ea83af45 | -13.1712 | -47.89196 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 465f1976-69e3-3b70-8287-f1b4f87aa00b | -14.61551 | -48.24744 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ff60e26-3d7f-3cb1-aa52-82b3a10bee9a | -14.24113 | -51.71846 | 2025-10-03 04:34:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed835ba6-2e83-3f9a-a2c4-907c5948ef80 | -13.77211 | -47.57271 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 55201ff3-78d5-309b-9378-e98cf1fa8ad1 | -12.86483 | -46.99545 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ec17dff5-f59d-3d53-a127-19057f6b2f3c | -19.7157 | -45.91321 | 2025-10-03 04:34:00 | NOAA-20 | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4ab3ae3b-e0b0-3ead-b730-c6558e9f4d3d | -14.18797 | -46.6851 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2a887aa2-1eb1-3eb0-9479-3b1c2768d0fb | -13.34544 | -48.08284 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 123105a8-bae6-3f6e-9688-6d7512a0173d | -15.28509 | -49.30481 | 2025-10-03 04:34:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2bf8f30e-ca71-3268-a957-31260ce3d60e | -18.64349 | -50.68562 | 2025-10-03 04:34:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9f673dae-94b8-385a-886b-33da56bc4c20 | -12.60301 | -49.90156 | 2025-10-03 04:34:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1a0d7542-b61d-3024-9f08-82a85330df85 | -16.78102 | -50.11444 | 2025-10-03 04:34:00 | NOAA-20 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee3a72f7-66eb-3208-a24f-3f8e98a8087f | -12.62682 | -46.97206 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 050b5797-3811-344f-8738-bf99118bb66d | -16.0402 | -51.0265 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f45d9576-ecf6-386b-bb03-ed55dcfb2e2c | -20.11716 | -44.3951 | 2025-10-03 04:34:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| e843c323-5f9c-362e-b6d0-e6edbc29c929 | -14.64918 | -48.2529 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 38b01705-fb3d-39bc-bad4-8176df46062d | -13.86017 | -47.93757 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 6a451372-3cd2-3b08-94d8-eedae292323e | -15.12103 | -48.49228 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 64c16805-160c-3984-a2dd-6038050dc100 | -13.67564 | -48.02959 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d852e032-3631-39dc-8ddf-77fd3aa8b27b | -14.93398 | -46.89197 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 694cf89d-9d87-3eb6-a705-9c7dca487955 | -16.01866 | -50.93256 | 2025-10-03 04:34:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fe8ff9b-3dcd-3658-bb12-6dd72e51053a | -15.19852 | -47.99824 | 2025-10-03 04:34:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c1cbe5bf-ae6f-3855-bc20-22184b598d19 | -19.597 | -45.90642 | 2025-10-03 04:34:00 | NOAA-20 | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 51c617ac-ce36-3dce-befb-12b91b0e9c11 | -15.60916 | -47.03922 | 2025-10-03 04:34:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d84040e2-f4e2-3a5d-960a-5ce7a54fdb11 | -13.53795 | -47.2453 | 2025-10-03 04:34:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 168f2a34-a2b0-382c-ac87-c86986711c5d | -13.74411 | -47.98777 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6e3df7bd-2329-3d16-b071-2ee43356203e | -14.29734 | -45.8836 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5a2938a5-d7e6-3c84-add0-d0e155d7fa04 | -13.78805 | -47.58285 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| bd51cac9-1afd-3f1a-bd3d-943a6a10dba2 | -14.29234 | -45.91962 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d497a21-ecab-3aba-bb05-bc4f6fbc2946 | -13.38432 | -47.28923 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9055f236-cdf5-3a1f-82e9-0475c0c4d72d | -13.23093 | -47.35506 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| bd33a378-2450-3940-957b-29919d04c509 | -13.33148 | -47.5953 | 2025-10-03 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5e172627-eea3-3047-9544-5d5a4e82fae7 | -20.11766 | -44.3909 | 2025-10-03 04:34:00 | NOAA-20 | MATEUS LEME | MINAS GERAIS | Brasil | 3140704 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 5476db86-0943-36d0-be5b-2040d98658b2 | -16.87578 | -52.79646 | 2025-10-03 04:34:00 | NOAA-20 | DOVERLÂNDIA | GOIÁS | Brasil | 5207253 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 03e2339f-ef36-34cc-aed1-27b456d2a8f5 | -14.95235 | -49.99548 | 2025-10-03 04:34:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee7a052e-0ca1-310a-a472-50cc538baf2a | -14.70163 | -43.88768 | 2025-10-03 04:34:00 | NOAA-20 | MATIAS CARDOSO | MINAS GERAIS | Brasil | 3140852 | 31 | 33 | nan | nan | nan | Caatinga | 21.5 |
| 3948999f-c12a-3698-8447-9d0c2e3fca3e | -12.37842 | -46.52365 | 2025-10-03 04:34:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc5e0b04-ecf5-3458-b146-e12516444295 | -13.19868 | -47.8018 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e44247fe-eefa-3914-b442-d3e81e688176 | -14.1927 | -46.67747 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 18c92868-7695-314a-9359-a6f08bad9518 | -14.291 | -45.88548 | 2025-10-03 04:34:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06a3f221-230f-3fc2-a4b3-bc309315ff73 | -15.35293 | -47.06414 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 23e176b2-5c6c-3cf4-859a-c175e96134dd | -14.29777 | -45.98847 | 2025-10-03 04:34:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f1094e72-a1a5-3d2e-b249-1d144fbe727b | -12.79161 | -46.87844 | 2025-10-03 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9492c334-e0af-34e2-a6b2-753890861b6e | -16.04842 | -51.03925 | 2025-10-03 04:34:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8c9ddcbd-9651-3999-81f4-8f551bd2100c | -14.6531 | -48.24979 | 2025-10-03 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 05892de7-29a8-336d-8a57-7ee1fdc0f3f9 | -15.31594 | -46.27795 | 2025-10-03 04:34:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63f74036-a0d1-392a-a274-726376f0d5ec | -14.60164 | -46.72369 | 2025-10-03 04:34:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0f73abed-38fa-356d-a52c-9aca80eed33a | -13.75533 | -48.07233 | 2025-10-03 04:34:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ec0ed765-5d3b-341a-b47b-76a981910333 | -13.31831 | -47.19345 | 2025-10-03 04:34:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4476fee0-b508-3d75-900d-2063f7a6a194 | -14.19862 | -46.11111 | 2025-10-03 04:34:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| fd30df09-8d23-3539-8e9a-0e749d8f275f | -13.21214 | -47.82698 | 2025-10-03 04:34:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 189b54fd-55e4-3b93-872f-85b4cb56c11c | -13.23247 | -46.43549 | 2025-10-03 04:34:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eec573f3-8bbd-3a2c-b80a-f0e4a52de4a5 | -14.91661 | -48.34086 | 2025-10-03 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 01b1ada7-6b07-33fa-b2ae-e44a982c5528 | -18.87918 | -48.03119 | 2025-10-03 04:34:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README114.md)
