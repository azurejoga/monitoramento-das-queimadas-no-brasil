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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 798b6b64-dd80-320c-b708-7bbdaf7c9779 | -3.5059 | -53.82774 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| d2900e47-cfde-3382-840b-95d554a6d082 | -0.914 | -51.64102 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8ddf2e1c-e45a-3106-ae7a-3de5c729498c | -2.81674 | -53.05528 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 88.1 |
| 94f16fa4-e295-3939-be0b-b483fa7656c4 | -2.8987 | -54.16322 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| bb8d39a4-867b-3586-a420-f0e561122e35 | -2.46518 | -53.96705 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8d44a4d2-e0d2-3b78-a599-a7354f69d029 | -2.63667 | -54.20024 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 31a4046f-1e9e-3e58-8b78-055bc5ee9ea7 | -3.11098 | -54.04009 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| cca5d12a-853f-3b32-9566-7d98008a7eb7 | -3.37317 | -53.21296 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 27.1 |
| ccead120-1e7f-336a-a47d-144c5e502a5b | -3.02369 | -53.41364 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 34472fd4-936c-3ca3-9f82-1ae0d84b8559 | -2.89866 | -55.23153 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| a33cb64d-1ded-317f-8ef7-a730426f297f | -3.26376 | -53.6198 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 50.0 |
| 7994ff46-1c80-3f6e-8840-18907e16e390 | -1.90556 | -52.85977 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 38395eff-2a89-387e-bb46-f795c6c75dbc | -1.73693 | -52.641 | 2024-12-02 01:13:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7a1b846b-4ee4-36f8-9264-2725df3f74ee | 0.90695 | -59.44521 | 2024-12-02 01:13:00 | TERRA_M-M | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 46f9d6bc-39cd-38be-add3-5c3123361474 | -3.07023 | -53.81216 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| b118fe31-d7d6-35e5-b9dc-7b63f4fb9a4e | -2.92039 | -54.12415 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5ed557ed-f21d-3fc5-8bf2-fa69c9f21685 | -2.87421 | -53.98679 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 07cc8ac9-7c8e-3041-94c6-ddb995748e06 | -0.81867 | -51.6172 | 2024-12-02 01:13:00 | TERRA_M-M | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 38cd5861-f6fa-343b-b2a6-940127bfeefc | -3.75835 | -54.65769 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 22.3 |
| dd9b856b-6f38-32f8-999e-4f66e9022942 | -2.80655 | -53.04756 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| 74a7f627-fa2c-333f-bb81-3ccad64ea89c | -2.02416 | -54.30247 | 2024-12-02 01:13:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 274b7110-1e96-3889-893a-18fc010d55fe | -2.89738 | -55.22229 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 209f29a9-b6d8-38a2-8e6e-9dd3db3f7798 | -3.41312 | -53.22828 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 0f10e321-c7a9-32ca-95ca-a715796f389d | -2.81799 | -53.06427 | 2024-12-02 01:13:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 6b51c0a4-059d-3830-bde5-f11c8a6d84cd | -3.25614 | -53.62988 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.5 |
| b0c36a67-f032-3d65-b335-a896b4f55a45 | -2.83487 | -54.1061 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 6dfc284a-2f99-352c-b52e-3b72bdd2cef8 | -3.29105 | -53.67254 | 2024-12-02 01:13:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 6c7294f2-b72f-3927-a41c-54b5e2e32a96 | -3.7473 | -54.51224 | 2024-12-02 01:13:00 | TERRA_M-M | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.2 |
| dfe79864-6e36-3564-854c-b451cc06afad | -2.70388 | -54.16379 | 2024-12-02 01:13:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5301e91c-805a-3361-9694-dfbfbbee36dc | -2.63827 | -53.35695 | 2024-12-02 01:13:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 74.6 |
| fdc5d096-2dcb-30e3-932d-3a73e064a786 | 3.3894 | -60.5343 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 7d2c7ad0-5d03-3f95-9274-030bdfa2e36e | 3.38041 | -60.54392 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 1a6d4776-649b-3035-95c1-5ece9cdc8543 | 3.37762 | -60.53257 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 4089eafb-b8fc-351d-abec-b49ddb22c6a0 | 3.37332 | -60.50956 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 24.8 |
| 79fd2885-6c79-3dca-9eca-5ce3776a35c1 | 2.42239 | -60.65257 | 2024-12-02 01:15:00 | TERRA_M-M | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| acdacf07-1175-30ff-a9c6-69d9481adc3d | 3.38254 | -60.50009 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 7166c77e-1003-3930-8423-727b8b968abc | 3.38971 | -60.47888 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 649af2d4-aa7b-3c7d-92ca-807e39ca15c1 | 3.38507 | -60.5113 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 26.1 |
| b2141e8b-028d-3f31-a25e-c395e376b303 | 3.38742 | -60.4678 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| fc3f2d93-10cd-3d1d-ab46-203193980cc1 | 3.37799 | -60.47715 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 34.9 |
| b5467fed-9309-3b76-b215-3e5ba9b5f80b | 3.37566 | -60.49333 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 73800b27-4af9-3fc7-9bef-9faf1db7b3f3 | 3.38008 | -60.51631 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 2df22b79-9afe-3dfe-94f9-bf1825c28129 | 3.39202 | -60.46274 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 28.6 |
| 61e59d25-36e0-3919-9c29-ca43c176929b | 3.38739 | -60.49507 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 68.9 |
| 0b609653-818e-3f16-a7bb-4f1ac81a87cb | 3.38274 | -60.52759 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 2ee2617a-af3a-37c4-8f98-d07d67efd591 | 3.39184 | -60.51803 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| a7490330-f23c-33e3-ba3e-73dcef269689 | 3.38498 | -60.48392 | 2024-12-02 01:15:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 101.7 |
| 42e8b493-618f-3fe4-8301-e17a5b2a5706 | -2.5612 | -53.4133 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 120.2 |
| 0dbf77e5-6144-3c96-9df2-4b9cdff24af9 | -20.7421 | -54.4306 | 2024-12-02 01:20:00 | GOES-16 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 76.9 |
| d7cc90fc-9eef-319a-b314-6170542e6cd2 | -4.5932 | -43.3471 | 2024-12-02 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 38.0 |
| 49d83f5c-81e7-39e1-b806-06782ea85a63 | -12.4358 | -63.7455 | 2024-12-02 01:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 161.0 |
| 6178fb5d-7bb0-384b-b800-8c06cd72157f | -2.5428 | -53.4137 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 384f5f1a-09d1-3bdf-855f-4d05114b603b | -1.0735 | -53.4562 | 2024-12-02 01:20:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 46.6 |
| d876f045-a9fa-3acd-a239-e0153c52247f | -3.7084 | -51.8301 | 2024-12-02 01:20:00 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 17dc758b-3e42-35ee-96f0-9efb083f50b2 | -12.4359 | -63.7264 | 2024-12-02 01:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 183.1 |
| 7ef50feb-4a3a-3642-908d-e85cc4123663 | -5.5882 | -45.1412 | 2024-12-02 01:20:00 | GOES-16 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| b78b8d8e-fb1b-3621-a819-3d3d7c2b1cca | -3.2774 | -53.6383 | 2024-12-02 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.1 |
| c9bf0ba4-17ec-3605-8fc8-28afebd4ca2a | -2.8013 | -53.043 | 2024-12-02 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 622ea0be-afff-391e-89c7-e356f5eda881 | -12.4169 | -63.7465 | 2024-12-02 01:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 94.0 |
| 8d23e132-c0e3-3342-a8aa-dd89e0645dea | -3.4017 | -50.2381 | 2024-12-02 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 673100dc-c749-3c89-a9cd-347f96af840d | -2.5796 | -53.3927 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 48.0 |
| 44ef6c8d-7492-39dc-a1ad-f13c2f7701b0 | -2.8197 | -53.0425 | 2024-12-02 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 65.4 |
| d5a52399-34d5-37e4-b8c8-7cda3fdbe511 | 3.3841 | -60.5135 | 2024-12-02 01:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.2 |
| 9dd6e62d-5fd9-362e-a7a7-a9b452c17c51 | -4.267 | -50.8551 | 2024-12-02 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 92a71d12-782a-3c3f-b7b6-33c190b924cc | -2.2666 | -53.6212 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| a1525cc4-3643-3b03-9875-ef137a3ec9f9 | -4.9272 | -41.3358 | 2024-12-02 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 121.4 |
| 513c6d48-f68b-3b01-a215-9ca558c225ac | -6.0862 | -48.0339 | 2024-12-02 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 94.9 |
| 10d11ec8-c250-3bd4-b8da-10e8e5233cd7 | -4.9085 | -41.3371 | 2024-12-02 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 216.1 |
| 1f1f2b95-96ef-3c02-b009-bad30ace0946 | -2.6076 | -45.2469 | 2024-12-02 01:20:00 | GOES-16 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 146.1 |
| 69461b97-b1f4-359a-b4db-573d3fb32da3 | -2.6075 | -45.2695 | 2024-12-02 01:20:00 | GOES-16 | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 74.4 |
| eeec4af5-e853-38d3-90d4-96e709f2fb94 | -12.2493 | -63.4688 | 2024-12-02 01:20:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| 2511a8f5-d2a1-358a-b488-29332575ef7c | -3.4201 | -50.2375 | 2024-12-02 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 98a67e63-73ba-3c89-928f-a20e30c5d085 | -3.259 | -53.6388 | 2024-12-02 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 76.4 |
| d963913e-9b49-32a2-a57c-710496dd5e74 | -2.5612 | -53.3931 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 118.6 |
| d73a7b26-5f97-36bf-a167-af31613ffd3e | -12.4171 | -63.7274 | 2024-12-02 01:20:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 99.4 |
| 63ef4a25-13b4-30fd-bdf4-ca20c1fd4a08 | -2.8196 | -53.0629 | 2024-12-02 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 94a03d31-51b9-3b76-afa7-4908b704bf71 | 3.384 | -60.5325 | 2024-12-02 01:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 062c10fb-80c3-3f8b-a8ec-3b2cabb332df | -3.2775 | -53.6181 | 2024-12-02 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| fd213e58-445d-34d2-aa41-fd832f9ffec6 | -2.6348 | -53.3712 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 79.1 |
| 627f6d8e-38b1-3d37-bce3-6045bd56f031 | -2.5428 | -53.3935 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 46.8 |
| 025757e3-82ef-34bb-85ab-58497464b464 | -6.086 | -48.0557 | 2024-12-02 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 263.9 |
| 4ac4fad0-f737-3de6-8c95-735d377f05c6 | -2.8012 | -53.0633 | 2024-12-02 01:20:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| e74dadc3-9ae9-33ec-9153-807ea18fcea3 | -4.9087 | -41.313 | 2024-12-02 01:20:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 78.5 |
| f35594a3-c20b-307e-84ff-59090613b0ae | -2.6349 | -53.351 | 2024-12-02 01:20:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 2af3fc7e-8ab0-3ad6-bc55-bbeed1412421 | -4.5745 | -43.3483 | 2024-12-02 01:20:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 3be9cf74-003f-36f6-a0f2-2a0851d1cec9 | -6.0674 | -48.0569 | 2024-12-02 01:20:00 | GOES-16 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| 81a7fa9a-004f-3a34-910a-bdaae552aeb3 | -3.4017 | -50.2171 | 2024-12-02 01:20:00 | GOES-16 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 5a0a5525-9604-38c5-9b7b-ec9b8728e397 | 3.3841 | -60.4946 | 2024-12-02 01:20:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 0552f952-599f-3565-be3a-a81e002ec12f | -3.2591 | -53.6186 | 2024-12-02 01:20:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 90.4 |
| b4275658-4538-3baa-a57f-e04341d27a6e | -2.8197 | -53.0425 | 2024-12-02 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 75.1 |
| 1cc66ed3-d788-3474-abc0-809d7a1f02a7 | -2.0263 | -54.3088 | 2024-12-02 01:30:00 | GOES-16 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 90.3 |
| e15c0a67-fb53-3f52-9363-0cab5c972368 | -12.4169 | -63.7465 | 2024-12-02 01:30:00 | GOES-16 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 06132e1f-bb58-3920-8ba0-26630bdf81c5 | -2.8012 | -53.0633 | 2024-12-02 01:30:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 18706ea9-949b-3c6f-ba14-8332da240dde | -2.5428 | -53.4137 | 2024-12-02 01:30:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 84.4 |
| 35f285d2-eb98-3a9a-8021-8a42464eb772 | -4.9272 | -41.3358 | 2024-12-02 01:30:00 | GOES-16 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 83.5 |
| eb8fdd33-323f-3f92-a01c-799f4f7deaa7 | -3.2591 | -53.6186 | 2024-12-02 01:30:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 100.9 |
| cd47f544-7572-3185-a217-cff609cb15e0 | -1.0735 | -53.4562 | 2024-12-02 01:30:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| fdcc59a6-1f2a-3bad-bea7-8bd1ee046e3b | 3.384 | -60.5325 | 2024-12-02 01:30:00 | GOES-16 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| c9e00c6f-0831-33f9-904a-c0b03ac20872 | -12.2493 | -63.4688 | 2024-12-02 01:30:00 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 40.5 |
| 54063746-0cc2-3915-9397-063050fd0e21 | -4.5743 | -43.3716 | 2024-12-02 01:30:00 | GOES-16 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 31.8 |


[Clique aqui para ver as próximas entradas](README17.md)
