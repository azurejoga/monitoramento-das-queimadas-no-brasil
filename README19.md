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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8afe3888-f7cb-3ebc-8aee-d9e38973dd7c | -10.73213 | -47.92781 | 2026-08-14 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d5155ff1-9933-3e21-b939-cc376fb0559f | -8.45047 | -45.11365 | 2026-08-14 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e00871f2-baf3-3250-91de-09804936e760 | -6.90915 | -43.6344 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 82609ab8-515c-3cf5-b89d-ed9f3c515560 | -3.85414 | -51.33964 | 2026-08-14 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35aef1ff-9f52-3060-8b41-77e6d337dade | -8.60759 | -54.67025 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4020c418-569d-3901-a19c-c648f05ebbec | -7.02439 | -41.44482 | 2026-08-14 04:32:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 33d5111f-a120-381b-9ddd-ca8ba55a0793 | -9.81324 | -51.95086 | 2026-08-14 04:32:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d2861ac-ef98-3da1-bdb1-ec31ae67f1e4 | -9.12573 | -46.40123 | 2026-08-14 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4561563d-8c86-3753-a2d4-4abd1099c20f | -6.59745 | -56.33502 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c12f955c-5577-3fa4-991f-ab2c64042c97 | -7.85033 | -56.59653 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3cd3fc2e-57ec-3205-b154-0eaa4af03af9 | -6.11124 | -44.02515 | 2026-08-14 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f31cf675-643c-36b2-9718-725790c7aec6 | -6.70127 | -58.95312 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6d6cc15f-2cc8-3845-9f37-0dcf06e213a9 | -7.60393 | -46.46725 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 01d6fd9f-e650-34f4-866f-599a74df20b6 | -7.33495 | -47.81508 | 2026-08-14 04:32:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b92d4bdc-d7ce-3ef0-b241-2637cc62bce5 | -6.91148 | -43.64306 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 554c190a-df9f-3b89-bd2d-227911e56bda | -6.83183 | -56.42099 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3d7d9672-ed7f-371b-a32c-e78dd3f82c74 | -4.01458 | -48.96069 | 2026-08-14 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497692b2-b677-3efd-b3d5-389b7f0c3a58 | -7.37112 | -59.97271 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1569c42e-4cee-3ba6-a56c-f16b095ef7e0 | -4.27121 | -49.36718 | 2026-08-14 04:32:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7c5fcffa-895a-3520-9f2b-e4eb6fb608cb | -6.84456 | -42.90434 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 30726cdf-31bc-3a0f-a408-b7dcb28bde78 | -5.31862 | -43.55922 | 2026-08-14 04:32:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ccaf04b3-2548-3703-baec-2c09293affba | -6.59884 | -56.33415 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 89791554-ae3c-3911-91a2-7f9421b1a42d | -9.48548 | -51.63488 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23700e85-e938-3471-bcbd-c04ff26593d6 | -10.29534 | -46.65105 | 2026-08-14 04:32:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b62d5266-080c-3442-8903-5ee2980fd746 | -4.19546 | -46.81256 | 2026-08-14 04:32:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 277368e6-34d8-3b8b-aa9a-355ca3c3dbd3 | -7.60338 | -46.47071 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc127139-5652-386b-8a79-c3423e3878aa | -7.80838 | -44.1153 | 2026-08-14 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5f75a4c5-dce0-34b4-9f40-0c1e9d9fb35c | -8.0235 | -55.12042 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8457f162-90d3-305a-b81e-0ca3d41f1e3b | -4.50388 | -42.54059 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| bdb0775f-15f9-3601-8bea-f23368e16c9f | -9.12905 | -46.40175 | 2026-08-14 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47efd050-efba-36c6-987b-87b20e2e83c0 | -4.50321 | -42.54491 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e50eb95a-81f2-3195-8760-3b3b9a29a6b9 | -7.61065 | -46.46835 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8ac133bc-238c-3d4d-9dbb-20293d16422d | -6.78402 | -58.7593 | 2026-08-14 04:32:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 65d1efd9-90b6-315f-a7b3-f479b50bea0d | -3.1107 | -47.90929 | 2026-08-14 04:32:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9a2cad38-6041-3074-b79e-c661e7b6ddc3 | -6.24598 | -47.69543 | 2026-08-14 04:32:00 | NOAA-20 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e03c0f1b-0309-31ab-beda-9694fa780680 | -10.18963 | -48.73747 | 2026-08-14 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ea263378-2bcb-36e5-832c-b0feaf0274b0 | -10.18568 | -48.74051 | 2026-08-14 04:32:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3ef310bb-7f75-301d-b5a3-7d092e1a31da | -5.78442 | -45.0521 | 2026-08-14 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a16f2227-6902-3eaf-be6e-012fe21b5b9f | -6.59562 | -56.35252 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f838415-c52c-3076-a3e3-d8e977d0cf5b | -4.4922 | -42.54321 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| ca6716df-45ae-3a95-8858-a33766494f3c | -6.77746 | -42.65878 | 2026-08-14 04:32:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 064a026a-8b00-3f4c-ae4a-2197f6192b56 | -7.80486 | -44.11474 | 2026-08-14 04:32:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 705d6acd-1df0-332a-9d40-deb7df542d45 | -4.49454 | -42.55239 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20c1a736-dd58-39cd-bed4-b63d7759ea90 | -5.55465 | -44.11437 | 2026-08-14 04:32:00 | NOAA-20 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79283e1c-0dd9-39d9-a84d-a7322d0798d1 | -7.60724 | -46.46777 | 2026-08-14 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1584d870-20c9-33c3-8fb4-1eba98c4a947 | -6.6233 | -59.04344 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8a10cc9b-694c-34b8-a8fd-ba570e9bdc6a | -8.46426 | -51.55402 | 2026-08-14 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd4e557d-8c78-3844-a1cd-fb7ad3af9b16 | -6.6059 | -56.35155 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96732233-838d-32bd-9b16-be333f58c90d | -6.6222 | -59.04924 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d17beea9-9fe2-32ca-95a7-da75842de14f | -8.55063 | -45.33147 | 2026-08-14 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5019b12a-b057-3f68-bfd8-8ba80d71f9b8 | -6.60439 | -56.33517 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f733aa8-0985-3dbd-8191-8b470c096561 | -4.42621 | -46.30215 | 2026-08-14 04:32:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8395b0c6-1aa5-3a51-92ed-82595fc176d0 | -7.71565 | -46.23219 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e5b6f2f4-3124-3c94-b5e3-4dde41e3a258 | -4.741 | -48.0202 | 2026-08-14 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| fe086f7f-d4a8-38d1-b71c-0f346979480a | -5.5943 | -37.7395 | 2026-08-14 04:32:00 | NOAA-20 | FELIPE GUERRA | RIO GRANDE DO NORTE | Brasil | 2403707 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f3956612-693f-3b68-9710-88fb75623245 | -4.50088 | -42.53571 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 18.5 |
| d041c074-755c-3cac-a96b-3e1fa04a54d6 | -4.64324 | -50.92993 | 2026-08-14 04:32:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 921a9455-87e0-3414-9a1a-b46f3f6ec810 | -6.18842 | -47.33413 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 23.9 |
| a62a5230-902f-3d51-aab5-33cf1d546296 | -5.78106 | -45.05157 | 2026-08-14 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 66ee2da3-af38-373f-b092-f68aff3896f8 | -7.71233 | -46.23167 | 2026-08-14 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a2332ebd-e1a2-38cd-8b16-1cfd6a1a2d14 | -7.4507 | -44.87552 | 2026-08-14 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 08451a7e-4980-30a2-a2bf-9a0f4805fd01 | -6.85845 | -42.92698 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 816c1b6f-999d-3299-939b-d4c6cc95b794 | -6.99972 | -44.82574 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e4d3d8fa-0aef-30f1-aa54-90c2c2482d85 | -3.33733 | -50.14598 | 2026-08-14 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07e65996-c459-307c-a24a-237e0cc66fae | -6.60034 | -56.35061 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7a55d41-8b6f-3477-a4b4-b1d444ffca3a | -6.96577 | -59.29074 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| edfcb948-83bd-3200-9d8f-bd492e09d746 | -6.95696 | -59.30108 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 38091ffc-f183-36d2-8c62-21d2c8c7e66a | -6.11062 | -44.0291 | 2026-08-14 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a5b5a62a-1cef-3495-acea-d5cfea9c3908 | -6.26005 | -43.27509 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3b0b2175-afe0-3de6-85b1-d786710789c1 | -4.25216 | -48.54443 | 2026-08-14 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0859c57e-0d05-353b-ae6c-9ef580d9d707 | -6.67576 | -43.40368 | 2026-08-14 04:32:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca4c4253-9500-397a-85b8-a0264d181749 | -10.38997 | -47.34438 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2ce9c4df-6430-3fa4-b25f-834480ef81aa | -3.2366 | -49.46059 | 2026-08-14 04:32:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6110608d-df0d-3e2c-86e9-fb3496d44250 | -3.26072 | -49.52378 | 2026-08-14 04:32:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4acc9f57-2eb6-38b9-b55f-0826fe288ad7 | -6.4185 | -39.25984 | 2026-08-14 04:32:00 | NOAA-20 | IGUATU | CEARÁ | Brasil | 2305506 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2ae7d5ef-b9ea-36ea-8ab6-4fa8dbfddfd3 | -6.26166 | -43.27428 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b3cd8529-d60a-32ac-9f9f-dcd6fc72dc5b | -2.97283 | -51.69087 | 2026-08-14 04:32:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61cb1055-c9c8-35f8-b161-e51750698cb7 | -9.1296 | -46.39824 | 2026-08-14 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07459daa-a9b6-30ae-b642-08d1f8b7e1a1 | -6.18452 | -47.33711 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef69bb31-aef7-3e83-8568-67d7342fd678 | -6.61998 | -58.99608 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 132aa298-ecdc-34e9-a577-8d6b32b36f9b | -3.3412 | -50.14659 | 2026-08-14 04:32:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b3c6a28f-bb68-3d30-bf41-71a0bd816e31 | -8.46818 | -51.55465 | 2026-08-14 04:32:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ee7339d-ba58-3ee7-ade0-107ab33b652d | -6.59692 | -56.34512 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79ef6ab5-94e8-34fa-ae20-d1ba76e1976b | -6.62724 | -56.26565 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 7ae9cd6b-3aac-3457-bb1c-baab44729367 | -1.77791 | -55.52874 | 2026-08-14 04:32:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8d7b67ef-4177-385c-8530-f11a7f744402 | -4.50622 | -42.54977 | 2026-08-14 04:32:00 | NOAA-20 | LAGOA ALEGRE | PIAUÍ | Brasil | 2205557 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 746b23d6-af8d-3400-8971-d4f36650c5aa | -6.70874 | -58.94926 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 32535c5b-464b-3e61-8fca-da40f44dc62d | -8.023 | -55.1232 | 2026-08-14 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2df0a241-f6f5-3bae-a0fb-0bc0e4fc077f | -6.90853 | -43.63844 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 26a248fe-2c39-3ec9-aeea-c745944164ee | -6.18786 | -47.33764 | 2026-08-14 04:32:00 | NOAA-20 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c6c4b51-fb9f-36b5-b70b-01c9c94e998f | -5.78497 | -45.04853 | 2026-08-14 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3fd38348-cf30-3439-9816-9ee0766cfec8 | -6.27186 | -43.28011 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 709e96ff-d779-360b-a345-7aa0bf50a9f6 | -6.86345 | -42.91879 | 2026-08-14 04:32:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 995ca96d-aee1-34c2-a1a3-1826e4092d6f | -6.59966 | -56.35433 | 2026-08-14 04:32:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| df34f7bc-3553-32af-83ef-97cc2c20c630 | -9.48868 | -51.63283 | 2026-08-14 04:32:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b6d768f8-4b21-3438-adce-f92c35d2ea6f | -6.96467 | -59.29657 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| e307e8a8-b488-391a-9b72-682979a40552 | -6.41059 | -45.67647 | 2026-08-14 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9ca225ab-9c55-3374-bbc4-dd8cd368794a | -6.91567 | -43.63956 | 2026-08-14 04:32:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 93e73c66-07f4-3792-8e91-ba1e7727ec73 | -6.95914 | -59.28952 | 2026-08-14 04:32:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 9f53a1d1-c4d3-3bd0-bfcb-1f86fe0916be | -8.52074 | -45.33801 | 2026-08-14 04:32:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README20.md)
