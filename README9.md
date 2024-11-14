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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| de2c3d7f-2bee-3ba8-a763-c1b6d4dc4c8f | -2.63332 | -46.17226 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 2e0f9c7e-8720-39c9-bdba-cc63b231bde4 | -5.35078 | -43.54683 | 2024-11-14 00:41:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d48d8769-58a0-3608-b5ab-92496b630105 | -2.17118 | -46.09714 | 2024-11-14 00:41:00 | TERRA_M-M | MARACAÇUMÉ | MARANHÃO | Brasil | 2106326 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d21f4352-72db-3c71-b637-84c562ab2b15 | -4.59532 | -47.03647 | 2024-11-14 00:41:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 5b6dd031-fef7-34a8-9548-d7bbc07e6262 | -4.41472 | -46.12393 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8f6c7ee0-649b-3749-b5b4-c0dda3db3888 | -4.79588 | -45.29132 | 2024-11-14 00:41:00 | TERRA_M-M | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3dd07d57-9027-3c8d-ae15-152fde5936b4 | -4.15479 | -46.2422 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 8e4f8a75-f466-3821-84c2-81b21f1ac530 | -3.17784 | -45.45072 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a322e503-7852-30ae-bbf4-a84708e19322 | -3.30174 | -45.67908 | 2024-11-14 00:41:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2d1b4d1f-ee10-3947-a6c7-9272e960119a | -3.0615 | -45.53653 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ec4355aa-7a1a-3a50-9d95-f817ad9c9b20 | -4.13104 | -46.94122 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c81ca68a-3742-3260-8b6f-f44450dc2462 | -2.8935 | -46.84954 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 49c1da3a-154d-35c1-9de4-a31781378ddb | -2.53803 | -45.35849 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 16450415-c905-3d8a-8222-305bcbd8546e | -3.25373 | -50.31216 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 4b9257f3-8b91-32d8-9246-d2962a4ab6a2 | -3.74026 | -50.43554 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 16.5 |
| f553834c-9016-3c7a-bc4d-c54ce5d444f1 | -1.68207 | -48.46528 | 2024-11-14 00:41:00 | TERRA_M-M | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| afc40001-851e-3c1a-aa45-0f62036c827f | -3.4291 | -43.88977 | 2024-11-14 00:41:00 | TERRA_M-M | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 96e709ec-0243-3c5e-87d2-b8ff254f31ba | -4.14525 | -46.24979 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 2cf0b1d8-ea22-3058-8d0d-b6035e399e64 | -3.36874 | -45.96588 | 2024-11-14 00:41:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e9bd584-63f0-3a35-95d8-079914304d90 | -2.54017 | -47.02497 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 45484249-bb18-3ec2-93a0-9851bc70e739 | -3.27444 | -50.05606 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 38cf28a1-3342-3417-aec0-9aa75db845f9 | -5.03082 | -43.31135 | 2024-11-14 00:41:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d2f92192-f96b-3d97-8858-7191af75e8f6 | -1.34859 | -49.1399 | 2024-11-14 00:41:00 | TERRA_M-M | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5d9b200-d9e1-3517-9e7a-06ead635d421 | -3.11513 | -45.26093 | 2024-11-14 00:41:00 | TERRA_M-M | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 48bfc08d-843a-3d70-96bc-4fd565e48865 | -4.85806 | -45.54337 | 2024-11-14 00:41:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 81da6dec-6cfc-3d45-8b5c-f66609e3e068 | -3.32317 | -44.05807 | 2024-11-14 00:41:00 | TERRA_M-M | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Amazônia | 22.1 |
| 5b55292b-ae39-3ca7-b1c9-ae69260153e2 | -6.03801 | -44.03436 | 2024-11-14 00:41:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| 547ebccc-6361-3202-80f2-1947a5e7e154 | -2.87669 | -51.79615 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 44.2 |
| 01eb0195-cb48-3132-bb6c-17085bc6a8d9 | -5.08502 | -46.17782 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ca066e6f-77f3-3f7f-844f-a5138adad972 | -4.43949 | -46.57485 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 29f73616-2202-3274-8b54-64736a4daa06 | -7.00589 | -43.58327 | 2024-11-14 00:41:00 | TERRA_M-M | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 39ccc6ea-cb7d-351b-abad-29bbb04b7060 | -3.71862 | -50.61146 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 20987783-fc70-38dc-aee6-1c27f069f9ca | -5.19831 | -44.34991 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 3f3598b2-8717-3446-aece-7dfaf97a3848 | -3.5779 | -45.61246 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 5.8 |
| df0fcc49-4772-348d-ab74-baccc073fdf5 | -5.5616 | -45.36766 | 2024-11-14 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.3 |
| 88d9ad4a-9097-3742-a2d5-dbb94a22a208 | -2.41086 | -45.23706 | 2024-11-14 00:41:00 | TERRA_M-M | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| fe61b4ba-c062-3df0-9c32-30b804757b8b | -4.29717 | -48.07143 | 2024-11-14 00:41:00 | TERRA_M-M | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 665a66ff-0819-31a2-aaae-f0fd4c8e2b24 | -2.07004 | -46.56407 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 5e768977-3fdd-3479-9bd2-b48f7a7e3e84 | -3.77525 | -41.59393 | 2024-11-14 00:41:00 | TERRA_M-M | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 05da0e1a-65a7-3942-ae68-1b7e89fb0ed4 | -2.19789 | -46.35369 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 20.7 |
| fd11ab32-4ead-36be-8eef-84f32bd0cd38 | -3.25405 | -50.39898 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 5ff73c59-1fc4-315f-a680-0063244ceead | -1.65442 | -47.48122 | 2024-11-14 00:41:00 | TERRA_M-M | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7158504-94a0-3ab5-9f5a-363ffb36db6b | -4.02336 | -46.96259 | 2024-11-14 00:41:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 2496442d-b5bc-3673-9f02-19181e9566fb | -6.1638 | -42.59647 | 2024-11-14 00:41:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 38.4 |
| ec37863b-1a5e-3be1-8bf0-1ad8e7136e90 | -6.26768 | -44.55202 | 2024-11-14 00:41:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9904fc25-176b-3f54-b773-52f4ef8adcc6 | -2.02264 | -46.9499 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 31.8 |
| 4fcde9f5-2cbb-3010-b673-c8e9b5f1a3c5 | -1.68425 | -46.57055 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2564234a-fa92-3818-9015-a53c1c061abe | -2.16873 | -46.07956 | 2024-11-14 00:41:00 | TERRA_M-M | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| e76fb657-6d30-3894-9256-af5091d245b9 | -3.42647 | -44.98309 | 2024-11-14 00:41:00 | TERRA_M-M | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 93a01775-1e7e-3f98-b2d3-64ed931c83e1 | -3.16851 | -50.44651 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| af2be8a2-9346-3242-868f-9030c02284c2 | -4.42817 | -49.68374 | 2024-11-14 00:41:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 70290e10-6a79-3cb8-a8ee-50f2922085ae | -6.0393 | -44.04355 | 2024-11-14 00:41:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 97e26ff9-3c56-3bb4-b4a4-51398672ddc9 | -3.25982 | -46.10403 | 2024-11-14 00:41:00 | TERRA_M-M | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2f890af6-a49a-34a0-9c6e-6bd8cbbf7d10 | -5.86363 | -46.41731 | 2024-11-14 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 648a222c-783b-35b0-b0ba-160ed723ff1e | -2.12295 | -50.69217 | 2024-11-14 00:41:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| ed0d9762-e03c-3e55-b0f5-a69b0ef9f41b | -2.27564 | -45.45894 | 2024-11-14 00:41:00 | TERRA_M-M | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 06568b93-b1ef-341c-8030-2826f843b9a4 | -2.65192 | -46.83708 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| b98e04ec-761b-39e7-ba1a-7a9fdcf9fe12 | -2.02593 | -46.5071 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d1a9ed6a-9670-3901-b555-cdbed67a5ee1 | -2.07753 | -46.47597 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 694037c8-a722-3707-8bb5-ed9e3c72857a | -2.37497 | -46.49683 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 3a8574b8-1052-3582-a62d-a38cfc5b55f5 | -2.09702 | -46.35624 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d1133625-215d-3909-be60-3ee78723cf53 | -2.03032 | -46.93965 | 2024-11-14 00:41:00 | TERRA_M-M | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 3a7c6e81-c283-3323-b7d3-523a5359a187 | -2.98735 | -45.87357 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8dc61608-5083-3e25-a298-31cb75e4e53a | -3.05265 | -45.53778 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.3 |
| c8308e0d-10ed-3677-a034-b68502062dfb | -2.52543 | -45.3331 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 19.5 |
| 12cb8650-b225-3999-bbeb-a7afd9e30c1e | -2.93937 | -44.99755 | 2024-11-14 00:41:00 | TERRA_M-M | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4c658631-568e-3ad5-8836-8e20e667e057 | -5.08577 | -45.98634 | 2024-11-14 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 670782e7-d018-3148-ba1c-2caf41a14af3 | -2.88369 | -40.30185 | 2024-11-14 00:41:00 | TERRA_M-M | CRUZ | CEARÁ | Brasil | 2304251 | 23 | 33 | nan | nan | nan | Caatinga | 11.4 |
| c12f47fa-bc68-3f4f-b6fd-7a0623f922a9 | -4.04123 | -47.22728 | 2024-11-14 00:41:00 | TERRA_M-M | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 12.1 |
| aec7bfa7-c519-359a-81f1-d5e9848bac5b | -3.05018 | -45.52013 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 5f01383a-97df-3962-9871-d92b43d6078e | -5.19063 | -44.36025 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 69fd31c2-310c-33cf-a8b4-a8827d2371b4 | -2.0247 | -46.49827 | 2024-11-14 00:41:00 | TERRA_M-M | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6e55885b-9770-316b-99ee-e5eb27caca5e | -4.28818 | -46.87907 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 1d801357-f3b5-3ec9-83e9-eaab837e00d3 | -5.57044 | -45.36641 | 2024-11-14 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.0 |
| d19d0e86-b012-3654-b3f0-1be6e8c5e0f7 | -3.4961 | -50.84143 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 54722132-9f72-3bec-b4fe-319ee8bd54ba | -4.3534 | -46.75141 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| abd2b796-6061-3e93-a922-69e28b79a5be | -2.25236 | -47.47462 | 2024-11-14 00:41:00 | TERRA_M-M | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| e21081bd-809a-3fd9-a536-6c23e4d7322d | -3.47652 | -50.26955 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 6adb0431-ad79-3791-a3d1-4ff0875502c6 | -4.33984 | -45.98652 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 046e9116-bab4-3696-b440-666311f515f5 | -4.43575 | -45.94911 | 2024-11-14 00:41:00 | TERRA_M-M | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bba2cb1c-21fe-33b8-8fc5-525109cd2d86 | -1.96031 | -47.95671 | 2024-11-14 00:41:00 | TERRA_M-M | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ff44b1fb-40b2-3a1b-a1af-0be2c49451bf | -4.33798 | -45.44097 | 2024-11-14 00:41:00 | TERRA_M-M | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 28.2 |
| e7d99678-bd03-3390-ac3d-e45085233087 | -3.87941 | -52.2684 | 2024-11-14 00:41:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| df5a26cf-beed-3bf6-b1b1-52e1fb3a472e | -3.40009 | -50.30073 | 2024-11-14 00:41:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8bb70f6f-1763-3fb2-ba47-4351737ec380 | -1.59694 | -46.99744 | 2024-11-14 00:41:00 | TERRA_M-M | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fc4d3d92-79ce-3cee-837a-afb26dac7c69 | -4.28945 | -46.88828 | 2024-11-14 00:41:00 | TERRA_M-M | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a40a88bd-577c-3e97-906d-6f1af80d69f1 | -4.45461 | -43.97694 | 2024-11-14 00:41:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ae9dab98-5b4c-3949-8b48-8f6ad87a2310 | -3.03371 | -45.0788 | 2024-11-14 00:41:00 | TERRA_M-M | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 19.4 |
| c44c448a-23de-33af-ac5e-f01bf7854a05 | -3.02463 | -45.67354 | 2024-11-14 00:41:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 16143cdb-509d-34e1-8dbb-eee378c6978d | -5.12036 | -44.45068 | 2024-11-14 00:41:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a6f03411-2445-3710-aaf8-f0bbb5244107 | -3.88457 | -46.09055 | 2024-11-14 00:41:00 | TERRA_M-M | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 8ef3a8c0-86d4-380e-90a5-e210c3a96775 | -5.07595 | -45.51231 | 2024-11-14 00:41:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 0995cc9b-46f0-3de2-b4e0-9874b2f80dd9 | -5.85463 | -46.41859 | 2024-11-14 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0344586e-b603-37b8-be62-cc8f344426de | -2.97156 | -45.68105 | 2024-11-14 00:41:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| a0dde897-6a41-328b-a87e-27fc75455eeb | -1.8001 | -52.17259 | 2024-11-14 00:41:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 0425e668-efe3-3023-90d7-5d2146874ebd | -1.14085 | -47.36515 | 2024-11-14 00:41:00 | TERRA_M-M | NOVA TIMBOTEUA | PARÁ | Brasil | 1505007 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 18b92b14-a37f-3095-81f6-86799121e6ff | -2.8199 | -46.65485 | 2024-11-14 00:41:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 5f1de291-ffbb-3102-bbd8-bddfc29e079a | -3.05142 | -45.52896 | 2024-11-14 00:41:00 | TERRA_M-M | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 142.0 |
| 4b64244f-1fb6-3ccb-bda7-5da9a38ad83f | -5.35011 | -46.03123 | 2024-11-14 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 95689824-873e-3bda-9ca7-fc98a4405447 | -3.86901 | -43.943 | 2024-11-14 00:41:00 | TERRA_M-M | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |


[Clique aqui para ver as próximas entradas](README10.md)
