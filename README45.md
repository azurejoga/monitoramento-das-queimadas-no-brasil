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

## Dados Diários - Página 45

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8c83f146-d7a1-346d-8f5d-6ccfdff3ff3d | -6.89607 | -51.72811 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 195c8ec0-7204-356d-89d2-ebaa49780107 | -4.4969 | -43.67846 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 86ec16cb-32b0-3831-ab48-b11a4c46a775 | -3.02912 | -45.37498 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.7 |
| a49439c8-4e38-38fa-b653-ac5160c0a198 | -7.26881 | -45.01046 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3e7d05d9-149c-336c-b24b-775c9469eab6 | -3.14648 | -53.1434 | 2025-10-28 04:42:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ae387f0-2939-3cf9-a156-48f2ffb912d7 | -2.43605 | -49.75981 | 2025-10-28 04:42:00 | NPP-375D | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b43e9fb2-207b-3b5c-bf9e-9b6e0c09e792 | -3.14128 | -50.15859 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a0035e7-6f47-39fc-9c3f-541fced7de69 | -5.7301 | -45.26237 | 2025-10-28 04:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f3b02945-368f-33fa-8802-fd00bd016f27 | -7.96403 | -45.5175 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5567d254-271c-33cd-a1f0-1a465249b39c | -6.11501 | -42.45332 | 2025-10-28 04:42:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3b5c20bf-05e7-35d0-927a-807f0a6923c0 | -4.45378 | -43.64241 | 2025-10-28 04:42:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f703b267-71e5-346f-84bb-234615d0d8f5 | -7.45765 | -47.15589 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ee26d59a-80c4-3d56-820c-f41f57d5357c | -4.47517 | -50.51097 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72fa6ca7-1a04-3e01-8c3b-61cacd2f58b6 | -7.06932 | -47.36694 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 132e8e00-e107-3092-98d1-14ababf71c7a | -7.98976 | -46.7345 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 41c1498c-45c0-3600-ae95-6e28e9b8a5fb | -4.86504 | -47.35509 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49afc253-4dfb-34db-ba59-4f5fb76f8242 | -7.97277 | -46.74905 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| b234a361-a263-316a-9022-81bb07646204 | -5.67116 | -47.82473 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cfd9d7a0-8a5a-36c2-bbf9-716185dddf0d | -1.54964 | -55.42 | 2025-10-28 04:42:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f79aaa0-967b-3209-821e-0b525c914037 | -7.9735 | -45.5336 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e450709a-62d4-3ba3-9d4c-7d8ccdab0e51 | -7.61111 | -46.48098 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 98b4566b-2e0b-3e94-b8f9-98a17242d3f9 | -7.94367 | -45.49451 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 3a38da43-83d9-37a1-b02a-330a62382b16 | -5.20652 | -46.18671 | 2025-10-28 04:42:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee99fab-fc21-37a9-9d6f-b6218fd53344 | -7.29684 | -45.06629 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f7dbe31b-9466-3e9e-9045-da35891f464d | -7.94857 | -45.51498 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 802f042e-45c5-373a-8051-854ede27880a | -3.09988 | -54.61662 | 2025-10-28 04:42:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d15b393a-a9f5-3264-8ed4-4eb2a9e3da98 | -7.82606 | -46.46307 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 98bba317-0561-3772-913f-79a95b338884 | -8.05253 | -45.15287 | 2025-10-28 04:42:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d8adb78-ef68-3539-9462-019dd9d8b60d | -1.43522 | -52.86387 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6b24381c-775b-3bd8-b735-10eb8e9c84bb | -1.387 | -55.2378 | 2025-10-28 04:42:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d5f9970-6464-3f74-b0a6-19bb80bad783 | -8.13934 | -47.02879 | 2025-10-28 04:42:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95cb37cd-148e-34e4-9dcf-5e6e7d499ebd | -3.02179 | -45.37383 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.4 |
| eca609ba-cc83-3c29-ad28-52baa3a852eb | -6.16555 | -46.0976 | 2025-10-28 04:42:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8d18bdaf-5dd1-3e56-abf5-6c21f16f8e8d | -7.97278 | -45.53837 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f1f5bcd7-de52-33ff-bc6a-840780a46220 | -7.80696 | -46.49051 | 2025-10-28 04:42:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4b2157d-8f31-3f34-bba5-6fb956c4956f | -4.45588 | -43.23412 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b71c8e76-453c-3359-9c79-c7e0f9cdd11c | -7.25447 | -44.99794 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4f7410f-5589-3f22-ac58-3fa2adc72aac | -4.22486 | -48.37411 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3eb1e94f-dab2-396b-b207-009c71510354 | -8.1833 | -45.71405 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1533e6a2-b746-3fd7-a5ae-7cbae5d6502c | -6.46537 | -43.18821 | 2025-10-28 04:42:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eadd1bc2-6ac3-3cee-a1c6-252a22faa770 | -7.07282 | -47.3674 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b6daabb9-af3e-3058-8518-acb482eaa75a | -6.48333 | -44.44173 | 2025-10-28 04:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 42730d40-c6d2-3287-b830-d3d55e663fff | -5.71798 | -47.47915 | 2025-10-28 04:42:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2961a1d-fe80-3174-ade1-09ea1212e028 | -7.87215 | -46.39777 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 34942a8a-d2f4-379f-ba8e-d5a3692ba927 | -7.32452 | -47.20115 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eef95d78-d711-3c43-a32b-6a46ad2a5d9d | -3.91726 | -43.32037 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ee62faa9-7e89-3a29-bb52-077886ab2678 | -2.76616 | -48.57467 | 2025-10-28 04:42:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b364bc3f-b2ca-3d8b-89c0-486d1e64de79 | -5.79119 | -35.60023 | 2025-10-28 04:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| de78dca1-7a93-3d3f-8a52-8954b94a3a60 | -6.89119 | -46.36664 | 2025-10-28 04:42:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d4b04d8-9938-32b6-bb15-4d491a4a7eb3 | -7.64959 | -45.23962 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9366e67a-b5cf-3c75-a273-b64d289c68ec | -4.85563 | -46.74052 | 2025-10-28 04:42:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6085e868-af13-36b2-8ca0-2a929fb1b6c1 | -7.96853 | -46.75269 | 2025-10-28 04:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 9ed84f83-c4f3-3a6e-9276-91bd1100c789 | -7.84117 | -46.4128 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fdccbb8e-17c4-3db9-bf26-7d1293d48cd8 | -4.90573 | -48.56576 | 2025-10-28 04:42:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2a994ee1-c3f4-35a9-b551-20b89c745f41 | -3.58918 | -43.63608 | 2025-10-28 04:42:00 | NPP-375D | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 82cb7775-3d13-342d-ac6c-f92581949b2c | -3.14722 | -50.44926 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7fd38932-ec8c-39e1-ab67-665abab29a25 | -7.15749 | -46.99666 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8e926695-e037-37b0-bec3-4ef666ff558a | -7.35848 | -47.64647 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb7165d1-4a50-38ec-942a-2acf72a7caf2 | -7.45252 | -49.4045 | 2025-10-28 04:42:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 876d42c5-db8b-3ce2-a4f0-339734c58b35 | -3.57086 | -43.61835 | 2025-10-28 04:42:00 | NPP-375D | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a60b7b95-d991-360f-b7e6-c17f8b0c4caa | -6.45009 | -48.51193 | 2025-10-28 04:42:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 57fa6523-41ac-3865-a272-197bab4ab3b1 | -7.8622 | -46.39808 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 873fe41a-0e99-35a3-afe0-5d8b9d791945 | -4.47679 | -43.43207 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa254fb0-7d05-32ff-96b3-a012f6fc8534 | -4.43475 | -48.00812 | 2025-10-28 04:42:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3897de38-b2a1-39c1-9f50-990125030dc9 | -4.03108 | -50.44883 | 2025-10-28 04:42:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c35c1480-44cf-3ded-a2d0-a8fc54ec490d | -7.84183 | -46.40847 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6c20bc88-b987-3fc1-a9b5-47d2cc7c3bde | -5.16782 | -45.41459 | 2025-10-28 04:42:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fc4d5859-9005-34bc-8daf-7627c5eb9351 | -1.50168 | -53.12756 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98d58023-cf89-301e-b349-3c488470b385 | -1.50248 | -53.12244 | 2025-10-28 04:42:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 199126d4-57a1-3f99-810e-bc2068178ded | -3.94764 | -48.09102 | 2025-10-28 04:42:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 679362e3-573c-33d7-bb39-75e37da2060c | -7.91705 | -45.70159 | 2025-10-28 04:42:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd04e83d-2bf8-36a0-8048-657810a2f77b | -5.63359 | -47.61741 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ae28f74-4a47-3028-af36-947cf695e11a | -4.91074 | -47.41792 | 2025-10-28 04:42:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3cfb2fba-e49c-37ee-9521-f1f4c1230fa7 | -5.67512 | -47.82164 | 2025-10-28 04:42:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63b04e05-d98f-3e0b-ab99-e9c8542b2fde | -3.23503 | -50.05241 | 2025-10-28 04:42:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ff08158e-b608-3dec-aa7a-cb4df989c0bb | -6.98305 | -47.34273 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 609713fb-0ce0-3c21-9b1f-9319b41ce83f | -7.85115 | -46.39653 | 2025-10-28 04:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51f7be9c-0765-3bfd-9e97-de9afa87521c | -2.75348 | -47.75148 | 2025-10-28 04:42:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 867cb391-020f-38f3-a108-0622a49a43ea | -7.1563 | -47.00454 | 2025-10-28 04:42:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de43babe-3bc1-3614-a191-85d93741480f | -4.43251 | -43.44227 | 2025-10-28 04:42:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f357a2fe-922b-3d08-9d8a-00cbab1848a4 | -7.27351 | -45.00602 | 2025-10-28 04:42:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 376a2e54-0949-3b13-87a5-26a361ea8b14 | -3.08204 | -44.44382 | 2025-10-28 04:42:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0478f88c-e6ce-380d-a32f-76a7724328c4 | -7.94888 | -45.53964 | 2025-10-28 04:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 796b62fb-6c3e-3348-b8f4-7a355c74cff6 | -6.0362 | -46.55798 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5f64e421-f236-3852-b9f1-e8ff64433587 | -2.75657 | -45.40169 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 4ba662d3-474c-3269-9e84-1b783c7b9949 | -6.03559 | -46.562 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| abfec863-ca20-3243-a0d1-ae4ab853c96a | -6.48844 | -42.22693 | 2025-10-28 04:42:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 27124a03-4192-386f-a47d-ecd632b55726 | -3.91305 | -43.31973 | 2025-10-28 04:42:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe5c3a5b-0bbb-341e-a48a-618985f1c0d1 | -6.10966 | -41.74411 | 2025-10-28 04:42:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| b71993a0-8811-3515-82c6-e579b89f68b5 | -5.47175 | -47.26255 | 2025-10-28 04:42:00 | NPP-375D | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b973212b-210d-368a-8cf7-ba68e8b4bde1 | -7.30025 | -45.06424 | 2025-10-28 04:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b8f4851a-a20c-33b3-b154-b076a0e7302b | -4.96416 | -48.25956 | 2025-10-28 04:42:00 | NPP-375D | SÃO PEDRO DA ÁGUA BRANCA | MARANHÃO | Brasil | 2111532 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b7b4b11d-0c2d-3774-9fb2-c9b966bc5b35 | -2.75722 | -45.39747 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 17.9 |
| 2ec70390-c4e8-3f2a-84ef-8b7edc427f11 | -4.75307 | -46.42466 | 2025-10-28 04:42:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12da7d77-5066-3850-b568-7bb73a70e10a | -7.36665 | -47.8012 | 2025-10-28 04:42:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 765ec7b7-0f39-35f9-87a4-a9804f7dbcec | -2.45025 | -49.03056 | 2025-10-28 04:42:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ba91add-5de9-3c02-932e-a7dec21ded54 | -5.64726 | -47.64204 | 2025-10-28 04:42:00 | NPP-375D | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03ba48b9-e123-38b1-9a9e-e4b3fc7a69b9 | -2.74499 | -45.40418 | 2025-10-28 04:42:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 86aabd74-4672-3e37-babe-89bffaf0daba | -5.79557 | -49.82935 | 2025-10-28 04:42:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ffbed5-d25d-3019-865f-02376b387cc9 | -6.13218 | -42.689 | 2025-10-28 04:42:00 | NPP-375D | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |


[Clique aqui para ver as próximas entradas](README46.md)
