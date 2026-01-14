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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8b4131a2-0269-3cfc-be8c-f3c5e812cf1f | -12.8662 | -52.4983 | 2026-01-14 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d6ba98db-f4b6-35b1-b5d8-3f9bd015d89d | -7.2599 | -43.041 | 2026-01-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 93.8 |
| 71d0ce2c-7baa-31d3-8bb7-124fb8d734e4 | -12.8659 | -52.5194 | 2026-01-14 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 136.1 |
| a8bc25dc-f673-37a4-b892-10a46fb1e922 | 4.0761 | -61.4469 | 2026-01-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 38.3 |
| f86d5c2b-88b7-36a6-9255-a66d948181d6 | -6.5591 | -35.2442 | 2026-01-14 00:00:00 | GOES-19 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 63.4 |
| 7ff8b643-f8e4-368d-b9a7-07afe1111edd | -12.8468 | -52.5216 | 2026-01-14 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 268.1 |
| a36f5cec-3ab4-3a13-822f-d2a8cb4e1d10 | 4.0578 | -61.4473 | 2026-01-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.5 |
| ccc9c7ec-95db-3439-8942-2647e0a4b75f | 4.0578 | -61.4661 | 2026-01-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 85.6 |
| 02532151-5016-30b5-bf56-c0b53c7b350f | -7.2597 | -43.0645 | 2026-01-14 00:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 95.6 |
| 4e3cf698-baa9-376a-aad4-e667f2406bef | -12.8276 | -52.5238 | 2026-01-14 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| 836110dd-32c5-3816-8e44-803fd4627b1b | 4.076 | -61.4658 | 2026-01-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 36.6 |
| baeea216-e5b9-394d-bb97-491bb7ad8196 | -6.5595 | -35.2168 | 2026-01-14 00:00:00 | GOES-19 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 89.3 |
| 07952178-4a3c-3806-997f-d9ffdd8d41df | 4.0395 | -61.4665 | 2026-01-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 8d0818d1-5b9f-3de9-987e-9677921a75b8 | -12.8471 | -52.5005 | 2026-01-14 00:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 107.7 |
| 7906016a-b8ba-3d31-9e94-7c9576bf84b5 | 4.0395 | -61.4476 | 2026-01-14 00:00:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 42.6 |
| a9e4719a-ce8c-30d3-addf-2872a359807b | -12.8471 | -52.5005 | 2026-01-14 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 126.7 |
| 941764e5-8f51-3b0e-b3c1-55b168b10317 | 4.0395 | -61.4665 | 2026-01-14 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 21ad7045-fa52-319a-88f6-ff2e68c65501 | -12.8276 | -52.5238 | 2026-01-14 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 7e787608-467e-3f14-98fb-143a235866c4 | -12.8659 | -52.5194 | 2026-01-14 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 118.6 |
| f8d1becd-5923-3021-af47-4e463708d48a | -12.8468 | -52.5216 | 2026-01-14 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 247.8 |
| 3a1e9279-2ca7-3cb8-9c63-a209f6acbdf6 | 4.0578 | -61.4473 | 2026-01-14 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 65.6 |
| e0a90363-f7ad-3763-8a07-a9736c2c9a91 | 4.076 | -61.4658 | 2026-01-14 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 33.6 |
| d10f4049-4c75-383a-bec7-d4a9425f2f32 | -16.0937 | -56.7651 | 2026-01-14 00:10:00 | GOES-19 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 02b2203c-709c-3527-a1b4-166c3b2fe8d1 | -12.8662 | -52.4983 | 2026-01-14 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 76.7 |
| 84741788-527a-3108-a060-be3207c1ab9a | 4.0578 | -61.4661 | 2026-01-14 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 75.7 |
| e64bdaed-e84c-3b2d-a349-571634633cbd | -12.8464 | -52.5426 | 2026-01-14 00:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 81.1 |
| e723b1d3-d0ca-372d-a573-fe1b6799fd10 | -7.2599 | -43.041 | 2026-01-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 88.7 |
| 900974ee-f46d-332c-914f-842a74b93b5d | -7.2597 | -43.0645 | 2026-01-14 00:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.7 |
| 78100e3b-be02-3efe-82a5-6f827608c209 | 4.0395 | -61.4476 | 2026-01-14 00:10:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 35.4 |
| 0562f6c1-7263-3205-ae1c-245cd714c105 | -7.3256 | -34.9808 | 2026-01-14 00:20:00 | GOES-19 | ALHANDRA | PARAÍBA | Brasil | 2500601 | 25 | 33 | nan | nan | nan | Mata Atlântica | 43.6 |
| 4f931492-765c-3a4f-b923-49722018a1e1 | -12.8659 | -52.5194 | 2026-01-14 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 112.6 |
| 4830e6ef-d1a5-3713-8ca0-77b847a3c286 | -12.8276 | -52.5238 | 2026-01-14 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| fb835c25-d24a-3588-b518-88a7ef0b2dea | -12.8468 | -52.5216 | 2026-01-14 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 243.6 |
| b4265849-5a8d-3692-a05b-919c1c4ad450 | -7.2597 | -43.0645 | 2026-01-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.9 |
| da3333fd-b723-381a-a124-ca1c2cfd0b64 | -12.8471 | -52.5005 | 2026-01-14 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 118.2 |
| e2d0d9c4-dc27-38e3-8690-362461ee6372 | -12.8464 | -52.5426 | 2026-01-14 00:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| d69ce545-9167-3544-b03d-abee001fa2fb | -7.2599 | -43.041 | 2026-01-14 00:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 90.1 |
| 46d5283c-0ddb-3483-b35f-2f4ff64fad6f | -7.2599 | -43.041 | 2026-01-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.3 |
| efc645bf-1c0e-3221-b895-eee0d156ab83 | -12.8276 | -52.5238 | 2026-01-14 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 61d0bd6f-9c8d-3eba-b987-fc110588b7bd | -7.2597 | -43.0645 | 2026-01-14 00:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.5 |
| 4895dad2-f608-3cc3-9c73-8032fba8be48 | -12.8468 | -52.5216 | 2026-01-14 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 235.0 |
| 71d4c188-4a71-364a-a5d5-759d138434e8 | -12.8659 | -52.5194 | 2026-01-14 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 115.6 |
| 0a149d36-1280-3c10-a7f0-18876814fdb6 | -12.8464 | -52.5426 | 2026-01-14 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 81.8 |
| d025f7a1-e35a-39bc-93ca-1472fa5eee81 | -12.8471 | -52.5005 | 2026-01-14 00:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 106.2 |
| acb1e051-b329-3417-a829-41258f8a8851 | -17.756001 | -40.165401 | 2026-01-14 00:36:00 | METOP-B | IBIRAPUÃ | BAHIA | Brasil | 2912806 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 43d2cbb9-1dcb-3576-b06c-a1eca1e28c8e | -1.9769 | -54.218399 | 2026-01-14 00:36:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49edaf03-447b-3c6f-85b2-b6e447422d36 | -12.8471 | -52.5005 | 2026-01-14 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 114.5 |
| ea7e4a93-8dd0-3bf4-92ea-5ec2047c2254 | -10.1028 | -36.3372 | 2026-01-14 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 49.6 |
| e25f4064-30a6-3410-81c4-acf72390b588 | -12.8468 | -52.5216 | 2026-01-14 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 237.5 |
| aa7362c9-f401-3e5c-9ec5-fefb323f6b0e | -12.8276 | -52.5238 | 2026-01-14 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| 127dad14-56b7-364f-aa92-45d830e71499 | -7.2597 | -43.0645 | 2026-01-14 00:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| b1101559-0277-3c17-9fbc-5f0dd03349c1 | -10.1221 | -36.3337 | 2026-01-14 00:40:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 47.2 |
| 8063fd6e-701b-3413-b5c9-e87487ef008e | -12.8659 | -52.5194 | 2026-01-14 00:40:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 104.0 |
| 7799bccf-1606-3a81-b7f3-cc1e8dc42656 | -12.8659 | -52.5194 | 2026-01-14 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 105.4 |
| ca7544f5-d28e-3d3b-83a6-978d64c03959 | -12.8471 | -52.5005 | 2026-01-14 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 0da532ac-996f-3c87-b3f1-0a592e2fd263 | -12.8276 | -52.5238 | 2026-01-14 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 89.1 |
| 78919b19-0400-333c-b9ed-85f71c5ddd61 | -12.8468 | -52.5216 | 2026-01-14 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 214.1 |
| f7c96d45-39ca-3e57-af4f-575dc636865a | -12.8464 | -52.5426 | 2026-01-14 00:50:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 77.4 |
| 411897de-8146-37e9-b212-f1206e9542a9 | -12.8659 | -52.5194 | 2026-01-14 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 84.4 |
| d131d3d3-a706-3d06-96d0-e0247d4239c6 | -5.1178 | -43.2431 | 2026-01-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 97.8 |
| c6fc0877-1112-3405-9f84-cd2e9b695ad7 | -5.118 | -43.2198 | 2026-01-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 61eba0e9-2deb-3bcd-a1e0-18766fef8999 | -12.8471 | -52.5005 | 2026-01-14 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 3b83111d-d9c4-32cc-b06b-b12bbf6007d1 | -12.8468 | -52.5216 | 2026-01-14 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 256.3 |
| 024d653d-99bb-3db8-9d57-096038221268 | -5.099 | -43.2444 | 2026-01-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 35f1819b-0099-3e25-965f-58b1900e31bf | -5.0992 | -43.2211 | 2026-01-14 01:00:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 82.5 |
| 9b2b43ba-f15e-302b-a2b7-d10247322066 | -12.8276 | -52.5238 | 2026-01-14 01:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 3c18113e-26c2-3a4b-85e1-d25cb6aa925f | -17.8844 | -54.8664 | 2026-01-14 01:06:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 04e13728-4406-3a4b-8bc6-50d2154f1711 | -17.88621 | -54.87803 | 2026-01-14 01:06:00 | TERRA_M-M | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6776dd9c-ab6f-3751-9d67-8b69f32ad9c2 | -16.59897 | -58.2179 | 2026-01-14 01:06:00 | TERRA_M-M | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 12373a5c-c3be-3b62-bd8d-4096663083b9 | -9.11331 | -61.48578 | 2026-01-14 01:09:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ed652d70-7acf-31cd-b7c1-6a198e8828a8 | -12.83885 | -52.52398 | 2026-01-14 01:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 147.3 |
| 7e09d9ca-2def-34c0-ac7f-906569c88875 | -12.8398 | -52.53872 | 2026-01-14 01:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 33.0 |
| 38449a48-201d-3d9b-9b83-fb820d6a019d | -12.83624 | -52.51784 | 2026-01-14 01:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 65.8 |
| d3a4aa89-a248-3651-8361-93331d516048 | -12.8528 | -52.53639 | 2026-01-14 01:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 67.9 |
| 19b946f0-e4f5-3c76-99b6-12db290fe7d4 | -12.84928 | -52.51561 | 2026-01-14 01:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 264.2 |
| 53863a9c-7055-3966-93fe-e36da1fcc664 | -12.85187 | -52.52165 | 2026-01-14 01:09:00 | TERRA_M-M | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 181.1 |
| 2a133d88-3d7c-3e2f-8fdc-e86708da639d | -12.8659 | -52.5194 | 2026-01-14 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6788dcb2-0420-3a5e-9b41-dd2517afa23f | -12.8471 | -52.5005 | 2026-01-14 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 103.3 |
| 1357fe6f-9488-33cd-aeb3-54d7786169ae | -5.0992 | -43.2211 | 2026-01-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 100.1 |
| db3b6ef0-8ce6-3cfe-92bd-c0618126cb7c | -12.8464 | -52.5426 | 2026-01-14 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 9630e48d-05d0-31c7-837d-d7863f6819e3 | -12.8276 | -52.5238 | 2026-01-14 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 80.9 |
| 59d70f85-d220-311f-ac4d-3d3e409416b7 | -5.118 | -43.2198 | 2026-01-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| fa040a92-b02b-3989-9de0-af693f25f753 | -5.1178 | -43.2431 | 2026-01-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 88.2 |
| fbff636c-d62d-3ca8-98c8-cab8d0a180fc | -12.8468 | -52.5216 | 2026-01-14 01:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 267.0 |
| e5e428fb-4fd9-3fc7-9152-83c8c8a2c3ab | -5.099 | -43.2444 | 2026-01-14 01:10:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 7c8dffa5-07ec-31e4-a5d2-a046ad7d4ca6 | -1.938 | -53.466599 | 2026-01-14 01:15:00 | METOP-C | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bc93fc8-3f23-30eb-8d82-a648b66dc317 | -5.099 | -43.2444 | 2026-01-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 145.8 |
| f35e0098-f8a9-3e1a-8e8d-ed81a54b3983 | -5.118 | -43.2198 | 2026-01-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| baa41839-551b-3f48-845f-05147ecab783 | -12.8471 | -52.5005 | 2026-01-14 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 92.4 |
| c7efeaa1-de88-3158-a7ec-0da3af0d5299 | -9.3197 | -36.0412 | 2026-01-14 01:20:00 | GOES-19 | MURICI | ALAGOAS | Brasil | 2705507 | 27 | 33 | nan | nan | nan | Mata Atlântica | 61.1 |
| 8998903c-5740-352c-bfcc-dc998bb0ffd2 | -12.8659 | -52.5194 | 2026-01-14 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 122.3 |
| 11b28d7b-78b7-3e5d-8b3c-fadb51c5e400 | -5.1178 | -43.2431 | 2026-01-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 44ed8af2-14ce-3fd2-a492-f2c2c1441d65 | -12.8468 | -52.5216 | 2026-01-14 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 234.0 |
| 4611bab7-ca59-3b3a-8f11-904cc12709d4 | -5.0992 | -43.2211 | 2026-01-14 01:20:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 117.1 |
| 36e14714-3258-3912-b7c7-676b2ddc50c8 | -12.8276 | -52.5238 | 2026-01-14 01:20:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 94.4 |
| dc5e2607-235b-3a3a-a580-fd3c74b2ed65 | -12.8468 | -52.5216 | 2026-01-14 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 193.1 |
| 2fa1b755-ac76-3d62-a4e5-f91205a16e97 | -12.8464 | -52.5426 | 2026-01-14 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 96da1ebe-5155-365f-9e8c-34ee9d90e7fc | -12.8471 | -52.5005 | 2026-01-14 01:30:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 101.5 |
| a7b9a0e0-16f9-30b4-89b9-3c80622515a0 | -10.4923 | -37.1221 | 2026-01-14 01:30:00 | GOES-19 | SIRIRI | SERGIPE | Brasil | 2807204 | 28 | 33 | nan | nan | nan | Mata Atlântica | 66.6 |
| 76fe6c6d-ad25-3423-a1ea-49ed495b67b7 | -5.099 | -43.2444 | 2026-01-14 01:30:00 | GOES-19 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 159.5 |


[Clique aqui para ver as próximas entradas](README2.md)
