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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d74ae4a1-fb7f-3b4c-a4b4-6fae812f4d14 | -13.26402 | -51.28848 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| cfae73c0-6378-3807-aac7-6944aca45d6f | -8.59363 | -44.47382 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 956faf9e-1b18-3c43-b0a9-9c6bb719a045 | -11.97588 | -44.92921 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 248746b5-68eb-3ac5-b0a4-144238cf37c9 | -10.88184 | -51.55066 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ad0d031-4161-3110-8e30-89688b0ec67a | -10.80524 | -46.20762 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| a34fadf6-9ffc-3b8b-950c-ca7f59dad23b | -15.04391 | -48.55832 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7c4e6e22-a7db-3b78-a0e1-c37e80bb50b7 | -9.36443 | -50.10529 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2a9d2dc5-a179-3c71-8f2c-34468e3c347f | -10.67043 | -54.13874 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 35fbeb74-e3e9-3de4-ad8f-466c61ba873e | -14.76842 | -42.94599 | 2026-09-15 04:34:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 05fcd54c-a88a-3079-9cc1-3da2b7608355 | -8.58366 | -44.49216 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 256d75e0-c4d1-3999-8a7f-f93b3ae5252a | -13.61281 | -48.28819 | 2026-09-15 04:34:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eb4778e-39e0-339d-8eaf-d82a39dee68d | -8.53414 | -54.70982 | 2026-09-15 04:34:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cbb78a02-54b2-3129-929a-5f471583c576 | -15.04931 | -48.58848 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8f5c6a1d-777d-329a-bad6-978b7bcfc54c | -10.59773 | -57.31838 | 2026-09-15 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f41da7cb-ad03-36d5-b814-8e10c7463791 | -8.80039 | -50.49202 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9fd79ba7-f2f0-36ec-80f8-e3920d696dee | -11.3854 | -43.95111 | 2026-09-15 04:34:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e1f033d-0a59-3b06-a776-034b78057ea4 | -11.16985 | -42.79771 | 2026-09-15 04:34:00 | NOAA-20 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 180a8bae-541f-30c0-a8f2-76e879117377 | -13.30295 | -51.28477 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| b2e97a73-326b-360c-bec6-84e0ca2bf14c | -14.2209 | -47.42142 | 2026-09-15 04:34:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c3c18001-2c7a-3063-a3c6-9bd368dca4f0 | -12.494 | -41.42617 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| c070e3be-53c8-3abc-9713-a8dd84ff6973 | -8.8471 | -45.89869 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c84cd57-e614-34f6-b6f9-b5c9848f2ec8 | -13.27338 | -51.28382 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 61e51223-feca-3c82-9cf0-706a34779dba | -10.79852 | -46.20653 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15841433-d06b-3ff7-b862-0a5108bea862 | -13.06688 | -48.60136 | 2026-09-15 04:34:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 304450e7-fff9-3f4c-a047-7722c5522dce | -11.79678 | -46.59458 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 458832ef-813d-3085-be61-775e8b717b4a | -9.41217 | -50.10499 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 22.8 |
| af1552a5-465d-38dd-940b-22960c5748a3 | -13.29788 | -51.29261 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9b8764be-691c-3516-a253-b1e14c8010ba | -13.5744 | -51.44974 | 2026-09-15 04:34:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| da150cab-0ea2-36d1-81b6-d4a86f168f70 | -9.36087 | -50.10468 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c353d36-c9e0-3c49-8bc1-09a32f037c04 | -9.54593 | -45.42714 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 577b7c30-4d35-359b-9e47-e88d37ba3970 | -13.28706 | -51.29066 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aff4d40c-fd69-3a1d-8908-6f56ad4a7367 | -10.42741 | -48.63869 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f51852b0-88f6-3bdd-a1b8-55f22db27ce2 | -15.59028 | -42.57405 | 2026-09-15 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |
| 975c9dc3-e683-32ca-81ef-372567925e18 | -10.66641 | -54.16122 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a55dabbb-f133-3dbf-a563-b92b4ec943b7 | -13.5954 | -47.90398 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1b7c56ac-191a-3680-bb8e-20f56b98a35a | -10.25556 | -57.69901 | 2026-09-15 04:34:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 386b36d3-e8af-3fab-be25-c4483140382b | -10.67124 | -54.1342 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 51388659-b7d7-3c57-bb2d-26fddfd92241 | -10.68186 | -54.17822 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a36d8589-b64c-3208-bb44-95da9b30af86 | -12.55336 | -47.12056 | 2026-09-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aca382e6-b18b-3a04-afc3-7f34783806e6 | -10.60252 | -57.32329 | 2026-09-15 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37c0ad63-99c6-3b01-8b25-5f9a4701a3a9 | -9.36006 | -50.0877 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e824a68e-7b03-3e61-82d2-92313056be66 | -9.26565 | -59.64103 | 2026-09-15 04:34:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5d4e349c-6ab0-39df-9315-5e0555d99a61 | -13.32679 | -51.60542 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a02b04be-faa0-372e-b7c4-adfbf222ba93 | -12.4739 | -41.40882 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5c3ab7d4-b531-390e-97b4-b169a73fe85c | -15.00208 | -48.52191 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f413df01-8af3-3d81-99a9-9dc11521de14 | -10.597 | -57.3222 | 2026-09-15 04:34:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2bebc81d-28f2-328b-ac04-a649c8e14ba2 | -10.88239 | -47.83622 | 2026-09-15 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53d9898a-643e-327b-8a29-fdec301cf3ae | -14.19533 | -47.43215 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c266decc-18ac-3a4d-9e48-5a1c209ed59b | -15.14641 | -49.59008 | 2026-09-15 04:34:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a999580d-4472-3321-aa35-f082985e5e6e | -9.47843 | -45.45823 | 2026-09-15 04:34:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50d827b5-d0c2-3a3d-aac4-405650a3e470 | -13.30149 | -51.29326 | 2026-09-15 04:34:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2355bba0-9302-3412-ac8e-9dca926fbf3e | -9.87656 | -47.77316 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 87fbc85a-1cb1-316b-b703-86ef9cf8c253 | -9.35925 | -50.20179 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1cbe1d4d-947f-3432-8866-dc1c857e6977 | -15.98833 | -43.27416 | 2026-09-15 04:34:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| abce8ffe-976e-3877-a0c5-7e367a23cbec | -13.57167 | -47.90369 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c9d00a2-ac94-30cd-bed8-634e98f9f7de | -9.13229 | -51.58419 | 2026-09-15 04:34:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 323058e2-146d-3db3-a867-7e5d68ca085b | -14.76505 | -42.94966 | 2026-09-15 04:34:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.7 |
| fdfda7eb-098d-32c3-9737-442d4a7d1164 | -14.19256 | -47.42801 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9213fbb9-ca6e-3099-891b-53c3b6f2a546 | -8.80508 | -46.9065 | 2026-09-15 04:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2cf6dec-890b-3ef5-82be-5657ea6cbf48 | -8.32862 | -49.99343 | 2026-09-15 04:34:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 865214f7-0f0e-3d77-9579-7614d7ab8c9f | -14.99603 | -48.51723 | 2026-09-15 04:34:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8b9e13d8-0739-3b30-adaf-48a06103a3b5 | -8.837 | -45.87526 | 2026-09-15 04:34:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 789b3ee7-2a4b-32d8-89d5-be9f5e5fc6ed | -10.70115 | -47.50185 | 2026-09-15 04:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 14bad21b-252e-379d-8f56-c217587aa29c | -10.89535 | -51.56263 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| b5d001a9-e212-398d-9d11-9f593b591fa9 | -13.72644 | -48.97871 | 2026-09-15 04:34:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6526d96e-14b7-3f91-879b-0c8a97decc28 | -12.55724 | -47.11757 | 2026-09-15 04:34:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1abf8cf1-b42d-3e86-b649-fbc0e40c4266 | -10.99105 | -48.32424 | 2026-09-15 04:34:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6f2e0ebc-54a5-3737-9286-b38389af8761 | -10.23338 | -50.91126 | 2026-09-15 04:34:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8d8a7116-12e6-3b8a-b28f-a9cf537c1dbc | -8.48753 | -44.5846 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fef6bc5c-2a42-305b-a9de-ff5adb5ed444 | -14.85522 | -48.14018 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1712e55-01bf-3fb0-b375-e61522b275da | -9.36018 | -50.10878 | 2026-09-15 04:34:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 0ae885fb-502f-3d33-9c30-c980072a7fb2 | -11.8085 | -46.58535 | 2026-09-15 04:34:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8b7d414f-8a17-3330-adc8-3cdf6f7d91eb | -8.59125 | -44.48933 | 2026-09-15 04:34:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4d8bac44-ce36-3c37-8ffd-265be5d10e46 | -11.21424 | -43.4342 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 08528b2d-120b-3a56-9466-c3fcdb4b1a01 | -8.08426 | -50.9689 | 2026-09-15 04:34:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c46db2eb-dc11-3198-80f4-216b185bae19 | -8.80405 | -50.49265 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62050f1d-2c09-33dd-8bae-d09c25ecb989 | -12.47963 | -41.39977 | 2026-09-15 04:34:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 8f90594d-2a20-358f-b2b7-864b733878a9 | -11.04768 | -47.94989 | 2026-09-15 04:34:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dbd3f49c-80bf-3ccc-9ebd-bf6fd6b6405c | -10.87736 | -54.01703 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 646e354b-1033-3b63-8043-fc3e0f9ec015 | -15.16788 | -43.84615 | 2026-09-15 04:34:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 42c1925e-5049-3200-8b70-f83b6c8fc49a | -8.80453 | -46.90998 | 2026-09-15 04:34:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 27e6e9ad-b629-3659-b7f8-8eb15c62d91a | -15.03518 | -48.52747 | 2026-09-15 04:34:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aee5f389-d8b4-3b71-9148-44f295bf15e6 | -10.89157 | -51.56197 | 2026-09-15 04:34:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a06a21b8-0e3e-3fbc-b6ca-3fe747d48a84 | -14.04192 | -43.29303 | 2026-09-15 04:34:00 | NOAA-20 | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 32d7fe07-4272-399e-8200-8bbf487b5a78 | -11.23293 | -43.46588 | 2026-09-15 04:34:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 462cb557-b46f-3bff-8596-806c35161a0d | -10.66962 | -54.14325 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| bcae5bfe-3046-3bbb-9000-34009ed1ce61 | -10.68107 | -54.1827 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9ac6912-876b-3ddb-96ca-78a64bcf0a83 | -13.25002 | -49.51752 | 2026-09-15 04:34:00 | NOAA-20 | NOVO PLANALTO | GOIÁS | Brasil | 5215256 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| dee63573-d199-3b1a-aeb2-a202e02b985f | -14.20645 | -47.42651 | 2026-09-15 04:34:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a8ce79f8-57e9-3e93-811a-a6b446ab04c2 | -13.57498 | -47.90424 | 2026-09-15 04:34:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 22b74e95-28e0-3f7e-a186-48417e6e4f58 | -10.69688 | -54.17173 | 2026-09-15 04:34:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4fe6dbf8-5df2-35d8-b947-f7dc11f294a5 | -11.12024 | -40.47256 | 2026-09-15 04:34:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| aa6fe605-18bb-32d4-bbe8-92ae9d314c1c | -11.5028 | -45.79212 | 2026-09-15 04:34:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 844a9dbf-8f57-35aa-bdbc-1289f9e49f51 | -14.76793 | -42.94982 | 2026-09-15 04:34:00 | NOAA-20 | ESPINOSA | MINAS GERAIS | Brasil | 3124302 | 31 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ccc26af3-54e9-3561-9c65-01e30d8c31ce | -8.46895 | -50.77791 | 2026-09-15 04:34:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bca2d428-57e8-3ad8-bb94-ce2bc7ce08ec | -14.95698 | -47.53177 | 2026-09-15 04:34:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 28312c84-cef2-3767-81a7-e116095586d6 | -9.88927 | -47.77882 | 2026-09-15 04:34:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d44f2e65-2ae9-3b3d-8503-156956061deb | -15.28287 | -42.7892 | 2026-09-15 04:34:00 | NOAA-20 | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22e105af-df2b-3f58-a231-b5ce69543544 | -8.64614 | -48.59422 | 2026-09-15 04:34:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a93f3058-facf-3fd2-95f1-37b1e8d7c58d | -15.586 | -42.5735 | 2026-09-15 04:34:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 33.7 |


[Clique aqui para ver as próximas entradas](README47.md)
