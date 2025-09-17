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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a086dfe9-4eca-328f-bb07-34c890fcc440 | -12.7102 | -47.9872 | 2025-09-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 93.3 |
| 0ff0035d-2905-3538-a2a4-b390d8114cb5 | -11.6434 | -46.591 | 2025-09-17 13:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 86.0 |
| cc959758-08cd-3a7d-a2a9-4b45b1c65364 | -13.9653 | -44.921 | 2025-09-17 13:20:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 192.6 |
| 3417cae6-edc8-3846-8739-961dbe63eea7 | -11.1108 | -45.3452 | 2025-09-17 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 15841a75-1b4c-3814-add0-9a4d30aa3cae | -12.7106 | -47.9649 | 2025-09-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 110.5 |
| b38b0140-ee3b-34ab-8712-65b87b3a5856 | -8.0005 | -45.6864 | 2025-09-17 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 85.3 |
| 58777eff-24bd-3d75-88a5-470e8021b587 | -14.6143 | -46.3806 | 2025-09-17 13:20:00 | GOES-19 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 55a4eeef-cd56-3792-8e4a-0cb523c5fbb0 | -8.0597 | -45.4544 | 2025-09-17 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 9e5509a8-c4af-374a-858a-b805b2372b6a | -8.6313 | -46.4329 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 7f10d8e9-fcc5-3782-af70-283995bb4180 | -8.4467 | -47.692 | 2025-09-17 13:20:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 80.3 |
| da3e0bb6-333b-36e8-a5ec-48821ebe4b4c | -8.899 | -46.136 | 2025-09-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 13436d48-c46a-3616-ab36-9f026a1d6b23 | -7.5807 | -44.589 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 5b32c9d2-adab-3d2e-9591-bd562d30861f | -8.631 | -46.4553 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 100.7 |
| d1950013-d753-39b6-8f61-eed9e4b1f620 | -7.5996 | -44.5872 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 149.6 |
| c4c4a9b6-0d36-3e75-8ce3-1ce8c078e317 | -11.5966 | -48.2902 | 2025-09-17 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 57.3 |
| f95dd0d5-a962-3c47-9926-37a0485f84ff | -10.6334 | -44.2324 | 2025-09-17 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 83176a9c-9900-374b-a766-8ad20d6468d4 | -8.5609 | -47.5712 | 2025-09-17 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 3d1d83ee-7b1c-3f66-8fd0-4babef8f8c93 | -10.6925 | -46.4904 | 2025-09-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e1f667e8-5117-3429-86ff-43965c07d02c | -12.6821 | -45.3209 | 2025-09-17 13:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 5194644e-abda-3fa9-a7aa-cae768e14355 | -8.8958 | -47.8683 | 2025-09-17 13:20:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 54.6 |
| 01f47074-c513-3636-93e2-dcc390d8c162 | -7.45 | -46.1871 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 212.9 |
| b56a6815-cff5-337e-aa72-e5660a87512d | -7.6574 | -44.4667 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 153.2 |
| dd1e4eb8-c793-3116-8257-ffe5f49f7d77 | -7.6763 | -44.4649 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 039389e6-0e37-39a0-b82d-4893c2e460b3 | -12.7294 | -47.9845 | 2025-09-17 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 0aa57c39-9651-3f9c-83e9-6f8af49e67cd | -14.7719 | -60.2305 | 2025-09-17 13:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 9c492c03-6341-3101-bc58-f480290588ef | -11.5775 | -48.2926 | 2025-09-17 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 1f65ec9e-cb07-31ca-8bd2-a6b89b3fc977 | -12.0047 | -46.6989 | 2025-09-17 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 425.4 |
| f5176095-a4b0-3bf8-889f-3c07e9b79e9c | -8.8987 | -46.1585 | 2025-09-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 110.3 |
| 622f3ac2-8358-3a81-8391-5b6f14177efc | -6.8734 | -43.9636 | 2025-09-17 13:20:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 100.4 |
| 6d55acf5-4752-3879-b712-81f856c422ab | -8.5611 | -47.5492 | 2025-09-17 13:20:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| a4d02670-fa1b-3f86-8f0c-c1d90f5f79ed | -10.6734 | -46.4928 | 2025-09-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 71.1 |
| 1456baa6-b2e4-38bf-803a-c1991f27a16f | -8.4137 | -45.7583 | 2025-09-17 13:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 58d8ac3e-6795-32e8-af06-58aa5b4449f7 | -15.8417 | -59.4799 | 2025-09-17 13:20:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 2e78de92-4600-3507-a4e2-dfb47ee215e5 | -14.7911 | -60.2289 | 2025-09-17 13:20:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| a7d070f5-6c90-3f4b-84fd-65781653a3e9 | -8.6882 | -46.4047 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 88.9 |
| 1de41e63-2b42-387e-afb4-6dc304fafc0f | -10.6731 | -46.5154 | 2025-09-17 13:20:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 69.6 |
| f658b5c9-5717-3fe7-b5a3-0a11704b549a | -8.992 | -46.2385 | 2025-09-17 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 112.2 |
| 0bc5ede7-2e7a-37fd-8679-783b3fd00c54 | -8.9445 | -45.5438 | 2025-09-17 13:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 215.7 |
| f770a1a9-1364-3cfc-accf-c82456ce01bc | -12.0051 | -46.6763 | 2025-09-17 13:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 202.3 |
| 2ad16d31-54d8-36ba-b74a-645a17e5762b | -8.6887 | -46.3599 | 2025-09-17 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 93f0bb23-dc1b-3417-b3c3-42cda0ddc8bd | -7.581 | -44.566 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 116.0 |
| 41edb121-899a-3415-aa5d-8322b6e67005 | -19.7784 | -48.3011 | 2025-09-17 13:20:00 | GOES-19 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 89.7 |
| 35b9b9b2-9303-3a84-837d-2f335183e01d | -7.6951 | -44.463 | 2025-09-17 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.5 |
| 6b0f78b1-1733-3052-8a50-8120dd7f085e | -5.8807 | -45.8865 | 2025-09-17 13:30:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 7d5d1dc2-9c27-33af-87b9-31a69b78a13f | -9.4747 | -48.2698 | 2025-09-17 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| acd76871-0a29-3787-9476-8fa58ce516f7 | -8.631 | -46.4553 | 2025-09-17 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 124.5 |
| 2704be42-c9cd-315c-8bd6-9b4c29990b74 | -8.414 | -45.7356 | 2025-09-17 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 88.4 |
| fb3dd94f-01ca-305d-b687-d659d2e73959 | -7.4109 | -50.0019 | 2025-09-17 13:30:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 82.0 |
| 8efd721a-ef36-3cec-a242-ec5e64f15f80 | -7.6574 | -44.4667 | 2025-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 98.2 |
| 9cbb1a30-ae26-3286-aa94-bd6b7e0aa80a | -7.45 | -46.1871 | 2025-09-17 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 123.9 |
| 37e19366-fe44-336a-9a09-c6e81e897c13 | -7.8256 | -46.1754 | 2025-09-17 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 3b38df03-5bb7-35ef-a086-f85d8b3ea8ef | -15.0549 | -42.4653 | 2025-09-17 13:30:00 | GOES-19 | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Caatinga | 96.0 |
| 0a300e79-1d6f-306b-8acf-1ad0ddd448f6 | -8.0005 | -45.6864 | 2025-09-17 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 62.3 |
| b3f91966-e94d-3cf5-825a-27a32c461cf4 | -8.1569 | -46.7693 | 2025-09-17 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| d47b3230-9522-3f2d-b851-6a0ad555b18d | -11.5775 | -48.2926 | 2025-09-17 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 55ba7048-8632-3ca2-84e8-b46c5fc2e045 | -12.8601 | -47.1163 | 2025-09-17 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| c472e57d-4f6b-3825-8f0c-627f4b45baf1 | -8.4137 | -45.7583 | 2025-09-17 13:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 141.1 |
| 07e8569e-7e82-3e9d-8e6b-adcbfb2378da | -9.0478 | -44.8936 | 2025-09-17 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 4dfcadfa-e1bd-3d8c-9d3a-0a98cca2d455 | -9.1236 | -44.8849 | 2025-09-17 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 114.5 |
| 1d80bf1e-834c-3732-b900-a24145e1a290 | -5.786 | -43.9147 | 2025-09-17 13:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.9 |
| bbce5ed1-c16e-39aa-b370-5ae26c717708 | -8.953 | -46.3324 | 2025-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 89fb054f-95ea-3893-81c2-066cf1a176ed | -8.8958 | -47.8683 | 2025-09-17 13:30:00 | GOES-19 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| df23256f-bf93-31c8-93e2-1683bf897abd | -6.4804 | -45.7296 | 2025-09-17 13:30:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 73.5 |
| e6df01a2-c76a-3af3-8a82-251f8a827107 | -12.0051 | -46.6763 | 2025-09-17 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 177.5 |
| ae8d96b4-99b7-3e05-a32a-7c891ef22378 | -7.581 | -44.566 | 2025-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.9 |
| 7954e310-3e9a-3c36-b3c4-e028866dc5ef | -14.7732 | -45.3354 | 2025-09-17 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 102.4 |
| 1acfe9ec-d176-3d29-a94f-a6e2e694dccf | -9.0851 | -44.9352 | 2025-09-17 13:30:00 | GOES-19 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 144.9 |
| fc96f3c0-fada-31e9-9f3d-10583aac76e8 | -14.7716 | -60.2503 | 2025-09-17 13:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 61.3 |
| edce530f-6741-3c43-98bc-91897df07c0c | -3.8756 | -41.6188 | 2025-09-17 13:30:00 | GOES-19 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 138.0 |
| fd0b0a18-edd2-3e61-bd21-47c46d743f67 | -8.6313 | -46.4329 | 2025-09-17 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.1 |
| 0db6108b-3b8b-34b4-9913-7b55b8b72264 | -7.8259 | -46.153 | 2025-09-17 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 1a7d7bcd-c139-331b-93a6-01b2299fc3b6 | -9.4935 | -48.2679 | 2025-09-17 13:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 64.8 |
| e563da17-338d-33b9-abf0-948cabe5b3ee | -7.6763 | -44.4649 | 2025-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 87.7 |
| f47e6f2f-8d98-30e8-a58d-50d5aa35bcc5 | -10.6734 | -46.4928 | 2025-09-17 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.7 |
| 094516b3-8828-352e-b8a2-5f61f221cc66 | -8.992 | -46.2385 | 2025-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 83c408c3-9219-34ca-984d-7b80cf2750f6 | -7.5807 | -44.589 | 2025-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 185.4 |
| 43b58463-0e39-38f8-a2fc-101b5fda3c24 | -8.899 | -46.136 | 2025-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 141.0 |
| d9acc273-04fd-3099-a0a2-36ac82f99498 | -6.4102 | -43.3534 | 2025-09-17 13:30:00 | GOES-19 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 64.1 |
| 0319d1aa-96ed-30ec-bea4-6453b12f0f11 | -7.5996 | -44.5872 | 2025-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 108.2 |
| 3274da88-dd00-3d43-b65d-ffd29eccfcdd | -12.729 | -48.0068 | 2025-09-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 30975bc1-618f-3023-9995-9585dc285c21 | -8.9176 | -46.1565 | 2025-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 9573c7e3-c00e-3cfe-b3ab-abcb5e7ebf75 | -12.6821 | -45.3209 | 2025-09-17 13:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 7e0a441e-b433-3870-9d4f-13e249384f1e | -7.5227 | -44.7321 | 2025-09-17 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 103.7 |
| ba9060d0-f618-3c81-9629-052b3774b791 | -12.7106 | -47.9649 | 2025-09-17 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 4000d4af-a787-3ac5-8045-0c251bcc460f | -10.6925 | -46.4904 | 2025-09-17 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 73.0 |
| dddebb82-c58b-3031-8104-82d0202a69ad | -3.8042 | -44.1072 | 2025-09-17 13:30:00 | GOES-19 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 135.0 |
| 6c9a5ca3-69c6-3617-b086-114fa8483aa5 | -10.6731 | -46.5154 | 2025-09-17 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 6e0bfbcb-cfa4-38ac-a55a-66f681181857 | -8.9179 | -46.134 | 2025-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| ea271fe3-c95f-326d-bde8-a3ae317d48f9 | -13.9648 | -44.9445 | 2025-09-17 13:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 104.6 |
| c9a4ef44-f5bc-31da-966d-264d8a6ad1cf | -8.8987 | -46.1585 | 2025-09-17 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.2 |
| 7a9b9090-725e-30d3-b173-d53bebefa757 | -10.33 | -46.6025 | 2025-09-17 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 211d47b9-d6ba-3027-9b19-843950a11183 | -11.1108 | -45.3452 | 2025-09-17 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 89.0 |
| e96e809b-4c22-317d-bcc7-d2b592474603 | -8.0597 | -45.4544 | 2025-09-17 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 104.4 |
| 11e116b6-8978-3407-ba09-9d1cbcee351b | -14.7911 | -60.2289 | 2025-09-17 13:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 158.1 |
| ef994c6e-0e22-34aa-8a39-439d23ffe8da | -12.0047 | -46.6989 | 2025-09-17 13:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 475.6 |
| 9903dc1c-03f9-3bf2-bff8-ca48af637a21 | -14.7719 | -60.2305 | 2025-09-17 13:30:00 | GOES-19 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 107.2 |
| 0a0af9dc-47cb-3959-9b15-c19f3fc44efb | -6.8734 | -43.9636 | 2025-09-17 13:30:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 6814ecb8-ad00-3d16-bc4f-09d376e59588 | -8.1572 | -46.747 | 2025-09-17 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 51dbad1a-a27f-352b-b740-c4e695c36782 | -8.5609 | -47.5712 | 2025-09-17 13:30:00 | GOES-19 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 40e116ec-2e45-3ab8-8580-6a4e25fdee3b | -8.1757 | -46.7675 | 2025-09-17 13:30:00 | GOES-19 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |


[Clique aqui para ver as próximas entradas](README64.md)
