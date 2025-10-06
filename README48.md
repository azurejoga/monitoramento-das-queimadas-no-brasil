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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 61cdc02c-0b65-3bbe-80f9-3bcc90ec506a | -16.05396 | -50.99807 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 81dddf43-41dd-3a44-9321-a74bff610887 | -15.23321 | -49.28211 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 37988206-e59d-35aa-a78c-18805f935bde | -10.31149 | -50.26346 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b3b6ff9c-c706-3cbe-b362-492347ea0516 | -16.03077 | -51.05152 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93d33633-40bd-353a-8cb3-c3001666d14b | -14.71503 | -48.38553 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5f478145-1e6e-3580-9fd3-6b938f526742 | -9.91358 | -49.94851 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 187f89be-ee02-3edb-afcb-0be8088ae494 | -16.29108 | -45.24572 | 2025-10-06 04:27:00 | NOAA-21 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 18d1f3c9-11d8-3c0d-8f0d-c84ee374e704 | -13.63235 | -48.71138 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 53107dd1-43f8-3ef8-aea8-fc6fa04d064c | -12.9912 | -51.05159 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8c442a40-0674-3e8a-9ebc-fdae976bf141 | -13.12818 | -48.00391 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4dcb3969-b7a5-32da-894f-ae6399e19385 | -14.63729 | -52.53617 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f59aa6ea-dadb-3565-8e4e-c2dc692d2057 | -13.49484 | -47.24263 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e168f7c7-75ac-3fb9-8ed1-49efd0e53112 | -15.16817 | -45.76426 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88d5e732-0c19-34b7-ae6e-56a5eacae796 | -14.91284 | -46.85644 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 40340f4c-a2e0-30f4-b75c-e90c644ecac1 | -15.3509 | -46.05066 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7f69bbf2-e876-3d33-88d2-036831752dcc | -15.2454 | -53.78159 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06b6b778-85be-33b7-afa8-6bc822eb9c52 | -13.269 | -47.84285 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ab026a15-b4b5-33a9-97e4-7f80cbba6517 | -11.49318 | -45.03917 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 99e98abb-fbe9-3ccf-9bbd-9ac78ea80a72 | -13.49232 | -47.28201 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10e3af1e-5bf1-3f71-86a0-47ca435cce61 | -11.02538 | -46.54132 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b8d46199-c2d8-36e2-b639-3acd29649fcd | -13.63075 | -48.70012 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e7b16e83-1708-3411-a8c7-16ce1969548b | -14.55395 | -46.64975 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 12b68ee6-a430-3028-9dd1-8c0cb144d107 | -14.68933 | -48.31226 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 76742f75-5345-3df0-a633-cd147ec08f6d | -13.28375 | -47.57455 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f951e890-e678-3aa3-87cf-ffdd29cb353a | -13.27065 | -47.83228 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a0d33e0-a9dc-3ea7-8b4f-0a2d4e5d8ba4 | -9.67403 | -48.40467 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 996937a7-a124-32df-afbf-466513fe49c4 | -10.3663 | -51.20454 | 2025-10-06 04:27:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b329af92-b29f-3d89-b0bf-8396630a55a1 | -15.94487 | -48.61622 | 2025-10-06 04:27:00 | NOAA-21 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 678758a2-0583-3085-9d45-e4be50d02e1c | -11.01759 | -46.5256 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bb3ffd0a-3804-37c2-8819-852c1ca402d0 | -12.48908 | -45.55267 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d6b0e8a0-9f3e-383f-b82e-a23ec58eadfc | -14.54778 | -46.95636 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| bf6dc785-d9a2-389c-9a17-296ff5179ffc | -14.56406 | -46.65135 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3ce0692-21aa-346f-81bc-72fbabee7673 | -13.10902 | -47.80247 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8344e50b-5107-3c2b-9a9d-4abea238abca | -16.06233 | -50.92608 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6e8fe66-3d12-368a-8224-e0dab360f1c5 | -11.86895 | -56.89092 | 2025-10-06 04:27:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a76bc3bb-daf2-3552-ba7f-915ae601a2cf | -13.32339 | -48.06144 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 230df59c-a12c-35d7-a310-05435ee5348d | -8.61218 | -54.96315 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 696b0b34-692e-3d50-b7ac-c7e440d7b0c4 | -13.26735 | -47.83175 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2390c514-d07c-37da-928e-3b3881489b05 | -9.79001 | -48.27572 | 2025-10-06 04:27:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d3a00ed4-a3cb-3454-ab41-7e655941c095 | -16.3473 | -47.05782 | 2025-10-06 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f57eb0ab-c795-3412-b208-868c89c4a8c8 | -10.82577 | -49.3908 | 2025-10-06 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b1d8d91f-0e94-39dd-a883-bdf073eaf12a | -11.07604 | -47.93815 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2f86a6c8-16c5-3993-a27a-731a5c664eae | -13.50107 | -47.24715 | 2025-10-06 04:27:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 994c7b79-2fff-32f5-b62d-82a0db06be98 | -12.25878 | -49.2056 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a15a9d1c-a1cb-3729-9772-fa629e6331ce | -12.55307 | -48.15476 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d5bce78-ee3c-3134-8ee3-7c5b22746049 | -8.62305 | -54.95937 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 905f2936-61ae-3e17-a1ca-f7e92c292125 | -11.14723 | -47.1615 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f143cc5e-c811-328b-ae81-00a7ab3979fb | -10.93753 | -47.08818 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 174d532f-4f39-36b6-a677-cfa879cf3851 | -11.93945 | -46.45538 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ba9f97aa-e360-349b-9ae6-0879bfc462d9 | -12.38389 | -51.08057 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9494173b-ac33-3c23-b857-638d98fb6cdb | -10.81156 | -48.82773 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 441f6336-c135-339e-ab75-fc4f228e6a2b | -15.2293 | -49.28523 | 2025-10-06 04:27:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 900ffbd0-c0d8-326c-8367-0121af499384 | -10.82888 | -47.99462 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fbbd048-e1c6-3b7e-a4af-01b9349756c2 | -15.88339 | -46.26521 | 2025-10-06 04:27:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 46e0f64a-398f-330e-9121-8823ec2b77c7 | -14.60614 | -52.4903 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| d1273502-1373-38bf-a086-9301e895056f | -9.32847 | -54.51963 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1d2de807-df3d-360f-bac6-58e9148d7e79 | -13.06649 | -47.89652 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e349472a-0417-3cb9-845e-4fe6f37327eb | -14.72311 | -48.09634 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 03ffda91-c49a-3b1c-9533-5f180748a954 | -13.11058 | -48.00826 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7f56cfef-d4f5-39a4-a391-abfc3bb8e0bf | -14.55565 | -46.66139 | 2025-10-06 04:27:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b2845475-d6e2-3138-a7c2-9525d1033943 | -12.37437 | -46.50111 | 2025-10-06 04:27:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8e5838f0-286f-35c0-8cc4-f8dccc42b1df | -14.93492 | -47.13655 | 2025-10-06 04:27:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 745d0d18-27be-3c42-b618-ae334e5ee2cb | -11.00743 | -50.68424 | 2025-10-06 04:27:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f041de6c-607a-3053-a6df-5af8f6131bb2 | -16.01063 | -50.93701 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75231480-68ae-38c6-add8-614cde8092e8 | -9.26676 | -51.80548 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22a00f02-7d0b-3524-817f-a99c65ef2df2 | -9.62385 | -48.20902 | 2025-10-06 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 93583c22-d3dd-3039-b73e-cdd85ed39bc8 | -13.68526 | -47.35309 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 99a05944-8963-3e28-8706-1ed284e6ba6d | -13.2953 | -48.08938 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| faf27271-f21f-3330-8597-c138736478d6 | -13.25324 | -48.46259 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5692155c-b416-3f69-b5a7-cd020f93a7e8 | -12.41512 | -51.1171 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0fd87d12-3bd4-3973-a4f4-9169c8b1fe01 | -12.69856 | -45.84045 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6bb8e2ed-d014-356f-b0b0-7f2cc42122e7 | -12.93088 | -54.71938 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06ab14bc-95e0-35e9-85bb-ced644e6f726 | -11.81103 | -45.11727 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd2eb547-cc20-3da7-aa63-b0d04e75a3b7 | -15.3512 | -47.99568 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1fb75916-cf17-3a69-b322-c1d46bbde96e | -12.91061 | -46.81703 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 66fa738e-b6e9-35e0-83d7-5fc5e7eda1c8 | -13.08428 | -47.87415 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7a4d7bd1-84b4-3580-a1a7-8e0790cfb2e7 | -11.67485 | -44.26231 | 2025-10-06 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| b1de8755-6ec4-3799-bb59-95a1fa8cfc07 | -13.29592 | -47.77874 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af8e62d9-02e1-33bc-86b6-46b064346ccd | -9.27466 | -51.80693 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 95800cfc-3d79-3b82-b241-62f621f0db23 | -13.26422 | -47.19483 | 2025-10-06 04:27:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84d07453-fc30-3535-986a-ae000515ef1a | -10.41703 | -48.10114 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| fcdceb04-7eba-33d6-bc8a-0339679e95b5 | -13.60091 | -48.69527 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 83160b41-da19-3afc-acb6-bdbf55b2efc1 | -11.65861 | -47.02076 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e727c1a7-0f2b-3073-a6e4-100d03f734b1 | -13.35639 | -48.04515 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e6fdf1f-8862-3943-bd81-7e51e78e69d7 | -14.48446 | -47.55161 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5cd5df47-8faa-34d2-8e97-b3fb1bb68f21 | -12.92103 | -54.72227 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2a9e6708-1fac-3c03-8ab3-fa45ac6b816a | -10.47723 | -50.44309 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 12d6e1cd-cd99-3a5d-b309-4ca3d3c2abb8 | -14.69032 | -48.37055 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a6c39397-f384-3e3b-9f9a-a92c93910743 | -15.57162 | -52.44994 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 65ab1dc5-8b16-3faa-8278-254ae1323c33 | -15.60146 | -52.54974 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1c6cb2a9-d3ff-3bb5-98fd-b643db94e401 | -12.44896 | -54.40468 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 416e288f-84a7-35ca-aa2a-c025b8280a40 | -11.14983 | -47.94635 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cb609ad4-7b34-3ab4-9c63-c04dcf3acd6e | -11.48911 | -45.04266 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d424559-87ae-3c1c-aa6a-06647b8d032b | -14.61795 | -52.51216 | 2025-10-06 04:27:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d704b67f-00c3-3621-b984-1a72ec76b877 | -13.28599 | -47.62545 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3a639d00-c5e9-3af1-baea-1cccd4b8e9ca | -11.70683 | -45.41716 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58c9b3eb-c9d8-3b4c-9e4e-fc2881ce4a82 | -11.20009 | -47.82138 | 2025-10-06 04:27:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cc505068-0718-31f9-aa98-1c9cab51e844 | -13.85849 | -43.99125 | 2025-10-06 04:27:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a6724921-8114-391e-a5c6-1969342b2467 | -14.64036 | -48.32236 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8153e633-a6ea-3aa3-a23d-48cb377d8bcb | -10.3582 | -48.1498 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README49.md)
