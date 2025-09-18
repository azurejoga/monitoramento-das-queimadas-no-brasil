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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f7c0de5a-395b-3c23-b370-0634e234010f | -9.08687 | -44.9425 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 104d4d60-77fe-35af-afe6-4cb2e01decdf | -9.15272 | -46.95842 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 97aeb7e4-ec10-3128-a491-0b8ff54b576e | -11.17485 | -44.41823 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3657544d-da08-3905-ae88-24cf7cb3339b | -7.24226 | -46.61125 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8bd6fd2-0c76-388a-8e2a-b275fe4b873c | -7.86506 | -45.60202 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7aab7f24-bdc9-3245-918c-7ac987bc9f70 | -9.72659 | -46.58247 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 05b6dd1d-808d-3b0b-bd6f-cf642e32ac0d | -10.20157 | -42.54009 | 2025-09-18 04:14:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 4d8e179e-c560-3243-af5a-efda51b563c5 | -9.8439 | -48.41693 | 2025-09-18 04:14:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 346948f7-a44a-384a-ae88-eee29a6d1ba9 | -9.00707 | -48.17564 | 2025-09-18 04:14:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cd4bc370-98c4-315b-ae0e-67303b3d5005 | -8.83067 | -43.0222 | 2025-09-18 04:14:00 | NOAA-20 | SÃO BRAZ DO PIAUÍ | PIAUÍ | Brasil | 2209559 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2abb7f89-3027-3ed2-ad52-631c2cd6dbc0 | -11.44388 | -43.54684 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79915c09-dca8-3e0c-ae95-f005365c4632 | -11.24409 | -47.39154 | 2025-09-18 04:14:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4dab1203-3e9d-3da9-904c-dc7d7e1ea2ce | -8.70234 | -39.60782 | 2025-09-18 04:14:00 | NOAA-20 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 998a23f6-6e0f-30a3-9249-86b5acbc8438 | -8.90109 | -46.13519 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7034e67-7cf2-3e4d-9143-64db47d0dd4d | -8.13452 | -44.84513 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| a38b7424-07fc-3869-9f14-488fc451f183 | -10.60829 | -46.4725 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c477c91d-bd43-307c-a7a1-c56e35838a30 | -11.93265 | -38.33396 | 2025-09-18 04:14:00 | NOAA-20 | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 26.0 |
| 4e770e4b-73b6-35d8-b03a-0fa63cca61e3 | -9.16581 | -46.96925 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.5 |
| ad521fbb-2c8d-3c38-9adb-01c673d03569 | -9.16359 | -46.96019 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 24391c4e-bc7d-3faf-8184-ab540afa4dae | -11.03444 | -45.06487 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8216abe4-245a-32b5-a326-5aca1e02fd5c | -8.13115 | -44.84459 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7e0ede6b-e8ed-31f0-945e-79b83f56438e | -11.37802 | -50.82513 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.9 |
| eb5b7cdf-202e-3b47-ad03-3bc3cbecd420 | -8.02209 | -45.65482 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| abed6990-c286-3e5a-add0-f4e468e22730 | -13.07834 | -42.13702 | 2025-09-18 04:14:00 | NOAA-20 | RIO DO PIRES | BAHIA | Brasil | 2926905 | 29 | 33 | nan | nan | nan | Caatinga | 34.1 |
| 148efb21-46e1-3807-a7f4-a8636118f5cb | -7.58777 | -44.60603 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0c704af-eb7d-321c-9cd1-936ae4f3ec56 | -12.44236 | -49.73701 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4837bafb-62c9-3e7c-b491-10c97558a62a | -8.58969 | -45.71785 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cccc1cc1-03ed-3bd9-914c-7820e7cb28fb | -9.07344 | -44.94033 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 195d7449-ec0c-3497-87c5-86a6c11171c2 | -13.39946 | -46.80793 | 2025-09-18 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5256eac7-9a0c-3db8-a679-5b6d3cdd16f9 | -13.25899 | -43.50004 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95cab48b-8c2b-30b5-be5c-920887927fe1 | -8.00618 | -45.68748 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57d274b7-5e91-31a7-9ba3-404544d407ed | -9.73012 | -46.58307 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce28591b-2cf7-3ac6-8d85-e55307272f57 | -7.65195 | -44.46281 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1a087cfb-61c1-36b3-be56-9ed3b07fa88d | -8.9304 | -44.49744 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 091bf7d3-5630-3c0c-948a-596a20ffb578 | -11.37677 | -50.84021 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 13c2e4c0-10e6-3bb0-b7f7-40a6af4cbc5b | -10.64166 | -42.31821 | 2025-09-18 04:14:00 | NOAA-20 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.7 |
| bb4fd984-a781-3fe6-9889-e660144efa5f | -11.59944 | -49.82129 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c76e9204-d995-3878-b49a-636a7bc054ad | -8.13057 | -43.63103 | 2025-09-18 04:14:00 | NOAA-20 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9e0f4029-47e9-34ec-8aba-e1497055e637 | -8.93814 | -44.51318 | 2025-09-18 04:14:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| da854103-acbe-3ef1-9ccb-f95060a764de | -9.18746 | -46.95095 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 125bcd74-6195-3053-abcc-46fd94105946 | -11.49806 | -43.67882 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b93a61e7-4888-3bf2-a0c3-0ebd1fa9fb8d | -11.33237 | -43.47832 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 63b9ffc3-f1b1-3530-bc72-0eb36cf37574 | -7.59403 | -47.13175 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 739300fa-9b91-30f7-892f-5b86b3f473ac | -11.49877 | -43.60994 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2b601d50-0313-3b79-93bc-8c03b1306ef9 | -10.90155 | -45.44091 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f78a36ed-f9b5-3429-a006-20394d166d9c | -9.16872 | -46.97412 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 02729a48-cc74-3109-a439-db95f7c1beab | -7.51859 | -45.29583 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4612b0d3-17b7-34c5-99fc-a8a995f2c217 | -12.43785 | -49.73987 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f8b73421-0b24-3586-aec0-363647e07f96 | -7.32876 | -43.99522 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 681334e0-10c4-300e-b384-b2a43a1ac839 | -7.32488 | -43.9982 | 2025-09-18 04:14:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43f8861e-67be-32eb-8e2f-905182467735 | -9.07867 | -46.92939 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 20bc9785-ebfb-3230-85d7-07c52ef6c574 | -13.90187 | -44.97686 | 2025-09-18 04:14:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 41cdac5a-4a5b-3343-b545-863ac212bdd9 | -10.63791 | -46.44524 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 582dda3f-5305-3220-a33e-09a8a170bf5b | -11.46981 | -48.70137 | 2025-09-18 04:14:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 14d72827-56c6-33dc-8363-2c68cd26264c | -9.96822 | -45.43874 | 2025-09-18 04:14:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 890408de-2a2c-3f96-8cdf-c2f6ad862b4f | -10.94062 | -49.48248 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3abe93ce-793a-3580-a18a-74bd19546b93 | -7.65977 | -44.45676 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 719a24d4-89cb-38d3-9065-cca2deee73de | -8.87474 | -46.14254 | 2025-09-18 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 37254eb5-ff3a-3124-8038-14c81420eafc | -7.24805 | -46.62146 | 2025-09-18 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 82091d30-5596-305f-ac75-c09aa1ea8fd3 | -11.01271 | -48.92225 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 26e83eb2-51e5-3b04-82bc-c2267a73c948 | -7.65138 | -44.46638 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c6fe01c1-8b48-3633-8ecb-876e03ae1cbc | -8.65308 | -46.43478 | 2025-09-18 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d565b7c-34f1-38f9-aba9-8cfd8eac29ef | -7.93134 | -39.79812 | 2025-09-18 04:14:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd467a9b-63cd-3efd-a867-f38b54f9e196 | -7.20402 | -45.33477 | 2025-09-18 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c1151898-2de2-3352-b7c3-04a355e68262 | -7.09248 | -48.29579 | 2025-09-18 04:14:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35ffa2d0-cd8c-3a71-9169-3e3240a04e7b | -15.12736 | -41.9891 | 2025-09-18 04:14:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 3cee865d-5614-37d1-b7e4-d7b4ed4a14e0 | -11.19864 | -45.37508 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0ad5fac0-4fb4-3508-851b-7cd6f4b96bb1 | -9.01317 | -45.53045 | 2025-09-18 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8dc84fe9-a3e0-3ba2-b78c-a3e8048381b2 | -7.98474 | -45.68821 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bf19533-e72d-348b-967a-6b7677a228b7 | -13.94098 | -47.98859 | 2025-09-18 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f5812a7-b65a-30a2-ac83-a12aa6cf1883 | -12.08188 | -46.56593 | 2025-09-18 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5afcc85-7f80-3160-ab6b-e38e4ce871bf | -10.79856 | -44.24235 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f02a89bf-d6ea-3dcb-8883-8c77d00ef3ea | -9.15343 | -46.95415 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 4c1ac4fe-4de5-350b-b4e4-a019be08dfe2 | -10.74349 | -46.55027 | 2025-09-18 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b5fe488f-c60e-3e1f-a5a0-e830a8ee402b | -7.82752 | -43.85027 | 2025-09-18 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a26af446-22c0-390c-9d38-1d300a3c9b21 | -11.5036 | -43.68694 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 92d1320c-6cf6-3dd9-8de6-35bda681965c | -7.34659 | -44.58212 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ebc7f58d-6692-3cd1-8bf5-0d02f62ca0c5 | -7.49213 | -44.3754 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ef910262-70e6-33c2-ba2f-456e237dfcc4 | -8.05971 | -41.27325 | 2025-09-18 04:14:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| d3a96219-e576-39f4-a234-4fc77538999a | -11.50573 | -43.62936 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4fcc1c4-5d44-377b-ade8-940b9690a446 | -11.382 | -50.83657 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 38408cd6-23f6-3a55-b47b-105d18e93e10 | -12.44103 | -49.74437 | 2025-09-18 04:14:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 43f1d858-e73f-3bd2-8b65-cce6f4c64700 | -13.94401 | -43.98826 | 2025-09-18 04:14:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 39bbd7fd-2872-332a-8352-b79648483c10 | -11.17968 | -45.36457 | 2025-09-18 04:14:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97bdbd3c-6c4c-3393-8610-97602b0b0c78 | -11.01665 | -48.92301 | 2025-09-18 04:14:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d874337-4088-3911-bbde-6ef8fc2a82d7 | -9.15777 | -46.95046 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 7d0d6610-cb23-33e8-96ad-61fba8561206 | -11.99941 | -46.71945 | 2025-09-18 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a658b473-b45f-3c44-a5f2-0b5dfaab7040 | -14.5905 | -45.17474 | 2025-09-18 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 12eb60c1-59d6-33b9-b4b9-13494f4efa25 | -12.27545 | -45.29094 | 2025-09-18 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e508d570-ecb6-3ada-882d-45e201595073 | -12.40089 | -51.42259 | 2025-09-18 04:14:00 | NOAA-20 | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f7b566c5-322a-37cb-addd-b49cac3068ec | -7.81365 | -46.89305 | 2025-09-18 04:14:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6af5d5af-affb-3aa5-a9b3-64cc758b23e3 | -11.37638 | -50.83403 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 6bbe470d-7333-3215-84d9-cdcd89c9ad28 | -7.54547 | -44.76151 | 2025-09-18 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aa338cc6-fb48-333a-9f1b-6c7a10cba661 | -8.01452 | -45.69214 | 2025-09-18 04:14:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 43d949b0-aa98-3e52-a15b-0d5f61a54b96 | -7.26661 | -44.89951 | 2025-09-18 04:14:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac22d892-5664-32d4-8072-1b1c7cc11bfd | -9.16502 | -46.95161 | 2025-09-18 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 1d22f6fd-8b8b-3d60-ac78-a285b51a8a94 | -11.44443 | -43.5433 | 2025-09-18 04:14:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 224f7831-89f9-3419-b28f-a28867885b96 | -7.52322 | -45.28894 | 2025-09-18 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f4e6e491-a7b3-35b1-8b7f-a962b9cf42eb | -13.94245 | -48.00195 | 2025-09-18 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e868f67d-12bb-3828-abbb-dcdca4baacec | -7.29633 | -44.13391 | 2025-09-18 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README17.md)
