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

## Dados Diários - Página 89

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 553ca557-2826-3ebb-a0cc-06cbe645b945 | -11.6579 | -43.5899 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 187.9 |
| 1ae0c66c-1c20-3ae8-ac0a-ece9bedd5154 | -11.2438 | -44.2626 | 2026-10-02 14:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 324.8 |
| 1caebaaf-57a7-3b3a-8eae-2de529c9ad78 | -11.487 | -43.4981 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 168.1 |
| 958feb09-ed79-3e84-ab5d-144ef180279b | -15.303 | -42.7544 | 2026-10-02 14:30:00 | GOES-19 | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 108.7 |
| c71764be-c8de-3c24-8690-5c7eda2c9023 | -11.2749 | -43.5776 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 94.6 |
| e749ceb6-b845-3593-9cb3-83e1cfbb8b36 | -6.1976 | -52.809 | 2026-10-02 14:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| ef4d7ff5-a1d4-3825-80ae-eb9694df7edf | -11.6771 | -43.587 | 2026-10-02 14:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 226.4 |
| a1dbeb15-0286-377e-b1bd-f503adf3883b | -11.6964 | -43.584 | 2026-10-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 230.7 |
| fb9a6e9e-181c-3f23-a83f-4118b8fe845f | -11.2438 | -44.2626 | 2026-10-02 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.0 |
| adcb398b-1b42-3b31-9afd-62abd2192513 | -6.2129 | -53.2575 | 2026-10-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 111.1 |
| c8a33934-fe63-3974-9ada-886b2519380a | -11.716 | -43.5573 | 2026-10-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 177.4 |
| 2f563a14-fed6-31b3-acd9-b0a28190568e | -11.2246 | -44.2654 | 2026-10-02 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 131.8 |
| 1784f5d6-ec09-3977-9fce-919410e33f8a | -6.6129 | -43.7317 | 2026-10-02 14:40:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 6f0537f1-e024-3e97-bd96-252b0588069a | 0.6324 | -54.4037 | 2026-10-02 14:40:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c98b11c6-7ebc-3105-b135-a1e9215e27c2 | -0.5073 | -49.1326 | 2026-10-02 14:40:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 94.9 |
| 7266bc66-934b-367c-b2b8-f18492f19eaa | -11.3931 | -43.3942 | 2026-10-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 380.3 |
| 0c0dc0ab-ca19-3843-84e4-8df2710737ed | -11.6771 | -43.587 | 2026-10-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 201.0 |
| 118bfebf-6425-33c8-8af5-52e087832486 | -11.3935 | -43.3705 | 2026-10-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 130.2 |
| 46a32859-a46d-3022-bb43-de0b70ec16c3 | -11.2629 | -44.2598 | 2026-10-02 14:40:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1017.1 |
| a311e2aa-d335-3fa9-8042-056bfd371c0b | -12.5135 | -43.0943 | 2026-10-02 14:40:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 168.1 |
| a9b3b610-404e-3d34-8ebb-7b06eaa083c1 | -7.1825 | -52.6283 | 2026-10-02 14:40:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| 2a8efac5-d022-314d-a828-da3a0906d142 | -10.1435 | -45.1289 | 2026-10-02 14:40:00 | GOES-19 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 64.9 |
| cc631731-56dd-305e-ac7a-82f291de272a | -11.6395 | -43.5455 | 2026-10-02 14:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| fa39c977-91e5-3af9-ba7c-fb6a609e6b45 | -1.4487 | -48.9313 | 2026-10-02 14:40:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.0 |
| 81ac123c-e072-3c7f-9a6a-9ecfb8d6708c | -11.6583 | -43.5662 | 2026-10-02 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 163.5 |
| f8e997ce-54da-3543-8297-eaabd18e4cf0 | -11.2749 | -43.5776 | 2026-10-02 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 100.6 |
| 62123a8f-49b5-333c-a342-3b2b0ff5ad19 | -6.3952 | -56.4158 | 2026-10-02 14:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 159.1 |
| 356130b4-5c30-3d71-ac77-0d9ba2a979af | -6.2129 | -53.2575 | 2026-10-02 14:50:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 125.6 |
| f260e9a2-fcae-3469-ad9e-282595880a48 | -11.6968 | -43.5603 | 2026-10-02 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 3b6ccc82-4b39-3d5a-9c20-456ac1f2546d | -8.0162 | -42.8917 | 2026-10-02 14:50:00 | GOES-19 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 43.8 |
| 5a9e6f92-b4dc-3721-85dc-db0c43ea939b | -5.8597 | -53.479 | 2026-10-02 14:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.1 |
| c40df2f9-721d-332a-88e0-a08da3ed565b | -11.3935 | -43.3705 | 2026-10-02 14:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 114.8 |
| a5dc64a1-a0a1-3edc-bb31-0582c4bc706c | -12.5135 | -43.0943 | 2026-10-02 14:50:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 139.6 |
| 7e3652ef-27a8-3431-a5e7-e2c8523dee3a | 0.6324 | -54.4037 | 2026-10-02 14:50:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 99.1 |
| f1edb660-b5f0-3784-80d9-8ae47f7e416c | -14.2531 | -41.6256 | 2026-10-02 15:00:00 | GOES-19 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 143.3 |
| 004706d5-3c6f-36f3-aa97-0eafc8604ed9 | -1.2271 | -49.0197 | 2026-10-02 15:00:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 23baaa41-0538-3bab-85e4-b18275412ad4 | -6.2129 | -53.2575 | 2026-10-02 15:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 117.0 |
| 90d3f837-e7ea-326a-9e2b-ad1d3db37a87 | -0.4889 | -49.1327 | 2026-10-02 15:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 85.1 |
| 8d890b27-8843-3e78-99e1-c48dd852b482 | 1.2612 | -50.7053 | 2026-10-02 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 405b41d3-82ae-328b-9955-1405dc238f75 | 0.6324 | -54.4037 | 2026-10-02 15:00:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 33c33463-f059-3ab3-bf7f-f1c997ef1354 | -5.9148 | -53.5372 | 2026-10-02 15:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 3792a400-c20b-3636-aa6a-5b690a649c56 | 1.1323 | -50.7277 | 2026-10-02 15:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 95b06550-e127-3512-87a9-fb01cb08a4ca | -9.83351 | -36.13146 | 2026-10-02 15:09:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 42a7cfc9-88bf-3420-9c2a-347a331b75dd | -9.83387 | -36.13907 | 2026-10-02 15:09:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| 2a736de0-5167-32f9-9f15-45f67fb88e59 | -8.36873 | -36.95621 | 2026-10-02 15:09:00 | NOAA-20 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 2d38ec5b-4cb5-33d9-a2a9-1b77e5bf67df | -9.82736 | -36.1385 | 2026-10-02 15:09:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 8.3 |
| 9c02e09b-a715-3068-b8d8-07bb4a298b54 | -8.37191 | -36.962 | 2026-10-02 15:09:00 | NOAA-20 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 14.9 |
| e897e03f-199d-3a59-8643-1c03b28c2621 | -8.371 | -36.95482 | 2026-10-02 15:09:00 | NOAA-20 | ARCOVERDE | PERNAMBUCO | Brasil | 2601201 | 26 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 6a3f1ac4-8abd-3001-b8bc-bf4b4b87131f | -8.72849 | -36.91109 | 2026-10-02 15:09:00 | NOAA-20 | PEDRA | PERNAMBUCO | Brasil | 2610806 | 26 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 832a9d02-dde0-3f25-9132-0cb411a8b189 | -5.14893 | -37.39047 | 2026-10-02 15:09:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 30.7 |
| 63a52198-ba53-3479-a9d7-69daf12b4ce7 | -5.14802 | -37.38402 | 2026-10-02 15:09:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 31.0 |
| af065bd5-5f90-3797-8db1-1585f36c6e77 | -5.1467 | -37.38342 | 2026-10-02 15:09:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 8407358f-9838-3290-98e8-a329a7448250 | -9.83423 | -36.13773 | 2026-10-02 15:09:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| 312cebbc-6234-3248-b658-95d4f314b1bd | -9.83311 | -36.1328 | 2026-10-02 15:09:00 | NOAA-20 | SÃO MIGUEL DOS CAMPOS | ALAGOAS | Brasil | 2708600 | 27 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| d5dfc433-e5b9-39fa-b5c1-c24e2b72a9f9 | -5.14756 | -37.38987 | 2026-10-02 15:09:00 | NOAA-20 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 20.9 |
| 628bd372-d346-3009-a22b-7668022fb4fe | 0.6324 | -54.4037 | 2026-10-02 15:10:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 95.9 |
| 80957506-c26d-3d74-a6e8-3ccecbcd6e16 | -1.6396 | -55.1319 | 2026-10-02 15:10:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 100.5 |
| e7aebdb5-c6aa-3bfd-9625-f9f0d90311f8 | -1.2271 | -49.0197 | 2026-10-02 15:10:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 121.7 |
| 091a82b7-78c6-371f-9d2a-8ea446491a2c | -1.2556 | -54.5589 | 2026-10-02 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 631.8 |
| 51cfa4bd-eb37-38e4-91c1-922333f52016 | 1.3901 | -50.7245 | 2026-10-02 15:10:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 4ff3aa71-5ef8-3299-8dc4-e4f6a98059a3 | -2.0264 | -54.2888 | 2026-10-02 15:10:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 92.4 |
| 8aca24ce-6586-39e2-a5bf-3bca7e3652ad | -1.135 | -48.8715 | 2026-10-02 15:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| b768a0e7-bcb2-37d0-834b-ec58c6087fb5 | -1.1351 | -48.8501 | 2026-10-02 15:10:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 875cb441-c8da-3a93-966a-d16f3371b53c | -6.2129 | -53.2575 | 2026-10-02 15:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 138.2 |
| 7f9082cd-6e61-374a-b9bf-e23f98f0a5f0 | -11.47 | -43.4 | 2026-10-02 15:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6932cbc6-7155-3e09-86ca-a9ab8592a7f9 | -1.26 | -54.61 | 2026-10-02 15:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e866878-0917-3266-81ca-5d1bb24caaf2 | -11.32 | -44.28 | 2026-10-02 15:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 954b802b-47e8-3ed1-a9fa-1f94a93347a7 | -12.76 | -45.13 | 2026-10-02 15:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 23ad98a0-374e-3bfc-84b0-2106e0a54dfd | -13.35 | -43.85 | 2026-10-02 15:15:00 | MSG-03 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| db835a56-eadf-35f7-b9df-3321962698de | -13.38 | -43.86 | 2026-10-02 15:15:00 | MSG-03 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 10968378-f7b0-3c7e-9a94-48d8d693cea6 | -1.26 | -54.55 | 2026-10-02 15:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a3df722-6b45-32ae-94a9-6d523eff216c | -12.77 | -45.18 | 2026-10-02 15:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ecd7ed4d-85c5-38ea-b8c8-77fffc31537c | -11.15 | -44.61 | 2026-10-02 15:15:00 | MSG-03 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e52ee49e-c723-3f02-933e-18e05813ccec | -1.29 | -54.55 | 2026-10-02 15:15:00 | MSG-03 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e37ccb8a-4742-322f-ab85-19abb128f219 | -11.8 | -43.57 | 2026-10-02 15:15:00 | MSG-03 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f141b8f7-c6f3-3734-885b-73cd8103a1df | -13.35 | -43.9 | 2026-10-02 15:15:00 | MSG-03 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ad9b8624-9453-3d92-9746-f7f05c444f0d | -12.79 | -45.14 | 2026-10-02 15:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 89b9e210-f044-30c2-89bc-3b5718e92cda | -11.29 | -44.27 | 2026-10-02 15:15:00 | MSG-03 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9feb5042-7253-3b7e-8e19-2dd469748c6e | -15.77 | -43.63 | 2026-10-02 15:15:00 | MSG-03 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a57fc785-cb67-3581-b059-d91b0533034d | -12.8 | -45.19 | 2026-10-02 15:15:00 | MSG-03 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 71416d69-25d3-39d7-911f-6f16a2aa8d5a | -1.6213 | -55.152 | 2026-10-02 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 85.2 |
| beb53de8-bd87-3134-81fc-4d62527e371c | -1.6578 | -55.211 | 2026-10-02 15:20:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 2475a380-d44e-3318-8af0-b70f4554c236 | -1.1716 | -49.1055 | 2026-10-02 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| bc142ed4-2183-3ea4-98d7-40932b1f69ae | -1.2082 | -49.2752 | 2026-10-02 15:20:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 62.7 |
| edb37b78-8c3c-3448-9012-6188c6a2b66d | 2.5502 | -50.9734 | 2026-10-02 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 88.2 |
| be1bf9dc-aa73-3508-8825-77cfc520ccca | 0.6324 | -54.4037 | 2026-10-02 15:20:00 | GOES-19 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| af428325-4401-3ab0-ae51-3efa5a2c8096 | -1.6213 | -55.1321 | 2026-10-02 15:20:00 | GOES-19 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 89.4 |
| a0ba06f9-b825-3602-877c-2915d1bbb03c | -2.0264 | -54.2888 | 2026-10-02 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 92194fba-eb6d-3d38-8733-5672e294acdb | -1.2556 | -54.5589 | 2026-10-02 15:20:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 632.2 |
| cca32d67-a9d3-3772-9e58-57809c252f7e | -1.1715 | -49.1268 | 2026-10-02 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 1eb47358-56f3-30f6-b8b8-c617a772759f | -1.1351 | -48.8501 | 2026-10-02 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| d88090ca-9132-328f-bd33-addcbce7d6bc | -1.4672 | -48.9097 | 2026-10-02 15:20:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 1667a43e-621c-3db4-9d7a-7b878df5d5c2 | 2.5502 | -50.9526 | 2026-10-02 15:20:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 137.6 |
| 4f398e05-fe95-3819-9a7d-3cbafa2febf8 | 1.3901 | -50.7245 | 2026-10-02 15:20:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 20c3d4be-4d9e-3004-8e3e-2c8d75143097 | -0.5073 | -49.1539 | 2026-10-02 15:20:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 9a78de17-c61c-346e-8afc-f1c2ac662ca2 | -9.5004 | -66.7831 | 2026-10-02 15:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.2 |
| d9fd57c0-b324-3cee-b502-68b717cbd725 | -1.4303 | -48.9102 | 2026-10-02 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 575c03ee-a216-3b7a-b0d6-f3219c68be9e | -1.2085 | -49.0838 | 2026-10-02 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| d1d5f330-92cc-3912-a384-61496fb019fc | -1.2556 | -54.5589 | 2026-10-02 15:30:00 | GOES-19 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 723.3 |
| 02619202-ede5-35d0-bc7f-6c645c4f75b4 | -1.2085 | -49.1051 | 2026-10-02 15:30:00 | GOES-19 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 69.9 |


[Clique aqui para ver as próximas entradas](README90.md)
