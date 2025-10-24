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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3dbfcffc-3999-3ec0-be8b-49d6c880b5f8 | -10.95891 | -45.07815 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a7508cac-e029-385a-b321-44c0386b872b | -4.87554 | -47.53848 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a24da0b-833a-33de-8b4c-accd09e67138 | -6.89505 | -38.26744 | 2025-10-24 04:17:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 358178a9-81a7-34f0-8e8e-254341f90a73 | -2.85375 | -50.74697 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8c4eef1-b1c7-33ba-ae87-e59e45e91bf5 | -4.03636 | -51.1608 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d99e4053-6f2a-3bb9-9c06-ddd73229e6e0 | -10.64372 | -44.78225 | 2025-10-24 04:17:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0e04b902-5278-3acf-89d3-8f3fe52ace57 | -5.45621 | -45.41395 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| ed6d7a56-6339-3300-b706-44c06595d4f8 | -11.82255 | -44.16402 | 2025-10-24 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eed218c1-773d-3e2a-858c-ca83d3f99727 | -11.36765 | -45.93827 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8545e813-bc49-37ae-ae7b-ed69d72fd003 | -10.52677 | -45.00771 | 2025-10-24 04:17:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c3458d45-2be7-3c6d-aafb-e03e7f57af5f | -12.15275 | -47.02056 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fd9d3dc0-b735-3384-8b87-331b42101d14 | -2.80858 | -49.13608 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 846de4ed-2276-341a-afe1-76e2eca80979 | -3.81829 | -42.47137 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOÃO DO ARRAIAL | PIAUÍ | Brasil | 2209971 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cefe1266-f16e-3fda-83b5-038c2de8d8fe | -10.98284 | -50.36269 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8835e06b-7980-3b4a-a568-cf0bc5883a5c | -5.45231 | -45.4135 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 5e98aa4a-c735-3327-a574-bfc4381e895f | -4.17742 | -42.98152 | 2025-10-24 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e7452dcb-a31f-37b7-9d00-8fc4367dbde9 | -5.43082 | -40.88369 | 2025-10-24 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6d916866-8035-3028-be0f-50130773c13c | -11.58052 | -49.53724 | 2025-10-24 04:17:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b30d49de-b034-3e68-b47c-9e549d424fa7 | -12.0565 | -46.42603 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e8e98fb4-aaed-361c-a353-56820b3b335c | -4.2878 | -40.70087 | 2025-10-24 04:17:00 | NPP-375D | PIRES FERREIRA | CEARÁ | Brasil | 2310951 | 23 | 33 | nan | nan | nan | Caatinga | 19.9 |
| be245955-7488-32ff-8794-22d88aea6321 | -3.24042 | -48.75829 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ab7d28f-7b8d-3da2-991c-c7923455b378 | -10.97679 | -54.24836 | 2025-10-24 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9f598c4f-0851-31e9-ac9a-8a29b5892bb7 | -11.27623 | -44.64248 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c363c893-e1ed-3412-8f6e-973f74478931 | -3.83337 | -52.37031 | 2025-10-24 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fe77cb83-fa5d-3b6f-8908-052d911f5449 | -2.86992 | -41.74856 | 2025-10-24 04:17:00 | NPP-375D | PARNAÍBA | PIAUÍ | Brasil | 2207702 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 39a2b500-0541-3496-a708-668ac791a5cf | -11.01264 | -47.89985 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 52836834-425a-3ae3-bd40-97cad4a2dadf | -5.01855 | -47.15186 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cbba2a65-f19c-3d58-bf24-e95b38d4bb46 | -5.44943 | -45.40898 | 2025-10-24 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 890ea370-1055-3555-8e3c-c5db63a3577c | -11.03116 | -47.90344 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4ba71e70-26d4-38ab-8703-f0c73431e0f8 | -8.74198 | -45.83405 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d996e622-d4b8-3111-9386-7cc14b86ffdd | -9.67216 | -45.45015 | 2025-10-24 04:17:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12f5c06e-7c7f-32e7-b28f-8f28c6eb719a | -6.53747 | -43.86539 | 2025-10-24 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aff0be4d-7cd7-32e1-b5d1-11145632ace7 | -12.64947 | -44.12695 | 2025-10-24 04:17:00 | NPP-375D | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3ddea77e-eb9f-3659-90ea-b5760c16f178 | -12.05836 | -46.41476 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 116147ec-d451-3a17-9629-12123c64ce96 | -3.24014 | -47.25693 | 2025-10-24 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d29d2d32-92e9-3572-9d1a-e9dfe618d645 | -5.55128 | -41.34837 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 29149511-6aca-3d41-8948-039f37306369 | -6.30857 | -41.88466 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6d1f8b33-3b4b-37fe-884e-387eafd089d9 | -3.24984 | -52.91439 | 2025-10-24 04:17:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 81e4ee9e-45fb-3290-9f86-7fa5631e53ce | -4.11752 | -42.18489 | 2025-10-24 04:17:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 849d315e-5265-3a33-9c81-71e250d676b0 | -3.02675 | -49.49312 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9654c364-6a14-3d36-91ff-8f0ef1f0eea9 | -12.03241 | -46.91921 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f16a88e2-09f1-3d44-9ad9-c4263ed84352 | -9.552 | -46.70101 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e77c13f8-486f-3430-be44-c90c89b9bfdd | -4.96258 | -48.67097 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0eb84f65-b064-3dee-bee6-34e43cc0f0c6 | -2.95666 | -49.14849 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 551ec481-55d2-3ac8-8778-45e3f3957ce7 | -10.95032 | -50.36962 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4ad23c8b-553b-38a5-a569-30dfba326fdd | -5.56893 | -46.52409 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| acb7c2ed-e2df-3255-aea3-ad1d61e660e1 | -12.02781 | -46.53515 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77365d1a-0870-38be-8c50-a34775f293cd | -12.31436 | -47.26184 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17b32af4-f032-357d-a8f6-20e770c41d95 | -9.60148 | -46.92441 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7cc6d94a-2546-3a4e-883d-08d068de27a3 | -2.80246 | -49.14462 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 88fb579c-8ce5-3192-850d-6d23303f34c9 | -9.26161 | -46.4695 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04b90881-0c2a-3dc9-bdb6-b51be4437607 | -2.26248 | -47.84659 | 2025-10-24 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d8d280a2-f10a-3177-a390-57fdaa5312d5 | -9.36805 | -50.81158 | 2025-10-24 04:17:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 964384ed-c1b6-3a74-9fe0-4d713fa2e4dd | -10.58928 | -49.64091 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3668dee1-921e-3203-b510-86ed776a5a4c | -9.87014 | -47.4649 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3d542894-22a8-35db-aa08-e38be32b7dee | -2.76774 | -48.60092 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6ae4fe9-e0d0-30b7-9b02-101bae39839d | -5.58359 | -41.31897 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 1acf88da-8010-3e14-9b8d-a1badc0f2cb7 | -11.48153 | -43.24627 | 2025-10-24 04:17:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| caf42476-a44d-3033-a43e-5a1a44b6fe08 | -4.27745 | -40.69944 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cbc5dc7a-62cc-3fdd-9293-66ec817a8ef4 | -9.63148 | -46.89941 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 6cdc7e25-becc-3bf2-816e-f76bd403fb24 | -3.24414 | -48.76329 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b44d7092-be16-316c-85d4-86862a0ec118 | -9.25742 | -46.47291 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2d66ea4-edb0-37df-b92c-8ada8699cc9a | -9.60218 | -46.92023 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| abff1834-3b90-3615-89fe-93cf084c338d | -9.23339 | -51.82445 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b09ac455-ca83-3bb8-81e1-75de6028d126 | -9.24316 | -46.40522 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 88d57b30-d952-366f-ab6c-616e9af1f0ab | -2.44553 | -47.15818 | 2025-10-24 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| b7261bff-5d2f-3da0-8e9a-ebc3f1ebc54e | -4.91127 | -47.65625 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0607dfd-86b6-3794-82d1-af2b6b556eaf | -9.59996 | -46.91133 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 551ae295-4be6-383d-88f8-361b9cf41801 | -11.99265 | -45.42761 | 2025-10-24 04:17:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fe943a5d-ed62-3f19-bc72-1ee226fee431 | -11.3556 | -45.94777 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 03a071ac-fda1-305b-9662-df8b663250a9 | -11.35839 | -45.95205 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2e959f9-2619-3589-b98d-4f85f13f1d4b | -6.30239 | -41.88004 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| bd5a6a5d-4286-39a0-85e9-3bb4cbb487e3 | -10.90257 | -48.04535 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 4d4cec6a-e87e-3f54-9f71-a43d245bbbec | -10.67095 | -54.31385 | 2025-10-24 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f5f7f913-6ece-362e-b276-4a039720fa2a | -2.81694 | -49.14219 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.8 |
| e6e5bce9-a9f7-36a8-8333-74db0e345955 | -3.78316 | -43.90505 | 2025-10-24 04:17:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| cc6423a0-7667-3f4c-851b-c2e7be232127 | -9.55267 | -46.69696 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b131878-8124-3938-9df3-10ada9b898bf | -6.30576 | -41.88057 | 2025-10-24 04:17:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a04208d6-428b-3142-85f1-715a76dd334b | -8.34863 | -49.39724 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 772b0680-638f-30d3-8a16-899ffd92573d | -6.29694 | -40.87243 | 2025-10-24 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 20386fed-c8e4-3400-a58a-434fc211c0e0 | -2.49046 | -48.14775 | 2025-10-24 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 619ccd41-1390-3163-818f-9f3fd51b4d9e | -11.03809 | -47.88527 | 2025-10-24 04:17:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 07006b16-93b3-37a1-ae36-9dba875f77ef | -2.74809 | -47.13618 | 2025-10-24 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a08cd610-c1e7-359b-a4fd-5731bb5519b3 | -4.55213 | -46.74456 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 08d999fd-7e06-347d-a33f-59315848de6f | -2.81159 | -49.14613 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 483d6e9f-b503-3fc1-8ec1-89ee6bee09ca | -6.00987 | -45.87261 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3da73e93-a9af-30bd-b0cc-a3dbe97ae5b6 | -3.23903 | -48.76683 | 2025-10-24 04:17:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5de3f222-d5cf-3387-92a6-c17a69ae88ef | -6.01344 | -45.87317 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a555135a-3263-3e35-a237-5066f6212d98 | -5.62885 | -42.59296 | 2025-10-24 04:17:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| ab809359-1e3c-3f7e-8b9f-67cf4a06970f | -11.11999 | -47.77542 | 2025-10-24 04:17:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 9f834c08-b91e-3be1-9506-01ba3e2fa7f1 | -11.12104 | -47.77749 | 2025-10-24 04:17:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2a49897-6d10-3591-8256-a55e5af24f95 | -4.00096 | -43.28125 | 2025-10-24 04:17:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6d699bf3-57da-3fee-a9b9-ba3b0bcb4290 | -4.27399 | -40.69897 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| b4bd4931-534b-3367-ace2-43f7da4c7779 | -12.07302 | -46.43304 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| eda99f51-3464-38e5-ad79-4814a7d875d0 | -11.06053 | -45.39662 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17d00830-c8f5-362b-afa1-63eab335dc09 | -6.84588 | -41.54738 | 2025-10-24 04:17:00 | NPP-375D | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b16f7ed0-d7d6-3c2a-9f9e-2d6be56ed6e3 | -4.87635 | -47.53345 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f618c381-4e2a-3298-a7d4-6821b55d7d5d | -9.60786 | -46.90828 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 54b68442-4118-3865-a633-6903b896424b | -9.23735 | -51.83078 | 2025-10-24 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 375476bd-c01c-339b-9571-814acc8d44a8 | -9.63865 | -46.90079 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README21.md)
