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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3b10093-561d-3d7d-b9d0-b89e7be3143a | -10.8511 | -51.28812 | 2025-10-17 04:21:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 3869506f-ca70-33c7-bd61-5a8166e3ee04 | -12.23708 | -47.67793 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 23420beb-39a7-3462-8dd2-2ff854c2d6b6 | -12.31145 | -47.25851 | 2025-10-17 04:21:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3f07c99-2816-3888-8d84-5f5e18f73db0 | -14.32927 | -51.46953 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| d79ceb73-a10f-3c53-9974-883982735acf | -11.2892 | -49.88789 | 2025-10-17 04:21:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7e276e5a-4dea-3610-8069-d7ff12398081 | -11.97585 | -46.56593 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9c7b25c2-9ab9-3782-bd34-209eb6a8ebf4 | -12.78138 | -44.88583 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8fc6511a-072a-30cf-ab71-3a93bc2a2782 | -12.77694 | -44.89253 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| f6facd04-e7f7-384c-bebc-61bad5329cfa | -11.62372 | -48.48146 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbd9b258-e170-319a-9031-7eb4af370cca | -13.42897 | -47.96345 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 02c9bfbf-2f39-34cd-bacb-e2d4e7ab49d1 | -14.33172 | -51.45548 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 9.3 |
| b253c8c3-5a80-35b2-99cc-1d8d492a8e20 | -14.3462 | -51.44276 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| db3ab011-6100-32c4-acf8-072e20e2c868 | -13.13734 | -46.47494 | 2025-10-17 04:21:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 12064cba-c410-3ba2-b955-ed09ecc6fbe0 | -13.01604 | -43.83858 | 2025-10-17 04:21:00 | NOAA-21 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d99885aa-f697-35af-8742-ac7662eecfc6 | -16.39915 | -41.96049 | 2025-10-17 04:21:00 | NOAA-21 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| febc2f28-d5b3-3e41-935a-9db1cd3708a4 | -10.00268 | -56.11464 | 2025-10-17 04:21:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6ada7470-1552-3015-82f1-f79fd0f5c754 | -13.94765 | -48.69523 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 41a745a9-ebdd-33af-a515-b65a3d60d041 | -11.57842 | -44.05549 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a5593156-ceb4-3493-b826-3b2644d0ea2f | -13.9373 | -48.69339 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7ca6360-896a-3398-b09d-1cf8afd845c2 | -11.58166 | -48.56058 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 20de3fef-1e9a-3fe1-9c02-c5ce18c52a69 | -14.35767 | -51.46307 | 2025-10-17 04:21:00 | NOAA-21 | ARAGUAIANA | MATO GROSSO | Brasil | 5101001 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0fc3a755-35c2-3ab6-b7da-ba7d9e9e8509 | -10.94509 | -49.48167 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 665d5328-7c5c-37bb-957b-2ee7f62d5e35 | -18.21927 | -46.05893 | 2025-10-17 04:21:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6758ebef-8d8e-3de7-9e3c-904f193f8b42 | -12.78473 | -44.88636 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| def46848-719d-3793-bdb2-c2f40b84fec1 | -13.25998 | -48.56067 | 2025-10-17 04:21:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bc229a21-8197-3ff2-97f5-619facd4bf3d | -11.96025 | -45.36174 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 15.6 |
| cbe9acf5-66ca-3a86-b8e5-369b71e1ef11 | -10.9837 | -47.90714 | 2025-10-17 04:21:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 76f23105-6bf1-3b51-827a-e76e9852537f | -13.4336 | -47.95644 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9abbb6df-895f-3ca9-becf-7de97eec9c7a | -16.61635 | -43.36628 | 2025-10-17 04:21:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 799b20be-96e4-3d7f-b7a3-96d3ae161a9d | -15.7837 | -43.65553 | 2025-10-17 04:21:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b00ebbe1-38af-32d4-8f0a-46721061cc87 | -12.92494 | -41.82596 | 2025-10-17 04:21:00 | NOAA-21 | PIATÃ | BAHIA | Brasil | 2924306 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6dfb92b8-0d10-3b61-846e-727277d3b4c0 | -11.57814 | -48.55999 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4da51245-4c15-32c3-b6db-ade51602c058 | -18.53454 | -43.98977 | 2025-10-17 04:21:00 | NOAA-21 | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90dfbd0c-5797-3d72-a2ce-8398efd5589c | -12.17206 | -45.06916 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 26d27268-684b-349d-83a1-5357d4e4ba71 | -13.44623 | -48.11305 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f32001f-3ea9-320c-89f0-d6636eed94c0 | -11.95694 | -45.36122 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 20.9 |
| ef21ba34-4d59-39a7-8f6c-7046a2408cb3 | -14.33567 | -51.42647 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5f38f625-9819-32cc-85f1-dadac26636f5 | -14.33581 | -51.44817 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 4437536a-1fe3-3646-a353-36b15e171615 | -16.81555 | -53.9192 | 2025-10-17 04:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cc84147c-15a4-35e2-bc38-258d35406526 | -11.47314 | -45.08218 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 00201c72-0aba-3603-9154-24650c500cb4 | -18.26019 | -47.82454 | 2025-10-17 04:21:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71ccdfbf-f72d-3c09-a06d-1bb921422598 | -14.34225 | -51.44202 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.7 |
| 5efeb938-82f0-3d03-a02d-2dd55ed443c0 | -14.33912 | -51.47506 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| eeef3420-d62f-34b3-b39b-14db37e9f40f | -11.58975 | -44.07245 | 2025-10-17 04:21:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 22263a7c-aac6-37e0-84fe-dc95687a73e0 | -13.24106 | -47.10679 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 99bb9061-f943-3152-9eb4-cf33e72e05a7 | -14.33645 | -51.45182 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 75ef62be-a863-3cbc-b890-27a5f15ef584 | -13.82618 | -42.34745 | 2025-10-17 04:21:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 7afa99b3-4821-3cc9-ad00-008767019a54 | -16.59587 | -42.43484 | 2025-10-17 04:21:00 | NOAA-21 | JOSENÓPOLIS | MINAS GERAIS | Brasil | 3136579 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f575b723-f573-36fe-b680-479cb311f709 | -15.73548 | -44.61324 | 2025-10-17 04:21:00 | NOAA-21 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 37231ce5-3ce2-33c0-9ac8-a89c28c37d47 | -13.27359 | -44.48483 | 2025-10-17 04:21:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab20bbcf-c284-3823-b0c7-db4b9af78a76 | -12.77359 | -44.89201 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.7 |
| 3eb371ce-5b80-309e-b99d-6d78ba4cc4d9 | -13.20114 | -48.32113 | 2025-10-17 04:21:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cdf7f09d-a78b-30cc-b208-88af9b94d9ee | -13.73512 | -48.11124 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e441147-c12b-3117-8364-165d3d724b22 | -12.43787 | -51.31421 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d0985b3-48be-342b-82ba-9a8f2fd81b3a | -16.81471 | -53.92369 | 2025-10-17 04:21:00 | NOAA-21 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| e6808407-b94e-3259-9dd1-b78cf5aa5b81 | -14.15365 | -44.31866 | 2025-10-17 04:21:00 | NOAA-21 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a1e3120e-4c43-3d04-8a2d-ae7e916940d1 | -11.56076 | -46.90561 | 2025-10-17 04:21:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b7ad7112-2608-3c39-ba45-b3599c2f4137 | -11.71583 | -48.58255 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e51889f7-2c68-3451-acac-01b5aace66b5 | -13.44949 | -47.94419 | 2025-10-17 04:21:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7c1051ea-b386-316c-b520-747d85f176b6 | -14.08961 | -43.622 | 2025-10-17 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cd28f32c-71c9-3bdb-ae90-c98d1234f4a4 | -11.59373 | -44.09206 | 2025-10-17 04:21:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 03b14c3b-b156-3858-85a8-fda0cbc84069 | -12.76856 | -44.88012 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 72f47c93-ebdb-375a-98e0-1dde4ee777ef | -13.90647 | -43.613 | 2025-10-17 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4b07d273-536e-3b6d-b9e4-606415cd3a7e | -13.23816 | -47.12477 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 28483520-f213-3863-a5fc-115ea100d4c2 | -11.97641 | -46.56239 | 2025-10-17 04:21:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04b1ad0c-73c3-353a-a4d5-ac1ee8bd23c7 | -12.27665 | -47.11222 | 2025-10-17 04:21:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fad908d8-aa1c-3707-822e-fc7449aa5227 | -11.5753 | -48.55538 | 2025-10-17 04:21:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 00e19dca-4ff6-35e4-b80c-29626a90f0b1 | -12.62679 | -43.43502 | 2025-10-17 04:21:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a6b2c8f-18e8-36ae-a475-08488807ebd2 | -12.42572 | -51.31202 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 248d67af-ffc6-3604-9c6f-24c03d85db88 | -14.30966 | -51.4414 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3f729fe-8753-3ec4-8b0d-268df0f5a0a6 | -18.16272 | -45.30201 | 2025-10-17 04:21:00 | NOAA-21 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 516272c0-33fd-3824-a398-2152fa9c668a | -14.71214 | -48.30661 | 2025-10-17 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f454612-0d3a-31bd-a455-a8c45c76a907 | -9.4474 | -56.65205 | 2025-10-17 04:21:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 699b7ce6-c42b-38a5-9747-12756ad7a130 | -16.19937 | -43.67792 | 2025-10-17 04:21:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a387d816-92e1-3558-bb66-d1232190de6c | -12.95975 | -47.9465 | 2025-10-17 04:21:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3b2f709-e554-3ac4-967d-82286895607d | -13.8277 | -43.55667 | 2025-10-17 04:21:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b5cc8e8-74ae-3dd4-a6ab-bbfeb179f278 | -14.33313 | -51.42405 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f31f6895-e627-37d8-8ee6-6890359a772c | -13.4896 | -40.33178 | 2025-10-17 04:21:00 | NOAA-21 | LAJEDO DO TABOCAL | BAHIA | Brasil | 2919058 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| d8406a96-ca4b-3811-9ebd-d1169a44e5fb | -12.15364 | -45.01138 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dec686f1-2e6a-3a3c-990b-14ce6782fe96 | -12.16928 | -45.06506 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 86ee1c0a-1518-35ce-b69b-0999ba977ebf | -13.23716 | -47.10984 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b4b41339-0eb4-3c5f-80b8-1486a18d5d53 | -14.23827 | -54.91195 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3e0082c0-4b38-30a5-be38-c32d9754758b | -12.78024 | -44.87085 | 2025-10-17 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 67f18836-5719-33fe-8d37-aa21c3de96e4 | -15.04845 | -46.61322 | 2025-10-17 04:21:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81db5eec-47b5-379b-978a-dbd28cc30925 | -14.33452 | -51.47784 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 45f812b2-1622-3e19-8e4f-da532c0bf257 | -10.95172 | -49.76796 | 2025-10-17 04:21:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 9e2de22e-2034-3254-bfae-c9925355402f | -12.16486 | -45.0717 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79457337-db96-3675-bddd-7498483f56ff | -14.33676 | -51.44293 | 2025-10-17 04:21:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 43.7 |
| c7d23dd0-aac9-34df-92ae-96c9244438fa | -14.23998 | -54.90328 | 2025-10-17 04:21:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f4e7718e-ab42-3540-a5f6-f09ace7043ec | -13.236 | -47.11702 | 2025-10-17 04:21:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 2a336562-1adb-3a62-981d-3626ec05b2da | -13.37424 | -43.59152 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 50a61cd5-6c07-358e-8cb9-ede4904eadbf | -12.17593 | -45.06611 | 2025-10-17 04:21:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6bad59f-6789-3042-9cd0-9a5a0621c8f6 | -17.96528 | -39.88241 | 2025-10-17 04:21:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 5ea7a145-8f7a-3d1f-9d96-e8f77074c634 | -12.43722 | -51.31785 | 2025-10-17 04:21:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43868843-37e2-3827-88a3-ee824d7d08b7 | -11.47646 | -45.0827 | 2025-10-17 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b7ddbc46-4b10-3a2c-943e-39cf42bee5dd | -13.29847 | -43.61328 | 2025-10-17 04:21:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34c38989-f60b-3a71-ad29-a398579c2426 | -13.93795 | -48.68955 | 2025-10-17 04:21:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bb6f18a0-2ad8-3c22-91e5-80853f8012cd | -18.4189 | -44.27962 | 2025-10-17 04:21:00 | NOAA-21 | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 925341c6-ae4b-3c4e-86a6-d7e318d095da | -13.73234 | -48.10696 | 2025-10-17 04:21:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 491c2203-b4c5-3bea-b5c6-f2132aaf1010 | -16.92091 | -49.83958 | 2025-10-17 04:21:00 | NOAA-21 | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README69.md)
