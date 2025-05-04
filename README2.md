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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8243f8a7-eb01-317e-a041-3b2bdbe1048b | -5.58606 | -45.20383 | 2025-05-04 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9411041f-2942-3dc2-9d60-3c2e3e49f521 | -2.65412 | -48.79795 | 2025-05-04 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33d21dd8-1672-3a7e-af0a-be130a17fc72 | -6.71578 | -45.43637 | 2025-05-04 04:32:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 486e1445-c0e7-32cc-bf9e-753e0272abd9 | -2.79185 | -49.61938 | 2025-05-04 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f140afe-4716-3f20-88f7-a8fd448e2b61 | -3.90471 | -47.79476 | 2025-05-04 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fad0184e-9014-3f18-ab76-a727ffe5087e | -2.6547 | -48.79428 | 2025-05-04 04:32:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c5b95e9-f60c-3f3e-bbc0-8f7721d804e8 | -5.16946 | -45.10812 | 2025-05-04 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 67bae2de-1b38-3a1b-a743-acfb64ba7156 | -3.8404 | -47.8131 | 2025-05-04 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f1f3377d-8098-3bb9-81fd-1b277c6a19c7 | -5.75592 | -46.25616 | 2025-05-04 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61301660-b4c1-31ae-af53-66cd8f8fb561 | -7.82921 | -40.90143 | 2025-05-04 04:32:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| c7ef9a6b-6641-3f81-8e90-e8f7020f90b8 | -3.89549 | -47.18017 | 2025-05-04 04:32:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 609f9249-f4c7-36c4-8044-25a02961f30c | -4.25462 | -47.58156 | 2025-05-04 04:32:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5e87a3c-8ff8-3284-b528-d0eebf7fb9f8 | -5.16656 | -45.10377 | 2025-05-04 04:32:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c8ff752-3bf9-3a11-bdd3-101ff6da24a4 | -2.4147 | -48.07214 | 2025-05-04 04:32:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0398898-71b3-3bdf-8bc6-7da8903b324e | -9.20046 | -50.73129 | 2025-05-04 04:32:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bd7bec51-d83e-32ab-83fe-0885d9ab12cb | -2.38079 | -51.89627 | 2025-05-04 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f9b7e275-1419-3cd7-814d-d33a07dcc0c8 | -2.79123 | -49.62331 | 2025-05-04 04:32:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f909500e-a8d2-3e94-a2c3-bb602a400458 | -5.75256 | -46.25564 | 2025-05-04 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8abf4355-46e4-30a6-b156-73fb8c78d9c9 | -2.98218 | -49.51944 | 2025-05-04 04:32:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 138fcf1e-c293-30eb-adb3-b440376d34ea | -6.22909 | -48.05284 | 2025-05-04 04:32:00 | NOAA-21 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 516200dc-9cf0-3201-8d49-a2948ffa073d | -2.3877 | -51.9046 | 2025-05-04 04:32:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5fd25c1-0415-3592-8c27-7d4d6d10e880 | -7.82587 | -40.90456 | 2025-05-04 04:32:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 0303e8f7-ec7a-3c1a-b0fd-e2ace90d7d3a | -7.82855 | -40.90631 | 2025-05-04 04:32:00 | NOAA-21 | CURRAL NOVO DO PIAUÍ | PIAUÍ | Brasil | 2203271 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 14613e87-9089-3cb3-83e7-14bc183ee13e | -13.53925 | -52.96584 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a944bbac-ba6c-3f74-931e-31bb8ff4a52e | -10.65081 | -44.49405 | 2025-05-04 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 36e0250d-4391-3852-8889-a1242c8c0d76 | -13.53634 | -52.96085 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea3991dd-af4b-3ebc-b3fd-ce1546fea395 | -15.46228 | -42.9035 | 2025-05-04 04:34:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 512f0e9a-14e3-326d-9446-2c1904f24ddf | -13.53121 | -52.96888 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7168439-b69b-32b7-af9d-309fd14f139f | -11.39086 | -52.9435 | 2025-05-04 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f39ec4f-b522-3e63-9fa8-75f61146f0c9 | -17.4874 | -43.3208 | 2025-05-04 04:34:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 73cb90ff-3f37-32dc-a13a-350e20960b3b | -15.46168 | -42.9083 | 2025-05-04 04:34:00 | NOAA-21 | MATO VERDE | MINAS GERAIS | Brasil | 3141009 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 92977cb6-b9d0-37bc-b218-d1fdad21d175 | -13.04973 | -53.72795 | 2025-05-04 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7a04076-328c-3bb6-a7dd-4d5ccb5d2ba7 | -13.53268 | -52.96021 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 02282089-d67f-3a24-bdf1-be7ab2defa9d | -13.04929 | -53.70783 | 2025-05-04 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e76108ca-9ad0-3a7e-822d-b04dfe37daf2 | -13.70739 | -45.20311 | 2025-05-04 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4c05e91f-3af3-3648-a72e-a22b0f83483a | -13.71187 | -45.19876 | 2025-05-04 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f497e968-d619-3fd9-8c13-a4e30237234b | -13.71121 | -45.20366 | 2025-05-04 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98594b5c-40eb-3424-8327-93e77a27ca96 | -15.0783 | -48.94369 | 2025-05-04 04:34:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 78774af4-1dc5-3514-a70b-1775fdcdaea9 | -13.70805 | -45.19821 | 2025-05-04 04:34:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3a1b3c1b-285f-31c0-a80a-4318f8475041 | -13.05228 | -53.71337 | 2025-05-04 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5ecc8312-4084-34c3-a9e1-2934b7f21544 | -13.04845 | -53.71265 | 2025-05-04 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 8cd9dfd4-bdd2-31eb-ae0d-396872d655cd | -11.39384 | -52.94878 | 2025-05-04 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6f51619b-76af-3c9b-99b9-0650bd4760c4 | -15.60263 | -39.62819 | 2025-05-04 04:34:00 | NOAA-21 | PAU BRASIL | BAHIA | Brasil | 2923902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5713ea32-f64c-3c8e-a418-b1f5cc0f2644 | -13.54291 | -52.96647 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a0f10c47-61ed-3793-9871-99b22ebf7438 | -16.05645 | -47.96128 | 2025-05-04 04:34:00 | NOAA-21 | VALPARAÍSO DE GOIÁS | GOIÁS | Brasil | 5221858 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 943eca42-a219-367c-8720-84c1d8645eeb | -13.5356 | -52.96519 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b6a9fba-a6cb-37b7-85cd-68715d9ac386 | -13.05143 | -53.71823 | 2025-05-04 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bef900d8-dc46-36d5-928f-26b1d8bfe587 | -15.5712 | -47.8564 | 2025-05-04 04:34:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4faa4640-2f44-34d9-ba97-1b7e3b54d042 | -13.53194 | -52.96455 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3cf71fb4-f309-3b3b-9928-f5303e602cf3 | -11.39462 | -52.94416 | 2025-05-04 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 2521c74a-5f91-3cb3-b3ce-8ed9e6f2516c | -13.53852 | -52.97017 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b97890b-9f55-3e05-8108-1fb1c4ec4f71 | -13.53486 | -52.96953 | 2025-05-04 04:34:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f532fd3c-b56d-3735-8007-d5166f29e8d2 | -11.3976 | -52.94945 | 2025-05-04 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1c22e86f-b5ba-3cd7-9812-c9acfbd7d9c4 | -18.21765 | -43.34057 | 2025-05-04 04:36:00 | NOAA-21 | SÃO GONÇALO DO RIO PRETO | MINAS GERAIS | Brasil | 3125507 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5d7a3b1e-ad21-3217-8563-e33a1f4c7bf4 | -20.41942 | -43.5519 | 2025-05-04 04:36:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 0de53109-f982-37b1-94b6-4c20655ac94f | -21.19422 | -44.93802 | 2025-05-04 04:36:00 | NOAA-21 | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2adf2abd-3eab-3598-9fd4-7d46a4e5d3a8 | -21.10707 | -48.6529 | 2025-05-04 04:36:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| a3d7f5eb-722e-3059-aea4-ef77f508170e | -19.57203 | -49.67997 | 2025-05-04 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| eceb518e-0f2c-3f39-9a6e-edb9af6bdccb | -21.18077 | -43.98188 | 2025-05-04 04:36:00 | NOAA-21 | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| ca42877c-0406-3078-823a-27e361002efd | -19.81488 | -54.50065 | 2025-05-04 04:36:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d193b27d-f8b6-3f21-ab21-0f9b408b1428 | -18.57768 | -55.53499 | 2025-05-04 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fc774cc9-aa42-3824-ab44-348d4d39bf3f | -19.68264 | -45.37882 | 2025-05-04 04:36:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 1f96b827-e442-3d03-9217-3248ae95a36d | -21.46545 | -57.153 | 2025-05-04 04:36:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ed81043e-034a-3b55-9629-7a449d6e4fca | -19.04663 | -54.37293 | 2025-05-04 04:36:00 | NOAA-21 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 67b6ba5c-fbb6-3043-9873-d6d514143713 | -19.98478 | -47.1953 | 2025-05-04 04:36:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ca879443-505d-3f17-b28c-80ca96cfa44e | -17.62407 | -50.91657 | 2025-05-04 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9ab66a89-0689-3d4c-a361-1eaebfcf8842 | -21.34548 | -49.08735 | 2025-05-04 04:36:00 | NOAA-21 | ITAJOBI | SÃO PAULO | Brasil | 3521903 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5e0629dd-f04a-3995-a5b5-8dbe87f1d357 | -19.81567 | -54.4962 | 2025-05-04 04:36:00 | NOAA-21 | ROCHEDO | MATO GROSSO DO SUL | Brasil | 5007505 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91259684-f953-3a7f-96c6-81e8eb7b7b46 | -19.57482 | -49.68428 | 2025-05-04 04:36:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b92442e3-4f2b-300a-a925-a1932423e0c6 | -22.24777 | -52.97723 | 2025-05-04 04:36:00 | NOAA-21 | ANAURILÂNDIA | MATO GROSSO DO SUL | Brasil | 5000807 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 387391de-b135-3ee4-ba7e-9e3b2f47acb7 | -27.32226 | -51.15075 | 2025-05-04 04:38:00 | NOAA-21 | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 18e5484d-e909-35b0-96bc-5691e8c2ed48 | -29.89264 | -52.43834 | 2025-05-04 04:38:00 | NOAA-21 | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Pampa | 1.4 |
| 9159676d-33f3-3e00-93f1-4f3fbed0e5ac | -28.63733 | -56.00624 | 2025-05-04 04:38:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| ebda1ece-fc19-3c40-9585-bc3e32d6c4da | -29.86923 | -51.0925 | 2025-05-04 04:38:00 | NOAA-21 | GRAVATAÍ | RIO GRANDE DO SUL | Brasil | 4309209 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| 8a8e15f8-fdc1-3e45-a8ee-6ad02cfa35f3 | -25.17472 | -49.30686 | 2025-05-04 04:38:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 440ee1a5-74a6-38e8-9830-365d44a769e8 | -28.63385 | -56.00546 | 2025-05-04 04:38:00 | NOAA-21 | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 0.7 |
| d7de7ecc-89e6-36f4-a482-c74c25ace717 | -25.19354 | -49.32792 | 2025-05-04 04:38:00 | NOAA-21 | RIO BRANCO DO SUL | PARANÁ | Brasil | 4122206 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b11a7fd7-5988-3379-a11c-1d98530451cd | -25.04878 | -51.91668 | 2025-05-04 04:38:00 | NOAA-21 | GOIOXIM | PARANÁ | Brasil | 4108650 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 709c23da-e1c2-398c-b77a-b276c3088e0d | -27.38196 | -50.427 | 2025-05-04 04:38:00 | NOAA-21 | PONTE ALTA | SANTA CATARINA | Brasil | 4213302 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b0d680d6-791b-3ec0-9b9d-0ed10537e2d9 | -24.92387 | -52.26025 | 2025-05-04 04:38:00 | NOAA-21 | PALMITAL | PARANÁ | Brasil | 4117800 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aad3e7ed-3408-37da-b2c3-1096ea3fe891 | -31.03739 | -52.82365 | 2025-05-04 04:40:00 | NOAA-21 | CANGUÇU | RIO GRANDE DO SUL | Brasil | 4304507 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 5debb1ae-ce29-3049-848b-26925862caf5 | -30.72389 | -54.21227 | 2025-05-04 04:40:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e604276b-78d8-3b95-bad3-c8e8e4902ec1 | -9.6099 | -37.0373 | 2025-05-04 04:51:00 | AQUA_M-M | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 5df6016f-6577-3846-9554-a1dedf9895db | -5.30289 | -55.97136 | 2025-05-04 04:57:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 40c1c951-7bcd-3b02-b168-3f4b3f9de846 | -2.65387 | -48.79468 | 2025-05-04 04:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 40aafda4-d3d6-3171-b7d3-21dadce015ef | -5.17115 | -45.10715 | 2025-05-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b33e74c-11cf-3133-9467-43bfd9b09dc1 | -2.79184 | -49.61901 | 2025-05-04 04:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 60ce91f4-2a90-3b08-ad86-478f0d0b257b | -1.59465 | -67.15095 | 2025-05-04 04:57:00 | NPP-375D | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 06b2cfc0-5371-30f3-b57c-31b5825cfd48 | -5.16632 | -45.10332 | 2025-05-04 04:57:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 462420d3-b7ad-3967-bfe1-47993ecef607 | -2.98048 | -49.52032 | 2025-05-04 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bd3400d-d059-3f33-908f-eeb8ca26bf7f | -4.25294 | -47.58192 | 2025-05-04 04:57:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81cc4736-31a8-3223-9532-c77479b02688 | -2.98024 | -49.51832 | 2025-05-04 04:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9809cf-ed29-34ed-be8e-a017e35784ec | -2.65465 | -48.79337 | 2025-05-04 04:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 68457f74-d025-39fd-b5f2-88ecb8b58924 | -13.53233 | -52.96416 | 2025-05-04 04:59:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da2cedde-04fa-3e02-9599-0bb01e2a3f28 | -12.53638 | -57.73158 | 2025-05-04 04:59:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca6ec891-81fe-3009-b070-7e1a9dbeb12f | -13.37802 | -54.25529 | 2025-05-04 04:59:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8f6b1901-156e-38db-acbe-81080dcd532a | -13.0477 | -53.71397 | 2025-05-04 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a807fadf-aab7-3526-877c-74e4e0143d72 | -13.70723 | -45.20408 | 2025-05-04 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 66e6c080-35a0-3c84-85cf-898bcd5c45de | -13.05115 | -53.7145 | 2025-05-04 04:59:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dbf65789-97c9-3c5a-bdac-186c50de3d9a | -13.71097 | -45.20364 | 2025-05-04 04:59:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README3.md)
