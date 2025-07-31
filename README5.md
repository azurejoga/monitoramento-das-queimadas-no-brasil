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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b35ac50-1e38-3d89-8506-2d666693f6c9 | -6.50789 | -56.21566 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 20.4 |
| 7ca00be9-03d0-3436-b27d-de1fe1188b59 | -6.53939 | -56.20504 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 45308e3f-1344-3643-b2d6-278a9101d91e | -6.51878 | -56.22425 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 75fbf0da-9227-3cb7-adbc-a4fb41eb6d50 | -6.66074 | -56.39924 | 2025-07-31 01:26:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 7d5e378e-e00c-3c4c-aebf-63125cf49d11 | -6.64906 | -58.82079 | 2025-07-31 01:26:00 | TERRA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| d54b7bed-822a-3bad-bfff-c137514a1f2b | -1.3012 | -66.98322 | 2025-07-31 01:28:00 | TERRA_M-M | SANTA ISABEL DO RIO NEGRO | AMAZONAS | Brasil | 1303601 | 13 | 33 | nan | nan | nan | Amazônia | 12.4 |
| e9336786-9aeb-34fe-b149-0caff275b072 | -11.7508 | -48.1825 | 2025-07-31 01:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 89.1 |
| 1fceda1e-05a6-3b70-9ec9-c870928a59e3 | -6.6725 | -56.4029 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 114.1 |
| a77b8d9e-0a18-37d4-a0cd-b1b8a21af985 | -6.526 | -56.1923 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e76b6390-8f7b-360f-92af-85dffa18c205 | -19.2257 | -46.3537 | 2025-07-31 01:30:00 | GOES-19 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 80.5 |
| fa3d063c-c1ef-3838-a8ab-7a96e305e8c3 | -10.0655 | -53.8727 | 2025-07-31 01:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 84.2 |
| 8e182073-2c3a-3801-95b0-ba2100d35c06 | -6.5075 | -56.1932 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| 280ea738-f72f-3690-9465-6e64d71d0c9b | -10.0843 | -53.8712 | 2025-07-31 01:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 34cbb8cf-65b0-33b2-ac41-ba90d7568b0a | -6.5074 | -56.213 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 1325cc66-dacd-3295-af14-58144d365b19 | -6.6726 | -56.3831 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| b383e7e0-b235-3f5c-b178-a82f7bc8d1e0 | -6.5258 | -56.2121 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.2 |
| 6ef31ab6-94c4-3615-8b91-bed68bbede21 | -6.654 | -56.4038 | 2025-07-31 01:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.6 |
| 4424fc5e-af92-39a1-b80d-433482c07d1f | -9.4383 | -40.3668 | 2025-07-31 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 316d573b-6977-3b15-bcdc-266e4a336ed5 | -10.0843 | -53.8712 | 2025-07-31 01:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 157.7 |
| 403f7570-6495-3a16-9fb0-d1c6012b7a54 | -6.6143 | -59.9848 | 2025-07-31 01:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.4 |
| d0bdf691-f9dc-3dbc-9ee0-ab330f8e557c | -6.5075 | -56.1932 | 2025-07-31 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| bf9391b6-9f8c-3d0d-8dab-010fc1df4dd8 | -6.6725 | -56.4029 | 2025-07-31 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 113.5 |
| b18786f3-eaf7-3afb-ab27-75929914377a | -19.2257 | -46.3537 | 2025-07-31 01:40:00 | GOES-19 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 45.2 |
| 9860a353-4ef1-3790-a046-8293219427ed | -6.5074 | -56.213 | 2025-07-31 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 55dc9c23-3eed-38a7-bdaa-22fa8d14e895 | -11.7508 | -48.1825 | 2025-07-31 01:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 98.2 |
| f99202b6-a380-3c80-9819-417184cd654a | -6.526 | -56.1923 | 2025-07-31 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 004c7334-6de6-3bdf-9bec-7d4d3b1e3cd1 | -9.4192 | -40.3695 | 2025-07-31 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 56.5 |
| 846ce24d-8452-343a-b14a-935e402f82a0 | -6.5258 | -56.2121 | 2025-07-31 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.4 |
| b7ad7938-2a19-3369-a60a-89c6ecacc882 | -9.4387 | -40.3419 | 2025-07-31 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 58.6 |
| bb7d608d-b569-33be-80b3-abdfb94c4437 | -6.6726 | -56.3831 | 2025-07-31 01:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 46.2 |
| edc2511b-005a-359d-ad08-dc4a0bd487e7 | -10.0655 | -53.8727 | 2025-07-31 01:40:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 72383068-6aac-3308-be99-34569b194955 | -10.0843 | -53.8712 | 2025-07-31 01:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 60ec0a9d-7871-317a-a9bf-65970034891e | -10.0655 | -53.8727 | 2025-07-31 01:50:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 105.6 |
| 919049da-461b-3bd0-983c-6d66e4a990d2 | -11.7508 | -48.1825 | 2025-07-31 01:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 82.7 |
| 311a0c78-ea54-3755-9dcd-9f6bc8d6173b | -6.5075 | -56.1932 | 2025-07-31 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.9 |
| 9f1d74ee-6d47-3746-a4be-4a21d16206d2 | -6.5074 | -56.213 | 2025-07-31 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.8 |
| 91a238f1-986b-3960-98c8-da21a295be03 | -6.6725 | -56.4029 | 2025-07-31 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 110.4 |
| 240b16c8-8824-3646-96f6-2dc64a7790f1 | -6.6143 | -59.9848 | 2025-07-31 01:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 44.2 |
| dfd79be3-e1ee-3e14-a635-ae960059402c | -6.526 | -56.1923 | 2025-07-31 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.8 |
| 52097538-a56b-37df-a719-08cd22ab5276 | -6.5258 | -56.2121 | 2025-07-31 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| ec0c83f2-d746-33e4-b4f8-a52eba1e24a9 | -6.6726 | -56.3831 | 2025-07-31 01:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| bd81783d-bf3f-35de-b85e-05947f75553b | -10.0843 | -53.8712 | 2025-07-31 02:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.3 |
| f975c1e5-d1af-39f6-8990-10b56b9e4e86 | -6.6725 | -56.4029 | 2025-07-31 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 98.7 |
| 20fec0b1-2ed8-3837-a161-575cfb06d547 | -11.7508 | -48.1825 | 2025-07-31 02:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 81.3 |
| 58a55461-7f3b-37cd-ac22-daf11efb6bc1 | -6.5258 | -56.2121 | 2025-07-31 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| a533be6c-464d-3ec5-8707-3fa95ed52694 | -6.6143 | -59.9848 | 2025-07-31 02:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 47.4 |
| ec584c9b-0bc7-3d48-8b0b-2ed76de8dc71 | -10.0655 | -53.8727 | 2025-07-31 02:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| ac2113ff-2863-39a1-a101-3ae61ea7a181 | -10.0845 | -53.8507 | 2025-07-31 02:00:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 43.6 |
| dbdb30ed-efe4-30b4-8a86-629f87823ea0 | -6.5075 | -56.1932 | 2025-07-31 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 829a6a71-5745-36ef-aaed-b8ddace9f39f | -6.5074 | -56.213 | 2025-07-31 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 720d4ad8-0c55-3fcf-990c-41d4da202bca | -6.526 | -56.1923 | 2025-07-31 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.8 |
| 61cca030-d351-3d7b-b9bb-fe46cf88849a | -6.6726 | -56.3831 | 2025-07-31 02:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| 334d1ea5-1ee3-37d9-8746-f5744f9e5495 | -11.9697 | -55.4991 | 2025-07-31 02:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| a25660e7-637a-3c6d-9bd9-a618cc8cad8e | -11.9694 | -55.5194 | 2025-07-31 02:00:00 | GOES-19 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 077f2f13-adc9-3ee2-9c29-5807a04ace25 | -6.526 | -56.1923 | 2025-07-31 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| a4513f18-e87e-3ac6-b20c-2f9fa152b8ff | -6.6725 | -56.4029 | 2025-07-31 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 1d75bc7d-a90e-3f37-9c4f-f4368542c73a | -6.5075 | -56.1932 | 2025-07-31 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 365b07cb-0eb5-304a-a051-2aeaa417b389 | -6.5074 | -56.213 | 2025-07-31 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 974dc4ad-fe38-3f33-96df-672dbdd54714 | -11.7508 | -48.1825 | 2025-07-31 02:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 403af41a-3d95-31b9-a0c3-f43c85990ca1 | -6.5258 | -56.2121 | 2025-07-31 02:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| be3e4b2a-b1d3-31da-ac25-dc6fb2b54ded | -10.0843 | -53.8712 | 2025-07-31 02:10:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 53.5 |
| ecc9ba9f-58a3-30da-b166-61676c0d8460 | -6.526 | -56.1923 | 2025-07-31 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.3 |
| 1babf2d3-77b9-3d58-bc96-8b4225a5edff | -10.234 | -47.9908 | 2025-07-31 02:20:00 | GOES-19 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 14b19fa2-6deb-3248-b97a-578381b0335c | -11.7508 | -48.1825 | 2025-07-31 02:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 66.5 |
| d97357ba-3cdc-35b5-bd5b-db754938265e | -6.5074 | -56.213 | 2025-07-31 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 6f99c51b-7c7a-30e2-a487-bc9abebf62f4 | -6.5075 | -56.1932 | 2025-07-31 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 08177648-3f0c-35dd-a1ca-b8aff032ebaa | -10.0843 | -53.8712 | 2025-07-31 02:20:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 63.9 |
| 8003ec96-3e5d-367f-8f29-0d9d166cbfb1 | -6.6725 | -56.4029 | 2025-07-31 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 101.3 |
| 15750a0b-885d-3287-ab12-b70a829886ce | -6.6143 | -59.9848 | 2025-07-31 02:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 42.5 |
| a0404808-7c79-306f-bb67-34703285f9d1 | -6.5258 | -56.2121 | 2025-07-31 02:20:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.6 |
| 3673c999-b54b-3902-95d1-60e23ec45748 | -6.6726 | -56.3831 | 2025-07-31 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 35113792-696e-326e-b43a-d8d8c896c597 | -6.5258 | -56.2121 | 2025-07-31 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 3006eabb-d8cb-3737-81a3-bb611b5cd2ad | -6.5074 | -56.213 | 2025-07-31 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 511b98e0-d0dc-3fe3-b94d-6baa52d2b620 | -9.4387 | -40.3419 | 2025-07-31 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 185.8 |
| 0df76fe8-6b1a-3187-9107-d24293ee87c6 | -9.4383 | -40.3668 | 2025-07-31 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 140.2 |
| 9964871b-d7a4-3f31-9451-773b8bb4103a | -6.5075 | -56.1932 | 2025-07-31 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 70.6 |
| abb32e77-26d1-3ef6-933d-c29a85f911af | -6.6725 | -56.4029 | 2025-07-31 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| 18d692c5-2e12-3a83-b366-730c77818a67 | -9.4196 | -40.3447 | 2025-07-31 02:30:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 76.9 |
| fc654713-60ce-3694-b027-ca5e393c827d | -6.526 | -56.1923 | 2025-07-31 02:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| bf598aff-1cc3-3ef4-9d7c-1864606d692b | -11.7508 | -48.1825 | 2025-07-31 02:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 90bd909b-69b2-354e-a2fc-f81a03422f78 | -12.7576 | -44.402 | 2025-07-31 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 7fc74edd-fdc5-3998-acec-ae56e8bb5d7a | -6.5075 | -56.1932 | 2025-07-31 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 61873e4c-8473-3956-a691-463201c23744 | -6.6725 | -56.4029 | 2025-07-31 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 87.9 |
| d188239a-3779-35e5-9709-9c331363229e | -6.526 | -56.1923 | 2025-07-31 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| dcadd127-a066-34d5-8254-86cb349ee80c | -6.5074 | -56.213 | 2025-07-31 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| cd193eac-385d-39fd-aee0-ed758201fef5 | -6.5258 | -56.2121 | 2025-07-31 02:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 73bc3ae6-d7aa-360d-8138-192975adffdb | -6.6143 | -59.9848 | 2025-07-31 02:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 35.6 |
| 5b46fa74-642b-3115-8908-9ad7ed79248f | -6.5258 | -56.2121 | 2025-07-31 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 2a048b3b-9515-38ef-8810-4bee00c0cab3 | -6.6725 | -56.4029 | 2025-07-31 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 86.0 |
| d6baf27a-113c-3e55-b2c0-45fcc864ef8a | -6.526 | -56.1923 | 2025-07-31 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| 58c77bc3-b4e6-3ff9-a6a6-0ed0b717839d | -6.5074 | -56.213 | 2025-07-31 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 86d75169-7487-3d63-8cf8-59d0e057d370 | -6.5075 | -56.1932 | 2025-07-31 02:50:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| 65e36255-a7a2-36e1-9dda-918ed8e2d705 | -6.6725 | -56.4029 | 2025-07-31 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 43596fd9-cbc7-3866-a9b6-6f67aaeb0f37 | -6.5258 | -56.2121 | 2025-07-31 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 32a5230d-dd8d-3355-953e-c4a39ca5ee3a | -6.526 | -56.1923 | 2025-07-31 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| e17681df-92e0-39a1-8b03-6912057e2ccf | -6.5075 | -56.1932 | 2025-07-31 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| 5e3a4efc-ac22-3dfe-80f9-6cabf3e8e88d | -6.5074 | -56.213 | 2025-07-31 03:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 9051fe03-7b1a-3d58-8760-40161169d01f | -9.3989 | -45.4928 | 2025-07-31 03:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 7a7582e0-1e4a-3015-8afc-e87b21ce11e4 | -6.6725 | -56.4029 | 2025-07-31 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 8301bd5d-5a63-36d9-87fe-8dedff126685 | -6.5075 | -56.1932 | 2025-07-31 03:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |


[Clique aqui para ver as próximas entradas](README6.md)
