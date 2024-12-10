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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d289030e-6bf7-380e-a747-6a096ce5bfea | -1.64177 | -45.91094 | 2024-12-10 03:57:00 | NOAA-20 | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 554b7fa8-6e97-3cee-94f1-180dd71cc779 | -3.67775 | -49.57551 | 2024-12-10 03:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98b925eb-9319-3517-995e-93ab95b1669c | -6.72984 | -46.29478 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43108a72-322b-3f42-8d2c-151c0fd6bc45 | -6.90908 | -43.51652 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 61a3f358-13ae-30a4-b125-85d5d2f89209 | -5.92054 | -48.05713 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08e5e5ab-8247-3752-b01e-a0dc38acdbb2 | -5.91494 | -48.05941 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 43cd867c-24ce-3eac-bc3f-8034d1808d8e | -2.81079 | -52.9827 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c154cae3-5b8a-3a15-bbf0-4e584ba31777 | -6.73061 | -46.29038 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 881fde4c-cf25-3d77-99dd-f809ebc3686e | -6.33947 | -43.43302 | 2024-12-10 03:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c507d557-4d16-3fd9-9649-4355a49c96be | -6.33506 | -43.43678 | 2024-12-10 03:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5a0ff4-9824-36b0-8e1b-cccc5f188eed | -6.02461 | -46.25035 | 2024-12-10 03:57:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1b966ec5-c279-3788-9e1f-567833cd8f79 | -5.48741 | -44.70675 | 2024-12-10 03:57:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9891ab07-0fa9-30ef-acd7-8fe00fbb0e4a | -3.95728 | -38.45008 | 2024-12-10 03:57:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ce54da71-49f3-3f9d-b873-16d78cbd48f8 | -4.54615 | -48.014 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5c34596-5366-38d0-b2e8-03c9b3bd4622 | -5.49694 | -39.46038 | 2024-12-10 03:57:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a2d60739-9c0f-37be-8780-e023a9de9933 | -7.85952 | -35.20139 | 2024-12-10 03:57:00 | NOAA-20 | PAUDALHO | PERNAMBUCO | Brasil | 2610608 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 77918df7-f962-35fe-865e-72570b5e164d | -3.66658 | -39.47919 | 2024-12-10 03:57:00 | NOAA-20 | UMIRIM | CEARÁ | Brasil | 2313757 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0798fa0f-fb53-305e-9fd9-c356eb836bc2 | -2.87973 | -40.46254 | 2024-12-10 03:57:00 | NOAA-20 | JIJOCA DE JERICOACOARA | CEARÁ | Brasil | 2307254 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c6519cae-3696-3ad6-9bd4-3ade2d7722c1 | -3.52222 | -52.15122 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 893048d4-d2bb-349f-9e04-66e3e4ada8f7 | -2.77683 | -44.99651 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 5fb38748-31b9-3664-b8b6-d2165758ba22 | -3.35184 | -42.33245 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c42458eb-f371-339f-ab9a-3c4669aa7605 | -3.30209 | -42.48085 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee6ceff0-7cad-3a4c-a714-7d9c987afe33 | -7.23663 | -40.85327 | 2024-12-10 03:57:00 | NOAA-20 | ALEGRETE DO PIAUÍ | PIAUÍ | Brasil | 2200277 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 573b8a71-e6cf-3e6f-ab64-9a4cf624152e | -6.83302 | -44.38491 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 798a07e1-fc95-35d7-8c63-26b8285a1a8e | -3.62781 | -52.68495 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 6c7424c3-a244-343b-b33f-52f887f3329f | -9.40853 | -36.00468 | 2024-12-10 03:57:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f7879d41-3910-3d16-92f2-83f9e0ab2399 | -4.61834 | -37.69729 | 2024-12-10 03:57:00 | NOAA-20 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8f08a775-1586-3da7-9660-58e8efe41b79 | -6.90444 | -47.83643 | 2024-12-10 03:57:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8240351a-bc26-36e7-8754-7b764a74acb3 | -9.03994 | -35.70431 | 2024-12-10 03:57:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 3c3c660d-32d9-3d36-b2b5-b5c145b6b645 | -9.03921 | -35.70929 | 2024-12-10 03:57:00 | NOAA-20 | JOAQUIM GOMES | ALAGOAS | Brasil | 2703809 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 9f3d354f-8de1-305b-8dd1-7b16b72d1c9a | -5.91599 | -48.05339 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6bef3c47-2f8f-377c-bf65-3ca9d44f1ef9 | -3.22773 | -42.43127 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab45a79b-1dc3-3ae9-8ff1-04b01d7c4d60 | -6.73562 | -46.29315 | 2024-12-10 03:57:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b672100c-089a-3157-8732-74c0e93ce8a5 | -5.86893 | -38.24602 | 2024-12-10 03:57:00 | NOAA-20 | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 95800f6a-bd91-3de8-8631-c676db7535cd | -6.25455 | -43.55529 | 2024-12-10 03:57:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 717a1073-a4ad-32fd-b65e-fefefccfd1a2 | -8.87837 | -41.1058 | 2024-12-10 03:57:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e0b2ca4e-555d-3226-aa71-0e73a2e168ed | -5.62376 | -44.84091 | 2024-12-10 03:57:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| eeaef48f-3a49-3c27-a42d-49cff3ff4106 | -7.88919 | -42.44398 | 2024-12-10 03:57:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 007c4255-a918-35c3-8c8b-c1022b160675 | -6.59704 | -44.15834 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c0187e9-d8ad-3cfa-b95c-5c636ffb03cf | -6.91351 | -43.51272 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| ac2a4012-a1a9-34f3-9e1d-3348659cd635 | -3.07465 | -40.04521 | 2024-12-10 03:57:00 | NOAA-20 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 3.8 |
| e144ae14-bffa-35b7-bf0e-6bdd8fc3b00d | -6.83603 | -44.38853 | 2024-12-10 03:57:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 3cd6f857-55a7-3712-bc90-ebbd2054f2f5 | -5.19445 | -47.73515 | 2024-12-10 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c2b39887-9847-36be-a353-ac8d66e9c8a6 | -4.87269 | -48.21656 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 97a521f0-be64-34eb-af99-2b522a790ede | -5.76221 | -47.8735 | 2024-12-10 03:57:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| aba1d5aa-adab-35c1-84d8-ae969ace2b66 | -7.25003 | -48.42331 | 2024-12-10 03:57:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e68c47fc-5743-30df-a292-d03ca5203bfc | -6.91278 | -43.51712 | 2024-12-10 03:57:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 8.6 |
| eef4f8e1-1c18-37f3-b453-516762010e8a | -5.44653 | -45.58781 | 2024-12-10 03:57:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 995ae4e9-e998-3b86-8ab3-60cf67bfa649 | -4.14641 | -44.29012 | 2024-12-10 03:57:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0c1c9111-c98e-3413-8c7b-8753e564d290 | -5.28626 | -44.91396 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 103dd50c-e5a5-35c6-9704-8fd8246037f2 | -9.41241 | -36.00521 | 2024-12-10 03:57:00 | NOAA-20 | ATALAIA | ALAGOAS | Brasil | 2700409 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 9cd3bb39-2fe4-38ae-9cd4-f35bd7590c6b | -3.8266 | -52.35816 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2d515c7c-9fbc-3fff-9d88-ea92ec4a470b | -6.94329 | -42.84906 | 2024-12-10 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| e3d64506-7c76-3806-88a2-56f20faca660 | -6.33876 | -43.43748 | 2024-12-10 03:57:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29a56d84-84e2-3f2e-8261-951b4ecae99a | -5.19395 | -47.73805 | 2024-12-10 03:57:00 | NOAA-20 | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a90a53b1-2375-3b4d-a620-f4bc7461ed5e | -2.98773 | -44.94972 | 2024-12-10 03:57:00 | NOAA-20 | OLINDA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2107456 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9d586033-e969-3aee-939f-8259c05163f0 | -3.23572 | -42.42811 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| d929e9fc-30e7-3b7c-891f-a9f6de293748 | -4.54457 | -48.02333 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6f25792-ea0f-38dc-806b-9363e084260e | -5.92107 | -48.05412 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb0551f4-f0c5-322e-a2f8-16e510e6e90e | -4.5451 | -48.02022 | 2024-12-10 03:57:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 268058cf-388b-3b95-b0e9-fd4b7e367e4a | -6.56239 | -46.5802 | 2024-12-10 03:57:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 03c65ff9-9ae9-3a4b-8d2c-ebf53bd2f9c8 | -3.39082 | -52.67237 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 05061262-3269-3626-aa29-320bed8dfd67 | -3.3713 | -42.32695 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 74119b5f-1c70-362d-b136-4afcaa67726d | -4.70343 | -43.79068 | 2024-12-10 03:57:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 27650033-72ee-3871-a955-57d35aa4cb04 | -5.62145 | -43.9561 | 2024-12-10 03:57:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c3574e3c-ca59-372d-91e9-3fda28838d97 | -5.33609 | -45.11277 | 2024-12-10 03:57:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 33694626-101e-348f-b1b0-49494bcaf0e1 | -3.97351 | -45.62164 | 2024-12-10 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ef801bce-743f-3291-8e9a-8c53224bedea | -1.70536 | -52.61497 | 2024-12-10 03:57:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89de7de2-3831-3e3f-a368-58ba642b09d9 | -3.78283 | -50.00904 | 2024-12-10 03:57:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d21704f3-c6a9-388e-9c83-19800bbec9c0 | -5.71063 | -46.54642 | 2024-12-10 03:57:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fc1f66b1-f5c2-34bd-8ec0-625216f59ce2 | -4.88972 | -48.05191 | 2024-12-10 03:57:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 71697009-c023-3b48-9130-35f4416df19f | -2.99474 | -52.84893 | 2024-12-10 03:57:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 18.7 |
| ad04076a-da61-38f6-b22d-12aad69b394d | -7.40344 | -41.32083 | 2024-12-10 03:57:00 | NOAA-20 | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 6985429e-f7fd-3704-89ea-86d57333e772 | -5.38751 | -43.66252 | 2024-12-10 03:57:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7104b861-0795-3c0d-b70c-66c85c8e0933 | -4.35106 | -38.03977 | 2024-12-10 03:57:00 | NOAA-20 | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 76d29671-6b74-3197-83c9-653c5b8f3ffc | -3.83332 | -52.36021 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 651c583b-9b54-3cae-96f6-0b85adf39c93 | -7.83111 | -44.74116 | 2024-12-10 03:57:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 181a9056-4833-345d-a500-00674a529f55 | -5.07062 | -37.71696 | 2024-12-10 03:57:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 0.8 |
| e5c20919-b146-3b3f-bdb0-6aa7505a6679 | -8.45948 | -35.07081 | 2024-12-10 03:57:00 | NOAA-20 | IPOJUCA | PERNAMBUCO | Brasil | 2607208 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| eb4a0fb0-fcee-3b4b-8466-e28ea3d7d522 | -3.31811 | -51.47901 | 2024-12-10 03:57:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf98fd21-c5da-3da2-96dc-ff630cce14f9 | -4.01844 | -38.25227 | 2024-12-10 03:57:00 | NOAA-20 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0f0bcec8-3344-3827-8cd5-8afeabca1a37 | -3.37298 | -42.32186 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 872b0754-6c78-3505-b42a-87160c2a41d6 | -3.23639 | -42.42385 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 41920a63-c3b0-3eed-9cfc-169b16a35786 | -6.68623 | -39.26093 | 2024-12-10 03:57:00 | NOAA-20 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 1edbb69b-9e0a-3e64-be2f-b2ecffccb04f | -3.97721 | -45.62671 | 2024-12-10 03:57:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 7b52b4f8-c474-3abb-9c8f-9f52728e5680 | -6.40235 | -35.20483 | 2024-12-10 03:57:00 | NOAA-20 | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 47c1cbb3-c66e-3c76-a86e-53307ddfe73e | -4.16656 | -45.54515 | 2024-12-10 03:57:00 | NOAA-20 | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c208386a-c0be-346a-91a8-c4e640bb316f | -4.67319 | -49.50371 | 2024-12-10 03:57:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7da63cba-e74c-3a89-80ad-b1ca5cdeaad8 | -3.23139 | -42.43183 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3d19be6-3128-3f6b-85f5-163651e1dcf0 | -6.96979 | -42.99184 | 2024-12-10 03:57:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2bac7918-0466-3c67-bade-dad508634f39 | -2.91854 | -52.97341 | 2024-12-10 03:57:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e48ebcc9-6d71-3fec-bae1-240fbbacb509 | -3.23206 | -42.42755 | 2024-12-10 03:57:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a5cbf36-02b2-36f6-a96f-807806c7e1f6 | -6.06241 | -47.3824 | 2024-12-10 03:57:00 | NOAA-20 | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d07e51bf-d244-37cb-90a7-b934e97640d8 | -3.80955 | -52.25372 | 2024-12-10 03:57:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0df1f469-3404-31cd-97cf-2411e964f57a | -3.68424 | -49.57238 | 2024-12-10 03:57:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c9cd3dc7-3d1d-31c6-b2ce-9ef1df6d4e7a | -6.56078 | -46.5817 | 2024-12-10 03:57:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dd46456-06c6-3fa9-9861-8048f4ce41c7 | -10.44454 | -44.8903 | 2024-12-10 03:59:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 8b5df13e-022e-35aa-a3bc-ac91bfc77981 | -13.93827 | -44.36266 | 2024-12-10 03:59:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 15b518ad-8b19-3ff9-81af-82b0a3e49047 | -10.0869 | -42.40751 | 2024-12-10 03:59:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| c89cf7de-2c49-38c8-84c6-ebcabe3c705d | -8.86131 | -47.67236 | 2024-12-10 03:59:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README16.md)
