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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2be83255-d6ec-37ba-9922-6eec50110ce7 | -3.2131 | -46.80713 | 2025-10-23 04:55:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8ca194b-40c5-39bb-b285-e427e5b6ef99 | -7.17274 | -44.7902 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7d3f5ae0-d88c-3902-93d0-4f2b72d02597 | -1.97739 | -50.8154 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| dd23894c-3886-3c81-a75a-2d877a9a03ad | -4.37932 | -50.35437 | 2025-10-23 04:55:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a9f8908e-f712-3d1e-9f04-94cd2590b94f | -3.75183 | -52.15522 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d9190bc-6159-357e-93a9-343774b95f9a | -2.73776 | -48.42883 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 664ff76d-c0f7-3691-a33f-f22c655c2bcf | -3.70036 | -49.56481 | 2025-10-23 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c17a3d47-447a-3ce8-a731-e1c1c87d7387 | -2.79646 | -48.89098 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08ea3b51-642e-350e-9f2c-038aede44b72 | -3.39894 | -51.49823 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d72f4d96-a103-3da6-93b6-35d252cd44cf | -6.53351 | -44.36582 | 2025-10-23 04:55:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 480a1689-98d4-311f-bcbd-9c97f1ba6eeb | -2.90657 | -48.98375 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77987908-9945-3eda-9811-3592d413648c | -3.01774 | -49.44997 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| f4bc9ce8-32f6-3455-bf9b-1ac45353f6f9 | -3.93549 | -52.17279 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc5d1205-6027-31b4-9c76-1fc2a57e5e0a | -2.25548 | -51.92841 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e457c8d6-1f73-3e95-8e4f-05910a7e9c98 | -7.35753 | -45.04483 | 2025-10-23 04:55:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ef36ca2c-cd3e-3e98-bbdf-fbbf7c01795f | -3.14513 | -50.16405 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f9b3149c-84c3-368b-856b-c43108eb6eee | 0.38573 | -51.08069 | 2025-10-23 04:55:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a5a3f14-f6ce-36d6-81dc-0198be43de84 | -5.32326 | -48.18197 | 2025-10-23 04:55:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 16e77887-db11-339b-b7b5-ae19f18db9c2 | -3.15171 | -50.16932 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb456697-ef31-3f76-879b-07daea44f018 | -2.87539 | -54.86477 | 2025-10-23 04:55:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8370703e-0b1a-3580-b1e2-07450c32a913 | -3.80355 | -52.145 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6c7ba9da-c8e5-3d87-b15b-970eea77fcce | -3.24484 | -48.76263 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3df6c763-1e82-36c3-904d-36731d93977f | -2.80769 | -51.35624 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 87d84018-ffa1-3f68-91dc-0eada2095aca | -2.73254 | -48.28751 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afa3357b-9fca-337f-80ff-d400e9286b23 | -3.02797 | -49.48367 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| fc95ebe4-c336-39e1-872f-517f9f5466f4 | -1.89658 | -54.07387 | 2025-10-23 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb8bbdb1-6a6d-3dd9-8119-9abced1aff61 | -3.0256 | -49.47405 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| d95d2e9c-1f54-3d47-84d4-58008d04ce38 | -2.81013 | -49.1349 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ecde187e-9648-36e1-a5b6-73bf3133fc24 | -2.11074 | -47.10065 | 2025-10-23 04:55:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d6bde970-68f1-3ed9-b04f-558e752f15e4 | -3.69592 | -49.56874 | 2025-10-23 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b77588fe-6b57-30f4-adf2-9e9be6dcc219 | -2.80275 | -50.27433 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a32782a-db21-3656-9ba3-689816e4f4b3 | -3.98488 | -47.88355 | 2025-10-23 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0cf15914-7e4e-345d-8326-e5d2ad5b5ef0 | -2.69158 | -48.70634 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f87a5be7-0b52-3806-b86a-3a5d216c1fc4 | -2.85412 | -50.74067 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a701b064-586a-3d3e-9ba3-5270e46ab540 | -7.08281 | -46.19427 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 009b44e2-885b-3c92-9265-b53549633119 | -3.69661 | -49.56421 | 2025-10-23 04:55:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 550de9e3-ac46-3b1e-a162-47cf85b0560b | -3.93946 | -52.2135 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 59afcb9b-3a2a-383f-b08f-fbe0ec6e0399 | -6.73088 | -44.15191 | 2025-10-23 04:55:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9dfeb0ed-03ad-34bc-8655-384d7bed8dc6 | -3.84496 | -51.67076 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5e0cb90-39ec-3e9f-9c92-5986c4ff1660 | -6.64486 | -43.60855 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| cbdc59e8-63e2-3851-bfdd-8f9f30efb965 | -7.88822 | -43.54797 | 2025-10-23 04:55:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfb02dee-4647-3d83-b9b2-ee3da29321bf | -7.62912 | -44.57112 | 2025-10-23 04:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33ec984d-2d9f-38a2-afb7-49075c4edb39 | -6.78676 | -45.45997 | 2025-10-23 04:55:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| babee3bc-6e51-3005-ab4e-0a3f1bd476d4 | -6.39822 | -47.11626 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeef9c29-035f-30af-bea3-741c13bac423 | -3.80179 | -51.74655 | 2025-10-23 04:55:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12b5c25e-b7cf-3199-aa0a-11fd9360fbbe | -3.24796 | -50.12739 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a6b0ad52-69a5-3d00-ade9-5180c221cddc | -3.67748 | -47.62919 | 2025-10-23 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 044c9f31-ecf9-34c5-8b27-02b8cd804b0b | -3.02258 | -49.48455 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 3a53e333-5033-37fe-a9bd-a2ee575a5b95 | -3.96282 | -49.02793 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b8d7f01a-dbba-3bf7-9d37-1bc67ac41f0e | -2.74002 | -48.29219 | 2025-10-23 04:55:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f3149cf-d21c-3fae-8532-7b35a9a4fab3 | -2.87643 | -50.71227 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e8b5164a-b7bd-39b3-952d-c72d02b38c16 | -3.42256 | -50.36791 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fda4b849-2bd4-3f19-951e-7c91abcae646 | -3.59853 | -48.99342 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cd6cd09-b1c1-37f3-8667-9e6d504ced9b | -2.56703 | -49.5001 | 2025-10-23 04:55:00 | NOAA-20 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c22c9075-f4d5-3050-ac00-774a64016eae | -2.87523 | -50.72004 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9ad2b37-bd91-3568-9496-c6a6071c5f85 | -2.86943 | -50.71119 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96b15d0f-6dd7-3d06-ac98-f250d33737f0 | -3.89231 | -52.36206 | 2025-10-23 04:55:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ca619569-5d21-3b1e-aa29-92d39713561b | -2.25604 | -51.92487 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c72649-1901-3144-a92e-215a04a33b5d | -6.60056 | -44.21348 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ce87d8e1-d957-3ccb-9885-97d9bd008ebc | -2.83439 | -48.55953 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| be2fb7cb-36a2-36c1-8ebd-9acad39dc9ba | -6.27716 | -47.01572 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ec0a6d7f-6857-352e-a59d-a631c7000ae2 | -3.83232 | -51.29964 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afdf7ab4-ed7b-3a7f-b240-c7750f6cddb7 | -3.12513 | -51.29814 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e823237a-f120-305b-a1da-eb855a4126a9 | -3.68357 | -51.33612 | 2025-10-23 04:55:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47d2500e-e23a-3618-9503-3325ca01ea98 | -3.25032 | -50.13627 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d2fc1922-cc6a-3355-8c83-5d6d445bf51a | -3.02081 | -49.45503 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4d0fb72d-cd5d-3c48-89a4-c4c7f5b1aa42 | -3.86688 | -49.76931 | 2025-10-23 04:55:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 93c50570-ba05-35b7-9f4c-8fb1caa77206 | -3.04698 | -49.50942 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cb126cba-f399-3122-be20-76f1ba8e1236 | -2.14361 | -54.4414 | 2025-10-23 04:55:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab7a8571-72e0-3a43-83c9-a8cbd55ea59a | -3.67688 | -47.63316 | 2025-10-23 04:55:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 035a399f-7443-3da9-bbe9-33c8651683f8 | -3.02423 | -49.48309 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 70875d26-8150-377f-87fe-c4ebb2e6e80d | -2.55957 | -50.99514 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 96e5da37-7c05-3d22-975b-8c92ad7025f9 | -6.78848 | -45.44764 | 2025-10-23 04:55:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ae70194-804c-3d15-a697-e7467ea2a571 | -5.68993 | -45.96337 | 2025-10-23 04:55:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 60461ba3-697f-3589-883d-3f3d53874735 | -7.32464 | -45.28735 | 2025-10-23 04:55:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 92ed3790-6af8-36a8-ab8c-af3969c71f62 | -3.38656 | -52.96766 | 2025-10-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 76cbcd01-6ecb-3e12-8d87-b240fd60c51e | -6.59838 | -44.21678 | 2025-10-23 04:55:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a591d614-cf47-33a3-9b93-7abda9143ae2 | -6.96554 | -46.00625 | 2025-10-23 04:55:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3658352d-3c0d-3530-9e59-fd0b9e2a7d76 | -2.22542 | -48.37194 | 2025-10-23 04:55:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d274aa58-db70-3f42-add8-d2849c473c0d | -1.65088 | -55.13305 | 2025-10-23 04:55:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 713e6815-7308-388b-988c-5950652f697b | -6.30472 | -41.88823 | 2025-10-23 04:55:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 8690c242-74d0-3262-b656-df88ef92d3b4 | -7.63187 | -42.20557 | 2025-10-23 04:55:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8c09e55b-4811-3e98-8b7b-a87665e7a29f | -3.12076 | -49.10283 | 2025-10-23 04:55:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c73d668d-12b8-3c27-8518-038196e6ba31 | -3.39856 | -49.99756 | 2025-10-23 04:55:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb511fca-7099-3170-835b-379b7b551bc1 | -3.76602 | -48.92326 | 2025-10-23 04:55:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4127ec68-0752-3bdf-9625-613523995dfd | -6.28247 | -47.01162 | 2025-10-23 04:55:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ed4bf17-aae5-3514-b422-31e25d425b41 | -2.83466 | -48.56281 | 2025-10-23 04:55:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c59012f-ba69-395b-8d86-09c355ddec0e | -2.1644 | -51.94654 | 2025-10-23 04:55:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a6362b35-5232-3b01-98ab-ce9d23971ca1 | -5.47225 | -47.13937 | 2025-10-23 04:55:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3e011d9b-ccb4-3449-aaf2-0d377cef7698 | -7.0771 | -46.19922 | 2025-10-23 04:55:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3f25f366-7fd6-3251-8934-7dbff708a5c1 | -3.25158 | -50.12794 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ede21b98-1f02-3e17-98e3-889df27cae1c | -2.87173 | -50.71951 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c056787-17b8-366b-8a64-f475bf73147a | -5.32383 | -48.1781 | 2025-10-23 04:55:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 3b02ac3d-fb40-3360-b1e6-2bca4dc214c9 | -2.25156 | -51.90971 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d814428-8873-39cf-bbaa-a51f0b6800b6 | -2.97677 | -53.21639 | 2025-10-23 04:55:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 570d7484-afa6-3ce5-a8aa-32812757263c | -5.31964 | -48.17747 | 2025-10-23 04:55:00 | NOAA-20 | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7fde6177-42b5-3517-a919-f829c6bc51d4 | -1.59944 | -55.75573 | 2025-10-23 04:55:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2389b4f2-3c2b-3229-9bcd-12c0974dba77 | -2.85882 | -50.73343 | 2025-10-23 04:55:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7f4b003a-e8bd-37fd-9b4e-a33282a23cc3 | -3.11401 | -45.23563 | 2025-10-23 04:55:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d7c375ae-bf8a-3e23-b3b1-8b26cdc91f82 | -3.9489 | -46.96784 | 2025-10-23 04:55:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README31.md)
