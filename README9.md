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
| d6b5700c-0062-3b95-96a9-bf509f8627dc | -5.13195 | -45.11725 | 2025-09-17 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 81f00868-76ae-34b5-8c0b-a194811f5c3a | -6.879 | -43.96607 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 4d83b758-5710-3ddc-b1b5-cfd4b009592a | -6.40739 | -42.66027 | 2025-09-17 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| f06b54c5-f498-3ab3-9635-32ebe76a4582 | -6.96141 | -44.55325 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbbe4a2e-4ded-3f0a-9205-dec930d2328d | -6.1762 | -41.22556 | 2025-09-17 03:42:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d3abb3ed-67e9-3403-854b-f501f817e3aa | -7.06873 | -44.34227 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f5257e7e-757a-3f24-a52e-e73a127c21f1 | -5.74555 | -39.76138 | 2025-09-17 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e8eedd9c-2c95-3c40-a3d1-e4971183733b | -6.39929 | -43.33916 | 2025-09-17 03:42:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f3fdbed2-f2de-3cb4-93d0-2da0963ed30f | -6.03894 | -43.13696 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 274866bf-9bd4-3a6f-8e8c-d9c92b7a5cfe | -7.32553 | -43.96774 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4a721d83-a8aa-37b0-bb56-5b7b50798512 | -7.8361 | -43.85252 | 2025-09-17 03:42:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f409f78-4d5e-3597-b588-f35bc84761ac | -6.15925 | -44.53375 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2c862442-dbef-370c-b0fc-3dcddda417f3 | -6.16038 | -44.52736 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e660996b-3663-325a-941e-99dc196eccb5 | -3.50463 | -48.44771 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d00bd41-2fc0-3b06-b069-4d30c213aea5 | -6.19636 | -45.12759 | 2025-09-17 03:42:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7293497d-e773-364e-9946-fb11b20e02d7 | -6.22879 | -42.02525 | 2025-09-17 03:42:00 | NOAA-21 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ed0f1e4c-46e6-3d54-89f5-454d288806f5 | -7.57121 | -44.55851 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ff233e75-feb6-3c70-9e0c-1ecc6736cf63 | -3.23758 | -46.78882 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 27f4200c-d941-3380-a0ba-66139c7b4bfa | -2.37597 | -47.63874 | 2025-09-17 03:42:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a2147a62-c159-3cf3-b520-c18ad227be8d | -5.74164 | -39.76072 | 2025-09-17 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cc15062-6a7e-394b-9b8b-b8f99c1dacd1 | -6.96025 | -44.5599 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 85cb0fe1-fced-3a6e-9c43-6526f8306d66 | -7.57879 | -44.57663 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87ecf7dc-3276-34b1-8641-786aff0c1f6f | -7.33898 | -44.58668 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c9c838c1-3ed3-3877-b638-139e82793c8c | -6.22427 | -42.0245 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ed0a75b-cef2-3567-90c5-54b6c4f30b80 | -2.91613 | -48.31002 | 2025-09-17 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6f9a99f7-28f0-33fb-80f8-c5f00ab73d86 | -6.04042 | -43.14128 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8a1c1df4-b2eb-3f4a-b353-9edc736d24e4 | -6.10113 | -45.9416 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4913229a-b05f-398e-8a9e-5d191dabcac9 | -2.92324 | -48.31121 | 2025-09-17 03:42:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 529ca6f8-9854-34cf-925e-cc471ee12b54 | -6.88002 | -43.9601 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cad14002-045f-3e90-892d-e923a1dba7a9 | -6.87951 | -43.96309 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f2f5374c-91be-31b0-a9a2-55c38ff4d7b3 | -7.0941 | -44.53624 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9f3e9a66-8ca5-3c37-82b0-92fe0192ee58 | -5.62908 | -44.8332 | 2025-09-17 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9a403681-8e74-32e6-8ec3-1a2a2e5b401b | -5.74544 | -39.76432 | 2025-09-17 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| eee417d3-0dbb-3926-994f-4a152fa807c0 | -3.75689 | -38.70203 | 2025-09-17 03:42:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6eb226c5-701a-36cf-8886-c77a511fa5b8 | -6.87443 | -43.96214 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 3818fa18-e5df-3bd3-9bd1-eb432c307d89 | -6.87289 | -43.97114 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 38bc5492-8328-324f-b1f0-7fa73768e9ba | -5.3283 | -44.99414 | 2025-09-17 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 8ace22e3-ba21-3976-ab40-cae892114ed4 | -3.2364 | -46.79287 | 2025-09-17 03:42:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 75cd45c9-f377-3433-b51f-c8e3df712bbd | -6.36025 | -44.40957 | 2025-09-17 03:42:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bac667c-442e-313b-89ba-b6f5727fa816 | -5.81268 | -46.36429 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 629ad86c-e20d-3e9b-afd5-51718e235e56 | -5.4932 | -43.98717 | 2025-09-17 03:42:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 82d9d708-2bd6-316d-a814-ab660e0c2b1f | -5.39854 | -46.52863 | 2025-09-17 03:42:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7f986a8-1bbb-3f9f-ac32-3b68bae37491 | -7.07409 | -44.5574 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f28764de-67b8-31fd-8dc8-6f5ee5ba8013 | -5.63527 | -44.83032 | 2025-09-17 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| baf53eb0-3c43-316a-bb37-7690d7bf64a6 | -7.57412 | -44.57251 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac0801e5-7ee3-38c3-a86a-e7e351b6807b | -3.31045 | -42.16661 | 2025-09-17 03:42:00 | NOAA-21 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Caatinga | 9.9 |
| c6fe9a53-b1ff-34bd-84b5-16dd46b40dd7 | -7.57645 | -44.55946 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d320004-e40f-3b3b-b4ed-1ff7c0807bf4 | -5.76809 | -45.9217 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 055149be-1bc9-321e-b2c8-15c05700b9b7 | -6.98119 | -44.53355 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29ec7d48-fce0-3ce0-949f-13d136423036 | -7.13935 | -46.08711 | 2025-09-17 03:42:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 94fd35d4-5aba-3353-938a-de0dfbb427b2 | -6.39733 | -43.35057 | 2025-09-17 03:42:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bf3b63ae-da3c-3547-97c5-9db4570cc854 | -6.40649 | -42.66555 | 2025-09-17 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| e273b5f3-03c7-38b1-ae62-62c230e84bc6 | -6.95562 | -44.55515 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae118397-2e1c-3b56-96fd-034d56094887 | -7.31645 | -43.96027 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d3077f33-6bba-3a9a-a138-aa6644d80d32 | -5.80186 | -43.48701 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c5ba3e06-4042-3298-b373-8dc314b08f94 | -6.21479 | -43.90459 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a0d0df3c-3ff8-3118-aa12-51de9cd71d4b | -6.96732 | -44.55061 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| aedd2cc8-e66b-31ae-a8a1-2c9159793ed4 | -7.57821 | -44.57986 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 57e96690-0bde-3d24-9229-44e72196ba42 | -6.98505 | -44.60574 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 836433d3-76dc-3eeb-93b4-7f995c0b13b6 | -3.80124 | -47.5772 | 2025-09-17 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ef46a72e-9f75-3215-b4a4-2d56ea8098da | -5.81037 | -43.49761 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba20f8f6-db64-363b-bd96-540335e117fe | -4.59727 | -45.5835 | 2025-09-17 03:42:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 949a919b-0512-328e-84d4-70c1a7229e72 | -5.32762 | -44.99803 | 2025-09-17 03:42:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 41dc650f-5fe0-31c0-b4c9-f0dfc8d41c09 | -4.05547 | -47.5021 | 2025-09-17 03:42:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 24.0 |
| 1719c459-766f-336f-8e80-644c602cb9d3 | -6.76383 | -37.89041 | 2025-09-17 03:42:00 | NOAA-21 | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 2fa79441-9a36-3c28-9a69-c79a14c54ba5 | -7.26778 | -46.58439 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 93d87ecf-7df2-380e-9eb8-75568394c09c | -6.97806 | -44.45807 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 35f490aa-69c8-369f-aeba-f05a052bf3c7 | -6.87561 | -43.97298 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 15735807-f33e-3fbd-b8b5-89998b440ff7 | -6.68542 | -46.30537 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 29507a78-1986-3269-b298-a1d7250c5183 | -7.5718 | -44.55524 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dc5188f4-d13d-353b-9d4e-61a0dd3a5e69 | -3.59994 | -38.94783 | 2025-09-17 03:42:00 | NOAA-21 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 46.8 |
| d8fc8319-3990-337b-b839-73972e861ceb | -5.80113 | -45.70742 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 510bc6c0-74ad-3a68-a1f0-85969f5d3a2d | -6.87253 | -45.1867 | 2025-09-17 03:42:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2fbdc2a7-bfce-3cf5-8be3-f4d58c461e25 | -5.76887 | -45.91745 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7a60b465-c95f-38a6-b534-9f1a3eac8309 | -7.57706 | -44.58633 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 19.8 |
| 0807c093-8fc7-34e0-9de4-62a4986c86e7 | -6.97495 | -44.44486 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f73a6c0c-6aa2-32d7-8954-edfa18d78f52 | -5.49264 | -43.99039 | 2025-09-17 03:42:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46e6fd60-30c6-38d5-a18a-524e6362e309 | -5.81405 | -46.36283 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 283b8cc8-ec99-3d1d-8035-995952d3cc33 | -6.21426 | -43.90766 | 2025-09-17 03:42:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6caa257b-ed45-3e40-bdf6-58822dbfa1d8 | -6.40993 | -41.79134 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3eb2cd20-e1d9-3e86-a176-c75dd98e8f45 | -6.5233 | -41.81691 | 2025-09-17 03:42:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| edf3609d-ee8a-3bca-a0d5-7c28e309c3c6 | -6.86544 | -43.97108 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a943e088-bd6b-3612-b2ea-0e780199e501 | -5.62978 | -44.82936 | 2025-09-17 03:42:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ca24e4d2-d575-38c8-8da0-41c28a436eb4 | -7.06644 | -44.35522 | 2025-09-17 03:42:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 6645e8c8-aab2-34f3-bc55-96e23fb4d415 | -6.67268 | -46.30777 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2075f807-305d-3dd4-ba76-c5f975e132ac | -3.76066 | -38.70264 | 2025-09-17 03:42:00 | NOAA-21 | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 6bb44e32-e18a-38cf-ba4d-9400fede9f4e | -5.74153 | -39.76368 | 2025-09-17 03:42:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 019a7fc6-843a-36a1-98c3-1162cf50ffed | -6.67617 | -46.30561 | 2025-09-17 03:42:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| efaed941-05b6-31de-8553-8d30884bee68 | -5.50194 | -39.70045 | 2025-09-17 03:42:00 | NOAA-21 | PEDRA BRANCA | CEARÁ | Brasil | 2310506 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d07678db-c024-3085-89af-9702713e53b8 | -6.4478 | -42.63427 | 2025-09-17 03:42:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 54772d91-e5e0-358f-b2bc-38831a03526b | -7.30969 | -43.96886 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04c43169-8957-3754-ad21-1d199109f521 | -7.58111 | -44.56363 | 2025-09-17 03:42:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2072e097-58ea-36c8-b1c5-b1a7d4c8d888 | -6.88284 | -43.96193 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5ebc0bbd-f6e5-3f2b-9489-dd28427cd175 | -7.26693 | -46.58895 | 2025-09-17 03:42:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| c40e90c5-1138-3d3d-9b5f-ec522d1c0d9c | -6.8858 | -43.97474 | 2025-09-17 03:42:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 253310d7-72f4-3576-838e-db8336aaf933 | -6.96673 | -44.554 | 2025-09-17 03:42:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b6bf73a3-4062-3fa9-bc6e-b813e088ef3c | -6.04138 | -43.13553 | 2025-09-17 03:42:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.9 |
| b760c933-cadf-3241-a02b-eec855350b89 | -7.32425 | -44.06287 | 2025-09-17 03:42:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 98d82cc2-1d6c-3e3d-8cc2-f2672dfcb970 | -5.56761 | -43.44009 | 2025-09-17 03:42:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 353d55e2-3eb2-3712-ac3e-c356369a34de | -5.81877 | -46.3652 | 2025-09-17 03:42:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README10.md)
