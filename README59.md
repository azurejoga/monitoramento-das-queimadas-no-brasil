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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ae6711e-e462-3a6e-aae7-bad93b81efef | -12.05323 | -46.37768 | 2025-10-27 05:01:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6b891f8a-5d82-38f4-9b9d-2bfdd7ee93bd | -10.35969 | -47.18284 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 34.4 |
| 3a764326-f7a8-3df1-99c2-5d9a9ea12efe | -7.4361 | -41.87823 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 1be0d073-4a5c-36ad-b371-f475a1e7f6ed | -10.8402 | -56.95769 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 99068efd-23dd-35a0-8311-799b697c4667 | -8.10151 | -47.05889 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d7b3ac51-8836-3dc7-9e5b-52973ad949e5 | -10.93792 | -47.60382 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80678b43-27c8-3194-ab06-30d5525b2491 | -10.68694 | -47.84143 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4c0839b7-f0db-3137-9679-e7404983047d | -10.58206 | -47.86689 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 99619111-1c79-321b-ab3b-88ba14725ddb | -10.58739 | -47.863 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 23bd61fe-85f9-3587-834f-b36c8287692f | -11.02366 | -47.82655 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6ad4809d-6f99-3340-a249-11434dab7cd8 | -7.23668 | -44.98232 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31c5a4e5-89fe-3536-9d3a-65e1e6eb9a7e | -10.8396 | -56.96141 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ddf263c4-7573-3fcb-b2f9-bb3ad8001280 | -11.01822 | -47.83079 | 2025-10-27 05:01:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1c421f7e-1e0c-3c77-81a0-e375a92c300b | -10.63288 | -52.18404 | 2025-10-27 05:01:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21e7fdb7-0ee0-3d53-bad8-a748ee0c0e1f | -6.37481 | -44.26446 | 2025-10-27 05:01:00 | NPP-375D | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98733ee0-10a5-3f40-a938-5a8a144ee49f | -10.36388 | -47.18893 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 23.9 |
| b01d50e5-6728-3d8c-a349-f8421af13619 | -12.28369 | -43.76237 | 2025-10-27 05:01:00 | NPP-375D | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47fb9a4f-271c-324d-8dbd-b0914c872111 | -7.81151 | -45.40119 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2a4e08b4-c681-3907-aa76-a899135c68f4 | -6.63613 | -44.63348 | 2025-10-27 05:01:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 101d56cb-d0ab-3720-83e4-0bba58d1f041 | -11.43357 | -46.12295 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2b21fd44-a81e-3c5c-beb0-780ba65e9988 | -7.42687 | -41.87702 | 2025-10-27 05:01:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c821c453-194e-39a3-8a6c-1754958c4ba6 | -9.23132 | -45.84251 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4aa1cb2d-90ad-318b-9729-7ef82d2e1f91 | -7.79224 | -45.38223 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bd5334fd-eaa9-3ce5-878e-60704590c4f3 | -8.11527 | -47.02396 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a90a4c7-f917-3385-9d81-dc2329c9338f | -5.60819 | -47.09861 | 2025-10-27 05:01:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 86a5ccc3-7c06-323d-b53b-8bf4f4bdf068 | -7.06624 | -47.36083 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ebdf6f0e-5699-36f8-95f8-cd2d98b5b09b | -7.78193 | -45.37754 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f9f05b98-1f72-3cf6-97c4-6000947ec2b1 | -10.87651 | -54.04689 | 2025-10-27 05:01:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f6ac2e90-9ad3-367e-92d4-f6880f1d710c | -10.83217 | -56.96397 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 933408c1-285a-3f2a-8e06-1c516f3ddadb | -12.04255 | -46.39038 | 2025-10-27 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d3450d3f-060c-3385-9d2e-1b770b9baff0 | -7.88461 | -47.24863 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 269f01af-a8d6-3e94-94ae-4fd6d28c65d3 | -7.80246 | -45.38752 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1752698a-9328-3040-a52e-b702bfd316ec | -7.2185 | -46.86762 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6ba15b5-3b70-37f5-ac59-ad8cdfe02b66 | -7.06489 | -46.75429 | 2025-10-27 05:01:00 | NPP-375D | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 0001f706-98c9-313f-90a3-cf433b45e605 | -10.90192 | -50.23705 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f9a169be-02e4-39c5-87f9-5977cf152d7f | -8.0261 | -46.76731 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 9812285a-5c92-3a78-8e3a-152c38a7cd63 | -7.396 | -45.12777 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f6b69baf-bbf6-3366-893a-80300da32b6a | -6.8866 | -45.15586 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea10aaa7-3dbf-342f-b16c-f38bb492ce39 | -7.84789 | -46.40485 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 776ffd9a-70f1-338e-9fb1-0f4a069c4ff7 | -7.97603 | -45.47568 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eb9d0163-fc2c-3312-ad9e-86f5bbd5a893 | -9.44386 | -56.64685 | 2025-10-27 05:01:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9fa10133-4636-3848-b956-4d92a1c24ab3 | -8.52872 | -47.20137 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c754a83-451e-36e7-8944-dac5978bf7a5 | -5.60357 | -47.09792 | 2025-10-27 05:01:00 | NPP-375D | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6378e7b8-cc92-3d8c-8d46-0385a03d1b6b | -11.83755 | -49.86056 | 2025-10-27 05:01:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e6f4e637-edd2-319c-b63f-9bcb34e9837d | -8.52801 | -47.20666 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6868a9df-96a4-3f8e-bf90-b261b4bf89e1 | -7.87604 | -47.24857 | 2025-10-27 05:01:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1c38732e-b006-3b12-aca6-987fb4887a51 | -8.52938 | -47.19878 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6c5fd552-8154-3ed3-9f20-8136ec85b5f8 | -9.72467 | -45.41943 | 2025-10-27 05:01:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c3575624-e5f9-3220-bec7-30abc9b33e87 | -10.04566 | -48.16276 | 2025-10-27 05:01:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100dd7bf-6f82-341d-bc39-adab7a01bf74 | -10.35551 | -47.17669 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 2be8bd42-9c30-36f4-8a15-e0256763a2e8 | -7.85452 | -46.50323 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d2c15278-d51f-3c53-bfae-7a5cdf811a1b | -11.33004 | -53.93044 | 2025-10-27 05:01:00 | NPP-375D | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe523eba-4fda-3c75-a9af-9efe935d8721 | -7.24438 | -46.96172 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| f4babb16-4e7e-3275-a3be-91316bf27c9b | -7.22327 | -46.86859 | 2025-10-27 05:01:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8b75a0a4-ec77-3e5b-9120-5c5a5a6cc459 | -6.89028 | -45.14756 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c32908d2-dfb0-3c01-9708-7cf0eaaa4f73 | -7.86057 | -46.42389 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d6a9b744-38eb-3786-a6c6-15b1a4d7816a | -10.20571 | -52.66482 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9ab0bc89-7114-349c-9e2b-1e68e96f5592 | -10.2176 | -52.65743 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4891c405-d1bf-356e-8b1c-2c6367cb67b8 | -10.63648 | -52.18459 | 2025-10-27 05:01:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9840dfa8-1fbd-310c-a04d-d226ff3d6b26 | -10.90645 | -50.23407 | 2025-10-27 05:01:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2f228490-6e5f-3e29-b597-c7390af423da | -7.82992 | -46.46075 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3ed96a2b-0033-38c4-83a8-4a34163947d9 | -11.09399 | -55.55909 | 2025-10-27 05:01:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ebf4a2d3-65f6-30ce-8454-f53ba877df18 | -9.58649 | -44.94947 | 2025-10-27 05:01:00 | NPP-375D | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cec93cd7-8af0-3918-9f36-09162a37f094 | -7.03477 | -43.93595 | 2025-10-27 05:01:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aaf41e56-5817-3239-b32d-7aacd7dfb4a2 | -10.83297 | -47.87626 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a72e5613-c52b-3977-8c22-ca4c7e056efa | -5.71531 | -49.30556 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| eb43e898-03c9-3b18-a248-3e20960a82fc | -11.79934 | -52.49378 | 2025-10-27 05:01:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccb1e1f5-715b-3414-82e3-ae5d2c64c3ad | -7.91828 | -45.66139 | 2025-10-27 05:01:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1676be82-66d7-39f1-818a-18807ece2e7f | -7.86561 | -46.4244 | 2025-10-27 05:01:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a71f9847-06af-3ab2-bdaa-d669dbc85014 | -11.41956 | -46.10415 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7ce896cc-8898-3384-9754-db272de64b6a | -7.24256 | -44.98088 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e80157c6-fe4c-3c57-baba-4fd01c7026e3 | -10.35106 | -47.17795 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db3f96c0-f06e-338a-a81d-e3c0b2f85ff2 | -3.69315 | -60.56549 | 2025-10-27 05:01:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dc377f03-2f06-328c-9d18-629261067491 | -9.25112 | -45.57339 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d958a4d7-f2e2-3b3b-a25e-c1fadd8355a9 | -10.21702 | -52.66138 | 2025-10-27 05:01:00 | NPP-375D | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cd740367-55ec-32e0-b4b0-3f9bfa34b369 | -12.04875 | -46.38428 | 2025-10-27 05:01:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4011415-e087-3160-a29a-d4df4eb57e9d | -5.71853 | -49.31129 | 2025-10-27 05:01:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76ba0e28-54ed-3b7b-9ecc-cf714495f6b8 | -8.11045 | -48.81628 | 2025-10-27 05:01:00 | NPP-375D | BERNARDO SAYÃO | TOCANTINS | Brasil | 1703206 | 17 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4a5c76a4-dd93-3550-9b92-88765ec6fe3f | -6.4409 | -42.34927 | 2025-10-27 05:01:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1e3b4b51-31b3-367d-a23b-a926e6e2df42 | -11.39286 | -55.16724 | 2025-10-27 05:01:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a633d3fa-5d25-31ae-b689-83d3fc4ace8c | -5.75586 | -53.3966 | 2025-10-27 05:01:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 46e95d23-9c5c-3bc2-b50a-269568ff1693 | -9.72923 | -45.42233 | 2025-10-27 05:01:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 096e30bc-846e-3c63-84bd-f0d7128710d1 | -8.0665 | -46.95698 | 2025-10-27 05:01:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 815a2fd8-60f6-3968-8cd7-a0b0db8a18a5 | -10.54947 | -48.0067 | 2025-10-27 05:01:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 95b5bd41-639b-384a-8a95-722fc3979712 | -10.39888 | -57.32331 | 2025-10-27 05:01:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62a6756a-eb81-31e9-bdf9-7a2dc1acc005 | -12.32159 | -47.48954 | 2025-10-27 05:01:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c3dc99fa-d313-319a-9d7f-ae7449fd397e | -6.88801 | -45.14594 | 2025-10-27 05:01:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 77fa3806-b05a-3fcc-af2d-d36a8d8db46c | -10.31164 | -47.20395 | 2025-10-27 05:01:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db8c5ce2-b3c6-36e6-b48d-9e082bf2c1a8 | -6.25235 | -41.84105 | 2025-10-27 05:01:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 41f1c462-77bb-3d3b-90be-1eee0f46c249 | -8.52309 | -47.20864 | 2025-10-27 05:01:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0cc0d982-5dec-32de-9e8a-dd97df212c42 | -7.84111 | -46.49007 | 2025-10-27 05:01:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0e46702-4a97-3597-a97f-f9b30564856b | -11.41012 | -51.46581 | 2025-10-27 05:01:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2c582ef0-8af9-3cfc-a197-6e61b4634e7b | -11.42001 | -46.10061 | 2025-10-27 05:01:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 04677cde-92bf-3c47-9839-6b6582e53c22 | -6.26198 | -41.81991 | 2025-10-27 05:01:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e5c5276c-b5d8-3f67-849b-9876e6c43da4 | -8.53196 | -45.56276 | 2025-10-27 05:01:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe9cfe67-70a8-3be0-8f12-b5fc22127fd1 | -7.76355 | -45.3918 | 2025-10-27 05:01:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 780ed5d1-b2c6-3896-bb0c-d8e6c58c3aac | -12.08272 | -46.40228 | 2025-10-27 05:01:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d55f0bf0-ee04-3814-8baa-8e495857a67e | -12.07002 | -47.99381 | 2025-10-27 05:01:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 33620d4d-8ee6-3d9e-b41b-1344137bb13b | -8.69691 | -50.80966 | 2025-10-27 05:01:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 5d7dfd5c-7377-3967-b293-40a2e6cf291d | -9.60087 | -50.78875 | 2025-10-27 05:01:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |


[Clique aqui para ver as próximas entradas](README60.md)
