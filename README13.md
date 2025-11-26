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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9111e0a9-26b3-3951-a107-b2e725799245 | -22.89724 | -43.65792 | 2025-11-26 04:04:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| cb6568bb-5291-3219-a4c9-cec317523c89 | -23.60023 | -48.34613 | 2025-11-26 04:04:00 | NPP-375D | ITAPETININGA | SÃO PAULO | Brasil | 3522307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0b57fef6-0041-3aab-bc9e-4ac288581da9 | -23.25021 | -47.23475 | 2025-11-26 04:04:00 | NPP-375D | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 1a7f1256-8615-3606-b010-830aa2c7086d | -1.50929 | -46.76502 | 2025-11-26 04:18:00 | NOAA-20 | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 107dffe2-3f8a-3efe-888a-8670766b79f3 | -1.75995 | -47.09686 | 2025-11-26 04:18:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eb68bdd2-e24d-3b28-ad63-e0707e2ddacb | -1.8602 | -44.59532 | 2025-11-26 04:18:00 | NOAA-20 | PORTO RICO DO MARANHÃO | MARANHÃO | Brasil | 2109056 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa14f0bd-2744-3081-96d3-fe701a8eb64e | -1.7563 | -47.09629 | 2025-11-26 04:18:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 760b79ba-020a-3dd3-81b4-139ceb3a380e | -7.4967 | -42.88288 | 2025-11-26 04:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fde48a13-3059-34b9-82e2-5566498cb93f | -4.28703 | -47.31084 | 2025-11-26 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f01f76cb-dc6a-3986-beee-ae52962690c4 | -6.30124 | -43.79535 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05b965d8-bda7-3259-b3bb-65c68550cd00 | -6.32879 | -43.98952 | 2025-11-26 04:21:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 155b063f-f510-3b02-96c9-f0efff46d449 | -4.01196 | -46.49984 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 0e9684c5-c4da-3f63-84aa-3fca2e651582 | -2.5008 | -47.81953 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c82edf19-2ebb-3613-8389-a08d9ce3102f | -6.68588 | -43.94124 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0b143754-e50d-3aec-ad2f-088ac0646864 | -4.72341 | -46.46297 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5b60433e-5d67-3962-bcef-66ac0f04b7b0 | -6.03486 | -45.82658 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48f3eb19-385b-311b-8445-c195a4d0b51f | -4.16666 | -43.71852 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 437c143f-f5a9-3868-9a6f-23b2da18c9d4 | -6.06298 | -43.25309 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0bced90a-8918-3259-b691-61a325350adb | -2.3472 | -48.49308 | 2025-11-26 04:21:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d1023a1-c7ad-36d7-9adf-e4a3a7b78094 | -5.22848 | -45.42705 | 2025-11-26 04:21:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 36adc686-44ce-31b7-8411-c44e05827969 | -6.60592 | -35.23172 | 2025-11-26 04:21:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 77be5316-d465-3ff2-9c6b-a61e63d4c067 | -4.82697 | -43.81862 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 60c2229a-9216-3637-b6e9-c9d565e5a5f2 | -3.26914 | -50.59542 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a5e6770b-41e9-3815-95bd-b9fa935e6004 | -4.71714 | -46.45807 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9527be9c-6577-326c-b65d-81e8c99ce294 | -3.74412 | -44.5443 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00d1481f-9c89-3b2e-8f4d-3c6dfe16a0be | -6.1123 | -42.95612 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 8131788b-722d-307a-99c6-3345de7ad8ac | -8.04441 | -43.12207 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| db1c11c9-2145-3b12-b670-cead522c81b7 | -4.95698 | -44.71889 | 2025-11-26 04:21:00 | NOAA-20 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3bdb41c-af34-3cce-911c-32c2b089df71 | -2.47777 | -48.22931 | 2025-11-26 04:21:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bdeea1d4-4cac-31a1-8520-1f52e6637306 | -7.61035 | -42.98355 | 2025-11-26 04:21:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0bbc33a2-6216-3f61-858b-3e574ba5ede4 | -4.25946 | -45.13056 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70eb2d4f-5775-3282-b749-bd41dd138a69 | -8.07843 | -41.08462 | 2025-11-26 04:21:00 | NOAA-20 | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4da0d586-dbe4-326d-b42e-d978cd74cc39 | -6.76987 | -46.51843 | 2025-11-26 04:21:00 | NOAA-20 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cf847454-a573-388d-92a5-29ee9b3bee4d | -8.04499 | -43.11832 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 16.6 |
| 294c15b3-b47f-39d8-9420-703deab06b16 | -2.63668 | -49.26558 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e58e4e13-3bbb-3c1a-ba6e-2deff23ce696 | -8.0507 | -43.12687 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 27.8 |
| b55a2493-6fc4-36e2-a68b-cdf2018f784d | -7.56638 | -45.87602 | 2025-11-26 04:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 777219f1-8425-3cb9-aa61-36b4b45c31b6 | -4.99602 | -40.78923 | 2025-11-26 04:21:00 | NOAA-20 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 268a9f11-c53b-34dd-8642-ace6fc185d5c | -5.75205 | -47.47839 | 2025-11-26 04:21:00 | NOAA-20 | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 761d858d-2a10-3203-a8c1-b48ff2096734 | -2.71163 | -45.68767 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f76f0d0-4812-333b-81ac-2e9cd0a5c41c | -5.7128 | -46.52572 | 2025-11-26 04:21:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 20ac3145-e825-3949-930d-d50f06e06d86 | -4.05752 | -48.82428 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ed9881b0-9293-399e-ad2e-dc3973bbc52e | -4.53495 | -45.55632 | 2025-11-26 04:21:00 | NOAA-20 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16ecd901-5c51-3993-a443-e59bd0d330a3 | -2.9425 | -49.35947 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e6546f12-cfb0-3905-be31-a2db03d6dcab | -4.82974 | -43.8226 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6896d1cc-2588-3479-a8b4-07b890569462 | -6.10946 | -42.95195 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d0b7a407-4e64-3f44-b658-d8243ffba200 | -4.27111 | -45.12166 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 74573c76-ffa3-3681-b4c7-546b1fe3e049 | -8.06899 | -43.12201 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59a8353d-1255-37a9-80cd-e2ebf24a9104 | -9.11137 | -44.43517 | 2025-11-26 04:21:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6810330-059f-35cb-bfd2-a067966ad38d | -3.85473 | -49.36348 | 2025-11-26 04:21:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1b74a87-4cae-3530-af58-caf9dd1d2671 | -6.79299 | -44.12664 | 2025-11-26 04:21:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bacdf80-2b4d-3553-a1c5-755def4e5e22 | -6.35738 | -46.05669 | 2025-11-26 04:21:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 968c3e20-7284-32fe-b198-c999235de9ac | -3.21765 | -50.58572 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31a8aabf-2030-3b1e-a137-04d21b0adb2d | -4.16557 | -43.72544 | 2025-11-26 04:21:00 | NOAA-20 | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83748d0d-1dcf-30d6-b961-9318a5043968 | -5.27913 | -43.64327 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d3b29b53-2e83-3ca2-a2e0-94ff42437da9 | -3.26302 | -51.17356 | 2025-11-26 04:21:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2709f490-f400-3df4-9adf-4cce0df38a48 | -2.70764 | -45.69078 | 2025-11-26 04:21:00 | NOAA-20 | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 481e3c68-48bc-38bd-bf7f-c38cc71cc88c | -8.06156 | -43.12471 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 1b8854ec-6eae-37c9-8b3e-b9f7e0598a6c | -5.41765 | -43.05554 | 2025-11-26 04:21:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10a5cd01-17ba-32ec-a17d-e262dc54b3a8 | -4.28409 | -47.30623 | 2025-11-26 04:21:00 | NOAA-20 | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4b68c5f7-97fb-334b-8c7e-c962273b1cb6 | -4.5613 | -43.80161 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 3c15c62e-31dc-3ead-ac65-1554a1e7f07c | -3.17611 | -48.0316 | 2025-11-26 04:21:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 85c9b041-4442-30ff-8ab9-5240e6356888 | -6.0432 | -45.8388 | 2025-11-26 04:21:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5fbb207b-c984-38fc-8d35-3149507c7d48 | -3.49055 | -44.51521 | 2025-11-26 04:21:00 | NOAA-20 | MIRANDA DO NORTE | MARANHÃO | Brasil | 2106755 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22305a01-9d49-32b9-804f-d389de3d527f | -7.50679 | -45.71553 | 2025-11-26 04:21:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 34f07572-6c08-3a3f-9e28-15e58493fd48 | -3.91576 | -47.75608 | 2025-11-26 04:21:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b64d013-8340-34bb-8156-a6d93cb4c643 | -4.61484 | -49.46176 | 2025-11-26 04:21:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| df1d5940-bb2b-30df-868b-bf3517ed3e2c | -3.17791 | -48.62281 | 2025-11-26 04:21:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 74fc721b-ede6-3d2d-a145-9c548ea23ff7 | -4.04716 | -48.88934 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 624172da-968e-380a-92bb-557b07641058 | -3.37611 | -50.57573 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 61807fda-70f3-33ed-abe8-10cb8f99f0aa | -4.70587 | -43.98382 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f0db35f-42a5-3bff-bf38-6737acd1e0b4 | -4.26778 | -45.12114 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 66475b79-81a8-391b-b4c7-c4e7a8a1d4c9 | -3.8465 | -41.709 | 2025-11-26 04:21:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 90836ba4-0be8-3071-a4d4-69694bfd848c | -4.72401 | -46.4592 | 2025-11-26 04:21:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 54209967-209c-333c-9593-b41c53283b66 | -8.03641 | -43.10549 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e91317b7-069b-38d8-8820-f109a8aa45d6 | -5.31988 | -44.829 | 2025-11-26 04:21:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| cc2b40b5-69e5-3a19-9e46-0b6969f7a9b4 | -3.18413 | -46.59555 | 2025-11-26 04:21:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7240f298-0034-356a-a5c7-8083fed7cbfe | -8.05242 | -43.11563 | 2025-11-26 04:21:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 36.8 |
| 76c0807d-8aad-38d4-a7c2-117b00dfd2e4 | -4.01134 | -46.50364 | 2025-11-26 04:21:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4250d00c-2061-3bb1-b77e-21cd4febc0f3 | -3.84349 | -40.49267 | 2025-11-26 04:21:00 | NOAA-20 | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| b30cd047-0b20-3a72-ba8c-ad31e9438f79 | -6.24004 | -45.3273 | 2025-11-26 04:21:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6399f6d6-afcc-3c95-b9f1-3746f7628d74 | -3.22301 | -50.56964 | 2025-11-26 04:21:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f0ab53a8-f0b7-3853-b4c0-78a53c7c68e5 | -10.21346 | -36.37126 | 2025-11-26 04:21:00 | NOAA-20 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 47.3 |
| e28c9ce9-ab7c-3a69-9b0a-b9dc3cfbe6da | -10.01241 | -42.33811 | 2025-11-26 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 54d1b771-1751-3d1e-8ee8-bcd6229cb900 | -6.68175 | -44.70618 | 2025-11-26 04:21:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0ddd6c8-78aa-3a68-8f37-75054ca83e9f | -4.15777 | -45.15004 | 2025-11-26 04:21:00 | NOAA-20 | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1e199b5e-1176-3a52-a4d8-5a2373a460ff | -2.47973 | -47.83018 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ad8aaaab-243c-3fe0-83f9-5b26acc055e1 | -2.87391 | -51.80435 | 2025-11-26 04:21:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c4629006-0f50-36d9-b69e-ba10290e0ae5 | -3.82865 | -48.99238 | 2025-11-26 04:21:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18fdbad9-d433-31ad-8b31-ff51e4641e91 | -6.06635 | -43.25362 | 2025-11-26 04:21:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a9532ff7-22b7-3f95-b474-a4626d27db50 | -4.70424 | -43.99418 | 2025-11-26 04:21:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae44343f-b878-3f4b-b501-38a1f2a978a9 | -5.17385 | -35.70598 | 2025-11-26 04:21:00 | NOAA-20 | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 4eb68bd5-ad9f-3e9c-8eb5-78bae023d731 | -6.30287 | -43.78486 | 2025-11-26 04:21:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ba1c5c71-8525-32b1-b9a7-6b7e66ccafbc | -6.10607 | -42.95142 | 2025-11-26 04:21:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 2fae7ab6-e24b-3e3b-afa8-c0b541392082 | -2.4963 | -47.82346 | 2025-11-26 04:21:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2c2f1baa-c2e9-30ff-ae5f-50d76c96b415 | -3.39599 | -49.52463 | 2025-11-26 04:21:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b9b5dad-7cdb-3240-bb81-24d0fe66cfcc | -10.01303 | -42.33388 | 2025-11-26 04:21:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 9fe3aa90-17ac-34e6-a4b7-47d85e0ab9c6 | -3.13547 | -49.40176 | 2025-11-26 04:21:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3e37f954-7f58-3ab7-a1e8-8e9a43448828 | -3.48163 | -43.43039 | 2025-11-26 04:21:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ec6dd51b-ec85-3cb0-acdb-5eba1cd745bb | -6.16504 | -41.82893 | 2025-11-26 04:21:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |


[Clique aqui para ver as próximas entradas](README14.md)
