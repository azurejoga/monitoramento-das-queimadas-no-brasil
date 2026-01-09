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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 90f5d1fe-ef79-3a90-89f3-5139d6f6b4d1 | -4.2726 | -43.7832 | 2026-01-09 01:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.5 |
| 566122dd-2879-3f69-bda3-08b52230fc5b | -4.2539 | -43.7843 | 2026-01-09 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 286ead02-47f2-386a-ac70-015f3e021c9e | -3.3069 | -50.8064 | 2026-01-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 507f3468-531f-3f0f-be9b-38ea8e7444f4 | -4.2726 | -43.7832 | 2026-01-09 01:40:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 92.9 |
| 5656ee2b-7981-3497-88f3-57048d2fd834 | -3.3068 | -50.8273 | 2026-01-09 01:40:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.6 |
| c696324a-346d-353d-b672-70ab0e62342e | -4.2726 | -43.7832 | 2026-01-09 01:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| faad4b9a-32ed-3c55-aa7c-c29c02cb76b1 | -4.2726 | -43.7832 | 2026-01-09 02:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 507b5263-ad3e-32da-9518-64edb021091b | -4.2726 | -43.7832 | 2026-01-09 02:10:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.3 |
| f51df00e-5f75-3bd9-a12b-d6d8d69efa03 | -4.2726 | -43.7832 | 2026-01-09 02:20:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 83.2 |
| 0aef9407-b6fb-37a6-960e-82b044761a0d | -4.2726 | -43.7832 | 2026-01-09 02:30:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 87.0 |
| a7f5530b-286b-3a36-92e6-dcc044139568 | -4.2726 | -43.7832 | 2026-01-09 02:50:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| fc825047-5478-30c2-9bf8-db215b7e6d92 | -4.2726 | -43.7832 | 2026-01-09 03:00:00 | GOES-19 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| 095a6e4b-31e1-3366-9a1e-1ee6f4cdb939 | -6.1629 | -35.18927 | 2026-01-09 03:04:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b443a908-5060-30e7-af4c-04be7f085f1f | -5.7494 | -35.38321 | 2026-01-09 03:04:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 18fde2bf-a482-31fd-bee7-afb6acf6d4e7 | -5.57142 | -36.25503 | 2026-01-09 03:04:00 | NOAA-21 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| c166ebfc-4a0a-3754-92a9-994f7e0c810d | -5.57066 | -36.2593 | 2026-01-09 03:04:00 | NOAA-21 | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| ed9f7b91-c843-3ac2-8301-749086aeb80b | -6.16456 | -35.19135 | 2026-01-09 03:04:00 | NOAA-21 | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| f0f1abc3-6da4-3d65-9a33-f4a1f2d991b1 | -6.16229 | -35.1928 | 2026-01-09 03:04:00 | NOAA-21 | NÍSIA FLORESTA | RIO GRANDE DO NORTE | Brasil | 2408201 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ce1a2136-f7e0-38fa-bc27-c1c7b5990723 | -5.74875 | -35.3869 | 2026-01-09 03:04:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 00db2347-0098-3e2a-bd60-c3b1d89a407d | -7.34197 | -34.95824 | 2026-01-09 03:06:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 60e16f42-f47f-3d28-8bcd-3528a503fe4d | -10.9199 | -37.52289 | 2026-01-09 03:06:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 25d332e5-c11f-39e4-a276-031e4e0015a3 | -8.78463 | -35.6925 | 2026-01-09 03:06:00 | NOAA-21 | PALMARES | PERNAMBUCO | Brasil | 2610004 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 811e81fb-d988-3a86-a8bf-58f5b8b251f8 | -6.94183 | -35.1172 | 2026-01-09 03:06:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| e8c69d30-7fbe-3b38-b74e-4acea10c97e8 | -6.83237 | -35.0624 | 2026-01-09 03:06:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9bba1595-3558-3358-9461-c4e43a293fbb | -9.96274 | -36.37993 | 2026-01-09 03:06:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ab343f98-8d8f-3280-97fc-968ebb72671d | -10.92093 | -37.51728 | 2026-01-09 03:06:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0eadbe51-07be-3eb9-b5cb-9430b32274c6 | -7.40194 | -35.16708 | 2026-01-09 03:06:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| a47fcb38-aaf2-3330-8449-7f3507d2f8ba | -10.92011 | -37.52144 | 2026-01-09 03:06:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| ff0dd975-56b0-35d4-bcb4-c19811c639d3 | -9.96412 | -36.37268 | 2026-01-09 03:06:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64b75583-3529-329f-b9ce-c6a787b2ff99 | -6.83067 | -35.06428 | 2026-01-09 03:06:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d87dbb8d-3045-3f33-8acc-6e8ca48bc82b | -10.92149 | -37.51455 | 2026-01-09 03:06:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9f11796f-7597-30b5-aaa5-6c697c28083d | -7.34254 | -34.955 | 2026-01-09 03:06:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| c9b98ccc-4b50-3fec-9821-92fa467f3537 | -9.96343 | -36.37629 | 2026-01-09 03:06:00 | NOAA-21 | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 780d46e1-8066-39d0-bc86-28c455f277d9 | -7.5751 | -34.95421 | 2026-01-09 03:06:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| e84e0bd9-f8cb-3990-8006-38c5a988cd82 | -10.92069 | -37.51876 | 2026-01-09 03:06:00 | NOAA-21 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 80cc2ab8-5359-31a0-b665-7eec3ff849a4 | -7.40431 | -35.24566 | 2026-01-09 03:06:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a9ef4768-7747-3d25-9ae7-77169cd57e6e | -6.72185 | -35.25146 | 2026-01-09 03:06:00 | NOAA-21 | CURRAL DE CIMA | PARAÍBA | Brasil | 2505279 | 25 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c95b9b05-f053-3256-ac1a-24ef615d7f36 | -7.34779 | -34.95581 | 2026-01-09 03:06:00 | NOAA-21 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 8ad16046-245f-3010-bc62-a5ac47f36ded | -6.83179 | -35.06576 | 2026-01-09 03:06:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 7d24fcf2-0537-3cc9-82e5-3f9980630410 | -7.40253 | -35.16376 | 2026-01-09 03:06:00 | NOAA-21 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 28f9405b-8017-3fb6-b2d8-2ac818ca34fe | -22.92258 | -42.45153 | 2026-01-09 03:10:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.5 |
| 2007fa09-d857-36c4-a03e-976ea955ecaa | -22.92131 | -42.45675 | 2026-01-09 03:10:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| b6234da6-92d9-3327-bf13-41f27ecc8004 | -22.91516 | -42.45504 | 2026-01-09 03:10:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 075f9282-9f44-311a-859f-8c83ec1900f1 | -22.92006 | -42.46189 | 2026-01-09 03:10:00 | NOAA-21 | SAQUAREMA | RIO DE JANEIRO | Brasil | 3305505 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.0 |
| 321ea339-3b13-303c-b0b0-09082fe27357 | -7.71285 | -35.09538 | 2026-01-09 03:34:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b6c6413c-95db-30f5-be6a-4f0bb55ae471 | -4.27209 | -43.78891 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e2df09cf-19ea-3c78-83c3-26e90515cf15 | -5.75024 | -35.38363 | 2026-01-09 03:34:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| fd704bac-6f81-3650-8dc1-d31f86241729 | -6.33463 | -39.61609 | 2026-01-09 03:34:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 5087b720-e27d-3004-92b9-da281838e8a9 | -6.46699 | -39.78109 | 2026-01-09 03:34:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 9b6d2693-f76b-34f2-ae33-d5e095d723aa | -7.40687 | -35.24613 | 2026-01-09 03:34:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 410af2b9-6486-39ea-b036-6c6730c3c857 | -6.85118 | -35.69651 | 2026-01-09 03:34:00 | NPP-375D | SERRARIA | PARAÍBA | Brasil | 2515906 | 25 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 51a20017-3bdc-3fa4-9ddf-f18a00c5e3a5 | -6.53002 | -40.32383 | 2026-01-09 03:34:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 07e3d0e1-e5e1-378f-a39e-a9e16094ead5 | -7.11224 | -35.13043 | 2026-01-09 03:34:00 | NPP-375D | CRUZ DO ESPÍRITO SANTO | PARAÍBA | Brasil | 2504900 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b4092726-e836-35b7-8cc3-1b65eaaa8d27 | -4.25362 | -43.77987 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| def8ac63-566c-3f6e-9744-fa31b340c8f9 | -6.33553 | -39.61084 | 2026-01-09 03:34:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 60c98df9-2e9b-352e-80ce-631c96df62e0 | -6.31774 | -38.31697 | 2026-01-09 03:34:00 | NPP-375D | JOSÉ DA PENHA | RIO GRANDE DO NORTE | Brasil | 2406007 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 7796826c-5aa6-3db1-84f6-810d32386367 | -4.26636 | -43.78339 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 56832436-7b7c-3e00-a5b8-6d2defaf6073 | -7.40329 | -35.24556 | 2026-01-09 03:34:00 | NPP-375D | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5da6bb28-4b68-3181-a52b-01b1161d34de | -3.85534 | -42.25804 | 2026-01-09 03:34:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 31433a7c-67ac-3c67-a9c1-23f30767c84b | -4.26564 | -43.78761 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 04fb6d68-e18d-3acb-ada1-49de1c617141 | -4.2654 | -43.78881 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 02012eee-dccc-379d-9bd8-0c7104be33fb | -4.27185 | -43.79008 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 286891c2-0196-31d8-9006-e5c8ae53a9b0 | -4.25342 | -43.78112 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 221f2c74-dee6-32f8-9df8-c84db3ddaea2 | -3.26103 | -42.54633 | 2026-01-09 03:34:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e45257bc-1340-3e09-b50f-b97f2a6ff03a | -5.74586 | -35.38738 | 2026-01-09 03:34:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 54676b10-b629-3f04-a1e9-40a7e1b76a8f | -4.45069 | -44.13257 | 2026-01-09 03:34:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4c80ce3e-ee07-38c3-9465-341ffa9b292f | -4.6844 | -43.24709 | 2026-01-09 03:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48bd5acf-8d63-35d4-878f-79290a897703 | -4.4573 | -44.13361 | 2026-01-09 03:34:00 | NPP-375D | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 957b4f81-0c41-3e6a-b4e0-1b20798899f3 | -3.85606 | -42.25379 | 2026-01-09 03:34:00 | NPP-375D | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2b90360e-a627-3223-afd2-42b5ec2246d0 | -4.26657 | -43.78215 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6e28cb6-f9e0-3e05-b146-22bf1dc41999 | -5.57155 | -36.25697 | 2026-01-09 03:34:00 | NPP-375D | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 0e7e0dcc-57db-3651-9b1e-46dd339386bf | -6.36361 | -35.11974 | 2026-01-09 03:34:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 576add6d-ed81-3d53-9b61-d53f74aa788c | -4.27305 | -43.78328 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1677a0f3-22e1-3460-952e-d030ab0ce546 | -5.56769 | -36.25632 | 2026-01-09 03:34:00 | NPP-375D | PEDRO AVELINO | RIO GRANDE DO NORTE | Brasil | 2409704 | 24 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4039c3a9-5641-31b7-abd0-8401d20c6bba | -2.83823 | -40.17597 | 2026-01-09 03:34:00 | NPP-375D | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 70dd2a3e-27f2-37ef-ba6f-e2986e35b7fe | -4.2544 | -43.77562 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 042f2937-4915-352d-b865-26a80313526e | -7.64975 | -34.95171 | 2026-01-09 03:34:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| ae917891-57f1-3163-bcca-8107c95235e2 | -3.26713 | -42.54731 | 2026-01-09 03:34:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e4c613e-e090-34d0-9293-85c41f693475 | -7.83915 | -35.3632 | 2026-01-09 03:34:00 | NPP-375D | LAGOA DO CARRO | PERNAMBUCO | Brasil | 2608453 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b49e662b-2f19-3d3c-b9c6-886fa6e25fcf | -3.26181 | -42.54173 | 2026-01-09 03:34:00 | NPP-375D | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ac3fd1ba-5b07-38d1-931c-b41db02f0a2c | -6.46228 | -39.77969 | 2026-01-09 03:34:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3f7ffd6d-38d3-3c73-ba4f-329f43f32778 | -7.57757 | -34.95321 | 2026-01-09 03:34:00 | NPP-375D | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| a15b2534-6b64-3620-bac8-dbf41b1209fc | -6.46282 | -39.78357 | 2026-01-09 03:34:00 | NPP-375D | SABOEIRO | CEARÁ | Brasil | 2311900 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 1df06fe4-932e-367a-92dd-592646cbf5cb | -6.30503 | -39.39343 | 2026-01-09 03:34:00 | NPP-375D | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4f6ac205-68df-3fe2-8c8b-2ac185a16191 | -5.75475 | -39.79853 | 2026-01-09 03:34:00 | NPP-375D | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a93859b1-8d4c-361e-8c17-9b916394a145 | -6.16631 | -35.19056 | 2026-01-09 03:34:00 | NPP-375D | ARÊS | RIO GRANDE DO NORTE | Brasil | 2401206 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 2aac10cd-f246-34a1-8e99-af58fe35976c | -3.35813 | -39.13148 | 2026-01-09 03:34:00 | NPP-375D | PARAIPABA | CEARÁ | Brasil | 2310258 | 23 | 33 | nan | nan | nan | Caatinga | 49.8 |
| d0c3e8eb-ca4d-3cc5-bc14-b0f8d268e813 | -7.31334 | -35.15691 | 2026-01-09 03:34:00 | NPP-375D | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c1c14a65-0a10-3353-9d2b-d119686f3412 | -5.74954 | -35.38794 | 2026-01-09 03:34:00 | NPP-375D | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| bdf4fd4f-39f7-369f-83da-0c6c22de8620 | -5.33365 | -37.31119 | 2026-01-09 03:34:00 | NPP-375D | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2ddf8eda-406b-3ecd-99d5-ad119ef3cb38 | -5.82258 | -35.8167 | 2026-01-09 03:34:00 | NPP-375D | RIACHUELO | RIO GRANDE DO NORTE | Brasil | 2410900 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9d5fd5cf-1e53-33f8-93c8-191eb16818c2 | -5.67594 | -39.29056 | 2026-01-09 03:34:00 | NPP-375D | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79ac9436-1eb8-3cbc-b4f1-23df7cf5e6db | -4.27283 | -43.78457 | 2026-01-09 03:34:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 30046c59-0177-3456-afbc-bb0afd623868 | -4.67819 | -43.24589 | 2026-01-09 03:34:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18943acd-c46f-3fba-a3c8-7983bac925e7 | -7.64036 | -35.03113 | 2026-01-09 03:34:00 | NPP-375D | ITAQUITINGA | PERNAMBUCO | Brasil | 2607802 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 7aadc368-36f8-3186-87f1-b5503930fd77 | -11.82579 | -46.61238 | 2026-01-09 03:36:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 318d2445-4130-39ad-b9cd-109f634dd1ad | -10.92161 | -37.51475 | 2026-01-09 03:36:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| dce1ad9d-a246-3179-929b-08d7769061d4 | -9.6499 | -42.9559 | 2026-01-09 03:36:00 | NPP-375D | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e10a575d-eee0-3182-9bb0-95b27a273b1b | -9.96733 | -36.37492 | 2026-01-09 03:36:00 | NPP-375D | TEOTÔNIO VILELA | ALAGOAS | Brasil | 2709152 | 27 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 6f4f79a3-28ef-3b42-bc5f-1656a5808194 | -10.92243 | -37.5099 | 2026-01-09 03:36:00 | NPP-375D | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |


[Clique aqui para ver as próximas entradas](README3.md)
