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

## Dados Diários - Página 155

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e48af51a-fee7-39e7-aab4-71fa3a011883 | -9.9193 | -43.6508 | 2025-10-01 13:30:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 212.1 |
| 7d1f9b4b-272e-354e-be8c-287ed13b5666 | -11.7797 | -47.5806 | 2025-10-01 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 208.9 |
| c1e1ee89-7e56-34ee-89cf-defe9dc9f995 | -8.8543 | -46.6781 | 2025-10-01 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 173.9 |
| 1af8f50c-d7a7-37db-ab1e-de8e6fd430c1 | -8.5079 | -47.2897 | 2025-10-01 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| 257cdbd4-e498-3dc0-a193-fc10b43be71e | -13.3615 | -48.0936 | 2025-10-01 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 59c69b08-c1b8-3fb0-a1ae-201caa2024cd | -8.8923 | -46.6519 | 2025-10-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 117.9 |
| 1c12005d-ff52-32df-a68c-e6413faeca44 | -13.6703 | -48.07 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 110.8 |
| 12d3f976-daf9-378c-95f5-14e9cbd874a8 | -13.3808 | -48.0908 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 70f50bc9-ddc3-39ce-9b4b-6cc81e3bbb08 | -8.8926 | -46.6296 | 2025-10-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 0fb1e492-4e70-3a5e-bab2-b505c8e2bb03 | -16.0221 | -50.8989 | 2025-10-01 13:40:00 | GOES-19 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 1fafb1e6-69c1-3592-ba6f-2ae7d11759c0 | -7.8218 | -48.2069 | 2025-10-01 13:40:00 | GOES-19 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 95.4 |
| 71795f18-91fe-356b-9ac0-20292b5d0e56 | -6.0625 | -42.4422 | 2025-10-01 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 77.7 |
| fbcbe626-c094-3aa7-a1fb-7bcd3c10bacc | -13.7876 | -47.9853 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 469ff209-7efc-32a5-86ae-4d329cdfbf9c | -8.5267 | -47.2879 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 6d0da209-90a2-3e01-81dc-e8034342e177 | -10.0717 | -50.2173 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 75.1 |
| e650573b-9bb2-37c0-b1cb-0b2b1d914fb4 | -6.0997 | -42.4865 | 2025-10-01 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 113.0 |
| 1ce58512-0449-3a68-9be0-d021c52348eb | -8.6911 | -47.6906 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 9b6c4e0a-f1f1-3510-ac7e-c0bd01f5bf17 | -13.3274 | -47.8536 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 8f0a22ce-6de1-3b63-81c3-7a6313442566 | -5.4967 | -42.7471 | 2025-10-01 13:40:00 | GOES-19 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 81.1 |
| 2af37148-df6f-3b8e-a901-f5f9fbc99bcc | -12.2156 | -47.7889 | 2025-10-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 04dc7c3f-d02e-3c3b-b78a-c26516ec5486 | -8.163 | -46.2554 | 2025-10-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| ca234f02-166f-3c68-a425-1b409f917650 | -8.88 | -47.6282 | 2025-10-01 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 44821119-f283-33b3-9251-d1f10aa8013b | -11.8618 | -45.0307 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 8449dcf7-a5d8-3e22-aa02-181d1a682899 | -8.6722 | -47.6924 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 1a6dfc57-b7bd-3ed6-b421-b23bbec734b2 | -15.9381 | -43.3223 | 2025-10-01 13:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 326.7 |
| 99a6ade1-0dd1-362f-a5a9-668f5ec4c2d7 | -10.0337 | -50.2424 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 142.5 |
| cf66f385-7a37-35df-aeee-68fd79fddcbb | -12.2344 | -47.8086 | 2025-10-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 80.4 |
| c152bca9-c907-3980-b8ad-8e91f1e37f47 | -13.3611 | -48.1159 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 209.2 |
| cbe50ae2-5a2b-3f43-82ab-a9e8a4c95aee | -12.254 | -47.7837 | 2025-10-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 53.8 |
| 3383fe6e-fc52-37a9-bb16-5c26391f9f6f | -11.8287 | -48.0841 | 2025-10-01 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.1 |
| d95e33b7-4ed2-3215-8211-8e232ba1475d | -8.483 | -47.7983 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| 40a3b5bc-e4a3-375d-a887-c233fecde7f2 | -11.7984 | -47.6003 | 2025-10-01 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 96.7 |
| d45c6493-8ab7-3f2a-972b-ac6a0fb64cd8 | -12.8967 | -45.1711 | 2025-10-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 158.5 |
| 5b22164f-56c7-3988-a1e6-d715cc74cef2 | -13.2969 | -50.6821 | 2025-10-01 13:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 92.1 |
| b62ae4e1-a4f4-3dc8-88f9-48e634d60bfd | -13.7868 | -48.03 | 2025-10-01 13:40:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 111.9 |
| ff1953be-0500-3a0d-be81-8fa0a5dc4791 | -11.1178 | -49.7845 | 2025-10-01 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 863aa6b1-ce53-3efc-a351-db2f6b697632 | -6.0978 | -42.6758 | 2025-10-01 13:40:00 | GOES-19 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 99.6 |
| 9f9c8eea-65d1-3ffe-8d26-fb2db3476d96 | -12.2536 | -47.806 | 2025-10-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 205.6 |
| ece6b064-7431-3af6-b902-c76ce2de1c43 | -5.8418 | -43.9566 | 2025-10-01 13:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| e1c13937-fe81-37e9-86b7-b0db42d80a19 | -9.938 | -43.6718 | 2025-10-01 13:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 229.2 |
| 21e547cf-a5e5-3922-9bec-4bd600d172af | -7.7944 | -42.5132 | 2025-10-01 13:40:00 | GOES-19 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 98866cc7-7add-3676-bc9b-e2895a02f39b | -10.1081 | -50.3203 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 191.7 |
| cfeda367-8bba-3c7d-9f4e-586a4cbcc459 | -13.7872 | -48.0077 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 787cfb09-9086-3dcf-982c-6f956e546659 | -11.829 | -48.0619 | 2025-10-01 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 75.3 |
| 7bb3fae2-e9ed-3fe4-84bc-b81b6de915d0 | -5.6412 | -45.4989 | 2025-10-01 13:40:00 | GOES-19 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 62.0 |
| afd8148f-21d1-3193-9c2e-5f48a76500a5 | -11.3486 | -48.3211 | 2025-10-01 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 506.8 |
| 2ae459fa-3f86-3902-968c-4659c806f8a1 | -8.5584 | -44.7644 | 2025-10-01 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 153.1 |
| 2dc1eb39-301d-3ec5-94ee-f1f8478228c8 | -10.0526 | -50.2406 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 32da36c2-3f55-31e5-bb8e-cd03f1b70ecb | -5.9366 | -45.905 | 2025-10-01 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 186.5 |
| b1a5a1fb-5818-3449-8543-387dca47b7ab | -8.5018 | -47.7965 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 154.7 |
| 53cf9a94-e598-35b1-a453-822317994c17 | -8.4827 | -47.8202 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 55.8 |
| 196a25ce-4649-362e-8c17-db1424690763 | -12.8963 | -45.1943 | 2025-10-01 13:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 116.2 |
| 17e5c320-a080-31b5-acb5-aed7d8e1b356 | -12.122 | -43.4215 | 2025-10-01 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 186.4 |
| 08f8f8b1-2619-3938-ba25-bd22fc89a4a4 | -7.5749 | -46.7778 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 136.0 |
| b61191fa-2e4d-305c-8fcc-391246929f2d | -15.9388 | -43.2979 | 2025-10-01 13:40:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 308.4 |
| 2481c153-f163-33ae-a7f9-c46075707934 | -12.1224 | -43.3977 | 2025-10-01 13:40:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 173.5 |
| 010f5399-50a6-3faf-a4ad-9c3e50e9a0ce | -11.3296 | -48.3235 | 2025-10-01 13:40:00 | GOES-19 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 277.3 |
| 8d19135e-9b2c-3b74-8657-3f33592fd498 | -12.7683 | -46.8821 | 2025-10-01 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.8 |
| 264f197d-1704-3675-9da4-bbb3bbf26bb4 | -7.8884 | -47.259 | 2025-10-01 13:40:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| f228f7aa-8431-31cd-9ac9-4ff8acbc7642 | -8.5016 | -47.8184 | 2025-10-01 13:40:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 51.7 |
| d9347cc1-1c53-336b-b4ac-14d9f881c972 | -12.7679 | -46.9047 | 2025-10-01 13:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 2093c133-9494-3a8f-999c-2f4b44855a3e | -13.816 | -47.5107 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 1468ceca-a5fb-3b50-8e6b-eb4983872811 | -11.7797 | -47.5806 | 2025-10-01 13:40:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 158.0 |
| d9bfd5ee-5d54-3cfe-aa7a-d1561f451a34 | -10.0145 | -50.2657 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 679f32ba-7165-3351-87e0-8dda14ee1fcb | -6.0999 | -42.4628 | 2025-10-01 13:40:00 | GOES-19 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 830c4e98-67f1-3c57-a16b-69b9dadbfb89 | -10.0148 | -50.2443 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 7b0cf82d-bd7f-3999-a961-23914c218045 | -11.0225 | -49.8167 | 2025-10-01 13:40:00 | GOES-19 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 59.2 |
| ac0fbed9-2068-3bad-b0eb-7f139f4c925a | -9.8201 | -47.8386 | 2025-10-01 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| af911f0f-07e3-361e-b6ba-33d51a205edd | -11.9258 | -47.9829 | 2025-10-01 13:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 9df3fed2-113b-357d-b751-b1091b5ebdd7 | -15.7509 | -43.7239 | 2025-10-01 13:40:00 | GOES-19 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 97.0 |
| f3fb95b8-9b16-3d92-bc2e-cb793068e61a | -14.9084 | -47.1965 | 2025-10-01 13:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 57d00280-e1b3-337d-9880-bec01f074deb | -14.9738 | -46.8668 | 2025-10-01 13:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 141.7 |
| fdac6b69-6efb-3ee6-a69d-1c913bfa1ce4 | -8.8797 | -47.6502 | 2025-10-01 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 60.8 |
| d557bda6-e26e-3559-8fc2-ac12b69f17e7 | -14.8884 | -47.2226 | 2025-10-01 13:40:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 0690c994-695e-3297-a9b1-0b3cd6dbcef3 | -8.5773 | -44.7623 | 2025-10-01 13:40:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 94.6 |
| a6859ec4-d433-3622-989d-c9ff15e5de28 | -5.9557 | -45.8588 | 2025-10-01 13:40:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 102.2 |
| 63129c24-5687-32dc-a48e-0b5ab6aa5e7b | -8.9182 | -47.5803 | 2025-10-01 13:40:00 | GOES-19 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 084b9d13-0cc6-3585-8c84-9ecb500984f8 | -13.3414 | -48.1411 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 216.8 |
| cfb12a79-7b49-3951-a1cd-1dba3e8ec5a6 | -7.1815 | -41.6931 | 2025-10-01 13:40:00 | GOES-19 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 77.2 |
| e67f26df-06c4-3795-aa85-e0e925269640 | -8.8609 | -47.6521 | 2025-10-01 13:40:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 1522d4d2-5189-3987-9a26-27e0f2c3760f | -15.3596 | -47.0724 | 2025-10-01 13:40:00 | GOES-19 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 421a5480-2b19-3a95-b81f-3f754f5b5d73 | -13.3607 | -48.1382 | 2025-10-01 13:40:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 237.7 |
| 6444b3b3-8f7e-3040-80b7-fd99057d49a4 | -9.4115 | -47.3308 | 2025-10-01 13:40:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 4476d281-f6bf-3dcc-94d4-2ee6fed8e522 | -7.5559 | -46.8017 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 110.9 |
| ae608c3e-0017-3fdb-badd-3c41c8b8aa3d | -11.4596 | -45.0433 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 2b651c47-23ce-3adc-a504-d5aa3f7f9297 | -6.214 | -44.2272 | 2025-10-01 13:40:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 27624eec-df89-3733-8ee9-b26e6fdccc1d | -10.2951 | -50.4507 | 2025-10-01 13:40:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 700a12fd-cf0d-3552-a8ad-18f1cc54a34f | -11.8622 | -45.0075 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 129.9 |
| 65ff7123-ee9d-305c-927c-998845e1563e | -10.072 | -50.1959 | 2025-10-01 13:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 8d8b3da4-2b8c-3beb-92d8-8a1536893628 | -13.1747 | -47.7869 | 2025-10-01 13:40:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 104.6 |
| 6588836e-fa75-3ab6-b178-d67c62b14232 | -16.0225 | -50.8771 | 2025-10-01 13:40:00 | GOES-19 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 115.0 |
| 34839d83-e786-3264-963d-d6e82e3990f3 | -8.9115 | -46.6276 | 2025-10-01 13:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 110.6 |
| fa106358-0279-360f-be37-7b6b98c2ba48 | -7.6272 | -45.4507 | 2025-10-01 13:40:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 852473a0-46a0-3121-8ea8-ae44d1f7ef74 | -6.7165 | -44.5987 | 2025-10-01 13:40:00 | GOES-19 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 105.6 |
| 9ce92703-5f2b-3744-a6c5-4e0a1ec49bd6 | -14.5526 | -40.5636 | 2025-10-01 13:40:00 | GOES-19 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Caatinga | 101.7 |
| 179881e2-6406-3078-95ac-043d377abf59 | -14.5947 | -47.3174 | 2025-10-01 13:40:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 2c6f41b6-048c-3103-a970-e69664cdca90 | -6.5546 | -43.9221 | 2025-10-01 13:40:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 134.5 |
| 5294ad14-86cc-32e5-9f53-3fbdab9dc817 | -11.9411 | -47.0675 | 2025-10-01 13:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 173.7 |
| 06d284ea-3944-3540-9fff-5c9d7e22a734 | -7.5561 | -46.7795 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 155.1 |
| c1e9cb45-6a6f-3f83-a517-a9e3295111cf | -11.46 | -45.0202 | 2025-10-01 13:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 178.7 |


[Clique aqui para ver as próximas entradas](README156.md)
