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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c833adf1-5802-35f3-9ec7-d32298853653 | -5.3696 | -56.0509 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f9bce3b-93e8-3b7b-b739-57868f1a4467 | -4.37 | -43.8255 | 2026-10-03 00:52:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| df777d55-5b23-32d0-a420-ffdf9352daef | 1.7867 | -55.595699 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 74759e30-31fe-3485-84fe-2c9f38922933 | -11.4869 | -43.411701 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4fbaebdc-7d2c-3b04-8531-dee2d7b81b7a | -3.2146 | -53.938202 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2deeeb29-994b-35f1-9c2b-1c8080d574a4 | -1.1411 | -54.157501 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5840f437-64b5-3623-b7cd-2763d98dd10f | -3.1799 | -54.1022 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73c9c6fe-23b3-3f36-99dc-227605fb8d45 | -3.2804 | -53.820202 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a37d0c02-a6f8-3e0d-a01f-4bd3eeb78940 | -6.0075 | -53.533699 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c1043421-b1e2-384c-b0dc-f9079f49d6b6 | -6.4346 | -55.622501 | 2026-10-03 00:52:00 | METOP-C | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86885370-a1f5-35de-9bb4-49dc570d1881 | -3.0605 | -54.166 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08e738e7-9f95-3bea-91d7-e233b66b37cc | -6.8471 | -59.293201 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1ce0a393-c96b-352a-a913-389ba7008d05 | -12.9792 | -41.164001 | 2026-10-03 00:52:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 89306a77-5139-3e52-9e4e-cf1ac2788271 | -3.295 | -53.839001 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91c164f7-74eb-33da-8e64-4a3788102af8 | -11.8237 | -43.556999 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ebd980a-fb21-3aa5-bebb-f950dc61393e | -1.2024 | -47.777699 | 2026-10-03 00:52:00 | METOP-C | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 86d043c8-8419-35d0-804c-551026c496e2 | -11.7145 | -43.493301 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9ba540fa-8023-3c4d-996e-8e163efd9237 | -5.2476 | -55.9184 | 2026-10-03 00:52:00 | METOP-C | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca346bd4-7ed0-36e0-8d25-acea6995b648 | -10.9754 | -59.125099 | 2026-10-03 00:52:00 | METOP-C | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83522049-29a0-3263-a543-48210217c93f | -3.0589 | -54.158901 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3463871a-f6a7-31ca-a22a-ed7fec5a36ef | -4.1828 | -48.672401 | 2026-10-03 00:52:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 855beadc-d6f1-3447-8f28-dca8cf2c39e8 | -1.2166 | -54.5317 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28ed9ae6-bd2a-34ee-8c35-55ae97eda142 | -2.9774 | -53.262001 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c4032d2f-6e40-3ae7-86d3-e54b0e2f00e3 | -1.7628 | -55.026299 | 2026-10-03 00:52:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bb724fe-4a9e-3d0b-9ffc-53153f10d1c2 | -11.7048 | -43.4958 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 347b1743-6e98-32fc-9809-5cb9ef9cf16f | -3.1159 | -53.731899 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b62c91c4-b4dd-31f5-866e-8d916be7bbb9 | -11.4443 | -43.407001 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0b120414-84ed-3910-a7dc-d332cda2fb69 | -3.1205 | -48.670799 | 2026-10-03 00:52:00 | METOP-C | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b63a8136-453a-3cb8-9512-43ab4ed081b1 | -3.6403 | -55.492802 | 2026-10-03 00:52:00 | METOP-C | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| da7c330a-22b3-36a5-8436-e70a4ec782c7 | 1.7949 | -55.605202 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4635883-a700-3033-9007-7c3723f9cd93 | -5.7432 | -45.156601 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ed6e2a11-2bf3-349d-9d86-74fad51fc589 | -3.1403 | -53.748402 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5cb145e2-6ad8-3dbc-8816-63024e83c774 | -9.6947 | -57.445499 | 2026-10-03 00:52:00 | METOP-C | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 1169d0ee-d4b3-35ee-a8db-49ae7645b076 | -3.1321 | -53.757599 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a49fe285-e4cf-36c4-b967-ff80b24e68e8 | -3.2934 | -53.832001 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d876ea04-7e8c-30db-9ec2-cecc5beaecfb | 2.3526 | -50.748699 | 2026-10-03 00:52:00 | METOP-C | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 20100002-cf1d-36f0-aa1b-93262509c726 | 0.627 | -54.4067 | 2026-10-03 00:52:00 | METOP-C | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d15a9b5-7673-30b5-bcaa-d1fe39c7d909 | -3.282 | -53.827202 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e88bc84d-ff24-36fd-a25f-af3e12f03801 | -3.0172 | -53.8862 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21b13dc7-7e70-3ce3-9187-9ec6de8b0d6d | -6.0092 | -53.540901 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3dc1144c-18ca-3821-8756-515267fd29f1 | -11.7152 | -43.4151 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1bb566ff-5a0b-3856-957b-8eb0e64f9d78 | -2.5727 | -54.7379 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 68c13d68-6455-335a-b53a-afd0598fd05f | 1.9261 | -55.796398 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02d9447c-f213-3c21-a04e-c315193d90d9 | -12.9652 | -41.189098 | 2026-10-03 00:52:00 | METOP-C | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| ee87db07-f432-37ad-bec9-8f188535d72a | -3.4138 | -52.826698 | 2026-10-03 00:52:00 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77f8191a-53f1-354f-a52f-19788152a940 | -3.1751 | -54.080898 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a54e720e-7f8c-3171-bb61-780a1c0a5415 | -11.701 | -43.481201 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| da062f7d-8d95-3e5a-b2ab-799a87b85fd7 | -11.6419 | -43.573898 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5961284f-1a7d-3320-bbed-156477096b55 | -15.3131 | -42.790199 | 2026-10-03 00:52:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 26cb05ad-e152-395c-8106-f22c9195b871 | -11.4772 | -43.414299 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2985810e-cf59-35a1-b476-3bd888f44ba9 | -11.8334 | -43.554501 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3003f0e0-15b2-3488-a457-7143982e6a05 | -3.71 | -50.667198 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba3e35c8-b447-3bb0-9700-975a7283adb2 | -4.813 | -49.865101 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e6520b54-c56f-3262-82c0-a58e81af60f1 | -6.0173 | -53.531502 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4239920b-5bdf-30aa-810b-d268cb0b9842 | -2.1421 | -59.2202 | 2026-10-03 00:52:00 | METOP-C | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7441b9e2-f61f-31fc-bd58-7ba6e3821dd1 | -4.4114 | -49.956902 | 2026-10-03 00:52:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c700bcd-e255-34b2-af51-8e4cd7e1b883 | -11.7874 | -43.5359 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 17551c33-9dcd-3990-a724-6fba3b434444 | -5.9544 | -43.629601 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4c27be9f-8439-35d7-9dbf-b0cc3a337c9e | 1.8033 | -55.568802 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 797239d7-7d3d-3b5b-bc0a-441dda8974f4 | -1.2737 | -54.556301 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76450c9a-9dd8-33ed-b441-66325f6a6045 | -2.021 | -54.3078 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 505b7288-4c4f-3588-8979-b54eafe0b453 | -15.2998 | -42.778702 | 2026-10-03 00:52:00 | METOP-C | MONTE AZUL | MINAS GERAIS | Brasil | 3142908 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e13d8284-f3eb-3287-9dd0-c0428589c54e | -4.8539 | -43.0397 | 2026-10-03 00:52:00 | METOP-C | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 601ff4a8-4e86-376a-be0d-504d0ca6e30d | -4.4293 | -55.752701 | 2026-10-03 00:52:00 | METOP-C | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 670ae044-c081-3584-8eb4-d68825a63d9f | -5.7387 | -45.053398 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 144a9dc6-b817-3605-ae61-cc8ce403618a | -11.8008 | -43.547699 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6b40e583-5194-3427-8290-1091ae24a7a2 | -6.8341 | -59.279999 | 2026-10-03 00:52:00 | METOP-C | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d22799b5-f895-3f01-9283-689f05cac44d | -4.5704 | -46.569 | 2026-10-03 00:52:00 | METOP-C | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f88a4592-42ee-38a0-8abe-61830902bda1 | -11.7279 | -43.505299 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 56f84cbd-ed5d-3b77-af8b-8cd1df2eb6cf | -11.6382 | -43.559502 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5ed6e02a-41f8-3740-9427-eed1713eb2a7 | -3.0042 | -53.874298 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f860228b-35d4-30f2-9e90-15e067eabbea | -6.7113 | -45.959599 | 2026-10-03 00:52:00 | METOP-C | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b7030f5f-a4b0-3581-9e50-c8b7975f29f2 | -11.7383 | -43.424599 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 779e6906-d925-32d0-81c4-2b862655bfbd | -14.319 | -43.802399 | 2026-10-03 00:52:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c284ce1f-0aaf-3cbd-b3fc-6a4dae8cd084 | 1.7851 | -55.603001 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2c7964a-1151-3b70-b89f-3d3c5c416e7c | -3.1273 | -53.736698 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 594968b3-2d07-39ba-9b7a-5f0968126fac | -5.9588 | -43.647202 | 2026-10-03 00:52:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 41fc317e-804f-3559-b2fb-85f59dd4fe81 | -11.4734 | -43.399399 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| aec51edb-3255-3e3a-b670-af8d7c7f34e7 | -3.2852 | -53.841202 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a091cff-dd68-38a1-b039-54f5c1f82c30 | -2.8873 | -54.129902 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c00156aa-17a8-3636-9a49-61635b78f680 | -3.2673 | -49.5186 | 2026-10-03 00:52:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8b5d796-2670-3cb0-8cbe-81dc6ac8ca75 | -11.6553 | -43.585701 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4040c2d4-bf44-3fe0-b85f-b14818dd2b3d | -5.7495 | -45.140202 | 2026-10-03 00:52:00 | METOP-C | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 78a1f0ef-fcc1-3c5c-90db-8a67cb1ba1b3 | -3.7049 | -50.645302 | 2026-10-03 00:52:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 569700c7-17f0-3a90-9f79-9b6fd657113f | -2.9626 | -54.098301 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12524f74-75d3-35ae-ba36-98b195149788 | -11.4599 | -43.387001 | 2026-10-03 00:52:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0d15d8f8-faab-33d0-bb3c-637f649d034e | -3.7525 | -45.946499 | 2026-10-03 00:52:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b103c311-19e1-3501-b3fd-53b06b209327 | -1.1052 | -54.1362 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9567ab4-9728-36f8-8ac0-70ab4430b65d | 1.7966 | -55.5979 | 2026-10-03 00:52:00 | METOP-C | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31de9781-6ba5-390b-a22f-51c80d1f8d49 | -0.4057 | -51.991299 | 2026-10-03 00:52:00 | METOP-C | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 41fc3876-1a03-352f-a316-6516517615e1 | -3.1881 | -54.092899 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91d96b0c-949b-3d12-92be-2f8607b39aaa | -1.1068 | -54.1432 | 2026-10-03 00:52:00 | METOP-C | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3fd9d197-71cc-309c-a010-59892c7a6232 | -5.859 | -53.4692 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0e7b5d1f-d0d0-3ad0-a33c-deb7823e93b9 | -2.8841 | -54.1157 | 2026-10-03 00:52:00 | METOP-C | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5477ae17-2158-3038-80ea-14ed8db21e63 | -3.5861 | -54.5285 | 2026-10-03 00:52:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f76cc268-1209-30f0-b4ce-8f5ca84a41e6 | -3.5097 | -54.599701 | 2026-10-03 00:52:00 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b00f6588-3d04-3b9b-ac7d-e131cc02ef88 | 3.6947 | -51.592201 | 2026-10-03 00:52:00 | METOP-C | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 02872f50-6ce1-33de-b754-dfe5202c6233 | -6.0059 | -53.526501 | 2026-10-03 00:52:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1aef433b-cf79-3439-ad8b-e7f2bbf12401 | -3.8736 | -49.686001 | 2026-10-03 00:52:00 | METOP-C | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e49bca9-a173-3f85-a5f7-3a3ee888364e | -3.1257 | -53.729698 | 2026-10-03 00:52:00 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README9.md)
