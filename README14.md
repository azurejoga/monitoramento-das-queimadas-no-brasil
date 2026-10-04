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
| 922d70ac-fddb-3e6c-a583-3dea05464754 | -2.57004 | -51.87641 | 2026-10-04 00:37:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 39.7 |
| 43ccef30-5d4b-3afd-9011-69069e7676bc | -8.5629 | -67.05794 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 9fd639af-01ca-304e-854b-0b197345c92b | -2.80378 | -54.09329 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 4d67a874-5096-32f5-ada3-98a8353132b4 | -6.1997 | -52.80133 | 2026-10-04 00:37:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.7 |
| 00322581-8a43-3b35-b5eb-f34610dc532d | -4.2875 | -50.2994 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 51.9 |
| 1f8058c3-0b92-335a-8f73-4bd8a44cb193 | -10.95902 | -60.91935 | 2026-10-04 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 14574460-aac4-3cd6-ab7a-055f63be12c0 | -4.7895 | -55.71943 | 2026-10-04 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| f9030ad1-6737-3ee0-98c9-bf70486b5881 | -4.27532 | -50.26249 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 40.6 |
| 27aeefa6-8423-32fe-bc5b-4b3ab0b2b24e | -3.11762 | -53.71574 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 80272541-9860-3738-a09d-98069de2c658 | -3.17985 | -50.54319 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 1d1154d9-822f-3085-ba7c-cdbf99a8af11 | -3.13253 | -53.7321 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 156d1782-04e5-34ff-9824-ee05b77bda27 | -6.06586 | -53.48592 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 66e17244-2bb0-3153-818e-809fdaa43f6c | -3.46779 | -50.08853 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 205.7 |
| 1284e308-2f70-3c1e-bca1-373c27748f27 | -4.54829 | -55.97324 | 2026-10-04 00:37:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 599dacff-61ff-3601-a71c-58edd19d326b | -10.28372 | -55.07012 | 2026-10-04 00:37:00 | TERRA_M-M | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 29f37576-d14d-3c73-863a-ead1e4cd6bfe | -2.79174 | -54.09504 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 23.2 |
| a5c7f060-914b-3ece-8477-7ee2590c18bf | -3.10526 | -53.71753 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f0bc906b-b97a-304c-babf-62708f64347c | -3.47331 | -50.12366 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 5e88058a-28da-357e-8e30-666d18686e83 | -4.21029 | -53.45512 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 3fe847a1-e5d5-3f08-9558-c293848bfa2d | -2.80843 | -54.08704 | 2026-10-04 00:37:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 79aa1fd4-a2a7-3e12-91c7-061031a532e6 | -3.7184 | -59.6853 | 2026-10-04 00:37:00 | TERRA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 7fd0c5f2-22d6-3f06-82aa-d7f3c1d9a406 | -3.87037 | -55.80167 | 2026-10-04 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 4f2401ea-8161-380c-a114-511ddf9233b8 | -2.57897 | -51.85498 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 106.5 |
| 59f1858f-99a1-36cc-ace2-696cf728334c | -6.21152 | -52.80581 | 2026-10-04 00:37:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| d9047c48-78bd-336d-8e0a-ed08a5585a35 | -11.92275 | -63.16091 | 2026-10-04 00:37:00 | TERRA_M-M | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 9ef1d9e2-eab9-3ace-861d-bfc8a72ff115 | -6.00571 | -53.53552 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.9 |
| c326848a-da15-306a-a7f8-a82502dc57f3 | -6.06319 | -53.46815 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 8e2fc81c-5232-3e75-9221-415ee8601c6d | -6.45949 | -55.45464 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| d7563c68-0568-3fcc-af78-ca1b7f5c1d17 | -3.18411 | -54.10053 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| b071bc20-e7b6-39bd-83a0-e462763cceff | -8.56067 | -67.05263 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 74.8 |
| f95d44b9-9dfc-30e3-9099-e632c93aa1ac | -3.77824 | -51.39958 | 2026-10-04 00:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 28.0 |
| fd3d41c0-eb70-305c-954c-11eba4c6d3d9 | -2.58271 | -51.88124 | 2026-10-04 00:37:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 48f3cba0-17a3-31e5-a0a8-e9482ceae1bb | -9.79295 | -60.1394 | 2026-10-04 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 4db70d04-b55a-36da-977c-fcf8e55cd45d | -6.01766 | -53.534 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 2890c3e6-4e94-388c-83f7-3de4f5d5e117 | -4.13145 | -54.16504 | 2026-10-04 00:37:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 26.8 |
| d6c9c92b-733d-3763-b0fb-32290c06f680 | -3.00446 | -50.48059 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 38.9 |
| fe7af4f0-f69b-330c-9f94-5b7c96490e63 | -5.86147 | -55.70769 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 17c1e9d7-2ad0-3d6d-a5d0-9067e6e014b5 | -3.21291 | -50.76703 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 35.9 |
| 7f7074cf-87a8-3d04-b1d6-c912978a190b | -3.18682 | -54.07656 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.0 |
| a07912d5-3491-3fb7-ae0e-0f0b1e5e4de8 | -2.81097 | -54.14449 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| dd10d934-3307-3634-bd2d-ebf2513fea39 | -2.58059 | -51.848 | 2026-10-04 00:37:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 7a741433-d602-374e-b1b4-a25e91823d38 | -9.70278 | -57.45129 | 2026-10-04 00:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 1efd7ab4-0c24-3cc1-8e9e-8d5fd49c3615 | -4.213 | -53.47338 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 4467ae9a-2030-30d1-825d-27ae96459897 | -3.47781 | -50.09228 | 2026-10-04 00:37:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 93.1 |
| 99de9868-5061-3075-8540-c106a22c37b9 | -8.2369 | -61.18287 | 2026-10-04 00:37:00 | TERRA_M-M | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 873bcd24-1dd3-3191-a984-852de7321b96 | -3.58528 | -55.315 | 2026-10-04 00:37:00 | TERRA_M-M | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| 3507cdf3-2c9f-35e0-8786-c9e9c2453f1c | -11.05066 | -62.57382 | 2026-10-04 00:37:00 | TERRA_M-M | MIRANTE DA SERRA | RONDÔNIA | Brasil | 1101302 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| b9272216-1657-3139-8929-d8251ccdcb2b | -2.58453 | -51.87432 | 2026-10-04 00:37:00 | TERRA_M-M | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 156.8 |
| 6340546a-fbea-36f4-87e0-d936a32c20c3 | -4.46253 | -50.98097 | 2026-10-04 00:37:00 | TERRA_M-M | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 2c794e9f-eab1-313b-9994-ebdd94eddfbc | -2.8135 | -54.12135 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 129.4 |
| 25c9e3c3-294e-303e-aaea-0f6bc26a8010 | -8.71534 | -61.40555 | 2026-10-04 00:37:00 | TERRA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 22.1 |
| a042bf64-adbc-3bad-915d-931309246894 | -8.35688 | -62.83668 | 2026-10-04 00:37:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1b01589b-cb8e-38b6-8f4a-eb08f0127c4e | -3.04986 | -54.2298 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| c30a6e44-49a9-3d42-9905-6e076de5333d | -6.21227 | -52.79924 | 2026-10-04 00:37:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 17.2 |
| ba6748fe-49d1-355b-b9fc-4e8881a9f539 | -2.89039 | -54.14495 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.4 |
| b31b45ed-6c2e-35c8-ab45-0ecb41f7889f | -5.61756 | -57.23605 | 2026-10-04 00:37:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 28948d75-d957-33f9-a5c1-24882d487285 | -8.57993 | -66.82337 | 2026-10-04 00:37:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 6bf4e205-a169-3806-a857-7f782d5641de | -2.97473 | -54.09127 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1bcfd538-95fb-3b9e-83bf-259457329361 | -3.17744 | -54.09578 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 55bd5588-189a-348f-b2ff-32d3ce18d8e8 | -2.8086 | -54.12764 | 2026-10-04 00:37:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 64a9fff4-0d42-33c2-adba-5574003b5ce2 | -3.13507 | -53.72585 | 2026-10-04 00:37:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| abd1c38a-55a1-32f0-bfc2-cef4227f5c87 | -9.16344 | -61.41144 | 2026-10-04 00:37:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 34118d56-b3b9-3362-9147-6329b6a09a26 | -6.07516 | -53.46643 | 2026-10-04 00:37:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 0ab6780e-d8d9-3bfe-b72e-66c974eb17ed | -3.51213 | -59.80416 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 27188279-da5c-3e77-a41a-8fdb3c042c8f | 2.51667 | -60.99838 | 2026-10-04 00:39:00 | TERRA_M-M | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 54bba828-d916-3e62-ad70-37875cc9b3ec | -3.45275 | -59.63356 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 67b58d69-618c-3e70-8804-eb3f5cfbdd57 | -3.50452 | -59.81417 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 81652fb1-2fb1-38a0-9899-93df95053a1a | 1.91177 | -55.76785 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| a6bd794b-f581-3910-881e-5a95328aa695 | -2.68509 | -54.6416 | 2026-10-04 00:39:00 | TERRA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 5319fd2c-f7f1-309d-b1ec-558c71e395a8 | -3.10264 | -58.56467 | 2026-10-04 00:39:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d7adb56e-8f9c-3e00-951c-372eacfb4713 | -2.53925 | -58.0299 | 2026-10-04 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 79adddc9-90fa-3b5d-b6df-2764730272aa | -3.17784 | -57.91652 | 2026-10-04 00:39:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| eb3b881a-1e75-3969-bffa-d74069b13986 | 1.76818 | -55.64223 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 25.7 |
| 2026e04a-9123-305f-817e-b6ee510931a6 | 1.91573 | -55.7473 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 88095f23-81cb-329c-82ea-b0645ea6f625 | -2.22729 | -53.71046 | 2026-10-04 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 540673ab-13c9-3e94-ab61-a0fc97705346 | -3.24013 | -58.75972 | 2026-10-04 00:39:00 | TERRA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b64c4113-044b-334e-8908-2747c8ed1cb8 | -3.28652 | -59.42122 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| c4b15eb7-4cd0-3411-bde3-069cf34c2d49 | 3.58447 | -60.12936 | 2026-10-04 00:39:00 | TERRA_M-M | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 4.7 |
| d263a703-cbc1-3e75-94f6-19d929b29769 | 2.01288 | -61.09706 | 2026-10-04 00:39:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 8.0 |
| cd6f6c34-8bf5-32c9-9235-363f3f0fc08d | -2.32329 | -60.06664 | 2026-10-04 00:39:00 | TERRA_M-M | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 40a8736b-5ef9-3435-a110-c70579b54850 | -2.77738 | -57.6915 | 2026-10-04 00:39:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 73276e10-caee-3be5-8e7c-6b87bb8eceec | 1.04004 | -59.46176 | 2026-10-04 00:39:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 34be60a4-70bd-3e4e-bca6-5dcb21ede3fc | -3.45396 | -59.64234 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 0f0d5d90-8728-3c2e-ad43-3ea450e07923 | -1.81749 | -59.93563 | 2026-10-04 00:39:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dbe3d892-e738-36c6-9e36-718ca05b2747 | -3.23805 | -57.87874 | 2026-10-04 00:39:00 | TERRA_M-M | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 1691b073-4517-3cdb-8fcb-3c0b6b20c7d6 | -3.50331 | -59.80539 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e4b0097b-2032-3656-b744-6ac00e83b7c8 | 1.75707 | -55.65068 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 58a5bc11-d5ff-3ab7-8fbe-a29fe04d9496 | 0.45034 | -60.5436 | 2026-10-04 00:39:00 | TERRA_M-M | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2c349ed5-9049-3c1e-af91-a2b22e02634b | -2.54059 | -58.03945 | 2026-10-04 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 1c55fe12-37ea-3425-bde2-5188ad35c833 | -1.09149 | -54.1084 | 2026-10-04 00:39:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 52.5 |
| a031cd54-bea4-39bb-851c-1953081ed3bc | -1.81629 | -59.92688 | 2026-10-04 00:39:00 | TERRA_M-M | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 80a53d66-113e-3754-9fc8-bbffaecc9db8 | -2.05597 | -56.86964 | 2026-10-04 00:39:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 7c3c3dc1-aabb-3af8-b2d8-244643082b46 | -2.77599 | -57.68166 | 2026-10-04 00:39:00 | TERRA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| dc5e7657-1f7b-3d37-b5a0-a35bce9c096b | -2.05752 | -56.88078 | 2026-10-04 00:39:00 | TERRA_M-M | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 34.1 |
| 117be213-87ba-3545-adb0-028925db8561 | 1.76612 | -55.6576 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 34.6 |
| 871435b1-72d7-3d13-9ff9-db2e3606ecc2 | -1.10391 | -54.10682 | 2026-10-04 00:39:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 36.5 |
| 5a8d6e5c-9e66-3df3-a839-2094aad84310 | -2.22452 | -53.69142 | 2026-10-04 00:39:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 18.0 |
| 3ab76ef6-4ef5-3822-8a4d-9fc03ca4fc78 | 1.7567 | -55.64061 | 2026-10-04 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 298c8368-6886-33e3-864a-26e1a3def98a | -3.42549 | -59.56585 | 2026-10-04 00:39:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8a3d1793-fa16-3f85-8cea-084ac8133af9 | -2.67938 | -54.43084 | 2026-10-04 00:39:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 25.1 |


[Clique aqui para ver as próximas entradas](README15.md)
