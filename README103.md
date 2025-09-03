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

## Dados Diários - Página 103

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 541775a9-0550-3b5d-93e2-08b049d09992 | -5.91293 | -57.72239 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 117f0378-6a91-3c96-84d5-5de72bbfb543 | -6.06156 | -57.97007 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2f20089-0924-3c6d-88b0-83e2bf0f7910 | -5.91295 | -57.74189 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 4f9a34a8-f3b3-3f8d-bd14-83fddbd379ff | -5.92125 | -57.71432 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f8cc7e0d-5313-3de4-8da1-a8411d07dbb2 | -6.7917 | -52.80845 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| da8aeaa5-3dcc-3d8c-ab96-468c5b48a94c | -7.69767 | -50.26947 | 2025-09-03 05:33:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f168f79c-e17c-3e90-8415-379b9edc3b0b | -6.8167 | -52.81602 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 137aea54-2e20-39b8-a5f8-6e7828771c57 | -6.82278 | -52.81666 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| aeaf81e9-9c09-30a3-a7a7-6c3d30a52002 | -5.91525 | -57.72575 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 2b223242-27b1-3085-a9e0-8539daccb656 | -5.92146 | -57.72384 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| cb63a6e9-7228-3dc4-bfeb-372e5a444086 | -6.33781 | -58.17616 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| acf62ba6-b526-3427-a758-84d52a297d1d | -6.83133 | -52.8451 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f350231-ec57-311c-98b1-cda86cbef002 | -6.25809 | -57.89513 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eabc74e7-a26b-3f3b-bcd0-062f4b82130c | -5.91895 | -57.73044 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 44fdc827-f826-3a3d-b2fd-026c08244443 | -3.52865 | -59.51519 | 2025-09-03 05:33:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7d127aa-c870-3d7a-8992-bf86b252534d | -5.86728 | -57.76514 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2e364241-127d-3d16-9dbc-18f056acc5b3 | -6.83675 | -52.85057 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08c8ae5d-27e6-39e9-943a-42d06584cb45 | -2.93795 | -54.80302 | 2025-09-03 05:33:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b31d6ece-878c-3243-84c5-5491259eaa61 | -5.90192 | -57.73754 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 15b073ae-8e58-3ddb-819d-ea9b40c77bc3 | -6.43645 | -58.12328 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86ff6104-25b6-359d-8282-257019262a6e | -5.91902 | -57.71096 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1231fcd0-b87c-3232-8d0c-07476701466b | -6.44316 | -58.1361 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 237dd240-a941-39cc-bc9b-36b9baf810c5 | -6.75631 | -56.39417 | 2025-09-03 05:33:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8590c09c-da2d-3fab-9972-0889a8badca7 | -5.8661 | -57.77314 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 8f4831c0-cf64-39b6-97af-2ed5a9e58028 | -5.92573 | -57.72453 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6eb5c322-3b0f-3f60-8953-ca302335c582 | -5.91966 | -57.73581 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0150c010-9834-3c08-a6b0-75340c883c41 | -2.28305 | -56.13312 | 2025-09-03 05:33:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d9897ec6-9c46-32b8-8f9c-8f3f339095fc | -5.91698 | -57.71362 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7216070a-eb24-358c-9bd7-6b1dd3677dd8 | -7.68969 | -50.27541 | 2025-09-03 05:33:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 97e84dde-b51e-369a-ade2-793c4ca2c361 | -5.91049 | -57.73863 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 29c9265b-4e92-31e0-a6a4-5d3a72caa719 | -5.90559 | -57.7422 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| cbcb007b-52e7-3ebb-8b0c-2361998f57ae | -5.8618 | -57.77275 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| b983b77d-721d-30cc-a5ec-4fcde97b111a | -5.86787 | -57.76111 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d8fc4a63-2a57-3b5c-8ec4-e3595ee4c50a | -6.84993 | -52.7978 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50a69e23-1425-3620-b9be-a828188bbbe3 | -5.86418 | -57.75657 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 4f70cb63-5438-3793-ac41-bfc8da922ff5 | -6.81528 | -52.81611 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2117e4fb-6a39-310f-9622-a51a61241cfa | -6.84868 | -52.79772 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7f7975e-0973-3ec1-983d-fe340a87a5e2 | -6.8026 | -52.81876 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8ac82d58-cc60-3edd-88cc-f61679ed8621 | -6.43063 | -55.60966 | 2025-09-03 05:33:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1ff5f162-7b40-394d-bb81-f7083d4ea28d | -6.83855 | -52.83698 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 318ece37-7ef0-3cf6-8af2-98f55b38d146 | -5.91755 | -57.70959 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fba824d2-467a-33bb-88e2-ee3f9b365684 | -7.70117 | -50.29944 | 2025-09-03 05:33:00 | NOAA-20 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 759ab98a-7b56-3d47-86d2-0181f70c707f | -6.83253 | -52.83601 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d967d20f-fa85-3c67-9461-b629402c986a | -6.77962 | -52.80664 | 2025-09-03 05:33:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8a3bb872-271d-3da9-b570-dfc9450ef725 | -5.91539 | -57.73515 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| c78d2164-480a-35fe-9dda-00a5387b0e36 | -2.94213 | -49.45827 | 2025-09-03 05:33:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e99da60-7e37-3a93-9c1b-b08d382070dd | -6.05219 | -58.00433 | 2025-09-03 05:33:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cec9996d-054c-3575-bbb2-09f778876a27 | -10.95451 | -50.77014 | 2025-09-03 05:36:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6ca656d3-b5c6-3089-a753-36ab06ee8bdd | -7.5344 | -61.33603 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| fbbe102a-f6e9-376c-a608-3d3ea14cf772 | -11.59969 | -52.11206 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 12928fc7-3f45-3cd3-b976-338d025ce0d2 | -7.54669 | -61.35003 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d22ce1cf-ac10-3329-a4c5-c95f3429cb03 | -11.59634 | -52.14169 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 02000947-9ec6-3f75-b634-f0d67873178c | -11.61049 | -52.07667 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 96467992-213d-3618-9145-f2edc679d178 | -11.59562 | -52.12003 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| e3775886-c327-36d8-b2fd-ab7e2ae386d9 | -12.17815 | -53.88955 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e68840ef-c41e-33fa-9a34-e747f1dd786c | -11.60036 | -52.10611 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5337e19-284b-31ac-b9cf-162719886322 | -12.61464 | -57.00864 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2860ad87-a6b6-399e-8970-8ad99b85798c | -11.5889 | -52.11938 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6d91fea8-99d8-3aad-adaf-872b0d5a4fb9 | -12.92608 | -56.96017 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 3680f6ef-a266-39ce-b104-ec3a0dd8aaa9 | -7.54872 | -61.33707 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ae1c1705-0295-35b2-bd25-2b856f652fa3 | -10.42981 | -54.77269 | 2025-09-03 05:36:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2bb00007-ff53-359b-822e-a7dda3fb5718 | -11.61185 | -52.06466 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a8719849-4bef-3a3a-8f8e-0c76d187e879 | -12.92326 | -56.94181 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0876050f-8b4d-3b52-b4f4-94caca2b72b1 | -7.55344 | -61.32963 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a1901a58-a20a-35ab-81fe-ffca0b1ff833 | -12.6047 | -57.00739 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1f40547-06db-313a-97dc-0349d6a54614 | -12.91613 | -56.99959 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 6ef8ea86-5f3b-3aa6-9d3d-c558de4b97d3 | -13.01825 | -56.87284 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 233f7e88-cc4e-379e-9c76-d3c4f991f692 | -7.54269 | -61.32912 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef36de76-6f5e-370d-8ad5-1ea307ad9243 | -11.60371 | -52.13657 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f88db549-d7c1-39c9-ab6d-10077dd3c891 | -12.89697 | -56.94895 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8126e25e-20aa-3f4e-a74a-bdc72b4f4806 | -12.93677 | -56.99663 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9c611546-5600-36fe-8f85-42a4052f4294 | -12.93108 | -57.00164 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 24c9036b-7604-3ba0-bb8e-3cb697cf3dc2 | -12.94392 | -56.98008 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 74b3eb82-5cb5-3ebe-8d9e-7acc98a63f7b | -12.94108 | -56.96217 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a10ea2ba-4738-3b90-85ff-95035e17c97f | -11.58679 | -52.1371 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 047dd520-8e7d-306d-bb67-0ea35dfa268e | -11.59835 | -52.12389 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 79e69ca9-67af-3d0a-a1ff-6097c87208ee | -10.49252 | -53.65307 | 2025-09-03 05:36:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e9621169-7098-3507-8816-49655b48365f | -11.63336 | -52.05539 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| abcc1b2d-7340-3470-8071-c3bc019ea5ca | -7.55036 | -61.32617 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ea81f01e-a0c4-371e-b805-a1cf20de1761 | -11.66054 | -57.3516 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 72d27742-e912-3937-b9b4-f381e251a33f | -12.97548 | -54.76403 | 2025-09-03 05:36:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 01df1613-7519-399d-8fd4-edd8c64a251a | -7.53501 | -61.33205 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 3c3aad1c-1862-3f1f-ad2f-315c9f99a95f | -11.42076 | -55.1858 | 2025-09-03 05:36:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0d10912-72d2-341f-bc1d-84996323367e | -7.55106 | -61.34554 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c4572090-24c0-3ca3-bd39-203e089688d2 | -11.65985 | -57.35675 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f343b19e-bac2-318a-9981-146034c761e4 | -12.90184 | -56.95056 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3307c51-037e-340b-bb2a-ee44bb4097e6 | -7.54637 | -61.32858 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f39535dc-857a-3c3d-8a0a-b37188868ad7 | -12.93821 | -56.98515 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 986b8482-29d2-3d01-8276-70da690f7947 | -11.58151 | -52.12439 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8310d5b5-b644-332e-953e-281bb5b0da48 | -11.67074 | -57.34979 | 2025-09-03 05:36:00 | NOAA-20 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4a8df739-e114-34c1-94b0-6d9361e84196 | -7.76481 | -61.20024 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b55ef4b2-33c4-3c1b-8af6-329c0c518734 | -12.62107 | -56.99763 | 2025-09-03 05:36:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08072cac-459a-3356-997d-21ff18621442 | -7.53854 | -61.33258 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 963fdf6a-8c66-306a-9839-efbf366f05ff | -7.67337 | -61.08815 | 2025-09-03 05:36:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a404c13-ba13-3f22-bed0-d74fadbe406a | -11.58896 | -52.147 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.7 |
| da2e28d0-fa71-3d09-8aaa-2fea40adae46 | -10.45071 | -54.78725 | 2025-09-03 05:36:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f70c61a0-1e6f-37fc-8f9b-a4199ee30e61 | -11.60068 | -52.07764 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 775df2ae-c4f3-3740-b4a5-39bd69f728e8 | -7.54519 | -61.33656 | 2025-09-03 05:36:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5ba4adb6-bebd-3e12-8425-a0db1113e1fb | -10.45118 | -54.78359 | 2025-09-03 05:36:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b35063a-60f6-3858-93b3-d3b4738cd609 | -11.5923 | -52.11729 | 2025-09-03 05:36:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README104.md)
