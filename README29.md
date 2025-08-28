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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 701b4937-a2ef-3f9f-bc02-7085ae0a7889 | -16.64427 | -46.72284 | 2025-08-28 03:49:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3913f194-b9e8-3b39-8346-43a7efb204f8 | -17.54902 | -46.61819 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 37dd85b5-5a3d-362f-862b-8eba1d8700b7 | -17.90741 | -44.25447 | 2025-08-28 03:49:00 | NPP-375D | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a8dc392e-ddd7-31a4-832a-d6ee0c738c1c | -17.54772 | -46.62449 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a51cdb8-2b29-3ce8-aa27-33c1202a2503 | -29.77706 | -51.17793 | 2025-08-28 03:49:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 91e1806a-e9f0-3053-8792-c4f4c2d7093e | -17.81622 | -44.51023 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 33caf232-fd9d-35f2-bc5b-649436909596 | -17.54837 | -46.62135 | 2025-08-28 03:49:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53b88941-7b42-3a93-82d0-1f2590fae74e | -17.76705 | -44.4908 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 652487ad-e385-3aeb-a9e9-d2c15cdf2298 | -19.06186 | -42.13291 | 2025-08-28 03:49:00 | NPP-375D | FERNANDES TOURINHO | MINAS GERAIS | Brasil | 3125804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| 377b34e4-a673-3ada-a9a5-4d36145a704f | -18.18725 | -45.56511 | 2025-08-28 03:49:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80e95e2e-a6a0-354b-8d1d-a5f6cdfc97ec | -29.77794 | -51.17422 | 2025-08-28 03:49:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| fcfa6a7c-b9b7-3aeb-ac3c-9190b992cee9 | -19.1128 | -44.02212 | 2025-08-28 03:49:00 | NPP-375D | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ef7033b1-5789-35e6-89f3-3082d610ebf4 | -17.81723 | -44.51796 | 2025-08-28 03:49:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc352499-e13e-393e-8664-78dc786492a1 | -17.77638 | -48.4999 | 2025-08-28 03:49:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 30f717e2-6a03-3f52-830f-0d68bc292c09 | -9.0969 | -65.7892 | 2025-08-28 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.9 |
| 59daf80b-78f0-3887-a7d8-2ceb4e213928 | -8.433 | -41.4559 | 2025-08-28 03:50:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 181.3 |
| e7fb6e32-d5fa-3b06-9cdd-d974091ee5dc | -8.9479 | -65.9616 | 2025-08-28 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 47.8 |
| ad29bf38-676a-3310-9e7c-e8c123abc6b0 | -7.3958 | -39.6595 | 2025-08-28 03:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 51.7 |
| 1a0c8a51-c92c-35a9-99ad-55f22f03d32d | -8.4333 | -41.4316 | 2025-08-28 03:50:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 73.7 |
| 12cf4bda-1780-3005-8de8-225595db6c64 | -6.8772 | -43.6152 | 2025-08-28 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 130.4 |
| 030ac3d6-9b2b-336e-8230-854b21585e23 | -7.3955 | -39.6845 | 2025-08-28 03:50:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 133.8 |
| abb0ceb5-97d8-3212-be95-b3e914a8ae92 | -9.1155 | -65.7699 | 2025-08-28 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 121.2 |
| 4318b028-4c57-3aaa-9596-2a1e95166e90 | -9.134 | -65.7694 | 2025-08-28 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 101.9 |
| 7a42a400-0831-3dc6-a174-3168564eefd3 | -8.452 | -41.4536 | 2025-08-28 03:50:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 97.7 |
| a4d616b1-6292-3572-ba55-a21628ddc2a5 | -9.1339 | -65.788 | 2025-08-28 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 196.0 |
| ad66c71c-c383-323f-97a5-4e52423fda9e | -10.4736 | -57.9563 | 2025-08-28 03:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 73.4 |
| a1d3dc80-dbc6-3838-9863-78a17e781a0c | -6.896 | -43.6135 | 2025-08-28 03:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| f72dde9f-1822-3e92-8ba3-698224f38c94 | -7.3542 | -59.6476 | 2025-08-28 03:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 37.6 |
| f2b7f900-01bf-3fda-9063-fb52f1859bae | -9.1154 | -65.7886 | 2025-08-28 03:50:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 274.0 |
| 7207604a-1a5e-3bc7-ae94-bd742621a9ed | -10.4738 | -57.9366 | 2025-08-28 03:50:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 0ab60d60-6b6c-374c-95ac-a87ec1c65776 | -9.1154 | -65.7886 | 2025-08-28 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 246.7 |
| 3129794d-22a6-3463-8a11-89db3145f11b | -8.2896 | -45.1357 | 2025-08-28 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 38.9 |
| c893455e-8c93-3cde-82d1-55994f71cfa9 | -8.2705 | -45.1605 | 2025-08-28 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 150.0 |
| cdf4bc96-1c0d-33a9-99d6-9164b0e2d775 | -9.406 | -60.5711 | 2025-08-28 04:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e403fc26-470a-3f5c-a26a-e4dd6ab8cc81 | -9.134 | -65.7694 | 2025-08-28 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 96.7 |
| ca1d90a5-e068-39b8-bb54-1c6c474a2b0b | -7.3955 | -39.6845 | 2025-08-28 04:00:00 | GOES-19 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 119.1 |
| 17f66e36-b4f7-34f0-b705-d6ef520e4e1c | -8.433 | -41.4559 | 2025-08-28 04:00:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 136.6 |
| ca3115e0-5ab0-3ee4-9ead-f318d5890769 | -9.1339 | -65.788 | 2025-08-28 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 195.6 |
| 47402776-fa78-356b-a7fd-a7c12d43066f | -8.9479 | -65.9616 | 2025-08-28 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 1a6a6ab6-2f5e-3835-9b78-ee1c9ff34149 | -10.5375 | -46.6894 | 2025-08-28 04:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 54.1 |
| 73ce8b77-5803-3a80-9825-6b46cd0612ac | -8.452 | -41.4536 | 2025-08-28 04:00:00 | GOES-19 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 112.1 |
| 54d1379a-09fd-35d2-b734-1f5b1246d589 | -8.289 | -45.1814 | 2025-08-28 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 183.8 |
| a9272399-06bb-3367-8b6a-6a492886cfa2 | -7.3542 | -59.6476 | 2025-08-28 04:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.7 |
| 6530eb8b-d59a-3052-95a8-2d98e757dead | -9.1155 | -65.7699 | 2025-08-28 04:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 113.3 |
| 983057e8-993b-3f3b-b2d6-66e9f3a70ae9 | -6.8772 | -43.6152 | 2025-08-28 04:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 141.3 |
| 0968cf8c-dcbf-343d-8415-137699b4cb80 | -8.2702 | -45.1833 | 2025-08-28 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 03966ac0-f74c-3113-8657-93afaed75a59 | -8.2893 | -45.1586 | 2025-08-28 04:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 190.4 |
| 4f44c20f-6e82-3f24-a855-d8391036be26 | -7.38413 | -39.68986 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| e8f6a6ac-a020-3fec-b910-e744a7037297 | -6.57508 | -47.38277 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dabdec5f-4a23-3cce-b40a-b1dbb8d051af | -6.18636 | -44.03467 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9d79ef3a-a028-35e0-8836-1ffdbc021c99 | -5.15826 | -47.84737 | 2025-08-28 04:06:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2e2867d2-aa06-3bab-857f-9840fdd514e9 | -4.15652 | -43.88285 | 2025-08-28 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 96eebd25-a294-31b2-be67-b7059f266eda | -6.17839 | -44.06149 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ba03bf4d-c8a4-3e1c-945f-ca1f0ecd3ec0 | -6.57164 | -47.37599 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e87e1fe1-020e-30f9-9f59-a30dc8f9707c | -6.88153 | -43.62085 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| b176d09f-e9ff-358b-a915-d2a38a7aa640 | -6.86165 | -43.61399 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ea9361fb-ceee-312d-8a85-e88bf176e3e1 | -6.15832 | -44.38484 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b45eca67-565f-39b5-a43b-eb8c323c904f | -6.52801 | -42.98015 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7e2148ff-c0db-3051-9031-e3e537dd6912 | -6.24177 | -43.82562 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a0b1c3e8-058b-30d1-b31f-bb695bfcb143 | -6.86671 | -43.62629 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 4e11fd7c-9efb-3f27-9d58-c25ea9642416 | -7.06 | -44.36486 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c1f7037-ac47-3111-b41f-97f04e815963 | -7.06703 | -44.36607 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e1cf29d-8023-384d-b7a5-ebf422af1ddb | -6.71388 | -43.0913 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4e3c2038-a255-3aa8-81ee-7e56adcee317 | -6.4347 | -44.57663 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 7129484c-7bf9-3c4d-a0b5-df936bb01969 | -4.29335 | -40.93862 | 2025-08-28 04:06:00 | NOAA-20 | CROATÁ | CEARÁ | Brasil | 2304236 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cee52153-ac5d-3dd8-b4e3-bb870deb65ba | -6.44187 | -44.57772 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| e5687916-8c9c-3293-9c49-58899fdc053c | -4.87812 | -44.95572 | 2025-08-28 04:06:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f94c9937-4da8-3274-b417-d3501d9f9f97 | -6.26606 | -43.8294 | 2025-08-28 04:06:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4828b1c-d6bd-352c-8823-d82fe3e8a902 | -6.07645 | -43.99738 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a832c40a-0105-3fe1-808e-6211e67d19f6 | -6.30993 | -42.48966 | 2025-08-28 04:06:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2ab3898b-cdd8-3d02-80da-25d2addd07a9 | -4.08105 | -48.04367 | 2025-08-28 04:06:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a8bef25-379b-3b18-a72b-4e1affec3e19 | -4.15717 | -43.87881 | 2025-08-28 04:06:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d118d1f3-f635-3f52-8e10-847d033b34e7 | -7.39847 | -39.68821 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 0aa73128-d4a8-3b39-998c-11e3db43cc70 | -7.06767 | -44.36211 | 2025-08-28 04:06:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6d995a0a-3990-318a-84d6-171a501c4fd0 | -5.20917 | -44.31995 | 2025-08-28 04:06:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0dba983-4697-3f99-98a8-1ca53e4f9c66 | -4.63535 | -41.39809 | 2025-08-28 04:06:00 | NOAA-20 | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4bc19452-816d-39f3-af25-472c6c74d386 | -6.28038 | -44.48218 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11bcc158-09e7-375e-b0e2-d2646ef58378 | -5.43735 | -46.2864 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a358212d-3c0a-3874-b46a-3c8455be44fc | -5.22816 | -46.08913 | 2025-08-28 04:06:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce12e220-4e11-3275-b114-76a3333b3af5 | -7.62597 | -42.69661 | 2025-08-28 04:06:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 7f0362c2-e420-3bec-9168-192c5fa98107 | -6.52859 | -42.97657 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b90add97-7260-3342-a8d6-b8f038bd4ae0 | -6.87207 | -43.59273 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 21d886e7-537c-35da-ab1c-a9c4327fc794 | -6.7086 | -43.14603 | 2025-08-28 04:06:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d2194d0-aa19-3231-adce-94d4a94fbbae | -6.76431 | -44.8267 | 2025-08-28 04:06:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7284ae18-d36a-3cdc-bdfe-a92bb8a8566f | -7.39273 | -39.6796 | 2025-08-28 04:06:00 | NOAA-20 | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 708d4549-144a-3a54-b1b7-a689f07942d4 | -6.43895 | -44.57312 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6165d301-6862-3350-b50d-8bdd6390c19d | -6.57087 | -47.38202 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 2f2f9701-7c3e-3844-96eb-e3f06eaf4848 | -6.18126 | -44.0659 | 2025-08-28 04:06:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 733d684c-bd18-3eac-8a57-7c5805b1ae77 | -6.15992 | -44.39742 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6e148f89-9ec4-30cb-b398-d0d1260b736a | -7.66042 | -42.65178 | 2025-08-28 04:06:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8a284dad-d53b-3d69-a3b6-b196a1a02d92 | -6.22488 | -43.36455 | 2025-08-28 04:06:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60032777-2a6d-38c4-b901-e914fd5db06b | -6.86791 | -43.61882 | 2025-08-28 04:06:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 100346c5-1bc5-362e-b7ec-680f93ba168c | -7.15328 | -44.14935 | 2025-08-28 04:06:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c4137ba2-e31a-34a8-bf58-26f7232e7be2 | -7.42578 | -40.08059 | 2025-08-28 04:06:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ff57c3b6-fd5a-3591-b62f-62c4b2c79e2a | -6.5673 | -47.3773 | 2025-08-28 04:06:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4287f89b-101e-30a5-b0bd-04c9f4be5b22 | -6.43761 | -44.58126 | 2025-08-28 04:06:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86690b55-820d-36fd-b740-d3009ed2ab9a | -7.17493 | -43.84311 | 2025-08-28 04:06:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c4286d54-8997-3980-899e-a9858a5614e8 | -6.36764 | -44.05137 | 2025-08-28 04:06:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 06abc922-7cc3-3197-9298-d1fbc2148029 | -5.47893 | -41.41079 | 2025-08-28 04:06:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b05dbbdc-f334-31e8-84ce-888ca04b9d03 | -5.89957 | -45.56282 | 2025-08-28 04:06:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |


[Clique aqui para ver as próximas entradas](README30.md)
