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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4966f2f1-e546-3aab-aef9-89122932e9da | -6.68491 | -43.55011 | 2024-10-01 05:04:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af246f63-bcb0-3935-93b9-7f13159be1d4 | -6.5413 | -43.0378 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 23.5 |
| f33e527b-55c2-3927-b2d8-1f36fd75d6dc | -6.54048 | -43.0439 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 19c19de5-6b74-3886-a2a2-02abd32cef88 | -6.50488 | -43.15832 | 2024-10-01 05:04:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 635a9883-a1dc-3004-b468-eceaf671946f | -3.47257 | -43.35612 | 2024-10-01 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 612cb662-40c0-3512-8c2f-6adf808f8fcb | -3.46958 | -43.35538 | 2024-10-01 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 71f2afc8-e10f-30c3-851a-607b256c1479 | -3.46882 | -43.3605 | 2024-10-01 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19b456b0-3a6b-36b4-9da9-21cb78410c30 | -3.46626 | -43.3551 | 2024-10-01 05:04:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a9cabbd9-9b11-376f-9a8a-a7c9b46345d9 | -5.40736 | -43.43559 | 2024-10-01 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2539d3bc-30a6-383e-ab02-156118105c70 | -5.40663 | -43.4409 | 2024-10-01 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0b883261-c24f-34e8-aed6-7a3bddbb9175 | -5.40094 | -43.4344 | 2024-10-01 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c87f98de-496e-3dbb-9711-67ed0958a1bd | -5.40022 | -43.43969 | 2024-10-01 05:04:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 303742a3-6790-3e7e-91fa-6c306cc85cfb | -6.24829 | -44.14394 | 2024-10-01 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 23e25cc3-d285-3539-822b-d7441560ce2e | -6.24764 | -44.14882 | 2024-10-01 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7cc300fc-4647-38f2-8669-3dee48d3db03 | -6.24276 | -44.13759 | 2024-10-01 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3228d6b0-e647-37c5-a9fc-d05ae952fd35 | -6.24208 | -44.14273 | 2024-10-01 05:04:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 203c1f01-754b-314f-ac77-247219b239c5 | -7.30219 | -43.79237 | 2024-10-01 05:04:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fba77050-8708-397e-8e3f-11a9aa17e80a | -7.29499 | -43.79697 | 2024-10-01 05:04:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca874555-2c97-3ab4-a587-576e8451abaf | -5.98748 | -45.37204 | 2024-10-01 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a985a111-2b83-353b-8890-35b7cf1dcd15 | -5.98173 | -45.37113 | 2024-10-01 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 29.6 |
| d72c37f9-bba0-383d-a424-f91bb8466866 | -5.98118 | -45.37516 | 2024-10-01 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| d81884a4-a539-31d2-9c66-cfdac8897dcf | -5.97545 | -45.37415 | 2024-10-01 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 97a840f7-82b5-3c66-99bd-d32ead3019c5 | -5.9749 | -45.37819 | 2024-10-01 05:04:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| ff4be07f-f248-3769-bd77-d9ab590f60f9 | -5.77785 | -45.55236 | 2024-10-01 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 036f7edc-27cd-3e2a-b216-8c92f21711fc | -5.77271 | -45.54776 | 2024-10-01 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fc934575-7b4b-30ce-a81d-00afcf24edf1 | -5.77218 | -45.55154 | 2024-10-01 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f51605a3-6bd5-34be-b151-ff83e1d083fa | -5.77165 | -45.55534 | 2024-10-01 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a2b32856-9eed-320b-8116-d69e198a5778 | -5.76598 | -45.55453 | 2024-10-01 05:04:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 292fb138-da62-379e-814b-a0374564b276 | -6.93506 | -45.60085 | 2024-10-01 05:04:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1db9f245-9ae2-30bd-8793-50988081aef4 | -8.74511 | -47.13002 | 2024-10-01 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4642cd3f-62bf-3d60-8c2c-20461a9bd78c | -8.74467 | -47.13335 | 2024-10-01 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 621e8d03-88ba-39f7-9616-13df4688f22b | -8.62501 | -46.5437 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22f7b7fe-7250-3e25-bffe-8099d0408670 | -8.61947 | -46.54296 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7377ff9e-0e53-35fb-84d2-0a5cc996c8bc | -8.47694 | -46.85536 | 2024-10-01 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e83b9ca7-2b85-3f1b-b97c-17bd5742acec | -8.47653 | -46.85844 | 2024-10-01 05:04:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0dc480ea-c763-3c1c-b739-6f97cf02c5e2 | -8.45803 | -46.44663 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 085fe604-e56f-32b5-80cf-5ea11caf8248 | -8.45248 | -46.44586 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2c2e647-01be-3df9-8fa8-298461c3eb29 | -8.45195 | -46.44975 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| f436e8ae-d4b6-32e6-9f0e-5ed49f8f1a0d | -8.4459 | -46.45278 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb166abf-c4ae-32be-ac89-2a846eeb2b99 | -8.44538 | -46.45667 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c9037539-daa7-3198-80a5-933b2c96a2be | -8.43565 | -46.35918 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0fb6928d-b47a-32e7-bd03-33ce54fb2b49 | -8.43514 | -46.36311 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 338851e8-574b-328d-8f9d-7a85081589ba | -8.42742 | -46.33528 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2ccc483f-7cc1-3b50-a794-20877b7e38c2 | -8.42177 | -46.33495 | 2024-10-01 05:04:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 76a8b140-40b6-3c1f-9690-01f0d8bd01bc | -2.20158 | -46.27378 | 2024-10-01 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a9f8d208-4089-3609-ad20-fc7fff4a0774 | -2.20113 | -46.27682 | 2024-10-01 05:04:00 | NOAA-21 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 175eac98-89c6-3a1e-83ef-6cf7d4f7b54f | -2.53883 | -47.23033 | 2024-10-01 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 815093d9-3bb3-361a-9805-a5fae218f89b | -2.53401 | -47.22963 | 2024-10-01 05:04:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 986791c3-ab6d-3eb5-ad19-2c4cde3d9afc | -8.43357 | -47.13998 | 2024-10-01 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5cab6b99-5e88-330a-ab00-3fbebbc0858f | -8.43313 | -47.14324 | 2024-10-01 05:04:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ff56cf5-a811-3ec3-909a-520707ceba03 | -4.76136 | -48.0075 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1a6c7392-50e5-3658-bfe8-e11e7ae4e227 | -4.75663 | -48.00682 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ea230d7c-ad1f-36f1-afbe-9eaebd4e9d2c | -4.58031 | -48.03394 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6fac5800-726e-3c73-b116-a1252632573d | -4.49228 | -48.11182 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1569736d-03bb-35ca-98ac-288a17ab2da5 | -4.48986 | -48.1101 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 83d47b74-d283-3dc0-8a1e-8a42be71bfc8 | -4.48912 | -48.11502 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a7f53032-a497-3eec-a62d-50012f575459 | -4.46972 | -48.11704 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| a976c681-b2c8-3943-82a7-bbd69a1d7651 | -4.46823 | -48.1131 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| c06084c4-78d8-3a12-8cf9-cd40cb8f870b | -4.46754 | -48.11801 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 285389ae-c6ea-3efb-9721-f86e97569d0f | -4.46505 | -48.11631 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 5a072e11-07c4-3448-bb5e-9979d07fb3a4 | -4.46432 | -48.1212 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 838f8a00-bbd8-3a29-96ea-64c8bc7b4e66 | -4.19372 | -48.2342 | 2024-10-01 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 75b61497-cc44-3f10-b9d2-b5595c75b4aa | -4.15119 | -48.3961 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ede72e2e-586d-386d-8793-f6249c6b90bf | -4.15053 | -48.40057 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c7027ae6-9517-3fb5-8c74-ee658495bbdb | -4.14596 | -48.39998 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 75094983-5cf5-35df-adff-051602aed08b | -4.14529 | -48.40455 | 2024-10-01 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b876661e-49d5-3d34-b8fa-dbd6f155e873 | -4.08904 | -48.27512 | 2024-10-01 05:04:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| adbba1e5-5efa-3a9b-8e8a-4e37edc3b85a | -7.63582 | -49.71424 | 2024-10-01 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b03138c-dcb9-3ec3-9bb8-97db71fc7f3c | -7.63521 | -49.71854 | 2024-10-01 05:04:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6f4c6f47-4f76-3474-85e5-292c45e4b808 | -8.66483 | -49.42461 | 2024-10-01 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c89e3db0-fd41-3d2e-8745-a565fb862db2 | -8.66418 | -49.4293 | 2024-10-01 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2a109326-4363-36c0-8774-2008b323685b | -8.6603 | -49.42387 | 2024-10-01 05:04:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9206600-3d28-3040-a3df-7dc383e198bd | -8.55456 | -49.60728 | 2024-10-01 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f8141c42-29bf-36f7-b829-4745fda375d4 | -3.36034 | -50.37581 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c06ce81-b967-307b-a539-8e2f3384d0da | -3.30665 | -50.0463 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89de0e85-9d3f-3d8b-a391-2ec80feba369 | -3.21674 | -50.44838 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8469b22f-922c-3517-90f4-36c7d19c4293 | -3.216 | -50.45324 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 62f306af-eadb-3b37-bb78-cc7fe752df0d | -3.21283 | -50.4478 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 03933ca3-798e-3122-831d-7ecbb5049701 | -3.09556 | -50.47885 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 08d6f5d8-2b88-332e-9601-45a55f98195e | -3.09166 | -50.47827 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6f7d6d48-04b2-3169-ae72-9ad78cd2c4d1 | -3.08776 | -50.47768 | 2024-10-01 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1df723a4-f532-38f1-b219-e19f6db37f7e | -2.40885 | -50.32091 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 00fc7a54-ed41-34b2-b607-51b60b45b9ee | -2.40846 | -50.31916 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 571a932b-6ce2-3c77-9f29-bfe15bec0038 | -2.40811 | -50.32585 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d3bbb3d1-0196-356a-b081-6b102cad10fb | -2.40769 | -50.32409 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8cefad8d-66e7-360a-a098-0055f98c3ee4 | -2.40738 | -50.33079 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| af75592b-691e-30c7-a148-de1d9c3ddf37 | -2.40692 | -50.32903 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1f3eaf52-01af-3965-97a1-2899455c27b7 | -2.40616 | -50.33392 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 27dc1d69-d69a-307e-9d2b-a1d8d74b91f2 | -2.40456 | -50.31858 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2abf1f02-9f4e-311d-9cbb-2f560305a4f0 | -2.40379 | -50.32351 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed97d848-8c0b-3e54-8736-68228d34b15a | -2.40303 | -50.32843 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 6a7ed634-0eee-33e5-b217-f948df28cb10 | -2.40226 | -50.33333 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5e570d54-1b98-326b-a6ab-2a8dfc67b776 | -2.4015 | -50.33823 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0af28f31-d0c6-37f9-9c83-155a3dcddd2d | -2.39989 | -50.32291 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 49cca41f-c2f6-388d-b0a3-ff640cae1886 | -2.39913 | -50.32783 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 6643b9c3-e248-358c-bd3b-9c561406fca8 | -2.39837 | -50.33274 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e8772887-6777-31ed-837f-5edb89ea3bab | -2.3976 | -50.33764 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| d099936b-af72-3d9e-9f21-887e2c772d58 | -2.396 | -50.32231 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fcbe2d29-8a32-3703-b334-32ea9a0c1c3e | -2.3921 | -50.3217 | 2024-10-01 05:04:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| cf10f335-8a99-31ce-89c9-4e5b02311deb | -3.93991 | -49.99533 | 2024-10-01 05:04:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README100.md)
