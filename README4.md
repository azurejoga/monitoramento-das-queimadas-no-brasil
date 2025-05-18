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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8755bfc9-b90d-37dd-80a5-efd87239db50 | -6.44858 | -46.19339 | 2025-05-18 04:17:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bbcb1619-f405-38f6-b5bb-56bf9727c718 | -8.00859 | -46.80579 | 2025-05-18 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce36031e-2a19-3d1d-8dbf-ecf4d6a211ec | -7.94864 | -49.75983 | 2025-05-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 30a937c0-7a30-37fc-b195-e70070fb519d | -6.64893 | -41.98993 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| b56de337-dfe8-3b99-a5e6-3b7e5bcb41d9 | -7.07656 | -44.91877 | 2025-05-18 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e3d30d0e-600e-35e3-87f3-84bdc717de9e | -6.64773 | -41.99791 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| ac0181c3-218b-317b-8bdc-b060859a190b | -6.65186 | -41.99445 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 16ba49bc-0f8e-348f-b900-a877d4f00c63 | -7.9495 | -49.75474 | 2025-05-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48d065fb-9a37-3c8c-8da9-68c23eb10d73 | -6.66118 | -43.38154 | 2025-05-18 04:17:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ea6cea2-3ff6-3af9-9a07-daa3cef959ed | -7.30832 | -47.95103 | 2025-05-18 04:17:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 361f7228-2294-3734-9c6c-49b5dea4f673 | -6.64833 | -41.99392 | 2025-05-18 04:17:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5e996273-e4df-3622-8e13-d3a3d4f85461 | -7.95345 | -49.75541 | 2025-05-18 04:17:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca633e60-c160-3cc7-ae68-57ff039647ee | -7.07987 | -44.91929 | 2025-05-18 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b309ea92-e116-31e8-9575-fc5a05e9248e | -10.68375 | -57.60863 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10906c7a-2488-394b-a61f-661a1ce87ae3 | -11.38323 | -46.99316 | 2025-05-18 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d76db209-fdaa-3a20-93d2-f164b72cb07c | -13.29563 | -45.37357 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e58b3b37-ff9b-3704-bcb9-7aee17ca8aad | -13.14579 | -56.80656 | 2025-05-18 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| eb91e7c9-69bd-3f97-8db1-eb74fd2963d1 | -12.12189 | -54.65829 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d8d9d8d-aac0-3e91-aeae-d44884c70aeb | -10.7573 | -57.22902 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 23229c76-1e24-3d07-a506-7fbef50a052d | -11.4191 | -54.31747 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 40f1e9d7-9747-3060-8fa9-063849db8ad0 | -13.70594 | -47.71075 | 2025-05-18 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9cd2362d-eb59-392f-9d0b-425da954014c | -12.10174 | -44.75454 | 2025-05-18 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 864348d2-c6b3-30a5-a498-6345dcc307b9 | -11.6459 | -54.39597 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| efee8d52-f1e7-3cf2-a69a-450976da0763 | -11.65095 | -54.39691 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| febc008b-cc11-3492-8076-6c9cfeba2abf | -13.65876 | -47.89242 | 2025-05-18 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 49ad1f07-ff7d-3ac9-bb13-850b00e95585 | -11.79387 | -49.31685 | 2025-05-18 04:19:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 67f43801-7b65-3fdd-b4c4-822cf6c849f0 | -11.42695 | -54.29737 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5300ecb1-1ec7-3b50-94dc-86ce6af20dd3 | -10.34708 | -47.52309 | 2025-05-18 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0b0e26da-aae2-3d1c-b781-fd96939c2b27 | -11.58487 | -47.61363 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50668110-e5eb-39be-bddb-0afbb1c119ed | -11.57745 | -47.6162 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a806a68b-e4a3-3b4e-a606-0155655a8692 | -11.58025 | -47.62053 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0fe3fe50-2656-3b64-a007-58ee303119f6 | -9.194 | -49.819 | 2025-05-18 04:19:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7d69437-4fa7-3d9e-a226-5e0ba039efba | -8.43116 | -49.10447 | 2025-05-18 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| afe7f73d-964e-371e-a8ff-1a2aa1fb581c | -13.89317 | -43.44901 | 2025-05-18 04:19:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17074a47-1551-31c2-9e23-fd77ab13142f | -11.57527 | -47.60812 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8703446a-9f82-33f7-98ce-061bba8782ba | -11.56018 | -47.8728 | 2025-05-18 04:19:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| bed973c5-8834-3f08-b3f9-16aa83591f56 | -9.54343 | -47.67099 | 2025-05-18 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2983d7de-8575-325a-b00e-d7e0fca4f3bc | -13.30119 | -45.38182 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3a5468f3-8d2c-369d-a8f0-4854abf45f75 | -12.10119 | -44.75816 | 2025-05-18 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2bee54dd-e921-34b6-8227-2bcc2ffef55b | -13.67574 | -45.26418 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1212332f-f737-3592-b654-aa3ef2bf3f7c | -13.94715 | -54.4899 | 2025-05-18 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 486a3a2f-5feb-34c8-b447-ff4eb439b849 | -11.14359 | -47.6954 | 2025-05-18 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1cce3f62-936f-37aa-b241-d882b31833a6 | -13.14417 | -56.81459 | 2025-05-18 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| b63e4c20-5f82-33ba-b8ad-a52f88ebc0a9 | -8.43572 | -49.10048 | 2025-05-18 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 120a40cd-2371-3d0f-b4a6-f8a91e53aec3 | -11.79312 | -49.3212 | 2025-05-18 04:19:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2bac627b-058f-3ea0-9c19-ac7a6a1d9284 | -12.29883 | -52.4753 | 2025-05-18 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cd516fa-45cf-3db3-85b8-a8fb10854db1 | -10.47246 | -49.15009 | 2025-05-18 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ddca356e-5ff7-3680-93be-d27af1e28d08 | -11.42294 | -54.29651 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f7f4713-a4aa-3fb4-86e8-036790efcd3d | -11.48245 | -43.80621 | 2025-05-18 04:19:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50023bce-5051-34f6-9bdc-45ae8a48fdd5 | -14.01816 | -55.13954 | 2025-05-18 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ebe416d0-8d3b-3e96-b377-d7bf678499a6 | -13.89182 | -43.45205 | 2025-05-18 04:19:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 757958fb-fd20-3e07-82fe-18628769fdd2 | -11.62886 | -48.47177 | 2025-05-18 04:19:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1652a8b6-2cdb-3a80-93f6-823103eaf0b8 | -13.04556 | -53.7214 | 2025-05-18 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b5d8481a-167d-39a8-98fb-577e85f70f7c | -13.29508 | -45.37714 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 643c0bc6-31d2-31e0-a237-71dfa25c8582 | -11.29104 | -53.97907 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e8201dba-3f44-3d87-b995-a5be683e1de0 | -11.41848 | -54.3144 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4889c068-7194-35a8-b3fe-42283829a728 | -13.67184 | -45.26726 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| beb3c6fc-3509-396a-819d-b5d52e0dd1aa | -12.59349 | -45.44072 | 2025-05-18 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ae0c880-c67c-3e8a-9c41-be93805edd7a | -11.56043 | -47.61334 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 872caa1e-ae1e-3a83-acf8-406e5d6ac1ca | -12.10509 | -44.75508 | 2025-05-18 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 63984e7b-2360-3630-9b08-3a5d386b9e47 | -10.67998 | -57.6094 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b5d5dd8e-9099-317d-be89-6956c48ffb91 | -14.01309 | -55.1385 | 2025-05-18 04:19:00 | NOAA-20 | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1e45fa6d-8297-3313-96d8-f9a50ae614b7 | -10.75519 | -57.23539 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2b37387e-af5d-3d7e-95b2-aefcd7279106 | -15.56898 | -47.85644 | 2025-05-18 04:19:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| eb60a71f-b191-3e5d-a420-2de8d7333b3f | -12.12582 | -54.6653 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d5bf2ac-6980-33c0-b231-1380dda62dbc | -12.09894 | -44.75039 | 2025-05-18 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2ee01e5d-46a4-3b10-947e-db10d3aaf70b | -13.30232 | -45.39668 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23017cfd-c51d-3275-8a25-b7acfe965e2a | -10.68097 | -57.6045 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c8723fb4-db4d-3978-9c87-fc5725ac2428 | -16.0296 | -43.67908 | 2025-05-18 04:19:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 18cf4d16-84c4-357b-9835-aa1e763801ef | -13.58194 | -47.36866 | 2025-05-18 04:19:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e049a0f-b05f-305f-b099-f0d16cb918aa | -15.29388 | -53.20754 | 2025-05-18 04:19:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ae9a46e-ef09-325f-9d3e-497f4b4ac704 | -11.41791 | -54.31736 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1a6a2c45-16e5-35ff-b60a-4c3eb15ee6bc | -9.29323 | -46.71575 | 2025-05-18 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 02e818bb-0b2b-3a6e-a0f0-daafa5e93dfc | -12.29961 | -52.47094 | 2025-05-18 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a3ef582-0aed-3817-87a8-79d523bae5cc | -14.8748 | -45.36355 | 2025-05-18 04:19:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12ac0bcc-aab6-3660-89af-2cb11fbb08fe | -11.4235 | -54.29348 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 188a4f41-6313-37a9-ae86-40a7edc2f553 | -12.29444 | -52.47447 | 2025-05-18 04:19:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fb306b5-199c-3356-87d9-56c1f6566f57 | -11.41735 | -54.32031 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de1b758e-085d-35ff-8cea-bbeae30592d3 | -15.26424 | -51.48067 | 2025-05-18 04:19:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 52c94f4b-cee5-3aca-8faf-1acae2c8e3b8 | -11.42239 | -54.29954 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebefb117-d9b5-3cb4-a85b-b323546f7460 | -11.64646 | -54.39301 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 41edd78c-b963-3ece-b3b5-2aa76dea2c6b | -12.36784 | -56.39991 | 2025-05-18 04:19:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52cc8020-e28d-3c87-b260-9344aae701f6 | -12.12699 | -54.65923 | 2025-05-18 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7228c4a0-4db4-37cc-9d0e-d932b69d9a0c | -11.41404 | -54.31659 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9673947f-b002-33b5-afd5-010bf8ab71b4 | -11.57867 | -47.60872 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 20f3fa6b-ad10-3dac-85d1-695d252a70ea | -12.03373 | -54.97284 | 2025-05-18 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ca3013b6-6bd5-3731-bd28-64d18e1956a3 | -12.60612 | -54.06885 | 2025-05-18 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6d3c5b4-4474-3215-8f8e-107532b3a1a2 | -12.36138 | -56.40274 | 2025-05-18 04:19:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70a89f3c-e4d8-3849-b870-194bddfd3e1b | -13.03829 | -53.71575 | 2025-05-18 04:19:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6efdbdf8-a87f-3195-b173-370ca5d5873b | -9.3176 | -44.83292 | 2025-05-18 04:19:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 48876cb4-3084-3d0c-83b9-f800e97ee9d0 | -11.55702 | -47.61276 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3fd8ad57-9fe9-3ff8-8b09-c3345c3f8b0a | -13.1401 | -56.80521 | 2025-05-18 04:19:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 659e5903-83c6-3345-9262-68f00797d8e2 | -11.64702 | -54.39007 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 42991374-7471-3486-969a-8ba627a129c2 | -13.30843 | -45.40134 | 2025-05-18 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 198b7516-f826-3e0f-b4a0-be9b2b8b9898 | -12.29885 | -49.37096 | 2025-05-18 04:19:00 | NOAA-20 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d73d3168-53e3-320c-85f0-967675b04183 | -11.41964 | -54.31451 | 2025-05-18 04:19:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 77f1b3c0-62c6-3747-bb9e-ae43224be8dc | -10.3477 | -47.51933 | 2025-05-18 04:19:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9fc59164-fe7b-3387-b05f-049b7d126024 | -10.75637 | -57.23382 | 2025-05-18 04:19:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 265ce646-7728-382e-b8a9-626f6a03991f | -8.43494 | -49.10507 | 2025-05-18 04:19:00 | NOAA-20 | COUTO MAGALHÃES | TOCANTINS | Brasil | 1706001 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c5cfc0e-b5aa-387f-9dfd-342f7ef5172a | -11.58086 | -47.61679 | 2025-05-18 04:19:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README5.md)
