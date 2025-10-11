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
| 6d02a2d8-29e6-33ec-94ea-bdd25233fc1a | -17.8964 | -57.67282 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 43994242-02ea-3687-ad9e-f78001138224 | -18.38723 | -42.9816 | 2025-10-11 04:36:00 | NOAA-21 | MATERLÂNDIA | MINAS GERAIS | Brasil | 3140605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| aaac9fc5-739b-3ec8-b5c5-8822880ecb92 | -17.24368 | -52.27028 | 2025-10-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 66c1c8b5-354e-3f89-bf3e-333d35b2835a | -17.25682 | -46.89819 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d503a017-9bb8-3d72-a41f-b4d9a9d1feed | -18.58958 | -46.54824 | 2025-10-11 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df1f6dcb-4cb9-31f7-93c9-1950b7abded4 | -17.82209 | -57.66295 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.5 |
| a3dd7a38-2393-3c89-9c51-6c797abc22c9 | -16.30785 | -47.16082 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c8dbcb42-aec7-3023-b800-e2435a4fe82b | -16.87825 | -49.67658 | 2025-10-11 04:36:00 | NOAA-21 | GUAPÓ | GOIÁS | Brasil | 5209200 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ed088f7-6945-3ede-8aac-63bca744908d | -17.21613 | -47.65688 | 2025-10-11 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 4de2d575-db9e-337b-a6b4-1fec7ea2d1e8 | -15.1869 | -56.77915 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a09f4f9-c549-3da3-99e1-961f90a27748 | -18.04239 | -44.48587 | 2025-10-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0ec1c813-e3a9-3b77-a5ee-f71023a1a2dd | -17.26471 | -46.8949 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 4f1e214f-5df0-353f-9913-ec3e1f74773c | -17.48674 | -43.33029 | 2025-10-11 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eeee055e-a11e-3b54-b609-2b9444d2b028 | -17.49129 | -43.33092 | 2025-10-11 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 09ee7dae-8a38-3bf2-8980-dbdf5575244f | -15.21992 | -56.73994 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e41f8547-e5b0-358a-94b4-44a88976016e | -15.01661 | -56.08191 | 2025-10-11 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 880bf784-0c4e-357f-b3c3-e74dbb757513 | -18.07139 | -57.52516 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5fe90896-38ff-3104-80cf-762b6be8b708 | -15.22435 | -56.74093 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2ee604fc-7b57-3a1d-b70c-257028447090 | -17.49071 | -43.33563 | 2025-10-11 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 0fa551bc-4408-3d01-86e3-a83a37db4c87 | -16.53733 | -46.72942 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 68b2461f-0d54-36b3-ab44-c7763051e437 | -17.26712 | -46.90442 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 17.1 |
| ac369787-2529-3755-8f3c-066d867dab64 | -15.18862 | -56.7698 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 73ee27b6-13a4-3c13-b72c-421ebca68e1a | -17.30766 | -50.97677 | 2025-10-11 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8c67ed19-65e8-3f39-a3f6-bfd2db88122b | -17.83189 | -57.66075 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 8358fa77-c462-3ace-a95c-903d5986da37 | -17.24794 | -52.28679 | 2025-10-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f4ae06ff-4078-34b4-8708-0a43f3dfe472 | -17.2132 | -47.65229 | 2025-10-11 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| a52c5185-8510-3fc3-9b3a-6c3823bd7266 | -17.25134 | -52.28739 | 2025-10-11 04:36:00 | NOAA-21 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| aa70b2be-17e6-338e-a43a-c7ae85e1e31e | -16.31027 | -47.14391 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0c4f17f-a0c7-3fea-8ed3-ffeee873009e | -17.82648 | -57.66452 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 28654ea7-6b6f-306d-b5fc-d3179c152581 | -17.21262 | -47.65635 | 2025-10-11 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 3b0984c2-acdf-31e2-9cfd-5d148edde23d | -15.86475 | -56.74312 | 2025-10-11 04:36:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f1b66f01-9f2b-3143-ad01-8a427de7b5b2 | -16.30726 | -47.16495 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 5192c117-eb3f-3b09-9d7c-d2f2bb637628 | -17.84717 | -57.58101 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| c674d9b0-6903-34e7-a098-d7e4a1484cef | -15.1594 | -56.82762 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a97f3ef-0c9a-3bfd-bdc0-d8ada7e6f0a6 | -17.95411 | -57.61603 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2677b903-8a39-3de1-adc3-82c741a58318 | -18.81824 | -54.96187 | 2025-10-11 04:36:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7d5dd969-4da2-3c03-a37e-71ca69328bc4 | -18.04668 | -44.48622 | 2025-10-11 04:36:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dbc99e1-8995-3c09-b1e9-983bf9679ac9 | -17.83091 | -57.66585 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3e5aacaf-244e-32e9-989d-507004afd19b | -20.40625 | -43.2892 | 2025-10-11 04:36:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| b5131913-1de2-3d1b-bd31-4d133b83f716 | -18.81733 | -54.96688 | 2025-10-11 04:36:00 | NOAA-21 | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b7bc9f8-4b5d-3819-9ae4-7b09d67b4838 | -17.90088 | -57.67387 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 31e16b54-c743-37da-a470-46c57561743c | -15.16957 | -56.7229 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cf451ba8-a665-3a16-b3bb-26fa23b75a51 | -16.75836 | -49.21461 | 2025-10-11 04:36:00 | NOAA-21 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7cbe369e-fe31-308c-aee0-87e395affb47 | -16.75831 | -56.29227 | 2025-10-11 04:36:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 11.9 |
| 8b5d12ec-d69c-3fd9-86bd-bb0cc9145ea5 | -15.27186 | -56.90853 | 2025-10-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fa640d4e-5251-3c00-9a5b-2f8fb166357e | -17.81418 | -57.65538 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| f1b8ead7-926d-3670-85a3-7b8743adc451 | -18.08457 | -44.70345 | 2025-10-11 04:36:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b600a069-e95c-309e-bf78-62e4757823ed | -15.19958 | -56.79819 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bc2d8bc5-9372-3393-8303-c6edcdd499f5 | -16.31201 | -47.15719 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 59dbf8a7-212e-3b3b-abd1-fdfeabfc5cba | -20.41099 | -43.29001 | 2025-10-11 04:36:00 | NOAA-21 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 4d64581b-f834-378d-9a18-950fa4054618 | -15.45258 | -55.96643 | 2025-10-11 04:36:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3185e56-b4f1-349c-b55e-ab02821e9a0f | -18.37254 | -46.7286 | 2025-10-11 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb4b054d-683a-3263-bada-333e6091505a | -17.55266 | -47.67986 | 2025-10-11 04:36:00 | NOAA-21 | CAMPO ALEGRE DE GOIÁS | GOIÁS | Brasil | 5204805 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 7eabfb43-8c68-3ff2-a175-4aa7dc9b34fc | -17.84341 | -57.65628 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| f02f9d13-2f7b-301e-8712-49933f3e7fe8 | -18.22447 | -42.37661 | 2025-10-11 04:36:00 | NOAA-21 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3687c5f-791e-3e51-8ffe-498c95ec71b3 | -17.88655 | -57.50892 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0eec80da-0f52-3884-b457-8ae29d3647fa | -17.84175 | -57.65815 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8e2c9003-61fe-3437-b97f-732fb742b089 | -16.92869 | -46.57185 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 290c2ccf-c582-33af-b2fd-fa657403e97f | -17.71497 | -42.61511 | 2025-10-11 04:36:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 0554a026-1cc8-3c72-83ac-5966f55c3aca | -18.13288 | -44.34115 | 2025-10-11 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3ba4e924-03d7-3b30-9f81-034292e3d0e5 | -17.48616 | -43.33497 | 2025-10-11 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5bdb9a7a-3f93-37de-b2ae-24be8c4f3110 | -15.01463 | -56.06879 | 2025-10-11 04:36:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9f2eddf0-9f35-3e6f-bd3f-c7fe95819aab | -17.39246 | -46.86163 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8de35ad2-f3ae-3ea1-a391-90cd0f345811 | -17.89734 | -57.66801 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 29f97fcf-1002-3674-9be6-43380c9f26a0 | -17.37232 | -46.65814 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 59ab1d54-51b5-3c9f-9cf4-f69adb7e102a | -18.58523 | -46.54993 | 2025-10-11 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9e165b81-0eae-3ebc-9fd8-641f66008821 | -15.18874 | -56.85494 | 2025-10-11 04:36:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b0c86298-b009-3ec8-a252-7b16b0d247ce | -17.25318 | -46.89761 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8e750fca-f822-3c8a-91bf-24caeda98d8f | -18.07217 | -57.5452 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b1d47f6e-c8b9-3116-9387-47925802b486 | -15.1867 | -56.7551 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6a22268d-0808-358d-a75e-67de43299ebd | -18.04979 | -57.5652 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| dacff7a5-a9c7-307e-b8a8-b35c141fe87f | -15.01514 | -56.01867 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6bd9a9a7-96ff-30d1-8ddf-413a808895eb | -17.2091 | -47.65582 | 2025-10-11 04:36:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 82cc3419-3fb6-3c99-8242-b39a08db22ba | -14.95334 | -59.4335 | 2025-10-11 04:36:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07ccb5c0-673d-32c4-a247-820eeff846d0 | -15.19051 | -56.78472 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1a0fc211-684c-3840-acd2-f424c3ae5e4e | -15.19138 | -56.79251 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca5f1948-430f-3942-8bbe-f3b451de1ec1 | -16.30905 | -47.15244 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 93a96918-2762-3224-ae8e-1a996c82199c | -17.35368 | -44.45087 | 2025-10-11 04:36:00 | NOAA-21 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2a66282d-b802-3110-8e49-7fb04ca24b31 | -18.58581 | -46.54768 | 2025-10-11 04:36:00 | NOAA-21 | PATOS DE MINAS | MINAS GERAIS | Brasil | 3148004 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ade1e5df-1c31-3183-9816-e98eb03839c9 | -15.19052 | -56.77284 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| db2dd6e9-be8b-3a9f-9257-a169dd1ab3f1 | -17.30436 | -50.97619 | 2025-10-11 04:36:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46ff23c1-3873-34d9-9815-300a8543e52f | -14.94874 | -59.42877 | 2025-10-11 04:36:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32babcc3-d707-35ba-91c4-c9382b25ba10 | -18.1372 | -44.3416 | 2025-10-11 04:36:00 | NOAA-21 | AUGUSTO DE LIMA | MINAS GERAIS | Brasil | 3104809 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 02c52c76-5582-3116-94a7-3725c067772a | -15.21025 | -56.74222 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91ff48c3-82a2-3a72-9400-4ac98889dcdf | -17.48728 | -43.33164 | 2025-10-11 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2795646f-d334-3851-8719-5b5a4368208b | -17.36861 | -46.65764 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8d5fdfee-80f0-3cc6-83e9-e7f7c4d57187 | -16.92932 | -46.56727 | 2025-10-11 04:36:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc59fe17-6109-33aa-ab90-9edde0ec7fcd | -18.07656 | -57.54649 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 40f9703f-43f7-3fd6-8a79-3b7519a1cdb2 | -16.31261 | -47.15298 | 2025-10-11 04:36:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0424be7c-6e4a-35e9-be4e-be7fe5a973fd | -17.82382 | -57.62964 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| b20ca586-7334-3b77-bd37-20fc1a26c790 | -17.49184 | -43.33228 | 2025-10-11 04:36:00 | NOAA-21 | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ef9b9a29-39b1-3779-9f13-da65d9875cdd | -15.18777 | -56.77443 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3fd361ec-4889-38d5-89a6-e3689564b345 | -17.84177 | -57.58489 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 336eda5f-cb9e-38a4-88b8-361df801d5c0 | -17.49129 | -43.33701 | 2025-10-11 04:36:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 594a45f6-08ba-3944-9323-1ce8ddd46d51 | -19.24995 | -45.02304 | 2025-10-11 04:36:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f71f0230-789c-36a9-a6df-224d7df188ab | -15.16506 | -56.72237 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| f884743e-3a37-32cc-9e63-dd8741330382 | -15.20576 | -56.7415 | 2025-10-11 04:36:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d8b45389-a7bc-3bce-96bf-0bf0143eb83f | -18.07574 | -57.52657 | 2025-10-11 04:36:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b9638b83-1da9-39bd-a396-1c70e8fe041f | -16.30411 | -47.93537 | 2025-10-11 04:36:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2b2ddce-f57d-3f59-89a5-7b71ea87ecef | -16.70082 | -45.00027 | 2025-10-11 04:36:00 | NOAA-21 | PONTO CHIQUE | MINAS GERAIS | Brasil | 3152131 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README31.md)
