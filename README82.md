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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a5e38c47-062f-3b3a-abc7-87b3dc5a487c | -9.6205 | -61.8259 | 2026-09-16 15:20:00 | GOES-19 | VALE DO ANARI | RONDÔNIA | Brasil | 1101757 | 11 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 7f83a7d9-88b4-3778-a247-f3733da980ba | -10.9105 | -54.025 | 2026-09-16 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 45.7 |
| d5b40d52-9e84-31c7-b392-7fa90914ee16 | -1.6022 | -55.5682 | 2026-09-16 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 25375e59-fb37-3b03-9268-d5cd59993ed3 | -4.7217 | -55.7321 | 2026-09-16 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 48.1 |
| 100e495f-8601-3cbd-9790-d12b52a461c1 | -11.2299 | -54.1396 | 2026-09-16 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 50.2 |
| 702b447f-0e74-37c3-897e-8721b2b11e27 | -8.8585 | -44.9149 | 2026-09-16 15:20:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 357.2 |
| f659ca22-7553-3058-988c-52523b789d91 | -5.144 | -55.9345 | 2026-09-16 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 161.8 |
| 581865ad-ea20-396b-98a1-8ecf167baa7e | -13.3758 | -51.7193 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.5 |
| b399deb2-1544-3a2e-9e8c-785a8f9cff68 | -6.174 | -53.524 | 2026-09-16 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| bd5509b9-8467-3157-91fc-41d102c94d0d | -6.7315 | -58.805 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 43d6051b-1e82-3f32-b9c1-31505c6bf947 | -5.221 | -49.3125 | 2026-09-16 15:20:00 | GOES-19 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 49.3 |
| 6c9f1032-c153-3f74-a8be-e630546384ba | -6.1046 | -55.6367 | 2026-09-16 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 94fc226e-3826-36ee-8dbc-bd7f21e6abff | -11.2693 | -54.0129 | 2026-09-16 15:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 48f5f2d8-2c3f-3d4f-bd25-be8aff2aca62 | -12.6821 | -54.7174 | 2026-09-16 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.8 |
| 54e31ab6-f81a-37b1-8287-289a82054630 | -11.0437 | -49.6635 | 2026-09-16 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 44.9 |
| 170b2213-57a2-31e7-89ce-027ef645e619 | -8.6178 | -44.5511 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 174.9 |
| 85ee4b7e-d949-30b8-a0f5-1f16f7ac953e | -13.4471 | -54.5761 | 2026-09-16 15:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 75.8 |
| 3392eef7-e4d7-3640-be65-608528e4a03d | -9.1337 | -65.844 | 2026-09-16 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 110.1 |
| 433136b7-018e-343f-867d-9c8f3376c7a0 | -10.8571 | -50.8183 | 2026-09-16 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 89.0 |
| 51a223c6-6dc1-3143-823c-7f362713b245 | -6.1362 | -59.8871 | 2026-09-16 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.4 |
| aec18998-ef48-3991-a170-b44e3ba923fb | -6.1177 | -59.9069 | 2026-09-16 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 86.9 |
| 0c4ecd3c-b8a0-3a1c-a54f-e8fa7dab53d5 | -13.4499 | -51.8799 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 53.4 |
| d6a47b8c-1872-3d0a-8822-c011538dbef9 | -11.2302 | -54.119 | 2026-09-16 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| f9976657-72e6-31e8-b7df-d4a634dce54e | -9.4078 | -60.3205 | 2026-09-16 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.8 |
| bbf04830-f004-38fb-89e2-46f7855f1d91 | -3.1174 | -57.6779 | 2026-09-16 15:20:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 85.0 |
| de660cf2-846c-3b58-8f0e-ae4e6090158e | -11.4905 | -50.2581 | 2026-09-16 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 5904c13c-2192-3a45-b87c-3d2576edbcce | -7.7808 | -66.9208 | 2026-09-16 15:20:00 | GOES-19 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 00bbb175-59c6-3f9c-a1f0-0c74ec246072 | -7.0058 | -59.2382 | 2026-09-16 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 1ac4f363-d5d0-353b-b853-aa0362f31f41 | -11.2113 | -54.1208 | 2026-09-16 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 52.5 |
| b4f8ee06-6bf6-3284-92df-9edaec61da54 | -9.031 | -61.0122 | 2026-09-16 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| 8a8bab4b-2ee6-32ae-bc0a-277317996c32 | -15.3408 | -52.9704 | 2026-09-16 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5ac510d0-de29-3542-8501-5a0c9ab226b0 | -3.2752 | -54.2622 | 2026-09-16 15:20:00 | GOES-19 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| bd7e1f84-f2a6-30d6-a967-3202e92e8fa7 | -2.6968 | -57.5307 | 2026-09-16 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 3eea8a11-a68b-35f4-a5f8-e6179f148b15 | -10.876 | -50.8163 | 2026-09-16 15:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c62469d6-45eb-3a7a-82ba-4ed4ed3c2221 | -6.6767 | -58.7105 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 395f3aca-c0c2-3a19-b70c-531f23aa55bb | -8.5989 | -44.5531 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 352.3 |
| 17cf052d-4340-3584-8bef-e9a7915b0d34 | -15.0547 | -48.5883 | 2026-09-16 15:20:00 | GOES-19 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 42.6 |
| f132e906-36d4-3eb9-b62f-026cadd5af75 | -8.6311 | -66.5287 | 2026-09-16 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 67.2 |
| d2441ecf-ff38-33dd-a259-caf85da7154f | -13.5844 | -51.8632 | 2026-09-16 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 17bde7ff-eeb2-3bd4-a4f8-ad047aa91c0a | -9.0059 | -65.4186 | 2026-09-16 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ae07b57c-f3b4-3f9c-b23c-354f9c29a371 | -3.1697 | -58.6437 | 2026-09-16 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 6082dc09-703d-3f77-8b2f-8510987e2fd1 | -2.6785 | -57.5115 | 2026-09-16 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 54.2 |
| c43c3c5a-b663-36b3-9d3a-c7aaee69d286 | -5.1256 | -55.9352 | 2026-09-16 15:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| e1cee7b0-3867-3a65-a998-73b8f6742615 | -12.6826 | -54.6763 | 2026-09-16 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 4a592ab5-426b-3e9c-a1eb-0e56a90e2980 | -3.4461 | -58.0199 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.5 |
| f62a02b6-8224-3c64-9aed-b21054a22e68 | -8.2831 | -45.6585 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 208.2 |
| 1cb91e3f-afba-3bfc-badd-54f2e53dd3c5 | -12.6636 | -54.6782 | 2026-09-16 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 75.6 |
| 77f67826-a426-31b8-a972-f57047a7ff70 | -13.395 | -51.7169 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 5314845a-cbe7-3011-8aa5-157fe0d58b47 | -9.1725 | -59.4241 | 2026-09-16 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.9 |
| 032dc8d0-3dec-3f68-a28f-110354e8ef74 | -9.0866 | -61.0287 | 2026-09-16 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 70ab96de-875a-3230-a2b7-0db22de4add4 | -11.4908 | -50.2366 | 2026-09-16 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 63a70831-8ecd-33ec-a603-b376caf905d0 | -11.4715 | -50.2603 | 2026-09-16 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 593af0e3-e13f-3ee9-b5b2-97fefba183c8 | -6.6758 | -58.8654 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| e130eec9-3e02-3fb5-9b38-74ef9a5a3b13 | -9.3572 | -50.137 | 2026-09-16 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 39a00d6b-d9d6-39c3-a14d-a1a5147abe0a | -2.6784 | -57.5504 | 2026-09-16 15:20:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f338063f-5fa8-3d58-85f0-25eb7be21ee8 | -6.9872 | -59.2582 | 2026-09-16 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| fa7d0b2a-28b0-3bbf-9a34-984ad553ba29 | -10.9595 | -50.2529 | 2026-09-16 15:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 21abd52c-35e1-3781-87eb-9988f9073c92 | -10.7015 | -54.1663 | 2026-09-16 15:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1fbdda08-2eaa-3f00-93c2-e5f54c563ade | -10.6335 | -50.5651 | 2026-09-16 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 73b70bde-4ea8-38e0-9f5b-1217210caeec | -9.7322 | -64.9067 | 2026-09-16 15:20:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 175.1 |
| 7641537b-91b3-3aea-8011-8aa55a101c60 | -9.7793 | -60.4744 | 2026-09-16 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| d2d06519-17c6-3c82-a55d-93ae767c284d | -6.1609 | -52.7496 | 2026-09-16 15:20:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| e798a191-62bf-3088-b5bf-de8504b84614 | -8.3737 | -54.7299 | 2026-09-16 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 181aa34b-7243-3188-85a5-48f6c9feb99e | -9.3569 | -50.1583 | 2026-09-16 15:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 89dfd14e-5939-3acc-9875-abda23286813 | -9.7608 | -60.4561 | 2026-09-16 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 0f2cac1c-f1f9-3f29-8b01-6094e1374bee | -11.0247 | -49.6656 | 2026-09-16 15:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 5f061e88-f746-3e3a-b271-eb9070203541 | -15.6557 | -52.7366 | 2026-09-16 15:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 66.0 |
| 0e8df39f-1ca9-387a-9a37-ad5efc304e4a | -10.3766 | -58.3171 | 2026-09-16 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 47.5 |
| dada27c9-66c0-3f18-a007-3763c18e24ab | -10.331 | -45.2883 | 2026-09-16 15:20:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 6f49524a-a7ba-3c69-84f2-a0946324cdef | -13.3391 | -51.6176 | 2026-09-16 15:20:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 3ffc7a9f-4368-3311-8699-a05dc31c85a1 | -4.4271 | -55.7817 | 2026-09-16 15:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| eba4c515-b672-306b-87b3-15eabda28e0d | -8.6188 | -44.4819 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 274.8 |
| bdb39367-42a9-3b25-ba5e-6b76bc39207d | -10.6525 | -50.5631 | 2026-09-16 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 17a4230f-6c8e-3d07-b8cd-d000775922b1 | -8.8456 | -45.8939 | 2026-09-16 15:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 237.6 |
| cfb3937d-d515-3007-b092-8b455a7b631b | -13.5127 | -51.5532 | 2026-09-16 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 70.5 |
| d58d673b-4f73-3dcd-8cf6-d34a9af61682 | -10.2824 | -49.9821 | 2026-09-16 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 48.2 |
| a1eb77a9-cc00-3ce2-87ac-56194a6f0636 | -10.3953 | -58.3159 | 2026-09-16 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 82589578-0e5e-374f-b3fc-72fbd17b55eb | -8.5604 | -54.6973 | 2026-09-16 15:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 48.8 |
| 33a1cf29-c719-3cb4-8c17-ab3710f46e15 | -8.6181 | -44.528 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 226.1 |
| 88a7c4c2-6973-32b8-9eee-a1531df3532c | -8.6184 | -44.5049 | 2026-09-16 15:20:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 280.4 |
| 6f817f47-9d1d-3b45-a5bd-1aa2716ed199 | -11.5095 | -50.2559 | 2026-09-16 15:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 018c3c28-f55c-3be8-822c-a34882364fcf | -12.6818 | -54.7379 | 2026-09-16 15:20:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 71908355-04af-327b-80f5-31f643c4e844 | -11.4167 | -51.4371 | 2026-09-16 15:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 4f51fc18-e688-353a-bf1d-1b255cbb1f46 | -10.2821 | -50.0035 | 2026-09-16 15:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 51.4 |
| 5cacbf45-a645-31db-a03c-45eb8e4654a7 | 1.2609 | -50.8928 | 2026-09-16 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 0bfe3bad-7af0-3c98-8bac-6d389351217b | -12.6628 | -50.8264 | 2026-09-16 15:20:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 8b0feb0b-877b-3a45-bc84-3b0ac8d1bf22 | -9.7913 | -45.8555 | 2026-09-16 15:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 5e1b4d9c-bb99-3860-9c2a-d4725bbb1d8f | -9.0124 | -61.0131 | 2026-09-16 15:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 59.4 |
| a3fd5bd0-1386-3fe8-97d7-754597a73f7d | -6.7863 | -58.8995 | 2026-09-16 15:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.5 |
| e4d16ecd-4bb8-38fb-89a2-4a20cba0825c | -3.1514 | -58.644 | 2026-09-16 15:20:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| fa047f80-bd05-3afa-ad2e-002707a8b597 | -1.861 | -54.4315 | 2026-09-16 15:20:00 | GOES-19 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ee94c792-8fef-3515-b22a-1bc0f83544e1 | -8.5497 | -64.0477 | 2026-09-16 15:20:00 | GOES-19 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| f0f9578e-e2a4-3eca-8dd8-06f3605f6c2e | -6.4484 | -60.0101 | 2026-09-16 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.5 |
| 604c2080-30c1-30a6-83eb-4026553a412d | -9.7979 | -60.4734 | 2026-09-16 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 9b753eee-1130-3ac1-9795-2b1e8ec81fe9 | -9.3892 | -60.3215 | 2026-09-16 15:20:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 72.4 |
| 831ad9cc-280b-3830-a4e4-fb11aa6d23b6 | -3.4279 | -57.9816 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 168ea81f-0cc1-357c-8962-5d35cf9bc147 | -10.2513 | -57.6952 | 2026-09-16 15:20:00 | GOES-19 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| aceb0f7a-c626-30b5-b815-346437c054f6 | -3.4462 | -57.9812 | 2026-09-16 15:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 89.9 |
| 4f8bd15e-c13f-33a5-909d-b6d83a40f6e5 | -13.5652 | -51.8656 | 2026-09-16 15:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 17b01325-773f-36b4-8bd2-a1019df53021 | -6.0256 | -59.9293 | 2026-09-16 15:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |


[Clique aqui para ver as próximas entradas](README83.md)
