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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da3d64f6-0925-33c0-ac0d-0856c9fa4bb9 | -10.49119 | -42.42536 | 2025-05-26 03:28:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 1228568f-1c76-3c8d-b150-d01b7b25ac9c | -7.91218 | -44.47913 | 2025-05-26 03:28:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3eb09bc-5839-305c-ba0d-38e90ff2830a | -7.4669 | -43.37488 | 2025-05-26 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c900f30-a24f-3087-909e-99d7be3ec082 | -8.04737 | -43.14087 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 22e0a011-c2b4-361a-a9e8-63981d58116a | -5.68256 | -44.12725 | 2025-05-26 03:28:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d5422a4a-dfd6-399b-9ef7-d1b059a3dd9f | -8.07395 | -34.97576 | 2025-05-26 03:28:00 | NOAA-20 | RECIFE | PERNAMBUCO | Brasil | 2611606 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 398b1151-4f07-3ad9-9318-0131f1f53b12 | -8.06818 | -43.12704 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| 6f35d3fe-692d-3e2e-9cbd-c09605f61e3a | -8.02336 | -43.20476 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| b153c4d4-7401-303a-9a3e-66c264be2860 | -8.02581 | -43.19156 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| d70707a6-6ce3-3cde-8a39-3f5898700537 | -7.66545 | -46.11295 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ea1c303-ba30-3dd7-921d-791e54d6ceca | -8.07037 | -43.13686 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 893deea1-b95f-31d2-9d43-ee7a13d9bbb2 | -8.04658 | -43.1452 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8fd835a7-d7cb-3df9-be3d-f077722adf74 | -7.47376 | -43.37152 | 2025-05-26 03:28:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9d9cfb9-1a32-3ce9-99cf-e6b3a8dadaf0 | -6.40279 | -35.27579 | 2025-05-26 03:28:00 | NOAA-20 | PEDRO VELHO | RIO GRANDE DO NORTE | Brasil | 2409803 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 22dd70bf-6233-3edf-a929-f9a9778b2ddc | -7.59641 | -46.27756 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 6d51a025-4522-3b3f-a8d8-60861e082237 | -8.01995 | -43.19015 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 3a868c71-697c-3ffc-afee-bae169e29317 | -7.66166 | -46.11093 | 2025-05-26 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3757bb9-71db-3b21-ae1f-92dd58c125b5 | -8.07204 | -43.12809 | 2025-05-26 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6178dd06-11f5-3360-82d2-ad6a64b4a5f6 | -8.0309 | -43.2199 | 2025-05-26 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 2b926e07-b4b0-3d51-90b1-3f8bc6c2d530 | -8.0123 | -43.1984 | 2025-05-26 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.2 |
| b2f34fb7-3a14-3356-8d6a-23a9d7ca9130 | -8.0315 | -43.1728 | 2025-05-26 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| bc263904-ed73-393c-baa0-29e06cde2139 | -7.6574 | -46.1013 | 2025-05-26 03:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.2 |
| c6365d29-65d6-3c12-b21f-aa0bd2e53fbd | -8.0312 | -43.1964 | 2025-05-26 03:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 207.6 |
| 3013677d-a505-36db-8909-bf5e23c10ad2 | -15.42628 | -42.16751 | 2025-05-26 03:30:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ebcf03e0-2d4d-37f6-a60b-e5ab2329dcb5 | -15.42971 | -42.16383 | 2025-05-26 03:30:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 464032d4-f2da-3a75-b5c9-0a9196921a88 | -10.65012 | -44.49695 | 2025-05-26 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 19d9eec0-7b6b-39e1-b22d-39d119a2479b | -15.42861 | -42.16943 | 2025-05-26 03:30:00 | NOAA-20 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.9 |
| b8d410f7-34d3-3235-8a33-7bd238937db0 | -12.86165 | -38.36713 | 2025-05-26 03:30:00 | NOAA-20 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 57aa7537-12dc-3ee3-86d1-cec9367d05d5 | -10.65624 | -44.4982 | 2025-05-26 03:30:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a0a25d62-307d-3ecc-8123-55561937992e | -22.53852 | -48.81559 | 2025-05-26 03:32:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d61e3ad-40ee-355f-9a60-e46101bbc2ba | -22.69682 | -43.34699 | 2025-05-26 03:32:00 | NOAA-20 | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6de1ea30-840c-3049-821e-19e45843f51c | -20.60721 | -48.86482 | 2025-05-26 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 6478fb3a-fd28-3b07-a45e-79d67f9daea3 | -20.59827 | -47.55407 | 2025-05-26 03:32:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2bd846a-7ab5-3a32-9c2a-3b327afd9099 | -22.34117 | -41.78593 | 2025-05-26 03:32:00 | NOAA-20 | MACAÉ | RIO DE JANEIRO | Brasil | 3302403 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| dacd641c-6dee-375c-a007-7c65bed635bf | -19.53245 | -43.89029 | 2025-05-26 03:32:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 839a15b0-64e3-36a0-9f1e-3536d4e9b917 | -20.59941 | -47.54919 | 2025-05-26 03:32:00 | NOAA-20 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4fec310b-dbea-3e08-bbbe-24d510056a66 | -17.66588 | -46.68013 | 2025-05-26 03:32:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fdc9bf09-8cde-3bd3-a818-775a81323e3d | -20.61092 | -48.8681 | 2025-05-26 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 2d2cfd4e-2a5f-36c8-8cb4-9b86b321214d | -21.27075 | -48.61503 | 2025-05-26 03:32:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 2acc9d8d-0e69-3d6d-be41-1272005b5966 | -20.60572 | -48.87112 | 2025-05-26 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5c5076bf-73ee-39c3-b699-ab3aa85ac56c | -19.53309 | -43.88725 | 2025-05-26 03:32:00 | NOAA-20 | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 228f905b-9f06-335e-9b3e-ec3a1cfd39bc | -20.6044 | -48.8663 | 2025-05-26 03:32:00 | NOAA-20 | OLÍMPIA | SÃO PAULO | Brasil | 3533908 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 3588ea20-ada1-3a1c-aec3-61e1dab04b4d | -22.53716 | -48.81229 | 2025-05-26 03:32:00 | NOAA-20 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6a64353a-8b6c-308a-9920-26c886e7f8fe | -22.90314 | -43.75317 | 2025-05-26 03:32:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 53288fc9-c73d-320c-a5cb-0b341b4b8d4a | -21.27705 | -48.61702 | 2025-05-26 03:32:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| b7ae1471-e646-3644-9b22-2b208ec4f2b9 | -8.0123 | -43.1984 | 2025-05-26 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 65.9 |
| a72e2fbd-96db-3231-93f8-20d6cab1ee9c | -8.0315 | -43.1728 | 2025-05-26 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 94.6 |
| 012825c3-4479-380f-89cf-43dfd66465cb | -8.0312 | -43.1964 | 2025-05-26 03:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 244.4 |
| f2412f96-7d88-3fb0-b728-d36d365e3fd8 | -8.0123 | -43.1984 | 2025-05-26 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 71.2 |
| 0eeb191d-8138-3bfe-899e-842a8945aa35 | -7.6574 | -46.1013 | 2025-05-26 03:50:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 50.1 |
| f12837e3-38c7-38f8-874f-ccaeb379a796 | -8.0315 | -43.1728 | 2025-05-26 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 66.8 |
| b0e95b56-4fdd-386d-9e12-c17fbeb2c9fe | -8.0312 | -43.1964 | 2025-05-26 03:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 210.3 |
| ad500040-7340-3f79-ac60-b7d6282f3e25 | -8.0123 | -43.1984 | 2025-05-26 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 83.6 |
| ca253d50-1f1a-306d-a362-b7ec8449ee57 | -8.0312 | -43.1964 | 2025-05-26 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 158.5 |
| 5a4f7c39-c95e-352c-b1a3-fab9367771d1 | -8.0315 | -43.1728 | 2025-05-26 04:00:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 61.1 |
| 6f50c8fa-4c5f-39f9-be0f-bffa49654885 | -8.0312 | -43.1964 | 2025-05-26 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 155.3 |
| ba8f6dab-1fd0-3f4b-bb91-1946ba38a1e1 | -8.0123 | -43.1984 | 2025-05-26 04:10:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 110.0 |
| 5d6e16d6-6258-3da9-aa8e-1cfda8eb96d6 | -7.59352 | -43.38239 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ca86b0af-1934-3a2c-a2ee-1a0c2dc8bf54 | -8.02423 | -43.2028 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| be1a31ae-3cbd-38fa-8118-9adbbd3f7137 | -9.37612 | -48.41307 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 243ffaa1-b431-3484-bba2-a99afce953bf | -8.06951 | -43.13382 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 13.2 |
| 738b2e31-564f-3048-95ca-75316104a42f | -8.07063 | -43.12637 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 0b3e020b-5985-3e32-a80f-75dc3785d7ef | -7.35673 | -43.6883 | 2025-05-26 04:19:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 84f2cbc7-4624-317c-867b-b36b197aeb03 | -8.0282 | -43.1996 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 14eff905-18be-3931-85aa-147cf527a449 | -6.98693 | -46.31408 | 2025-05-26 04:19:00 | NOAA-21 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a6e66e58-d26d-36e3-a4e3-563b433e78f1 | -8.07007 | -43.1301 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 121f2e8c-e093-30fb-8efc-588ab8c6064b | -8.02986 | -43.18849 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 2927fc3c-6acd-3c05-8b4b-389917eacb4b | -7.65608 | -46.10672 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| bd2964d7-9b16-358d-96c9-23a527609aea | -9.37681 | -48.40897 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 386c14bb-acd5-30ca-b14b-c79835415e42 | -7.52279 | -43.36009 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4da1ec30-2d92-345d-83d5-837c366c0f97 | -10.06114 | -46.52349 | 2025-05-26 04:19:00 | NOAA-21 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31e33aae-52f1-3f0f-9539-9f4f1e9e5d40 | -9.18773 | -49.63736 | 2025-05-26 04:19:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bad789d2-57c3-3cac-871a-b4c7620cecbe | -7.53488 | -43.1671 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 657f8c15-090f-3a66-8124-048327be4d17 | -8.02248 | -43.19118 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 396191dd-b5e5-3eeb-9bcb-366b6dfb6c31 | -7.67964 | -46.10669 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 908f2ee1-94ca-3ef1-8af5-711de8dcded0 | -9.79686 | -48.52626 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9e3e519-6756-397c-b3bd-3d80ffc7b527 | -7.60174 | -46.27639 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d614b455-d96e-3369-970b-1e41c9935157 | -8.02246 | -43.1879 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9599f72d-d4a5-3355-b06b-efc61bccda78 | -7.47611 | -43.37156 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a62552ad-d7f8-3765-9242-de971e54fc04 | -8.02875 | -43.1959 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 86.1 |
| 1c31e1c2-1633-3335-ab5a-bdb3db70b16e | -9.37543 | -48.41718 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 75007e6d-8978-3119-b380-eb0be22599bf | -10.65574 | -44.49764 | 2025-05-26 04:19:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 30892e9a-6aa4-303e-97ea-565e45f9b255 | -7.06577 | -44.92781 | 2025-05-26 04:19:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 517b35e0-1a81-311e-b970-b45e3937bef2 | -6.30234 | -46.05475 | 2025-05-26 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d2e8db00-d155-3a18-8fee-47abbda6efc5 | -7.54352 | -45.82891 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fe537a7b-68b4-3be8-bc61-b9c239220e12 | -9.377 | -48.41415 | 2025-05-26 04:19:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d73d8b2-655d-3606-a686-d82e8e73d950 | -8.03327 | -43.18901 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| d4003807-bc4b-3807-b465-e067d14739ad | -8.02415 | -43.18006 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 260294bf-d09a-3750-ac00-b7dee66f4906 | -7.59462 | -43.3751 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| effc0b97-6e47-3306-b933-db07272dfb8a | -6.30569 | -46.05529 | 2025-05-26 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| daab4298-0589-3bf2-a49b-a1f9fbcfc74a | -7.51603 | -43.35907 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 21054046-b92d-3bdf-9dcd-84f7c62c59ce | -8.02931 | -43.1922 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| b4af0fc6-354e-344a-980f-fe91c9429fd8 | -7.53544 | -43.16343 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 786150b3-9fca-3804-9fe4-138fd4d6865b | -7.35725 | -43.32388 | 2025-05-26 04:19:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 70c29a00-95ae-350a-bc06-b4c80a30ffea | -6.30904 | -46.05583 | 2025-05-26 04:19:00 | NOAA-21 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 82fea1f5-b52b-32dd-9ad2-3d638cffd0f4 | -7.65387 | -46.0991 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 624a89c5-6247-3c52-9130-ecf2d79789d7 | -7.59837 | -43.30474 | 2025-05-26 04:19:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1090978-c0ff-3cfa-8ed0-8e56bbd9047d | -8.05075 | -43.14239 | 2025-05-26 04:19:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cf7ace50-d05c-3293-9b9f-443f1baa6bff | -7.66275 | -46.10778 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb23f4b6-1e2c-3c0c-9516-82125e444fc8 | -7.65776 | -46.09609 | 2025-05-26 04:19:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |


[Clique aqui para ver as próximas entradas](README4.md)
