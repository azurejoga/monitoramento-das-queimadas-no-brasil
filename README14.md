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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4ba0991f-56a3-39bf-a31b-fcd65d746a0d | -15.79736 | -43.65419 | 2025-10-19 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 52e9e021-29b9-3298-90e6-920d63a277d2 | -10.57846 | -41.5021 | 2025-10-19 03:45:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 646f6fbb-7af5-3d51-83ed-2e94ec16c0a2 | -16.78718 | -42.81984 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 30b45aab-8896-3c9e-8adb-c47281c9111b | -12.14538 | -45.06773 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b393d132-e370-32a6-9889-641dc3cedc36 | -10.88073 | -47.4519 | 2025-10-19 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 230e2e80-36a5-3a05-baeb-e64b1fe50556 | -10.88924 | -46.08444 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| fc430583-c5cd-3a69-9142-d9a204e2cf98 | -16.81909 | -40.17125 | 2025-10-19 03:45:00 | NOAA-21 | JUCURUÇU | BAHIA | Brasil | 2918456 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 308fc869-7493-310a-9020-b7b5e090fc78 | -12.01466 | -46.4859 | 2025-10-19 03:45:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ddaa162d-8523-3c46-97ab-f3dd16151f28 | -12.15206 | -45.06014 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cbefbf57-682f-3ff0-919e-02848ad55059 | -16.50968 | -40.78389 | 2025-10-19 03:45:00 | NOAA-21 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4c43b962-5db9-3c3d-a306-13e1278b41d2 | -9.88777 | -47.65346 | 2025-10-19 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3351d13f-b396-33b6-8039-cc2fdcfabf02 | -10.14966 | -44.52264 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fa4a6437-86e1-39d9-82f5-b2de0e8a93d8 | -15.79034 | -43.64398 | 2025-10-19 03:45:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 781243f0-7f48-3bd6-9d56-78b495e23680 | -16.74475 | -42.79644 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e713784c-db3d-38b5-9dc1-603afb00a0e8 | -10.22895 | -44.06366 | 2025-10-19 03:45:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7270e9b9-e69b-3572-8676-93242a48f774 | -13.71511 | -40.98567 | 2025-10-19 03:45:00 | NOAA-21 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8f3412d4-8d85-3cc3-8dde-3b8443fb16ed | -15.48866 | -41.3359 | 2025-10-19 03:45:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 45f82bf7-aa38-3bea-b73f-364fe9997e27 | -12.45895 | -45.43971 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 12bd3b70-bdb9-3282-ad9f-24dbc406b388 | -16.74947 | -42.7704 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 39185e07-7fca-30d5-9509-0d1f47e92499 | -16.75957 | -42.78339 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7289d477-9764-32fd-9cd8-33e395e2816c | -15.79816 | -43.64994 | 2025-10-19 03:45:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 143f7079-2361-3514-b17d-bf09981b154b | -13.89254 | -45.50968 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fddbf954-43af-3dac-810c-71a0c03805ca | -15.69139 | -42.58927 | 2025-10-19 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4c482fc9-35b0-376c-971b-b9db881959fd | -10.8871 | -46.0957 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 52a1b544-23e2-3628-acee-7f9d79cb59f7 | -13.21477 | -43.15282 | 2025-10-19 03:45:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2372db9e-d087-3be9-aab6-59434f219fd8 | -12.15653 | -45.06417 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d063f0f2-a64a-3e3f-9865-fca3598d0498 | -13.01855 | -46.95245 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| c454f2f6-49d6-31db-9e29-a4add1c501df | -16.78614 | -41.46763 | 2025-10-19 03:45:00 | NOAA-21 | PONTO DOS VOLANTES | MINAS GERAIS | Brasil | 3152170 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 48901925-8c7c-3d10-999d-a06f530cf67b | -15.25551 | -43.58812 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d708d1d-cdb2-3635-9894-62ae948883f4 | -10.3666 | -47.47874 | 2025-10-19 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fa298874-2023-3ebc-80b6-381b5fe3c9f4 | -12.14591 | -45.06493 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2fe441d-48a4-3064-a5d9-183d5e2b5114 | -16.66962 | -42.11079 | 2025-10-19 03:45:00 | NOAA-21 | CORONEL MURTA | MINAS GERAIS | Brasil | 3119500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 2f9c5154-0c54-392d-b6b6-f7e1d22eed12 | -13.53635 | -43.00643 | 2025-10-19 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 0ba34dda-82dc-334f-bb69-bdd711471ef7 | -13.89058 | -43.45367 | 2025-10-19 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2e020d4b-3fd1-39fa-8020-6248f6917d7d | -12.18347 | -45.0879 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16846338-b40e-3b2f-af36-18488ebf01d0 | -10.77924 | -40.30975 | 2025-10-19 03:45:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| aac596bf-9aa2-364a-babf-51808b070330 | -10.87889 | -47.46107 | 2025-10-19 03:45:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 38e86301-05fe-33e0-bce5-a22d475a2b16 | -16.81389 | -41.0031 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| c2f77135-cac4-3566-82e5-376d56b6c75e | -12.98285 | -47.2846 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea7b77be-1c87-3d8c-9853-a3dfdbcd41c3 | -10.15289 | -44.52584 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 158c47a4-7a7b-366e-8aba-6e6defb979a3 | -13.91742 | -43.18455 | 2025-10-19 03:45:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| a720cbbf-188f-3f75-adde-bddd883b1b34 | -16.74881 | -42.774 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 92ca6b3b-403b-3aba-9ba6-93f709f668bd | -13.85552 | -42.44398 | 2025-10-19 03:45:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 6c642c20-9b44-3da3-a093-d11e4ab2f10f | -16.7495 | -42.79313 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac2fc8b1-0bd6-3688-9476-d8fd04d1e08d | -10.77843 | -40.31441 | 2025-10-19 03:45:00 | NOAA-21 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 59e2f8a4-d137-35e5-9d0a-79822a9010bf | -10.8703 | -43.93874 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9b0418ff-8d35-3d01-8550-4c690113641c | -10.68757 | -44.54382 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 985e6ae5-f3dd-3739-a353-ee3652423b46 | -11.68717 | -47.29807 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| eec12d26-cf7d-3a40-965e-adb9253cc9b4 | -10.68204 | -44.5458 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b56a2a35-9039-38f7-b894-1735698012ca | -12.18852 | -45.0889 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ee643b53-d0f8-370b-9984-23d671b20457 | -16.75152 | -42.78197 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 83e79002-388a-3cab-9274-2872f09e2b78 | -10.68836 | -44.53893 | 2025-10-19 03:45:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2657c6fa-ef76-3555-be9b-ff4790ff3498 | -16.78131 | -42.76202 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 860b4cbb-36ea-3606-813d-6cd90ce14fc6 | -15.52783 | -43.83192 | 2025-10-19 03:45:00 | NOAA-21 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dcf91941-7b6c-350e-aa21-61c327661157 | -11.65479 | -47.31624 | 2025-10-19 03:45:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 576a8894-26db-3280-8682-ebf7c7d1f36f | -13.88396 | -45.47348 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4bc1bb65-88c2-3109-8985-1adf9e362754 | -12.15262 | -45.05716 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19566057-0f62-38bc-97da-aa6706526ddb | -16.74618 | -42.78854 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1f65d88-2f07-3548-930f-5df180b760d2 | -16.76425 | -42.78044 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 58.4 |
| 39a657c7-275e-31ec-8ef1-8983951924d0 | -15.01144 | -40.46265 | 2025-10-19 03:45:00 | NOAA-21 | CAATIBA | BAHIA | Brasil | 2904803 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 5f25b85e-7835-3116-9083-643fda12d966 | -16.73934 | -42.80331 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 597d5ef0-28a6-3ad0-a82b-19ae32c92772 | -9.96348 | -45.27861 | 2025-10-19 03:45:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6d287963-d3df-364b-a965-fe5e9f525fd0 | -13.89139 | -43.44925 | 2025-10-19 03:45:00 | NOAA-21 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90e732df-2c0c-30c9-aee8-d8c482fd4100 | -15.01833 | -41.99182 | 2025-10-19 03:45:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 65bb87e5-e7f6-3aa8-be5c-67b80e5af8f2 | -12.4641 | -45.4407 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e4d6e333-75c7-31d2-9aae-2d920cdaf214 | -10.10172 | -44.55637 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 76ca1fd4-898f-30f5-ba62-1f2bdce5d540 | -11.62946 | -44.08046 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b8327c11-e002-3cd5-8987-67db4f800a77 | -13.89133 | -45.51587 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3bdcfe06-33b0-39a9-8ee9-22f094a7d1a7 | -12.98132 | -47.26785 | 2025-10-19 03:45:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8663114c-cbfe-3066-a9a1-9f955d1e0865 | -16.34631 | -41.75368 | 2025-10-19 03:45:00 | NOAA-21 | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 74b6934c-97e9-38dd-a165-dfbcc90dd405 | -13.62272 | -44.10775 | 2025-10-19 03:45:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad516e5f-7e6b-31be-8d8d-5d8d67524298 | -15.09566 | -40.16742 | 2025-10-19 03:45:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 2b3638f3-3e8f-3b90-a6ff-ce675094b5b5 | -10.53477 | -44.50343 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5233e798-2b82-33cb-9177-164829562062 | -13.89072 | -45.51896 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 0351cdc3-9caf-3eeb-84a0-c4cfbef3b834 | -9.89442 | -47.66 | 2025-10-19 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3bad7f7-2db3-3f17-8ef7-d62e98b80c4e | -12.47203 | -45.43643 | 2025-10-19 03:45:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80f3069e-1086-394a-a2eb-05ec3808591d | -16.7448 | -42.77326 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 868b3d61-5e3f-3e03-b075-a942aa6f8c94 | -10.36052 | -47.47762 | 2025-10-19 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| d53da0b4-7714-3bc4-9a24-e6c9d9c64ad8 | -11.6136 | -44.05906 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| fa9cbb74-128c-37fe-911a-32a518727213 | -11.39132 | -40.68761 | 2025-10-19 03:45:00 | NOAA-21 | MIGUEL CALMON | BAHIA | Brasil | 2921203 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e17db7dd-eced-3bdc-a9b9-bd05a981542b | -15.53946 | -46.44938 | 2025-10-19 03:45:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 18a870d4-c6a8-35eb-acbf-08bc8c865708 | -15.79966 | -42.50129 | 2025-10-19 03:45:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7326945d-2d09-343c-bf53-225ef1e7eef9 | -11.62746 | -44.09107 | 2025-10-19 03:45:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5376541b-0fbf-393a-84f1-6c700a3d437d | -15.98647 | -41.80239 | 2025-10-19 03:45:00 | NOAA-21 | SANTA CRUZ DE SALINAS | MINAS GERAIS | Brasil | 3157377 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 464e5aee-6621-3750-a8fd-e98eca95ce77 | -10.88782 | -46.0919 | 2025-10-19 03:45:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| fa7dae57-db4c-36ec-898e-055c1b15c03a | -11.41955 | -41.31239 | 2025-10-19 03:45:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 44a3e666-1bab-31de-88e2-e64ad7a29160 | -9.98424 | -47.0534 | 2025-10-19 03:45:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2fd01744-9fc1-3d6e-8d9f-abfc87c3514c | -16.74077 | -42.77258 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6493611-90d3-3d07-af62-963fa95446b5 | -15.23666 | -43.3404 | 2025-10-19 03:45:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 4588cad8-457e-30e7-be57-7bb9714fe9c3 | -16.07839 | -42.5642 | 2025-10-19 03:45:00 | NOAA-21 | FRUTA DE LEITE | MINAS GERAIS | Brasil | 3127073 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8510dea-fbcd-31ac-b9a5-48d0c86c8f84 | -10.36143 | -47.473 | 2025-10-19 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f85e9792-1a71-3217-8b55-ef408def5f9a | -13.86116 | -45.4612 | 2025-10-19 03:45:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a33b1af8-130b-366e-882d-553bdda0bde2 | -16.98186 | -41.16198 | 2025-10-19 03:45:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 36f994c7-2729-3b9c-bf3e-b26b4611acb4 | -15.78417 | -43.25577 | 2025-10-19 03:45:00 | NOAA-21 | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b33fb332-5a63-3699-a979-c6ac0ede538e | -16.78198 | -42.75843 | 2025-10-19 03:45:00 | NOAA-21 | CRISTÁLIA | MINAS GERAIS | Brasil | 3120300 | 31 | 33 | nan | nan | nan | Cerrado | 35.3 |
| 264cf52d-687f-37c4-aab7-42b661717f7e | -12.14701 | -45.05914 | 2025-10-19 03:45:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68c20f86-2a40-34b6-8b73-61051e670f6f | -10.13354 | -44.52515 | 2025-10-19 03:45:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 65822ced-aee3-3a8b-aaf6-01c9b7657787 | -10.87508 | -43.93971 | 2025-10-19 03:45:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4780ff63-f6e1-3627-82bb-ba9489116019 | -9.88913 | -47.65403 | 2025-10-19 03:45:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2a585954-ac91-30a4-a795-4d8104e2197a | -10.36846 | -47.46932 | 2025-10-19 03:45:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |


[Clique aqui para ver as próximas entradas](README15.md)
