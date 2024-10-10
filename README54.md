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

## Dados Diários - Página 54

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed4ebff1-5b79-3b75-b0d4-db2598bd7a4f | -14.57779 | -48.72466 | 2024-10-10 03:57:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c94bca54-d115-30f2-b244-7cc2f184d8fa | -14.21034 | -49.74403 | 2024-10-10 03:57:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 6ec0ffa9-dcad-3c35-b993-0ce8b87837cc | -14.20963 | -49.74755 | 2024-10-10 03:57:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2180582e-189f-393e-bec5-cbde76c48aff | -14.20892 | -49.7511 | 2024-10-10 03:57:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 81fc8868-7311-360c-ab61-7e1effbe80eb | -14.2036 | -49.74987 | 2024-10-10 03:57:00 | NOAA-21 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37513c60-5a12-3cd5-893a-1ba01500e621 | -12.19413 | -50.60596 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2fefe771-a2cf-3180-823b-7d69be36e8f2 | -12.19327 | -50.61027 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c8fc4e4-d886-3083-a21e-2fc56d8e0136 | -12.18828 | -50.60477 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5935ddd-6767-3c55-9fab-9c6725581c65 | -12.16576 | -49.68476 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ea9fc4d0-c939-33ef-b1e9-3616c32f111a | -12.16503 | -49.6885 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ad37a9a7-8f14-3e6e-ac7a-a879404dd197 | -12.07408 | -50.81893 | 2024-10-10 03:57:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7274ed09-2c4d-3b0c-9411-177e35e09678 | -12.07318 | -50.82343 | 2024-10-10 03:57:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9a32cd3-7932-33ee-a636-41bc0e441962 | -11.55683 | -49.9079 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 26073d82-23ea-381d-b7e5-269c764c550a | -11.55604 | -49.91187 | 2024-10-10 03:57:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e1453de-d0ae-3b47-80c5-10e7bf72f2a3 | -11.20443 | -49.92852 | 2024-10-10 03:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24ce6273-08ed-3956-b02a-c5004ed2fff5 | -11.20363 | -49.93258 | 2024-10-10 03:57:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9caee483-885a-3a11-967c-d04ede960d72 | -12.94021 | -51.13655 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e85190b1-e37d-3142-a802-5fa82856f8cb | -14.82063 | -50.80361 | 2024-10-10 03:57:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3b9c380c-4685-3509-b581-88f354cec1b0 | -14.81729 | -50.80227 | 2024-10-10 03:57:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 2b37ac75-6c21-3141-b2dc-c88e712ecc0d | -14.81644 | -50.80634 | 2024-10-10 03:57:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 488f9ac4-f53f-3977-bfb0-f65a02567e96 | -11.29834 | -51.04587 | 2024-10-10 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 3c4bf63a-61a2-30c3-a0eb-edf3e3e0e948 | -11.29804 | -51.04811 | 2024-10-10 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 60b85b20-3b3a-3686-a960-835ce5d4a474 | -11.29738 | -51.05059 | 2024-10-10 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 03c912e4-ab80-31d6-92f8-19ec577a2467 | -11.29712 | -51.05283 | 2024-10-10 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 4fe15ddd-d5e5-3123-b6f7-e1fe3bede5be | -11.24643 | -51.3435 | 2024-10-10 03:57:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a5adde6a-2408-3552-9771-8d5b6236f235 | -13.18531 | -51.70795 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ce7a6364-bd77-3862-93ce-a8fa375ca3f4 | -13.1843 | -51.71289 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d0571109-dd74-3a0f-afc2-24bf838fe769 | -13.17705 | -51.68581 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bede4a4-6575-3f80-a24a-b5087284f42b | -13.17003 | -51.68879 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b84c9d8-99df-3e15-b7d9-a01fd60f2fd2 | -13.16898 | -51.69385 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8344fa8d-fb81-3a3e-85b5-bb2a549fb42f | -13.12515 | -51.66195 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cdb7b10a-7e97-3cf8-9e44-4db5796ef7a3 | -13.12488 | -51.65946 | 2024-10-10 03:57:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 06ff3b16-ff5f-35c4-a700-b36c45593a6e | -22.25386 | -42.72898 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60461b02-59f8-3287-8203-ac1d0e9a8f5a | -22.25115 | -42.72463 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| e1aa5c81-fda9-39a9-ad0c-d5fcc7a03a7e | -22.25055 | -42.72838 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 186e0b43-a955-3950-a7df-f409be4a7254 | -22.24994 | -42.73213 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 97da844a-f575-368c-9efb-d5c61abd1705 | -22.24784 | -42.72404 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 93cdec2c-fe85-3f8c-beae-0f6ca7b76063 | -22.24723 | -42.72778 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| ba058b7b-0272-3c9b-9aa7-32d8e44237e3 | -22.24663 | -42.73153 | 2024-10-10 04:00:00 | NOAA-21 | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 8f05909a-bee6-39ac-ab9b-edacb5a70553 | -20.54222 | -45.14011 | 2024-10-10 04:00:00 | NOAA-21 | ITAPECERICA | MINAS GERAIS | Brasil | 3133501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| ca1b5ddb-091d-3eaf-98f3-9c8f4ffa472c | -20.41697 | -43.95886 | 2024-10-10 04:00:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 399ad563-3708-397f-b777-4c0a59659f25 | -20.41352 | -43.95823 | 2024-10-10 04:00:00 | NOAA-21 | BELO VALE | MINAS GERAIS | Brasil | 3106408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a6d63c58-9739-3736-b23b-f04b7ee3920e | -20.22986 | -44.43151 | 2024-10-10 04:00:00 | NOAA-21 | ITATIAIUÇU | MINAS GERAIS | Brasil | 3133709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| edaa58e6-26b6-3b39-afe8-9591e1f8c643 | -21.07066 | -45.13594 | 2024-10-10 04:00:00 | NOAA-21 | PERDÕES | MINAS GERAIS | Brasil | 3149903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 56454718-ad69-3398-83e2-672e7497087b | -20.76324 | -45.94909 | 2024-10-10 04:00:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 80c57829-b3c4-3a62-afde-19714ea17eb5 | -20.75948 | -45.94835 | 2024-10-10 04:00:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7486054d-ead5-3933-8713-c1e90b5baf0c | -20.75283 | -45.94208 | 2024-10-10 04:00:00 | NOAA-21 | GUAPÉ | MINAS GERAIS | Brasil | 3128105 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 22beb513-66a7-34f3-83be-219fa2f82089 | -2.67 | -53.35 | 2024-10-10 04:05:12 | MSG-03 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b54a565-ce54-3344-94d0-0017d91f618b | -2.6533 | -53.3506 | 2024-10-10 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 121.1 |
| 8b7a6db3-ee55-31a6-a6ae-0d1cf89c26b5 | -2.6716 | -53.3704 | 2024-10-10 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 69.2 |
| 4c4da3ec-207d-3e03-83e0-f89e9e2858d4 | -2.6716 | -53.3502 | 2024-10-10 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 260.0 |
| 785223e0-9b1c-30d6-8f2c-f02ca2925294 | -2.6717 | -53.3299 | 2024-10-10 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 90.5 |
| e0d64f4e-f828-36cc-8182-40db7811bcd4 | -2.69 | -53.3497 | 2024-10-10 04:05:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 78.8 |
| 5b8c6380-cd25-3d72-bd1a-a601d837d12e | -4.0961 | -48.2739 | 2024-10-10 04:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 140.3 |
| 4a2344b9-d0f4-3412-b534-e8db08d6fc72 | -4.0962 | -48.2523 | 2024-10-10 04:05:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 100.8 |
| e9d54a55-43fd-3f6a-a9ed-064ff63049f4 | -4.1146 | -48.2731 | 2024-10-10 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 161.1 |
| 849db3c6-6c4e-3fb2-a501-cc4bd42c7b3a | -4.1148 | -48.2515 | 2024-10-10 04:05:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 78.9 |
| 102dad73-18e7-3c38-a4e7-d69f52bd1783 | -6.747 | -59.3259 | 2024-10-10 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 896eef91-3923-3e4a-9f7b-5098eadad9e5 | -6.7654 | -59.3252 | 2024-10-10 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.4 |
| 30913824-8068-32d5-9847-9b0e07b32f9d | -6.7655 | -59.3059 | 2024-10-10 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 6131e02b-d409-3955-825c-3fb85ece5ecd | -6.7839 | -59.3245 | 2024-10-10 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| 517f93a1-6365-3123-86ee-ecaae5b542df | -6.784 | -59.3052 | 2024-10-10 04:05:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 0d3f60dc-f44f-3b24-a9f2-d496d577efa3 | -8.1475 | -42.9717 | 2024-10-10 04:05:52 | GOES-16 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.8 |
| c7959cb7-b415-377e-a95a-ad5636eee0fb | -9.0656 | -61.3934 | 2024-10-10 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 4e0d914f-b470-3b77-82e0-f010193a76e0 | -9.0841 | -61.4117 | 2024-10-10 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 74b7ce94-b988-3a5c-bb85-85e2c53ae577 | -9.0842 | -61.3925 | 2024-10-10 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| daa631b5-3ca4-36f1-b2b4-d74d52992d8e | -9.1035 | -61.2769 | 2024-10-10 04:05:58 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 64.3 |
| 7e7b4439-66e3-348f-854d-a421b11d9332 | -9.122 | -61.2951 | 2024-10-10 04:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.6 |
| df2080bc-543a-3421-902a-be5fa0dd2bb5 | -9.1221 | -61.276 | 2024-10-10 04:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 166.2 |
| ece0463d-ed9f-3f3e-af9c-59eef0b77179 | -9.1223 | -61.2569 | 2024-10-10 04:05:59 | GOES-16 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 045bf723-f2ed-3568-99cb-1be0c25c104c | -9.8551 | -60.3159 | 2024-10-10 04:06:03 | GOES-16 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 5ebd823f-4ad3-3533-b422-04670a5f996c | -10.3632 | -55.8554 | 2024-10-10 04:06:05 | GOES-16 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 50.4 |
| f29acc31-f7e7-38b8-a99b-3c4a88ea0d33 | -10.4287 | -60.9979 | 2024-10-10 04:06:06 | GOES-16 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 544d9635-bbcb-3d15-bcd4-6d162fc698c5 | -11.0254 | -57.2237 | 2024-10-10 04:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 97.6 |
| 34622ce8-3779-3c0e-9a17-0dd81e28f7bf | -11.0256 | -57.2038 | 2024-10-10 04:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 2e812e3a-9161-3fd5-9bf4-f6b255cec526 | -11.0443 | -57.2222 | 2024-10-10 04:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 23ec6d97-430e-381f-9704-a0131667fc33 | -11.0445 | -57.2023 | 2024-10-10 04:06:09 | GOES-16 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 74.7 |
| dbd9b0fd-424d-3af9-b637-a016cf992e6f | -11.281 | -64.9018 | 2024-10-10 04:06:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 56.0 |
| d42289c4-cf91-34cc-bd51-af160cf9c2b8 | -12.2893 | -43.7258 | 2024-10-10 04:06:15 | GOES-16 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 321fad89-5e34-3983-adbe-122233856a10 | -12.9447 | -51.1337 | 2024-10-10 04:06:19 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 85.6 |
| fe7c670b-73c4-394d-8fa5-d5c4eeaed29e | -12.9736 | -62.6987 | 2024-10-10 04:06:20 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| 81fae72c-4634-3615-8a28-041f161412d6 | -13.8379 | -44.522 | 2024-10-10 04:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 112.0 |
| 22e7e91f-d9c2-3e6c-9517-d72fb884db54 | -13.8384 | -44.4984 | 2024-10-10 04:06:23 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 70.8 |
| e314e41d-43a1-350b-b3f5-673485c8926d | -13.8574 | -44.5185 | 2024-10-10 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 126.0 |
| 745276ad-29b3-3439-96fe-8e6d2db69bc3 | -13.8579 | -44.4949 | 2024-10-10 04:06:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 86.7 |
| a35c0c1b-bc95-35f8-be83-549aceadf3a1 | -2.6533 | -53.3506 | 2024-10-10 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 122.1 |
| ba735152-ab72-34ee-ad35-3d36382231d4 | -2.6533 | -53.3303 | 2024-10-10 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 996c4912-f636-3560-93f7-86fa49dd3384 | -2.6716 | -53.3704 | 2024-10-10 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b7d7c7a7-dbb8-35da-a811-53e1b183ac98 | -2.6716 | -53.3502 | 2024-10-10 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 249.7 |
| 43e8324e-4826-3af6-ba08-e1ac2c55002a | -2.6717 | -53.3299 | 2024-10-10 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 109.0 |
| d10b4945-5620-3dc8-8086-e31f7ac571ea | -2.69 | -53.3497 | 2024-10-10 04:15:21 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| b380af26-bdd0-3be7-b399-d9f0abb7aab5 | -4.0962 | -48.2523 | 2024-10-10 04:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 96.8 |
| b5eb6bda-9b23-3068-a4a7-9966b0a26527 | -4.0961 | -48.2739 | 2024-10-10 04:15:29 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| 491c30ab-6de8-3356-a0ae-874b3eb0b462 | -4.1146 | -48.2731 | 2024-10-10 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 146.3 |
| c0a2e254-0cb6-3e74-8f1e-8eceadda6ece | -4.1148 | -48.2515 | 2024-10-10 04:15:30 | GOES-16 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 104.5 |
| 1fee86c9-305e-3aaa-bfc3-0fe2c5abb7aa | -6.7654 | -59.3252 | 2024-10-10 04:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 85.6 |
| b88b1495-4cda-32b5-adbc-17ada850882d | -6.7655 | -59.3059 | 2024-10-10 04:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.5 |
| f559991b-fb65-3ede-b948-b733da8a35d6 | -6.7839 | -59.3245 | 2024-10-10 04:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.9 |
| f8916aae-966a-354a-9927-4a53859611e6 | -6.784 | -59.3052 | 2024-10-10 04:15:45 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 32baae98-5bc4-3bfd-8922-b40052abaa1f | -7.0786 | -59.4087 | 2024-10-10 04:15:47 | GOES-16 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 130.8 |


[Clique aqui para ver as próximas entradas](README55.md)
