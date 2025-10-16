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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cea24fdc-26db-3faa-8fac-12f92abf148e | -4.4061 | -43.3816 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 9cb406b1-dd90-3dc7-af74-73ab69ff2fe6 | -8.4528 | -44.1767 | 2025-10-16 02:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 83ce8bc3-7873-317f-86eb-541d5e3b7e5d | -6.1723 | -40.8954 | 2025-10-16 02:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 92.8 |
| ba643d0d-d1fa-356d-9704-b516e3e3d613 | -12.6805 | -43.4235 | 2025-10-16 02:50:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 1c116cb2-fc96-3031-8c24-b8df437adc90 | -5.4575 | -42.9381 | 2025-10-16 02:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 56.1 |
| d3466802-3cb6-35b3-8b7a-529bb57e3008 | -5.5147 | -47.3069 | 2025-10-16 02:50:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 134.0 |
| 6014075b-8008-36b0-8dbc-181e22a737ca | -4.0976 | -48.0144 | 2025-10-16 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 130.5 |
| fde85792-8239-32a7-a52d-8892385d6ca2 | -6.172 | -40.9198 | 2025-10-16 02:50:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 41.6 |
| 56a66b65-535d-3e3c-a3eb-d8f6fdfc6cd3 | -3.0158 | -45.3679 | 2025-10-16 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 7906240b-622d-36e5-a15b-5fc25a97c1a6 | -5.8802 | -43.8613 | 2025-10-16 02:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 7e2fa21b-8d60-35d1-a300-cc1338950a98 | -3.0157 | -45.3903 | 2025-10-16 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 217.0 |
| bd43b46a-7203-3b9b-ab45-1511988debc8 | -4.3498 | -43.4082 | 2025-10-16 02:50:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 87254e70-67bf-3902-9edb-a4bf4ba3eac8 | -4.1161 | -48.0136 | 2025-10-16 02:50:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 121.5 |
| de264606-879b-3101-8774-22b397b6a09f | -3.0343 | -45.3896 | 2025-10-16 02:50:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 37.0 |
| 320d657f-0841-3386-a54b-ed5023fd5672 | 1.8401 | -55.7429 | 2025-10-16 02:50:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 9b029c42-2dc0-3b1a-a625-5d3145d9d5be | -5.4762 | -42.9367 | 2025-10-16 02:50:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 103.0 |
| 421e4e1b-0c6b-3289-9412-06177c0ada13 | -7.9628 | -44.1362 | 2025-10-16 02:50:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 78.2 |
| cd48f3ac-2c0c-3d17-b4f4-af44ec9cda51 | -8.4714 | -44.1978 | 2025-10-16 02:50:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 74.6 |
| ca332f7f-f6fd-39c6-8c65-a8a886632995 | -9.55642 | -36.89948 | 2025-10-16 02:58:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 29e01c2c-10af-361e-8dac-29b70f418df8 | -8.55956 | -36.25552 | 2025-10-16 02:58:00 | NOAA-21 | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| c1733acf-a5b1-3e1f-8ef8-e59a713cc915 | -5.79134 | -35.60113 | 2025-10-16 02:58:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| a5daebdf-9122-36c1-b1b5-9516a07f5f6d | -7.65798 | -34.9864 | 2025-10-16 02:58:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 7d4622dd-1cd7-38ad-ad25-87753a8de3e7 | -5.79853 | -35.59704 | 2025-10-16 02:58:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 4ffc25a8-c212-34b5-800f-36e1cf864d85 | -5.79363 | -35.59941 | 2025-10-16 02:58:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 9.6 |
| b5e2a675-60b1-3a15-8ac3-85ea35df5a63 | -7.65723 | -34.99048 | 2025-10-16 02:58:00 | NOAA-21 | GOIANA | PERNAMBUCO | Brasil | 2606200 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e65c93b1-6712-383f-aef7-7812c34bb958 | -5.79759 | -35.60216 | 2025-10-16 02:58:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1ea3e5ea-26b1-3e8f-8290-97ae49b3d742 | -5.79225 | -35.59615 | 2025-10-16 02:58:00 | NOAA-21 | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 11211473-b2ba-399a-83a9-445db2091d9a | -9.55746 | -36.89422 | 2025-10-16 02:58:00 | NOAA-21 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 2.6 |
| d69cc1d0-c0f9-3012-9680-963f7907df23 | -5.496 | -47.308 | 2025-10-16 03:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 9e553b12-309b-3b10-8ed3-d0cc2b1714cc | -4.6626 | -44.0832 | 2025-10-16 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 944f1a9f-4391-362e-9110-767ff48e2ad2 | -4.3498 | -43.4082 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.1 |
| f27d4cd7-f192-343c-8c9b-b180dcf9521c | -8.4717 | -44.1746 | 2025-10-16 03:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 95.7 |
| b7bcfa48-4b76-351e-95f2-a32639ff17da | -5.8799 | -43.8844 | 2025-10-16 03:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 674c8a43-8a8d-3659-ba68-95877b5cf157 | -9.5339 | -40.3531 | 2025-10-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 73.5 |
| 19ac5bff-8410-38e0-bd79-7c5ba29ba56b | -4.0974 | -48.0361 | 2025-10-16 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 80.8 |
| 547a7cb0-b04b-3881-9a67-956a7af9dd4c | -4.6624 | -44.1062 | 2025-10-16 03:00:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 3fd71c3a-f54f-3885-b980-8599d531727d | -6.1534 | -40.8971 | 2025-10-16 03:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 55.3 |
| 79865a52-adbd-33ae-bc4f-aee46df83a36 | -3.0157 | -45.3903 | 2025-10-16 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 127.5 |
| a4708cf8-6f04-3419-a4ef-dd9f20eccb35 | -4.3874 | -43.3827 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 329.4 |
| 05991718-1b49-393c-bb47-6ab4920877aa | -3.0343 | -45.3896 | 2025-10-16 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 91e072fd-0f57-3ef3-afbc-c1145eca9578 | -3.0158 | -45.3679 | 2025-10-16 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 93.7 |
| cf5d2eec-8397-3dea-ab02-944f3af5a16f | 1.8401 | -55.7429 | 2025-10-16 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.5 |
| 107d95df-9e0c-3d20-9eaf-3c63c52aa29e | -4.4061 | -43.3816 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 84.0 |
| 51fe7d09-020b-3482-9924-ca628f152655 | -5.5147 | -47.3069 | 2025-10-16 03:00:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 113.4 |
| e3bb16ee-b67e-3d36-b62b-cf495af2c39d | 1.8217 | -55.7629 | 2025-10-16 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| ea76950f-5c31-38e2-b67e-a61e443cc0aa | -4.116 | -48.0352 | 2025-10-16 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 126.8 |
| 2830b3ab-2986-3edb-b6e4-7a4ca91eca0a | -4.3687 | -43.3838 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 223.2 |
| 96227ff7-441c-311c-b6b0-a380d0f9fbf9 | -7.9628 | -44.1362 | 2025-10-16 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 0297dd7a-9bd0-3730-9f79-6963ddd9129f | -4.3685 | -43.4071 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 217.0 |
| 6354f977-62d9-3135-8765-405fb8e14163 | -4.35 | -43.3849 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 37.2 |
| b1510308-67b7-3688-bfaf-74e9fd139499 | -6.172 | -40.9198 | 2025-10-16 03:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 46.9 |
| b05b8aeb-4fa5-37e1-9ccd-c367b1ffc0a5 | -9.5343 | -40.3282 | 2025-10-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 72.1 |
| d9e16c2e-f6aa-35ff-a954-49d02a8a4f2f | -4.3872 | -43.406 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 356.5 |
| 52321622-bb07-32e9-b440-a4084bd0f30a | -9.553 | -40.3503 | 2025-10-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 94.8 |
| 29eadde4-90ee-3629-8ed4-811a4ddfefc6 | -2.9971 | -45.391 | 2025-10-16 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 5f9d0657-b458-3371-bdcf-3a2de1473a65 | 1.8218 | -55.7431 | 2025-10-16 03:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| ce606d5c-6ce6-322f-9d9c-ba4535f3b030 | -7.9439 | -44.1381 | 2025-10-16 03:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 8b5bb6e5-c49d-3906-b594-9e473b49a217 | -10.133 | -44.5777 | 2025-10-16 03:00:00 | GOES-19 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 2112e784-bbb7-3cdf-81cb-b967ea2940c3 | -2.9972 | -45.3685 | 2025-10-16 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.1 |
| aacb6f9f-65ef-3903-aa5c-b81ba6c2bd93 | -8.4528 | -44.1767 | 2025-10-16 03:00:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 4748e75a-4ac5-3ea0-8570-719b9d84d832 | -4.4059 | -43.4049 | 2025-10-16 03:00:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 115.2 |
| d35e3043-2ed4-3b69-918e-27aace76e0e4 | -6.1723 | -40.8954 | 2025-10-16 03:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.8 |
| 1634b1c3-a2b5-376f-8dbb-5eddf3760572 | -4.0976 | -48.0144 | 2025-10-16 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 78fa2111-6095-3250-a859-f262ad9b3447 | -3.0344 | -45.3672 | 2025-10-16 03:00:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 32.2 |
| a279197a-9da3-336c-a78e-b9e221cdd68d | -9.5534 | -40.3254 | 2025-10-16 03:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 95.0 |
| d3cde774-67c8-3f0b-80ff-38d5fe84415f | -4.1161 | -48.0136 | 2025-10-16 03:00:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 151.9 |
| 5e8b4509-a974-3a04-8196-d3c65a5cb871 | -5.4762 | -42.9367 | 2025-10-16 03:00:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 99.3 |
| 7e08294b-90f3-3544-95ac-9914fb29b97e | -6.1534 | -40.8971 | 2025-10-16 03:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 79.7 |
| 8c2a25bd-b752-3a23-be44-d159b5e2a84e | -4.35 | -43.3849 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 44.2 |
| ee60d818-f901-3a2f-97e9-e29ed7c45fe8 | -4.116 | -48.0352 | 2025-10-16 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.4 |
| 2f86076c-a21e-3b61-af8a-a8a7001258ed | -3.0343 | -45.3896 | 2025-10-16 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 39.0 |
| fff0d73e-159c-3ba1-8fce-33048339d047 | -2.9971 | -45.391 | 2025-10-16 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 68f5bfd5-46f5-3fce-acc6-66e2247e9085 | 1.8218 | -55.7431 | 2025-10-16 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 7c194744-c545-37f5-bb47-3edb460381d6 | -7.9439 | -44.1381 | 2025-10-16 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| b45f3632-35c3-37fc-b730-7325a3828ace | -5.4762 | -42.9367 | 2025-10-16 03:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 80.0 |
| ca017244-97f6-3be3-93e4-5af2a62caa30 | -4.4061 | -43.3816 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| 95f57ba9-b447-3453-b11c-6dc558b7b777 | -8.4528 | -44.1767 | 2025-10-16 03:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 8f52bb2b-820a-3b72-95b0-184a72890e0b | -5.5147 | -47.3069 | 2025-10-16 03:10:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 83.4 |
| e76c6bb0-7b4d-3954-ac1b-06e6ef0f3114 | -8.4717 | -44.1746 | 2025-10-16 03:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 84.2 |
| 3ffed0b4-43b9-3b90-a533-5b8310395e8a | -4.7224 | -46.1608 | 2025-10-16 03:10:00 | GOES-19 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 8ff66170-0cab-3c2e-ad65-d2ac0a0a20ea | -4.3872 | -43.406 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 251.4 |
| c2f7e12e-2fca-35dc-a4cb-d46cad1d3c54 | -4.6624 | -44.1062 | 2025-10-16 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 117.3 |
| 51114a67-68b7-3ddd-9434-46d49d0572f6 | -5.8799 | -43.8844 | 2025-10-16 03:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 35.7 |
| e4cefbe3-c265-3aa4-91a1-3ebb2e25bc99 | -14.1749 | -47.9477 | 2025-10-16 03:10:00 | GOES-19 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 93.4 |
| d5ce241a-6699-3524-9972-1b3953f8af11 | -4.0974 | -48.0361 | 2025-10-16 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 88.3 |
| c6a465f7-c857-3c95-b045-f251cdf972cf | -4.4059 | -43.4049 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 62.4 |
| 81460133-b850-39d2-85db-357391f8c2f7 | -5.6821 | -45.0893 | 2025-10-16 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7b9061e6-944c-348e-9ec0-9e5f9f285a00 | -4.3874 | -43.3827 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 268.0 |
| 969a67fa-149a-3a7c-a847-556b957fae4a | -5.6819 | -45.112 | 2025-10-16 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.8 |
| 93cc42aa-38d9-316f-b161-c4834858a0ce | 1.8217 | -55.7629 | 2025-10-16 03:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 2b007796-2baa-3c2c-a8ac-712fcd48c69d | -8.4714 | -44.1978 | 2025-10-16 03:10:00 | GOES-19 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 73.1 |
| b3dddc7f-33fa-3584-8e22-ca85b15d5e43 | -5.4575 | -42.9381 | 2025-10-16 03:10:00 | GOES-19 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 48.2 |
| b50f5a63-d7e8-30a1-9e95-44e45a9b5605 | -7.9628 | -44.1362 | 2025-10-16 03:10:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 67.4 |
| 22ad65e3-2e29-30f5-8f9a-259656c90e35 | -12.6805 | -43.4235 | 2025-10-16 03:10:00 | GOES-19 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 76.9 |
| 7ca5d99d-d16b-32e5-857c-fa4616210d23 | -3.0157 | -45.3903 | 2025-10-16 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 163.7 |
| a7eda862-0c13-319e-a0bd-2710b8ab414a | -6.1723 | -40.8954 | 2025-10-16 03:10:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 87.6 |
| e5046984-d14c-3f09-b2e5-876eab70378b | -4.0976 | -48.0144 | 2025-10-16 03:10:00 | GOES-19 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 137.9 |
| f5d5d8ea-1fed-3d86-840c-f8152eb47ef0 | -2.9972 | -45.3685 | 2025-10-16 03:10:00 | GOES-19 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 36.3 |
| a8af709c-36a2-3a5e-b8f3-3f94b7ba30c9 | -4.3498 | -43.4082 | 2025-10-16 03:10:00 | GOES-19 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 40.3 |
| 614aa2d5-0cbf-3695-b4ab-7817d733272c | -4.6626 | -44.0832 | 2025-10-16 03:10:00 | GOES-19 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 93.0 |


[Clique aqui para ver as próximas entradas](README11.md)
